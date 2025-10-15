def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 6, 3, 4, 5, 6]),val = 6), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 6, 3, 4, 5, 6]),val = 6), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50]),val = 10), list_node([20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50]),val = 10), list_node([20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 20, 30, 20, 10]),val = 20), list_node([50, 30, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 20, 30, 20, 10]),val = 20), list_node([50, 30, 10])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1]),val = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1]),val = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 40, 30, 20, 10]),val = 50), list_node([40, 30, 20, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 40, 30, 20, 10]),val = 50), list_node([40, 30, 20, 10])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([7, 7, 7, 7]),val = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([7, 7, 7, 7]),val = 7) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 2, 3, 5, 4, 5]),val = 5), list_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 2, 3, 5, 4, 5]),val = 5), list_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 5, 2, 5, 3, 5]),val = 5), list_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 5, 2, 5, 3, 5]),val = 5), list_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),val = 3), list_node([1, 2, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),val = 3), list_node([1, 2, 4, 5])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([]),val = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([]),val = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 3]),val = 1), list_node([2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 3]),val = 1), list_node([2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),val = 6), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),val = 6), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]),val = 35), list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 34, 33, 32, 31]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]),val = 35), list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 34, 33, 32, 31])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([42, 42, 42, 42, 42, 42]),val = 42) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([42, 42, 42, 42, 42, 42]),val = 42) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),val = 20), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),val = 20), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]),val = 2), list_node([1, 1, 1, 1, 3, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]),val = 2), list_node([1, 1, 1, 1, 3, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 2, 4, 2, 5, 2, 6]),val = 2), list_node([1, 3, 4, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 2, 4, 2, 5, 2, 6]),val = 2), list_node([1, 3, 4, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 1, 3, 3, 3, 2, 2, 1]),val = 2), list_node([1, 1, 3, 3, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 1, 3, 3, 3, 2, 2, 1]),val = 2), list_node([1, 1, 3, 3, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50]),val = 50), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50]),val = 50), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 10, 20, 30]),val = 20), list_node([10, 30, 40, 50, 10, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 10, 20, 30]),val = 20), list_node([10, 30, 40, 50, 10, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),val = 5), list_node([10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 15, 20, 25, 30, 35, 40, 45, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),val = 5), list_node([10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 15, 20, 25, 30, 35, 40, 45, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 8), list_node([10, 9, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 8), list_node([10, 9, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 11), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 11), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),val = 2), list_node([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),val = 2), list_node([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 20), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 20), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7]),val = 2), list_node([1, 3, 4, 5, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7]),val = 2), list_node([1, 3, 4, 5, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1, 2]),val = 2), list_node([1, 3, 1, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1, 2]),val = 2), list_node([1, 3, 1, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 5), list_node([1, 2, 3, 4, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 5), list_node([1, 2, 3, 4, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 9), list_node([10, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 9), list_node([10, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]),val = 10), list_node([20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]),val = 10), list_node([20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),val = 70), list_node([10, 20, 30, 40, 50, 60, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),val = 70), list_node([10, 20, 30, 40, 50, 60, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),val = 14), list_node([2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, 26, 28, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),val = 14), list_node([2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, 26, 28, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 1, 3, 1, 4, 1, 5]),val = 1), list_node([2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 1, 3, 1, 4, 1, 5]),val = 1), list_node([2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 1), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 1), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 7), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 7), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]),val = 22), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]),val = 22), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]),val = 3), list_node([1, 2, 4, 5, 6, 1, 2, 4, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]),val = 3), list_node([1, 2, 4, 5, 6, 1, 2, 4, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 5, 2, 3, 7, 3, 8, 3, 3]),val = 3), list_node([5, 2, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 5, 2, 3, 7, 3, 8, 3, 3]),val = 3), list_node([5, 2, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 2), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 2), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2]),val = 2), list_node([1, 3, 4, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2]),val = 2), list_node([1, 3, 4, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]),val = 10), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]),val = 10), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1, 4, 5, 6, 3, 7, 8, 9, 3]),val = 3), list_node([2, 1, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1, 4, 5, 6, 3, 7, 8, 9, 3]),val = 3), list_node([2, 1, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),val = 5), list_node([3, 1, 4, 1, 9, 2, 6, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),val = 5), list_node([3, 1, 4, 1, 9, 2, 6, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]),val = 3), list_node([2, 1, 2, 1, 2, 1, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]),val = 3), list_node([2, 1, 2, 1, 2, 1, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([15, 16, 15, 17, 15, 18, 15, 19, 15, 20]),val = 15), list_node([16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([15, 16, 15, 17, 15, 18, 15, 19, 15, 20]),val = 15), list_node([16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 25), list_node([30, 29, 28, 27, 26, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 25), list_node([30, 29, 28, 27, 26, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([34, 33, 32, 31, 30, 29, 28, 27, 26, 25]),val = 27), list_node([34, 33, 32, 31, 30, 29, 28, 26, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([34, 33, 32, 31, 30, 29, 28, 27, 26, 25]),val = 27), list_node([34, 33, 32, 31, 30, 29, 28, 26, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 2, 2, 1, 1, 1, 3, 3, 3]),val = 2), list_node([1, 1, 1, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 2, 2, 1, 1, 1, 3, 3, 3]),val = 2), list_node([1, 1, 1, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 19), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 19), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41]),val = 47), list_node([50, 49, 48, 46, 45, 44, 43, 42, 41]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41]),val = 47), list_node([50, 49, 48, 46, 45, 44, 43, 42, 41])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 1, 1]),val = 1), list_node([2, 2, 3, 3, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 1, 1]),val = 1), list_node([2, 2, 3, 3, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]),val = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]),val = 4) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 1), list_node([3, 5, 7, 9, 11, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 1), list_node([3, 5, 7, 9, 11, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]),val = 1), list_node([2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]),val = 1), list_node([2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]),val = 42) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]),val = 42) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]),val = 3), list_node([1, 2, 4, 2, 1, 2, 4, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]),val = 3), list_node([1, 2, 4, 2, 1, 2, 4, 2, 1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),val = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),val = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1]),val = 1), list_node([2, 3, 2, 3, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1]),val = 1), list_node([2, 3, 2, 3, 2, 3])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([42, 42, 42, 42, 42, 42, 42, 42, 42, 42]),val = 42) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([42, 42, 42, 42, 42, 42, 42, 42, 42, 42]),val = 42) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 18), list_node([2, 4, 6, 8, 10, 12, 14, 16, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 18), list_node([2, 4, 6, 8, 10, 12, 14, 16, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]),val = 19), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]),val = 19), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]),val = 31), list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]),val = 31), list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 10, 40, 10, 50]),val = 10), list_node([20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 10, 40, 10, 50]),val = 10), list_node([20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 16), list_node([2, 4, 6, 8, 10, 12, 14, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 16), list_node([2, 4, 6, 8, 10, 12, 14, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),val = 1), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),val = 1), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 7), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 7), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),val = 21), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),val = 21), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 2]),val = 2), list_node([3, 3, 3, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 2]),val = 2), list_node([3, 3, 3, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]),val = 2), list_node([1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]),val = 2), list_node([1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 4), list_node([1, 2, 2, 3, 3, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 4), list_node([1, 2, 2, 3, 3, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]),val = 2), list_node([1, 1, 1, 3, 3, 3, 4, 4, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]),val = 2), list_node([1, 1, 1, 3, 3, 3, 4, 4, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]),val = 1), list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]),val = 1), list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 2), list_node([1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 2), list_node([1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([42, 17, 22, 17, 35, 17, 5, 17]),val = 17), list_node([42, 22, 35, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([42, 17, 22, 17, 35, 17, 5, 17]),val = 17), list_node([42, 22, 35, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50]),val = 50), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50]),val = 50), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]),val = 25) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]),val = 25) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 6, 5, 4, 6, 7, 8, 6, 9]),val = 6), list_node([1, 3, 2, 5, 4, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 6, 5, 4, 6, 7, 8, 6, 9]),val = 6), list_node([1, 3, 2, 5, 4, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([5, 6, 7, 8, 9, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([5, 6, 7, 8, 9, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),val = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),val = 5) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 1), list_node([2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 1), list_node([2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 20), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 20), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5]),val = 1), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5]),val = 1), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 10]),val = 5), list_node([1, 2, 3, 4, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 10]),val = 5), list_node([1, 2, 3, 4, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 3), list_node([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 3), list_node([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),val = 26), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),val = 26), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),val = 3), list_node([1, 4, 1, 5, 9, 2, 6, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),val = 3), list_node([1, 4, 1, 5, 9, 2, 6, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]),val = 3), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]),val = 3), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9, 3]),val = 3), list_node([1, 2, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9, 3]),val = 3), list_node([1, 2, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 3, 2, 1]),val = 3), list_node([1, 2, 4, 2, 1, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 3, 2, 1]),val = 3), list_node([1, 2, 4, 2, 1, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 10, 30, 10, 40]),val = 10), list_node([20, 30, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 10, 30, 10, 40]),val = 10), list_node([20, 30, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41, 40])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),val = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),val = 5) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 20), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 20), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),val = 50), list_node([10, 20, 30, 40, 60, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),val = 50), list_node([10, 20, 30, 40, 60, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),val = 50), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),val = 50), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]),val = 3), list_node([1, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]),val = 3), list_node([1, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 40, 30, 20, 10]),val = 30), list_node([10, 20, 40, 50, 40, 20, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 40, 30, 20, 10]),val = 30), list_node([10, 20, 40, 50, 40, 20, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 3), list_node([10, 9, 8, 7, 6, 5, 4, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 3), list_node([10, 9, 8, 7, 6, 5, 4, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),val = 2), list_node([3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),val = 2), list_node([3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([49, 48, 47, 46, 45, 44, 43, 42, 41, 40]),val = 45), list_node([49, 48, 47, 46, 44, 43, 42, 41, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([49, 48, 47, 46, 45, 44, 43, 42, 41, 40]),val = 45), list_node([49, 48, 47, 46, 44, 43, 42, 41, 40])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1]),val = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1]),val = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]),val = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]),val = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([42, 23, 42, 23, 42, 23, 42, 23, 42]),val = 42), list_node([23, 23, 23, 23]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([42, 23, 42, 23, 42, 23, 42, 23, 42]),val = 42), list_node([23, 23, 23, 23])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]),val = 30), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 34, 36, 38, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]),val = 30), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 34, 36, 38, 40])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([1, 2, 6, 3, 4, 5, 6]),val = 6), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50]),val = 10), list_node([20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([50, 20, 30, 20, 10]),val = 20), list_node([50, 30, 10]))
    assert candidate(head = list_node([1, 1, 1, 1, 1]),val = 1) == None
    assert is_same_list(candidate(head = list_node([50, 40, 30, 20, 10]),val = 50), list_node([40, 30, 20, 10]))
    assert candidate(head = list_node([7, 7, 7, 7]),val = 7) == None
    assert is_same_list(candidate(head = list_node([5, 1, 2, 3, 5, 4, 5]),val = 5), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(head = list_node([5, 1, 5, 2, 5, 3, 5]),val = 5), list_node([1, 2, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),val = 3), list_node([1, 2, 4, 5]))
    assert candidate(head = list_node([]),val = 1) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 3]),val = 1), list_node([2, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),val = 6), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]),val = 35), list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 34, 33, 32, 31]))
    assert is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20]))
    assert candidate(head = list_node([42, 42, 42, 42, 42, 42]),val = 42) == None
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),val = 20), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]),val = 2), list_node([1, 1, 1, 1, 3, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 2, 4, 2, 5, 2, 6]),val = 2), list_node([1, 3, 4, 5, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 1, 3, 3, 3, 2, 2, 1]),val = 2), list_node([1, 1, 3, 3, 3, 1]))
    assert is_same_list(candidate(head = list_node([50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50]),val = 50), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 10, 20, 30]),val = 20), list_node([10, 30, 40, 50, 10, 30]))
    assert is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),val = 5), list_node([10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 15, 20, 25, 30, 35, 40, 45, 50]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 8), list_node([10, 9, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 11), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),val = 2), list_node([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 20), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7]),val = 2), list_node([1, 3, 4, 5, 6, 7]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1, 2]),val = 2), list_node([1, 3, 1, 3, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 5), list_node([1, 2, 3, 4, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 9), list_node([10, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]),val = 10), list_node([20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),val = 70), list_node([10, 20, 30, 40, 50, 60, 80, 90, 100]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),val = 14), list_node([2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, 26, 28, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 1, 3, 1, 4, 1, 5]),val = 1), list_node([2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 1), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 7), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]),val = 22), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]),val = 3), list_node([1, 2, 4, 5, 6, 1, 2, 4, 5, 6]))
    assert is_same_list(candidate(head = list_node([3, 5, 2, 3, 7, 3, 8, 3, 3]),val = 3), list_node([5, 2, 7, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 2), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2]),val = 2), list_node([1, 3, 4, 5, 6]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]),val = 10), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
    assert is_same_list(candidate(head = list_node([3, 2, 1, 4, 5, 6, 3, 7, 8, 9, 3]),val = 3), list_node([2, 1, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),val = 5), list_node([3, 1, 4, 1, 9, 2, 6, 3]))
    assert is_same_list(candidate(head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]),val = 3), list_node([2, 1, 2, 1, 2, 1, 2, 1]))
    assert is_same_list(candidate(head = list_node([15, 16, 15, 17, 15, 18, 15, 19, 15, 20]),val = 15), list_node([16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 25), list_node([30, 29, 28, 27, 26, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([34, 33, 32, 31, 30, 29, 28, 27, 26, 25]),val = 27), list_node([34, 33, 32, 31, 30, 29, 28, 26, 25]))
    assert is_same_list(candidate(head = list_node([2, 2, 2, 1, 1, 1, 3, 3, 3]),val = 2), list_node([1, 1, 1, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 19), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]))
    assert is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41]),val = 47), list_node([50, 49, 48, 46, 45, 44, 43, 42, 41]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 1, 1]),val = 1), list_node([2, 2, 3, 3, 2, 2, 2, 2]))
    assert candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]),val = 4) == None
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),val = 1), list_node([3, 5, 7, 9, 11, 13, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]),val = 1), list_node([2, 2, 2, 2, 2]))
    assert candidate(head = list_node([42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]),val = 42) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]),val = 3), list_node([1, 2, 4, 2, 1, 2, 4, 2, 1]))
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),val = 1) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1]),val = 1), list_node([2, 3, 2, 3, 2, 3]))
    assert candidate(head = list_node([42, 42, 42, 42, 42, 42, 42, 42, 42, 42]),val = 42) == None
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 18), list_node([2, 4, 6, 8, 10, 12, 14, 16, 20]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]),val = 19), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]))
    assert is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]),val = 31), list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 10, 40, 10, 50]),val = 10), list_node([20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 16), list_node([2, 4, 6, 8, 10, 12, 14, 18, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),val = 1), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 7), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),val = 21), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 2]),val = 2), list_node([3, 3, 3, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]),val = 2), list_node([1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 4), list_node([1, 2, 2, 3, 3, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]),val = 2), list_node([1, 1, 1, 3, 3, 3, 4, 4, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]),val = 1), list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 2), list_node([1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
    assert is_same_list(candidate(head = list_node([42, 17, 22, 17, 35, 17, 5, 17]),val = 17), list_node([42, 22, 35, 5]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50]),val = 50), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),val = 13), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21]))
    assert candidate(head = list_node([25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]),val = 25) == None
    assert is_same_list(candidate(head = list_node([1, 3, 2, 6, 5, 4, 6, 7, 8, 6, 9]),val = 6), list_node([1, 3, 2, 5, 4, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 10), list_node([5, 6, 7, 8, 9, 11, 12, 13, 14, 15]))
    assert candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),val = 5) == None
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]),val = 1), list_node([2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 20), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5]),val = 1), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 10]),val = 5), list_node([1, 2, 3, 4, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),val = 3), list_node([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),val = 26), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
    assert is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),val = 3), list_node([1, 4, 1, 5, 9, 2, 6, 5, 5]))
    assert is_same_list(candidate(head = list_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]),val = 3), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9, 3]),val = 3), list_node([1, 2, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 3, 2, 1]),val = 3), list_node([1, 2, 4, 2, 1, 2, 1]))
    assert is_same_list(candidate(head = list_node([10, 20, 10, 30, 10, 40]),val = 10), list_node([20, 30, 40]))
    assert is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41, 40]))
    assert candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),val = 5) == None
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),val = 20), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18]))
    assert is_same_list(candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41]),val = 45), list_node([50, 49, 48, 47, 46, 44, 43, 42, 41]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),val = 50), list_node([10, 20, 30, 40, 60, 70, 80, 90, 100]))
    assert is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),val = 50), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]),val = 3), list_node([1, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 40, 30, 20, 10]),val = 30), list_node([10, 20, 40, 50, 40, 20, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 3), list_node([10, 9, 8, 7, 6, 5, 4, 2, 1]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),val = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),val = 2), list_node([3]))
    assert is_same_list(candidate(head = list_node([49, 48, 47, 46, 45, 44, 43, 42, 41, 40]),val = 45), list_node([49, 48, 47, 46, 44, 43, 42, 41, 40]))
    assert candidate(head = list_node([1]),val = 1) == None
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]),val = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    assert is_same_list(candidate(head = list_node([42, 23, 42, 23, 42, 23, 42, 23, 42]),val = 42), list_node([23, 23, 23, 23]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]),val = 30), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 34, 36, 38, 40]))


