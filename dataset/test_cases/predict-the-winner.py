def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 17, 100, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 17, 100, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 7, 6, 5, 6, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 7, 6, 5, 6, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 18, 6, 3, 1, 19, 2, 4, 10, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 18, 6, 3, 1, 19, 2, 4, 10, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 233, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 233, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == True: {e}')
    
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
        result = candidate(nums = [1, 3, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 18, 4, 3, 9, 13, 13, 17]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 18, 4, 3, 9, 13, 13, 17]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7, 25, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7, 25, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 17, 10, 14, 3, 8, 15, 21]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 17, 10, 14, 3, 8, 15, 21]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 1, 1, 10, 100, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 1, 1, 10, 100, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 5, 4, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 5, 4, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 6, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 6, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7, 10, 12, 14, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7, 10, 12, 14, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 80, 90, 30, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 80, 90, 30, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 200, 250, 300, 150, 100, 50, 200, 250, 300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 200, 250, 300, 150, 100, 50, 200, 250, 300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 80, 60, 20, 40, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 80, 60, 20, 40, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 19, 45, 3, 12, 67, 2, 9, 15, 18, 21, 34, 56, 78, 90]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 19, 45, 3, 12, 67, 2, 9, 15, 18, 21, 34, 56, 78, 90]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 5, 7, 23, 19, 18, 15, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 5, 7, 23, 19, 18, 15, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 4, 6, 8, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 4, 6, 8, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 100, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 100, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7, 6, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7, 6, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 6, 10, 2, 1, 5, 9, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 6, 10, 2, 1, 5, 9, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 12, 5, 8, 7, 3, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 12, 5, 8, 7, 3, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 10, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 10, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 12, 32, 4, 55, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 12, 32, 4, 55, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 4, 2, 9, 10, 6, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 4, 2, 9, 10, 6, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7, 10, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7, 10, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 5, 3, 7, 1, 9, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 5, 3, 7, 1, 9, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 3, 8, 5, 2, 7, 6, 1, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 3, 8, 5, 2, 7, 6, 1, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 100, 50, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 100, 50, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 7, 11, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 7, 11, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 15, 56, 7, 98, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 15, 56, 7, 98, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 30, 27, 5, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 30, 27, 5, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 23, 7, 1, 9, 15, 3, 18, 11, 17, 2, 14, 6, 12, 8, 10, 4, 13, 16, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 23, 7, 1, 9, 15, 3, 18, 11, 17, 2, 14, 6, 12, 8, 10, 4, 13, 16, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 11, 17, 19, 21, 13, 5, 3, 2, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 11, 17, 19, 21, 13, 5, 3, 2, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 50, 25, 20, 10, 5, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 50, 25, 20, 10, 5, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 8, 9, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 8, 9, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 23, 45, 6, 78, 90, 12, 34]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 23, 45, 6, 78, 90, 12, 34]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 5, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 5, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 10, 10, 10]) == True
    assert candidate(nums = [1, 5, 2]) == False
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [10]) == True
    assert candidate(nums = [1]) == True
    assert candidate(nums = [5, 17, 100, 11]) == True
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [1, 2, 3, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, 2, 3, 7]) == True
    assert candidate(nums = [0, 0, 7, 6, 5, 6, 1]) == False
    assert candidate(nums = [5, 18, 6, 3, 1, 19, 2, 4, 10, 11]) == True
    assert candidate(nums = [1, 5, 233, 7]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [0, 0, 0, 0]) == True
    assert candidate(nums = [8, 15, 3, 7]) == True
    assert candidate(nums = [10, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert candidate(nums = [1, 2]) == True
    assert candidate(nums = [1, 2, 3]) == True
    assert candidate(nums = [1, 3, 1]) == False
    assert candidate(nums = [5, 18, 4, 3, 9, 13, 13, 17]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == True
    assert candidate(nums = [8, 15, 3, 7, 25, 10]) == True
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == True
    assert candidate(nums = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 0]) == True
    assert candidate(nums = [23, 17, 10, 14, 3, 8, 15, 21]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16]) == True
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [10, 20, 30, 40, 50]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [1000, 100, 10, 1, 1, 10, 100, 1000]) == True
    assert candidate(nums = [3, 1, 5, 4, 2]) == True
    assert candidate(nums = [1, 2, 3, 6, 5, 4, 3]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [10000000, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == True
    assert candidate(nums = [10, 2, 5, 6, 7, 8]) == True
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True
    assert candidate(nums = [8, 15, 3, 7, 10, 12, 14, 13]) == True
    assert candidate(nums = [10, 80, 90, 30, 50]) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == True
    assert candidate(nums = [100, 50, 200, 250, 300, 150, 100, 50, 200, 250, 300]) == True
    assert candidate(nums = [10, 80, 60, 20, 40, 30]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000000]) == True
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [23, 19, 45, 3, 12, 67, 2, 9, 15, 18, 21, 34, 56, 78, 90]) == True
    assert candidate(nums = [12, 5, 7, 23, 19, 18, 15, 10]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
    assert candidate(nums = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, 5, 2, 4, 6, 8, 10]) == True
    assert candidate(nums = [1, 2, 100, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == True
    assert candidate(nums = [8, 15, 3, 7, 10]) == False
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(nums = [8, 15, 3, 7, 6, 12]) == True
    assert candidate(nums = [3, 4, 6, 10, 2, 1, 5, 9, 7, 8]) == True
    assert candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == True
    assert candidate(nums = [7, 10, 12, 5, 8, 7, 3, 9]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996]) == True
    assert candidate(nums = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == True
    assert candidate(nums = [10, 20, 15, 10, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == True
    assert candidate(nums = [23, 12, 32, 4, 55, 2, 3]) == False
    assert candidate(nums = [3, 1, 5, 4, 2, 9, 10, 6, 8, 7]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [8, 15, 3, 7, 10, 12]) == True
    assert candidate(nums = [2, 8, 5, 3, 7, 1, 9, 4]) == True
    assert candidate(nums = [20, 10, 3, 8, 5, 2, 7, 6, 1, 4]) == True
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == True
    assert candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == True
    assert candidate(nums = [100, 200, 150, 100, 50, 25]) == True
    assert candidate(nums = [8, 15, 3, 7, 11, 12]) == True
    assert candidate(nums = [23, 15, 56, 7, 98, 1]) == True
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(nums = [3, 30, 27, 5, 20, 10]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [5, 23, 7, 1, 9, 15, 3, 18, 11, 17, 2, 14, 6, 12, 8, 10, 4, 13, 16, 19]) == True
    assert candidate(nums = [23, 11, 17, 19, 21, 13, 5, 3, 2, 8]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, 100, 50, 25, 20, 10, 5, 1]) == True
    assert candidate(nums = [3, 1, 5, 8, 9, 2]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [3, 9, 1, 2]) == True
    assert candidate(nums = [1, 23, 45, 6, 78, 90, 12, 34]) == True
    assert candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True
    assert candidate(nums = [1, 3, 1, 5, 2, 4]) == True
    assert candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]) == True


