def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 1, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 1, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 20, 20, 10, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 20, 20, 10, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 4, 4, 4, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 4, 4, 4, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 3, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 3, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 3, 2, 1, 5, 3, 2, 1, 6, 3, 2, 1, 7, 3, 2, 1, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 3, 2, 1, 5, 3, 2, 1, 6, 3, 2, 1, 7, 3, 2, 1, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 5, 7, 5, 8, 5, 9, 5, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 5, 7, 5, 8, 5, 9, 5, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 100, 98, 100, 97, 100, 96, 100, 95, 100, 94, 100, 93, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 100, 98, 100, 97, 100, 96, 100, 95, 100, 94, 100, 93, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 10, 40, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 10, 40, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10, 7, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10, 7, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 3, 1, 2, 2, 1, 4, 4, 4, 4, 1, 2, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 3, 1, 2, 2, 1, 4, 4, 4, 4, 1, 2, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 9, 8, 10, 8, 11, 8, 12, 8, 13, 8, 14, 8, 15, 8, 16, 8, 17, 8, 18]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 9, 8, 10, 8, 11, 8, 12, 8, 13, 8, 14, 8, 15, 8, 16, 8, 17, 8, 18]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6, 9, 7, 9, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6, 9, 7, 9, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 1, 7, 7, 7, 7, 1, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 1, 7, 7, 7, 7, 1, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 3, 5, 7, 5, 3, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 3, 5, 7, 5, 3, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 1, 5, 1, 4, 5, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 1, 5, 1, 4, 5, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 10, 30, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 10, 30, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 2, 10, 3, 10, 4, 10, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 2, 10, 3, 10, 4, 10, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 2, 7, 3, 7, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 2, 7, 3, 7, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 3, 6, 1, 5, 3, 6, 1, 5, 3, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 3, 6, 1, 5, 3, 6, 1, 5, 3, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 10, 20, 10]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 1]) == 2
    assert candidate(nums = [10, 10, 1, 10, 10]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50]) == 2
    assert candidate(nums = [5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [1, 1, 2, 2, 1, 1]) == 1
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 1
    assert candidate(nums = [10, 1, 10, 1, 10]) == 1
    assert candidate(nums = [10, 10, 10, 20, 20, 10, 10, 10]) == 1
    assert candidate(nums = [3, 3, 3, 4, 4, 4, 3]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 2
    assert candidate(nums = [1, 2, 1, 2]) == 1
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3
    assert candidate(nums = [2, 1, 3, 3, 2]) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]) == 9
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 2, 2]) == 8
    assert candidate(nums = [3, 2, 1, 4, 3, 2, 1, 5, 3, 2, 1, 6, 3, 2, 1, 7, 3, 2, 1, 8]) == 2
    assert candidate(nums = [5, 6, 5, 7, 5, 8, 5, 9, 5, 10]) == 1
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 2
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1]) == 3
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3]) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1]) == 8
    assert candidate(nums = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 1
    assert candidate(nums = [100, 99, 100, 98, 100, 97, 100, 96, 100, 95, 100, 94, 100, 93, 100]) == 1
    assert candidate(nums = [10, 20, 10, 30, 10, 40, 10]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1]) == 2
    assert candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10, 7, 7]) == 3
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 1, 1, 1]) == 8
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 3
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 3, 1, 2, 2, 1, 4, 4, 4, 4, 1, 2, 2, 1]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 5
    assert candidate(nums = [8, 9, 8, 10, 8, 11, 8, 12, 8, 13, 8, 14, 8, 15, 8, 16, 8, 17, 8, 18]) == 1
    assert candidate(nums = [6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 2
    assert candidate(nums = [9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6, 9, 7, 9, 8]) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1]) == 5
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 9
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
    assert candidate(nums = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6]) == 1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3]) == 3
    assert candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7]) == 1
    assert candidate(nums = [7, 7, 1, 7, 7, 7, 7, 1, 7]) == 1
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 2]) == 8
    assert candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5]) == 1
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1]) == 2
    assert candidate(nums = [8, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 1
    assert candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 1
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 0, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [7, 5, 3, 5, 7, 5, 3, 5]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 3
    assert candidate(nums = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 5
    assert candidate(nums = [5, 1, 4, 1, 5, 1, 4, 5, 4, 5]) == 2
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
    assert candidate(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 1
    assert candidate(nums = [10, 20, 10, 30, 20, 10, 30, 20, 10]) == 1
    assert candidate(nums = [10, 1, 10, 2, 10, 3, 10, 4, 10, 5]) == 1
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 10, 10]) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 5
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 8
    assert candidate(nums = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5]) == 7
    assert candidate(nums = [7, 2, 2, 7, 3, 7, 3, 3]) == 1
    assert candidate(nums = [7, 1, 5, 3, 6, 1, 5, 3, 6, 1, 5, 3, 6]) == 2
    assert candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9]) == 1
    assert candidate(nums = [9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9]) == 1
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 2
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4


