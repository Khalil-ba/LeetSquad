def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 5, 4, 9, 8]) == 4.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 5, 4, 9, 8]) == 4.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 8, 3, 10, 5]) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 8, 3, 10, 5]) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60]) == 35.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60]) == 35.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 25, 25, 25, 25]) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 25, 25, 25, 25]) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 10, 1, 11, 5, 4, 8]) == 4.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 10, 1, 11, 5, 4, 8]) == 4.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45]) == 47.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45]) == 47.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12]) == 7.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12]) == 7.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21]) == 11.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21]) == 11.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 4, 6, 5]) == 3.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 4, 6, 5]) == 3.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11]) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11]) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2]) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2]) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == 3.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == 3.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 25, 2, 50, 24]) == 24.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 25, 2, 50, 24]) == 24.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 3, 51, 6, 32, 28]) == 24.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 3, 51, 6, 32, 28]) == 24.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 40, 60, 50]) == 35.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 40, 60, 50]) == 35.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 10, 30, 5, 40, 15]) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 10, 30, 5, 40, 15]) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 3, 4, 15, 13, 4, 1]) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 3, 4, 15, 13, 4, 1]) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5]) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5]) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 30, 35, 20, 50, 40]) == 35.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 30, 35, 20, 50, 40]) == 35.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 50, 2, 50, 3]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 50, 2, 50, 3]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15]) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15]) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 7, 8, 9]) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 7, 8, 9]) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40]) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40]) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == -12.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == -12.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 19.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 19.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 9, 1, 5, 11, 13, 2, 8, 6, 10, 4]) == 6.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 9, 1, 5, 11, 13, 2, 8, 6, 10, 4]) == 6.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [48, 46, 44, 42, 40, 38, 36, 34]) == 41.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [48, 46, 44, 42, 40, 38, 36, 34]) == 41.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29]) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29]) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [27, 37, 23, 33, 29, 39, 21, 31]) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [27, 37, 23, 33, 29, 39, 21, 31]) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 1, 8, 15]) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 1, 8, 15]) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 6.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 6.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 8.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 8.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 30, 15, 5, 50, 35, 20, 10, 40, 25]) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 30, 15, 5, 50, 35, 20, 10, 40, 25]) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1]) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1]) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 7.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 7.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 12, 36, 6, 48, 24]) == 24.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 12, 36, 6, 48, 24]) == 24.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 15.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 15.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94]) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94]) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 17, 11, 5, 31, 29, 25, 19, 35, 33, 37, 13]) == 21.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 17, 11, 5, 31, 29, 25, 19, 35, 33, 37, 13]) == 21.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]) == 39.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]) == 39.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 10, 34, 15, 40, 5, 30, 20]) == 22.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 10, 34, 15, 40, 5, 30, 20]) == 22.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]) == 68.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]) == 68.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38]) == 43.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38]) == 43.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 29, 27, 25, 21, 28, 26, 22, 24, 20, 19, 30, 18, 31, 17, 32, 16, 33, 15, 34, 14, 35, 13, 36, 12, 37, 11, 38, 10, 39, 9, 40, 8, 41, 7, 42, 6, 43, 5, 44, 4, 45, 3, 46, 2, 47, 1, 48, 50]) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 29, 27, 25, 21, 28, 26, 22, 24, 20, 19, 30, 18, 31, 17, 32, 16, 33, 15, 34, 14, 35, 13, 36, 12, 37, 11, 38, 10, 39, 9, 40, 8, 41, 7, 42, 6, 43, 5, 44, 4, 45, 3, 46, 2, 47, 1, 48, 50]) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 42.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 42.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32]) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32]) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [48, 49, 50, 1, 2, 3, 47, 46, 45, 44]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [48, 49, 50, 1, 2, 3, 47, 46, 45, 44]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == 36.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == 36.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 1, 30, 45, 20, 15, 40]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 1, 30, 45, 20, 15, 40]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45]) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45]) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28]) == 28.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28]) == 28.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38]) == 43.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38]) == 43.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368]) == 195.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368]) == 195.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 29, 29, 29, 1, 1, 1, 1, 14, 14, 14, 14]) == 14.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 29, 29, 29, 1, 1, 1, 1, 14, 14, 14, 14]) == 14.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 19, 28, 18, 27, 17, 26, 16, 25, 15, 24, 14]) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 19, 28, 18, 27, 17, 26, 16, 25, 15, 24, 14]) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 38.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 38.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 45.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 45.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 34, 12, 12, 56, 56, 28, 28, 42, 42]) == 34.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 34, 12, 12, 56, 56, 28, 28, 42, 42]) == 34.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 11, 7, 15, 9, 17, 5, 13]) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 11, 7, 15, 9, 17, 5, 13]) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46, 6, 45, 7, 44, 8, 43, 9, 42, 10, 41]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46, 6, 45, 7, 44, 8, 43, 9, 42, 10, 41]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 22.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 22.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47]) == 47.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47]) == 47.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 65.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 65.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 12, 20]) == 22.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 12, 20]) == 22.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85]) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85]) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 45.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 45.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 10.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 10.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 20, 5, 10, 25, 30, 35, 40, 50, 55]) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 20, 5, 10, 25, 30, 35, 40, 50, 55]) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25]) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25]) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 42, 43, 41, 44, 46, 47, 48]) == 44.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 42, 43, 41, 44, 46, 47, 48]) == 44.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]) == 29.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]) == 29.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 12.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 12.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 8.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 8.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [28, 22, 16, 10, 4, 32, 26, 20, 14, 8, 30, 12]) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [28, 22, 16, 10, 4, 32, 26, 20, 14, 8, 30, 12]) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 11.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 11.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [22, 38, 26, 40, 24, 36, 28, 34]) == 31.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [22, 38, 26, 40, 24, 36, 28, 34]) == 31.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 65.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 65.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 5, 30, 20, 40, 10]) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 5, 30, 20, 40, 10]) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 4, 8, 12]) == 32.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 4, 8, 12]) == 32.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 16.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 16.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 1, 8, 15, 22, 29]) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 1, 8, 15, 22, 29]) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1]) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1]) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 15, 16, 23, 42, 1, 2, 3, 5, 7, 11, 13, 17, 19, 29]) == 11.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 15, 16, 23, 42, 1, 2, 3, 5, 7, 11, 13, 17, 19, 29]) == 11.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]) == 15.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]) == 15.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 43, 44, 45, 46, 47, 48, 49, 50, 1]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 43, 44, 45, 46, 47, 48, 49, 50, 1]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 7.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 7.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25]) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25]) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 50, 40, 30, 20, 10]) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 50, 40, 30, 20, 10]) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48, 18, 30, 42, 54]) == 33.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48, 18, 30, 42, 54]) == 33.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 24, 3, 12, 18, 6, 21, 9, 15, 1, 19, 7, 22, 10, 16, 4, 23, 2, 11, 13, 17, 14, 25, 20, 5]) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 24, 3, 12, 18, 6, 21, 9, 15, 1, 19, 7, 22, 10, 16, 4, 23, 2, 11, 13, 17, 14, 25, 20, 5]) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 49, 2, 48, 3, 47, 4, 46, 5, 45, 6]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 49, 2, 48, 3, 47, 4, 46, 5, 45, 6]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 29.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 29.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18]) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18]) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 50]) == 28.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 50]) == 28.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 18, 15, 12, 9, 6, 3, 0]) == 10.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 18, 15, 12, 9, 6, 3, 0]) == 10.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 2, 48, 3, 47, 4, 46, 5, 45, 6]) == 25.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 2, 48, 3, 47, 4, 46, 5, 45, 6]) == 25.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 40.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 40.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 12.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 12.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 17, 47, 31, 27, 13, 41, 23, 39, 29, 35, 19]) == 29.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 17, 47, 31, 27, 13, 41, 23, 39, 29, 35, 19]) == 29.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 1, 5, 4, 9, 8]) == 4.5
    assert candidate(nums = [1, 9, 8, 3, 10, 5]) == 5.5
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == 35.0
    assert candidate(nums = [25, 25, 25, 25, 25, 25]) == 25.0
    assert candidate(nums = [2, 3, 10, 1, 11, 5, 4, 8]) == 4.5
    assert candidate(nums = [50, 49, 48, 47, 46, 45]) == 47.5
    assert candidate(nums = [2, 4, 6, 8, 10, 12]) == 7.0
    assert candidate(nums = [1, 5, 9, 13, 17, 21]) == 11.0
    assert candidate(nums = [2, 3, 1, 4, 6, 5]) == 3.5
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 6.0
    assert candidate(nums = [2, 2, 2, 2, 2, 2]) == 2.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 3.5
    assert candidate(nums = [50, 1, 25, 2, 50, 24]) == 24.5
    assert candidate(nums = [42, 3, 51, 6, 32, 28]) == 24.0
    assert candidate(nums = [30, 20, 10, 40, 60, 50]) == 35.0
    assert candidate(nums = [25, 10, 30, 5, 40, 15]) == 20.0
    assert candidate(nums = [7, 8, 3, 4, 15, 13, 4, 1]) == 5.5
    assert candidate(nums = [5, 5, 5, 5, 5, 5]) == 5.0
    assert candidate(nums = [45, 30, 35, 20, 50, 40]) == 35.0
    assert candidate(nums = [50, 1, 50, 2, 50, 3]) == 25.5
    assert candidate(nums = [15, 15, 15, 15, 15, 15]) == 15.0
    assert candidate(nums = [1, 2, 3, 7, 8, 9]) == 5.0
    assert candidate(nums = [10, 20, 30, 40]) == 25.0
    assert candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == -12.5
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 19.5
    assert candidate(nums = [7, 3, 9, 1, 5, 11, 13, 2, 8, 6, 10, 4]) == 6.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert candidate(nums = [48, 46, 44, 42, 40, 38, 36, 34]) == 41.0
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29]) == 15.0
    assert candidate(nums = [27, 37, 23, 33, 29, 39, 21, 31]) == 30.0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2.0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 1, 8, 15]) == 18.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 6.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 8.5
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7.0
    assert candidate(nums = [45, 30, 15, 5, 50, 35, 20, 10, 40, 25]) == 27.5
    assert candidate(nums = [10, 20, 30, 40, 50, 1]) == 25.0
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 7.5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 45.0
    assert candidate(nums = [24, 12, 36, 6, 48, 24]) == 24.0
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 15.5
    assert candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94]) == 50.0
    assert candidate(nums = [23, 17, 11, 5, 31, 29, 25, 19, 35, 33, 37, 13]) == 21.0
    assert candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 30.0
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]) == 39.5
    assert candidate(nums = [20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 15.0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3.0
    assert candidate(nums = [29, 10, 34, 15, 40, 5, 30, 20]) == 22.0
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]) == 68.0
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38]) == 43.5
    assert candidate(nums = [23, 29, 27, 25, 21, 28, 26, 22, 24, 20, 19, 30, 18, 31, 17, 32, 16, 33, 15, 34, 14, 35, 13, 36, 12, 37, 11, 38, 10, 39, 9, 40, 8, 41, 7, 42, 6, 43, 5, 44, 4, 45, 3, 46, 2, 47, 1, 48, 50]) == 25.0
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 42.0
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32]) == 18.0
    assert candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 21.5
    assert candidate(nums = [48, 49, 50, 1, 2, 3, 47, 46, 45, 44]) == 25.5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 5.5
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == 36.0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10.0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 20.0
    assert candidate(nums = [50, 25, 1, 30, 45, 20, 15, 40]) == 25.5
    assert candidate(nums = [45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45]) == 45.0
    assert candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46]) == 25.5
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25.5
    assert candidate(nums = [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28]) == 28.0
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38]) == 43.5
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368]) == 195.5
    assert candidate(nums = [29, 29, 29, 29, 1, 1, 1, 1, 14, 14, 14, 14]) == 14.0
    assert candidate(nums = [29, 19, 28, 18, 27, 17, 26, 16, 25, 15, 24, 14]) == 21.5
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 38.5
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 45.5
    assert candidate(nums = [34, 34, 12, 12, 56, 56, 28, 28, 42, 42]) == 34.0
    assert candidate(nums = [3, 11, 7, 15, 9, 17, 5, 13]) == 10.0
    assert candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46, 6, 45, 7, 44, 8, 43, 9, 42, 10, 41]) == 25.5
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 22.0
    assert candidate(nums = [47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47]) == 47.0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3.0
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8.0
    assert candidate(nums = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 65.0
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 12, 20]) == 22.0
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85]) == 50.0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5.0
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 45.5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 10.5
    assert candidate(nums = [15, 20, 5, 10, 25, 30, 35, 40, 50, 55]) == 27.5
    assert candidate(nums = [30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25]) == 27.5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55.0
    assert candidate(nums = [45, 42, 43, 41, 44, 46, 47, 48]) == 44.5
    assert candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]) == 29.0
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 30.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 12.0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 8.0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21.0
    assert candidate(nums = [28, 22, 16, 10, 4, 32, 26, 20, 14, 8, 30, 12]) == 18.0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 11.0
    assert candidate(nums = [22, 38, 26, 40, 24, 36, 28, 34]) == 31.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1.0
    assert candidate(nums = [45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8.5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 65.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10.5
    assert candidate(nums = [15, 25, 35, 5, 30, 20, 40, 10]) == 22.5
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 4, 8, 12]) == 32.5
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 16.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 25.5
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]) == 20.0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 1, 8, 15, 22, 29]) == 21.5
    assert candidate(nums = [10, 20, 30, 40, 50, 1]) == 25.0
    assert candidate(nums = [1, 50, 2, 49, 3, 48, 4, 47]) == 25.5
    assert candidate(nums = [4, 8, 15, 16, 23, 42, 1, 2, 3, 5, 7, 11, 13, 17, 19, 29]) == 11.0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 4.0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 13.0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]) == 15.5
    assert candidate(nums = [42, 43, 44, 45, 46, 47, 48, 49, 50, 1]) == 25.5
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 7.5
    assert candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25]) == 22.5
    assert candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 21.5
    assert candidate(nums = [5, 15, 25, 35, 45, 50, 40, 30, 20, 10]) == 27.5
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 22.5
    assert candidate(nums = [12, 24, 36, 48, 18, 30, 42, 54]) == 33.0
    assert candidate(nums = [8, 24, 3, 12, 18, 6, 21, 9, 15, 1, 19, 7, 22, 10, 16, 4, 23, 2, 11, 13, 17, 14, 25, 20, 5]) == 13.0
    assert candidate(nums = [50, 1, 49, 2, 48, 3, 47, 4, 46, 5, 45, 6]) == 25.5
    assert candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]) == 27.5
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 29.5
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18]) == 21.5
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 50]) == 28.5
    assert candidate(nums = [21, 18, 15, 12, 9, 6, 3, 0]) == 10.5
    assert candidate(nums = [49, 2, 48, 3, 47, 4, 46, 5, 45, 6]) == 25.5
    assert candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 40.5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 12.0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 45.0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2.0
    assert candidate(nums = [33, 17, 47, 31, 27, 13, 41, 23, 39, 29, 35, 19]) == 29.0


