def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 2, 5, 6, 9, 7, 8, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 2, 5, 6, 9, 7, 8, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4, 6, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4, 6, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4, 3, 6, 5, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4, 3, 6, 5, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 5, 4, 8, 7, 10, 9, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 5, 4, 8, 7, 10, 9, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 6, 5, 4, 9, 7, 10, 8]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 6, 5, 4, 9, 7, 10, 8]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 3, 2, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 3, 2, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 6, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 6, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3, 5, 6, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3, 5, 6, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 4, 1, 6, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 4, 1, 6, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 3, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 3, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 1, 18, 3, 16, 5, 14, 7, 12, 9, 10, 11, 8, 13, 6, 15, 4, 17, 2, 19]) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 1, 18, 3, 16, 5, 14, 7, 12, 9, 10, 11, 8, 13, 6, 15, 4, 17, 2, 19]) == 370: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 15, 5, 30, 20, 10, 2, 24, 14, 4, 23, 13, 3, 22, 12, 1, 21, 11, 19, 9, 18, 8, 17, 7, 16, 6]) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 15, 5, 30, 20, 10, 2, 24, 14, 4, 23, 13, 3, 22, 12, 1, 21, 11, 19, 9, 18, 8, 17, 7, 16, 6]) == 252: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 15, 3, 14, 4, 13, 5, 12, 6, 11, 7, 10, 8, 9, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 15, 3, 14, 4, 13, 5, 12, 6, 11, 7, 10, 8, 9, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 10, 3, 6, 2, 8, 1, 7, 5, 9]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 10, 3, 6, 2, 8, 1, 7, 5, 9]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 6, 2, 5, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 6, 2, 5, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 8, 3, 7, 4, 10, 6, 1, 9]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 8, 3, 7, 4, 10, 6, 1, 9]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 1, 8, 3, 9, 2, 10, 5, 7, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 1, 8, 3, 9, 2, 10, 5, 7, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 1, 7, 6, 10, 9, 12, 11, 15, 14, 18, 17, 20, 19, 22, 21, 24, 23]) == 448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 1, 7, 6, 10, 9, 12, 11, 15, 14, 18, 17, 20, 19, 22, 21, 24, 23]) == 448: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 3, 2, 8, 5, 4, 9, 10, 7]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 3, 2, 8, 5, 4, 9, 10, 7]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 5, 7, 4, 3, 2, 1, 9, 10, 11, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 5, 7, 4, 3, 2, 1, 9, 10, 11, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 7, 3, 8, 5, 10, 6, 11, 9, 14, 12, 15, 13]) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 7, 3, 8, 5, 10, 6, 11, 9, 14, 12, 15, 13]) == 224: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 7, 10, 2, 6, 8, 3, 5, 9, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 7, 10, 2, 6, 8, 3, 5, 9, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 9, 3, 8, 4, 7, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 9, 3, 8, 4, 7, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 5, 2, 9, 4, 7, 1, 6, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 5, 2, 9, 4, 7, 1, 6, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [40, 1, 39, 2, 38, 3, 37, 4, 36, 5, 35, 6, 34, 7, 33, 8, 32, 9, 31, 10, 30, 11, 29, 12, 28, 13, 27, 14, 26, 15, 25, 16, 24, 17, 23, 18, 22, 19, 21, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [40, 1, 39, 2, 38, 3, 37, 4, 36, 5, 35, 6, 34, 7, 33, 8, 32, 9, 31, 10, 30, 11, 29, 12, 28, 13, 27, 14, 26, 15, 25, 16, 24, 17, 23, 18, 22, 19, 21, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 27, 21, 24, 15, 26, 18, 23, 10, 25, 12, 22, 6, 20, 9, 19, 3, 17, 2, 16, 5, 14, 8, 13, 1, 11, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 27, 21, 24, 15, 26, 18, 23, 10, 25, 12, 22, 6, 20, 9, 19, 3, 17, 2, 16, 5, 14, 8, 13, 1, 11, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 3, 2, 9, 5, 7, 4, 8, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 3, 2, 9, 5, 7, 4, 8, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 3, 5, 2, 6, 4, 7, 8, 9]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 3, 5, 2, 6, 4, 7, 8, 9]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 3]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 3]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 5, 3, 8, 2, 7, 6, 10, 9]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 5, 3, 8, 2, 7, 6, 10, 9]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 3, 9, 2, 8, 4, 10, 6]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 3, 9, 2, 8, 4, 10, 6]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 1, 6, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 1, 6, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 448: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 1, 5, 8, 2, 7, 4, 10, 9]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 1, 5, 8, 2, 7, 4, 10, 9]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 5, 4, 10, 6, 1, 9, 8, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 5, 4, 10, 6, 1, 9, 8, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 7, 2, 6, 3, 5, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 7, 2, 6, 3, 5, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3992, 3991, 3990, 3989, 3988, 3987, 3986, 3985, 3984, 3983, 3982, 3981, 3980, 3979, 3978, 3977, 3976, 3975, 3974, 3973, 3972, 3971, 3970, 3969, 3968, 3967, 3966, 3965, 3964, 3963, 3962, 3961, 3960, 3959, 3958, 3957, 3956, 3955, 3954, 3953, 3952, 3951, 3950, 3949, 3948, 3947, 3946, 3945, 3944, 3943, 3942, 3941, 3940, 3939, 3938, 3937, 3936, 3935, 3934, 3933, 3932, 3931, 3930, 3929, 3928, 3927, 3926, 3925, 3924, 3923, 3922, 3921, 3920, 3919, 3918, 3917, 3916, 3915, 3914, 3913, 3912, 3911, 3910, 3909, 3908, 3907, 3906, 3905, 3904, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3860, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809, 3808, 3807, 3806, 3805, 3804, 3803, 3802, 3801, 3800, 3799, 3798, 3797, 3796, 3795, 3794, 3793, 3792, 3791, 3790, 3789, 3788, 3787, 3786, 3785, 3784, 3783, 3782, 3781, 3780, 3779, 3778, 3777, 3776, 3775, 3774, 3773, 3772, 3771, 3770, 3769, 3768, 3767, 3766, 3765, 3764, 3763, 3762, 3761, 3760, 3759, 3758, 3757, 3756, 3755, 3754, 3753, 3752, 3751, 3750, 3749, 3748, 3747, 3746, 3745, 3744, 3743, 3742, 3741, 3740, 3739, 3738, 3737, 3736, 3735, 3734, 3733, 3732, 3731, 3730, 3729, 3728, 3727, 3726, 3725, 3724, 3723, 3722, 3721, 3720, 3719, 3718, 3717, 3716, 3715, 3714, 3713, 3712, 3711, 3710, 3709, 3708, 3707, 3706, 3705, 3704, 3703, 3702, 3701, 3700, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3992, 3991, 3990, 3989, 3988, 3987, 3986, 3985, 3984, 3983, 3982, 3981, 3980, 3979, 3978, 3977, 3976, 3975, 3974, 3973, 3972, 3971, 3970, 3969, 3968, 3967, 3966, 3965, 3964, 3963, 3962, 3961, 3960, 3959, 3958, 3957, 3956, 3955, 3954, 3953, 3952, 3951, 3950, 3949, 3948, 3947, 3946, 3945, 3944, 3943, 3942, 3941, 3940, 3939, 3938, 3937, 3936, 3935, 3934, 3933, 3932, 3931, 3930, 3929, 3928, 3927, 3926, 3925, 3924, 3923, 3922, 3921, 3920, 3919, 3918, 3917, 3916, 3915, 3914, 3913, 3912, 3911, 3910, 3909, 3908, 3907, 3906, 3905, 3904, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3860, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809, 3808, 3807, 3806, 3805, 3804, 3803, 3802, 3801, 3800, 3799, 3798, 3797, 3796, 3795, 3794, 3793, 3792, 3791, 3790, 3789, 3788, 3787, 3786, 3785, 3784, 3783, 3782, 3781, 3780, 3779, 3778, 3777, 3776, 3775, 3774, 3773, 3772, 3771, 3770, 3769, 3768, 3767, 3766, 3765, 3764, 3763, 3762, 3761, 3760, 3759, 3758, 3757, 3756, 3755, 3754, 3753, 3752, 3751, 3750, 3749, 3748, 3747, 3746, 3745, 3744, 3743, 3742, 3741, 3740, 3739, 3738, 3737, 3736, 3735, 3734, 3733, 3732, 3731, 3730, 3729, 3728, 3727, 3726, 3725, 3724, 3723, 3722, 3721, 3720, 3719, 3718, 3717, 3716, 3715, 3714, 3713, 3712, 3711, 3710, 3709, 3708, 3707, 3706, 3705, 3704, 3703, 3702, 3701, 3700, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 10, 4, 6, 2, 9, 3, 7, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 10, 4, 6, 2, 9, 3, 7, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3992, 3991, 3990, 3989, 3988, 3987, 3986, 3985, 3984, 3983, 3982, 3981, 3980, 3979, 3978, 3977, 3976, 3975, 3974, 3973, 3972, 3971, 3970, 3969, 3968, 3967, 3966, 3965, 3964, 3963, 3962, 3961, 3960, 3959, 3958, 3957, 3956, 3955, 3954, 3953, 3952, 3951, 3950, 3949, 3948, 3947, 3946, 3945, 3944, 3943, 3942, 3941, 3940, 3939, 3938, 3937, 3936, 3935, 3934, 3933, 3932, 3931, 3930, 3929, 3928, 3927, 3926, 3925, 3924, 3923, 3922, 3921, 3920, 3919, 3918, 3917, 3916, 3915, 3914, 3913, 3912, 3911, 3910, 3909, 3908, 3907, 3906, 3905, 3904, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3860, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809, 3808, 3807, 3806, 3805, 3804, 3803, 3802, 3801, 3800, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3992, 3991, 3990, 3989, 3988, 3987, 3986, 3985, 3984, 3983, 3982, 3981, 3980, 3979, 3978, 3977, 3976, 3975, 3974, 3973, 3972, 3971, 3970, 3969, 3968, 3967, 3966, 3965, 3964, 3963, 3962, 3961, 3960, 3959, 3958, 3957, 3956, 3955, 3954, 3953, 3952, 3951, 3950, 3949, 3948, 3947, 3946, 3945, 3944, 3943, 3942, 3941, 3940, 3939, 3938, 3937, 3936, 3935, 3934, 3933, 3932, 3931, 3930, 3929, 3928, 3927, 3926, 3925, 3924, 3923, 3922, 3921, 3920, 3919, 3918, 3917, 3916, 3915, 3914, 3913, 3912, 3911, 3910, 3909, 3908, 3907, 3906, 3905, 3904, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3860, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809, 3808, 3807, 3806, 3805, 3804, 3803, 3802, 3801, 3800, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 1, 6, 9, 3, 11, 4, 14, 2, 7, 13, 5, 12, 8, 10]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 1, 6, 9, 3, 11, 4, 14, 2, 7, 13, 5, 12, 8, 10]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 9, 4, 10, 3, 1, 8, 5, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 9, 4, 10, 3, 1, 8, 5, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 182: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 2, 7, 5, 1, 8, 3, 6, 10, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 2, 7, 5, 1, 8, 3, 6, 10, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 9, 3, 6, 4, 7, 8, 10]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 9, 3, 6, 4, 7, 8, 10]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 3, 6, 7, 2, 5, 9, 1, 8, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 3, 6, 7, 2, 5, 9, 1, 8, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 5, 1, 6, 2, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 5, 1, 6, 2, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 3, 10, 2, 8, 5, 9, 4, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 3, 10, 2, 8, 5, 9, 4, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 7, 3, 6, 9, 2, 10, 8, 4]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 7, 3, 6, 9, 2, 10, 8, 4]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922, 1921, 1920, 1919, 1918, 1917, 1916, 1915, 1914, 1913, 1912, 1911, 1910, 1909, 1908, 1907, 1906, 1905, 1904, 1903, 1902, 1901, 1900, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922, 1921, 1920, 1919, 1918, 1917, 1916, 1915, 1914, 1913, 1912, 1911, 1910, 1909, 1908, 1907, 1906, 1905, 1904, 1903, 1902, 1901, 1900, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 7, 4, 6, 3, 9, 1, 8, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 7, 4, 6, 3, 9, 1, 8, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 3, 6, 2, 4, 8, 9]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 3, 6, 2, 4, 8, 9]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 40: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 2, 4, 5]) == 2
    assert candidate(nums = [4, 3, 2, 1]) == 0
    assert candidate(nums = [4, 3, 2, 1, 5, 6]) == 0
    assert candidate(nums = [3, 1, 4, 2, 5, 6, 9, 7, 8, 10]) == 18
    assert candidate(nums = [5, 2, 3, 1, 4, 6, 7]) == 0
    assert candidate(nums = [2, 1, 4, 3, 6, 5, 7]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [3, 1, 2, 4, 5]) == 0
    assert candidate(nums = [2, 3, 1, 5, 4, 8, 7, 10, 9, 6]) == 25
    assert candidate(nums = [1, 2, 3, 4]) == 0
    assert candidate(nums = [5, 1, 4, 2, 3]) == 0
    assert candidate(nums = [3, 1, 2, 6, 5, 4, 9, 7, 10, 8]) == 42
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 35
    assert candidate(nums = [1, 4, 3, 2, 5]) == 3
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7]) == 0
    assert candidate(nums = [1, 2, 4, 3, 5, 6, 7]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert candidate(nums = [5, 2, 3, 4, 1, 6, 7]) == 0
    assert candidate(nums = [1, 4, 2, 3, 5]) == 2
    assert candidate(nums = [2, 3, 1, 4, 5]) == 0
    assert candidate(nums = [5, 1, 4, 3, 2]) == 0
    assert candidate(nums = [20, 1, 18, 3, 16, 5, 14, 7, 12, 9, 10, 11, 8, 13, 6, 15, 4, 17, 2, 19]) == 370
    assert candidate(nums = [25, 15, 5, 30, 20, 10, 2, 24, 14, 4, 23, 13, 3, 22, 12, 1, 21, 11, 19, 9, 18, 8, 17, 7, 16, 6]) == 252
    assert candidate(nums = [1, 15, 3, 14, 4, 13, 5, 12, 6, 11, 7, 10, 8, 9, 2]) == 0
    assert candidate(nums = [4, 10, 3, 6, 2, 8, 1, 7, 5, 9]) == 13
    assert candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]) == 0
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [7, 1, 6, 2, 5, 3, 4]) == 0
    assert candidate(nums = [5, 2, 8, 3, 7, 4, 10, 6, 1, 9]) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(nums = [6, 1, 8, 3, 9, 2, 10, 5, 7, 4]) == 8
    assert candidate(nums = [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 0
    assert candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 0
    assert candidate(nums = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [2, 3, 5, 1, 7, 6, 10, 9, 12, 11, 15, 14, 18, 17, 20, 19, 22, 21, 24, 23]) == 448
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == 0
    assert candidate(nums = [1, 6, 3, 2, 8, 5, 4, 9, 10, 7]) == 41
    assert candidate(nums = [8, 6, 5, 7, 4, 3, 2, 1, 9, 10, 11, 12]) == 0
    assert candidate(nums = [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 0
    assert candidate(nums = [1, 4, 2, 7, 3, 8, 5, 10, 6, 11, 9, 14, 12, 15, 13]) == 224
    assert candidate(nums = [4, 7, 10, 2, 6, 8, 3, 5, 9, 1]) == 9
    assert candidate(nums = [15, 1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]) == 0
    assert candidate(nums = [10, 1, 2, 9, 3, 8, 4, 7, 5, 6]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [3, 8, 5, 2, 9, 4, 7, 1, 6, 10]) == 20
    assert candidate(nums = [40, 1, 39, 2, 38, 3, 37, 4, 36, 5, 35, 6, 34, 7, 33, 8, 32, 9, 31, 10, 30, 11, 29, 12, 28, 13, 27, 14, 26, 15, 25, 16, 24, 17, 23, 18, 22, 19, 21, 20]) == 0
    assert candidate(nums = [30, 27, 21, 24, 15, 26, 18, 23, 10, 25, 12, 22, 6, 20, 9, 19, 3, 17, 2, 16, 5, 14, 8, 13, 1, 11, 7]) == 3
    assert candidate(nums = [10, 1, 3, 2, 9, 5, 7, 4, 8, 6]) == 15
    assert candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 0
    assert candidate(nums = [15, 1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]) == 0
    assert candidate(nums = [10, 1, 3, 5, 2, 6, 4, 7, 8, 9]) == 24
    assert candidate(nums = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13]) == 270
    assert candidate(nums = [1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 3]) == 140
    assert candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]) == 0
    assert candidate(nums = [4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11]) == 240
    assert candidate(nums = [4, 1, 5, 3, 8, 2, 7, 6, 10, 9]) == 41
    assert candidate(nums = [7, 1, 5, 3, 9, 2, 8, 4, 10, 6]) == 23
    assert candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0
    assert candidate(nums = [3, 5, 2, 1, 6, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 448
    assert candidate(nums = [3, 6, 1, 5, 8, 2, 7, 4, 10, 9]) == 33
    assert candidate(nums = [3, 7, 5, 4, 10, 6, 1, 9, 8, 2]) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
    assert candidate(nums = [8, 1, 7, 2, 6, 3, 5, 4]) == 0
    assert candidate(nums = [4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3992, 3991, 3990, 3989, 3988, 3987, 3986, 3985, 3984, 3983, 3982, 3981, 3980, 3979, 3978, 3977, 3976, 3975, 3974, 3973, 3972, 3971, 3970, 3969, 3968, 3967, 3966, 3965, 3964, 3963, 3962, 3961, 3960, 3959, 3958, 3957, 3956, 3955, 3954, 3953, 3952, 3951, 3950, 3949, 3948, 3947, 3946, 3945, 3944, 3943, 3942, 3941, 3940, 3939, 3938, 3937, 3936, 3935, 3934, 3933, 3932, 3931, 3930, 3929, 3928, 3927, 3926, 3925, 3924, 3923, 3922, 3921, 3920, 3919, 3918, 3917, 3916, 3915, 3914, 3913, 3912, 3911, 3910, 3909, 3908, 3907, 3906, 3905, 3904, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3860, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809, 3808, 3807, 3806, 3805, 3804, 3803, 3802, 3801, 3800, 3799, 3798, 3797, 3796, 3795, 3794, 3793, 3792, 3791, 3790, 3789, 3788, 3787, 3786, 3785, 3784, 3783, 3782, 3781, 3780, 3779, 3778, 3777, 3776, 3775, 3774, 3773, 3772, 3771, 3770, 3769, 3768, 3767, 3766, 3765, 3764, 3763, 3762, 3761, 3760, 3759, 3758, 3757, 3756, 3755, 3754, 3753, 3752, 3751, 3750, 3749, 3748, 3747, 3746, 3745, 3744, 3743, 3742, 3741, 3740, 3739, 3738, 3737, 3736, 3735, 3734, 3733, 3732, 3731, 3730, 3729, 3728, 3727, 3726, 3725, 3724, 3723, 3722, 3721, 3720, 3719, 3718, 3717, 3716, 3715, 3714, 3713, 3712, 3711, 3710, 3709, 3708, 3707, 3706, 3705, 3704, 3703, 3702, 3701, 3700, 1]) == 0
    assert candidate(nums = [8, 1, 10, 4, 6, 2, 9, 3, 7, 5]) == 8
    assert candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 480
    assert candidate(nums = [4000, 3999, 3998, 3997, 3996, 3995, 3994, 3993, 3992, 3991, 3990, 3989, 3988, 3987, 3986, 3985, 3984, 3983, 3982, 3981, 3980, 3979, 3978, 3977, 3976, 3975, 3974, 3973, 3972, 3971, 3970, 3969, 3968, 3967, 3966, 3965, 3964, 3963, 3962, 3961, 3960, 3959, 3958, 3957, 3956, 3955, 3954, 3953, 3952, 3951, 3950, 3949, 3948, 3947, 3946, 3945, 3944, 3943, 3942, 3941, 3940, 3939, 3938, 3937, 3936, 3935, 3934, 3933, 3932, 3931, 3930, 3929, 3928, 3927, 3926, 3925, 3924, 3923, 3922, 3921, 3920, 3919, 3918, 3917, 3916, 3915, 3914, 3913, 3912, 3911, 3910, 3909, 3908, 3907, 3906, 3905, 3904, 3903, 3902, 3901, 3900, 3899, 3898, 3897, 3896, 3895, 3894, 3893, 3892, 3891, 3890, 3889, 3888, 3887, 3886, 3885, 3884, 3883, 3882, 3881, 3880, 3879, 3878, 3877, 3876, 3875, 3874, 3873, 3872, 3871, 3870, 3869, 3868, 3867, 3866, 3865, 3864, 3863, 3862, 3861, 3860, 3859, 3858, 3857, 3856, 3855, 3854, 3853, 3852, 3851, 3850, 3849, 3848, 3847, 3846, 3845, 3844, 3843, 3842, 3841, 3840, 3839, 3838, 3837, 3836, 3835, 3834, 3833, 3832, 3831, 3830, 3829, 3828, 3827, 3826, 3825, 3824, 3823, 3822, 3821, 3820, 3819, 3818, 3817, 3816, 3815, 3814, 3813, 3812, 3811, 3810, 3809, 3808, 3807, 3806, 3805, 3804, 3803, 3802, 3801, 3800, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 0
    assert candidate(nums = [15, 1, 6, 9, 3, 11, 4, 14, 2, 7, 13, 5, 12, 8, 10]) == 83
    assert candidate(nums = [7, 2, 9, 4, 10, 3, 1, 8, 5, 6]) == 4
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 0
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 182
    assert candidate(nums = [9, 2, 7, 5, 1, 8, 3, 6, 10, 4]) == 11
    assert candidate(nums = [1, 5, 2, 9, 3, 6, 4, 7, 8, 10]) == 34
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 30
    assert candidate(nums = [10, 3, 6, 7, 2, 5, 9, 1, 8, 4]) == 4
    assert candidate(nums = [4, 3, 5, 1, 6, 2, 7, 8, 9, 10]) == 4
    assert candidate(nums = [7, 1, 3, 10, 2, 8, 5, 9, 4, 6]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == 1000
    assert candidate(nums = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]) == 0
    assert candidate(nums = [1, 5, 7, 3, 6, 9, 2, 10, 8, 4]) == 23
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922, 1921, 1920, 1919, 1918, 1917, 1916, 1915, 1914, 1913, 1912, 1911, 1910, 1909, 1908, 1907, 1906, 1905, 1904, 1903, 1902, 1901, 1900, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 0
    assert candidate(nums = [10, 2, 7, 4, 6, 3, 9, 1, 8, 5]) == 11
    assert candidate(nums = [7, 1, 5, 3, 6, 2, 4, 8, 9]) == 16
    assert candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0
    assert candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 40


