def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 9, 1, 4, 7, 10]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 9, 1, 4, 7, 10]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 11, 14, 17, 19]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 11, 14, 17, 19]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 6, 5, 4, 3, 2, 1]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 6, 5, 4, 3, 2, 1]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3]),k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3]),k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 11, 3, 6, 10, 12, 1, 5, 7, None, None, None, 8]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 11, 3, 6, 10, 12, 1, 5, 7, None, None, None, 8]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 1, 2, None, None, None, 3]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 1, 2, None, None, None, 3]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 27, 32, 38]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 27, 32, 38]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 19]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 19]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, 11, 14, 16, 19, 23, 28]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, 11, 14, 16, 19, 23, 28]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 28, 32, 40, 0, 3, 6, 8, 11, 13, 16, 19, 21, 23, 26, 29, 31, 33, 37, 39, 41]),k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 28, 32, 40, 0, 3, 6, 8, 11, 13, 16, 19, 21, 23, 26, 29, 31, 33, 37, 39, 41]),k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 12, 3, 7, 10, 14, 1, 4, 6, 8, 9, 11, 13, 15]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 12, 3, 7, 10, 14, 1, 4, 6, 8, 9, 11, 13, 15]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45]),k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45]),k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]),k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]),k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 7, 20, 3, 9, 18, 22, 2, 5, 8, 11, 17, 19, 21, 23, 1, 4, 6, None, None, None, None, None, 10, 12, 13, 14, 16, None, None, None, None, None, None, None, None]),k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 7, 20, 3, 9, 18, 22, 2, 5, 8, 11, 17, 19, 21, 23, 1, 4, 6, None, None, None, None, None, 10, 12, 13, 14, 16, None, None, None, None, None, None, None, None]),k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 5, 10, 3, 6, 8, 12, 2, 4, 9, 11, 13, 14]),k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 5, 10, 3, 6, 8, 12, 2, 4, 9, 11, 13, 14]),k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 13, 16, 19, 23, 27]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 13, 16, 19, 23, 27]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 11, 2, 5, 8, 13, 1, 4, 6, 9, 10, 12, 14, 15, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 11, 2, 5, 8, 13, 1, 4, 6, 9, 10, 12, 14, 15, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 56, 92, 6, 18, 29, 41, 52, 67, 85, 95, 3, 9, 15, 21, 26, 31, 35, 45, 53, 61, 70, 73, 80, 87, 90, 93, 98]),k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 56, 92, 6, 18, 29, 41, 52, 67, 85, 95, 3, 9, 15, 21, 26, 31, 35, 45, 53, 61, 70, 73, 80, 87, 90, 93, 98]),k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 8, 1, 5, 6, 10, 0, 2, None, None, None, None, None, 9, 11]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 8, 1, 5, 6, 10, 0, 2, None, None, None, None, None, 9, 11]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, 0, 2, 4, 6, 7, 9, 11, 13]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, 0, 2, 4, 6, 7, 9, 11, 13]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 1, 2, 3, 4, 5, 6, 7]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 1, 2, 3, 4, 5, 6, 7]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 10, 35, 5, 15, 28, 40, 1, 7, 12, 18, 23, 30, 36, 45]),k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 10, 35, 5, 15, 28, 40, 1, 7, 12, 18, 23, 30, 36, 45]),k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 8, 11, 13, 17, 19, 23]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 8, 11, 13, 17, 19, 23]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 15, 45, 75, 105, 10, 20, 40, 50, 70, 80, 100, 110]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 15, 45, 75, 105, 10, 20, 40, 50, 70, 80, 100, 110]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 2, 7, 11, 13, 16, 19, 22, 27]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 2, 7, 11, 13, 16, 19, 22, 27]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 3, 5, 6, 8, 10, 11]),k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 3, 5, 6, 8, 10, 11]),k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9]),k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9]),k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([80, 40, 120, 20, 60, 100, 140, 10, 30, 50, 70, 90, 110, 130, 150]),k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([80, 40, 120, 20, 60, 100, 140, 10, 30, 50, 70, 90, 110, 130, 150]),k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 27, 32, 37, 1, 4, 6, 8, 11, 13, 17, 19, 22, 24, 26, 28, 31, 33, 36, 38]),k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 27, 32, 37, 1, 4, 6, 8, 11, 13, 17, 19, 22, 24, 26, 28, 31, 33, 36, 38]),k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, 2, 6, 9, 11, 1, 3, 4, 7, 8, 12]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, 2, 6, 9, 11, 1, 3, 4, 7, 8, 12]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 3, 7, 12, 18, 28, 33, 37, 45]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 3, 7, 12, 18, 28, 33, 37, 45]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 12, 4, 6, 10, 14, 3, 7, 9, 11, 13, 15]),k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 12, 4, 6, 10, 14, 3, 7, 9, 11, 13, 15]),k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 15, 30, 40, 55, 65, 85, 100]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 15, 30, 40, 55, 65, 85, 100]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 7, 11, 13, 17, 19, 23]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 7, 11, 13, 17, 19, 23]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 11, 3, 6, 9, 12, 1, 4, 7, 8, 10, 11, 13, 14]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 11, 3, 6, 9, 12, 1, 4, 7, 8, 10, 11, 13, 14]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 20]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 20]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19, 0, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19, 0, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, 16, 18, 21, 23, 28, 32]),k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, 16, 18, 21, 23, 28, 32]),k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 11, 2, 5, 8, 13, 1, 4, 6, 9, 10, 12, 14, 15]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 11, 2, 5, 8, 13, 1, 4, 6, 9, 10, 12, 14, 15]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10, 12, 15, 18, 20]),k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10, 12, 15, 18, 20]),k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, 17, 25, 3, 7, 11, 13, 16, 19, 23, 27]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, 17, 25, 3, 7, 11, 13, 16, 19, 23, 27]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 6, 9, 12, 18, 22, 28, 33]),k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 6, 9, 12, 18, 22, 28, 33]),k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, None, 2, None, 5, None, None, None, None, None, None]),k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, None, 2, None, 5, None, None, None, None, None, None]),k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38]),k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38]),k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 5, 9, 11, 13, 14, 17, 18, 21, 23, 26, None, None, None, None, None, None, None, None, None, 19, 22, 24, None, None, None, 27]),k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 5, 9, 11, 13, 14, 17, 18, 21, 23, 26, None, None, None, None, None, None, None, None, None, 19, 22, 24, None, None, None, 27]),k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, 2, 5, 6, 7, 8, 9, 10, 11]),k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, 2, 5, 6, 7, 8, 9, 10, 11]),k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([17, 11, 23, 7, 13, 19, 27, 5, 9, 12, 15, 18, 21, 25, 29]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([17, 11, 23, 7, 13, 19, 27, 5, 9, 12, 15, 18, 21, 25, 29]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 180, 5, 15, 30, 45, 55, 65, 70, 85, 90, 105, 115, 130, 135, 145, 155, 165, 170, 185, 190, 200]),k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 180, 5, 15, 30, 45, 55, 65, 70, 85, 90, 105, 115, 130, 135, 145, 155, 165, 170, 185, 190, 200]),k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]),k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]),k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 33, 37]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 33, 37]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 15, 2, 6, 12, 18, 1, 3, 5, 7, 11, 13, 17, 19]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 15, 2, 6, 12, 18, 1, 3, 5, 7, 11, 13, 17, 19]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([11, 7, 19, 3, 9, 15, 23, 1, 5, 8, 10, 13, 17, 20, 25]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([11, 7, 19, 3, 9, 15, 23, 1, 5, 8, 10, 13, 17, 20, 25]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, 0, 2, 4, 6, 7, 11, 13, 14]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, 0, 2, 4, 6, 7, 11, 13, 14]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, -1, -1, -1, -1, -1, -1, 7, 8]),k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, -1, -1, -1, -1, -1, -1, 7, 8]),k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 1, 3, 7, 9, None, None, None, 5]),k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 1, 3, 7, 9, None, None, None, 5]),k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([14, 8, 20, 4, 10, 16, 24, 2, 6, 9, 12, 14, 18, 22, 26]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([14, 8, 20, 4, 10, 16, 24, 2, 6, 9, 12, 14, 18, 22, 26]),k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, None, 7, 8, 2, None, None, None, None, 9]),k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, None, 7, 8, 2, None, None, None, None, 9]),k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 48, 55]),k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 48, 55]),k = 4) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([5, 3, 9, 1, 4, 7, 10]),k = 2) == 1
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9]),k = 2) == 1
    assert candidate(root = tree_node([3, 2, 2]),k = 2) == 1
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9]),k = 2) == 1
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 2) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 11, 14, 17, 19]),k = 3) == 3
    assert candidate(root = tree_node([7, 6, 5, 4, 3, 2, 1]),k = 2) == 3
    assert candidate(root = tree_node([1, 2, 3]),k = 1) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 1) == 2
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),k = 3) == 3
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 2) == 2
    assert candidate(root = tree_node([1]),k = 1) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),k = 5) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19]),k = 3) == 3
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 3) == 1
    assert candidate(root = tree_node([9, 4, 11, 3, 6, 10, 12, 1, 5, 7, None, None, None, 8]),k = 2) == 3
    assert candidate(root = tree_node([3, 2, 3, 1, 2, None, None, None, 3]),k = 2) == 1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 27, 32, 38]),k = 4) == 1
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),k = 2) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 19]),k = 3) == 3
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, 11, 14, 16, 19, 23, 28]),k = 3) == 3
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 28, 32, 40, 0, 3, 6, 8, 11, 13, 16, 19, 21, 23, 26, 29, 31, 33, 37, 39, 41]),k = 8) == 1
    assert candidate(root = tree_node([8, 5, 12, 3, 7, 10, 14, 1, 4, 6, 8, 9, 11, 13, 15]),k = 4) == 1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37]),k = 5) == 1
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45]),k = 6) == 1
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]),k = 2) == 9
    assert candidate(root = tree_node([15, 7, 20, 3, 9, 18, 22, 2, 5, 8, 11, 17, 19, 21, 23, 1, 4, 6, None, None, None, None, None, 10, 12, 13, 14, 16, None, None, None, None, None, None, None, None]),k = 4) == 4
    assert candidate(root = tree_node([7, 5, 10, 3, 6, 8, 12, 2, 4, 9, 11, 13, 14]),k = 2) == 2
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 13, 16, 19, 23, 27]),k = 5) == 1
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 2) == 3
    assert candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 7) == 1
    assert candidate(root = tree_node([7, 3, 11, 2, 5, 8, 13, 1, 4, 6, 9, 10, 12, 14, 15, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),k = 3) == 2
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 56, 92, 6, 18, 29, 41, 52, 67, 85, 95, 3, 9, 15, 21, 26, 31, 35, 45, 53, 61, 70, 73, 80, 87, 90, 93, 98]),k = 10) == 1
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]),k = 5) == 1
    assert candidate(root = tree_node([7, 3, 8, 1, 5, 6, 10, 0, 2, None, None, None, None, None, 9, 11]),k = 4) == 1
    assert candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, 0, 2, 4, 6, 7, 9, 11, 13]),k = 2) == 3
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 1, 2, 3, 4, 5, 6, 7]),k = 2) == 3
    assert candidate(root = tree_node([25, 10, 35, 5, 15, 28, 40, 1, 7, 12, 18, 23, 30, 36, 45]),k = 6) == 1
    assert candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 8, 11, 13, 17, 19, 23]),k = 3) == 3
    assert candidate(root = tree_node([60, 30, 90, 15, 45, 75, 105, 10, 20, 40, 50, 70, 80, 100, 110]),k = 3) == 3
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 2, 7, 11, 13, 16, 19, 22, 27]),k = 5) == 1
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 3, 5, 6, 8, 10, 11]),k = 3) == 2
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9]),k = 2) == 2
    assert candidate(root = tree_node([80, 40, 120, 20, 60, 100, 140, 10, 30, 50, 70, 90, 110, 130, 150]),k = 8) == 0
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 27, 32, 37, 1, 4, 6, 8, 11, 13, 17, 19, 22, 24, 26, 28, 31, 33, 36, 38]),k = 5) == 3
    assert candidate(root = tree_node([8, 5, 10, 2, 6, 9, 11, 1, 3, 4, 7, 8, 12]),k = 2) == 3
    assert candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 3, 7, 12, 18, 28, 33, 37, 45]),k = 4) == 1
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),k = 2) == 0
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),k = 1) == 5
    assert candidate(root = tree_node([8, 5, 12, 4, 6, 10, 14, 3, 7, 9, 11, 13, 15]),k = 3) == 1
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),k = 2) == 0
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 15, 30, 40, 55, 65, 85, 100]),k = 4) == 1
    assert candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 7, 11, 13, 17, 19, 23]),k = 5) == 1
    assert candidate(root = tree_node([8, 5, 11, 3, 6, 9, 12, 1, 4, 7, 8, 10, 11, 13, 14]),k = 4) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 20]),k = 4) == 1
    assert candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 2) == 3
    assert candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),k = 3) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19, 0, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]),k = 5) == 2
    assert candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, 16, 18, 21, 23, 28, 32]),k = 6) == 1
    assert candidate(root = tree_node([7, 3, 11, 2, 5, 8, 13, 1, 4, 6, 9, 10, 12, 14, 15]),k = 4) == 1
    assert candidate(root = tree_node([5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10, 12, 15, 18, 20]),k = 3) == 1
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 17, 25, 3, 7, 11, 13, 16, 19, 23, 27]),k = 5) == 1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 6, 9, 12, 18, 22, 28, 33]),k = 5) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25]),k = 3) == 3
    assert candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, None, 2, None, 5, None, None, None, None, None, None]),k = 2) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38]),k = 4) == 3
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 5, 9, 11, 13, 14, 17, 18, 21, 23, 26, None, None, None, None, None, None, None, None, None, 19, 22, 24, None, None, None, 27]),k = 5) == 2
    assert candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, 2, 5, 6, 7, 8, 9, 10, 11]),k = 3) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20]),k = 3) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),k = 10) == 0
    assert candidate(root = tree_node([17, 11, 23, 7, 13, 19, 27, 5, 9, 12, 15, 18, 21, 25, 29]),k = 3) == 3
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),k = 1) == 0
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 180, 5, 15, 30, 45, 55, 65, 70, 85, 90, 105, 115, 130, 135, 145, 155, 165, 170, 185, 190, 200]),k = 5) == 4
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]),k = 3) == 0
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),k = 5) == 0
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 33, 37]),k = 2) == 3
    assert candidate(root = tree_node([9, 4, 15, 2, 6, 12, 18, 1, 3, 5, 7, 11, 13, 17, 19]),k = 2) == 3
    assert candidate(root = tree_node([11, 7, 19, 3, 9, 15, 23, 1, 5, 8, 10, 13, 17, 20, 25]),k = 4) == 1
    assert candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, 0, 2, 4, 6, 7, 11, 13, 14]),k = 4) == 1
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, -1, -1, -1, -1, -1, -1, 7, 8]),k = 2) == 6
    assert candidate(root = tree_node([6, 2, 8, 1, 3, 7, 9, None, None, None, 5]),k = 1) == 3
    assert candidate(root = tree_node([14, 8, 20, 4, 10, 16, 24, 2, 6, 9, 12, 14, 18, 22, 26]),k = 4) == 1
    assert candidate(root = tree_node([5, 4, 6, 3, None, 7, 8, 2, None, None, None, None, 9]),k = 2) == 2
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 48, 55]),k = 4) == 1


