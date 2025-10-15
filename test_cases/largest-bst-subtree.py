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
        result = candidate(root = tree_node([5, 4, 6, None, None, 3, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, None, None, 3, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, None, 2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, None, 2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, None, None, 7, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, None, None, 7, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 20, 5, 15, None, None, None, None, 13, 18])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 20, 5, 15, None, None, None, None, 13, 18])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, 0, 10, None, None, 35, 50, 65, 75])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, 0, 10, None, None, 35, 50, 65, 75])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, None, 3, 7, 12, 18, None, None, None, None, None, 25, 27, 35, 40, None, None, None, None, None, None, None, None, None, None, 22])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, None, 3, 7, 12, 18, None, None, None, None, None, 25, 27, 35, 40, None, None, None, None, None, None, None, None, None, None, 22])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 7, 18, 0, 6, None, None, 3, 9, None, None, None, None, 2])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 7, 18, 0, 6, None, None, 3, 9, None, None, None, None, 2])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 10, 60, 5, 20, 55, 70, 2, 8, None, 30, None, 51, 65, 75])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 10, 60, 5, 20, 55, 70, 2, 8, None, 30, None, 51, 65, 75])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 50, 5, 20, 45, 60, 1, None, 15, 25, 40, 48, 55, 70])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 50, 5, 20, 45, 60, 1, None, 15, 25, 40, 48, 55, 70])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, 9])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, 9])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, None, 14, 18, 25, None, 9])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, None, 14, 18, 25, None, 9])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, None, 14, 18, 25])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, None, 14, 18, 25])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, 2, None, 7, None, 25, 38, None, None, 32, 40, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, 2, None, 7, None, 25, 38, None, None, 32, 40, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, None, None, 10, 25, None, None, 35, 47, 65, 80, 1, None, None, None, None, None, None, None, None, None, 62, 67])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, None, None, 10, 25, None, None, 35, 47, 65, 80, 1, None, None, None, None, None, None, None, None, None, 62, 67])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, None, None, 11, 14, None, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, None, None, 11, 14, None, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, None, 6, 20])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, None, 6, 20])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 3, 7, None, None, 11, 17, 25, None, None, None, None, None, None, None, 2, 4, 6, None, None, 9, 13, 16, 19, 21, 24, None, None, None, None, None, None, 14, None, 18, 22, 23, None, None, None, None, None, None, 26, None, None, None, None, None, None, None, None, None, None, None])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 3, 7, None, None, 11, 17, 25, None, None, None, None, None, None, None, 2, 4, 6, None, None, 9, 13, 16, 19, 21, 24, None, None, None, None, None, None, 14, None, 18, 22, 23, None, None, None, None, None, None, 26, None, None, None, None, None, None, None, None, None, None, None])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 8.5, 12, 11, 13, 10.5, 10.7, 10.6, 10.8, 10.9, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 8.5, 12, 11, 13, 10.5, 10.7, 10.6, 10.8, 10.9, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, None, None, 4, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, None, None, 4, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 11, 14, 16, 19])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 11, 14, 16, 19])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, None, 4, 1, 7, None, None, None, None, None, 6, 8, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, None, 4, 1, 7, None, None, None, None, None, 6, 8, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 7, 16, 0, 4, 6, 9, 14, 17, None, None, None, None, None, None, None, None, 13, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 7, 16, 0, 4, 6, 9, 14, 17, None, None, None, None, None, None, None, None, 13, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, 1, None, None, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, 1, None, None, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 15, 35, 52, 65, 68, 75, 72, 73, 74, 76, 77])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 15, 35, 52, 65, 68, 75, 72, 73, 74, 76, 77])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, None, 70, None, None, 15, 35])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, None, 70, None, None, 15, 35])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 15, 35, 52, 65, 68, 75])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 15, 35, 52, 65, 68, 75])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 20, 40, 55, 70, 15, None, None, None, None, 65, 80, 52])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 20, 40, 55, 70, 15, None, None, None, None, 65, 80, 52])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 3, None, 9, None, 16, None, None, None, 2, None, None, None, None, 17, None, None, None, 18])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 3, None, 9, None, 16, None, None, None, 2, None, None, None, None, 17, None, None, None, 18])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 12, None, None, None, None, None, None, None, 11, 13, 14])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 12, None, None, None, None, None, None, None, 11, 13, 14])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, 1, None, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, 1, None, None, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, None, 14, None, 25, None, 9])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, None, 14, None, 25, None, 9])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 7, 20])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 7, 20])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 20, 0, None, None, 9, 16, 25])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 20, 0, None, None, 9, 16, 25])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 12, None, None, None, None, None, None, None, 11])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 12, None, None, None, None, None, None, None, 11])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 6, 9, 11, 13, 14, 17, 22, 27])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 6, 9, 11, 13, 14, 17, 22, 27])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, None, None, None, 6])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, None, None, None, 6])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 2, 6, 9])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 2, 6, 9])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 20, None, None, None, 16])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 20, None, None, None, 16])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 4, None, None, 6])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 4, None, None, 6])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 33, 37])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 33, 37])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 7, 9, 11, 13, 14, 18, 19, 23])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 7, 9, 11, 13, 14, 18, 19, 23])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, 16])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, 16])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 20, 50, 10, 25, 40, 60, 5, 15, None, None, 35, 45, 55, 65, 1, None, 12, 18, 23, 28, 32, 37, None, None, None, None, None, 43, 48, None, 53, 58, None, None, None, None, None, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 20, 50, 10, 25, 40, 60, 5, 15, None, None, 35, 45, 55, 65, 1, None, 12, 18, 23, 28, 32, 37, None, None, None, None, None, 43, 48, None, 53, 58, None, None, None, None, None, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 32, 37])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 32, 37])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, None, 2, None, None, None, 5, 6, 7, 8, 9, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, None, 2, None, None, None, 5, 6, 7, 8, 9, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 11, 14, 16, 19])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 11, 14, 16, 19])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 2, 4])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 2, 4])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 3, 7, 10, 0, None, 2.5, 4, 6, 9, None, None, None, None, None, 15, 12, 13, None, None, 11])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 3, 7, 10, 0, None, 2.5, 4, 6, 9, None, None, None, None, None, 15, 12, 13, None, None, 11])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, 6, 9, 11, 13, 18, 25])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, 6, 9, 11, 13, 18, 25])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, None, None, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, None, None, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37, 1, 4, 6, 8, 11, 13, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 34, 36, 38])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37, 1, 4, 6, 8, 11, 13, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 34, 36, 38])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 10, 25, None, 65, 80])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 10, 25, None, 65, 80])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, 7, None, 18, 22, 27, 32, 40])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, 7, None, 18, 22, 27, 32, 40])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 4, 9, 11, 13, 14, 17, 22, 27, 2, 6, None, 10, None, None, None, None, 18, 21, 24, 26, 28, 30, None, None, 5, 7, None, None, 19, None, 23, None, 29, None, None, None, None, 3, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 4, 9, 11, 13, 14, 17, 22, 27, 2, 6, None, 10, None, None, None, None, 18, 21, 24, 26, 28, 30, None, None, 5, 7, None, None, 19, None, 23, None, 29, None, None, None, None, 3, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, None, 6, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, None, 6, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90, 5, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, 32, None, None, 44, None, None, None, 48, None, None, None, 52, None, None, None, None, 62, None, None, None, None, 68, None, None, None, None, None, None, 72, None, None, None, None, None, None, 78, None, None, None, None, 85, None, None, None, 95, None])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90, 5, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, 32, None, None, 44, None, None, None, 48, None, None, None, 52, None, None, None, None, 62, None, None, None, None, 68, None, None, None, None, None, None, 72, None, None, None, None, None, None, 78, None, None, None, None, 85, None, None, None, 95, None])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 8, 12, 16, 25, 35, 48, 7, 9, 11, 13, 18, 22, 24, 33, 37, 42, 46, 6, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 8, 12, 16, 25, 35, 48, 7, 9, 11, 13, 18, 22, 24, 33, 37, 42, 46, 6, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 17, 35, 43, 48, 55, None, 8, 13, 16, None, None, 33, 38, None, 47, None, 53, 57, None, None, None, None, None, None, None, None, None])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 17, 35, 43, 48, 55, None, 8, 13, 16, None, None, 33, 38, None, 47, None, 53, 57, None, None, None, None, None, None, None, None, None])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, None, None, 11, 14, None, 7, 2, 9, 3, 6, 13, 17, 21, 16, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, None, None, 11, 14, None, 7, 2, 9, 3, 6, 13, 17, 21, 16, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 60, 5, 15, None, None, 3, 7, 12, 18])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 60, 5, 15, None, None, 3, 7, 12, 18])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, None, 9, None, 16, 18, 25, None, 17, None, 19, None, None, None, 13])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, None, 9, None, 16, 18, 25, None, 17, None, 19, None, None, None, 13])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, None, 20, None, None])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, None, 20, None, None])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, -2, 6, -3, -1, None, 8])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, -2, 6, -3, -1, None, 8])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 13, 18, 25])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 13, 18, 25])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 35, 60, 90, 110, 140, 180, 250])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 35, 60, 90, 110, 140, 180, 250])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 3, None, 9, None, 16, None, None, None, 2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 3, None, 9, None, 16, None, None, None, 2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, None, 3, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, None, 3, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 9, None, None, 6, 3, None])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 9, None, None, 6, 3, None])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 11, 14, 17, 20])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 11, 14, 17, 20])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 40, 60, 80, 125, 175, 250, 350])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 40, 60, 80, 125, 175, 250, 350])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 6, None, None, 3, 9, None, None, None, None, 2])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 6, None, None, 3, 9, None, None, None, None, 2])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 35, 50, 5, 12, 18, 25, 40, 48, 55, 60])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 35, 50, 5, 12, 18, 25, 40, 48, 55, 60])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, -2, 6, None, 3, 5, 8])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, -2, 6, None, 3, 5, 8])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 8.5, 12, None, None, None, None, None, None, 11, None, None, None, None, None, 13])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 8.5, 12, None, None, None, None, None, None, 11, None, None, None, None, None, 13])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, 16, 17, None, None, 18, 19, 20])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, 16, 17, None, None, 18, 19, 20])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 60, 5, 20, 45, 70, 3, 7, 18, 25, 40, 50, 65, 80, 1, 4, 6, 9, 17, 22, 35, 43, 55, 62, 75, 85, None, None, None, None, None, None, None, None, 10, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 11])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 60, 5, 20, 45, 70, 3, 7, 18, 25, 40, 50, 65, 80, 1, 4, 6, 9, 17, 22, 35, 43, 55, 62, 75, 85, None, None, None, None, None, None, None, None, 10, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 11])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, 1, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, 1, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, None, 3])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, None, 3])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, None, 6])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, None, 6])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, None, 4, None, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, None, 4, None, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, None, None, None, 9, 16, 14, 17, None, None, None, None, None, None, None, None, 18, None, None, None, None, None, 19, 20, 21, 22, 23, 24, 25])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, None, None, None, 9, 16, 14, 17, None, None, None, None, None, None, None, None, 18, None, None, None, None, None, 19, 20, 21, 22, 23, 24, 25])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 9, 2, 4, 7, 11, None, None, None, None, 6, 8, 10, 12])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 9, 2, 4, 7, 11, None, None, None, None, 6, 8, 10, 12])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 1, 7, 12, 18, 35, 45, 55, 65, 0, 4, 8, 11, 13, 17, 19, 33, 36, 44, 46, 54, 56, 64, 66])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 1, 7, 12, 18, 35, 45, 55, 65, 0, 4, 8, 11, 13, 17, 19, 33, 36, 44, 46, 54, 56, 64, 66])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 10, 55, None, 80, 5, None, 45, 58, None, 90])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 10, 55, None, 80, 5, None, 45, 58, None, 90])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, 6, None, None, None, None, None, None, None, None, 10])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, 6, None, None, None, None, None, None, None, None, 10])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, 5, 7, 1, None, None, None, None, None, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, 5, 7, 1, None, None, None, None, None, None, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, None, None, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, None, None, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, 12, 9, 14])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, 12, 9, 14])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, 1, None, 4, 6])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, 1, None, 4, 6])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, None, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, None, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 3, 7, 12, 18, 35, 45, 55, 65])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 3, 7, 12, 18, 35, 45, 55, 65])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 5, None, 3, None, 9, 10, None, None, None, 8, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 5, None, 3, None, 9, 10, None, None, None, 8, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, None, 10, None, 11])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, None, 10, None, 11])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 7, 20, 0, 6, None, None, 9, 16, 14, 17])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 7, 20, 0, 6, None, None, 9, 16, 14, 17])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 30, 60, 80, 110, 140, 180, 220])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 30, 60, 80, 110, 140, 180, 220])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 16, 25, 11, 14, 17, 22, None, None, None, None, None, None, None, None, None, None, None, 21, 24, 27, 18, 19, 23, 26, 30, 28, 29, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 16, 25, 11, 14, 17, 22, None, None, None, None, None, None, None, None, None, None, None, 21, 24, 27, 18, 19, 23, 26, 30, 28, 29, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, None, None, 10, 25, 40, 55, 65, 80])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, None, None, 10, 25, 40, 55, 65, 80])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 11, 14, 18, 25])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 11, 14, 18, 25])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, 1, None, 1, None, None, None, None, None, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, 1, None, 1, None, None, None, None, None, None, None])) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 1
    assert candidate(root = tree_node([5, 4, 6, None, None, 3, 7])) == 3
    assert candidate(root = tree_node([3, 1, 4, None, None, 2])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7])) == 3
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 3
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 7
    assert candidate(root = tree_node([4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1])) == 2
    assert candidate(root = tree_node([])) == 0
    assert candidate(root = tree_node([3, 2, 1])) == 1
    assert candidate(root = tree_node([5, 4, 6, None, None, 7, 8])) == 1
    assert candidate(root = tree_node([2, 1, 3])) == 3
    assert candidate(root = tree_node([30, 10, 20, 5, 15, None, None, None, None, 13, 18])) == 5
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3])) == 3
    assert candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, 0, 10, None, None, 35, 50, 65, 75])) == 7
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, None, 3, 7, 12, 18, None, None, None, None, None, 25, 27, 35, 40, None, None, None, None, None, None, None, None, None, None, 22])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 7, 18, 0, 6, None, None, 3, 9, None, None, None, None, 2])) == 5
    assert candidate(root = tree_node([50, 10, 60, 5, 20, 55, 70, 2, 8, None, 30, None, 51, 65, 75])) == 6
    assert candidate(root = tree_node([30, 10, 50, 5, 20, 45, 60, 1, None, 15, 25, 40, 48, 55, 70])) == 14
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, 9])) == 7
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, None, 14, 18, 25, None, 9])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, None, 14, 18, 25])) == 12
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, 2, None, 7, None, 25, 38, None, None, 32, 40, None, None, None, None])) == 3
    assert candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, None, None, 10, 25, None, None, 35, 47, 65, 80, 1, None, None, None, None, None, None, None, None, None, 62, 67])) == 1
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 1
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, None, None, 11, 14, None, 7])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == 8
    assert candidate(root = tree_node([10, 5, 15, 1, None, 6, 20])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 3, 7, None, None, 11, 17, 25, None, None, None, None, None, None, None, 2, 4, 6, None, None, 9, 13, 16, 19, 21, 24, None, None, None, None, None, None, 14, None, 18, 22, 23, None, None, None, None, None, None, 26, None, None, None, None, None, None, None, None, None, None, None])) == 6
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 8.5, 12, 11, 13, 10.5, 10.7, 10.6, 10.8, 10.9, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9])) == 1
    assert candidate(root = tree_node([3, 2, 5, None, None, 4, 6])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 11, 14, 16, 19])) == 14
    assert candidate(root = tree_node([3, 2, 5, None, 4, 1, 7, None, None, None, None, None, 6, 8, 9])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 7, 16, 0, 4, 6, 9, 14, 17, None, None, None, None, None, None, None, None, 13, None, None, None, None])) == 3
    assert candidate(root = tree_node([3, 2, 4, 1, None, None, 5])) == 5
    assert candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 15, 35, 52, 65, 68, 75, 72, 73, 74, 76, 77])) == 3
    assert candidate(root = tree_node([50, 30, 60, 5, 20, None, 70, None, None, 15, 35])) == 3
    assert candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 15, 35, 52, 65, 68, 75])) == 3
    assert candidate(root = tree_node([50, 30, 60, 20, 40, 55, 70, 15, None, None, None, None, 65, 80, 52])) == 4
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 3, None, 9, None, 16, None, None, None, 2, None, None, None, None, 17, None, None, None, 18])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 12, None, None, None, None, None, None, None, 11, 13, 14])) == 8
    assert candidate(root = tree_node([3, 2, 4, 1, None, None, None])) == 4
    assert candidate(root = tree_node([1, 2, None, 3])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, None, 14, None, 25, None, 9])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 7, 20])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 20, 0, None, None, 9, 16, 25])) == 10
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 3, 12, None, None, None, None, None, None, None, 11])) == 8
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 6, 9, 11, 13, 14, 17, 22, 27])) == 7
    assert candidate(root = tree_node([5, 4, 6, 3, 7])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, None, None, None, 6])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 2, 6, 9])) == 7
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 20, None, None, None, 16])) == 4
    assert candidate(root = tree_node([2, 1, 3, 4, None, None, 6])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 33, 37])) == 15
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 7, 9, 11, 13, 14, 18, 19, 23])) == 7
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, 16])) == 5
    assert candidate(root = tree_node([30, 20, 50, 10, 25, 40, 60, 5, 15, None, None, 35, 45, 55, 65, 1, None, 12, 18, 23, 28, 32, 37, None, None, None, None, None, 43, 48, None, 53, 58, None, None, None, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 32, 37])) == 15
    assert candidate(root = tree_node([3, 1, 4, None, None, 2, None, None, None, 5, 6, 7, 8, 9, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 11, 14, 16, 19])) == 15
    assert candidate(root = tree_node([2, 1, 3, None, None, 2, 4])) == 3
    assert candidate(root = tree_node([5, 2, 8, 1, 3, 7, 10, 0, None, 2.5, 4, 6, 9, None, None, None, None, None, 15, 12, 13, None, None, 11])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, 6, 9, 11, 13, 18, 25])) == 15
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, None, None, None])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37, 1, 4, 6, 8, 11, 13, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 34, 36, 38])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24])) == 1
    assert candidate(root = tree_node([50, 30, 60, 5, 20, 55, 70, None, None, 10, 25, None, 65, 80])) == 3
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, 7, None, 18, 22, 27, 32, 40])) == 13
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 4, 9, 11, 13, 14, 17, 22, 27, 2, 6, None, 10, None, None, None, None, 18, 21, 24, 26, 28, 30, None, None, 5, 7, None, None, 19, None, 23, None, 29, None, None, None, None, 3, 1])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, None, 6, None])) == 2
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90, 5, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, 32, None, None, 44, None, None, None, 48, None, None, None, 52, None, None, None, None, 62, None, None, None, None, 68, None, None, None, None, None, None, 72, None, None, None, None, None, None, 78, None, None, None, None, 85, None, None, None, 95, None])) == 7
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 8, 12, 16, 25, 35, 48, 7, 9, 11, 13, 18, 22, 24, 33, 37, 42, 46, 6, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None])) == 2
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 17, 35, 43, 48, 55, None, 8, 13, 16, None, None, 33, 38, None, 47, None, 53, 57, None, None, None, None, None, None, None, None, None])) == 6
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, 0, 4, None, None, 11, 14, None, 7, 2, 9, 3, 6, 13, 17, 21, 16, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 1
    assert candidate(root = tree_node([30, 10, 60, 5, 15, None, None, 3, 7, 12, 18])) == 9
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, None, 9, None, 16, 18, 25, None, 17, None, 19, None, None, None, 13])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, None, 20, None, None])) == 7
    assert candidate(root = tree_node([5, -2, 6, -3, -1, None, 8])) == 6
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 13, 18, 25])) == 14
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 35, 60, 90, 110, 140, 180, 250])) == 15
    assert candidate(root = tree_node([2, 1, 3, None, None, 4, 5])) == 1
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 3, None, 9, None, 16, None, None, None, 2])) == 2
    assert candidate(root = tree_node([3, 2, 5, None, 3, None, 9])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 9, None, None, 6, 3, None])) == 1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 15
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 11, 14, 17, 20])) == 14
    assert candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 40, 60, 80, 125, 175, 250, 350])) == 15
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 6, None, None, 3, 9, None, None, None, None, 2])) == 4
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 35, 50, 5, 12, 18, 25, 40, 48, 55, 60])) == 7
    assert candidate(root = tree_node([5, -2, 6, None, 3, 5, 8])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, 8.5, 12, None, None, None, None, None, None, 11, None, None, None, None, None, 13])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, 16, 17, None, None, 18, 19, 20])) == 1
    assert candidate(root = tree_node([30, 15, 60, 5, 20, 45, 70, 3, 7, 18, 25, 40, 50, 65, 80, 1, 4, 6, 9, 17, 22, 35, 43, 55, 62, 75, 85, None, None, None, None, None, None, None, None, 10, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 11])) == 3
    assert candidate(root = tree_node([3, 2, 4, 1, 5])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, 4, 6, 9, None, None, None, 3])) == 3
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, 0, None, None, 9, None, None, 6])) == 2
    assert candidate(root = tree_node([3, 2, 5, None, 4, None, 7])) == 2
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, None, None, None, 9, 16, 14, 17, None, None, None, None, None, None, None, None, 18, None, None, None, None, None, 19, 20, 21, 22, 23, 24, 25])) == 3
    assert candidate(root = tree_node([5, 3, 9, 2, 4, 7, 11, None, None, None, None, 6, 8, 10, 12])) == 11
    assert candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 1, 7, 12, 18, 35, 45, 55, 65, 0, 4, 8, 11, 13, 17, 19, 33, 36, 44, 46, 54, 56, 64, 66])) == 3
    assert candidate(root = tree_node([50, 30, 60, 10, 55, None, 80, 5, None, 45, 58, None, 90])) == 6
    assert candidate(root = tree_node([2, 1, 3, None, None, 4])) == 1
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, 6, None, None, None, None, None, None, None, None, 10])) == 3
    assert candidate(root = tree_node([5, 3, 6, 2, 4, 5, 7, 1, None, None, None, None, None, None, None])) == 4
    assert candidate(root = tree_node([3, 2, 4, None, None, None, 5])) == 4
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7, None, 12, 9, 14])) == 2
    assert candidate(root = tree_node([3, 2, 5, 1, None, 4, 6])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, None, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8])) == 1
    assert candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 3, 7, 12, 18, 35, 45, 55, 65])) == 15
    assert candidate(root = tree_node([3, 2, 5, None, 3, None, 9, 10, None, None, None, 8, None])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 15
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, None, 10, None, 11])) == 4
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 7, 20, 0, 6, None, None, 9, 16, 14, 17])) == 3
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 30, 60, 80, 110, 140, 180, 220])) == 15
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 16, 25, 11, 14, 17, 22, None, None, None, None, None, None, None, None, None, None, None, 21, 24, 27, 18, 19, 23, 26, 30, 28, 29, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([50, 30, 60, 5, 20, 45, 70, None, None, 10, 25, 40, 55, 65, 80])) == 7
    assert candidate(root = tree_node([10, 5, 15, 1, 8, 12, 20, None, None, 6, 9, 11, 14, 18, 25])) == 13
    assert candidate(root = tree_node([5, 3, 6, 2, 4, 1, None, 1, None, None, None, None, None, None, None])) == 4


