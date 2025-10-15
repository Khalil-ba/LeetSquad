def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 0, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 0, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 0, 4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 0, 4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 1, 3, 5, 7, 6, 9, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 1, 3, 5, 7, 6, 9, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 4, 0, 3, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 4, 0, 3, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 0, 3, 4, 5, 6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 0, 3, 4, 5, 6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 4, 5, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 4, 5, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 1, 2, 4, 5, 6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 1, 2, 4, 5, 6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 0, 2, 5, 4, 7, 6, 9, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 0, 2, 5, 4, 7, 6, 9, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2, 3, 4, 5, 6, 7, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2, 3, 4, 5, 6, 7, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 1, 3, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 1, 3, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 5, 4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 5, 4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 0, 5, 4, 3, 8, 7, 10, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 0, 5, 4, 3, 8, 7, 10, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 0, 1, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 0, 1, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 4, 2, 0, 3, 1, 8, 5, 7, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 4, 2, 0, 3, 1, 8, 5, 7, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 0, 4, 3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 0, 4, 3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 0, 2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 0, 2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 0, 5, 4, 3, 8, 7, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 0, 5, 4, 3, 8, 7, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 4, 5, 7, 6, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 4, 5, 7, 6, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 4, 2, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 4, 2, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 5, 3, 7, 2, 8, 1, 6, 9, 4, 0, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 5, 3, 7, 2, 8, 1, 6, 9, 4, 0, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 7, 5, 9, 3, 11, 2, 10, 12, 4, 1, 6, 8, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 7, 5, 9, 3, 11, 2, 10, 12, 4, 1, 6, 8, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 1, 2, 5, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 1, 2, 5, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 1, 2, 5, 4, 7, 6, 9, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 1, 2, 5, 4, 7, 6, 9, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 3, 1, 2, 6, 5, 8, 9, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 3, 1, 2, 6, 5, 8, 9, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 0, 2, 4, 5, 7, 6, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 0, 2, 4, 5, 7, 6, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 2, 1, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 2, 1, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 4, 0, 1, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 4, 0, 1, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 0, 2, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 0, 2, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 0, 1, 2, 3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 0, 1, 2, 3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 3, 4, 5, 2, 1, 8, 6, 9, 7, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 3, 4, 5, 2, 1, 8, 6, 9, 7, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4, 3, 5, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4, 3, 5, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 5, 4, 3, 2, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 5, 4, 3, 2, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 3, 4, 5, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 3, 4, 5, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 0, 4, 2, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 0, 4, 2, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 0, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 0, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 0, 2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 0, 2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2, 5, 4, 7, 6, 9, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2, 5, 4, 7, 6, 9, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 1, 4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 1, 4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 2, 4, 6, 5, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 2, 4, 6, 5, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 0, 5, 2, 1, 4, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 0, 5, 2, 1, 4, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 0, 7, 1, 6, 2, 5, 3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 0, 7, 1, 6, 2, 5, 3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 0, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 0, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 3, 5, 0, 4, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 3, 5, 0, 4, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 9, 10, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 9, 10, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 1, 2, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 1, 2, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4, 3, 5, 7, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4, 3, 5, 7, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 2, 1, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 2, 1, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 2, 1, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 2, 1, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 1, 2, 5, 4, 6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 1, 2, 5, 4, 6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 0, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 0, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 0, 5, 4, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 0, 5, 4, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 0, 1, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 0, 1, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 5, 4, 6, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 5, 4, 6, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 6, 4, 8, 2, 10, 1, 7, 11, 3, 0, 5, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 6, 4, 8, 2, 10, 1, 7, 11, 3, 0, 5, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 0, 1, 3, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 0, 1, 3, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 0, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 0, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 2, 5, 7, 1, 3, 6, 8, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 2, 5, 7, 1, 3, 6, 8, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 4, 1, 2, 0, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 4, 1, 2, 0, 5, 6]) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 1, 2, 3, 4]) == True
    assert candidate(nums = [4, 3, 2, 1, 0]) == False
    assert candidate(nums = [2, 0, 1, 3]) == False
    assert candidate(nums = [2, 1, 0, 3]) == False
    assert candidate(nums = [3, 2, 1, 0]) == False
    assert candidate(nums = [0, 2, 1, 3]) == True
    assert candidate(nums = [0, 1, 2, 3]) == True
    assert candidate(nums = [0, 1, 3, 2]) == True
    assert candidate(nums = [1, 0, 2]) == True
    assert candidate(nums = [1, 2, 0]) == False
    assert candidate(nums = [1, 2, 3, 0, 4, 5, 6]) == False
    assert candidate(nums = [0, 2, 4, 1, 3, 5, 7, 6, 9, 8]) == False
    assert candidate(nums = [6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [5, 2, 4, 0, 3, 1]) == False
    assert candidate(nums = [2, 1, 0, 3, 4, 5, 6, 7]) == False
    assert candidate(nums = [0, 2, 1, 3, 4, 5, 6, 7]) == True
    assert candidate(nums = [0, 3, 1, 2, 4, 5, 6, 7]) == False
    assert candidate(nums = [1, 3, 0, 2, 5, 4, 7, 6, 9, 8]) == False
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [8, 1, 2, 3, 4, 5, 6, 7, 0]) == False
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [0, 2, 4, 1, 3, 5]) == False
    assert candidate(nums = [0, 2, 1, 3, 5, 4, 6]) == True
    assert candidate(nums = [2, 1, 0, 5, 4, 3, 8, 7, 10, 9]) == False
    assert candidate(nums = [2, 3, 0, 1, 4, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]) == False
    assert candidate(nums = [6, 4, 2, 0, 3, 1, 8, 5, 7, 9, 10]) == False
    assert candidate(nums = [5, 1, 0, 4, 3, 2]) == False
    assert candidate(nums = [1, 3, 0, 2, 4]) == False
    assert candidate(nums = [2, 1, 0, 5, 4, 3, 8, 7, 6]) == False
    assert candidate(nums = [0, 2, 1, 3, 4, 5, 7, 6, 8]) == True
    assert candidate(nums = [5, 3, 1, 4, 2, 0]) == False
    assert candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]) == False
    assert candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == True
    assert candidate(nums = [11, 5, 3, 7, 2, 8, 1, 6, 9, 4, 0, 10]) == False
    assert candidate(nums = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [13, 7, 5, 9, 3, 11, 2, 10, 12, 4, 1, 6, 8, 0]) == False
    assert candidate(nums = [3, 0, 1, 2, 5, 4]) == False
    assert candidate(nums = [1, 0, 3, 2, 5, 4]) == True
    assert candidate(nums = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9]) == True
    assert candidate(nums = [3, 0, 1, 2, 5, 4, 7, 6, 9, 8]) == False
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11]) == False
    assert candidate(nums = [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]) == False
    assert candidate(nums = [4, 0, 3, 1, 2, 6, 5, 8, 9, 7]) == False
    assert candidate(nums = [0, 2, 1, 4, 3, 5]) == True
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 6]) == True
    assert candidate(nums = [1, 3, 0, 2, 4, 5, 7, 6, 8, 9]) == False
    assert candidate(nums = [4, 0, 2, 1, 3]) == False
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == True
    assert candidate(nums = [5, 2, 3, 4, 0, 1, 6, 7, 8, 9]) == False
    assert candidate(nums = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]) == False
    assert candidate(nums = [1, 3, 0, 2, 4, 5]) == False
    assert candidate(nums = [5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10]) == True
    assert candidate(nums = [5, 0, 1, 2, 3, 4]) == False
    assert candidate(nums = [10, 3, 4, 5, 2, 1, 8, 6, 9, 7, 0]) == False
    assert candidate(nums = [0, 1, 3, 2, 4, 5, 6]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True
    assert candidate(nums = [0, 1, 2, 4, 3, 5, 6, 7]) == True
    assert candidate(nums = [0, 2, 1, 3, 4]) == True
    assert candidate(nums = [1, 0, 5, 4, 3, 2, 6]) == False
    assert candidate(nums = [1, 0, 2, 3, 4, 5, 6, 7]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [3, 1, 0, 4, 2, 5]) == False
    assert candidate(nums = [1, 3, 2, 4, 0, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [0, 1, 3, 2, 4]) == True
    assert candidate(nums = [4, 3, 2, 1, 0]) == False
    assert candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == True
    assert candidate(nums = [1, 3, 0, 2, 4]) == False
    assert candidate(nums = [0, 1, 3, 2, 5, 4, 7, 6, 9, 8]) == True
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 9]) == False
    assert candidate(nums = [0, 2, 1, 3, 4, 5]) == True
    assert candidate(nums = [0, 2, 3, 1, 4, 5, 6]) == False
    assert candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 9]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 0]) == False
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14]) == False
    assert candidate(nums = [0, 1, 3, 2, 4, 6, 5, 7]) == True
    assert candidate(nums = [6, 0, 5, 2, 1, 4, 3]) == False
    assert candidate(nums = [8, 0, 7, 1, 6, 2, 5, 3, 4]) == False
    assert candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]) == False
    assert candidate(nums = [0, 2, 1, 3, 5, 4]) == True
    assert candidate(nums = [4, 3, 2, 1, 0, 5]) == False
    assert candidate(nums = [6, 2, 3, 5, 0, 4, 1]) == False
    assert candidate(nums = [2, 0, 1, 4, 3, 6, 5, 8, 7, 9, 10, 11]) == False
    assert candidate(nums = [0, 3, 1, 2, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [0, 1, 2, 4, 3, 5, 7, 6]) == True
    assert candidate(nums = [0, 3, 2, 1, 4]) == False
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == True
    assert candidate(nums = [3, 0, 2, 1, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6]) == True
    assert candidate(nums = [3, 0, 1, 2, 5, 4, 6, 7]) == False
    assert candidate(nums = [4, 3, 0, 1, 2]) == False
    assert candidate(nums = [1, 3, 2, 0, 5, 4, 6]) == False
    assert candidate(nums = [5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [5, 2, 3, 0, 1, 4]) == False
    assert candidate(nums = [0, 1, 2, 3, 5, 4, 6, 7, 8]) == True
    assert candidate(nums = [12, 6, 4, 8, 2, 10, 1, 7, 11, 3, 0, 5, 9]) == False
    assert candidate(nums = [2, 4, 0, 1, 3, 5]) == False
    assert candidate(nums = [1, 2, 3, 0, 4, 5]) == False
    assert candidate(nums = [9, 4, 2, 5, 7, 1, 3, 6, 8, 0]) == False
    assert candidate(nums = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [7, 3, 4, 1, 2, 0, 5, 6]) == False


