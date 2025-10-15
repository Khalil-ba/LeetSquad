def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 1000000, 1, 1000000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 1000000, 1, 1000000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 5, 1, 9, 2, 8, 6, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 5, 1, 9, 2, 8, 6, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 2, 7, 4, 1, 8, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 2, 7, 4, 1, 8, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 1, 3, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 1, 3, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4, 5, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4, 5, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 1000000, 1, 1000000, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 1000000, 1, 1000000, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4, 1, 3, 4, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4, 1, 3, 4, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 1090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 1090: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 435: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500001, 499999, 500002, 499998, 500003, 499997, 500004, 499996]) == 2499990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500001, 499999, 500002, 499998, 500003, 499997, 500004, 499996]) == 2499990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2, 1000000, 3, 1000000, 4, 1000000, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2, 1000000, 3, 1000000, 4, 1000000, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1, 1, 1000000, 1, 1000000, 1]) == 1000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1, 1, 1000000, 1, 1000000, 1]) == 1000003: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 3, 5, 7, 9, 1, 2, 8, 4, 6]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 3, 5, 7, 9, 1, 2, 8, 4, 6]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996, 6, 999995, 7, 999994, 8]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996, 6, 999995, 7, 999994, 8]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 5, 7, 3, 8, 6, 10, 4, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 5, 7, 3, 8, 6, 10, 4, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 3, 9, 1, 6, 2, 7, 4]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 3, 9, 1, 6, 2, 7, 4]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 169: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 1001, 1002, 997, 996, 995, 1003, 1004, 1005, 994, 993, 992, 1006]) == 6980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 1001, 1002, 997, 996, 995, 1003, 1004, 1005, 994, 993, 992, 1006]) == 6980: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 4, 7, 2, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 4, 7, 2, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 259
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 259: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 1000001, 1000002, 999997, 999996, 999995, 1000003, 1000004]) == 4999994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 1000001, 1000002, 999997, 999996, 999995, 1000003, 1000004]) == 4999994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 4, 5, 5, 5]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 4, 5, 5, 5]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 50, 60, 10, 70]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 50, 60, 10, 70]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 99, 98, 97, 103, 104, 105, 96, 95, 94, 106, 107, 108]) == 697
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 99, 98, 97, 103, 104, 105, 96, 95, 94, 106, 107, 108]) == 697: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 3, 2, 5, 4, 6, 8]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 3, 2, 5, 4, 6, 8]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 8, 9, 1, 2, 3, 4, 10]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 8, 9, 1, 2, 3, 4, 10]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990]) == 4999970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990]) == 4999970: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 10, 5, 1, 20, 25, 30, 35, 40, 45]) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 10, 5, 1, 20, 25, 30, 35, 40, 45]) == 116: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 125, 62, 31, 156, 78, 39, 200, 100, 50, 25, 125, 62, 31]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 125, 62, 31, 156, 78, 39, 200, 100, 50, 25, 125, 62, 31]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000]) == 2500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000]) == 2500000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [1, 1000000]) == 1
    assert candidate(nums = [1000000, 1, 1000000, 1, 1000000]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(nums = [7, 3, 5, 1, 9, 2, 8, 6, 4]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(nums = [5, 3, 6, 2, 7, 4, 1, 8, 9]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5]) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [2, 3, 5, 1, 3, 2]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 9
    assert candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1]) == 9
    assert candidate(nums = [2, 1, 3, 4, 5, 2]) == 7
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5]) == 14
    assert candidate(nums = [1000000, 1]) == 1
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 24
    assert candidate(nums = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
    assert candidate(nums = [5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [1000000]) == 1000000
    assert candidate(nums = [1000000, 1, 1000000, 1, 1000000, 1]) == 3
    assert candidate(nums = [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]) == 15
    assert candidate(nums = [2, 1, 4, 1, 3, 4, 2, 1]) == 7
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == 38
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 25
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6]) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 21
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 130
    assert candidate(nums = [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]) == 23
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 16
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 29
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 1]) == 9
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 1090
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 435
    assert candidate(nums = [500000, 500001, 499999, 500002, 499998, 500003, 499997, 500004, 499996]) == 2499990
    assert candidate(nums = [1000000, 2, 1000000, 3, 1000000, 4, 1000000, 5]) == 14
    assert candidate(nums = [1000000, 1000000, 1, 1, 1000000, 1, 1000000, 1]) == 1000003
    assert candidate(nums = [7, 5, 3, 5, 7, 9, 1, 2, 8, 4, 6]) == 22
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 6
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996, 6, 999995, 7, 999994, 8]) == 36
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996]) == 15
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225
    assert candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8]) == 45
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(nums = [9, 5, 7, 3, 8, 6, 10, 4, 2, 1]) == 19
    assert candidate(nums = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3]) == 26
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125
    assert candidate(nums = [5, 3, 8, 3, 9, 1, 6, 2, 7, 4]) == 13
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 6
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 120
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 24
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 169
    assert candidate(nums = [2, 3, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5]) == 11
    assert candidate(nums = [1000, 999, 998, 1001, 1002, 997, 996, 995, 1003, 1004, 1005, 994, 993, 992, 1006]) == 6980
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
    assert candidate(nums = [5, 3, 8, 1, 4, 7, 2, 6]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 24
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 80
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == 50
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 325
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 64
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 259
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 57
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 85
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 360
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
    assert candidate(nums = [1000000, 999999, 999998, 1000001, 1000002, 999997, 999996, 999995, 1000003, 1000004]) == 4999994
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 4, 5, 5, 5]) == 21
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 50, 60, 10, 70]) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(nums = [100, 101, 102, 99, 98, 97, 103, 104, 105, 96, 95, 94, 106, 107, 108]) == 697
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 95
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 19
    assert candidate(nums = [7, 1, 3, 2, 5, 4, 6, 8]) == 15
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [7, 6, 5, 8, 9, 1, 2, 3, 4, 10]) == 26
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990]) == 4999970
    assert candidate(nums = [15, 10, 5, 1, 20, 25, 30, 35, 40, 45]) == 116
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 13
    assert candidate(nums = [100, 50, 25, 125, 62, 31, 156, 78, 39, 200, 100, 50, 25, 125, 62, 31]) == 351
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 46
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000]) == 2500000
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5]) == 15


