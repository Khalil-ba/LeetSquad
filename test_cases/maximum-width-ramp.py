def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 3, 3, 7, 5, 2, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 3, 3, 7, 5, 2, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 5, 6, 3, 5, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 5, 6, 3, 5, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 5, 6, 6, 1, 3, 2, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 5, 6, 6, 1, 3, 2, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 20, 15, 11, 10, 9, 7, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 20, 15, 11, 10, 9, 7, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 9, 10, 1, 3, 5, 6, 4, 8, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 9, 10, 1, 3, 5, 6, 4, 8, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 0, 8, 2, 1, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 0, 8, 2, 1, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 6, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 6, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 5, 2, 3, 4, 8, 7, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 5, 2, 3, 4, 8, 7, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 7, 9, 10, 11, 15, 20, 25]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 7, 9, 10, 11, 15, 20, 25]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 23, 11, 33, 22, 55, 44, 33, 22, 11, 77, 88, 99, 66, 55]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 23, 11, 33, 22, 55, 44, 33, 22, 11, 77, 88, 99, 66, 55]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50000]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50000]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10000, 0, 9999, 0, 9998, 0, 9997, 0, 9996, 0, 9995, 0, 9994, 0, 9993, 0, 9992, 0, 9991]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10000, 0, 9999, 0, 9998, 0, 9997, 0, 9996, 0, 9995, 0, 9994, 0, 9993, 0, 9992, 0, 9991]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 6, 5, 1, 0, 5, 9, 10, 11, 12, 13, 14, 15]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 6, 5, 1, 0, 5, 9, 10, 11, 12, 13, 14, 15]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45000, 44999, 44998, 44997, 44996, 44995, 44994, 44993, 44992, 44991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45000, 44999, 44998, 44997, 44996, 44995, 44994, 44993, 44992, 44991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 19: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 2, 2, 3, 3, 7, 5, 2, 4]) == 9
    assert candidate(nums = [1, 5, 2, 5, 6, 3, 5, 4]) == 7
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 9
    assert candidate(nums = [1, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [1, 5, 2, 5, 6, 6, 1, 3, 2, 5]) == 9
    assert candidate(nums = [25, 20, 15, 11, 10, 9, 7, 6, 3, 1]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0]) == 4
    assert candidate(nums = [1, 2, 9, 10, 1, 3, 5, 6, 4, 8, 7]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [6, 0, 8, 2, 1, 5]) == 4
    assert candidate(nums = [0, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [6, 6, 6, 6, 6, 6]) == 5
    assert candidate(nums = [8, 1, 5, 2, 3, 4, 8, 7, 2]) == 7
    assert candidate(nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
    assert candidate(nums = [1, 3, 6, 7, 9, 10, 11, 15, 20, 25]) == 9
    assert candidate(nums = [1, 2, 3, 2, 1]) == 4
    assert candidate(nums = [1, 1, 1, 1, 2]) == 4
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == 10
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 19
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5]) == 19
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 18
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
    assert candidate(nums = [45, 23, 11, 33, 22, 55, 44, 33, 22, 11, 77, 88, 99, 66, 55]) == 14
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 25
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 50
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11]) == 19
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 19
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50000]) == 20
    assert candidate(nums = [0, 10000, 0, 9999, 0, 9998, 0, 9997, 0, 9996, 0, 9995, 0, 9994, 0, 9993, 0, 9992, 0, 9991]) == 19
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 18
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 18
    assert candidate(nums = [4, 8, 6, 5, 1, 0, 5, 9, 10, 11, 12, 13, 14, 15]) == 13
    assert candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 19
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 29
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 29
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 29
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]) == 20
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 18
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == 29
    assert candidate(nums = [45000, 44999, 44998, 44997, 44996, 44995, 44994, 44993, 44992, 44991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
    assert candidate(nums = [1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, 11, 9, 12, 10]) == 20
    assert candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
    assert candidate(nums = [100, 0, 99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9]) == 18
    assert candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981]) == 0
    assert candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981, 0]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 19


