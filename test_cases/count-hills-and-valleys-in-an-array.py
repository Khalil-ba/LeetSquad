def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 100, 98, 99, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 100, 98, 99, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 4, 3, 3, 2, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 4, 3, 3, 2, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 1, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 1, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 1, 1, 6, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 1, 1, 6, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 5, 5, 4, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 5, 5, 4, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 2, 1, 3, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 2, 1, 3, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 49, 51, 49, 51, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 49, 51, 49, 51, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 9, 8, 9, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 9, 8, 9, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 96, 97, 98, 99, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 96, 97, 98, 99, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 2, 3, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 2, 3, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 51, 50, 50, 50, 50, 51, 50, 50, 50, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 51, 50, 50, 50, 50, 51, 50, 50, 50, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 100, 90, 100, 90, 100, 80, 90, 80]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 100, 90, 100, 90, 100, 80, 90, 80]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 2, 2, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 2, 2, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 3, 2, 1, 2, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 3, 2, 1, 2, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1, 3, 2, 3, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1, 3, 2, 3, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 10, 20, 10, 30, 10, 20, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 10, 20, 10, 30, 10, 20, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 52, 51, 50, 51, 52, 51, 50, 51, 52, 51]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 52, 51, 50, 51, 52, 51, 50, 51, 52, 51]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 20, 30, 20, 10, 20, 30, 20, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 20, 30, 20, 10, 20, 30, 20, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 98, 99, 100, 99, 98, 97, 96, 97, 98, 99, 100, 99]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 98, 99, 100, 99, 98, 97, 96, 97, 98, 99, 100, 99]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 96, 97, 98, 99, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 96, 97, 98, 99, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 1, 2, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 1, 2, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 3, 2, 1, 2, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 3, 2, 1, 2, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 21, 20, 22, 21, 23, 22, 24, 23, 25, 24, 23, 22, 21, 20, 19, 20, 21, 22, 21]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 21, 20, 22, 21, 23, 22, 24, 23, 25, 24, 23, 22, 21, 20, 19, 20, 21, 22, 21]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 2, 1, 3, 3, 3, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 2, 1, 3, 3, 3, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 3, 3, 3, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 3, 3, 3, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 2, 3, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 8, 7, 8, 9, 10, 9, 10, 9, 8, 7, 8, 7, 6, 5, 4, 5, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 8, 7, 8, 9, 10, 9, 10, 9, 8, 7, 8, 7, 6, 5, 4, 5, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10]) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 4, 3, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 5]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(nums = [100, 99, 100, 98, 99, 100]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 4, 4, 3, 3, 2, 2, 1]) == 0
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 0
    assert candidate(nums = [1, 3, 2, 3, 1]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5]) == 4
    assert candidate(nums = [3, 1, 2, 1, 3, 2, 1]) == 4
    assert candidate(nums = [2, 4, 1, 1, 6, 5]) == 3
    assert candidate(nums = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 2, 2, 1, 1]) == 1
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 3
    assert candidate(nums = [6, 6, 5, 5, 4, 1]) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 2, 1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [1, 2, 2, 2, 3]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 2
    assert candidate(nums = [1, 3, 1, 2, 1, 3, 1]) == 5
    assert candidate(nums = [1, 2, 3, 2, 1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2]) == 2
    assert candidate(nums = [50, 50, 49, 51, 49, 51, 50]) == 4
    assert candidate(nums = [9, 8, 9, 8, 9, 8, 9]) == 5
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 3
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 96, 97, 98, 99, 100]) == 1
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2]) == 9
    assert candidate(nums = [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3]) == 11
    assert candidate(nums = [1, 3, 2, 3, 1, 2, 3, 4, 3, 2, 1]) == 5
    assert candidate(nums = [3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]) == 10
    assert candidate(nums = [50, 50, 50, 50, 51, 50, 50, 50, 50, 51, 50, 50, 50, 50]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1]) == 1
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2]) == 5
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 12
    assert candidate(nums = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == 3
    assert candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 17
    assert candidate(nums = [100, 90, 100, 90, 100, 90, 100, 80, 90, 80]) == 8
    assert candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 10
    assert candidate(nums = [1, 2, 2, 3, 3, 2, 2, 1, 1]) == 1
    assert candidate(nums = [3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2]) == 3
    assert candidate(nums = [1, 3, 2, 3, 1, 3, 2, 1, 2, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 1]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 3
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8
    assert candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1, 3, 2, 3, 1]) == 9
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 7
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 7
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [10, 20, 10, 30, 10, 20, 10, 30, 10, 20, 10]) == 9
    assert candidate(nums = [50, 51, 52, 51, 50, 51, 52, 51, 50, 51, 52, 51]) == 5
    assert candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 8
    assert candidate(nums = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]) == 9
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10]) == 18
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2]) == 4
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 12
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == 8
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [30, 20, 10, 20, 30, 20, 10, 20, 30, 20, 10]) == 4
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 13
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 8
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 5
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 0
    assert candidate(nums = [2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 2, 2, 2]) == 2
    assert candidate(nums = [3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 8
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9]) == 13
    assert candidate(nums = [100, 99, 98, 97, 98, 99, 100, 99, 98, 97, 96, 97, 98, 99, 100, 99]) == 4
    assert candidate(nums = [1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 5
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) == 8
    assert candidate(nums = [1, 1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1]) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 96, 97, 98, 99, 100]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == 3
    assert candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1]) == 5
    assert candidate(nums = [8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 5]) == 8
    assert candidate(nums = [7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 19
    assert candidate(nums = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 14
    assert candidate(nums = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9]) == 2
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2]) == 3
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 9
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3]) == 16
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 6
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(nums = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6]) == 2
    assert candidate(nums = [1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4]) == 4
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2]) == 7
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8]) == 10
    assert candidate(nums = [50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50, 49, 50]) == 17
    assert candidate(nums = [2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 1, 2, 2]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9]) == 2
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 1
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 11
    assert candidate(nums = [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 3, 2, 1, 2, 1]) == 11
    assert candidate(nums = [1, 2, 2, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 7
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4]) == 8
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 11
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 14
    assert candidate(nums = [20, 21, 20, 22, 21, 23, 22, 24, 23, 25, 24, 23, 22, 21, 20, 19, 20, 21, 22, 21]) == 11
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 2, 1, 3, 3, 3, 2, 2, 2]) == 3
    assert candidate(nums = [1, 3, 2, 3, 1, 2, 3, 2, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2]) == 2
    assert candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 18
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 18
    assert candidate(nums = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6, 7, 8, 9, 10]) == 3
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 11
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 3, 3, 3, 2, 2, 2]) == 1
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 8
    assert candidate(nums = [1, 3, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [9, 8, 7, 8, 7, 8, 9, 10, 9, 10, 9, 8, 7, 8, 7, 6, 5, 4, 5, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == 13
    assert candidate(nums = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1]) == 1
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10]) == 7


