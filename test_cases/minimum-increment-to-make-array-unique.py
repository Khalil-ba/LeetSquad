def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 5, 3, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 5, 3, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 3, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 3, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 3, 1, 4, 4, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 3, 1, 4, 4, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 5, 5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 5, 5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 3, 3, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 3, 3, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 2, 1, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 2, 1, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 101, 101, 101, 102, 102, 102, 103, 103, 103]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 101, 101, 101, 102, 102, 102, 103, 103, 103]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28]) == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28]) == 137: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 528: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]) == 462: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97, 96, 96]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97, 96, 96]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 435: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11]) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11]) == 163: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 496: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 685
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 685: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 285: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15, 16, 16]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15, 16, 16]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 163: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 99, 99, 98, 97, 97, 96, 96, 95, 95, 94, 94, 93, 93, 92, 92, 91, 91]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 99, 99, 98, 97, 97, 96, 96, 95, 95, 94, 94, 93, 93, 92, 92, 91, 91]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100, 100, 100, 100]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100, 100, 100, 100]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 2, 4, 5, 4, 6, 7, 8, 9, 9]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 2, 4, 5, 4, 6, 7, 8, 9, 9]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2, 2, 3, 3, 4, 4, 4, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2, 2, 3, 3, 4, 4, 4, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 147: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 105: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 16
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 45
    assert candidate(nums = [5, 3, 5, 3, 5]) == 4
    assert candidate(nums = [1, 2, 2]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [1, 3, 2, 2, 3, 3, 4]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 0
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 4, 5, 5]) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
    assert candidate(nums = [0, 0, 0, 0]) == 6
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums = [5, 3, 5, 5, 5]) == 6
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 45
    assert candidate(nums = [1, 3, 3, 3, 3, 3, 3]) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [3, 2, 1, 2, 1, 7]) == 6
    assert candidate(nums = [10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [100000, 100000, 100000]) == 3
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 140
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 192
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 45
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 300
    assert candidate(nums = [100, 100, 100, 101, 101, 101, 102, 102, 102, 103, 103, 103]) == 48
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 190
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 110
    assert candidate(nums = [20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28]) == 137
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 528
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000]) == 10
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 170
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 25
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]) == 462
    assert candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97, 96, 96]) == 25
    assert candidate(nums = [1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == 7
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 435
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == 140
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 225
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11]) == 163
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 496
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 685
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 121
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 89
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 285
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 100
    assert candidate(nums = [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000]) == 15
    assert candidate(nums = [2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15, 16, 16]) == 43
    assert candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 160
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 38
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 121
    assert candidate(nums = [100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105]) == 36
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 89
    assert candidate(nums = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 64
    assert candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7]) == 45
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]) == 32
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 163
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 65
    assert candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 81
    assert candidate(nums = [100, 100, 100, 99, 99, 98, 97, 97, 96, 96, 95, 95, 94, 94, 93, 93, 92, 92, 91, 91]) == 98
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 50
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 145
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) == 119
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 144
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 100
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100, 100, 100, 100]) == 15
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25]) == 3
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 190
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 5
    assert candidate(nums = [2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 94
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [1, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5]) == 99
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 15
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 190
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 225
    assert candidate(nums = [1, 3, 2, 3, 2, 4, 5, 4, 6, 7, 8, 9, 9]) == 28
    assert candidate(nums = [5, 3, 2, 2, 3, 3, 4, 4, 4, 5]) == 30
    assert candidate(nums = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 60
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 48
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 180
    assert candidate(nums = [1, 3, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]) == 135
    assert candidate(nums = [5, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 40
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 147
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 250
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 105


