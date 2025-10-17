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
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 48, None, None, 12, 49])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 48, None, None, 12, 49])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([90, 69, None, 49, 89, None, 52])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([90, 69, None, 49, 89, None, 52])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, None, 1, 3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, None, 1, 3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 47, 55])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 47, 55])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([88, 44, 132, 22, 66, 110, 154, 11, 33, 55, 77, 88, 99, 121, 143])) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([88, 44, 132, 22, 66, 110, 154, 11, 33, 55, 77, 88, 99, 121, 143])) == -11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 115, 140, 160, 185])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 115, 140, 160, 185])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 42, 48, 55, 1, 8, 14, 16, 19, 23, 28, 33, 37, 41, 44, 46, 49, 53, 52, 56, 58, 59, 60])) == -57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 42, 48, 55, 1, 8, 14, 16, 19, 23, 28, 33, 37, 41, 44, 46, 49, 53, 52, 56, 58, 59, 60])) == -57: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, None, 6, None, None, 4, 7, 9, 12])) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, None, 6, None, None, 4, 7, 9, 12])) == -6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, None, 0])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, None, 0])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 33, 37, 1, None, None, None, None, 13, None, None, 21, 27, None, 31, 36, None, None, None, 14, 17, None, 23, 26, 32, 34, None, None, None, None, None, None, None, None, 16])) == -13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 33, 37, 1, None, None, None, None, 13, None, None, 21, 27, None, 31, 36, None, None, None, 14, 17, None, 23, 26, 32, 34, None, None, None, None, None, None, None, None, 16])) == -13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([27, 18, 35, 12, 24, 30, 40, 9, 15, 21, 26, 28, 33, 38, 45])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([27, 18, 35, 12, 24, 30, 40, 9, 15, 21, 26, 28, 33, 38, 45])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 13, None, 7, 10, 18, None, None, 9, 12, 15, 20])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 13, None, 7, 10, 18, None, None, 9, 12, 15, 20])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 85, 95])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 85, 95])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([70, 30, 110, 10, 50, 90, 130, 5, 25, 40, 60, 80, 100, 120, 140])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([70, 30, 110, 10, 50, 90, 130, 5, 25, 40, 60, 80, 100, 120, 140])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, None, None, 30, 45, 55, 70, None, None, None, None, 35, 42, 52, 65, 68, 72, 85, 87, 95])) == -53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, None, None, 30, 45, 55, 70, None, None, None, None, 35, 42, 52, 65, 68, 72, 85, 87, 95])) == -53: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 15, 45, 75, 105, 5, 25, 35, 50, 65, 85, 95, 110, 3, 10, 20, 32, 40, 48, 55, 63, 68, 72, 80, 88, 92, 98, 102, 108, 113, 115, 118, 120])) == -110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 15, 45, 75, 105, 5, 25, 35, 50, 65, 85, 95, 110, 3, 10, 20, 32, 40, 48, 55, 63, 68, 72, 80, 88, 92, 98, 102, 108, 113, 115, 118, 120])) == -110: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([33, 16, 50, 13, 18, 45, 55, 8, 14, 17, 22, 40, 48, 52, 60])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([33, 16, 50, 13, 18, 45, 55, 8, 14, 17, 22, 40, 48, 52, 60])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 10, 2, 4, None, 15, 1, None, 6, 8, 13, 18])) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 10, 2, 4, None, 15, 1, None, 6, 8, 13, 18])) == -3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, None, 4, 9, 12, None, None, 7])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, None, 4, 9, 12, None, None, 7])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, 0, 4, 2, 5, None, None, None, 6, None, None, 7, 8, None, None, 9, 10])) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, 0, 4, 2, 5, None, None, None, 6, None, None, 7, 8, None, None, 9, 10])) == -5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([35, 18, 45, 12, 23, 40, 50, 8, 16, 20, 25, 38, 43, 48, 55, 5, 11, 14, 17, 19, 22, 24, 27, 32, 37, 42, 47, 49, 54, 57, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 41])) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([35, 18, 45, 12, 23, 40, 50, 8, 16, 20, 25, 38, 43, 48, 55, 5, 11, 14, 17, 19, 22, 24, 27, 32, 37, 42, 47, 49, 54, 57, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 41])) == -4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 4, 3, 5, 7, 9, 6, 8, 10])) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 4, 3, 5, 7, 9, 6, 8, 10])) == -6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([27, 14, 35, 10, 19, 31, 42, 4, 13, 17, 23, 29, 34, 39, 40, 1, 7, 12, 16, 18, 22, 25, 26, 28, 32, 36, 38, 41, 43, 44, 45, 46, 47, 48, 49, 50])) == -45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([27, 14, 35, 10, 19, 31, 42, 4, 13, 17, 23, 29, 34, 39, 40, 1, 7, 12, 16, 18, 22, 25, 26, 28, 32, 36, 38, 41, 43, 44, 45, 46, 47, 48, 49, 50])) == -45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 10, 45, 5, 20, 35, 50, 1, 7, 15, 25, 32, 37, 47, 55, None, 8, None, None, None, None, None, 22, None, None, None, None, 27, 40, 48, None, None, None, None, None, None, 52])) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 10, 45, 5, 20, 35, 50, 1, 7, 15, 25, 32, 37, 47, 55, None, 8, None, None, None, None, None, 22, None, None, None, None, 27, 40, 48, None, None, None, None, None, None, 52])) == -18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 23, 27, 32, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 23, 27, 32, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 10, 45, 75, 105, None, None, 35, 50, 70, 80, None, None, 55, None, None, None, None, 95, 100, 110, None, None, None, None, None, None, None, 115])) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 10, 45, 75, 105, None, None, 35, 50, 70, 80, None, None, 55, None, None, None, None, 95, 100, 110, None, None, None, None, None, None, None, 115])) == -25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, None, None, None, 9, None, None, 18, None, 23, 33, 43, 47, None, None, None, 27, None, None, 37, 41, 44, None, None, None, 46])) == -17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, None, None, None, 9, None, None, 18, None, 23, 33, 43, 47, None, None, None, 27, None, None, 37, 41, 44, None, None, None, 46])) == -17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, None, 16, 19])) == -13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, None, 16, 19])) == -13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 32, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 32, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 8, 12, 22, 28, 32, 40])) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 8, 12, 22, 28, 32, 40])) == -3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 10, 40, 5, 20, 35, 50, 3, 7, 15, 23, 30, 38, 45, 55])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 10, 40, 5, 20, 35, 50, 3, 7, 15, 23, 30, 38, 45, 55])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100000, 50000, 150000, 25000, 75000, None, 200000])) == 25000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100000, 50000, 150000, 25000, 75000, None, 200000])) == 25000: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([22, 15, 30, 10, 20, 25, 40, 5, 12, 18, 23, 27, 35, 37, 45])) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([22, 15, 30, 10, 20, 25, 40, 5, 12, 18, 23, 27, 35, 37, 45])) == -5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 13, 18, 12, 14, 16, 19])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 13, 18, 12, 14, 16, 19])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 45, 65, 80, 95, 105, 5, 15, None, 32, None, None, 55, 75, 85, 98, 103, 110, 1, None, None, 12, None, None, 33, None, None, None, None, 62, None, None, 72, None, None, 82, None, None, 102, None, 108, None, None, 107, None, 109, 111])) == -107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 45, 65, 80, 95, 105, 5, 15, None, 32, None, None, 55, 75, 85, 98, 103, 110, 1, None, None, 12, None, None, 33, None, None, None, None, 62, None, None, 72, None, None, 82, None, None, 102, None, 108, None, None, 107, None, 109, 111])) == -107: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 47, 55, 3, 7, 11, 16, 19, 23, 28, 33, 38, 42, 46, 49, 52, 57, 60, 65, 70, 2, 8, 13, 17, 21, 26, 31, 37, 41, 44, 48, 51, 54, 59, 63, 67, 71, 62, 66, 72, 69, 73])) == -67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 47, 55, 3, 7, 11, 16, 19, 23, 28, 33, 38, 42, 46, 49, 52, 57, 60, 65, 70, 2, 8, 13, 17, 21, 26, 31, 37, 41, 44, 48, 51, 54, 59, 63, 67, 71, 62, 66, 72, 69, 73])) == -67: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 1, None, None, 10])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 1, None, None, 10])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 20, 30, 40, 55, 65, 80, 95])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 20, 30, 40, 55, 65, 80, 95])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 85, 110, 140, 160, 185])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 85, 110, 140, 160, 185])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 9, 21, 7, 11, 19, 25, 6, 8, 10, 12, 18, 20, 24, 26])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 9, 21, 7, 11, 19, 25, 6, 8, 10, 12, 18, 20, 24, 26])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 2.5])) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 2.5])) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 1, 4, 6, 8, None, None, 2, None, None, None, None, None])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 1, 4, 6, 8, None, None, 2, None, None, None, None, None])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 99, 101, 98, 102, 97, 103, 96, 104, 95, 105, 94, 106, 93, 107, 92, 108, 91, 109, 90, 110, 89, 111, 88, 112, 87, 113, 86, 114, 85, 115])) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 99, 101, 98, 102, 97, 103, 96, 104, 95, 105, 94, 106, 93, 107, 92, 108, 91, 109, 90, 110, 89, 111, 88, 112, 87, 113, 86, 114, 85, 115])) == -18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, None, 1, 4, 6, 8, 12, 14, 11])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, None, 1, 4, 6, 8, 12, 14, 11])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 190])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 190])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375])) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375])) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 65, 85, 5, 15, 30, 40, 60, 70, 80, 90, 2, 8, 20, 32, 45, 55, 63, 68, 73, 78, 82, 87, 92, 3, 12, 18, 28, 42, 48, 53, 58, 62, 67, 72, 77, 81, 86, 91, 93])) == -77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 65, 85, 5, 15, 30, 40, 60, 70, 80, 90, 2, 8, 20, 32, 45, 55, 63, 68, 73, 78, 82, 87, 92, 3, 12, 18, 28, 42, 48, 53, 58, 62, 67, 72, 77, 81, 86, 91, 93])) == -77: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938])) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938])) == 62: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 292, 438, 563, 713, 813, 938])) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 292, 438, 563, 713, 813, 938])) == 37: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 20, None, None, 15, 25, None, None, None, 30, None, 35])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 20, None, None, 15, 25, None, None, None, 30, None, 35])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 27, 32, 40])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 27, 32, 40])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([42, 21, 63, 10, 31, 52, 74, 5, 15, 26, 36, 47, 57, 67, 83])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([42, 21, 63, 10, 31, 52, 74, 5, 15, 26, 36, 47, 57, 67, 83])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 17, 23, 27, 32, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 17, 23, 27, 32, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == -2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 8, 11, 14, 16, 19, 22, 27, 33, 43, 47, 49])) == -42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 8, 11, 14, 16, 19, 22, 27, 33, 43, 47, 49])) == -42: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 9, 2, 4, None, 10, None, 1, None, None, None, None, 6, 11])) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 9, 2, 4, None, 10, None, 1, None, None, None, None, 6, 11])) == -8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([77, 50, 100, 30, 60, 80, 110, 20, 40, 55, 65, 75, 90, 105, 120])) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([77, 50, 100, 30, 60, 80, 110, 20, 40, 55, 65, 75, 90, 105, 120])) == -2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([66, 33, 99, 16, 49, 82, 116, 8, 24, 41, 58, 69, 76, 106, 129])) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([66, 33, 99, 16, 49, 82, 116, 8, 24, 41, 58, 69, 76, 106, 129])) == -6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 2, 7, 12, 20, 1, None, None, 8, None, None, None, 9])) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 2, 7, 12, 20, 1, None, None, 8, None, None, None, 9])) == -11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 2, 7, None, 18, None, None, 6, 8])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 2, 7, None, 18, None, None, 6, 8])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, 4, 10, 20, None, None, 8, 12, 18, 25, None, None, 16, 19, 22, 27, None, None, None, None, None, 17, 21, 23, 26, 28, None, None, None, None, None, None, 14, None, None, None, None, None, 6, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None, None, 9, None, None, None, None, None, None, 11])) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, 4, 10, 20, None, None, 8, 12, 18, 25, None, None, 16, 19, 22, 27, None, None, None, None, None, 17, 21, 23, 26, 28, None, None, None, None, None, None, 14, None, None, None, None, None, 6, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None, None, 9, None, None, None, None, None, None, 11])) == -8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 69, 81, 93, 3, 9, 15, 21, 27, 34, 40, 48, 52, 60, 65, 72, 78, 84, 90, 96])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 69, 81, 93, 3, 9, 15, 21, 27, 34, 40, 48, 52, 60, 65, 72, 78, 84, 90, 96])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180, 5, 15, 28, 40, 55, 105, 120, 140, 170, 190, 3, None, 8, None, 13, None, None, None, None, None, None, None, 53, None, None, 95, None, None, 108, None, None, 135, None, None, None, None, None, None, 185, None, None, None])) == -177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180, 5, 15, 28, 40, 55, 105, 120, 140, 170, 190, 3, None, 8, None, 13, None, None, None, None, None, None, None, 53, None, None, 95, None, None, 108, None, None, 135, None, None, None, None, None, None, 185, None, None, None])) == -177: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 32, 38])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 32, 38])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 12, 20, 11, 13, None, 19, 18, 21, 17, 22])) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 12, 20, 11, 13, None, 19, 18, 21, 17, 22])) == -9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 5, 20, 3, 7, 16, 24, 1, 4, 6, 8, 14, 18, 22, 25, None, None, None, None, None, None, None, None, None, None, None, 17, 19, 21, 23, 26, 27])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 5, 20, 3, 7, 16, 24, 1, 4, 6, 8, 14, 18, 22, 25, None, None, None, None, None, None, None, None, None, None, None, 17, 19, 21, 23, 26, 27])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 32, 38])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 32, 38])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 9, 21, 7, 12, 18, 25, 5, 8, 10, 14, 17, 20, 23, 27])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 9, 21, 7, 12, 18, 25, 5, 8, 10, 14, 17, 20, 23, 27])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 115, 140, 160, 185, 5, 12, 20, 28, 52, 70, 80, 90, 105, 110, 130, 135, 145, 155, 165, 170, 180, 190, 195, 200])) == -183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 115, 140, 160, 185, 5, 12, 20, 28, 52, 70, 80, 90, 105, 110, 130, 135, 145, 155, 165, 170, 180, 190, 195, 200])) == -183: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 12, 18, 22, 28, None, None, None, None, 11, 13, None, 17, 19, 21, 23, 27, 29])) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 12, 18, 22, 28, None, None, None, None, 11, 13, None, 17, 19, 21, 23, 27, 29])) == -18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([45, 20, 65, 10, 30, 55, 75, 5, 15, 25, 35, 50, 60, 70, 80])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([45, 20, 65, 10, 30, 55, 75, 5, 15, 25, 35, 50, 60, 70, 80])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15, 17])) == -16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15, 17])) == -16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 3, 8, 13, 18, 22, 33, 38, 44, 46, 48, 49, 51])) == -42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 3, 8, 13, 18, 22, 33, 38, 44, 46, 48, 49, 51])) == -42: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 13, 17, None, 28, 32, 40])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 13, 17, None, 28, 32, 40])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 15, 1, 7, 12, 20, None, None, None, None, None, None, 10, 14, 16, 25, None, None, None, None, None, None, 22, 23, 26, 28])) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 15, 1, 7, 12, 20, None, None, None, None, None, None, 10, 14, 16, 25, None, None, None, None, None, None, 22, 23, 26, 28])) == -6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([4, 2, 6, 1, 3])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 2
    assert candidate(root = tree_node([2, 1, 3])) == 1
    assert candidate(root = tree_node([1, 0, 48, None, None, 12, 49])) == 1
    assert candidate(root = tree_node([90, 69, None, 49, 89, None, 52])) == 1
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9])) == 1
    assert candidate(root = tree_node([4, 2, None, 1, 3])) == 1
    assert candidate(root = tree_node([50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90])) == 5
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 1
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 42, 47, 55])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180])) == 5
    assert candidate(root = tree_node([88, 44, 132, 22, 66, 110, 154, 11, 33, 55, 77, 88, 99, 121, 143])) == -11
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 115, 140, 160, 185])) == 5
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 42, 48, 55, 1, 8, 14, 16, 19, 23, 28, 33, 37, 41, 44, 46, 49, 53, 52, 56, 58, 59, 60])) == -57
    assert candidate(root = tree_node([8, 3, 10, None, 6, None, None, 4, 7, 9, 12])) == -6
    assert candidate(root = tree_node([2, 1, None, 0])) == 1
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 1
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == -1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 33, 37, 1, None, None, None, None, 13, None, None, 21, 27, None, 31, 36, None, None, None, 14, 17, None, 23, 26, 32, 34, None, None, None, None, None, None, None, None, 16])) == -13
    assert candidate(root = tree_node([27, 18, 35, 12, 24, 30, 40, 9, 15, 21, 26, 28, 33, 38, 45])) == 1
    assert candidate(root = tree_node([8, 3, 13, None, 7, 10, 18, None, None, 9, 12, 15, 20])) == 1
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180])) == 5
    assert candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 85, 95])) == 5
    assert candidate(root = tree_node([70, 30, 110, 10, 50, 90, 130, 5, 25, 40, 60, 80, 100, 120, 140])) == 5
    assert candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, None, None, 30, 45, 55, 70, None, None, None, None, 35, 42, 52, 65, 68, 72, 85, 87, 95])) == -53
    assert candidate(root = tree_node([60, 30, 90, 15, 45, 75, 105, 5, 25, 35, 50, 65, 85, 95, 110, 3, 10, 20, 32, 40, 48, 55, 63, 68, 72, 80, 88, 92, 98, 102, 108, 113, 115, 118, 120])) == -110
    assert candidate(root = tree_node([33, 16, 50, 13, 18, 45, 55, 8, 14, 17, 22, 40, 48, 52, 60])) == 1
    assert candidate(root = tree_node([5, 3, 10, 2, 4, None, 15, 1, None, 6, 8, 13, 18])) == -3
    assert candidate(root = tree_node([8, 3, 10, None, 4, 9, 12, None, None, 7])) == -1
    assert candidate(root = tree_node([2, 1, 3, 0, 4, 2, 5, None, None, None, 6, None, None, 7, 8, None, None, 9, 10])) == -5
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20])) == 2
    assert candidate(root = tree_node([35, 18, 45, 12, 23, 40, 50, 8, 16, 20, 25, 38, 43, 48, 55, 5, 11, 14, 17, 19, 22, 24, 27, 32, 37, 42, 47, 49, 54, 57, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 41])) == -4
    assert candidate(root = tree_node([1, 2, 4, 3, 5, 7, 9, 6, 8, 10])) == -6
    assert candidate(root = tree_node([27, 14, 35, 10, 19, 31, 42, 4, 13, 17, 23, 29, 34, 39, 40, 1, 7, 12, 16, 18, 22, 25, 26, 28, 32, 36, 38, 41, 43, 44, 45, 46, 47, 48, 49, 50])) == -45
    assert candidate(root = tree_node([30, 10, 45, 5, 20, 35, 50, 1, 7, 15, 25, 32, 37, 47, 55, None, 8, None, None, None, None, None, 22, None, None, None, None, 27, 40, 48, None, None, None, None, None, None, 52])) == -18
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 23, 27, 32, 37])) == 2
    assert candidate(root = tree_node([60, 30, 90, 10, 45, 75, 105, None, None, 35, 50, 70, 80, None, None, 55, None, None, None, None, 95, 100, 110, None, None, None, None, None, None, None, 115])) == -25
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, None, None, None, 9, None, None, 18, None, 23, 33, 43, 47, None, None, None, 27, None, None, 37, 41, 44, None, None, None, 46])) == -17
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, None, 16, 19])) == -13
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 23, 28, 32, 37])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 8, 12, 22, 28, 32, 40])) == -3
    assert candidate(root = tree_node([25, 10, 40, 5, 20, 35, 50, 3, 7, 15, 23, 30, 38, 45, 55])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == -10
    assert candidate(root = tree_node([100000, 50000, 150000, 25000, 75000, None, 200000])) == 25000
    assert candidate(root = tree_node([22, 15, 30, 10, 20, 25, 40, 5, 12, 18, 23, 27, 35, 37, 45])) == -5
    assert candidate(root = tree_node([10, 5, 15, None, None, 13, 18, 12, 14, 16, 19])) == 1
    assert candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 45, 65, 80, 95, 105, 5, 15, None, 32, None, None, 55, 75, 85, 98, 103, 110, 1, None, None, 12, None, None, 33, None, None, None, None, 62, None, None, 72, None, None, 82, None, None, 102, None, 108, None, None, 107, None, 109, 111])) == -107
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 47, 55, 3, 7, 11, 16, 19, 23, 28, 33, 38, 42, 46, 49, 52, 57, 60, 65, 70, 2, 8, 13, 17, 21, 26, 31, 37, 41, 44, 48, 51, 54, 59, 63, 67, 71, 62, 66, 72, 69, 73])) == -67
    assert candidate(root = tree_node([10, 1, None, None, 10])) == 0
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 20, 30, 40, 55, 65, 80, 95])) == 5
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 85, 110, 140, 160, 185])) == 10
    assert candidate(root = tree_node([15, 9, 21, 7, 11, 19, 25, 6, 8, 10, 12, 18, 20, 24, 26])) == 1
    assert candidate(root = tree_node([2, 1, 3, None, None, 2.5])) == 0.5
    assert candidate(root = tree_node([5, 3, 7, 1, 4, 6, 8, None, None, 2, None, None, None, None, None])) == -1
    assert candidate(root = tree_node([100, 99, 101, 98, 102, 97, 103, 96, 104, 95, 105, 94, 106, 93, 107, 92, 108, 91, 109, 90, 110, 89, 111, 88, 112, 87, 113, 86, 114, 85, 115])) == -18
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, None, 1, 4, 6, 8, 12, 14, 11])) == -10
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 190])) == 10
    assert candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375])) == 25
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 65, 85, 5, 15, 30, 40, 60, 70, 80, 90, 2, 8, 20, 32, 45, 55, 63, 68, 73, 78, 82, 87, 92, 3, 12, 18, 28, 42, 48, 53, 58, 62, 67, 72, 77, 81, 86, 91, 93])) == -77
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9])) == 1
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938])) == 62
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 292, 438, 563, 713, 813, 938])) == 37
    assert candidate(root = tree_node([10, 5, 20, None, None, 15, 25, None, None, None, 30, None, 35])) == 5
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 27, 32, 40])) == 2
    assert candidate(root = tree_node([42, 21, 63, 10, 31, 52, 74, 5, 15, 26, 36, 47, 57, 67, 83])) == 4
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 17, 23, 27, 32, 37])) == 2
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == -2
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 8, 11, 14, 16, 19, 22, 27, 33, 43, 47, 49])) == -42
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1])) == 1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == 1
    assert candidate(root = tree_node([5, 3, 9, 2, 4, None, 10, None, 1, None, None, None, None, 6, 11])) == -8
    assert candidate(root = tree_node([77, 50, 100, 30, 60, 80, 110, 20, 40, 55, 65, 75, 90, 105, 120])) == -2
    assert candidate(root = tree_node([66, 33, 99, 16, 49, 82, 116, 8, 24, 41, 58, 69, 76, 106, 129])) == -6
    assert candidate(root = tree_node([10, 5, 15, 2, 7, 12, 20, 1, None, None, 8, None, None, None, 9])) == -11
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 18, None, None, 6, 8])) == 1
    assert candidate(root = tree_node([7, 3, 15, None, 4, 10, 20, None, None, 8, 12, 18, 25, None, None, 16, 19, 22, 27, None, None, None, None, None, 17, 21, 23, 26, 28, None, None, None, None, None, None, 14, None, None, None, None, None, 6, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None, None, 9, None, None, None, None, None, None, 11])) == -8
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 69, 81, 93, 3, 9, 15, 21, 27, 34, 40, 48, 52, 60, 65, 72, 78, 84, 90, 96])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180, 5, 15, 28, 40, 55, 105, 120, 140, 170, 190, 3, None, 8, None, 13, None, None, None, None, None, None, None, 53, None, None, 95, None, None, 108, None, None, 135, None, None, None, None, None, None, 185, None, None, None])) == -177
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 32, 38])) == 2
    assert candidate(root = tree_node([10, 5, 15, None, None, 12, 20, 11, 13, None, 19, 18, 21, 17, 22])) == -9
    assert candidate(root = tree_node([12, 5, 20, 3, 7, 16, 24, 1, 4, 6, 8, 14, 18, 22, 25, None, None, None, None, None, None, None, None, None, None, None, 17, 19, 21, 23, 26, 27])) == -10
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == -1
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 32, 38])) == 2
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 5
    assert candidate(root = tree_node([15, 9, 21, 7, 12, 18, 25, 5, 8, 10, 14, 17, 20, 23, 27])) == 1
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 115, 140, 160, 185, 5, 12, 20, 28, 52, 70, 80, 90, 105, 110, 130, 135, 145, 155, 165, 170, 180, 190, 195, 200])) == -183
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 12, 18, 22, 28, None, None, None, None, 11, 13, None, 17, 19, 21, 23, 27, 29])) == -18
    assert candidate(root = tree_node([45, 20, 65, 10, 30, 55, 75, 5, 15, 25, 35, 50, 60, 70, 80])) == 5
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15, 17])) == -16
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 47, 3, 8, 13, 18, 22, 33, 38, 44, 46, 48, 49, 51])) == -42
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 13, 17, None, 28, 32, 40])) == 2
    assert candidate(root = tree_node([8, 3, 15, 1, 7, 12, 20, None, None, None, None, None, None, 10, 14, 16, 25, None, None, None, None, None, None, 22, 23, 26, 28])) == -6


