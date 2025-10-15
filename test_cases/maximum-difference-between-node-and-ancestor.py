def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 0, 3])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 0, 3])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 2, 7, None, 18, None, None, 6, 8, 13, 19])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 2, 7, None, 18, None, None, 6, 8, 13, 19])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, None, 12, None, 22, 28, None, 33])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, None, 12, None, 22, 28, None, 33])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 7, 3, 8, 6, 9, 2, 9, 10, None, None, None, 11, None, 12, None, 13])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 7, 3, 8, 6, 9, 2, 9, 10, None, None, None, 11, None, 12, None, 13])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 8, 15, 7, 9, 12, 20, 6, None, 10, 11, 14, 18, None, None, None, None, 13, 17, 19, 25])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 8, 15, 7, 9, 12, 20, 6, None, 10, 11, 14, 18, None, None, None, None, 13, 17, 19, 25])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 11, 14, None, 13, None, None, None, None, None, None, 12, None, None, None, None, 16, None, None, None, None, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, None, 20, None, None, None, None, None, None, None, None])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 11, 14, None, 13, None, None, None, None, None, None, 12, None, None, None, None, 16, None, None, None, None, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, None, 20, None, None, None, None, None, None, None, None])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 90: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 4, 17, 3, 9, 15, 8, None, None, 7, None, None, None, None, None])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 4, 17, 3, 9, 15, 8, None, None, 7, None, None, None, None, None])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, None, 18, None, 28, 32, 40, None, None, None, None, None, None, None, None, 27])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, None, 18, None, 28, 32, 40, None, None, None, None, None, None, None, None, 27])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, None, 28, 40, 55, 70, 80, 95])) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, None, 28, 40, 55, 70, 80, 95])) == 45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 58, 65, 75, 1, None, None, None, None, None, None, None, 12, None, 28, None, None, 50, 56, 62, 68, 72, 78, 80])) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 58, 65, 75, 1, None, None, None, None, None, None, None, 12, None, 28, None, None, 50, 56, 62, 68, 72, 78, 80])) == 71: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 17, 3, 6, 10, 22, None, None, 5, 7, None, 20, None, 24])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 17, 3, 6, 10, 22, None, None, 5, 7, None, 20, None, 24])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, None, 7, None, 17, None, None, None, 25, 40])) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, None, 7, None, 17, None, None, None, 25, 40])) == 30: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 2, 7, 12, 18, 27, 32, 38, 45])) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 2, 7, 12, 18, 27, 32, 38, 45])) == 23: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180])) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180])) == 90: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 17, 20])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 17, 20])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 18, 25, 5, 9, 11, 14, 16, 19, 24, 30])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 18, 25, 5, 9, 11, 14, 16, 19, 24, 30])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 10, 20, None, 2, None, None, 6, 12, 18, 25])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 10, 20, None, 2, None, None, 6, 12, 18, 25])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 17, 3, 6, 15, 22, 2, 5, 12, 18, None, None, None, None, 16, 20, None, None, None, None, None, 24, 27])) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 17, 3, 6, 15, 22, 2, 5, 12, 18, None, None, None, None, 16, 20, None, None, None, None, None, 24, 27])) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, None, 12, 11, 14])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, None, 12, 11, 14])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 27, 32, 37])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 27, 32, 37])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 98, 102, 115, 118, 125])) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 98, 102, 115, 118, 125])) == 30: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 17, 3, 6, 12, 22, 2, 5, 8, 11, 15, 20, 24, 25])) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 17, 3, 6, 12, 22, 2, 5, 8, 11, 15, 20, 24, 25])) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2, None, None, None, None, None, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2, None, None, None, None, None, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 17, 23, 27, 33, 37])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 17, 23, 27, 33, 37])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, None, 18, None, 37, 47, None, None, None, None, None])) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, None, 18, None, 37, 47, None, None, None, None, None])) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 18, 23, 27, 33, 37])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 18, 23, 27, 33, 37])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 20, 40, 10, 25, 35, 50, 5, 15, None, None, 32, 37, 45, 60])) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 20, 40, 10, 25, 35, 50, 5, 15, None, None, 32, 37, 45, 60])) == 30: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 10, 1, 6, 9, 15, None, None, 4, 7, 8, 12, None, None, None, None, None, None, None, 14])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 10, 1, 6, 9, 15, None, None, 4, 7, 8, 12, None, None, None, None, None, None, None, 14])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, 7, None, 20, None, None, 18, 25])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, 7, None, 20, None, None, 18, 25])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 97, 102, 115, 125, 130])) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 97, 102, 115, 125, 130])) == 30: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2, None, None, None, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2, None, None, None, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, None, 13, None, 22, 28, 40])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, None, 13, None, 22, 28, 40])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 80, 10, 30, 70, 90, None, None, 25, 35, None, 75, 85, None])) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 80, 10, 30, 70, 90, None, None, 25, 35, None, 75, 85, None])) == 40: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 20, 30, 40, 55, 65, 85, 95])) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 20, 30, 40, 55, 65, 85, 95])) == 45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 44, 58, 69, 83, 90])) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 44, 58, 69, 83, 90])) == 44: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, 4, None, None, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, 4, None, None, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 9, None, None, 7, 10, None, 6, None, 11])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 9, None, None, 7, 10, None, 6, None, 11])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 10, 1, 3, 9, 12, None, None, 4, 6, 8, 11, 13])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 10, 1, 3, 9, 12, None, None, 4, 6, 8, 11, 13])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 15, 20, 35, 55, 65, 85, 100])) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 15, 20, 35, 55, 65, 85, 100])) == 50: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, 5, None, None, None, None, None, 6])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, 5, None, None, None, None, None, 6])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 35: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 49])) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 49])) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 65, 68, 75])) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 65, 68, 75])) == 45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, None, None, None, None, None, None, None])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, None, None, None, None, None, None, None])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, None, None, 2, 4, None, None, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, None, None, 2, 4, None, None, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 25, 40, 20, 28, 35, 45, 15, 22, None, 27, 32, 38, 43, 47])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 25, 40, 20, 28, 35, 45, 15, 22, None, 27, 32, 38, 43, 47])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 45, 48, 55])) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 45, 48, 55])) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, 10])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, 10])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, None, None, None, None, None, None, 8])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, None, None, None, None, None, None, 8])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 9, 0, 2, None, None, None, 4, 3])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 9, 0, 2, None, None, None, 4, 3])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 23, 28, 33, 37])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 23, 28, 33, 37])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, None, 3, None, None, None, 4, None, None, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, None, 3, None, None, None, 4, None, None, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 10, 20, None, None, 4, 6, 8, 12, 17, 23])) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 10, 20, None, None, 4, 6, 8, 12, 17, 23])) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, None, 3, 7, 13, 18])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, None, 3, 7, 13, 18])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30])) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30])) == 29: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, None, None, None, None, 20, None, 40, None, 90, None, None, 130, None, None, None, None, 150, None, None, 190, None, None])) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, None, None, None, None, 20, None, 40, None, 90, None, None, 130, None, None, None, None, 150, None, None, 190, None, None])) == 150: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 8, None, None, None, None, None, None])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 8, None, None, None, None, None, None])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, 16, 20])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, 16, 20])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187, 6, 18, 31, 44, 58, 69, 83, 90, 108, 118, 128, 138, 158, 168, 178, 188])) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187, 6, 18, 31, 44, 58, 69, 83, 90, 108, 118, 128, 138, 158, 168, 178, 188])) == 94: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 6, 12, 4, 7, 10, 14, 3, 5, 8, 11, 13, 15])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 6, 12, 4, 7, 10, 14, 3, 5, 8, 11, 13, 15])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 9, 1, 4, None, 11, None, None, 2, 6, 10, 12])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 9, 1, 4, None, 11, None, None, 2, 6, 10, 12])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 200, 25, 75, 150, 250, 12, None, 65, 85, 125, 175, 225, 275])) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 200, 25, 75, 150, 250, 12, None, 65, 85, 125, 175, 225, 275])) == 175: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 1, 8, None, 7])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 1, 8, None, 7])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 6, 1, None, None, 8, None, 4, None, None, None, 7, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 6, 1, None, None, 8, None, 4, None, None, None, 7, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 10, 14, None, None, 17, None, None, None, None, None, None, None, None])) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 10, 14, None, None, 17, None, None, None, None, None, None, None, None])) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 90: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 13, 18, 25, 8, 17, 19, 21, 30])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 13, 18, 25, 8, 17, 19, 21, 30])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, None, 25, None, None, None, None, 22, 28])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, None, 25, None, None, None, None, 22, 28])) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, None, 2, None, 0, 3])) == 3
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) == 7
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 18, None, None, 6, 8, 13, 19])) == 9
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 9
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, None, 12, None, 22, 28, None, 33])) == 17
    assert candidate(root = tree_node([5, 4, 7, 3, 8, 6, 9, 2, 9, 10, None, None, None, 11, None, 12, None, 13])) == 10
    assert candidate(root = tree_node([10, 8, 15, 7, 9, 12, 20, 6, None, 10, 11, 14, 18, None, None, None, None, 13, 17, 19, 25])) == 17
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 11, 14, None, 13, None, None, None, None, None, None, 12, None, None, None, None, 16, None, None, None, None, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, None, 20, None, None, None, None, None, None, None, None])) == 14
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 90
    assert candidate(root = tree_node([10, 4, 17, 3, 9, 15, 8, None, None, 7, None, None, None, None, None])) == 9
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, None, 18, None, 28, 32, 40, None, None, None, None, None, None, None, None, 27])) == 20
    assert candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, None, 28, 40, 55, 70, 80, 95])) == 45
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 7
    assert candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 58, 65, 75, 1, None, None, None, None, None, None, None, 12, None, 28, None, None, 50, 56, 62, 68, 72, 78, 80])) == 71
    assert candidate(root = tree_node([9, 4, 17, 3, 6, 10, 22, None, None, 5, 7, None, 20, None, 24])) == 15
    assert candidate(root = tree_node([10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 19
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, None, 7, None, 17, None, None, None, 25, 40])) == 30
    assert candidate(root = tree_node([25, 10, 35, 5, 15, 30, 40, 2, 7, 12, 18, 27, 32, 38, 45])) == 23
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180])) == 90
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 17, 20])) == 19
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 18, 25, 5, 9, 11, 14, 16, 19, 24, 30])) == 15
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 10, 20, None, 2, None, None, 6, 12, 18, 25])) == 18
    assert candidate(root = tree_node([9, 4, 17, 3, 6, 15, 22, 2, 5, 12, 18, None, None, None, None, 16, 20, None, None, None, None, None, 24, 27])) == 25
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, None, 12, 11, 14])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16])) == 15
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 27, 32, 37])) == 17
    assert candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 98, 102, 115, 118, 125])) == 30
    assert candidate(root = tree_node([9, 4, 17, 3, 6, 12, 22, 2, 5, 8, 11, 15, 20, 24, 25])) == 16
    assert candidate(root = tree_node([3, 1, 4, None, 2, None, None, None, None, None, None])) == 2
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 17
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 17, 23, 27, 33, 37])) == 18
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, None, 18, None, 37, 47, None, None, None, None, None])) == 25
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 18, 23, 27, 33, 37])) == 17
    assert candidate(root = tree_node([30, 20, 40, 10, 25, 35, 50, 5, 15, None, None, 32, 37, 45, 60])) == 30
    assert candidate(root = tree_node([5, 3, 10, 1, 6, 9, 15, None, None, 4, 7, 8, 12, None, None, None, None, None, None, None, 14])) == 10
    assert candidate(root = tree_node([10, 5, 15, None, 7, None, 20, None, None, 18, 25])) == 15
    assert candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 92, 97, 102, 115, 125, 130])) == 30
    assert candidate(root = tree_node([3, 1, 4, None, 2, None, None, None, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, None, 13, None, 22, 28, 40])) == 20
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 14
    assert candidate(root = tree_node([50, 20, 80, 10, 30, 70, 90, None, None, 25, 35, None, 75, 85, None])) == 40
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 9
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 20, 30, 40, 55, 65, 85, 95])) == 45
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 44, 58, 69, 83, 90])) == 44
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, None, None, 5])) == 4
    assert candidate(root = tree_node([5, 1, 9, None, None, 7, 10, None, 6, None, 11])) == 6
    assert candidate(root = tree_node([5, 2, 10, 1, 3, 9, 12, None, None, 4, 6, 8, 11, 13])) == 8
    assert candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 15, 20, 35, 55, 65, 85, 100])) == 50
    assert candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, 5, None, None, None, None, None, 6])) == 3
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 35
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 49])) == 25
    assert candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 65, 68, 75])) == 45
    assert candidate(root = tree_node([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 13
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, None, None, None, None, None, None, None])) == 20
    assert candidate(root = tree_node([1, None, 3, None, None, 2, 4, None, None, None, 5])) == 2
    assert candidate(root = tree_node([30, 25, 40, 20, 28, 35, 45, 15, 22, None, 27, 32, 38, 43, 47])) == 17
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 45, 48, 55])) == 25
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 9
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, 10])) == 7
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == 2
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, None, None, None, None, None, None, 8])) == 4
    assert candidate(root = tree_node([5, 1, 9, 0, 2, None, None, None, 4, 3])) == 5
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 23, 28, 33, 37])) == 19
    assert candidate(root = tree_node([1, 0, 2, None, None, 3, None, None, None, 4, None, None, None, 5])) == 2
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 10, 20, None, None, 4, 6, 8, 12, 17, 23])) == 16
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, None, 3, 7, 13, 18])) == 17
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30])) == 29
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, None, None, None, None, 20, None, 40, None, 90, None, None, 130, None, None, None, None, 150, None, None, 190, None, None])) == 150
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7, 0, 8, None, None, None, None, None, None])) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([4, 2, 6, 1, 3, 5, 7])) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, 16, 20])) == 10
    assert candidate(root = tree_node([2, 1, 3, None, None, 4])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187, 6, 18, 31, 44, 58, 69, 83, 90, 108, 118, 128, 138, 158, 168, 178, 188])) == 94
    assert candidate(root = tree_node([9, 6, 12, 4, 7, 10, 14, 3, 5, 8, 11, 13, 15])) == 6
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37])) == 17
    assert candidate(root = tree_node([5, 3, 9, 1, 4, None, 11, None, None, 2, 6, 10, 12])) == 7
    assert candidate(root = tree_node([100, 50, 200, 25, 75, 150, 250, 12, None, 65, 85, 125, 175, 225, 275])) == 175
    assert candidate(root = tree_node([10, 5, 15, 1, 8, None, 7])) == 9
    assert candidate(root = tree_node([5, 2, 6, 1, None, None, 8, None, 4, None, None, None, 7, 9])) == 8
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 10, 14, None, None, 17, None, None, None, None, None, None, None, None])) == 16
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 90
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 13, 18, 25, 8, 17, 19, 21, 30])) == 20
    assert candidate(root = tree_node([15, 10, 20, 8, 12, None, 25, None, None, None, None, 22, 28])) == 13


