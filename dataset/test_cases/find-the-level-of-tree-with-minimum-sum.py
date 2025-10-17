def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, None, 5, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, None, 5, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 6, 2, 30, 80, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 6, 2, 30, 80, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([36, 17, 10, None, None, 24])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([36, 17, 10, None, None, 24])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, None, 8, None, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, None, 8, None, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 10, 11, 12, 13, 14, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 10, 11, 12, 13, 14, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, None, 75, 12, 13, None, None, 30, None, None, 40, 50])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, None, 75, 12, 13, None, None, 30, None, None, 40, 50])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, 11, None, 13, 14, 15, 16, None, None, 19])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, 11, None, 13, 14, 15, 16, None, None, 19])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, None, 200, None, 300, None, 400, None, 500])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, None, 200, None, 300, None, 400, None, 500])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 18, None, None, None, None, 1, None, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 18, None, None, None, None, 1, None, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, 10, None, None, 13, None, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, 10, None, None, 13, None, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80, None, 90])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80, None, 90])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 500, None, 500, None, 500, None, 500, None, 500, None, 500, None, 500])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 500, None, 500, None, 500, None, 500, None, 500, None, 500, None, 500])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 30, 10, 25, 28, 35, None, None, None, 33, None, None, 31, 36])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 30, 10, 25, 28, 35, None, None, None, 33, None, None, 31, 36])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, None, 30])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, None, 30])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, None, None, 11, 12, None, None, 13])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, None, None, 11, 12, None, None, 13])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, None, None, None, None, None, 80])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, None, None, None, None, None, 80])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, None, 11, 12, 13, 14, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, None, 11, 12, 13, 14, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, None, None, None, None])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, None, None, None, None])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 63, 87, 112, 137, 162, 187])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 63, 87, 112, 137, 162, 187])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, None, 75, None, 200, 60, 80, 190, 210])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, None, 75, None, 200, 60, 80, 190, 210])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 12, 14, None, 17, None, 19])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 12, 14, None, 17, None, 19])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, None, 30, 40, None, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, None, 30, 40, None, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000000000, None, 1000000000, None, 1000000000])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000000000, None, 1000000000, None, 1000000000])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, None, 60, 70, None, 80, None, 100, 110, None, None, 140])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, None, 60, 70, None, 80, None, 100, 110, None, None, 140])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, None, 2, None, 6, None, 9, None, 11])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, None, 2, None, 6, None, 9, None, 11])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 13, 18, 12, None, 14, 17, None, 19])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 13, 18, 12, None, 14, 17, None, 19])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 13, None, None, 8, None, None])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 13, None, None, 8, None, None])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, None, 2, 2, None, None, 2, 2, 2, 2, None, None, 2, 2])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, None, 2, 2, None, None, 2, 2, 2, 2, None, None, 2, 2])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, 12, 13, None, None, None, None, 14])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, 12, 13, None, None, None, None, 14])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, None, 110, 120, 130, 140, 150])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, None, 110, 120, 130, 140, 150])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 2, None, None, 3, 8, 4, None, None, 5, 7, 6, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 2, None, None, 3, 8, 4, None, None, 5, 7, 6, None, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, None, None, 11, 12])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, None, None, 11, 12])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000000000, 500000000, None, 250000000, 750000000])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000000000, 500000000, None, 250000000, 750000000])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 15, 20, 25, 30, 35, 40, None, None, 45, 50, 55, 60, None, 65])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 15, 20, 25, 30, 35, 40, None, None, 45, 50, 55, 60, None, 65])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 30, 10, 25, 35, 40, 5, 15, None, None, 31, 36, None, None, None, None, 4, 16])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 30, 10, 25, 35, 40, 5, 15, None, None, 31, 36, None, None, None, None, 4, 16])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 8, None, None, 12])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 8, None, None, 12])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, None, 30, 40, None, 50, None, None, 60, None, None, 70])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, None, 30, 40, None, 50, None, None, 60, None, None, 70])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, None, 75, None, 200, 60, None, None, 180])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, None, 75, None, 200, 60, None, None, 180])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, None, 40, None, 60, None, None, 30, None, None, 70])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, None, 40, None, 60, None, None, 30, None, None, 70])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 10, 25, None, None, None, None, 30, 35])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 10, 25, None, None, None, None, 30, 35])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, None, None, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, None, None, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, None, None, 15, None, 20, None, None, 25, None, 30])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, None, None, 15, None, 20, None, None, 25, None, 30])) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 1
    assert candidate(root = tree_node([5, None, 5, None, 5])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([50, 6, 2, 30, 80, 7])) == 2
    assert candidate(root = tree_node([100])) == 1
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == 1
    assert candidate(root = tree_node([36, 17, 10, None, None, 24])) == 3
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7])) == 1
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 10, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 4
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 4
    assert candidate(root = tree_node([100, 50, 50, 25, 25, None, 75, 12, 13, None, None, 30, None, None, 40, 50])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, 11, None, 13, 14, 15, 16, None, None, 19])) == 1
    assert candidate(root = tree_node([100, None, 200, None, 300, None, 400, None, 500])) == 1
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 18, None, None, None, None, 1, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, 10, None, None, 13, None, 15])) == 1
    assert candidate(root = tree_node([10, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80, None, 90])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 1
    assert candidate(root = tree_node([1000, 500, 500, None, 500, None, 500, None, 500, None, 500, None, 500, None, 500])) == 1
    assert candidate(root = tree_node([50, 20, 30, 10, 25, 28, 35, None, None, None, 33, None, None, 31, 36])) == 1
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, None, 30])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, None, None, 11, 12, None, None, 13])) == 1
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, None, None, None, None, None, 80])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1
    assert candidate(root = tree_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 5
    assert candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, None, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19])) == 1
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, None, None, None, None])) == 1
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 63, 87, 112, 137, 162, 187])) == 1
    assert candidate(root = tree_node([100, 50, 150, None, 75, None, 200, 60, 80, 190, 210])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 12, 14, None, 17, None, 19])) == 1
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1
    assert candidate(root = tree_node([10, 20, None, 30, 40, None, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, None, None, 80, 90, None, None, 100, 110])) == 1
    assert candidate(root = tree_node([1000000000, None, 1000000000, None, 1000000000])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 1
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([10, 20, 30, 40, None, 60, 70, None, 80, None, 100, 110, None, None, 140])) == 1
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, None, 2, None, 6, None, 9, None, 11])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12])) == 1
    assert candidate(root = tree_node([10, 5, 15, None, None, 13, 18, 12, None, 14, 17, None, 19])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 1
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 13, None, None, 8, None, None])) == 5
    assert candidate(root = tree_node([2, 2, 2, 2, None, 2, 2, None, None, 2, 2, 2, 2, None, None, 2, 2])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, 12, 13, None, None, None, None, 14])) == 1
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, None, 110, 120, 130, 140, 150])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([10, 9, 2, None, None, 3, 8, 4, None, None, 5, 7, 6, None, None])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, None, None, 11, 12])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 1
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 1
    assert candidate(root = tree_node([1000000000, 500000000, None, 250000000, 750000000])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 1
    assert candidate(root = tree_node([10, 15, 20, 25, 30, 35, 40, None, None, 45, 50, 55, 60, None, 65])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1
    assert candidate(root = tree_node([50, 20, 30, 10, 25, 35, 40, 5, 15, None, None, 31, 36, None, None, None, None, 4, 16])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 8, None, None, 12])) == 1
    assert candidate(root = tree_node([10, 20, None, 30, 40, None, 50, None, None, 60, None, None, 70])) == 1
    assert candidate(root = tree_node([100, 50, 150, None, 75, None, 200, 60, None, None, 180])) == 1
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([100, 50, 50, None, 40, None, 60, None, None, 30, None, None, 70])) == 4
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 1
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 10, 25, None, None, None, None, 30, 35])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, None, None, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1
    assert candidate(root = tree_node([5, 10, None, None, 15, None, 20, None, None, 25, None, 30])) == 1


