def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 6, 1, 3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 6, 1, 3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 30, None, 10, None, None, 15, None, 18])) == -29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 30, None, 10, None, None, 15, None, 18])) == -29: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([236, 104, 701, None, 227, None, 911])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([236, 104, 701, None, 227, None, 911])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 48, None, None, 12, 49])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 48, None, None, 12, 49])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 190])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 190])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 4, 6, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 4, 6, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 20, 80, 10, 30, 70, 90, 5, 15, 25, 35, 65, 75, 85, 95, 2, 8, 12, 18, 27, 33, 37, 55, 68, 72, 77, 82, 88, 92, 97, 98])) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 20, 80, 10, 30, 70, 90, 5, 15, 25, 35, 65, 75, 85, 95, 2, 8, 12, 18, 27, 33, 37, 55, 68, 72, 77, 82, 88, 92, 97, 98])) == -3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 21])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 21])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 10, 30, 5, 15, 26, 40, 2, 7, 12, 18, 27, 35, 38, 45])) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 10, 30, 5, 15, 26, 40, 2, 7, 12, 18, 27, 35, 38, 45])) == -5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 35, 43, 48, 55])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 35, 43, 48, 55])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 12, 20, 11, None, None, 14])) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 12, 20, 11, None, None, 14])) == -6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 10, 40, 80, 100, 5, 15, 35, 45, 75, 85, 95, 105])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 10, 40, 80, 100, 5, 15, 35, 45, 75, 85, 95, 105])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500, 1250, 3750, 5875, 8625, 11250, 15250, 16750, 18250])) == -250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500, 1250, 3750, 5875, 8625, 11250, 15250, 16750, 18250])) == -250: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 2, None, 11, 18, 1, None, None, 13])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 2, None, 11, 18, 1, None, None, 13])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([999, 499, 1499, 249, 749, 1249, 1749, 125, 375, 587, 862, 1124, 1524, 1674, 1824])) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([999, 499, 1499, 249, 749, 1249, 1749, 125, 375, 587, 862, 1124, 1524, 1674, 1824])) == -25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([150, 75, 225, 37, 112, 188, 263, 18, 56, 87, 100, 163, 200, 242, 284])) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([150, 75, 225, 37, 112, 188, 263, 18, 56, 87, 100, 163, 200, 242, 284])) == -12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 27, 32, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 27, 32, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 3, 15, None, 8, 12, 20, 4, 7, 11, 13, 18, 25])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 3, 15, None, 8, 12, 20, 4, 7, 11, 13, 18, 25])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 17])) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 17])) == -3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([70, 35, 105, 20, 50, 85, 125, 10, 25, 40, 60, 80, 90, 110, 130])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([70, 35, 105, 20, 50, 85, 125, 10, 25, 40, 60, 80, 90, 110, 130])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 30, 10, 18, 25, 35, 5, 12, 16, 19, 23, 27, 32, 38])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 30, 10, 18, 25, 35, 5, 12, 16, 19, 23, 27, 32, 38])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 37, 42, 47, 52])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 37, 42, 47, 52])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 28, 33, 38])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 28, 33, 38])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 22, 32, 42, 58, 68, 78, 88, 108, 118, 138, 158, 178, 190])) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 22, 32, 42, 58, 68, 78, 88, 108, 118, 138, 158, 178, 190])) == -12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([90, 45, 135, 20, 60, 110, 160, 10, 30, 50, 70, 100, 120, 140, 170])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([90, 45, 135, 20, 60, 110, 160, 10, 30, 50, 70, 100, 120, 140, 170])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 13, None, 7, 10, 18, None, None, 9, 11, None, 15, 19, 22])) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 13, None, 7, 10, 18, None, None, 9, 11, None, 15, 19, 22])) == -12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 13, None, 7, 10, 17, None, None, 9, 12, 14, 16, 18, 20])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 13, None, 7, 10, 17, None, None, 9, 12, 14, 16, 18, 20])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([250, 125, 375, 62, 188, 312, 438, 31, 93, 156, 220, 275, 356, 400, 480])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([250, 125, 375, 62, 188, 312, 438, 31, 93, 156, 220, 275, 356, 400, 480])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 33, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 33, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, None, None, 2, None, 11, 14])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, None, None, 2, None, 11, 14])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 50, 5, 20, 40, 60, 1, None, 15, 25, 35, 45, 55, 65])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 50, 5, 20, 40, 60, 1, None, 15, 25, 35, 45, 55, 65])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 8, 11, 14, 17, 22, 24, 30])) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 8, 11, 14, 17, 22, 24, 30])) == -2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 5, 20, 30, 40, 60, 70, 80, 90])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 5, 20, 30, 40, 60, 70, 80, 90])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 7, 9, 11, 13, 16, 18, 23, 27, 6, None, 10, None, 14, None, None, 19, 21, 26, 30, None, None, None, None, None, None, None, None, 1])) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 7, 9, 11, 13, 16, 18, 23, 27, 6, None, 10, None, 14, None, None, 19, 21, 26, 30, None, None, None, None, None, None, None, None, 1])) == -12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 55, 60])) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 55, 60])) == -5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 18, 23, 28, 33, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 18, 23, 28, 33, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, None, 4, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, None, 4, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, None, 6, 8, 17, 19])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, None, 6, 8, 17, 19])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 17, 22, 27, 32, 37, 42])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 17, 22, 27, 32, 37, 42])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 288, 469, 513, 688, 763, 938, 31, 94, 134, 225, 334, 409, 494, 569, 654, 729, 794, 859, 904, 964, 987])) == -141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 288, 469, 513, 688, 763, 938, 31, 94, 134, 225, 334, 409, 494, 569, 654, 729, 794, 859, 904, 964, 987])) == -141: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90, 3, 7, 12, 18, 28, 32, 45, 52, 63, 68, 77, 82, 88, 93, 2, 4, 6, 8, 11, 13, 14, 17, 19, 27, 29, 31, 33, 39, 43, 48, 51, 54, 57, 62, 67, 70, 76, 79, 81, 83, 87, 89, 92, 95, 97, 1, 9, 16, 20, 23, 26, 34, 36, 38, 41, 42, 44, 46, 47, 49, 50, 53, 56, 58, 59, 61, 64, 66, 69, 71, 72, 73, 74, 75, 78, 80, 84, 86, 91, 94, 96, 98, 99])) == -95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90, 3, 7, 12, 18, 28, 32, 45, 52, 63, 68, 77, 82, 88, 93, 2, 4, 6, 8, 11, 13, 14, 17, 19, 27, 29, 31, 33, 39, 43, 48, 51, 54, 57, 62, 67, 70, 76, 79, 81, 83, 87, 89, 92, 95, 97, 1, 9, 16, 20, 23, 26, 34, 36, 38, 41, 42, 44, 46, 47, 49, 50, 53, 56, 58, 59, 61, 64, 66, 69, 71, 72, 73, 74, 75, 78, 80, 84, 86, 91, 94, 96, 98, 99])) == -95: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 17, 2, 6, 12, 22, 1, 3, 5, 7, 11, 13, 18, 25])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 17, 2, 6, 12, 22, 1, 3, 5, 7, 11, 13, 18, 25])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35, 55, 65, 77, 85])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35, 55, 65, 77, 85])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, None, 5, 15, None, 25, 2, None, 13, 18, None, None, 16, None])) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, None, 5, 15, None, 25, 2, None, 13, 18, None, None, 16, None])) == -8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 58, 60, 72, 90])) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 58, 60, 72, 90])) == -3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 18])) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 18])) == -2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 62, 188, 312, 438, 563, 712, 813, 938])) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 62, 188, 312, 438, 563, 712, 813, 938])) == 38: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 15, 25, 35, 45, 65, 75, 85, 105])) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 15, 25, 35, 45, 65, 75, 85, 105])) == -5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, 98, 102, 97, None, 101, 103, 96, None, None, None, None, None, None])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, 98, 102, 97, None, 101, 103, 96, None, None, None, None, None, None])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([90, 60, 120, 30, 75, 100, 150, 20, 40, 65, 80, 95, 110, 140, 160])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([90, 60, 120, 30, 75, 100, 150, 20, 40, 65, 80, 95, 110, 140, 160])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 15, 25, 35, 45, 65, 75, 85, 95, 10, 18, 23, 32, 43, 58, 63, 72, 78, 83, 92, 98, 110, 120, 130, 140, 150])) == -140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 15, 25, 35, 45, 65, 75, 85, 95, 10, 18, 23, 32, 43, 58, 63, 72, 78, 83, 92, 98, 110, 120, 130, 140, 150])) == -140: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, None, 4, None, None, None, None, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, None, 4, None, None, None, None, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 12, 20, None, None, None, None, 13, 18])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 12, 20, None, None, None, None, 13, 18])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([70, 35, 105, 15, 50, 85, 120, 10, 25, 40, 60, 80, 90, 110, 130])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([70, 35, 105, 15, 50, 85, 120, 10, 25, 40, 60, 80, 90, 110, 130])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 180])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 180])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, 4, 9, 20, None, None, None, None, 18, 22])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, 4, 9, 20, None, None, None, None, 18, 22])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([90, 45, 135, 22, 67, 112, 178, 11, 33, 55, 82, 100, 123, 165, 190])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([90, 45, 135, 22, 67, 112, 178, 11, 33, 55, 82, 100, 123, 165, 190])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([75, 50, 100, 25, 62, 87, 125, 10, 38, 56, 65, 82, 93, 112, 138])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([75, 50, 100, 25, 62, 87, 125, 10, 38, 56, 65, 82, 93, 112, 138])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 48, 55])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 48, 55])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 13, 1, None, 7, 15, 0, 2, 6, 9, 14, 17, None, None, None, None, None, None, None, None])) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 13, 1, None, 7, 15, 0, 2, 6, 9, 14, 17, None, None, None, None, None, None, None, None])) == -2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, None, 10, 20, 18, 25])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, None, 10, 20, 18, 25])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([75, 40, 100, 30, 55, 85, 110, 20, 35, 50, 60, 80, 90, 105, 115])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([75, 40, 100, 30, 55, 85, 110, 20, 35, 50, 60, 80, 90, 105, 115])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 50, 5, 25, 40, 60, None, 15, None, 20, 35, 45, 55, 65])) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 50, 5, 25, 40, 60, None, 15, None, 20, 35, 45, 55, 65])) == -5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, None])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, None])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 33, 40])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 33, 40])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75, 1, 9, 13, 22, 28, 33, 42, 48, 53, 57, 63, 68, 73, 77, 80, 83, 88, 93, 98, 100])) == -90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75, 1, 9, 13, 22, 28, 33, 42, 48, 53, 57, 63, 68, 73, 77, 80, 83, 88, 93, 98, 100])) == -90: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, 49, 149, 24, 74, 124, 174, 12, 37, 62, 87, 112, 137, 162, 187, 6, 22, 31, 43, 56, 71, 82, 93, 103, 118, 132, 143, 158, 168, 178, 182, 193])) == -187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, 49, 149, 24, 74, 124, 174, 12, 37, 62, 87, 112, 137, 162, 187, 6, 22, 31, 43, 56, 71, 82, 93, 103, 118, 132, 143, 158, 168, 178, 182, 193])) == -187: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 15, 35, 60, 85, 10, 20, 30, 40, 55, 65, 80, 90])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 15, 35, 60, 85, 10, 20, 30, 40, 55, 65, 80, 90])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 20, 40, 10, None, 35, 45, 5, None, None, 38, None, 47])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 20, 40, 10, None, 35, 45, 5, None, None, 38, None, 47])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875, 63, 225, 313, 438, 563, 688, 763, 894, 1063, 1188, 1313, 1438, 1563, 1688, 1813, 1938])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875, 63, 225, 313, 438, 563, 688, 763, 894, 1063, 1188, 1313, 1438, 1563, 1688, 1813, 1938])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 49, 55])) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 49, 55])) == -2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([4, 2, 6, 1, 3])) == 1
    assert candidate(root = tree_node([1, 30, None, 10, None, None, 15, None, 18])) == -29
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([236, 104, 701, None, 227, None, 911])) == 9
    assert candidate(root = tree_node([5, 4, 7])) == 1
    assert candidate(root = tree_node([1, 0, 48, None, None, 12, 49])) == 1
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == 1
    assert candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90])) == 5
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 190])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 4, 6, 8])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 2
    assert candidate(root = tree_node([60, 20, 80, 10, 30, 70, 90, 5, 15, 25, 35, 65, 75, 85, 95, 2, 8, 12, 18, 27, 33, 37, 55, 68, 72, 77, 82, 88, 92, 97, 98])) == -3
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 21])) == 1
    assert candidate(root = tree_node([25, 10, 30, 5, 15, 26, 40, 2, 7, 12, 18, 27, 35, 38, 45])) == -5
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 35, 43, 48, 55])) == 2
    assert candidate(root = tree_node([10, 5, 15, None, None, 12, 20, 11, None, None, 14])) == -6
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 5
    assert candidate(root = tree_node([60, 30, 90, 10, 40, 80, 100, 5, 15, 35, 45, 75, 85, 95, 105])) == 5
    assert candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500, 1250, 3750, 5875, 8625, 11250, 15250, 16750, 18250])) == -250
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 1
    assert candidate(root = tree_node([10, 5, 15, 2, None, 11, 18, 1, None, None, 13])) == 1
    assert candidate(root = tree_node([999, 499, 1499, 249, 749, 1249, 1749, 125, 375, 587, 862, 1124, 1524, 1674, 1824])) == -25
    assert candidate(root = tree_node([150, 75, 225, 37, 112, 188, 263, 18, 56, 87, 100, 163, 200, 242, 284])) == -12
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 27, 32, 37])) == 2
    assert candidate(root = tree_node([9, 3, 15, None, 8, 12, 20, 4, 7, 11, 13, 18, 25])) == -1
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 17])) == -3
    assert candidate(root = tree_node([70, 35, 105, 20, 50, 85, 125, 10, 25, 40, 60, 80, 90, 110, 130])) == 5
    assert candidate(root = tree_node([20, 15, 30, 10, 18, 25, 35, 5, 12, 16, 19, 23, 27, 32, 38])) == 1
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 37, 42, 47, 52])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 28, 33, 38])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 22, 32, 42, 58, 68, 78, 88, 108, 118, 138, 158, 178, 190])) == -12
    assert candidate(root = tree_node([90, 45, 135, 20, 60, 110, 160, 10, 30, 50, 70, 100, 120, 140, 170])) == 5
    assert candidate(root = tree_node([8, 3, 13, None, 7, 10, 18, None, None, 9, 11, None, 15, 19, 22])) == -12
    assert candidate(root = tree_node([8, 3, 13, None, 7, 10, 17, None, None, 9, 12, 14, 16, 18, 20])) == -10
    assert candidate(root = tree_node([250, 125, 375, 62, 188, 312, 438, 31, 93, 156, 220, 275, 356, 400, 480])) == 19
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 33, 37])) == 2
    assert candidate(root = tree_node([15, 10, 20, 5, 12, None, None, 2, None, 11, 14])) == 1
    assert candidate(root = tree_node([30, 10, 50, 5, 20, 40, 60, 1, None, 15, 25, 35, 45, 55, 65])) == 4
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 8, 11, 14, 17, 22, 24, 30])) == -2
    assert candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 5, 20, 30, 40, 60, 70, 80, 90])) == 5
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 7, 9, 11, 13, 16, 18, 23, 27, 6, None, 10, None, 14, None, None, 19, 21, 26, 30, None, None, None, None, None, None, None, None, 1])) == -12
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 55, 60])) == -5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == -10
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 18, 23, 28, 33, 37])) == 2
    assert candidate(root = tree_node([2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 2, None, 6, 8, 17, 19])) == 1
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 17, 22, 27, 32, 37, 42])) == 2
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 288, 469, 513, 688, 763, 938, 31, 94, 134, 225, 334, 409, 494, 569, 654, 729, 794, 859, 904, 964, 987])) == -141
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90, 3, 7, 12, 18, 28, 32, 45, 52, 63, 68, 77, 82, 88, 93, 2, 4, 6, 8, 11, 13, 14, 17, 19, 27, 29, 31, 33, 39, 43, 48, 51, 54, 57, 62, 67, 70, 76, 79, 81, 83, 87, 89, 92, 95, 97, 1, 9, 16, 20, 23, 26, 34, 36, 38, 41, 42, 44, 46, 47, 49, 50, 53, 56, 58, 59, 61, 64, 66, 69, 71, 72, 73, 74, 75, 78, 80, 84, 86, 91, 94, 96, 98, 99])) == -95
    assert candidate(root = tree_node([9, 4, 17, 2, 6, 12, 22, 1, 3, 5, 7, 11, 13, 18, 25])) == 1
    assert candidate(root = tree_node([50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35, 55, 65, 77, 85])) == 2
    assert candidate(root = tree_node([20, 10, None, 5, 15, None, 25, 2, None, 13, 18, None, None, 16, None])) == -8
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 1, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 1
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90])) == 5
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 58, 60, 72, 90])) == -3
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 18])) == -2
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 62, 188, 312, 438, 563, 712, 813, 938])) == 38
    assert candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 15, 25, 35, 45, 65, 75, 85, 105])) == -5
    assert candidate(root = tree_node([99, 98, 102, 97, None, 101, 103, 96, None, None, None, None, None, None])) == 1
    assert candidate(root = tree_node([90, 60, 120, 30, 75, 100, 150, 20, 40, 65, 80, 95, 110, 140, 160])) == 5
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75])) == 5
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190])) == 10
    assert candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 15, 25, 35, 45, 65, 75, 85, 95, 10, 18, 23, 32, 43, 58, 63, 72, 78, 83, 92, 98, 110, 120, 130, 140, 150])) == -140
    assert candidate(root = tree_node([2, 1, 3, None, None, None, 4, None, None, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([10, 5, 15, None, None, 12, 20, None, None, None, None, 13, 18])) == 2
    assert candidate(root = tree_node([70, 35, 105, 15, 50, 85, 120, 10, 25, 40, 60, 80, 90, 110, 130])) == 5
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 180])) == 5
    assert candidate(root = tree_node([7, 3, 15, None, 4, 9, 20, None, None, None, None, 18, 22])) == 1
    assert candidate(root = tree_node([90, 45, 135, 22, 67, 112, 178, 11, 33, 55, 82, 100, 123, 165, 190])) == 8
    assert candidate(root = tree_node([75, 50, 100, 25, 62, 87, 125, 10, 38, 56, 65, 82, 93, 112, 138])) == 3
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 48, 55])) == 2
    assert candidate(root = tree_node([8, 3, 13, 1, None, 7, 15, 0, 2, 6, 9, 14, 17, None, None, None, None, None, None, None, None])) == -2
    assert candidate(root = tree_node([30, 15, None, 10, 20, 18, 25])) == -10
    assert candidate(root = tree_node([75, 40, 100, 30, 55, 85, 110, 20, 35, 50, 60, 80, 90, 105, 115])) == 5
    assert candidate(root = tree_node([30, 10, 50, 5, 25, 40, 60, None, 15, None, 20, 35, 45, 55, 65])) == -5
    assert candidate(root = tree_node([2, 1, None])) == 1
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85])) == 5
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 33, 40])) == 2
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75, 1, 9, 13, 22, 28, 33, 42, 48, 53, 57, 63, 68, 73, 77, 80, 83, 88, 93, 98, 100])) == -90
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == -1
    assert candidate(root = tree_node([99, 49, 149, 24, 74, 124, 174, 12, 37, 62, 87, 112, 137, 162, 187, 6, 22, 31, 43, 56, 71, 82, 93, 103, 118, 132, 143, 158, 168, 178, 182, 193])) == -187
    assert candidate(root = tree_node([50, 25, 75, 15, 35, 60, 85, 10, 20, 30, 40, 55, 65, 80, 90])) == 5
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 5
    assert candidate(root = tree_node([30, 20, 40, 10, None, 35, 45, 5, None, None, 38, None, 47])) == 2
    assert candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875, 63, 225, 313, 438, 563, 688, 763, 894, 1063, 1188, 1313, 1438, 1563, 1688, 1813, 1938])) == 13
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 49, 55])) == -2


