def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 2, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 2, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 1, 1, 3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 1, 1, 3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 1, 1, 2, 3, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 1, 1, 2, 3, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 3, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 3, 1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 3, 1, 3, 2, 1, 3, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 3, 1, 3, 2, 1, 3, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 1, 1, 1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 1, 1, 1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 2, 3, 1, 2, 3, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 2, 3, 1, 2, 3, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 2, 1, 3, 3, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 2, 1, 3, 3, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 1, 1, 3, 3, 3, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 1, 1, 3, 3, 3, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 1, 3, 2, 3, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 1, 3, 2, 3, 1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 1, 3, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 1, 3, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 3, 2, 3, 1, 2, 1, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 3, 2, 3, 1, 2, 1, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 1, 2, 2, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 1, 2, 2, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 3, 2, 1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 3, 2, 1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 1, 1, 3, 3, 2, 2, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 1, 1, 3, 3, 2, 2, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 1, 2, 2, 1, 3, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 1, 2, 2, 1, 3, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 1, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 1, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 2, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 2, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 3, 2, 1, 2, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 3, 2, 1, 2, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 1, 2, 3, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 1, 2, 3, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 3, 2, 2, 1]) == 3
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6
    assert candidate(nums = [1, 2, 3, 1, 2, 3]) == 2
    assert candidate(nums = [1, 1, 1]) == 0
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [1, 2, 2, 1, 3]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3]) == 0
    assert candidate(nums = [1, 2, 3, 3, 3, 2, 1]) == 2
    assert candidate(nums = [1, 1, 1, 2, 2, 3]) == 0
    assert candidate(nums = [1, 3, 2, 1, 3, 3]) == 2
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 3, 3]) == 0
    assert candidate(nums = [2, 1, 3, 2, 1]) == 3
    assert candidate(nums = [3, 2, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2]) == 3
    assert candidate(nums = [2, 2, 2, 2, 3, 3]) == 0
    assert candidate(nums = [3, 1, 2, 3, 1, 2]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [3, 3, 2, 2, 1]) == 3
    assert candidate(nums = [2, 2, 1, 1, 3, 3]) == 2
    assert candidate(nums = [3, 2, 1]) == 2
    assert candidate(nums = [3, 2, 1, 2, 1]) == 3
    assert candidate(nums = [3, 3, 3]) == 0
    assert candidate(nums = [1, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [1, 2, 3, 3, 3]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3]) == 0
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1]) == 4
    assert candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 1, 1]) == 9
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]) == 2
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 12
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
    assert candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 7
    assert candidate(nums = [2, 2, 3, 1, 1, 2, 3, 3, 2, 1]) == 5
    assert candidate(nums = [3, 2, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 3, 2, 1, 3, 2]) == 5
    assert candidate(nums = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 4
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
    assert candidate(nums = [3, 3, 2, 1, 1, 1, 2, 3]) == 3
    assert candidate(nums = [2, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3]) == 5
    assert candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3
    assert candidate(nums = [3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 8
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 13
    assert candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3]) == 3
    assert candidate(nums = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 8
    assert candidate(nums = [1, 3, 1, 2, 3, 1, 2, 3, 1]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(nums = [3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]) == 1
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 7
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 7
    assert candidate(nums = [3, 1, 2, 2, 1, 3, 3, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 9
    assert candidate(nums = [3, 2, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 20
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [1, 1, 2, 2, 2, 1, 1, 3, 3, 3, 1, 1]) == 4
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [2, 1, 1, 3, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12
    assert candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [3, 2, 1, 2, 1, 3, 1]) == 4
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 1, 3, 2, 3, 1, 2, 1, 3]) == 5
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == 21
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [3, 3, 3, 1, 2, 2, 1, 1]) == 5
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 11
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 11
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 21
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 4
    assert candidate(nums = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3]) == 4
    assert candidate(nums = [2, 2, 1, 1, 3, 3, 2, 2, 3, 3]) == 4
    assert candidate(nums = [1, 3, 3, 1, 2, 2, 1, 3, 3, 2]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
    assert candidate(nums = [2, 2, 3, 1, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 9
    assert candidate(nums = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 19
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1]) == 7
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 12
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 2, 3]) == 5
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 6
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2]) == 6
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2]) == 4
    assert candidate(nums = [2, 1, 2, 1, 3, 2, 1, 2, 3, 3]) == 4
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
    assert candidate(nums = [2, 2, 3, 1, 2, 3, 1, 2]) == 4
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 13
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 8
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 10
    assert candidate(nums = [3, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 3
    assert candidate(nums = [3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 8
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 5
    assert candidate(nums = [1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 6
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 3]) == 4
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 6
    assert candidate(nums = [2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 9
    assert candidate(nums = [2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 6
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
    assert candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 6
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1]) == 5


