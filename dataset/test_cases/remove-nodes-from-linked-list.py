def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 9, 7, 6, 5])), list_node([9, 7, 6, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 9, 7, 6, 5])), list_node([9, 7, 6, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50])), list_node([50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50])), list_node([50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 7, 6, 5, 4])), list_node([9, 7, 6, 5, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 7, 6, 5, 4])), list_node([9, 7, 6, 5, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 5, 20, 3])), list_node([20, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 5, 20, 3])), list_node([20, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 5, 8, 9, 2])), list_node([10, 9, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 5, 8, 9, 2])), list_node([10, 9, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 5, 3, 20, 2])), list_node([20, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 5, 3, 20, 2])), list_node([20, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 5, 20, 3, 8])), list_node([20, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 5, 20, 3, 8])), list_node([20, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5])), list_node([5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5])), list_node([5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 40, 30, 20, 10])), list_node([50, 40, 30, 20, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 40, 30, 20, 10])), list_node([50, 40, 30, 20, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1])), list_node([1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1])), list_node([1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1])), list_node([3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1])), list_node([3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 7, 5, 3, 1])), list_node([9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 7, 5, 3, 1])), list_node([9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 1, 9, 1])), list_node([9, 9, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 1, 9, 1])), list_node([9, 9, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6])), list_node([10, 9, 8, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6])), list_node([10, 9, 8, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 7, 8, 9, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 7, 8, 9, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 2, 13, 3, 8])), list_node([13, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 2, 13, 3, 8])), list_node([13, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 6, 5, 4, 7, 8, 1])), list_node([8, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 6, 5, 4, 7, 8, 1])), list_node([8, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1])), list_node([10, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1])), list_node([10, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 10, 20, 30, 40, 50])), list_node([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 10, 20, 30, 40, 50])), list_node([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90])), list_node([100, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90])), list_node([100, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11])), list_node([11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11])), list_node([11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 5, 20, 30, 5, 10, 15, 5, 25, 30])), list_node([30, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 5, 20, 30, 5, 10, 15, 5, 25, 30])), list_node([30, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15])), list_node([15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15])), list_node([15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8])), list_node([9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8])), list_node([9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100])), list_node([100, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100])), list_node([100, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])), list_node([10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])), list_node([10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])), list_node([10, 9, 8, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])), list_node([10, 9, 8, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])), list_node([10, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])), list_node([10, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 25, 20, 15, 10, 5, 30, 25, 20, 15, 10, 5])), list_node([30, 30, 25, 20, 15, 10, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 25, 20, 15, 10, 5, 30, 25, 20, 15, 10, 5])), list_node([30, 30, 25, 20, 15, 10, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 6, 7, 8, 9])), list_node([10, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 6, 7, 8, 9])), list_node([10, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])), list_node([6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])), list_node([6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5])), list_node([6, 6, 6, 6, 6, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5])), list_node([6, 6, 6, 6, 6, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 7, 2, 8, 10, 5, 6, 12])), list_node([12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 7, 2, 8, 10, 5, 6, 12])), list_node([12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91])), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91])), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10])), list_node([11, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10])), list_node([11, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11])), list_node([13, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11])), list_node([13, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 15, 30, 25, 40, 35, 50, 45, 60])), list_node([60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 15, 30, 25, 40, 35, 50, 45, 60])), list_node([60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 25, 35, 45, 55])), list_node([55]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 25, 35, 45, 55])), list_node([55])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 1, 2, 3, 4, 5, 99999])), list_node([100000, 99999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 1, 2, 3, 4, 5, 99999])), list_node([100000, 99999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 1, 10, 1, 10, 1, 10, 1, 10])), list_node([10, 10, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 1, 10, 1, 10, 1, 10, 1, 10])), list_node([10, 10, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11])), list_node([11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11])), list_node([11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1])), list_node([3, 3, 3, 3, 3, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1])), list_node([3, 3, 3, 3, 3, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100])), list_node([100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100])), list_node([100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1])), list_node([3, 3, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1])), list_node([3, 3, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1])), list_node([17, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1])), list_node([17, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 250, 200, 150, 100, 50, 1])), list_node([300, 250, 200, 150, 100, 50, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 250, 200, 150, 100, 50, 1])), list_node([300, 250, 200, 150, 100, 50, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 15, 25, 30, 5, 35, 40, 45, 50])), list_node([50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 15, 25, 30, 5, 35, 40, 45, 50])), list_node([50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 25, 35, 40, 38, 45, 42, 48, 47, 50])), list_node([50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 25, 35, 40, 38, 45, 42, 48, 47, 50])), list_node([50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 7, 2, 9, 8, 10, 6])), list_node([10, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 7, 2, 9, 8, 10, 6])), list_node([10, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 11, 6, 5, 4, 3, 2, 1])), list_node([11, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 11, 6, 5, 4, 3, 2, 1])), list_node([11, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 9, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4])), list_node([20, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 9, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4])), list_node([20, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])), list_node([100000, 99999, 99998, 99997, 99996, 99995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])), list_node([100000, 99999, 99998, 99997, 99996, 99995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11])), list_node([11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11])), list_node([11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 900, 1001, 800, 1002, 700, 1003, 600, 1004, 500, 1005, 400, 1006, 300, 1007, 200, 1008, 100])), list_node([1008, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 900, 1001, 800, 1002, 700, 1003, 600, 1004, 500, 1005, 400, 1006, 300, 1007, 200, 1008, 100])), list_node([1008, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20])), list_node([20, 20, 20, 20, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20])), list_node([20, 20, 20, 20, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1, 10, 9, 8, 7, 6, 5, 4])), list_node([10, 9, 8, 7, 6, 5, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1, 10, 9, 8, 7, 6, 5, 4])), list_node([10, 9, 8, 7, 6, 5, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 100000, 2, 200000, 3, 300000, 4, 400000, 5, 500000])), list_node([500000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 100000, 2, 200000, 3, 300000, 4, 400000, 5, 500000])), list_node([500000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 9, 9, 2, 2, 8, 8, 3, 3, 7, 7, 4, 4, 6, 6, 5, 5])), list_node([9, 9, 8, 8, 7, 7, 6, 6, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 9, 9, 2, 2, 8, 8, 3, 3, 7, 7, 4, 4, 6, 6, 5, 5])), list_node([9, 9, 8, 8, 7, 7, 6, 6, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 5, 15, 5, 20, 5, 25, 5, 30])), list_node([30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 5, 15, 5, 20, 5, 25, 5, 30])), list_node([30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 1, 10, 2, 10, 3, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 10, 9, 10, 11])), list_node([11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 1, 10, 2, 10, 3, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 10, 9, 10, 11])), list_node([11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5])), list_node([9, 8, 7, 6, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5])), list_node([9, 8, 7, 6, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2])), list_node([2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2])), list_node([2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 50, 150, 200, 100, 250, 200])), list_node([250, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 50, 150, 200, 100, 250, 200])), list_node([250, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([100000, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([100000, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 10, 20, 30, 40])), list_node([105, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 10, 20, 30, 40])), list_node([105, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 25, 35, 45, 15, 25])), list_node([50, 45, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 25, 35, 45, 15, 25])), list_node([50, 45, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100])), list_node([100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100])), list_node([100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 11, 10, 12, 11, 13, 12])), list_node([13, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 11, 10, 12, 11, 13, 12])), list_node([13, 12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1, 4, 5, 6, 7, 8, 9, 10])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1, 4, 5, 6, 7, 8, 9, 10])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 50, 50, 50, 50, 49, 48, 47, 46, 45])), list_node([50, 50, 50, 50, 50, 49, 48, 47, 46, 45]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 50, 50, 50, 50, 49, 48, 47, 46, 45])), list_node([50, 50, 50, 50, 50, 49, 48, 47, 46, 45])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 10, 6, 5, 4, 3, 2, 1, 11])), list_node([11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 10, 6, 5, 4, 3, 2, 1, 11])), list_node([11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4])), list_node([10, 9, 8, 7, 6, 5, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4])), list_node([10, 9, 8, 7, 6, 5, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 4, 2, 5, 1, 6, 7])), list_node([7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 4, 2, 5, 1, 6, 7])), list_node([7])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([8, 9, 7, 6, 5])), list_node([9, 7, 6, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([5]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50])), list_node([50]))
    assert is_same_list(candidate(head = list_node([9, 7, 6, 5, 4])), list_node([9, 7, 6, 5, 4]))
    assert is_same_list(candidate(head = list_node([10, 5, 20, 3])), list_node([20, 3]))
    assert is_same_list(candidate(head = list_node([10, 5, 8, 9, 2])), list_node([10, 9, 2]))
    assert is_same_list(candidate(head = list_node([10, 5, 3, 20, 2])), list_node([20, 2]))
    assert is_same_list(candidate(head = list_node([10, 5, 20, 3, 8])), list_node([20, 8]))
    assert is_same_list(candidate(head = list_node([5])), list_node([5]))
    assert is_same_list(candidate(head = list_node([50, 40, 30, 20, 10])), list_node([50, 40, 30, 20, 10]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1])), list_node([1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([3, 2, 1])), list_node([3, 2, 1]))
    assert is_same_list(candidate(head = list_node([9, 7, 5, 3, 1])), list_node([9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([1, 9, 1, 9, 1])), list_node([9, 9, 1]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6])), list_node([10, 9, 8, 7, 6]))
    assert is_same_list(candidate(head = list_node([6, 7, 8, 9, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([5, 2, 13, 3, 8])), list_node([13, 8]))
    assert is_same_list(candidate(head = list_node([3, 2, 6, 5, 4, 7, 8, 1])), list_node([8, 1]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1])), list_node([10, 1]))
    assert is_same_list(candidate(head = list_node([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 10, 20, 30, 40, 50])), list_node([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 50]))
    assert is_same_list(candidate(head = list_node([10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90])), list_node([100, 90]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([9]))
    assert is_same_list(candidate(head = list_node([5, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 10]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11])), list_node([11]))
    assert is_same_list(candidate(head = list_node([10, 5, 20, 30, 5, 10, 15, 5, 25, 30])), list_node([30, 30]))
    assert is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15])), list_node([15]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8])), list_node([9, 8]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100])), list_node([100, 100]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])), list_node([10, 10]))
    assert is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])), list_node([10, 9, 8, 7, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])), list_node([10, 1]))
    assert is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([30, 25, 20, 15, 10, 5, 30, 25, 20, 15, 10, 5])), list_node([30, 30, 25, 20, 15, 10, 5]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 6, 7, 8, 9])), list_node([10, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])), list_node([6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5])), list_node([6, 6, 6, 6, 6, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
    assert is_same_list(candidate(head = list_node([3, 7, 2, 8, 10, 5, 6, 12])), list_node([12]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91])), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91]))
    assert is_same_list(candidate(head = list_node([2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10])), list_node([11, 10]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([5, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10, 13, 11])), list_node([13, 11]))
    assert is_same_list(candidate(head = list_node([10, 20, 15, 30, 25, 40, 35, 50, 45, 60])), list_node([60]))
    assert is_same_list(candidate(head = list_node([1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 25, 35, 45, 55])), list_node([55]))
    assert is_same_list(candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([100000, 1, 2, 3, 4, 5, 99999])), list_node([100000, 99999]))
    assert is_same_list(candidate(head = list_node([1, 10, 1, 10, 1, 10, 1, 10, 1, 10])), list_node([10, 10, 10, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11])), list_node([11]))
    assert is_same_list(candidate(head = list_node([2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1])), list_node([3, 3, 3, 3, 3, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100])), list_node([100]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10]))
    assert is_same_list(candidate(head = list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1])), list_node([3, 3, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([10, 9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1])), list_node([17, 1]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 250, 200, 150, 100, 50, 1])), list_node([300, 250, 200, 150, 100, 50, 1]))
    assert is_same_list(candidate(head = list_node([10, 20, 15, 25, 30, 5, 35, 40, 45, 50])), list_node([50]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 25, 35, 40, 38, 45, 42, 48, 47, 50])), list_node([50]))
    assert is_same_list(candidate(head = list_node([3, 7, 2, 9, 8, 10, 6])), list_node([10, 6]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 11, 6, 5, 4, 3, 2, 1])), list_node([11, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([5, 9, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4])), list_node([20, 4]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])), list_node([100000, 99999, 99998, 99997, 99996, 99995]))
    assert is_same_list(candidate(head = list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11])), list_node([11]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([1000, 900, 1001, 800, 1002, 700, 1003, 600, 1004, 500, 1005, 400, 1006, 300, 1007, 200, 1008, 100])), list_node([1008, 100]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20])), list_node([20, 20, 20, 20, 20]))
    assert is_same_list(candidate(head = list_node([3, 2, 1, 10, 9, 8, 7, 6, 5, 4])), list_node([10, 9, 8, 7, 6, 5, 4]))
    assert is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 100000, 2, 200000, 3, 300000, 4, 400000, 5, 500000])), list_node([500000]))
    assert is_same_list(candidate(head = list_node([1, 1, 9, 9, 2, 2, 8, 8, 3, 3, 7, 7, 4, 4, 6, 6, 5, 5])), list_node([9, 9, 8, 8, 7, 7, 6, 6, 5, 5]))
    assert is_same_list(candidate(head = list_node([5, 10, 5, 15, 5, 20, 5, 25, 5, 30])), list_node([30]))
    assert is_same_list(candidate(head = list_node([10, 1, 10, 2, 10, 3, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 10, 9, 10, 11])), list_node([11]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20]))
    assert is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5])), list_node([9, 8, 7, 6, 5]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2])), list_node([2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([100, 50, 150, 200, 100, 250, 200])), list_node([250, 200]))
    assert is_same_list(candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([100000, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 10, 20, 30, 40])), list_node([105, 40]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 25, 35, 45, 15, 25])), list_node([50, 45, 25]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100])), list_node([100]))
    assert is_same_list(candidate(head = list_node([10, 9, 11, 10, 12, 11, 13, 12])), list_node([13, 12]))
    assert is_same_list(candidate(head = list_node([3, 2, 1, 4, 5, 6, 7, 8, 9, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([50, 50, 50, 50, 50, 49, 48, 47, 46, 45])), list_node([50, 50, 50, 50, 50, 49, 48, 47, 46, 45]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 10, 6, 5, 4, 3, 2, 1, 11])), list_node([11]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4])), list_node([10, 9, 8, 7, 6, 5, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([25]))
    assert is_same_list(candidate(head = list_node([3, 4, 2, 5, 1, 6, 7])), list_node([7]))


