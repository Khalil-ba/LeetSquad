def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 8, 5, 0, 1, None, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 8, 5, 0, 1, None, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 18])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 18])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 10, 20, 5, None, 15, 25, 3, None, None, None, 18, 22])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 10, 20, 5, None, 15, 25, 3, None, None, None, 18, 22])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, 0, 2, 6, 9, None, None, None, None, None, None, None, None])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, 0, 2, 6, 9, None, None, None, None, None, None, None, None])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 6, 15, 3, 8, 12, 20, 1, 5, 7, 9, 11, 13, 17, 22])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 6, 15, 3, 8, 12, 20, 1, 5, 7, 9, 11, 13, 17, 22])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 8, 10, 14, 13])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 8, 10, 14, 13])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 5, 2, 4, 6, 7, None, None, None, None, None, None, None, 8])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 5, 2, 4, 6, 7, None, None, None, None, None, None, None, 8])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, 5, 5, 5, 5, 5, 5, 5, 5])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, 5, 5, 5, 5, 5, 5, 5, 5])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, 1, 3, 5, None, None, None, None, None])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, 1, 3, 5, None, None, None, None, None])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, None, 6])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, None, 6])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 2, 7, 13, 17, 28, 32, 38, 45])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 2, 7, 13, 17, 28, 32, 38, 45])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 10, 15, None, None, 12, 20])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 10, 15, None, None, 12, 20])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, None, 19, 23])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, None, 19, 23])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 5, 7, 2, 3, 6, 8, 1, 4, 5, 7, 6, 8, 9, 10])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 5, 7, 2, 3, 6, 8, 1, 4, 5, 7, 6, 8, 9, 10])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, None, None, None, None, 14, 15, None, None, None, None, None, 16])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, None, None, None, None, 14, 15, None, None, None, None, None, 16])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 99, 101, 98, 102, 97, 103])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 99, 101, 98, 102, 97, 103])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 9, 4, 6, 8, 10, None, None, None, None, 7, 11, None, None])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 9, 4, 6, 8, 10, None, None, None, None, 7, 11, None, None])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 8, 12, 18, 22, 28, 32, 40])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 8, 12, 18, 22, 28, 32, 40])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, 0, 2, None, None, None, None, 17, 25])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, 0, 2, None, None, None, None, 17, 25])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 63, 87, 112, 137, 162, 187])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 63, 87, 112, 137, 162, 187])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 0, 4, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 0, 4, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, None, None, 10, 40, 125, 175])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, None, None, 10, 40, 125, 175])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 3, 15, 1, None, 12, 20, None, None, None, 13, 18, 22])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 3, 15, 1, None, 12, 20, None, None, None, 13, 18, 22])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, None, None, 17, 20])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, None, None, 17, 20])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 10, 19])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 10, 19])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 10, 15, None, None, None, 20])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 10, 15, None, None, None, 20])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, None, None, 2, 6, 8, 10, 12, 14])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, None, None, 2, 6, 8, 10, 12, 14])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 8])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 8])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 0, 2, 2, 4, None, None, None, 3, None, None, 2, None])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 0, 2, 2, 4, None, None, None, 3, None, None, 2, None])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, None, 1, None, 3, None, None, 2, None, 2])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, None, 1, None, 3, None, None, 2, None, 2])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 8])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 8])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, 5, None, 9, 6, None, 7, None, 11, None, 13, None, 17])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, 5, None, 9, 6, None, 7, None, 11, None, 13, None, 17])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 15, 20, 25, None, None, 30, None, None, 35])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 15, 20, 25, None, None, 30, None, None, 35])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 5, 8, 13, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 5, 8, 13, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 12, 8, 24, 4, None, 2, None, 10])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 12, 8, 24, 4, None, 2, None, 10])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 4, None, 9, None, None, 3, 6])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 4, None, 9, None, None, 3, 6])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 11, 0, 3, 9, 12, None, None, 2, 4, 8, 10, None, 5, 6, 13])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 11, 0, 3, 9, 12, None, None, 2, 4, 8, 10, None, 5, 6, 13])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 9, None, 10, None, None, 13, None, None, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 9, None, 10, None, None, 13, None, None, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 14, 18, 22])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 14, 18, 22])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([4, 8, 5, 0, 1, None, 6])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 18])) == 4
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 3
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 7
    assert candidate(root = tree_node([6, 10, 20, 5, None, 15, 25, 3, None, None, None, 18, 22])) == 5
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, 0, 2, 6, 9, None, None, None, None, None, None, None, None])) == 10
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 23, 27, 33, 37])) == 12
    assert candidate(root = tree_node([9, 6, 15, 3, 8, 12, 20, 1, 5, 7, 9, 11, 13, 17, 22])) == 12
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 13
    assert candidate(root = tree_node([2, 3, 3, 8, 10, 14, 13])) == 4
    assert candidate(root = tree_node([1, 3, 5, 2, 4, 6, 7, None, None, None, None, None, None, None, 8])) == 6
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 5
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, 5, 5, 5, 5, 5, 5, 5, 5])) == 13
    assert candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10
    assert candidate(root = tree_node([5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10])) == 9
    assert candidate(root = tree_node([3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3])) == 8
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 3
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, 1, 3, 5, None, None, None, None, None])) == 9
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])) == 10
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 4
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 11
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, None, 6])) == 7
    assert candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 2, 7, 13, 17, 28, 32, 38, 45])) == 11
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 7
    assert candidate(root = tree_node([7, 10, 15, None, None, 12, 20])) == 4
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, None, 19, 23])) == 3
    assert candidate(root = tree_node([6, 5, 7, 2, 3, 6, 8, 1, 4, 5, 7, 6, 8, 9, 10])) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, None, None, None, None, 14, 15, None, None, None, None, None, 16])) == 8
    assert candidate(root = tree_node([100, 99, 101, 98, 102, 97, 103])) == 6
    assert candidate(root = tree_node([8, 5, 9, 4, 6, 8, 10, None, None, None, None, 7, 11, None, None])) == 8
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 12
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 8
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 8, 12, 18, 22, 28, 32, 40])) == 15
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 4
    assert candidate(root = tree_node([999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999])) == 15
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 15
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, 0, 2, None, None, None, None, 17, 25])) == 8
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 63, 87, 112, 137, 162, 187])) == 9
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938])) == 15
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 4
    assert candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 8
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 9
    assert candidate(root = tree_node([2, 1, 3, 0, 4, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0])) == 9
    assert candidate(root = tree_node([100, 50, 150, 25, 75, None, None, 10, 40, 125, 175])) == 6
    assert candidate(root = tree_node([9, 3, 15, 1, None, 12, 20, None, None, None, 13, 18, 22])) == 6
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, None, None, 17, 20])) == 7
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 10, 19])) == 4
    assert candidate(root = tree_node([7, 10, 15, None, None, None, 20])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 10
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18])) == 7
    assert candidate(root = tree_node([7, 3, 11, 1, 5, 9, 13, None, None, 2, 6, 8, 10, 12, 14])) == 12
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, 7])) == 5
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 8])) == 5
    assert candidate(root = tree_node([2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([2, 1, 3, 0, 2, 2, 4, None, None, None, 3, None, None, 2, None])) == 7
    assert candidate(root = tree_node([2, 3, None, 1, None, 3, None, None, 2, None, 2])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 8])) == 8
    assert candidate(root = tree_node([1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4])) == 10
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 15
    assert candidate(root = tree_node([1, 3, 2, None, 5, None, 9, 6, None, 7, None, 11, None, 13, None, 17])) == 3
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 12
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1])) == 3
    assert candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875])) == 15
    assert candidate(root = tree_node([5, 10, 15, 20, 25, None, None, 30, None, None, 35])) == 3
    assert candidate(root = tree_node([2, 3, 5, 8, 13, None, None])) == 3
    assert candidate(root = tree_node([6, 12, 8, 24, 4, None, 2, None, 10])) == 4
    assert candidate(root = tree_node([5, 2, 8, 1, 4, None, 9, None, None, 3, 6])) == 6
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25])) == 11
    assert candidate(root = tree_node([2, 1, 11, 0, 3, 9, 12, None, None, 2, 4, 8, 10, None, 5, 6, 13])) == 8
    assert candidate(root = tree_node([1, 3, 2, 5, 9, None, 10, None, None, 13, None, None, 7])) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 14, 18, 22])) == 12
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 5


