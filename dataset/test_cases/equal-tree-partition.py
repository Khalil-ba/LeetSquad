def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, -1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, -1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 10, None, None, 2, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 10, None, None, 2, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 10, None, None, 2, 20])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 10, None, None, 2, 20])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, -3, None, None, 3, -1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, -3, None, None, 3, -1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, None, 3, 3, 4, None, None, 4, 4, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, None, 3, 3, 4, None, None, 4, 4, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 20, None, None, 15, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 20, None, None, 15, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 62, 88, 6, 18, 30, 44, 55, 69, 82, 94])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 62, 88, 6, 18, 30, 44, 55, 69, 82, 94])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1, -1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1, -1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, -500, -500, 250, 250, 250, 250, -125, -125, -125, -125, -125, -125, -125, -125])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, -500, -500, 250, 250, 250, 250, -125, -125, -125, -125, -125, -125, -125, -125])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, -10000, 0, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, -10000, 0, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, None, None, None, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, None, None, None, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 14, 15, 16, 17, 18, 19])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 14, 15, 16, 17, 18, 19])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8, 9])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8, 9])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, None, None, None, 32, 33])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, None, None, None, 32, 33])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, None, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, None, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 10, 10, None, 10, None, None, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 10, 10, None, 10, None, None, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, -5000, -5000, 2500, 2500, 2500, 2500, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, -5000, -5000, 2500, 2500, 2500, 2500, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, 32])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, 32])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 10, -10, 10, -10, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 10, -10, 10, -10, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, -10000, 20000, -20000, 30000, -30000, 40000])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, -10000, 20000, -20000, 30000, -30000, 40000])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, -500, -500, 250, 250, 250, 250, -125, -125, -125, -125, -125, -125, -125, -125, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, -500, -500, 250, 250, 250, 250, -125, -125, -125, -125, -125, -125, -125, -125, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 1, None, 10, 2, 3, None, 10, 1, 1, None, None, 1, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 1, None, 10, 2, 3, None, 10, 1, 1, None, None, 1, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, -50, 25, 25, 25, 25, -12, -12, -12, -12, -12, -12, -12, -12])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, -50, 25, 25, 25, 25, -12, -12, -12, -12, -12, -12, -12, -12])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 8, 1, 4, 6, 9, 11, 13])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 8, 1, 4, 6, 9, 11, 13])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4, -4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4, -4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, -1000, 1000, -1000, 1000, -1000, 1000])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, -1000, 1000, -1000, 1000, -1000, 1000])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, None, None, 14, 13, 13, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, None, None, 14, 13, 13, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, 1, -1, 1, -1, 1, -1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, 1, -1, 1, -1, 1, -1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 1, -1, -1, -1, -1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 1, -1, -1, -1, -1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 14, None, None, 9, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 14, None, None, 9, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, None, None, None, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, None, None, None, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, -500, 500, 250, -250, 250, -250, 125, -125, 125, -125, 125, -125, 125, -125])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, -500, 500, 250, -250, 250, -250, 125, -125, 125, -125, 125, -125, 125, -125])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, 17, 20])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, 17, 20])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 12, 13, 12, 13, 12, 13])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 12, 13, 12, 13, 12, 13])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == False
    assert candidate(root = tree_node([0, 1, -1])) == False
    assert candidate(root = tree_node([5, 10, 10, None, None, 2, 3])) == True
    assert candidate(root = tree_node([1, 2, 10, None, None, 2, 20])) == False
    assert candidate(root = tree_node([1])) == False
    assert candidate(root = tree_node([0])) == False
    assert candidate(root = tree_node([1, -1, 0])) == True
    assert candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([5, 2, -3, None, None, 3, -1, 1])) == False
    assert candidate(root = tree_node([1, 2, 2, 3, None, 3, 3, 4, None, None, 4, 4, 4])) == False
    assert candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == False
    assert candidate(root = tree_node([10, -10, 20, None, None, 15, 5])) == False
    assert candidate(root = tree_node([1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])) == False
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25])) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == False
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 62, 88, 6, 18, 30, 44, 55, 69, 82, 94])) == False
    assert candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1, -1])) == True
    assert candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == False
    assert candidate(root = tree_node([1000, -500, -500, 250, 250, 250, 250, -125, -125, -125, -125, -125, -125, -125, -125])) == True
    assert candidate(root = tree_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([10000, -10000, 0, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156])) == True
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, None, None, None, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == False
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 14, 15, 16, 17, 18, 19])) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 25])) == False
    assert candidate(root = tree_node([0, 1, 1])) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == False
    assert candidate(root = tree_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8, 9])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, None, None, None, 32, 33])) == False
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == False
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == False
    assert candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7])) == False
    assert candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == False
    assert candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4])) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == True
    assert candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, None, None, 1])) == False
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False
    assert candidate(root = tree_node([10, 9, 10, 10, None, 10, None, None, 10])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == False
    assert candidate(root = tree_node([10000, -5000, -5000, 2500, 2500, 2500, 2500, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False
    assert candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == False
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None, None, None, None, 32])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False
    assert candidate(root = tree_node([10, -10, 10, -10, 10, -10, 10])) == False
    assert candidate(root = tree_node([10000, -10000, 20000, -20000, 30000, -30000, 40000])) == False
    assert candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1])) == False
    assert candidate(root = tree_node([1000, -500, -500, 250, 250, 250, 250, -125, -125, -125, -125, -125, -125, -125, -125, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == False
    assert candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40])) == False
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == False
    assert candidate(root = tree_node([5, 1, 1, None, 10, 2, 3, None, 10, 1, 1, None, None, 1, None])) == False
    assert candidate(root = tree_node([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])) == True
    assert candidate(root = tree_node([100, -50, -50, 25, 25, 25, 25, -12, -12, -12, -12, -12, -12, -12, -12])) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 8, 1, 4, 6, 9, 11, 13])) == False
    assert candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4, -4])) == False
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10])) == False
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == False
    assert candidate(root = tree_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == False
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == False
    assert candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3])) == False
    assert candidate(root = tree_node([1000, -1000, 1000, -1000, 1000, -1000, 1000])) == False
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, None, None, 14, 13, 13, None])) == False
    assert candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4])) == False
    assert candidate(root = tree_node([-1, 1, -1, 1, -1, 1, -1])) == False
    assert candidate(root = tree_node([0, 1, 1, -1, -1, -1, -1])) == True
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == False
    assert candidate(root = tree_node([7, 3, 14, None, None, 9, 10])) == False
    assert candidate(root = tree_node([5, 10, 10, None, None, 2, 3, 1, None, None, None, None, 1])) == False
    assert candidate(root = tree_node([1000, -500, 500, 250, -250, 250, -250, 125, -125, 125, -125, 125, -125, 125, -125])) == True
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, 17, 20])) == False
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 12, 13, 12, 13, 12, 13])) == False
    assert candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == False
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == True


