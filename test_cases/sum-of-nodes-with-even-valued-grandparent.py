def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 5, 0, 1, None, None, None, None, 7])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 5, 0, 1, None, None, None, None, 7])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, 8, None, None, None, None, 5])) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, 8, None, None, None, None, 5])) == 27: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 5, 1, 3, None, 7, None, None, None, None, None, 9])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 5, 1, 3, None, 7, None, None, None, None, None, 9])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 38: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 14, 3, None, 10, None, 7])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 14, 3, None, 10, None, 7])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4, 5, 6, 7])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4, 5, 6, 7])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 1, 4, None, 2, 6, 8, None, None, None, None, 7])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 1, 4, None, 2, 6, 8, None, None, None, None, 7])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, None, 4, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, None, 4, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([11, 10, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([11, 10, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 11, 1, None, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15, None, None, 16, None, None, 17, None, None, 18, None, None, 19, None, None, 20, None, None, 21, None, None, 22, None, None, 23, None, None, 24, None, None, 25, None, None, 26, None, None, 27, None, None, 28, None, None, 29, None, None, 30])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 11, 1, None, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15, None, None, 16, None, None, 17, None, None, 18, None, None, 19, None, None, 20, None, None, 21, None, None, 22, None, None, 23, None, None, 24, None, None, 25, None, None, 26, None, None, 27, None, None, 28, None, None, 29, None, None, 30])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8])) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8])) == 26: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, None, 9, 6, None, 10, 11, 2, None, None, None, 8, None, 7])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, None, 9, 6, None, 10, 11, 2, None, None, None, 8, None, 7])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])) == 114: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, 0, 5, None, None, None, 10, None, None, None, None, 11, None, None, 12])) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, 0, 5, None, None, None, 10, None, None, None, None, 11, None, None, 12])) == 31: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([24, 12, 16, 6, 10, 8, 20, 3, 9, 7, 11, 5, 15, 1, 13, None, None, None, None, None, None, None, None, None, 4, None, None, None, 14, 17, 18, 19, None, 21, 22, 23])) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([24, 12, 16, 6, 10, 8, 20, 3, 9, 7, 11, 5, 15, 1, 13, None, None, None, None, None, None, None, None, None, 4, None, None, None, 14, 17, 18, 19, None, 21, 22, 23])) == 161: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 30, 45, 55, 65, 80, 100, 115, 130, 135, 155, 165, 180, 195])) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 30, 45, 55, 65, 80, 100, 115, 130, 135, 155, 165, 180, 195])) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([18, 4, 5, 2, 9, 10, 6, None, None, 1, 3, None, None, 7, 8, None, None, 11, 12, 13, 14, 15, 16, 17])) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([18, 4, 5, 2, 9, 10, 6, None, None, 1, 3, None, None, 7, 8, None, None, 11, 12, 13, 14, 15, 16, 17])) == 89: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 12, 13, 8, 11, 14, 15, None, None, None, 10, None, 9, 16, 17, 18, 19, None, None, None, None, 21, 22, None, 23])) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 12, 13, 8, 11, 14, 15, None, None, None, 10, None, 9, 16, 17, 18, 19, None, None, None, None, 21, 22, None, 23])) == 81: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 96: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 1, 6, 2, None, 8, 4, None, None, None, 7, 9])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 1, 6, 2, None, 8, 4, None, None, None, 7, 9])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 2568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 2568: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([16, 12, 20, 8, 14, 18, 22, 4, 10, 13, 15, 17, 19, 21, 23])) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([16, 12, 20, 8, 14, 18, 22, 4, 10, 13, 15, 17, 19, 21, 23])) == 184: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 296: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([14, 11, 8, 6, 12, 9, 5, 2, 4, 13, 7, 3, 10, None, None, None, None, None, None, None, 1, None, None, 15, 16, 17, None, None, None, None, 18, 19, 20, 21])) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([14, 11, 8, 6, 12, 9, 5, 2, 4, 13, 7, 3, 10, None, None, None, None, None, None, None, 1, None, None, 15, 16, 17, None, None, None, None, 18, 19, 20, 21])) == 67: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 22, 35, 42, 48, 55, 3, 7, 9, 11, 13, 17, 19, 21, 23, 37, 38, 41, 43, 47, 49, 53, 57, 59])) == 551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 22, 35, 42, 48, 55, 3, 7, 9, 11, 13, 17, 19, 21, 23, 37, 38, 41, 43, 47, 49, 53, 57, 59])) == 551: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 1140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 1140: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([13, 11, 17, 7, 3, 16, 20, 1, 5, 9, 15, 12, None, None, None, 4, 6, 8, 10, 14, None, 18, 19, 21, 2, None, None, None, None, None, None, None, None, None, None, None])) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([13, 11, 17, 7, 3, 16, 20, 1, 5, 9, 15, 12, None, None, None, 4, 6, 8, 10, 14, None, 18, 19, 21, 2, None, None, None, None, None, None, None, None, None, None, None])) == 23: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([14, 7, 27, 4, 9, 20, 35, 2, 6, 8, 11, 16, 22, 29, 42])) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([14, 7, 27, 4, 9, 20, 35, 2, 6, 8, 11, 16, 22, 29, 42])) == 68: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([18, 9, 21, 15, 5, 10, 3, 7, None, 6, None, 8, 2, None, 4, None, None, 1, None, None, None, 11])) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([18, 9, 21, 15, 5, 10, 3, 7, None, 6, None, 8, 2, None, 4, None, None, 1, None, None, None, 11])) == 44: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, None, 3, 7, None, None, 2, None, 6, 8, 1, None, None, None, 4, 9, 10, None, None, None, None, 11, 12, 13, 14, 15])) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, None, 3, 7, None, None, 2, None, 6, 8, 1, None, None, None, 4, 9, 10, None, None, None, None, 11, 12, 13, 14, 15])) == 60: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 90, 6, 20, 30, 40, 55, 65, 85, 95])) == 202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 90, 6, 20, 30, 40, 55, 65, 85, 95])) == 202: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 49])) == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 49])) == 178: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == 666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == 666: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 10, 14, 4, 8, 12, 16, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 10, 14, 4, 8, 12, 16, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 424: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([22, 6, 18, 2, 14, 16, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])) == 493
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([22, 6, 18, 2, 14, 16, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])) == 493: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])) == 228: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([18, 3, 20, None, 5, 15, 25, None, None, None, None, 13, None, 22])) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([18, 3, 20, None, 5, 15, 25, None, None, None, None, 13, None, 22])) == 58: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 12, 1, 5, 9, 15, 0, None, None, 3, 7, 11, 13, 19, None, None, None, 4, 6, 8, 10, 12, 14, 16, 18, 20])) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 12, 1, 5, 9, 15, 0, None, None, 3, 7, 11, 13, 19, None, None, None, 4, 6, 8, 10, 12, 14, 16, 18, 20])) == 83: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 11, 16, 24, 29, 31, 34, 41])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 11, 16, 24, 29, 31, 34, 41])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 4, 6, 8, 2, None, 5, None, None, None, None, 1, 3, 7, 9, 11, 13, 15, 17, 19])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 4, 6, 8, 2, None, 5, None, None, None, None, 1, 3, 7, 9, 11, 13, 15, 17, 19])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 28: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, None, None, 6, None, None, None, None, 10])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, None, None, 6, None, None, None, None, 10])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 3, 7, 13, 17, 35, 45, 55, 65])) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 3, 7, 13, 17, 35, 45, 55, 65])) == 360: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([32, 16, 48, 8, 24, 36, 56, 4, 12, 20, 28, 32, 40, 52, 60])) == 372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([32, 16, 48, 8, 24, 36, 56, 4, 12, 20, 28, 32, 40, 52, 60])) == 372: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 96: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190, 5, 15, 22, 35, 55, 65, 72, 78, 85, 95, 105, 135, 137, 145, 155, 172, 180, 195, 200])) == 1755
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190, 5, 15, 22, 35, 55, 65, 72, 78, 85, 95, 105, 135, 137, 145, 155, 172, 180, 195, 200])) == 1755: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 6, 1, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16])) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 6, 1, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16])) == 74: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 480: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6])) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6])) == 28: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 5, 6, 3, 1, None, None, 2, 4, None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 5, 6, 3, 1, None, None, 2, 4, None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 279: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 13, 18, 22])) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 13, 18, 22])) == 42: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 6, 5, 2, 4, 9, 7, None, None, 1, None, None, 3, 10, None, None, 11, 12, 13, None, None, 14, 15, None, 16])) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 6, 5, 2, 4, 9, 7, None, None, 1, None, None, 3, 10, None, None, 11, 12, 13, None, None, 14, 15, None, 16])) == 34: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, 35, None, None, 45, 55])) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, 35, None, None, 45, 55])) == 60: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, None, None, 30, 60, 90, 110, 140, 180, 20, 40, 55, 65, 85, 95, 105, 115, 130, 145, 160, 185, 195, None, None, 22, 28, 35, 45, 58, 68, 72, 82, 92, 102, 112, 118, 128, 135, 148, 155, 165, 175, 188, 198])) == 3331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, None, None, 30, 60, 90, 110, 140, 180, 20, 40, 55, 65, 85, 95, 105, 115, 130, 145, 160, 185, 195, None, None, 22, 28, 35, 45, 58, 68, 72, 82, 92, 102, 112, 118, 128, 135, 148, 155, 165, 175, 188, 198])) == 3331: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 70, 100, 2, 6, 12, 20, 35, 43, 53, 57, 63, 67, 73, 77, 85, 95, 105])) == 993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 70, 100, 2, 6, 12, 20, 35, 43, 53, 57, 63, 67, 73, 77, 85, 95, 105])) == 993: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 4, 15, 1, None, 11, 19, 6, None, None, 12, None, None, 5])) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 4, 15, 1, None, 11, 19, 6, None, None, 12, None, None, 5])) == 37: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38, 39])) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38, 39])) == 240: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 210: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 18, 23, 28, 33, 38])) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 18, 23, 28, 33, 38])) == 242: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, 3, 6, None, 11, 1, None, 4, 7, None, 14])) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, 3, 6, None, 11, 1, None, 4, 7, None, 14])) == 34: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, 9, None, 1, 4, None, None, None, 5, 6, None, None, 8, 10])) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, 9, None, 1, 4, None, None, None, 5, 6, None, None, 8, 10])) == 33: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 3, 7, 13, 19, 23, 29, 37])) == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 3, 7, 13, 19, 23, 29, 37])) == 212: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 14, 17, 22, 0, None, None, None, None, None, None, 9, None, None, 13, None, None, 16, None, None, 18, None, None, 21, None, None])) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 14, 17, 22, 0, None, None, None, None, None, None, 9, None, None, 13, None, None, 16, None, None, 18, None, None, 21, None, None])) == 92: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 108: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([22, 11, 44, 7, 33, 55, 66, 1, 5, 9, 27, 50, 70, 100, 200])) == 581
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([22, 11, 44, 7, 33, 55, 66, 1, 5, 9, 27, 50, 70, 100, 200])) == 581: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 5, 2, 3, 4, 8, 5, 6, 7, 9, 10, 11, 12, 13])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 5, 2, 3, 4, 8, 5, 6, 7, 9, 10, 11, 12, 13])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 10, 1, 3, 7, 13, None, 4, None, 5, 8, 12, 14, 16])) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 10, 1, 3, 7, 13, None, 4, None, 5, 8, 12, 14, 16])) == 83: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([46, 23, 69, 11, 35, 55, 82, 5, 19, 30, 40, 50, 60, 70, 80, 2, 7, 14, 21, 27, 32, 39, 45, 47, 53, 57, 61, 67, 73, 77, 81, 1, 3, 8, 12, 20, 26, 31, 37, 43, 49, 52, 58, 62, 66, 72, 76, 83, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([46, 23, 69, 11, 35, 55, 82, 5, 19, 30, 40, 50, 60, 70, 80, 2, 7, 14, 21, 27, 32, 39, 45, 47, 53, 57, 61, 67, 73, 77, 81, 1, 3, 8, 12, 20, 26, 31, 37, 43, 49, 52, 58, 62, 66, 72, 76, 83, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1042: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 108: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([32, 16, 48, 8, 24, 36, 60, 4, 12, 20, 28, 32, 44, 52, 56, 2, 6, 10, 14, 18, 22, 26, 30, 34, 46, 50, 54, 58, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, 7, None, None, None, 11, None, None, None, None, None, None, None, None, None, 15, None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None])) == 782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([32, 16, 48, 8, 24, 36, 60, 4, 12, 20, 28, 32, 44, 52, 56, 2, 6, 10, 14, 18, 22, 26, 30, 34, 46, 50, 54, 58, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, 7, None, None, None, 11, None, None, None, None, None, None, None, None, None, 15, None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None])) == 782: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 5, 1, 3, None, 6, 0, 8, None, None, 7, 9])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 5, 1, 3, None, 6, 0, 8, None, None, 7, 9])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([17, 5, 10, None, None, 8, 9, None, None, 3, None, None, 13])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([17, 5, 10, None, None, 8, 9, None, None, 3, None, None, 13])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 60, 82, 6, 20, None, 40, 55, 70, 10, 5, 15, 30, 45, 65, 77, None, None, None, None, 58])) == 404
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 60, 82, 6, 20, None, 40, 55, 70, 10, 5, 15, 30, 45, 65, 77, None, None, None, None, 58])) == 404: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30])) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30])) == 192: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([24, 12, 25, 6, 18, 21, 29, 3, 9, 15, None, 19, 23, 27, 31, 1, 5, 7, 11, 13, None, 17, None, None, 22, None, 26, None, 30, 2, 4, 8, 10, 14, 16, None, None, None, None, None, 20, None, None, 25, None, None, 28, None, None, 32])) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([24, 12, 25, 6, 18, 21, 29, 3, 9, 15, None, 19, 23, 27, 31, 1, 5, 7, 11, 13, None, 17, None, None, 22, None, 26, None, 30, 2, 4, 8, 10, 14, 16, None, None, None, None, None, 20, None, None, 25, None, None, 28, None, None, 32])) == 138: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 31: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8, None, None, None, 9, None, None, None, 10])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8, None, None, None, 9, None, None, None, 10])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, 8, None, None, None, 5, 6, 7])) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, 8, None, None, None, 5, 6, 7])) == 32: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([14, 8, 22, 4, 12, 16, 28, 2, 6, 10, 14, 18, 22, 26, 30])) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([14, 8, 22, 4, 12, 16, 28, 2, 6, 10, 14, 18, 22, 26, 30])) == 188: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 5, 9, 3, 6, 8, 10, 2, 4, None, None, None, None, None, None])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 5, 9, 3, 6, 8, 10, 2, 4, None, None, None, None, None, None])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 38: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([22, 17, 30, 10, 21, 28, 32, 5, 14, 19, 29, None, 35, 3, None, None, 12, None, 18, None, None, None, None, None, 24, 26, 31, 33, 36])) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([22, 17, 30, 10, 21, 28, 32, 5, 14, 19, 29, None, 35, 3, None, None, 12, None, 18, None, None, None, None, None, 24, 26, 31, 33, 36])) == 240: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([8, 4, 5, 0, 1, None, None, None, None, 7])) == 8
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, 8, None, None, None, None, 5])) == 27
    assert candidate(root = tree_node([4, 2, 5, 1, 3, None, 7, None, None, None, None, None, 9])) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 38
    assert candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, None, 5])) == 4
    assert candidate(root = tree_node([5, 14, 3, None, 10, None, 7])) == 0
    assert candidate(root = tree_node([2, 1, 3, None, None, 4, 5, 6, 7])) == 9
    assert candidate(root = tree_node([5, 3, 1, 4, None, 2, 6, 8, None, None, None, None, 7])) == 0
    assert candidate(root = tree_node([2, None, 3, None, 4, None, 5])) == 4
    assert candidate(root = tree_node([11, 10, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 15
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])) == 18
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9])) == 19
    assert candidate(root = tree_node([6, 11, 1, None, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15, None, None, 16, None, None, 17, None, None, 18, None, None, 19, None, None, 20, None, None, 21, None, None, 22, None, None, 23, None, None, 24, None, None, 25, None, None, 26, None, None, 27, None, None, 28, None, None, 29, None, None, 30])) == 2
    assert candidate(root = tree_node([1])) == 0
    assert candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8])) == 26
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 0
    assert candidate(root = tree_node([3, None, 9, 6, None, 10, 11, 2, None, None, None, 8, None, 7])) == 17
    assert candidate(root = tree_node([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])) == 114
    assert candidate(root = tree_node([6, 3, 8, 1, 4, 7, 9, 0, 5, None, None, None, 10, None, None, None, None, 11, None, None, 12])) == 31
    assert candidate(root = tree_node([24, 12, 16, 6, 10, 8, 20, 3, 9, 7, 11, 5, 15, 1, 13, None, None, None, None, None, None, None, None, None, 4, None, None, None, 14, 17, 18, 19, None, 21, 22, 23])) == 161
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 30, 45, 55, 65, 80, 100, 115, 130, 135, 155, 165, 180, 195])) == 1200
    assert candidate(root = tree_node([18, 4, 5, 2, 9, 10, 6, None, None, 1, 3, None, None, 7, 8, None, None, 11, 12, 13, 14, 15, 16, 17])) == 89
    assert candidate(root = tree_node([20, 12, 13, 8, 11, 14, 15, None, None, None, 10, None, 9, 16, 17, 18, 19, None, None, None, None, 21, 22, None, 23])) == 81
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 96
    assert candidate(root = tree_node([5, 3, 1, 6, 2, None, 8, 4, None, None, None, 7, 9])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 2568
    assert candidate(root = tree_node([16, 12, 20, 8, 14, 18, 22, 4, 10, 13, 15, 17, 19, 21, 23])) == 184
    assert candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 296
    assert candidate(root = tree_node([14, 11, 8, 6, 12, 9, 5, 2, 4, 13, 7, 3, 10, None, None, None, None, None, None, None, 1, None, None, 15, 16, 17, None, None, None, None, 18, 19, 20, 21])) == 67
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 22, 35, 42, 48, 55, 3, 7, 9, 11, 13, 17, 19, 21, 23, 37, 38, 41, 43, 47, 49, 53, 57, 59])) == 551
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 1140
    assert candidate(root = tree_node([13, 11, 17, 7, 3, 16, 20, 1, 5, 9, 15, 12, None, None, None, 4, 6, 8, 10, 14, None, 18, 19, 21, 2, None, None, None, None, None, None, None, None, None, None, None])) == 23
    assert candidate(root = tree_node([14, 7, 27, 4, 9, 20, 35, 2, 6, 8, 11, 16, 22, 29, 42])) == 68
    assert candidate(root = tree_node([18, 9, 21, 15, 5, 10, 3, 7, None, 6, None, 8, 2, None, 4, None, None, 1, None, None, None, 11])) == 44
    assert candidate(root = tree_node([10, 5, None, 3, 7, None, None, 2, None, 6, 8, 1, None, None, None, 4, 9, 10, None, None, None, None, 11, 12, 13, 14, 15])) == 60
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 90, 6, 20, 30, 40, 55, 65, 85, 95])) == 202
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 49])) == 178
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == 666
    assert candidate(root = tree_node([6, 10, 14, 4, 8, 12, 16, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 424
    assert candidate(root = tree_node([22, 6, 18, 2, 14, 16, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])) == 493
    assert candidate(root = tree_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])) == 228
    assert candidate(root = tree_node([18, 3, 20, None, 5, 15, 25, None, None, None, None, 13, None, 22])) == 58
    assert candidate(root = tree_node([6, 2, 12, 1, 5, 9, 15, 0, None, None, 3, 7, 11, 13, 19, None, None, None, 4, 6, 8, 10, 12, 14, 16, 18, 20])) == 83
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 11, 16, 24, 29, 31, 34, 41])) == 0
    assert candidate(root = tree_node([10, 4, 6, 8, 2, None, 5, None, None, None, None, 1, 3, 7, 9, 11, 13, 15, 17, 19])) == 19
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 28
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, None, None, 6, None, None, None, None, 10])) == 10
    assert candidate(root = tree_node([30, 10, 50, 5, 15, 40, 60, 3, 7, 13, 17, 35, 45, 55, 65])) == 360
    assert candidate(root = tree_node([32, 16, 48, 8, 24, 36, 56, 4, 12, 20, 28, 32, 40, 52, 60])) == 372
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 96
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190, 5, 15, 22, 35, 55, 65, 72, 78, 85, 95, 105, 135, 137, 145, 155, 172, 180, 195, 200])) == 1755
    assert candidate(root = tree_node([8, 3, 6, 1, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16])) == 74
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 480
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6])) == 28
    assert candidate(root = tree_node([15, 5, 6, 3, 1, None, None, 2, 4, None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 279
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 13, 18, 22])) == 42
    assert candidate(root = tree_node([8, 6, 5, 2, 4, 9, 7, None, None, 1, None, None, 3, 10, None, None, 11, 12, 13, None, None, 14, 15, None, 16])) == 34
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, 35, None, None, 45, 55])) == 60
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, None, None, 30, 60, 90, 110, 140, 180, 20, 40, 55, 65, 85, 95, 105, 115, 130, 145, 160, 185, 195, None, None, 22, 28, 35, 45, 58, 68, 72, 82, 92, 102, 112, 118, 128, 135, 148, 155, 165, 175, 188, 198])) == 3331
    assert candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 70, 100, 2, 6, 12, 20, 35, 43, 53, 57, 63, 67, 73, 77, 85, 95, 105])) == 993
    assert candidate(root = tree_node([10, 4, 15, 1, None, 11, 19, 6, None, None, 12, None, None, 5])) == 37
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38, 39])) == 240
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 210
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 18, 23, 28, 33, 38])) == 242
    assert candidate(root = tree_node([8, 5, 10, 3, 6, None, 11, 1, None, 4, 7, None, 14])) == 34
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, 9, None, 1, 4, None, None, None, 5, 6, None, None, 8, 10])) == 33
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 3, 7, 13, 19, 23, 29, 37])) == 212
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 14, 17, 22, 0, None, None, None, None, None, None, 9, None, None, 13, None, None, 16, None, None, 18, None, None, 21, None, None])) == 92
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 108
    assert candidate(root = tree_node([22, 11, 44, 7, 33, 55, 66, 1, 5, 9, 27, 50, 70, 100, 200])) == 581
    assert candidate(root = tree_node([2, 1, 5, 2, 3, 4, 8, 5, 6, 7, 9, 10, 11, 12, 13])) == 17
    assert candidate(root = tree_node([6, 2, 10, 1, 3, 7, 13, None, 4, None, 5, 8, 12, 14, 16])) == 83
    assert candidate(root = tree_node([46, 23, 69, 11, 35, 55, 82, 5, 19, 30, 40, 50, 60, 70, 80, 2, 7, 14, 21, 27, 32, 39, 45, 47, 53, 57, 61, 67, 73, 77, 81, 1, 3, 8, 12, 20, 26, 31, 37, 43, 49, 52, 58, 62, 66, 72, 76, 83, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 1042
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 108
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 1200
    assert candidate(root = tree_node([32, 16, 48, 8, 24, 36, 60, 4, 12, 20, 28, 32, 44, 52, 56, 2, 6, 10, 14, 18, 22, 26, 30, 34, 46, 50, 54, 58, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, 7, None, None, None, 11, None, None, None, None, None, None, None, None, None, 15, None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None])) == 782
    assert candidate(root = tree_node([4, 2, 5, 1, 3, None, 6, 0, 8, None, None, 7, 9])) == 18
    assert candidate(root = tree_node([17, 5, 10, None, None, 8, 9, None, None, 3, None, None, 13])) == 3
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 60, 82, 6, 20, None, 40, 55, 70, 10, 5, 15, 30, 45, 65, 77, None, None, None, None, 58])) == 404
    assert candidate(root = tree_node([16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30])) == 192
    assert candidate(root = tree_node([24, 12, 25, 6, 18, 21, 29, 3, 9, 15, None, 19, 23, 27, 31, 1, 5, 7, 11, 13, None, 17, None, None, 22, None, 26, None, 30, 2, 4, 8, 10, 14, 16, None, None, None, None, None, 20, None, None, 25, None, None, 28, None, None, 32])) == 138
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 31
    assert candidate(root = tree_node([2, 1, 3, None, None, 4, None, None, None, 5, None, None, None, 6, None, None, None, 7, None, None, None, 8, None, None, None, 9, None, None, None, 10])) == 4
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, 8, None, None, None, 5, 6, 7])) == 32
    assert candidate(root = tree_node([14, 8, 22, 4, 12, 16, 28, 2, 6, 10, 14, 18, 22, 26, 30])) == 188
    assert candidate(root = tree_node([7, 5, 9, 3, 6, 8, 10, 2, 4, None, None, None, None, None, None])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 38
    assert candidate(root = tree_node([22, 17, 30, 10, 21, 28, 32, 5, 14, 19, 29, None, 35, 3, None, None, 12, None, 18, None, None, None, None, None, 24, 26, 31, 33, 36])) == 240


