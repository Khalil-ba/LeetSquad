def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 10, 10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 10, 10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 3, 3, 3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 3, 3, 3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [3, 3, 3, 3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [3, 3, 3, 3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 20, 30, 40, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 20, 30, 40, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [7, 8, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [7, 8, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 80]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 80]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 30]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 30]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 25000000, 25000000, 25000000, 25000000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 25000000, 25000000, 25000000, 25000000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [100, 100, 100, 100, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [100, 100, 100, 100, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 20, 30, 40, 10, 20, 30, 40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 20, 30, 40, 10, 20, 30, 40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 28]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 28]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [15, 15, 15, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [15, 15, 15, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 15]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 15]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [10, 20, 30, 40, 50, 15, 5, 25, 35]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [10, 20, 30, 40, 50, 15, 5, 25, 35]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 32]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 32]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [15, 15, 15, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [15, 15, 15, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [100000000, 100000000, 100000000, 100000000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [100000000, 100000000, 100000000, 100000000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True
    assert candidate(matchsticks = [10, 10, 10, 10]) == True
    assert candidate(matchsticks = [5, 5, 5, 5]) == True
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(matchsticks = [1, 3, 3, 3, 4]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2]) == True
    assert candidate(matchsticks = [1, 1, 2, 2, 2]) == True
    assert candidate(matchsticks = [1, 2, 3, 4, 5]) == False
    assert candidate(matchsticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 12]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 4, 4, 4, 4]) == True
    assert candidate(matchsticks = [3, 3, 3, 3, 4]) == False
    assert candidate(matchsticks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == False
    assert candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == True
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(matchsticks = [7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(matchsticks = [10, 20, 30, 40, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(matchsticks = [1, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == False
    assert candidate(matchsticks = [7, 8, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12]) == False
    assert candidate(matchsticks = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == False
    assert candidate(matchsticks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 80]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5]) == False
    assert candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 30]) == False
    assert candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == False
    assert candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 25000000, 25000000, 25000000, 25000000]) == True
    assert candidate(matchsticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == False
    assert candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == False
    assert candidate(matchsticks = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1]) == False
    assert candidate(matchsticks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == True
    assert candidate(matchsticks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15]) == True
    assert candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]) == True
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == False
    assert candidate(matchsticks = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True
    assert candidate(matchsticks = [10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(matchsticks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8]) == True
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == False
    assert candidate(matchsticks = [10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == False
    assert candidate(matchsticks = [100, 100, 100, 100, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == False
    assert candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000, 25000000]) == False
    assert candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 1]) == False
    assert candidate(matchsticks = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]) == False
    assert candidate(matchsticks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == False
    assert candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5]) == False
    assert candidate(matchsticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(matchsticks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]) == True
    assert candidate(matchsticks = [100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000]) == False
    assert candidate(matchsticks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == False
    assert candidate(matchsticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True
    assert candidate(matchsticks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4]) == False
    assert candidate(matchsticks = [10, 20, 30, 40, 10, 20, 30, 40]) == True
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 28]) == False
    assert candidate(matchsticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == False
    assert candidate(matchsticks = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]) == False
    assert candidate(matchsticks = [15, 15, 15, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 15]) == False
    assert candidate(matchsticks = [10, 20, 30, 40, 50, 15, 5, 25, 35]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
    assert candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(matchsticks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 32]) == False
    assert candidate(matchsticks = [15, 15, 15, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(matchsticks = [100000000, 100000000, 100000000, 100000000]) == True
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False
    assert candidate(matchsticks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]) == False
    assert candidate(matchsticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == False
    assert candidate(matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False
    assert candidate(matchsticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20]) == False
    assert candidate(matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == True


