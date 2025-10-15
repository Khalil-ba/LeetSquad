def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 7.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 7.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50])) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50])) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, None, 20, None, 30, None, 40])) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, None, 20, None, 30, None, 40])) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 6, 1])) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 6, 1])) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 8, 11, 13, None, None, 2])) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 8, 11, 13, None, None, 2])) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 25, 28, 32, 38, 45])) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 25, 28, 32, 38, 45])) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100000, 50000, 150000, None, None, None, None, 25000, 75000, None, 125000, None, 175000])) == 150000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100000, 50000, 150000, None, None, None, None, 25000, 75000, None, 125000, None, 175000])) == 150000.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 190.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 190.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 30, 10, 20, 25, 35, 5, 12, 18, 22, 28, 32, 40, 45])) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 30, 10, 20, 25, 35, 5, 12, 18, 22, 28, 32, 40, 45])) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, 6, None, None, None, None, None, None, None, None, None, 0])) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, 6, None, None, None, None, None, None, None, None, None, 0])) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, None, None, None, 11, 12])) == 12.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, None, None, None, 11, 12])) == 12.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2147483647, 2147483647, 2147483647])) == 2147483647.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2147483647, 2147483647, 2147483647])) == 2147483647.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 2, None, 5, 3, None, None, 9, None, 10])) == 11.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 2, None, 5, 3, None, None, 9, None, 10])) == 11.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, 17, 18, 19, 20])) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, 17, 18, 19, 20])) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, 0, 2, 6, 9])) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, 0, 2, 6, 9])) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 190.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 190.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 20, 3, 7, 15, 25, None, None, 4, 8, 12, 18, 22, 28, 2, 6, 9, 11, 13, 16, 19, 21, 23, 27, 29, 1, 14, 17, 24, 26, 30])) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 20, 3, 7, 15, 25, None, None, 4, 8, 12, 18, 22, 28, 2, 6, 9, 11, 13, 16, 19, 21, 23, 27, 29, 1, 14, 17, 24, 26, 30])) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, None, None, 3])) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, None, None, 3])) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 1, 1, None, 5])) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 1, 1, None, 5])) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1, 2])) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1, 2])) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 98, 102, 115, 118, 125])) == 125.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 98, 102, 115, 118, 125])) == 125.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 6, None, 4, None, 8, 3, None, None, None, 7, 9])) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 6, None, 4, None, 8, 3, None, None, None, 7, 9])) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 8])) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 8])) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 110.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 110.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, 8, 9, 10, None, None, 11, 12])) == 12.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, 8, 9, 10, None, None, 11, 12])) == 12.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, None, 4, None, None, None, None, None, None, 5])) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, None, 4, None, None, None, None, None, None, 5])) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, 6])) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, 6])) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, None, None, None, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, None, None, None, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, None, None, None, None, None])) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, None, None, None, None, None])) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, None, None, 15, None, None, 16])) == 16.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, None, None, 15, None, None, 16])) == 16.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10, None, None, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10, None, None, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100000, 50000, 50000, 25000, 25000, 25000, 25000, 12500, 12500, 12500, 12500, 12500, 12500, 12500, 12500])) == 26666.666666666668
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100000, 50000, 50000, 25000, 25000, 25000, 25000, 12500, 12500, 12500, 12500, 12500, 12500, 12500, 12500])) == 26666.666666666668: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 100, 200, 300, 400, 500, 600, 700, 800, 900])) == 900.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 100, 200, 300, 400, 500, 600, 700, 800, 900])) == 900.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 12, 13, 14, 16, None, None, None, None, 17, 18, None, None, None, 19, None, None, None, 20])) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 12, 13, 14, 16, None, None, None, None, 17, 18, None, None, None, 19, None, None, None, 20])) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, None, None, 1250, 3750, 6250, 8750])) == 15000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, None, None, 1250, 3750, 6250, 8750])) == 15000.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, None, None, 6, 9, 4, 7, 3, 10])) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, None, None, 6, 9, 4, 7, 3, 10])) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, None, 9])) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, None, 9])) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, 6, None])) == 7.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, 6, None])) == 7.5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, None, None, 40, 50, None, None, None, 60, 70, 80])) == 80.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, None, None, 40, 50, None, None, None, 60, 70, 80])) == 80.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37, 0, 2, 4, 6, 8, 11, 14, 16, 18, 21, 24, 26, 28, 31, 34, 36, 38, 39])) == 39.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37, 0, 2, 4, 6, 8, 11, 14, 16, 18, 21, 24, 26, 28, 31, 34, 36, 38, 39])) == 39.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, 7, 13, 20, None, None, 6, 8, 12, 18, 25, 30])) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, 7, 13, 20, None, None, 6, 8, 12, 18, 25, 30])) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, None, 6, 8])) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, None, 6, 8])) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 2, 5, 3, None, 0, 6, None, None, None, 8])) == 8.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 2, 5, 3, None, 0, 6, None, None, None, 8])) == 8.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100000, 99999, 1, None, None, 99998, 99997, 99996, None, None, 99995, 99994])) == 99999.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100000, 99999, 1, None, None, 99998, 99997, 99996, None, None, 99995, 99994])) == 99999.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, None, 1, 1, 1, 1, None, 1, None, None, None, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, None, 1, 1, 1, 1, None, 1, None, None, None, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, None, None, None, 3.5])) == 4.75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, None, None, None, 3.5])) == 4.75: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 12, None, 14, None, None, 13, None, None, None, None, 8, None, None, 11, None, None, 10])) == 14.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 12, None, 14, None, None, 13, None, None, None, None, 8, None, None, 11, None, None, 10])) == 14.0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 13.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 7.0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5.0
    assert candidate(root = tree_node([10, 20, 30, 40, 50])) == 50.0
    assert candidate(root = tree_node([10, None, 20, None, 30, None, 40])) == 40.0
    assert candidate(root = tree_node([0, None, 1])) == 1.0
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 15.0
    assert candidate(root = tree_node([1])) == 1.0
    assert candidate(root = tree_node([5, 6, 1])) == 6.0
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 180.0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 8, 11, 13, None, None, 2])) == 18.0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 40.0
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 20.0
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 25, 28, 32, 38, 45])) == 45.0
    assert candidate(root = tree_node([100000, 50000, 150000, None, None, None, None, 25000, 75000, None, 125000, None, 175000])) == 150000.0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 18.0
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 190.0
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 4.0
    assert candidate(root = tree_node([25, 15, 30, 10, 20, 25, 35, 5, 12, 18, 22, 28, 32, 40, 45])) == 45.0
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, 6, None, None, None, None, None, None, None, None, None, 0])) == 9.0
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, None, None, None, 11, 12])) == 12.0
    assert candidate(root = tree_node([2147483647, 2147483647, 2147483647])) == 2147483647.0
    assert candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 2, None, 5, 3, None, None, 9, None, 10])) == 11.0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, 17, 18, 19, 20])) == 20.0
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, 0, 2, 6, 9])) == 10.0
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 190.0
    assert candidate(root = tree_node([10, 5, 20, 3, 7, 15, 25, None, None, 4, 8, 12, 18, 22, 28, 2, 6, 9, 11, 13, 16, 19, 21, 23, 27, 29, 1, 14, 17, 24, 26, 30])) == 30.0
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, None, None, 3])) == 13.0
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 3.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
    assert candidate(root = tree_node([5, 4, 5, 1, 1, None, 5])) == 5.0
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1, 2])) == 13.0
    assert candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 98, 102, 115, 118, 125])) == 125.0
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
    assert candidate(root = tree_node([5, 2, 6, None, 4, None, 8, 3, None, None, None, 7, 9])) == 9.0
    assert candidate(root = tree_node([1, 2, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 15.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 30.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 20.0
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 8])) == 9.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 15.0
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 110.0
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, 8, 9, 10, None, None, 11, 12])) == 12.0
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 2.0
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, None, 4, None, None, None, None, None, None, 5])) == 2.0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, 6])) == 18.0
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 25.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 50.0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9.0
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, None, None, None, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20])) == 15.0
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, None, None, None, None, None])) == 6.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, None, None, 15, None, None, 16])) == 16.0
    assert candidate(root = tree_node([2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10.0
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10, None, None, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None])) == 15.0
    assert candidate(root = tree_node([100000, 50000, 50000, 25000, 25000, 25000, 25000, 12500, 12500, 12500, 12500, 12500, 12500, 12500, 12500])) == 26666.666666666668
    assert candidate(root = tree_node([1, 100, 200, 300, 400, 500, 600, 700, 800, 900])) == 900.0
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 12, 13, 14, 16, None, None, None, None, 17, 18, None, None, None, 19, None, None, None, 20])) == 20.0
    assert candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])) == 75.0
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 6.0
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15.0
    assert candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, None, None, 1250, 3750, 6250, 8750])) == 15000.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 30.0
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 4.0
    assert candidate(root = tree_node([5, 2, 8, None, None, 6, 9, 4, 7, 3, 10])) == 10.0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 18.0
    assert candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 1.0
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, None, 9])) == 9.0
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, 6, None])) == 7.5
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9.0
    assert candidate(root = tree_node([10, 20, 30, None, None, 40, 50, None, None, None, 60, 70, 80])) == 80.0
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37, 0, 2, 4, 6, 8, 11, 14, 16, 18, 21, 24, 26, 28, 31, 34, 36, 38, 39])) == 39.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 180.0
    assert candidate(root = tree_node([10, 5, 15, None, 7, 13, 20, None, None, 6, 8, 12, 18, 25, 30])) == 30.0
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, None, 6, 8])) == 13.0
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 2, 5, 3, None, 0, 6, None, None, None, 8])) == 8.0
    assert candidate(root = tree_node([100000, 99999, 1, None, None, 99998, 99997, 99996, None, None, 99995, 99994])) == 99999.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, None, 1, 1, 1, 1, None, 1, None, None, None, 1])) == 1.0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 13.0
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 6.0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1.0
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, None, None, None, 3.5])) == 4.75
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 12, None, 14, None, None, 13, None, None, None, None, 8, None, None, 11, None, None, 10])) == 14.0
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 13.0


