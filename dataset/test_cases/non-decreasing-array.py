def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 1, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 1, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 5, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 5, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 5, 6, 3, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 5, 6, 3, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 2, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 2, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 3, 4, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 3, 4, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 2, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 2, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 7, 6, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 7, 6, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 2, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 2, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 4, 3, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 4, 3, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10, 11, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10, 11, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 4, 5, 6, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 4, 5, 6, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 5, 1, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 5, 1, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 5, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 5, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 5, 6, 4, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 5, 6, 4, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 4, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 4, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 2, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 2, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 6, 5, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 6, 5, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 0, 100000, -100000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 0, 100000, -100000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 8, 11, 13, 15, 17, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 8, 11, 13, 15, 17, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 9, 10, 2, 11, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 9, 10, 2, 11, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 5, 7, 9, 11, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 5, 7, 9, 11, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 2, 2, 3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 2, 2, 3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10, 17]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10, 17]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 2, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 2, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 3, 4, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 3, 4, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 5, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 5, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3, 6, 5, 7, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3, 6, 5, 7, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -3, -2, -4, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -3, -2, -4, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8, 9, 10, 11, 12, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8, 9, 10, 11, 12, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 2, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 2, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 250, 300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 250, 300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 4, 5, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 4, 5, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 4, 2, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 4, 2, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 5, 3, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 5, 3, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 4, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 4, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 4, 3, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 4, 3, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 2, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 2, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 1, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 1, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 7, 6, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 7, 6, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 5, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 5, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 3, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 3, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 6, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 6, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 2, 5, 7, 7, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 2, 5, 7, 7, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 7, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 7, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 5, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 5, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8, 6, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8, 6, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 4, 5, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 4, 5, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 5, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 5, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 4, 7, 8, 6, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 4, 7, 8, 6, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 3, 2, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 3, 2, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 6, 5, 7, 6, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 6, 5, 7, 6, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 5, 6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 5, 6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 2, 3, 4]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 5, 4, 6]) == True
    assert candidate(nums = [10, 5, 7]) == True
    assert candidate(nums = [1, 2, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 5, 4]) == True
    assert candidate(nums = [1, 1, 1]) == True
    assert candidate(nums = [3, 3, 2, 2]) == False
    assert candidate(nums = [2, 2, 3, 2, 4]) == True
    assert candidate(nums = [1, 2, 4]) == True
    assert candidate(nums = [1]) == True
    assert candidate(nums = [2, 2, 2]) == True
    assert candidate(nums = [4, 2, 1]) == False
    assert candidate(nums = [3, 4, 2, 3]) == False
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, 3, 2]) == True
    assert candidate(nums = [4, 2, 3]) == True
    assert candidate(nums = [5, 7, 1, 8]) == True
    assert candidate(nums = [1, 3, 2, 4, 3]) == False
    assert candidate(nums = [1, 5, 4, 6]) == True
    assert candidate(nums = [1, 2]) == True
    assert candidate(nums = [1, 2, 3]) == True
    assert candidate(nums = [1, 2, 4, 5, 3]) == True
    assert candidate(nums = [1, 4, 5, 6, 3, 7]) == True
    assert candidate(nums = [2, 3, 3, 2, 4, 5]) == True
    assert candidate(nums = [1, 2, 3, 5, 4, 5, 6]) == True
    assert candidate(nums = [5, 6, 3, 4, 7]) == False
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
    assert candidate(nums = [1, 3, 2, 3, 2, 2, 3]) == False
    assert candidate(nums = [1, 3, 5, 4, 7, 6, 8]) == False
    assert candidate(nums = [1, 2, 3, 3, 3, 3, 3, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
    assert candidate(nums = [3, 3, 3, 3, 3, 3]) == True
    assert candidate(nums = [1, 3, 2, 4, 2, 5]) == False
    assert candidate(nums = [1, 2, 5, 4, 3, 5]) == False
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [1, 3, 2, 2, 2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10, 11, 12]) == True
    assert candidate(nums = [1, 5, 3, 5, 6]) == True
    assert candidate(nums = [1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 12]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10]) == True
    assert candidate(nums = [1, 3, 5, 4, 2]) == False
    assert candidate(nums = [1, 5, 3, 4, 5, 6, 2]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6]) == False
    assert candidate(nums = [3, 5, 2, 5, 1, 6, 7, 8, 9]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]) == True
    assert candidate(nums = [1, 4, 2, 3, 5]) == True
    assert candidate(nums = [1, 2, 2, 3, 3, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11]) == True
    assert candidate(nums = [1, 2, 4, 5, 3, 5]) == True
    assert candidate(nums = [1, 3, 2, 3, 5, 6, 4, 7, 8, 9, 10]) == False
    assert candidate(nums = [5, 1, 3, 4, 2]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 1]) == True
    assert candidate(nums = [1, 3, 2, 2, 5]) == True
    assert candidate(nums = [3, 3, 3, 3, 2, 3, 3, 3, 3]) == True
    assert candidate(nums = [1, 2, 3, 3, 3, 2, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 6]) == True
    assert candidate(nums = [1, 2, 3, 4, 6, 5, 7, 8, 9]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8]) == True
    assert candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8]) == True
    assert candidate(nums = [100000, -100000, 0, 100000, -100000]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7]) == False
    assert candidate(nums = [1, 3, 2, 3, 2, 3]) == False
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 11, 13, 15, 17, 19]) == True
    assert candidate(nums = [1, 3, 2, 4, 3, 5]) == False
    assert candidate(nums = [1, 3, 2, 2, 5]) == True
    assert candidate(nums = [1, 3, 5, 4, 7]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7]) == True
    assert candidate(nums = [1, 3, 5, 4, 6, 7]) == True
    assert candidate(nums = [8, 9, 10, 2, 11, 12]) == True
    assert candidate(nums = [1, 5, 3, 5, 7, 9, 11, 10]) == False
    assert candidate(nums = [1, 2, 3, 2, 1, 4]) == False
    assert candidate(nums = [1, 2, 3, 3, 2, 2, 3, 4]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 10, 17]) == True
    assert candidate(nums = [3, 3, 3, 3, 2, 3, 3, 3]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 3, 5]) == True
    assert candidate(nums = [5, 6, 3, 4, 7, 8, 9]) == False
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 5, 7]) == True
    assert candidate(nums = [3, 5, 4, 5, 6]) == True
    assert candidate(nums = [1, 2, 4, 3, 6, 5, 7, 8]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [6, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600]) == True
    assert candidate(nums = [-1, -3, -2, -4, 0]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8, 9, 10, 11, 12, 10]) == False
    assert candidate(nums = [1, 2, 2, 3, 3, 2, 4, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == True
    assert candidate(nums = [100, 200, 150, 250, 300]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 3, 5]) == True
    assert candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10]) == True
    assert candidate(nums = [5, 1, 3, 4, 5, 6, 7]) == True
    assert candidate(nums = [3, 3, 3, 2, 2, 2]) == False
    assert candidate(nums = [1, 3, 2, 3, 4, 5]) == True
    assert candidate(nums = [5, 1, 3, 4, 2, 5]) == False
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == True
    assert candidate(nums = [1, 2, 4, 5, 3, 6]) == True
    assert candidate(nums = [-1, 4, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8]) == True
    assert candidate(nums = [1, 2, 5, 4, 3, 6, 7, 8, 9]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 9]) == True
    assert candidate(nums = [5, 6, 2, 7, 8, 9]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == True
    assert candidate(nums = [6, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [5, 7, 1, 8]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 7, 6, 8, 9, 10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10]) == True
    assert candidate(nums = [1, 3, 2, 3, 5, 4]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 3, 8, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6]) == False
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 10]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]) == False
    assert candidate(nums = [10, 9, 2, 5, 7, 7, 8]) == False
    assert candidate(nums = [1, 2, 3, 5, 4, 7, 6]) == False
    assert candidate(nums = [3, 4, 2, 3]) == False
    assert candidate(nums = [1, 4, 5, 3, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 7, 8, 6, 9, 10]) == False
    assert candidate(nums = [1, 2, 3, 2, 4, 5, 3]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 2, 3]) == True
    assert candidate(nums = [1, 3, 2, 3, 5, 3]) == False
    assert candidate(nums = [5, 1, 3, 2, 4]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == False
    assert candidate(nums = [1, 2, 3, 5, 4, 7, 8, 6, 9]) == False
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7, 8]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == True
    assert candidate(nums = [1, 3, 2, 3, 3, 2, 4, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 3, 5, 6]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 6, 5, 7, 6, 8]) == False
    assert candidate(nums = [3, 5, 4, 5, 6, 7]) == True
    assert candidate(nums = [3, 5, 6, 3, 4, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2]) == False
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 4]) == True


