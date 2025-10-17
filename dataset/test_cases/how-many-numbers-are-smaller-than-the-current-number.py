def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96]) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96]) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3]) == [0, 0, 2, 2, 4, 4, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3]) == [0, 0, 2, 2, 4, 4, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97]) == [3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97]) == [3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 1, 2, 5]) == [3, 0, 1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 1, 2, 5]) == [3, 0, 1, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 4]) == [1, 2, 0, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 4]) == [1, 2, 0, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 50, 25, 75]) == [4, 0, 2, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 50, 25, 75]) == [4, 0, 2, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 6, 1, 5]) == [2, 0, 4, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 6, 1, 5]) == [2, 0, 4, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 4, 8]) == [2, 1, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 4, 8]) == [2, 1, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 1]) == [1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 1]) == [1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1]) == [0, 0, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1]) == [0, 0, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7]) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7]) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40]) == [4, 1, 2, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40]) == [4, 1, 2, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 50, 25, 75, 12, 37, 62, 88, 99]) == [9, 0, 4, 2, 6, 1, 3, 5, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 50, 25, 75, 12, 37, 62, 88, 99]) == [9, 0, 4, 2, 6, 1, 3, 5, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100]) == [0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100]) == [0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [13, 0, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 16, 16, 18, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [13, 0, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 16, 16, 18, 18]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8, 12, 12, 12, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8, 12, 12, 12, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 100, 99, 98, 97]) == [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 100, 99, 98, 97]) == [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 3, 9, 1, 7, 4, 6, 2, 0]) == [5, 8, 3, 9, 1, 7, 4, 6, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 3, 9, 1, 7, 4, 6, 2, 0]) == [5, 8, 3, 9, 1, 7, 4, 6, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 23, 78, 56, 34, 12, 90, 67, 89, 2, 3, 1, 5, 6, 7, 8, 9, 10, 11]) == [13, 11, 16, 14, 12, 10, 18, 15, 17, 1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 23, 78, 56, 34, 12, 90, 67, 89, 2, 3, 1, 5, 6, 7, 8, 9, 10, 11]) == [13, 11, 16, 14, 12, 10, 18, 15, 17, 1, 2, 0, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 31, 77, 28, 55, 19, 89, 64, 42, 77]) == [3, 2, 7, 1, 5, 0, 9, 6, 3, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 31, 77, 28, 55, 19, 89, 64, 42, 77]) == [3, 2, 7, 1, 5, 0, 9, 6, 3, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 25, 50, 75, 100]) == [0, 2, 4, 6, 0, 2, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 25, 50, 75, 100]) == [0, 2, 4, 6, 0, 2, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == [0, 2, 4, 6, 8, 10, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == [0, 2, 4, 6, 8, 10, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [47, 53, 100, 42, 55, 80, 86, 29, 93, 37, 48, 51, 21, 79, 68, 94, 3, 8, 58, 52]) == [6, 10, 19, 5, 11, 15, 16, 3, 17, 4, 7, 8, 2, 14, 13, 18, 0, 1, 12, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [47, 53, 100, 42, 55, 80, 86, 29, 93, 37, 48, 51, 21, 79, 68, 94, 3, 8, 58, 52]) == [6, 10, 19, 5, 11, 15, 16, 3, 17, 4, 7, 8, 2, 14, 13, 18, 0, 1, 12, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95]) == [5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95]) == [5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 0, 3, 4, 9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [2, 1, 0, 3, 4, 9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 0, 3, 4, 9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [2, 1, 0, 3, 4, 9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10]) == [4, 2, 0, 1, 3, 5, 7, 6, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10]) == [4, 2, 0, 1, 3, 5, 7, 6, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 67, 23, 89, 23, 67, 34, 23, 67, 89]) == [3, 5, 0, 8, 0, 5, 3, 0, 5, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 67, 23, 89, 23, 67, 34, 23, 67, 89]) == [3, 5, 0, 8, 0, 5, 3, 0, 5, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 25, 50, 75, 50, 25, 75, 50]) == [3, 0, 7, 0, 3, 7, 3, 0, 7, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 25, 50, 75, 50, 25, 75, 50]) == [3, 0, 7, 0, 3, 7, 3, 0, 7, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 12, 37, 88, 63, 49, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [14, 11, 16, 10, 12, 17, 15, 13, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 12, 37, 88, 63, 49, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [14, 11, 16, 10, 12, 17, 15, 13, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 9, 8, 7, 6, 0]) == [3, 1, 2, 4, 5, 9, 8, 7, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 9, 8, 7, 6, 0]) == [3, 1, 2, 4, 5, 9, 8, 7, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 24, 7, 9, 12, 33, 18, 42, 60, 5]) == [8, 5, 1, 2, 3, 6, 4, 7, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 24, 7, 9, 12, 33, 18, 42, 60, 5]) == [8, 5, 1, 2, 3, 6, 4, 7, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 10, 30, 40, 5, 15, 25, 35, 45]) == [9, 3, 1, 5, 7, 0, 2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 10, 30, 40, 5, 15, 25, 35, 45]) == [9, 3, 1, 5, 7, 0, 2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1, 0, 0, 0]) == [7, 7, 7, 5, 5, 3, 3, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1, 0, 0, 0]) == [7, 7, 7, 5, 5, 3, 3, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60]) == [9, 7, 5, 3, 1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60]) == [9, 7, 5, 3, 1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11]) == [2, 4, 6, 8, 1, 3, 5, 7, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11]) == [2, 4, 6, 8, 1, 3, 5, 7, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 0, 0, 0, 2, 2, 2, 2]) == [3, 3, 3, 0, 0, 0, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 0, 0, 0, 2, 2, 2, 2]) == [3, 3, 3, 0, 0, 0, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0]) == [9, 8, 7, 6, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0]) == [9, 8, 7, 6, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 100, 50, 25, 75, 20, 80, 30, 60, 40, 90]) == [0, 10, 5, 2, 7, 1, 8, 3, 6, 4, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 100, 50, 25, 75, 20, 80, 30, 60, 40, 90]) == [0, 10, 5, 2, 7, 1, 8, 3, 6, 4, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == [4, 9, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == [4, 9, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5]) == [13, 11, 9, 7, 5, 4, 3, 2, 1, 0, 13, 11, 9, 7, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5]) == [13, 11, 9, 7, 5, 4, 3, 2, 1, 0, 13, 11, 9, 7, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40]) == [4, 1, 2, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40]) == [4, 1, 2, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0]) == [15, 12, 9, 6, 3, 0, 15, 12, 9, 6, 3, 0, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0]) == [15, 12, 9, 6, 3, 0, 15, 12, 9, 6, 3, 0, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 30, 30, 20, 10, 40, 40, 50, 50, 60, 60, 70]) == [0, 3, 3, 0, 6, 6, 3, 0, 8, 8, 10, 10, 12, 12, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 30, 30, 20, 10, 40, 40, 50, 50, 60, 60, 70]) == [0, 3, 3, 0, 6, 6, 3, 0, 8, 8, 10, 10, 12, 12, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 25, 75, 50, 25, 75, 50, 25]) == [4, 0, 7, 0, 7, 4, 0, 7, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 25, 75, 50, 25, 75, 50, 25]) == [4, 0, 7, 0, 7, 4, 0, 7, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [0, 2, 1, 3, 5, 4, 6, 8, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [0, 2, 1, 3, 5, 4, 6, 8, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 38, 27, 16, 5, 48, 37, 26, 15, 4, 47, 36, 25, 14, 3, 46, 35, 24, 13, 2, 45, 34, 23, 12, 1, 44, 33, 22, 11, 0]) == [29, 23, 17, 11, 5, 28, 22, 16, 10, 4, 27, 21, 15, 9, 3, 26, 20, 14, 8, 2, 25, 19, 13, 7, 1, 24, 18, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 38, 27, 16, 5, 48, 37, 26, 15, 4, 47, 36, 25, 14, 3, 46, 35, 24, 13, 2, 45, 34, 23, 12, 1, 44, 33, 22, 11, 0]) == [29, 23, 17, 11, 5, 28, 22, 16, 10, 4, 27, 21, 15, 9, 3, 26, 20, 14, 8, 2, 25, 19, 13, 7, 1, 24, 18, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 40, 50, 10]) == [0, 3, 0, 4, 5, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 40, 50, 10]) == [0, 3, 0, 4, 5, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 10, 55, 72, 21, 45, 66, 100, 33, 55, 72, 21, 45, 66, 100, 33, 55, 72, 21, 45, 66, 100]) == [4, 0, 10, 16, 1, 7, 13, 19, 4, 10, 16, 1, 7, 13, 19, 4, 10, 16, 1, 7, 13, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 10, 55, 72, 21, 45, 66, 100, 33, 55, 72, 21, 45, 66, 100, 33, 55, 72, 21, 45, 66, 100]) == [4, 0, 10, 16, 1, 7, 13, 19, 4, 10, 16, 1, 7, 13, 19, 4, 10, 16, 1, 7, 13, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == [18, 14, 10, 6, 2, 0, 2, 6, 10, 14, 18, 14, 10, 6, 2, 0, 2, 6, 10, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == [18, 14, 10, 6, 2, 0, 2, 6, 10, 14, 18, 14, 10, 6, 2, 0, 2, 6, 10, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 23, 56, 12, 78, 45, 90, 67, 34, 23, 12, 56, 78, 45, 67, 90]) == [4, 2, 8, 0, 12, 6, 14, 10, 4, 2, 0, 8, 12, 6, 10, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 23, 56, 12, 78, 45, 90, 67, 34, 23, 12, 56, 78, 45, 67, 90]) == [4, 2, 8, 0, 12, 6, 14, 10, 4, 2, 0, 8, 12, 6, 10, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 32, 55, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == [4, 2, 6, 0, 1, 3, 5, 6, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 32, 55, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == [4, 2, 6, 0, 1, 3, 5, 6, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [0, 5, 0, 5, 0, 5, 0, 5, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [0, 5, 0, 5, 0, 5, 0, 5, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == [0, 2, 4, 6, 8, 10, 11, 12, 13, 14, 0, 2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == [0, 2, 4, 6, 8, 10, 11, 12, 13, 14, 0, 2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == [0, 19, 1, 18, 2, 17, 3, 16, 4, 15, 5, 14, 6, 13, 7, 12, 8, 11, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == [0, 19, 1, 18, 2, 17, 3, 16, 4, 15, 5, 14, 6, 13, 7, 12, 8, 11, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 67, 89, 23, 34, 56, 78, 90, 12, 34, 56, 78, 90, 23, 45, 67, 89]) == [5, 9, 13, 1, 3, 7, 11, 15, 0, 3, 7, 11, 15, 1, 5, 9, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 67, 89, 23, 34, 56, 78, 90, 12, 34, 56, 78, 90, 23, 45, 67, 89]) == [5, 9, 13, 1, 3, 7, 11, 15, 0, 3, 7, 11, 15, 1, 5, 9, 13]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 30, 40, 50]) == [0, 2, 0, 2, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 30, 40, 50]) == [0, 2, 0, 2, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    assert candidate(nums = [100, 99, 98, 97, 96]) == [4, 3, 2, 1, 0]
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3]) == [0, 0, 2, 2, 4, 4, 6, 6]
    assert candidate(nums = [100, 99, 98, 97]) == [3, 2, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [3, 0, 1, 2, 5]) == [3, 0, 1, 2, 4]
    assert candidate(nums = [10, 20, 30, 40, 50]) == [0, 1, 2, 3, 4]
    assert candidate(nums = [1, 2, 0, 3, 4]) == [1, 2, 0, 3, 4]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [100, 0, 50, 25, 75]) == [4, 0, 2, 1, 3]
    assert candidate(nums = [3, 0, 6, 1, 5]) == [2, 0, 4, 1, 3]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [6, 5, 4, 8]) == [2, 1, 0, 3]
    assert candidate(nums = [5, 5, 5, 5, 1]) == [1, 1, 1, 1, 0]
    assert candidate(nums = [0, 0, 0, 1]) == [0, 0, 0, 3]
    assert candidate(nums = [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
    assert candidate(nums = [7, 7, 7, 7]) == [0, 0, 0, 0]
    assert candidate(nums = [50, 20, 30, 10, 40]) == [4, 1, 2, 0, 3]
    assert candidate(nums = [3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [100, 0, 50, 25, 75, 12, 37, 62, 88, 99]) == [9, 0, 4, 2, 6, 1, 3, 5, 7, 8]
    assert candidate(nums = [0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100, 0, 50, 100]) == [0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56, 0, 28, 56]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [8, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [13, 0, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 16, 16, 18, 18]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8, 12, 12, 12, 12]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 100, 99, 98, 97]) == [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]
    assert candidate(nums = [5, 8, 3, 9, 1, 7, 4, 6, 2, 0]) == [5, 8, 3, 9, 1, 7, 4, 6, 2, 0]
    assert candidate(nums = [42, 23, 78, 56, 34, 12, 90, 67, 89, 2, 3, 1, 5, 6, 7, 8, 9, 10, 11]) == [13, 11, 16, 14, 12, 10, 18, 15, 17, 1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(nums = [42, 31, 77, 28, 55, 19, 89, 64, 42, 77]) == [3, 2, 7, 1, 5, 0, 9, 6, 3, 7]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    assert candidate(nums = [25, 50, 75, 100, 25, 50, 75, 100]) == [0, 2, 4, 6, 0, 2, 4, 6]
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == [0, 2, 4, 6, 8, 10, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [47, 53, 100, 42, 55, 80, 86, 29, 93, 37, 48, 51, 21, 79, 68, 94, 3, 8, 58, 52]) == [6, 10, 19, 5, 11, 15, 16, 3, 17, 4, 7, 8, 2, 14, 13, 18, 0, 1, 12, 9]
    assert candidate(nums = [100, 99, 98, 97, 96, 95]) == [5, 4, 3, 2, 1, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [2, 1, 0, 3, 4, 9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [2, 1, 0, 3, 4, 9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10]) == [4, 2, 0, 1, 3, 5, 7, 6, 8, 9]
    assert candidate(nums = [34, 67, 23, 89, 23, 67, 34, 23, 67, 89]) == [3, 5, 0, 8, 0, 5, 3, 0, 5, 8]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, 25, 75, 25, 50, 75, 50, 25, 75, 50]) == [3, 0, 7, 0, 3, 7, 3, 0, 7, 3]
    assert candidate(nums = [50, 25, 75, 12, 37, 88, 63, 49, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [14, 11, 16, 10, 12, 17, 15, 13, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [3, 1, 2, 4, 5, 9, 8, 7, 6, 0]) == [3, 1, 2, 4, 5, 9, 8, 7, 6, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
    assert candidate(nums = [50, 24, 7, 9, 12, 33, 18, 42, 60, 5]) == [8, 5, 1, 2, 3, 6, 4, 7, 9, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
    assert candidate(nums = [50, 20, 10, 30, 40, 5, 15, 25, 35, 45]) == [9, 3, 1, 5, 7, 0, 2, 4, 6, 8]
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 0, 0, 0]) == [7, 7, 7, 5, 5, 3, 3, 0, 0, 0]
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60]) == [9, 7, 5, 3, 1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11]
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8]
    assert candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11]) == [2, 4, 6, 8, 1, 3, 5, 7, 9, 0]
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 2, 2, 2, 2]) == [3, 3, 3, 0, 0, 0, 6, 6, 6, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0]) == [9, 8, 7, 6, 5, 0, 0, 0, 0, 0]
    assert candidate(nums = [100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(nums = [0, 100, 50, 25, 75, 20, 80, 30, 60, 40, 90]) == [0, 10, 5, 2, 7, 1, 8, 3, 6, 4, 9]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [23, 45, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == [4, 9, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18, 0, 5, 10, 14, 18]
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5]) == [13, 11, 9, 7, 5, 4, 3, 2, 1, 0, 13, 11, 9, 7, 5]
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [50, 20, 30, 10, 40]) == [4, 1, 2, 0, 3]
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0]) == [15, 12, 9, 6, 3, 0, 15, 12, 9, 6, 3, 0, 15, 12, 9, 6, 3, 0]
    assert candidate(nums = [10, 20, 20, 10, 30, 30, 20, 10, 40, 40, 50, 50, 60, 60, 70]) == [0, 3, 3, 0, 6, 6, 3, 0, 8, 8, 10, 10, 12, 12, 14]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, 25, 75, 25, 75, 50, 25, 75, 50, 25]) == [4, 0, 7, 0, 7, 4, 0, 7, 4, 0]
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [0, 2, 1, 3, 5, 4, 6, 8, 7, 9]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [49, 38, 27, 16, 5, 48, 37, 26, 15, 4, 47, 36, 25, 14, 3, 46, 35, 24, 13, 2, 45, 34, 23, 12, 1, 44, 33, 22, 11, 0]) == [29, 23, 17, 11, 5, 28, 22, 16, 10, 4, 27, 21, 15, 9, 3, 26, 20, 14, 8, 2, 25, 19, 13, 7, 1, 24, 18, 12, 6, 0]
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [10, 20, 10, 30, 40, 50, 10]) == [0, 3, 0, 4, 5, 6, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    assert candidate(nums = [33, 10, 55, 72, 21, 45, 66, 100, 33, 55, 72, 21, 45, 66, 100, 33, 55, 72, 21, 45, 66, 100]) == [4, 0, 10, 16, 1, 7, 13, 19, 4, 10, 16, 1, 7, 13, 19, 4, 10, 16, 1, 7, 13, 19]
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == [18, 14, 10, 6, 2, 0, 2, 6, 10, 14, 18, 14, 10, 6, 2, 0, 2, 6, 10, 14]
    assert candidate(nums = [34, 23, 56, 12, 78, 45, 90, 67, 34, 23, 12, 56, 78, 45, 67, 90]) == [4, 2, 8, 0, 12, 6, 14, 10, 4, 2, 0, 8, 12, 6, 10, 14]
    assert candidate(nums = [42, 32, 55, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == [4, 2, 6, 0, 1, 3, 5, 6, 8, 9, 10, 11]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [0, 5, 0, 5, 0, 5, 0, 5, 0, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == [0, 2, 4, 6, 8, 10, 11, 12, 13, 14, 0, 2, 4, 6, 8]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == [0, 19, 1, 18, 2, 17, 3, 16, 4, 15, 5, 14, 6, 13, 7, 12, 8, 11, 9, 10]
    assert candidate(nums = [45, 67, 89, 23, 34, 56, 78, 90, 12, 34, 56, 78, 90, 23, 45, 67, 89]) == [5, 9, 13, 1, 3, 7, 11, 15, 0, 3, 7, 11, 15, 1, 5, 9, 13]
    assert candidate(nums = [10, 20, 10, 20, 30, 40, 50]) == [0, 2, 0, 2, 4, 5, 6]
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


