def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 4, None, None, 3]),k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 4, None, None, 3]),k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6, 7]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6, 7]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6]),k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6]),k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6, 7, None, None, None, 8]),k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6, 7, None, None, None, 8]),k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2]),k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2]),k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7]),k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7]),k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 6, 1, None, None, None, None, 4, 3, None, None, None, None, None]),k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 6, 1, None, None, None, None, 4, 3, None, None, None, None, None]),k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),k = 16) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),k = 16) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]),k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]),k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, 21, 22, None, None, None, None, None, 23, 24, None, None, 25, 26, 27, 28, None, None, 29, 30, None, None, None, None, None, 31, None, None, 32, 33]),k = 15) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, 21, 22, None, None, None, None, None, 23, 24, None, None, 25, 26, 27, 28, None, None, 29, 30, None, None, None, None, None, 31, None, None, 32, 33]),k = 15) == 24: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),k = 12) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),k = 12) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 14) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 14) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),k = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),k = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9, 10, 11]),k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9, 10, 11]),k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 7, 3, 2, None, 6, 4, None, None, None, None, None, None, 8]),k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 7, 3, 2, None, 6, 4, None, None, None, None, None, None, 8]),k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9]),k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9]),k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, None, 6, 10, 11, None, None, None, None, None, 12, None, None, 13, None, None, 14, None, None, 15]),k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, None, 6, 10, 11, None, None, None, None, None, 12, None, None, 13, None, None, 14, None, None, 15]),k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),k = 17) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),k = 17) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),k = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),k = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, 3, 7, None, 18, None, None, None, 9, None, 11]),k = 20) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, 3, 7, None, 18, None, None, None, 9, None, 11]),k = 20) == 35: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, None, 11, 14, None, None, None, None, None, None, None, None, 13]),k = 15) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, None, 11, 14, None, None, None, None, None, None, None, None, 13]),k = 15) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 9, 20, 5, 12, None, 22, 3, 7, None, 14, None, None, 6, 8]),k = 12) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 9, 20, 5, 12, None, 22, 3, 7, None, 14, None, None, 6, 8]),k = 12) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, None, 2, None, None, 5]),k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, None, 2, None, None, 5]),k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30]),k = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30]),k = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 15) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 15) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, None, None, None, None]),k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, None, None, None, None]),k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, None, None, None, None, None, 20]),k = 7) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, None, None, None, None, None, 20]),k = 7) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),k = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),k = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, 7, 8, None, None, 9, 10, None, None, 11, 12]),k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, 7, 8, None, None, 9, 10, None, None, 11, 12]),k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9, 10, 11]),k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9, 10, 11]),k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),k = 32) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),k = 32) == 32: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 80, 5, 15, 30, 40, 55, 65, 70, 85, 1, 7, 12, 18, 28, 33, 45, 53, 63, 72, 83, 90, 95]),k = 35) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 80, 5, 15, 30, 40, 55, 65, 70, 85, 1, 7, 12, 18, 28, 33, 45, 53, 63, 72, 83, 90, 95]),k = 35) == 28: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, None, None, None, 9]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, None, None, None, 9]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 7, None, 2, None, 6, 3, None, None, None, None, 8, 4]),k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 7, None, 2, None, 6, 3, None, None, None, None, 8, 4]),k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 8, None, 11, 13, 17, None, 19, None, None, None, 20, None, None, None, None, None, None, 21]),k = 12) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 8, None, 11, 13, 17, None, 19, None, None, None, 20, None, None, None, None, None, None, 21]),k = 12) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 19, 21, 26, None, 13, 14, None, None, None, None, None, 23, 24]),k = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 19, 21, 26, None, 13, 14, None, None, None, None, None, 23, 24]),k = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 1, 3, 7, 9, None, None, 4, 5, None, None, None, None, 10]),k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 1, 3, 7, 9, None, None, 4, 5, None, None, None, None, 10]),k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 1]),k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 1]),k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, None, None, None, None, 12, 18, 11, 13, 16, 19]),k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, None, None, None, None, 12, 18, 11, 13, 16, 19]),k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, None, 8, 9]),k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, None, 8, 9]),k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),k = 12) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),k = 12) == 24: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16]),k = 14) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16]),k = 14) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 2, 5, None, 3, None, 6, 1, 4, None, None, None, 8]),k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 2, 5, None, 3, None, 6, 1, 4, None, None, None, 8]),k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, None, 10, 11]),k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, None, 10, 11]),k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 6, None, 7, 8, None, 11, 9, 12, 13, None, None, None, None, None, None, None, 14, 15, None, None, 16, 17]),k = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 6, None, 7, 8, None, 11, 9, 12, 13, None, None, None, None, None, None, None, 14, 15, None, None, 16, 17]),k = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, None, 11, 13, None, None, None, None, None, None, None, 8]),k = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, None, 11, 13, None, None, None, None, None, None, None, 8]),k = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),k = 30) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),k = 30) == 60: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 7, 3, 6, 9, 11, 2, 4, None, 8, None, None, None, None, None, None, None, None, 12, 13]),k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 7, 3, 6, 9, 11, 2, 4, None, 8, None, None, None, None, None, None, None, None, 12, 13]),k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, None, None, 10, 11, 12, None, 13, None, None, 14]),k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, None, None, 10, 11, 12, None, 13, None, None, 14]),k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 16, 19]),k = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 16, 19]),k = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, 5, 8]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, 5, 8]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 8]),k = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 8]),k = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13, None, None, None, None, None, None, None, 2, 5, 11, 12]),k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13, None, None, None, None, None, None, None, 2, 5, 11, 12]),k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190, 5, 15, 28, 40, 55, 65, 80, 95, 105, 115, 135, 145, 155, 165, 185, 195]),k = 125) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190, 5, 15, 28, 40, 55, 65, 80, 95, 105, 115, 135, 145, 155, 165, 185, 195]),k = 125) == 105: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 12) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 12) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9]),k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9]),k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, 8, 9, None, None, None, None, 10, None, 11, None, 12]),k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, 8, 9, None, None, None, None, 10, None, 11, None, 12]),k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14]),k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14]),k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, None, None, None, 10, None, None, None, None, 11, None, None, 12, None, None, None, None, 13]),k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, None, None, None, 10, None, None, None, None, 11, None, None, 12, None, None, None, None, 13]),k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6]),k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6]),k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15]),k = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15]),k = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, None]),k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, None]),k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 7, 14, 4, None, 13, 6, 3, 5, 11, None, None, None, None, 8]),k = 14) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 7, 14, 4, None, 13, 6, 3, 5, 11, None, None, None, None, 8]),k = 14) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 4, None, 3, None, 9, 1, None, None, None, 7, 8]),k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 4, None, 3, None, 9, 1, None, None, None, 7, 8]),k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, None, None, None, None, 7]),k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, None, None, None, None, 7]),k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9, 10]),k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9, 10]),k = 2) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),k = 4) == 5
    assert candidate(root = tree_node([2, 1, 4, None, None, 3]),k = 1) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6, 7]),k = 3) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6]),k = 2) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6, 7, None, None, None, 8]),k = 4) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),k = 3) == 5
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),k = 2) == 2
    assert candidate(root = tree_node([1]),k = 1) == 1
    assert candidate(root = tree_node([1, 3, 2]),k = 1) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7]),k = 3) == 5
    assert candidate(root = tree_node([5, 2, 6, 1, None, None, None, None, 4, 3, None, None, None, None, None]),k = 2) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),k = 16) == 16
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]),k = 3) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, 21, 22, None, None, None, None, None, 23, 24, None, None, 25, 26, 27, 28, None, None, 29, 30, None, None, None, None, None, 31, None, None, 32, 33]),k = 15) == 24
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),k = 12) == 15
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 14) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),k = 45) == 45
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9, 10, 11]),k = 4) == 4
    assert candidate(root = tree_node([5, 1, 7, 3, 2, None, 6, 4, None, None, None, None, None, None, 8]),k = 1) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 8) == 8
    assert candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9]),k = 4) == 6
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, None, 6, 10, 11, None, None, None, None, None, 12, None, None, 13, None, None, 14, None, None, 15]),k = 3) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),k = 17) == 17
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),k = 25) == 25
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),k = 11) == 11
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, 35, 3, 7, None, 18, None, None, None, 9, None, 11]),k = 20) == 35
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, None, 11, 14, None, None, None, None, None, None, None, None, 13]),k = 15) == 18
    assert candidate(root = tree_node([15, 9, 20, 5, 12, None, 22, 3, 7, None, 14, None, None, 6, 8]),k = 12) == 14
    assert candidate(root = tree_node([3, 1, 4, None, None, 2, None, None, 5]),k = 5) == 5
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30]),k = 30) == 30
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 15) == 18
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, None, None, None, None]),k = 4) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 7) == 14
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, None, None, None, None, None, 20]),k = 7) == 20
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),k = 15) == 30
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, 7, 8, None, None, 9, 10, None, None, 11, 12]),k = 6) == 6
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 7) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 7) == 14
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, 9, 10, 11]),k = 9) == 9
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),k = 32) == 32
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 80, 5, 15, 30, 40, 55, 65, 70, 85, 1, 7, 12, 18, 28, 33, 45, 53, 63, 72, 83, 90, 95]),k = 35) == 28
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, None, None, None, 9]),k = 3) == 3
    assert candidate(root = tree_node([5, 1, 7, None, 2, None, 6, 3, None, None, None, None, 8, 4]),k = 1) == 6
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 8, None, 11, 13, 17, None, 19, None, None, None, 20, None, None, None, None, None, None, 21]),k = 12) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),k = 15) == 15
    assert candidate(root = tree_node([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5]),k = 2) == 1
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 19, 21, 26, None, 13, 14, None, None, None, None, None, 23, 24]),k = 15) == 12
    assert candidate(root = tree_node([6, 2, 8, 1, 3, 7, 9, None, None, 4, 5, None, None, None, None, 10]),k = 7) == 7
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 1]),k = 2) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 5) == 10
    assert candidate(root = tree_node([20, 10, 30, 5, 15, None, None, None, None, 12, 18, 11, 13, 16, 19]),k = 10) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, None, 8, 9]),k = 6) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),k = 12) == 24
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16]),k = 14) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 15) == 15
    assert candidate(root = tree_node([7, 2, 5, None, 3, None, 6, 1, 4, None, None, None, 8]),k = 6) == 6
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),k = 1) == 1
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),k = 5) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, None, 10, 11]),k = 4) == 8
    assert candidate(root = tree_node([10, 5, 6, None, 7, 8, None, 11, 9, 12, 13, None, None, None, None, None, None, None, 14, 15, None, None, 16, 17]),k = 12) == 12
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, None, 11, 13, None, None, None, None, None, None, None, 8]),k = 15) == 12
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),k = 30) == 60
    assert candidate(root = tree_node([5, 1, 7, 3, 6, 9, 11, 2, 4, None, 8, None, None, None, None, None, None, None, None, 12, 13]),k = 3) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, None, None, 10, 11, 12, None, 13, None, None, 14]),k = 10) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 8) == 8
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 16, 19]),k = 7) == 6
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, 5, 8]),k = 3) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),k = 5) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 8]),k = 7) == 6
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13, None, None, None, None, None, None, None, 2, 5, 11, 12]),k = 8) == 1
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190, 5, 15, 28, 40, 55, 65, 80, 95, 105, 115, 135, 145, 155, 165, 185, 195]),k = 125) == 105
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),k = 5) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, None, None, None, None, None, 17]),k = 12) == 17
    assert candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9]),k = 6) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),k = 10) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, 8, 9, None, None, None, None, 10, None, 11, None, 12]),k = 7) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14]),k = 5) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, None, None, None, 10, None, None, None, None, 11, None, None, 12, None, None, None, None, 13]),k = 2) == 8
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6]),k = 3) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),k = 5) == 11
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),k = 15) == 15
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15]),k = 6) == 8
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, None]),k = 6) == 6
    assert candidate(root = tree_node([12, 7, 14, 4, None, 13, 6, 3, 5, 11, None, None, None, None, 8]),k = 14) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),k = 10) == 20
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),k = 2) == 0
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),k = 2) == 1
    assert candidate(root = tree_node([5, 2, 4, None, 3, None, 9, 1, None, None, None, 7, 8]),k = 2) == 9
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, None, None, None, None, 7]),k = 5) == 6
    assert candidate(root = tree_node([1, 2, None, 4, 5, 6, None, None, 7, None, None, 8, None, 9, 10]),k = 2) == 6


