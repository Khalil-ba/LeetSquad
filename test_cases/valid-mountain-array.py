def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 3, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 3, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 3, 4, 5, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 3, 4, 5, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 3, 3, 2, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 3, 3, 2, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 3, 4, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 3, 4, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 3, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 3, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 9, 10, 8, 6, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 9, 10, 8, 6, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 6, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 6, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 9, 11, 10, 8, 6, 4, 2, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 9, 11, 10, 8, 6, 4, 2, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 9, 10, 10, 9, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 9, 10, 10, 9, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 2, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 2, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 4, 3, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 4, 3, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 3, 2, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 3, 2, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 4, 3, 2, 1, 0, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 4, 3, 2, 1, 0, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 3, 4, 3, 2, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 3, 4, 3, 2, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 6, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 6, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 8, 7, 6, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 8, 7, 6, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2, 0, -2, -4, -6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2, 0, -2, -4, -6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 3, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 3, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 0, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 0, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 12, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 12, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 25, 20, 15, 10, 5, 0, -5, -10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 25, 20, 15, 10, 5, 0, -5, -10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 0, -1, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 0, -1, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 0, -1, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 0, -1, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 5, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 5, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 4, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 4, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [5, 4, 3, 2, 1]) == False
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(arr = [3, 1, 2]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2]) == False
    assert candidate(arr = [0, 2, 3, 3, 2, 1]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [0, 3, 2, 1]) == True
    assert candidate(arr = [0, 1, 2, 1, 2]) == False
    assert candidate(arr = [0, 1, 2, 3, 1]) == True
    assert candidate(arr = [0, 2, 3, 4, 5, 3, 2, 1]) == True
    assert candidate(arr = [1]) == False
    assert candidate(arr = [1, 1, 1, 1, 1]) == False
    assert candidate(arr = [2, 1]) == False
    assert candidate(arr = [0, 1, 2, 3, 1, 0]) == True
    assert candidate(arr = [0, 2, 3, 3, 2, 0]) == False
    assert candidate(arr = [3, 5, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 5]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(arr = [1, 3, 2]) == True
    assert candidate(arr = [0, 2, 3, 4, 5, 3, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(arr = [0, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 3, 2, 1]) == True
    assert candidate(arr = [0, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == True
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1]) == False
    assert candidate(arr = [1, 2, 2, 1]) == False
    assert candidate(arr = [1, 2, 2, 3, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2, 0]) == True
    assert candidate(arr = [1, 1, 1, 1, 1]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == True
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 2, 3, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 4, 7, 9, 10, 8, 6, 4, 2]) == True
    assert candidate(arr = [1, 3, 5, 7, 6, 4, 2]) == True
    assert candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1, 4, 7, 9, 11, 10, 8, 6, 4, 2, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == True
    assert candidate(arr = [1, 3, 2, 1, 3, 2, 1]) == False
    assert candidate(arr = [1, 3, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
    assert candidate(arr = [8, 9, 10, 10, 9, 8]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == True
    assert candidate(arr = [1, 3, 2, 1, 2, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(arr = [2, 3, 1, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 3, 5, 4, 3, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 3, 2, 1, 0]) == False
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == True
    assert candidate(arr = [1, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == False
    assert candidate(arr = [1, 5, 4, 3, 2, 1, 0, 2, 3]) == False
    assert candidate(arr = [1, 1, 1, 2, 3, 4, 3, 2, 1, 1, 1]) == False
    assert candidate(arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 3, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(arr = [1, 3, 5, 7, 6, 4, 2]) == True
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == True
    assert candidate(arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3]) == True
    assert candidate(arr = [5, 6, 7, 8, 9, 8, 7, 6, 5]) == True
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10]) == True
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2, 0, -2, -4, -6]) == True
    assert candidate(arr = [1, 2, 3, 2, 3, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1]) == False
    assert candidate(arr = [1, 3, 2, 1, 0, -1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == True
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 12, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]) == True
    assert candidate(arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [3, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == True
    assert candidate(arr = [1, 3, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 3, 2, 4, 3, 2]) == False
    assert candidate(arr = [10, 20, 30, 25, 20, 15, 10, 5, 0, -5, -10]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(arr = [10, 9, 8, 7, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]) == False
    assert candidate(arr = [1, 3, 2, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
    assert candidate(arr = [1, 3, 2, 1, 0, -1, -2]) == True
    assert candidate(arr = [9, 8, 7, 6, 5, 6, 7, 8, 9]) == False
    assert candidate(arr = [1, 2, 3, 2, 1, 0, -1, -2]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 5, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 2, 3, 4, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == True
    assert candidate(arr = [1, 2, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True


