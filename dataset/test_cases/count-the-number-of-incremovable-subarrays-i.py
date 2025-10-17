def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 7, 8]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 7, 8]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6, 7]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6, 7]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 30]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 30]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 4]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 4]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 25, 40]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 25, 40]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 6, 7, 2, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 6, 7, 2, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 8, 7, 10, 9, 11, 13, 12]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 8, 7, 10, 9, 11, 13, 12]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 18, 25, 30, 35, 40]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 18, 25, 30, 35, 40]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 14, 16, 18, 20, 19, 21, 23, 25, 24, 26, 28, 30]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 14, 16, 18, 20, 19, 21, 23, 25, 24, 26, 28, 30]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 1, 3, 4, 5, 6, 7]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 1, 3, 4, 5, 6, 7]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 7, 9, 2, 11, 13, 12, 14]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 7, 9, 2, 11, 13, 12, 14]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10, 11]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10, 11]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 20, 30, 40, 30, 20, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 20, 30, 40, 30, 20, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 2, 7, 8, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 2, 7, 8, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 3, 4, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 3, 4, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 7, 8, 2, 3, 4, 5, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 7, 8, 2, 3, 4, 5, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 5, 4, 7, 8, 9, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 5, 4, 7, 8, 9, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 25, 40, 10, 20, 30]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 25, 40, 10, 20, 30]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9, 11]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9, 11]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 35, 40, 30, 45]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 35, 40, 30, 45]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 40, 50, 15, 25, 35, 45]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 40, 50, 15, 25, 35, 45]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 35, 40, 38, 45]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 35, 40, 38, 45]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 6, 7, 8, 9]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 6, 7, 8, 9]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 25, 15, 30, 35, 28, 40, 45, 50, 55, 60]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 25, 15, 30, 35, 28, 40, 45, 50, 55, 60]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 8]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 8]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 10, 12, 14, 16]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 10, 12, 14, 16]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 10, 8, 11, 12]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 10, 8, 11, 12]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 7, 5, 3, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 7, 5, 3, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 9, 7, 10, 11, 12, 13, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 9, 7, 10, 11, 12, 13, 6]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [6, 5, 7, 8]) == 7
    assert candidate(nums = [1, 3, 2, 4, 5]) == 11
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 4]) == 11
    assert candidate(nums = [1, 2, 2, 3]) == 8
    assert candidate(nums = [1, 2, 3, 4]) == 10
    assert candidate(nums = [1, 2]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7]) == 19
    assert candidate(nums = [10, 20, 15, 25, 30]) == 11
    assert candidate(nums = [1, 2, 3, 2, 3, 4]) == 13
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 3]) == 8
    assert candidate(nums = [8, 7, 6, 6]) == 3
    assert candidate(nums = [1, 2, 3, 3, 4]) == 11
    assert candidate(nums = [10, 20, 15, 30, 25, 40]) == 9
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10]) == 22
    assert candidate(nums = [5, 3, 4, 6, 7, 2, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]) == 22
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25
    assert candidate(nums = [3, 5, 2, 8, 7, 10, 9, 11, 13, 12]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == 26
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]) == 9
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == 29
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 71
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(nums = [5, 10, 15, 20, 18, 25, 30, 35, 40]) == 29
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 13
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 11
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 12
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 14, 16, 18, 20, 19, 21, 23, 25, 24, 26, 28, 30]) == 45
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]) == 6
    assert candidate(nums = [3, 1, 2, 1, 3, 4, 5, 6, 7]) == 12
    assert candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 12
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 11
    assert candidate(nums = [1, 2, 3, 2, 1]) == 5
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9
    assert candidate(nums = [1, 5, 3, 7, 9, 2, 11, 13, 12, 14]) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10, 11]) == 46
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 26
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13]) == 9
    assert candidate(nums = [30, 20, 10, 20, 30, 40, 30, 20, 10]) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4
    assert candidate(nums = [5, 6, 2, 7, 8, 10]) == 13
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(nums = [5, 1, 2, 3, 4, 5, 6]) == 9
    assert candidate(nums = [3, 5, 6, 7, 8, 2, 3, 4, 5, 6]) == 15
    assert candidate(nums = [1, 2, 3, 6, 5, 4, 7, 8, 9, 10]) == 29
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 10, 20, 30]) == 9
    assert candidate(nums = [3, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12]) == 28
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9, 11]) == 15
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 22
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 30, 45]) == 11
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
    assert candidate(nums = [2, 2, 2, 2, 2]) == 3
    assert candidate(nums = [10, 20, 30, 25, 40, 50, 15, 25, 35, 45]) == 17
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 38, 45]) == 12
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11]) == 43
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4
    assert candidate(nums = [1, 3, 5, 4, 6, 7, 8, 9]) == 23
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 17
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4]) == 10
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 41
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 3
    assert candidate(nums = [20, 25, 15, 30, 35, 28, 40, 45, 50, 55, 60]) == 21
    assert candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == 38
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == 42
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 5
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9]) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 9
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 29
    assert candidate(nums = [5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 81
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 7
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50]) == 9
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 11
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == 28
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 8]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 36
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 10, 12, 14, 16]) == 34
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 66
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 26
    assert candidate(nums = [1, 3, 5, 7, 9, 10, 8, 11, 12]) == 26
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 9
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 3
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5]) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 7, 5, 3, 1]) == 7
    assert candidate(nums = [8, 9, 7, 10, 11, 12, 13, 6]) == 4


