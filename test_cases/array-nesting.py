def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 4, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 4, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 0, 6, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 0, 6, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 5, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 5, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 3, 4, 8, 6, 1, 7, 9, 2, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 3, 4, 8, 6, 1, 7, 9, 2, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 0, 1, 4, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 0, 1, 4, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 0, 3, 1, 6, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 0, 3, 1, 6, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 5, 7, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 5, 7, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 0, 5, 6, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 0, 5, 6, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 0, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 0, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 5, 4, 0, 8, 1, 6, 3, 7, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 5, 4, 0, 8, 1, 6, 3, 7, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 0, 7, 6, 5, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 0, 7, 6, 5, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 6, 3, 8, 2, 5, 1, 4, 9, 7, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 6, 3, 8, 2, 5, 1, 4, 9, 7, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 3, 5, 7, 6, 8, 9, 11, 10, 13, 12, 15, 14]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 3, 5, 7, 6, 8, 9, 11, 10, 13, 12, 15, 14]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 13, 12, 1, 9, 14, 10, 0, 8, 5, 11, 4, 7, 3, 2, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 13, 12, 1, 9, 14, 10, 0, 8, 5, 11, 4, 7, 3, 2, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 4, 3, 0, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 4, 3, 0, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 2, 5, 3, 6, 1, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 2, 5, 3, 6, 1, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 0, 6, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 0, 6, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 5, 4, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 5, 4, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 12, 14]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 12, 14]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 3, 1, 5, 6, 7, 0, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 3, 1, 5, 6, 7, 0, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 2, 6, 7, 3, 1, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 2, 6, 7, 3, 1, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 3, 7, 8, 0, 5, 4, 2, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 3, 7, 8, 0, 5, 4, 2, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 3, 0, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 3, 0, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 4, 5, 3, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 4, 5, 3, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 8, 10, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 8, 10, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 1, 4, 5, 2, 6, 7, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 1, 4, 5, 2, 6, 7, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 3, 5, 7, 2, 6, 1, 8, 9, 10, 11, 12, 13, 14]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 3, 5, 7, 2, 6, 1, 8, 9, 10, 11, 12, 13, 14]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 3, 5, 4, 6, 8, 7, 10, 9, 12, 11, 14, 13]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 3, 5, 4, 6, 8, 7, 10, 9, 12, 11, 14, 13]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 0, 1, 2, 5, 4, 8, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 0, 1, 2, 5, 4, 8, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 5, 3, 7, 6, 9, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 5, 3, 7, 6, 9, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 0, 9, 6, 1, 10, 11, 13, 8, 7, 5, 2, 4, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 0, 9, 6, 1, 10, 11, 13, 8, 7, 5, 2, 4, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 4, 1, 0, 6, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 4, 1, 0, 6, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 1, 6, 2, 5, 4, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 1, 6, 2, 5, 4, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 4, 3, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 4, 3, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 0, 1, 2, 3, 4, 5, 6, 13, 8, 9, 10, 11, 12, 14]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 0, 1, 2, 3, 4, 5, 6, 13, 8, 9, 10, 11, 12, 14]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 1, 5, 4, 0, 3, 7, 11, 8, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 1, 5, 4, 0, 3, 7, 11, 8, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 0, 7, 3, 1, 6, 5, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 0, 7, 3, 1, 6, 5, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 3, 6, 4, 0, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 3, 6, 4, 0, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 6, 0, 3, 5, 7, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 6, 0, 3, 5, 7, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 0, 1, 3, 6, 2, 8, 5, 4, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 0, 1, 3, 6, 2, 8, 5, 4, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 0, 4, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 0, 4, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 6, 4, 1, 0, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 6, 4, 1, 0, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 3, 1, 4, 5, 7, 6, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 3, 1, 4, 5, 7, 6, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 3, 5, 1, 8, 7, 6, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 3, 5, 1, 8, 7, 6, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 5, 2, 4, 7, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 5, 2, 4, 7, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 2, 6, 1, 5, 3, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 2, 6, 1, 5, 3, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 5, 3, 6, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 5, 3, 6, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 0, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 0, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 2, 1, 4, 5, 0, 6, 8, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 2, 1, 4, 5, 0, 6, 8, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 8, 5, 1, 9, 4, 3, 0, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 8, 5, 1, 9, 4, 3, 0, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 4, 3, 5, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 4, 3, 5, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 3, 4, 5, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 3, 4, 5, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 0, 6, 5, 4, 9, 8, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 0, 6, 5, 4, 9, 8, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 2, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 2, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 5, 1, 3, 2, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 5, 1, 3, 2, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 3, 6, 8, 5, 7, 9, 11, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 3, 6, 8, 5, 7, 9, 11, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 1, 3, 6, 7, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 1, 3, 6, 7, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 5, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 5, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2, 6, 5, 4, 7, 9, 8, 11, 10, 13, 12, 15, 14]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2, 6, 5, 4, 7, 9, 8, 11, 10, 13, 12, 15, 14]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 3, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 3, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 3, 5, 1, 4, 0, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 3, 5, 1, 4, 0, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 8, 3, 10, 2, 6, 11, 4, 0, 5, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 8, 3, 10, 2, 6, 11, 4, 0, 5, 1]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 0, 3, 4, 2]) == 3
    assert candidate(nums = [5, 1, 4, 2, 0, 6, 3]) == 6
    assert candidate(nums = [3, 2, 1, 0]) == 2
    assert candidate(nums = [1, 2, 0, 3]) == 3
    assert candidate(nums = [0, 2, 1]) == 2
    assert candidate(nums = [0, 2, 1, 3]) == 2
    assert candidate(nums = [0, 2, 1, 5, 3, 4]) == 3
    assert candidate(nums = [10, 5, 3, 4, 8, 6, 1, 7, 9, 2, 0]) == 5
    assert candidate(nums = [0, 1, 2]) == 1
    assert candidate(nums = [3, 0, 1, 2]) == 4
    assert candidate(nums = [5, 0, 1, 4, 3, 2]) == 4
    assert candidate(nums = [3, 0, 2, 1]) == 3
    assert candidate(nums = [5, 4, 0, 3, 1, 6, 2]) == 4
    assert candidate(nums = [1, 2, 0]) == 3
    assert candidate(nums = [1, 0]) == 2
    assert candidate(nums = [0, 2, 1, 4, 3, 5, 7, 6]) == 2
    assert candidate(nums = [2, 3, 1, 0, 5, 6, 4]) == 4
    assert candidate(nums = [1, 3, 0, 2]) == 4
    assert candidate(nums = [9, 5, 4, 0, 8, 1, 6, 3, 7, 2]) == 7
    assert candidate(nums = [0, 2, 1, 4, 3, 5, 6, 7, 8, 9]) == 2
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [3, 2, 1, 0, 7, 6, 5, 4]) == 2
    assert candidate(nums = [10, 6, 3, 8, 2, 5, 1, 4, 9, 7, 0]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]) == 10
    assert candidate(nums = [2, 3, 4, 5, 0, 1]) == 3
    assert candidate(nums = [2, 0, 1, 4, 3, 5, 7, 6, 8, 9, 11, 10, 13, 12, 15, 14]) == 3
    assert candidate(nums = [15, 13, 12, 1, 9, 14, 10, 0, 8, 5, 11, 4, 7, 3, 2, 6]) == 12
    assert candidate(nums = [5, 6, 4, 3, 0, 2, 1]) == 4
    assert candidate(nums = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2
    assert candidate(nums = [4, 0, 2, 5, 3, 6, 1, 7]) == 6
    assert candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 2
    assert candidate(nums = [1, 2, 3, 4, 0, 6, 5]) == 5
    assert candidate(nums = [1, 0, 3, 5, 4, 2]) == 3
    assert candidate(nums = [15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 12, 14]) == 6
    assert candidate(nums = [8, 2, 3, 1, 5, 6, 7, 0, 4]) == 6
    assert candidate(nums = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]) == 3
    assert candidate(nums = [4, 0, 2, 6, 7, 3, 1, 5]) == 7
    assert candidate(nums = [1, 6, 3, 7, 8, 0, 5, 4, 2, 9]) == 5
    assert candidate(nums = [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]) == 10
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == 2
    assert candidate(nums = [1, 4, 3, 0, 2]) == 5
    assert candidate(nums = [6, 2, 4, 5, 3, 0, 1]) == 7
    assert candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 8, 10, 9]) == 2
    assert candidate(nums = [0, 3, 1, 4, 5, 2, 6, 7, 8, 9]) == 5
    assert candidate(nums = [4, 0, 3, 5, 7, 2, 6, 1, 8, 9, 10, 11, 12, 13, 14]) == 4
    assert candidate(nums = [2, 0, 1, 3, 5, 4, 6, 8, 7, 10, 9, 12, 11, 14, 13]) == 3
    assert candidate(nums = [3, 6, 0, 1, 2, 5, 4, 8, 7]) == 6
    assert candidate(nums = [2, 3, 1, 0]) == 4
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1
    assert candidate(nums = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [2, 0, 1, 4, 5, 3, 7, 6, 9, 8]) == 3
    assert candidate(nums = [12, 0, 9, 6, 1, 10, 11, 13, 8, 7, 5, 2, 4, 3]) == 7
    assert candidate(nums = [7, 5, 4, 1, 0, 6, 2, 3]) == 8
    assert candidate(nums = [0, 3, 1, 6, 2, 5, 4, 7]) == 5
    assert candidate(nums = [0, 4, 3, 1, 2]) == 4
    assert candidate(nums = [7, 0, 1, 2, 3, 4, 5, 6, 13, 8, 9, 10, 11, 12, 14]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 10
    assert candidate(nums = [6, 2, 1, 5, 4, 0, 3, 7, 11, 8, 10, 9]) == 4
    assert candidate(nums = [8, 2, 0, 7, 3, 1, 6, 5, 4]) == 8
    assert candidate(nums = [7, 1, 5, 3, 6, 4, 0, 2]) == 6
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]) == 2
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
    assert candidate(nums = [8, 2, 4, 6, 0, 3, 5, 7, 1]) == 5
    assert candidate(nums = [7, 0, 1, 3, 6, 2, 8, 5, 4, 9]) == 5
    assert candidate(nums = [1, 5, 0, 4, 2, 3]) == 6
    assert candidate(nums = [7, 5, 6, 4, 1, 0, 2, 3]) == 6
    assert candidate(nums = [8, 2, 3, 1, 4, 5, 7, 6, 0]) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [2, 0, 3, 5, 1, 8, 7, 6, 4]) == 7
    assert candidate(nums = [1, 0, 3, 5, 2, 4, 7, 6, 8]) == 4
    assert candidate(nums = [12, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 4
    assert candidate(nums = [4, 0, 2, 6, 1, 5, 3, 7]) == 3
    assert candidate(nums = [2, 0, 1, 4, 5, 3, 6, 7]) == 3
    assert candidate(nums = [4, 5, 6, 7, 0, 1, 2, 3]) == 2
    assert candidate(nums = [9, 3, 2, 1, 4, 5, 0, 6, 8, 7]) == 4
    assert candidate(nums = [6, 2, 8, 5, 1, 9, 4, 3, 0, 7]) == 6
    assert candidate(nums = [6, 2, 4, 3, 5, 0, 1]) == 6
    assert candidate(nums = [6, 2, 3, 4, 5, 1, 0]) == 5
    assert candidate(nums = [3, 1, 2, 0, 6, 5, 4, 9, 8, 7]) == 2
    assert candidate(nums = [3, 5, 4, 2, 0, 1]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 7
    assert candidate(nums = [4, 0, 5, 1, 3, 2, 6]) == 4
    assert candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7]) == 2
    assert candidate(nums = [2, 0, 1, 4, 3, 6, 8, 5, 7, 9, 11, 10]) == 4
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 2
    assert candidate(nums = [8, 2, 4, 1, 3, 6, 7, 0, 5]) == 5
    assert candidate(nums = [0, 2, 1, 4, 5, 3]) == 3
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6]) == 2
    assert candidate(nums = [4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [0, 1, 3, 2, 6, 5, 4, 7, 9, 8, 11, 10, 13, 12, 15, 14]) == 2
    assert candidate(nums = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]) == 2
    assert candidate(nums = [2, 0, 1, 4, 3, 5]) == 3
    assert candidate(nums = [6, 3, 5, 1, 4, 0, 2]) == 4
    assert candidate(nums = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [9, 7, 8, 3, 10, 2, 6, 11, 4, 0, 5, 1]) == 5


