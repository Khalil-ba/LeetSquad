def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, None, None, 3, 7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, None, None, 3, 7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, 3, 2, 6, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, 3, 2, 6, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2147483647])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2147483647])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([32, 26, 47, 19, None, None, 56, None, 27])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([32, 26, 47, 19, None, None, 56, None, 27])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, None, None, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, None, None, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, 1, None, None, 6, 0, None, None, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, 1, None, None, 6, 0, None, None, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, None, 1.5, 2.5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, None, 1.5, 2.5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 1, 4, 6, 9, None, None, None, None, None, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 1, 4, 6, 9, None, None, None, None, None, 10])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, None, 6, 8, 15, None, None, 7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, None, 6, 8, 15, None, None, 7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 7, 10, None, None, 8, None, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 7, 10, None, None, 8, None, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 5, None, None, 4, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 5, None, None, 4, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, 9])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, 9])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, None, 30, 10, None, None, 15, None, 45])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, None, 30, 10, None, None, 15, None, 45])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, None, 20, 15, 30, None, None, 12, 17])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, None, 20, 15, 30, None, None, 12, 17])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 7, None, 20, None, None, 6, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 7, None, 20, None, None, 6, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, None, 1.5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, None, 1.5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 5, None, None, 5, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 5, None, None, 5, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, None, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, None, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 60, 10, 25, 55, 70, 5, 15, 22, 30, 52, 65, 67, 80])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 60, 10, 25, 55, 70, 5, 15, 22, 30, 52, 65, 67, 80])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, None, 4, None, 5, None, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, None, 4, None, 5, None, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 15, 1, 7, None, 18, None, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 15, 1, 7, None, 18, None, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 15, 1, 7, 10, 18, None, None, None, 8])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 15, 1, 7, 10, 18, None, None, None, 8])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([32, 26, 40, 17, 27, None, 45, None, None, None, 29, 30])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([32, 26, 40, 17, 27, None, 45, None, None, None, 29, 30])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 7, 14, 3, 9, 13, 15, None, None, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 7, 14, 3, 9, 13, 15, None, None, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90, None, None, 25, 45, 65, 75, None, None, None, None, 42])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90, None, None, 25, 45, 65, 75, None, None, None, None, 42])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 10, None, None, None, 11])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 10, None, None, None, 11])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 6, None, None, 3, 7, None, None, None, 8])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 6, None, None, 3, 7, None, None, None, 8])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2147483646, 2147483647])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2147483646, 2147483647])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, None, None, 60, 200])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, None, None, 60, 200])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 7, 14, 3, 9, 13, 20, 1, 5, 8, 11, 12, 17, 16, 18])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 7, 14, 3, 9, 13, 20, 1, 5, 8, 11, 12, 17, 16, 18])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 0, 5, None, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 0, 5, None, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, None, None, 3, 7, 2, None, None, None, 4, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, None, None, 3, 7, 2, None, None, None, 4, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, None, None, None, 16])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, None, None, None, 16])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, None, 20])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, None, 20])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, None, 3, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, None, 3, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([32, 26, 40, 18, 28, 36, 48, 13, 19, 27, 31, 34, 43, 49, 52, None, 14, None, None, 24, 29, None, None, 32, None, 35, 41, 44, 46, 47, 50, None, None, 51])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([32, 26, 40, 18, 28, 36, 48, 13, 19, 27, 31, 34, 43, 49, 52, None, 14, None, None, 24, 29, None, None, 32, None, 35, 41, 44, 46, 47, 50, None, None, 51])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, None, None, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, None, None, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 14, None, None, 10, 20, 8, 15, 11, 19])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 14, None, None, 10, 20, 8, 15, 11, 19])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 11, 13])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 11, 13])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 7, 14, 3, 9, 13, 18, 1, None, 8, None, 11, 15, None, 17])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 7, 14, 3, 9, 13, 18, 1, None, 8, None, 11, 15, None, 17])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 2, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 2, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([120, 70, 140, 50, 100, 130, 160, 20, 60, 80, 110, 125, 150, 180, 200])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([120, 70, 140, 50, 100, 130, 160, 20, 60, 80, 110, 125, 150, 180, 200])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6, 2, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6, 2, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([32, 26, 40, 19, 27, None, 44, None, None, None, None, None, 42])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([32, 26, 40, 19, 27, None, 44, None, None, None, None, None, 42])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, None, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, None, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, None, None, 3, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, None, None, 3, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 5, 18, 2, 9, 15, 19, 1, 3, 7, 11, 14, 17, 20])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 5, 18, 2, 9, 15, 19, 1, 3, 7, 11, 14, 17, 20])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 8, None, 4, 7, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 8, None, 4, 7, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, None, 6, 9, 11])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, None, 6, 9, 11])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, 9])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, 9])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 5, None, 7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 5, None, 7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 0, 2, None, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 0, 2, None, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, 3, 3])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, 3, 3])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 3, None, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 3, None, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, None, None, None, 13, 18])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, None, None, None, 13, 18])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 12, 20])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 12, 20])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, None, 2, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, None, 2, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2147483647, 2147483647])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2147483647, 2147483647])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, None, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, None, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90, None, None, 25, 45, 65, 75, None, None, None, None, 41])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90, None, None, 25, 45, 65, 75, None, None, None, None, 41])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, None, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, None, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, None, None, 7, 2, None, None, None, None, 8])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, None, None, 7, 2, None, None, None, None, 8])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 7, None, 18])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 7, None, 18])) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, None, 1])) == False
    assert candidate(root = tree_node([5, 4, 6, None, None, 3, 7])) == False
    assert candidate(root = tree_node([0, -1])) == True
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == False
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == True
    assert candidate(root = tree_node([3, 1, 4, 3, 2, 6, 5])) == False
    assert candidate(root = tree_node([2, 2, 2])) == False
    assert candidate(root = tree_node([2, None, 1])) == False
    assert candidate(root = tree_node([1, 2])) == False
    assert candidate(root = tree_node([2147483647])) == True
    assert candidate(root = tree_node([1, None, 2])) == True
    assert candidate(root = tree_node([2, 1, 3])) == True
    assert candidate(root = tree_node([32, 26, 47, 19, None, None, 56, None, 27])) == False
    assert candidate(root = tree_node([1, None, 2, 3])) == False
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7])) == True
    assert candidate(root = tree_node([1])) == True
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == False
    assert candidate(root = tree_node([5, 4, 6, 3, None, None, 7])) == True
    assert candidate(root = tree_node([3, 2, 5, 1, None, None, 6, 0, None, None, 4])) == False
    assert candidate(root = tree_node([1, 0, 2, None, None, 1.5, 2.5])) == True
    assert candidate(root = tree_node([5, 3, 7, 1, 4, 6, 9, None, None, None, None, None, 10])) == False
    assert candidate(root = tree_node([8, 5, 10, None, 6, 8, 15, None, None, 7])) == False
    assert candidate(root = tree_node([9, 7, 10, None, None, 8, None, 6])) == False
    assert candidate(root = tree_node([5, 1, 5, None, None, 4, 6])) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == True
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, 9])) == False
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == True
    assert candidate(root = tree_node([3, None, 30, 10, None, None, 15, None, 45])) == False
    assert candidate(root = tree_node([10, None, 20, 15, 30, None, None, 12, 17])) == False
    assert candidate(root = tree_node([2, 1, 3, None, None, 2])) == False
    assert candidate(root = tree_node([10, 5, 15, 1, 7, None, 20, None, None, 6, 8])) == True
    assert candidate(root = tree_node([1, 0, 2, None, None, 1.5])) == True
    assert candidate(root = tree_node([5, 1, 5, None, None, 5, 5])) == False
    assert candidate(root = tree_node([5, 3, 7, 2, 4, None, 8])) == True
    assert candidate(root = tree_node([50, 20, 60, 10, 25, 55, 70, 5, 15, 22, 30, 52, 65, 67, 80])) == False
    assert candidate(root = tree_node([2, None, 3, None, 4, None, 5, None, 6])) == True
    assert candidate(root = tree_node([8, 5, 15, 1, 7, None, 18, None, 6])) == False
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])) == False
    assert candidate(root = tree_node([8, 5, 15, 1, 7, 10, 18, None, None, None, 8])) == False
    assert candidate(root = tree_node([32, 26, 40, 17, 27, None, 45, None, None, None, 29, 30])) == False
    assert candidate(root = tree_node([12, 7, 14, 3, 9, 13, 15, None, None, 8])) == True
    assert candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90, None, None, 25, 45, 65, 75, None, None, None, None, 42])) == False
    assert candidate(root = tree_node([9, 4, 10, None, None, None, 11])) == True
    assert candidate(root = tree_node([5, 1, 6, None, None, 3, 7, None, None, None, 8])) == False
    assert candidate(root = tree_node([2147483646, 2147483647])) == False
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2])) == False
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == True
    assert candidate(root = tree_node([100, 50, 150, None, None, 60, 200])) == False
    assert candidate(root = tree_node([12, 7, 14, 3, 9, 13, 20, 1, 5, 8, 11, 12, 17, 16, 18])) == False
    assert candidate(root = tree_node([2, 1, 3, 0, 5, None, 4])) == False
    assert candidate(root = tree_node([5, 4, 6, None, None, 3, 7, 2, None, None, None, 4, None])) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, None, None, None, 16])) == True
    assert candidate(root = tree_node([7, 3, 15, None, None, None, 20])) == True
    assert candidate(root = tree_node([1, 0, 2, None, None, 3, None])) == False
    assert candidate(root = tree_node([32, 26, 40, 18, 28, 36, 48, 13, 19, 27, 31, 34, 43, 49, 52, None, 14, None, None, 24, 29, None, None, 32, None, 35, 41, 44, 46, 47, 50, None, None, 51])) == False
    assert candidate(root = tree_node([2, None, 3, None, None, 4])) == True
    assert candidate(root = tree_node([5, 2, 14, None, None, 10, 20, 8, 15, 11, 19])) == False
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 11, 13])) == True
    assert candidate(root = tree_node([12, 7, 14, 3, 9, 13, 18, 1, None, 8, None, 11, 15, None, 17])) == False
    assert candidate(root = tree_node([2, 1, 3, None, None, 2, 4])) == False
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == True
    assert candidate(root = tree_node([120, 70, 140, 50, 100, 130, 160, 20, 60, 80, 110, 125, 150, 180, 200])) == False
    assert candidate(root = tree_node([1, 1, None, 1])) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == False
    assert candidate(root = tree_node([1, 1])) == False
    assert candidate(root = tree_node([1, 0, 2])) == True
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6, 2, 2])) == False
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == True
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == True
    assert candidate(root = tree_node([32, 26, 40, 19, 27, None, 44, None, None, None, None, None, 42])) == False
    assert candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90])) == True
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4])) == True
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1])) == False
    assert candidate(root = tree_node([5, 1, 4, None, None, None, 6])) == False
    assert candidate(root = tree_node([3, 2, 4, None, None, 3, None])) == False
    assert candidate(root = tree_node([12, 5, 18, 2, 9, 15, 19, 1, 3, 7, 11, 14, 17, 20])) == False
    assert candidate(root = tree_node([5, 1, 8, None, 4, 7, 9])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([8, 5, 10, None, 6, 9, 11])) == True
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, 9])) == False
    assert candidate(root = tree_node([5, 1, 5, None, 7])) == False
    assert candidate(root = tree_node([2, 1, 3, 0, 2, None, 4])) == False
    assert candidate(root = tree_node([3, 1, 4, 3, 3])) == False
    assert candidate(root = tree_node([5, 2, 8, 1, 3, None, 9])) == True
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, None, None, None, 13, 18])) == True
    assert candidate(root = tree_node([10, 5, 15, None, None, 12, 20])) == True
    assert candidate(root = tree_node([3, 1, 4, None, None, 2, 6])) == False
    assert candidate(root = tree_node([2147483647, 2147483647])) == False
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == True
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, None, 9])) == True
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90])) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5])) == False
    assert candidate(root = tree_node([50, 30, 80, 20, 40, 70, 90, None, None, 25, 45, 65, 75, None, None, None, None, 41])) == False
    assert candidate(root = tree_node([1, None, 3, None, 2])) == False
    assert candidate(root = tree_node([5, 4, 6, 3, None, None, 7, 2, None, None, None, None, 8])) == False
    assert candidate(root = tree_node([10, 5, 15, 1, 7, None, 18])) == True


