def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = 8,nums = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,nums = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 9,nums = [4, 3, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 9,nums = [4, 3, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 11,nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 11,nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [10, 20, 30, 40, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [10, 20, 30, 40, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,nums = [2, 2, 2, 2, 2, 2, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,nums = [2, 2, 2, 2, 2, 2, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,nums = [3, 4, 3, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,nums = [3, 4, 3, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,nums = [2, 3, 1, 2, 4, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,nums = [2, 3, 1, 2, 4, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 4,nums = [1, 4, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4,nums = [1, 4, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 3,nums = [1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3,nums = [1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,nums = [5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,nums = [5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,nums = [2, 3, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,nums = [2, 3, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 10,nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,nums = [2, 3, 4, 2, 3, 4, 2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,nums = [2, 3, 4, 2, 3, 4, 2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 3,nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3,nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 3,nums = [1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3,nums = [1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,nums = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,nums = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 6,nums = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 6,nums = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 50,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 50,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(target = 1,nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1,nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 3,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 55,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 55,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 25,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(target = 50,nums = [10, 2, 3, 8, 5, 10, 2, 1, 3, 5, 7, 8]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 50,nums = [10, 2, 3, 8, 5, 10, 2, 1, 3, 5, 7, 8]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 25,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 18,nums = [1, 2, 3, 4, 5, 6, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 18,nums = [1, 2, 3, 4, 5, 6, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 99,nums = [50, 25, 20, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 99,nums = [50, 25, 20, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 25,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 150,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 150,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,nums = [100, 200, 300, 400, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 100, 200, 300, 400, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,nums = [100, 200, 300, 400, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 100, 200, 300, 400, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 200,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 25,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 30,nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 30,nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 10,nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 120,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 120,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 42,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 42,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 23,nums = [2, 3, 1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 23,nums = [2, 3, 1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 12,nums = [2, 3, 1, 2, 4, 3, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 12,nums = [2, 3, 1, 2, 4, 3, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 200,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 100000,nums = [10000, 20000, 30000, 40000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100000,nums = [10000, 20000, 30000, 40000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 50,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 50,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 120,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 120,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 25,nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25,nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 50,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 50,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 45,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 45,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,nums = [5, 1, 3, 5, 2, 1, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,nums = [5, 1, 3, 5, 2, 1, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,nums = [250, 250, 250, 250]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,nums = [250, 250, 250, 250]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 40,nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 40,nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 30,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 30,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 120,nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 120,nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = 8,nums = [1, 2, 3, 4, 5]) == 2
    assert candidate(target = 9,nums = [4, 3, 3, 2, 1]) == 3
    assert candidate(target = 11,nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(target = 100,nums = [10, 20, 30, 40, 50]) == 3
    assert candidate(target = 8,nums = [2, 2, 2, 2, 2, 2, 2, 2]) == 4
    assert candidate(target = 8,nums = [3, 4, 3, 1, 1, 1, 1, 1]) == 3
    assert candidate(target = 7,nums = [2, 3, 1, 2, 4, 3]) == 2
    assert candidate(target = 4,nums = [1, 4, 4]) == 1
    assert candidate(target = 3,nums = [1, 1, 1]) == 3
    assert candidate(target = 15,nums = [5, 5, 5, 5, 5]) == 3
    assert candidate(target = 5,nums = [2, 3, 1, 1, 1, 1, 1]) == 2
    assert candidate(target = 15,nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2
    assert candidate(target = 10,nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 1
    assert candidate(target = 8,nums = [2, 3, 4, 2, 3, 4, 2, 3, 4]) == 3
    assert candidate(target = 3,nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(target = 3,nums = [1, 1, 1, 1, 1]) == 3
    assert candidate(target = 15,nums = [1, 2, 3, 4, 5]) == 5
    assert candidate(target = 6,nums = [1, 2, 3, 4, 5]) == 2
    assert candidate(target = 50,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(target = 1,nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 1
    assert candidate(target = 15,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 1
    assert candidate(target = 3,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(target = 100,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 6
    assert candidate(target = 1000,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(target = 20,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(target = 5,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(target = 55,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3
    assert candidate(target = 250,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(target = 20,nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
    assert candidate(target = 100,nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(target = 25,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
    assert candidate(target = 50,nums = [10, 2, 3, 8, 5, 10, 2, 1, 3, 5, 7, 8]) == 10
    assert candidate(target = 500,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(target = 25,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(target = 18,nums = [1, 2, 3, 4, 5, 6, 7]) == 3
    assert candidate(target = 99,nums = [50, 25, 20, 5, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 4
    assert candidate(target = 25,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]) == 5
    assert candidate(target = 150,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 4
    assert candidate(target = 1000,nums = [100, 200, 300, 400, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 100, 200, 300, 400, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50]) == 4
    assert candidate(target = 15,nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5
    assert candidate(target = 200,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 8
    assert candidate(target = 100,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 4
    assert candidate(target = 25,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
    assert candidate(target = 30,nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10
    assert candidate(target = 5,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(target = 10,nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(target = 120,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]) == 3
    assert candidate(target = 42,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]) == 1
    assert candidate(target = 23,nums = [2, 3, 1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(target = 100,nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 2
    assert candidate(target = 100,nums = [50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 4
    assert candidate(target = 12,nums = [2, 3, 1, 2, 4, 3, 5]) == 3
    assert candidate(target = 200,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(target = 5,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(target = 100,nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(target = 100000,nums = [10000, 20000, 30000, 40000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000, 1000, 2000, 3000, 4000, 5000]) == 4
    assert candidate(target = 7,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(target = 50,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 4
    assert candidate(target = 120,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 5
    assert candidate(target = 25,nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 1
    assert candidate(target = 500,nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(target = 5,nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3
    assert candidate(target = 50,nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(target = 7,nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5
    assert candidate(target = 500,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 12
    assert candidate(target = 100,nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(target = 45,nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(target = 20,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 4
    assert candidate(target = 20,nums = [5, 1, 3, 5, 2, 1, 4]) == 7
    assert candidate(target = 1000,nums = [250, 250, 250, 250]) == 4
    assert candidate(target = 40,nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 3
    assert candidate(target = 30,nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 6
    assert candidate(target = 120,nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 3


