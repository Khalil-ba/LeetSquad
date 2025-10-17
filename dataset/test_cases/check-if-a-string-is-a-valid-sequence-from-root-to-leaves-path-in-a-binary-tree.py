def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3]),arr = [1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3]),arr = [1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, None, 2, 1, 5, 4]),arr = [8, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, None, 2, 1, 5, 4]),arr = [8, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 2, 2, 5, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 2, 2, 5, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, None, 5, 2]),arr = [2, 2, 5, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, None, 5, 2]),arr = [2, 2, 5, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),arr = [9, 8, 6, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),arr = [9, 8, 6, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10]),arr = [1, 2, 3, 6, 8, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10]),arr = [1, 2, 3, 6, 8, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, 9, 9, None, 9, 9, 9, None, None, None, 9, None, None, None, None, None, None]),arr = [9, 9, 9, 9, 9, 9, 9, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, 9, 9, None, 9, 9, 9, None, None, None, 9, None, None, None, None, None, None]),arr = [9, 9, 9, 9, 9, 9, 9, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 4, 3, None, None, 6, 9]),arr = [7, 4, 3, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 4, 3, None, None, 6, 9]),arr = [7, 4, 3, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 8, 13]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 8, 13]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 6, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 6, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [0, 1, 2, 4, 8, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [0, 1, 2, 4, 8, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 2, 8, 10, 4, None, 9, None, None, 1, None, None, None, 6]),arr = [5, 3, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 2, 8, 10, 4, None, 9, None, None, 1, None, None, None, 6]),arr = [5, 3, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 2, 2, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 2, 2, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 3, None, 4, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, None, None, None, 14, 15]),arr = [5, 2, 4, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 3, None, 4, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, None, None, None, 14, 15]),arr = [5, 2, 4, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 0, 1, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 0, 1, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 5, 4, 3, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 5, 4, 3, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, None]),arr = [6, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, None]),arr = [6, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),arr = [5, 4, 11, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),arr = [5, 4, 11, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 14, 3, 2, None, -4, 10, None, None, -1]),arr = [9, 3, -4, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 14, 3, 2, None, -4, 10, None, None, -1]),arr = [9, 3, -4, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 14, 3, 2, None, -4, 10, None, None, -1]),arr = [9, 14, 2, -4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 14, 3, 2, None, -4, 10, None, None, -1]),arr = [9, 14, 2, -4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 10, 11, 9, 2, None, 10, 4, None, 8, 6, None, 3, None, None, None, 5]),arr = [7, 10, 9, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 10, 11, 9, 2, None, 10, 4, None, 8, 6, None, 3, None, None, None, 5]),arr = [7, 10, 9, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),arr = [5, 4, 11, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),arr = [5, 4, 11, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 3, 5, 0, 8, 1, 9, 6, 7, None, 2, None, None, None, 3, None, None, None, None]),arr = [4, 5, 1, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 3, 5, 0, 8, 1, 9, 6, 7, None, 2, None, None, None, 3, None, None, None, None]),arr = [4, 5, 1, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 8, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 8, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 0, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 0, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 4, 3, 3, None, 8, 6, None, 5, None, 9, None, 7]),arr = [2, 2, 4, 8, 9, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 4, 3, 3, None, 8, 6, None, 5, None, 9, None, 7]),arr = [2, 2, 4, 8, 9, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 4, 3, 3, None, 8, 6, None, 5, None, 9, None, 7]),arr = [2, 2, 5, 3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 4, 3, 3, None, 8, 6, None, 5, None, 9, None, 7]),arr = [2, 2, 5, 3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, 8, 6]),arr = [6, 2, 0, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, 8, 6]),arr = [6, 2, 0, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 1, None, 2]),arr = [0, 0, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 1, None, 2]),arr = [0, 0, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 2]),arr = [2, 2, 5, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 2]),arr = [2, 2, 5, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),arr = [1, 2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),arr = [1, 2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 1, 0, 1, None, 1, 0, 0, 1, None, None, None, None, None, None]),arr = [0, 1, 0, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 1, 0, 1, None, 1, 0, 0, 1, None, None, None, None, None, None]),arr = [0, 1, 0, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, None, 6, 7, 4, None, None, None, None, 8]),arr = [5, 1, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, None, 6, 7, 4, None, None, None, None, 8]),arr = [5, 1, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),arr = [5, 4, 11, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),arr = [5, 4, 11, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),arr = [1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),arr = [1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, 4]),arr = [1, 2, 3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, 4]),arr = [1, 2, 3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 2, 1, None, 2, None, 1, None, None, 2, 4]),arr = [3, 1, 2, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 2, 1, None, 2, None, 1, None, None, 2, 4]),arr = [3, 1, 2, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),arr = [1, 2, 3, 6, 8, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),arr = [1, 2, 3, 6, 8, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 8, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 8, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 4, 8, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 4, 8, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 10, 7, 6, 9, 5, 1, 12, 8, None, 6, None, 7, None, None, None, None, None, None, 5, None]),arr = [7, 10, 6, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 10, 7, 6, 9, 5, 1, 12, 8, None, 6, None, 7, None, None, None, None, None, None, 5, None]),arr = [7, 10, 6, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 1, 10, None, 6, None, 11, 5, None, None, 7, None, None, None, 12]),arr = [9, 1, 10, 11, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 1, 10, None, 6, None, 11, 5, None, None, 7, None, None, None, 12]),arr = [9, 1, 10, 11, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),arr = [5, 6, 8, 12, 20, 24]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),arr = [5, 6, 8, 12, 20, 24]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, None, 1, None, 1, 0, None, None, 1, 0, None, None, 1, None, None, None, 1, 0, None, None, None, None, None, 0, None, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, None, 1, None, 1, 0, None, None, 1, 0, None, None, 1, None, None, None, 1, 0, None, None, None, None, None, 0, None, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 10, 11, None, 2, None, 8, 9, 4, 3]),arr = [7, 10, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 10, 11, None, 2, None, 8, 9, 4, 3]),arr = [7, 10, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),arr = [2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),arr = [2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),arr = [1, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),arr = [1, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 2, 4, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 2, 4, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, 7, 8]),arr = [1, 2, 4, 6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, 7, 8]),arr = [1, 2, 4, 6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, 8, 9]),arr = [1, 3, 5, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, 8, 9]),arr = [1, 3, 5, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, None, 0, 0]),arr = [0, 1, 0, 1, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, None, 0, 0]),arr = [0, 1, 0, 1, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, 3, None, 7]),arr = [2, 5, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, 3, None, 7]),arr = [2, 5, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 7, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 7, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 5, None, None, 5, 7]),arr = [2, 2, 5, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 5, None, None, 5, 7]),arr = [2, 2, 5, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 3, 6, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 3, 6, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 10, 5, 3, 1, None, 2, None, 8, 6, None, 4, None, None, 1]),arr = [7, 10, 3, 1, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 10, 5, 3, 1, None, 2, None, 8, 6, None, 4, None, None, 1]),arr = [7, 10, 3, 1, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 1, None, 2]),arr = [0, 0, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 1, None, 2]),arr = [0, 0, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, None, 9, 9, None, 9, 9, None, None, 9, 9, 9]),arr = [9, 9, 9, 9, 9, 9, 9, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, None, 9, 9, None, 9, 9, None, None, 9, 9, 9]),arr = [9, 9, 9, 9, 9, 9, 9, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5]),arr = [1, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5]),arr = [1, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 1, 5, 3, None, None, None, 1, None, 5, None]),arr = [6, 1, 5, 3, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 1, 5, 3, None, None, None, 1, None, 5, None]),arr = [6, 1, 5, 3, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, 2, 2, None, None, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, 2, None, None, None, None, 2, None, 2, 2, None, None, 2, None, None, 2, 2, 2, None, 2, 2, 2, None, None, 2, 2, 2, None, 2, 2, None, 2, None, 2]),arr = [2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, 2, 2, None, None, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, 2, None, None, None, None, 2, None, 2, 2, None, None, 2, None, None, 2, 2, 2, None, 2, 2, 2, None, None, 2, 2, 2, None, 2, 2, None, 2, None, 2]),arr = [2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 2, 4, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 2, 4, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),arr = [0, 1, 0, 1, 0, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),arr = [0, 1, 0, 1, 0, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 3, 8, 4, 5, None, None, 10, 13, None, None, 7, 14, None, None, 12, 15]),arr = [6, 8, 13, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 3, 8, 4, 5, None, None, 10, 13, None, None, 7, 14, None, None, 12, 15]),arr = [6, 8, 13, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 6, 8, None, None, None, 9]),arr = [3, 20, 15, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 6, 8, None, None, None, 9]),arr = [3, 20, 15, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0]),arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0]),arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 7, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 7, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, 4]),arr = [1, 2, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, 4]),arr = [1, 2, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 4, 8]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 0, 1]) == False
    assert candidate(root = tree_node([1, 2, 3]),arr = [1, 2]) == True
    assert candidate(root = tree_node([8, 3, None, 2, 1, 5, 4]),arr = [8, 3, 2, 1]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 1]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 0, 1]) == True
    assert candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 2, 2, 5, 4]) == False
    assert candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2]) == False
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 1]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1]) == False
    assert candidate(root = tree_node([2, 2, 5, None, None, 5, 2]),arr = [2, 2, 5, 2]) == False
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),arr = [9, 8, 6, 2]) == True
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == False
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10]),arr = [1, 2, 3, 6, 8, 10]) == False
    assert candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2, 2]) == False
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, 9, 9, None, 9, 9, 9, None, None, None, 9, None, None, None, None, None, None]),arr = [9, 9, 9, 9, 9, 9, 9, 9]) == False
    assert candidate(root = tree_node([7, 4, 3, None, None, 6, 9]),arr = [7, 4, 3, 6]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]),arr = [0, 1, 0, 0, 1, 0]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 8, 13]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 6, 12]) == True
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [0, 1, 2, 4, 8, 16]) == False
    assert candidate(root = tree_node([5, 3, 2, 8, 10, 4, None, 9, None, None, 1, None, None, None, 6]),arr = [5, 3, 8, 9]) == False
    assert candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 2, 2, 1, 2]) == False
    assert candidate(root = tree_node([5, 2, 3, None, 4, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, None, None, None, 14, 15]),arr = [5, 2, 4, 10]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 7]) == True
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 0, 1, 0, 0, 0]) == False
    assert candidate(root = tree_node([2, 2, 5, None, 2, None, 4, 3, None, 1, None, 2, 5, None, None, None, 4]),arr = [2, 5, 4, 3, 1]) == False
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, None]),arr = [6, 8, 9]) == True
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),arr = [5, 4, 11, 2]) == True
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 1, 0, None, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(root = tree_node([9, 14, 3, 2, None, -4, 10, None, None, -1]),arr = [9, 3, -4, 1]) == False
    assert candidate(root = tree_node([9, 14, 3, 2, None, -4, 10, None, None, -1]),arr = [9, 14, 2, -4]) == False
    assert candidate(root = tree_node([7, 10, 11, 9, 2, None, 10, 4, None, 8, 6, None, 3, None, None, None, 5]),arr = [7, 10, 9, 4, 5]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),arr = [5, 4, 11, 7]) == True
    assert candidate(root = tree_node([4, 3, 5, 0, 8, 1, 9, 6, 7, None, 2, None, None, None, 3, None, None, None, None]),arr = [4, 5, 1, 3]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 8, 13]) == True
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 0, 1, 0, 1]) == False
    assert candidate(root = tree_node([2, 2, 5, None, 4, 3, 3, None, 8, 6, None, 5, None, 9, None, 7]),arr = [2, 2, 4, 8, 9, 7]) == False
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(root = tree_node([2, 2, 5, None, 4, 3, 3, None, 8, 6, None, 5, None, 9, None, 7]),arr = [2, 2, 5, 3, 3]) == False
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, 8, 6]),arr = [6, 2, 0, 3]) == False
    assert candidate(root = tree_node([0, 0, 1, None, 2]),arr = [0, 0, 1, 2]) == False
    assert candidate(root = tree_node([2, 2, 5, None, 2]),arr = [2, 2, 5, 2]) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),arr = [1, 2, 4]) == False
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1]),arr = [1, 0, 1]) == True
    assert candidate(root = tree_node([0, 1, 0, 1, 0, 1, None, 1, 0, 0, 1, None, None, None, None, None, None]),arr = [0, 1, 0, 1, 0, 1]) == False
    assert candidate(root = tree_node([5, 1, 2, 3, None, 6, 7, 4, None, None, None, None, 8]),arr = [5, 1, 3, 4]) == True
    assert candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),arr = [5, 4, 11, 7]) == True
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),arr = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 4]),arr = [1, 2, 3, 4]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 1]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 5, 10, 20]) == False
    assert candidate(root = tree_node([3, 1, 2, 1, None, 2, None, 1, None, None, 2, 4]),arr = [3, 1, 2, 1, 2]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2, 5]) == False
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),arr = [1, 2, 3, 6, 8, 10]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),arr = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 8, 4, 5]) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 4, 8, 16]) == False
    assert candidate(root = tree_node([7, 10, 7, 6, 9, 5, 1, 12, 8, None, 6, None, 7, None, None, None, None, None, None, 5, None]),arr = [7, 10, 6, 12]) == True
    assert candidate(root = tree_node([9, 1, 10, None, 6, None, 11, 5, None, None, 7, None, None, None, 12]),arr = [9, 1, 10, 11, 12]) == False
    assert candidate(root = tree_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),arr = [5, 6, 8, 12, 20, 24]) == False
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, None, 1, None, 1, 0, None, None, 1, 0, None, None, 1, None, None, None, 1, 0, None, None, None, None, None, 0, None, 1]),arr = [1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(root = tree_node([7, 10, 11, None, 2, None, 8, 9, 4, 3]),arr = [7, 10, 2, 4]) == True
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),arr = [2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),arr = [1, 3, 5]) == True
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 2, 4, 8, 9]) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, 7, 8]),arr = [1, 2, 4, 6, 7]) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, 8, 9]),arr = [1, 3, 5, 9]) == True
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, None, 0, 0]),arr = [0, 1, 0, 1, 0, 0]) == False
    assert candidate(root = tree_node([2, 2, 2, 2, None, 2, 2]),arr = [2, 2, 2, 2, 2, 2]) == False
    assert candidate(root = tree_node([2, 2, 5, None, 3, None, 7]),arr = [2, 5, 7]) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 7, 14]) == True
    assert candidate(root = tree_node([2, 2, 5, None, None, 5, 7]),arr = [2, 2, 5, 7]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 3, 6, 10]) == False
    assert candidate(root = tree_node([7, 10, 5, 3, 1, None, 2, None, 8, 6, None, 4, None, None, 1]),arr = [7, 10, 3, 1, 8]) == False
    assert candidate(root = tree_node([0, 0, 1, None, 2]),arr = [0, 0, 2]) == True
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, None, 9, 9, None, 9, 9, None, None, 9, 9, 9]),arr = [9, 9, 9, 9, 9, 9, 9, 9]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5]),arr = [1, 3, 5]) == True
    assert candidate(root = tree_node([6, 1, 5, 3, None, None, None, 1, None, 5, None]),arr = [6, 1, 5, 3, 5]) == False
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, 2, 2, None, None, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, 2, None, None, None, None, 2, None, 2, 2, None, None, 2, None, None, 2, 2, 2, None, 2, 2, 2, None, None, 2, 2, 2, None, 2, 2, None, 2, None, 2]),arr = [2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, None, None, None, 10]),arr = [1, 2, 4, 7]) == False
    assert candidate(root = tree_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),arr = [0, 1, 0, 1, 0, 1, 0, 1]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2, 1]) == False
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),arr = [5, 4, 11, 2]) == True
    assert candidate(root = tree_node([6, 3, 8, 4, 5, None, None, 10, 13, None, None, 7, 14, None, None, 12, 15]),arr = [6, 8, 13, 12]) == False
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 6, 8, None, None, None, 9]),arr = [3, 20, 15, 6]) == False
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0]),arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 3, 7, 15]) == True
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 4]),arr = [1, 2, 5]) == True
    assert candidate(root = tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, 0, 0, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None, None, None, 0]),arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),arr = [1, 2, 4, 8]) == True


