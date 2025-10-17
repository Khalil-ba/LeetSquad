def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 7, 5, 3, 1])) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 7, 5, 3, 1])) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5])) == [2, 3, 4, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5])) == [2, 3, 4, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1])) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1])) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 7, 5, 1, 9, 2, 5, 1])) == [7, 9, 9, 9, 0, 5, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 7, 5, 1, 9, 2, 5, 1])) == [7, 9, 9, 9, 0, 5, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1])) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1])) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 5])) == [5, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 5])) == [5, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 2, 3, 4])) == [2, 3, 4, 0, 4, 3, 2, 3, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 2, 3, 4])) == [2, 3, 4, 0, 4, 3, 2, 3, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])) == [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])) == [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) == [5, 6, 4, 6, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) == [5, 6, 4, 6, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 7, 5, 3, 1, 2, 4, 6, 8, 10])) == [10, 8, 6, 4, 2, 4, 6, 8, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 7, 5, 3, 1, 2, 4, 6, 8, 10])) == [10, 8, 6, 4, 2, 4, 6, 8, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 1, 2, 5, 3, 9, 4, 6, 8, 7])) == [0, 2, 5, 9, 9, 0, 6, 8, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 1, 2, 5, 3, 9, 4, 6, 8, 7])) == [0, 2, 5, 9, 9, 0, 6, 8, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 1, 5, 1, 5, 1, 5, 1, 5, 1])) == [0, 5, 0, 5, 0, 5, 0, 5, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 1, 5, 1, 5, 1, 5, 1, 5, 1])) == [0, 5, 0, 5, 0, 5, 0, 5, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 5, 4, 6, 2, 8, 7, 3, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [5, 6, 6, 8, 8, 9, 9, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 5, 4, 6, 2, 8, 7, 3, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [5, 6, 6, 8, 8, 9, 9, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10])) == [0, 19, 0, 18, 0, 17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10])) == [0, 19, 0, 18, 0, 17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11])) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11])) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1])) == [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1])) == [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 12, 13, 14, 15, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 12, 13, 14, 15, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8])) == [3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8])) == [3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1])) == [2, 3, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1])) == [2, 3, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 1, 4, 2, 6, 3, 8, 7, 9, 10, 1, 2, 3, 4])) == [6, 4, 6, 6, 8, 8, 9, 9, 10, 0, 2, 3, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 1, 4, 2, 6, 3, 8, 7, 9, 10, 1, 2, 3, 4])) == [6, 4, 6, 6, 8, 8, 9, 9, 10, 0, 2, 3, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 2, 1, 5, 4, 6, 7, 8, 9, 1])) == [5, 5, 5, 6, 6, 7, 8, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 2, 1, 5, 4, 6, 7, 8, 9, 1])) == [5, 5, 5, 6, 6, 7, 8, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])) == [20, 30, 40, 50, 60, 70, 80, 90, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])) == [20, 30, 40, 50, 60, 70, 80, 90, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6])) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6])) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10])) == [3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10])) == [3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21])) == [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21])) == [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])) == [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])) == [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])) == [10, 0, 9, 0, 8, 0, 7, 0, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])) == [10, 0, 9, 0, 8, 0, 7, 0, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10])) == [2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10])) == [2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 7, 8, 4, 2, 10, 5, 9, 1])) == [7, 8, 10, 10, 10, 0, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 7, 8, 4, 2, 10, 5, 9, 1])) == [7, 8, 10, 10, 10, 0, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4])) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4])) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 1, 10, 1, 10, 1, 10])) == [10, 0, 10, 0, 10, 0, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 1, 10, 1, 10, 1, 10])) == [10, 0, 10, 0, 10, 0, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 6, 2, 5, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3])) == [6, 0, 5, 6, 4, 5, 6, 2, 3, 4, 5, 6, 0, 2, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 6, 2, 5, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3])) == [6, 0, 5, 6, 4, 5, 6, 2, 3, 4, 5, 6, 0, 2, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11])) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11])) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 8, 7, 6, 10, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15])) == [10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 13, 14, 15, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 8, 7, 6, 10, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15])) == [10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 13, 14, 15, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6])) == [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6])) == [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 1, 4, 3, 2, 6, 1, 2, 4, 3, 5, 1, 2, 4, 3, 6, 1, 2, 4, 3])) == [6, 4, 6, 6, 6, 0, 2, 4, 5, 5, 6, 2, 4, 6, 6, 0, 2, 4, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 1, 4, 3, 2, 6, 1, 2, 4, 3, 5, 1, 2, 4, 3, 6, 1, 2, 4, 3])) == [6, 4, 6, 6, 6, 0, 2, 4, 5, 5, 6, 2, 4, 6, 6, 0, 2, 4, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 2, 3, 4, 5, 6, 7, 8, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 1, 4, 2, 3, 6, 8, 7, 10, 9, 12])) == [6, 4, 6, 3, 6, 8, 10, 10, 12, 12, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 1, 4, 2, 3, 6, 8, 7, 10, 9, 12])) == [6, 4, 6, 3, 6, 8, 10, 10, 12, 12, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 7, 5, 3, 1, 0, 12, 8, 10])) == [12, 12, 12, 12, 12, 12, 0, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 7, 5, 3, 1, 0, 12, 8, 10])) == [12, 12, 12, 12, 12, 12, 0, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 5, 3, 4, 2, 6, 7, 8, 10, 9, 11])) == [5, 6, 4, 6, 6, 7, 8, 10, 11, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 5, 3, 4, 2, 6, 7, 8, 10, 9, 11])) == [5, 6, 4, 6, 6, 7, 8, 10, 11, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 8, 6, 5, 9, 1, 2, 4])) == [8, 9, 9, 9, 0, 2, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 8, 6, 5, 9, 1, 2, 4])) == [8, 9, 9, 9, 0, 2, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 50, 25, 10, 5, 1, 99, 49, 24, 9, 4, 2, 0])) == [0, 99, 99, 99, 99, 99, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 50, 25, 10, 5, 1, 99, 49, 24, 9, 4, 2, 0])) == [0, 99, 99, 99, 99, 99, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 8, 4, 7, 10, 3, 6, 2, 9, 1])) == [8, 10, 7, 10, 0, 6, 9, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 8, 4, 7, 10, 3, 6, 2, 9, 1])) == [8, 10, 7, 10, 0, 6, 9, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 5, 6, 2, 3, 1, 9, 8])) == [5, 5, 6, 9, 3, 9, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 5, 6, 2, 3, 1, 9, 8])) == [5, 5, 6, 9, 3, 9, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([109, 108, 107, 106, 105, 104, 103, 102, 101, 100])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([109, 108, 107, 106, 105, 104, 103, 102, 101, 100])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 3, 4, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 4, 5, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 3, 4, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 4, 5, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 2, 4, 6, 5, 7, 9, 8, 10])) == [3, 4, 4, 6, 7, 7, 9, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 2, 4, 6, 5, 7, 9, 8, 10])) == [3, 4, 4, 6, 7, 7, 9, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) == [2, 3, 4, 5, 0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) == [2, 3, 4, 5, 0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17])) == [3, 5, 7, 9, 11, 9, 7, 5, 3, 3, 5, 7, 9, 11, 13, 15, 17, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17])) == [3, 5, 7, 9, 11, 9, 7, 5, 3, 3, 5, 7, 9, 11, 13, 15, 17, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12])) == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12])) == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 1, 3, 2, 4, 3, 5, 4])) == [2, 3, 3, 4, 4, 5, 5, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 1, 3, 2, 4, 3, 5, 4])) == [2, 3, 3, 4, 4, 5, 5, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 3, 1, 4, 2, 6, 7, 8, 10, 9, 11])) == [6, 4, 4, 6, 6, 7, 8, 10, 11, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 3, 1, 4, 2, 6, 7, 8, 10, 9, 11])) == [6, 4, 4, 6, 6, 7, 8, 10, 11, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 2, 1, 5, 4, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) == [5, 5, 5, 6, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 2, 1, 5, 4, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) == [5, 5, 5, 6, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])) == [101, 102, 103, 104, 105, 106, 107, 108, 109, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])) == [101, 102, 103, 104, 105, 106, 107, 108, 109, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16])) == [2, 3, 4, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16])) == [2, 3, 4, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 8, 3, 7, 9, 1, 2, 4, 6])) == [8, 9, 7, 9, 0, 2, 4, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 8, 3, 7, 9, 1, 2, 4, 6])) == [8, 9, 7, 9, 0, 2, 4, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 2, 4, 5, 3, 2, 1, 6, 7, 8, 9, 10])) == [3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 2, 4, 5, 3, 2, 1, 6, 7, 8, 9, 10])) == [3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 1, 4, 2, 8, 7, 6, 9, 10])) == [8, 4, 8, 8, 9, 9, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 1, 4, 2, 8, 7, 6, 9, 10])) == [8, 4, 8, 8, 9, 9, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1])) == [2, 3, 0, 3, 2, 3, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1])) == [2, 3, 0, 3, 2, 3, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10])) == [3, 5, 5, 7, 7, 9, 9, 11, 11, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10])) == [3, 5, 5, 7, 7, 9, 9, 11, 11, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8])) == [5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8])) == [5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 5, 4, 3, 6, 7, 8, 9, 10])) == [5, 5, 6, 6, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 5, 4, 3, 6, 7, 8, 9, 10])) == [5, 5, 6, 6, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 22, 9, 33, 21, 50, 41, 60, 80])) == [22, 33, 33, 50, 50, 60, 60, 80, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 22, 9, 33, 21, 50, 41, 60, 80])) == [22, 33, 33, 50, 50, 60, 60, 80, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 20, 0, 19, 0, 18, 0, 17, 0, 16, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 20, 0, 19, 0, 18, 0, 17, 0, 16, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1])) == [2, 3, 0, 3, 3, 0, 3, 3, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1])) == [2, 3, 0, 3, 3, 0, 3, 3, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == [2, 3, 4, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == [2, 3, 4, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 7, 8, 5, 6, 4, 3, 2, 1])) == [0, 8, 0, 6, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 7, 8, 5, 6, 4, 3, 2, 1])) == [0, 8, 0, 6, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 3, 2, 7, 6, 4, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [7, 7, 7, 8, 8, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 3, 2, 7, 6, 4, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [7, 7, 7, 8, 8, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1])) == [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1])) == [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 2])) == [3, 5, 5, 6, 6, 7, 8, 9, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 2])) == [3, 5, 5, 6, 6, 7, 8, 9, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 5, 12, 9, 15, 3, 7, 11, 8])) == [12, 12, 15, 15, 0, 7, 11, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 5, 12, 9, 15, 3, 7, 11, 8])) == [12, 12, 15, 15, 0, 7, 11, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 1, 4, 2, 8, 7, 3, 6, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [8, 4, 8, 8, 9, 9, 6, 9, 10, 0, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 1, 4, 2, 8, 7, 3, 6, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [8, 4, 8, 8, 9, 9, 6, 9, 10, 0, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([17, 15, 13, 11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18])) == [18, 16, 14, 12, 10, 8, 6, 4, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([17, 15, 13, 11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18])) == [18, 16, 14, 12, 10, 8, 6, 4, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])) == [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])) == [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])) == [3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])) == [3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 2, 3, 4, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 2, 3, 4, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0]
    assert candidate(head = list_node([9, 7, 5, 3, 1])) == [0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5])) == [2, 3, 4, 5, 0]
    assert candidate(head = list_node([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
    assert candidate(head = list_node([1])) == [0]
    assert candidate(head = list_node([1, 7, 5, 1, 9, 2, 5, 1])) == [7, 9, 9, 9, 0, 5, 0, 0]
    assert candidate(head = list_node([1, 1, 1, 1, 1])) == [0, 0, 0, 0, 0]
    assert candidate(head = list_node([2, 1, 5])) == [5, 5, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 3, 2, 1, 2, 3, 4])) == [2, 3, 4, 0, 4, 3, 2, 3, 4, 0]
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])) == [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 0, 0, 0]
    assert candidate(head = list_node([1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) == [5, 6, 4, 6, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 0]
    assert candidate(head = list_node([9, 7, 5, 3, 1, 2, 4, 6, 8, 10])) == [10, 8, 6, 4, 2, 4, 6, 8, 10, 0]
    assert candidate(head = list_node([1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([10, 1, 2, 5, 3, 9, 4, 6, 8, 7])) == [0, 2, 5, 9, 9, 0, 6, 8, 0, 0]
    assert candidate(head = list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([5, 1, 5, 1, 5, 1, 5, 1, 5, 1])) == [0, 5, 0, 5, 0, 5, 0, 5, 0, 0]
    assert candidate(head = list_node([1, 5, 4, 6, 2, 8, 7, 3, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [5, 6, 6, 8, 8, 9, 9, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10])) == [0, 19, 0, 18, 0, 17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11])) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0]
    assert candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1])) == [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 0, 0]
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 12, 13, 14, 15, 0]
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0]
    assert candidate(head = list_node([1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8])) == [3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1])) == [2, 3, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([5, 1, 4, 2, 6, 3, 8, 7, 9, 10, 1, 2, 3, 4])) == [6, 4, 6, 6, 8, 8, 9, 9, 10, 0, 2, 3, 4, 0]
    assert candidate(head = list_node([3, 2, 1, 5, 4, 6, 7, 8, 9, 1])) == [5, 5, 5, 6, 6, 7, 8, 9, 0, 0]
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])) == [20, 30, 40, 50, 60, 70, 80, 90, 0]
    assert candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    assert candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6])) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10])) == [3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21])) == [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10])) == [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])) == [10, 0, 9, 0, 8, 0, 7, 0, 6, 0]
    assert candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10])) == [2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]
    assert candidate(head = list_node([3, 7, 8, 4, 2, 10, 5, 9, 1])) == [7, 8, 10, 10, 10, 0, 9, 0, 0]
    assert candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4])) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0]
    assert candidate(head = list_node([1, 10, 1, 10, 1, 10, 1, 10])) == [10, 0, 10, 0, 10, 0, 10, 0]
    assert candidate(head = list_node([5, 6, 2, 5, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3])) == [6, 0, 5, 6, 4, 5, 6, 2, 3, 4, 5, 6, 0, 2, 3, 0]
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11])) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0]
    assert candidate(head = list_node([9, 8, 7, 6, 10, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15])) == [10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 13, 14, 15, 0]
    assert candidate(head = list_node([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6])) == [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([5, 1, 4, 3, 2, 6, 1, 2, 4, 3, 5, 1, 2, 4, 3, 6, 1, 2, 4, 3])) == [6, 4, 6, 6, 6, 0, 2, 4, 5, 5, 6, 2, 4, 6, 6, 0, 2, 4, 0, 0]
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 0]
    assert candidate(head = list_node([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert candidate(head = list_node([5, 1, 4, 2, 3, 6, 8, 7, 10, 9, 12])) == [6, 4, 6, 3, 6, 8, 10, 10, 12, 12, 0]
    assert candidate(head = list_node([9, 7, 5, 3, 1, 0, 12, 8, 10])) == [12, 12, 12, 12, 12, 12, 0, 10, 0]
    assert candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 5, 3, 4, 2, 6, 7, 8, 10, 9, 11])) == [5, 6, 4, 6, 6, 7, 8, 10, 11, 11, 0]
    assert candidate(head = list_node([3, 8, 6, 5, 9, 1, 2, 4])) == [8, 9, 9, 9, 0, 2, 4, 0]
    assert candidate(head = list_node([100, 50, 25, 10, 5, 1, 99, 49, 24, 9, 4, 2, 0])) == [0, 99, 99, 99, 99, 99, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([5, 8, 4, 7, 10, 3, 6, 2, 9, 1])) == [8, 10, 7, 10, 0, 6, 9, 9, 0, 0]
    assert candidate(head = list_node([2, 1, 5, 6, 2, 3, 1, 9, 8])) == [5, 5, 6, 9, 3, 9, 9, 0, 0]
    assert candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    assert candidate(head = list_node([109, 108, 107, 106, 105, 104, 103, 102, 101, 100])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 3, 4, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 4, 5, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 0]
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
    assert candidate(head = list_node([1, 3, 2, 4, 6, 5, 7, 9, 8, 10])) == [3, 4, 4, 6, 7, 7, 9, 10, 10, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) == [2, 3, 4, 5, 0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 0, 2, 3, 4, 5, 0]
    assert candidate(head = list_node([1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 3, 5, 7, 9, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17])) == [3, 5, 7, 9, 11, 9, 7, 5, 3, 3, 5, 7, 9, 11, 13, 15, 17, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12])) == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 0]
    assert candidate(head = list_node([1, 2, 1, 3, 2, 4, 3, 5, 4])) == [2, 3, 3, 4, 4, 5, 5, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([5, 3, 1, 4, 2, 6, 7, 8, 10, 9, 11])) == [6, 4, 4, 6, 6, 7, 8, 10, 11, 11, 0]
    assert candidate(head = list_node([3, 2, 1, 5, 4, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) == [5, 5, 5, 6, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 0]
    assert candidate(head = list_node([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])) == [101, 102, 103, 104, 105, 106, 107, 108, 109, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16])) == [2, 3, 4, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([5, 8, 3, 7, 9, 1, 2, 4, 6])) == [8, 9, 7, 9, 0, 2, 4, 6, 0]
    assert candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    assert candidate(head = list_node([1, 3, 2, 4, 5, 3, 2, 1, 6, 7, 8, 9, 10])) == [3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    assert candidate(head = list_node([5, 1, 4, 2, 8, 7, 6, 9, 10])) == [8, 4, 8, 8, 9, 9, 9, 10, 0]
    assert candidate(head = list_node([1, 2, 3, 2, 1, 2, 3, 2, 1])) == [2, 3, 0, 3, 2, 3, 0, 0, 0]
    assert candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10])) == [3, 5, 5, 7, 7, 9, 9, 11, 11, 0, 0]
    assert candidate(head = list_node([1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8])) == [5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0, 0]
    assert candidate(head = list_node([2, 1, 5, 4, 3, 6, 7, 8, 9, 10])) == [5, 5, 6, 6, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([10, 22, 9, 33, 21, 50, 41, 60, 80])) == [22, 33, 33, 50, 50, 60, 60, 80, 0]
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16])) == [10, 11, 9, 11, 8, 11, 7, 11, 6, 11, 20, 0, 19, 0, 18, 0, 17, 0, 16, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1])) == [2, 3, 0, 3, 3, 0, 3, 3, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == [2, 3, 4, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([9, 7, 8, 5, 6, 4, 3, 2, 1])) == [0, 8, 0, 6, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 0]
    assert candidate(head = list_node([5, 3, 2, 7, 6, 4, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [7, 7, 7, 8, 8, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1])) == [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert candidate(head = list_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 2])) == [3, 5, 5, 6, 6, 7, 8, 9, 10, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [2, 3, 4, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([10, 5, 12, 9, 15, 3, 7, 11, 8])) == [12, 12, 15, 15, 0, 7, 11, 0, 0]
    assert candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
    assert candidate(head = list_node([5, 1, 4, 2, 8, 7, 3, 6, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [8, 4, 8, 8, 9, 9, 6, 9, 10, 0, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(head = list_node([17, 15, 13, 11, 9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18])) == [18, 16, 14, 12, 10, 8, 6, 4, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0]
    assert candidate(head = list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])) == [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]
    assert candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])) == [3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 0, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 2, 3, 4, 5, 0]
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]


