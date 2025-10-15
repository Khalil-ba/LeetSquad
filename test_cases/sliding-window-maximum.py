def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7],k = 3) == [3, 3, 5, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7],k = 3) == [3, 3, 5, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, -2],k = 2) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, -2],k = 2) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == [9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == [9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == [2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == [2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 1) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 1) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 2, 0, 5],k = 3) == [3, 3, 2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 2, 0, 5],k = 3) == [3, 3, 2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 4],k = 2) == [7, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 4],k = 2) == [7, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11],k = 2) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11],k = 2) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 4, 2, 3, 1, 5, 6, 7, 8, 9, 10],k = 4) == [4, 5, 6, 6, 6, 6, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 4, 2, 3, 1, 5, 6, 7, 8, 9, 10],k = 4) == [4, 5, 6, 6, 6, 6, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80, 70, 60, 50, 40, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80, 70, 60, 50, 40, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == [3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == [3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == [100, 90, 80, 70, 60, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == [100, 90, 80, 70, 60, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == [-1, -2, -3, -4, -5, -6, -7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == [-1, -2, -3, -4, -5, -6, -7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == [1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == [1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == [5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == [5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == [1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == [1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 2) == [10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 2) == [10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7, 1, 2, 4, 5, 6],k = 4) == [3, 5, 5, 6, 7, 7, 7, 7, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7, 1, 2, 4, 5, 6],k = 4) == [3, 5, 5, 6, 7, 7, 7, 7, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11],k = 6) == [5, 6, 6, 7, 8, 8, 9, 10, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11],k = 6) == [5, 6, 6, 7, 8, 8, 9, 10, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 5, 2, 8, 1, 9, 6, 4, 7],k = 5) == [8, 8, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 5, 2, 8, 1, 9, 6, 4, 7],k = 5) == [8, 8, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 4, 1, 5, 3, 6, 9, 5, 12, 2, 8, 7],k = 5) == [5, 5, 5, 6, 9, 9, 12, 12, 12, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 4, 1, 5, 3, 6, 9, 5, 12, 2, 8, 7],k = 5) == [5, 5, 5, 6, 9, 9, 12, 12, 12, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == [3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == [3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 1, 8, 7, 6, 9, 10, 11],k = 5) == [5, 8, 8, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 1, 8, 7, 6, 9, 10, 11],k = 5) == [5, 8, 8, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == [10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == [10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],k = 2) == [2, 3, 4, 5, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],k = 2) == [2, 3, 4, 5, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 5, 4, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 5) == [5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 5, 4, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 5) == [5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 3, -3, 5, -5, 6, -6, 7, -7],k = 5) == [5, 5, 6, 6, 7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 3, -3, 5, -5, 6, -6, 7, -7],k = 5) == [5, 5, 6, 6, 7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 5) == [-6, -5, -4, -3, -2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 5) == [-6, -5, -4, -3, -2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 9, 2, 7, 4, 6, 0],k = 3) == [8, 8, 9, 9, 9, 7, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 9, 2, 7, 4, 6, 0],k = 3) == [8, 8, 9, 9, 9, 7, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 10) == [10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 10) == [10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 4) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 4) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 3, 8, 2, -9, 15, 11, 1],k = 4) == [10, 8, 8, 15, 15, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 3, 8, 2, -9, 15, 11, 1],k = 4) == [10, 8, 8, 15, 15, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4],k = 4) == [4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4],k = 4) == [4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11, 8, 9, 10, 7, 12],k = 4) == [11, 11, 10, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11, 8, 9, 10, 7, 12],k = 4) == [11, 11, 10, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 5) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 5) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11, 8, 9, 10, 7, 9, 6, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [11, 11, 10, 10, 12, 12, 12, 12, 12, 11, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11, 8, 9, 10, 7, 9, 6, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [11, 11, 10, 10, 12, 12, 12, 12, 12, 11, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == [5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == [5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == [10, 9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == [10, 9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 2) == [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 2) == [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11, 8, 5, 7, 10, 6],k = 4) == [11, 11, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11, 8, 5, 7, 10, 6],k = 4) == [11, 11, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 14, 13, 7, 10, 6, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1],k = 4) == [14, 14, 13, 10, 10, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 14, 13, 7, 10, 6, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1],k = 4) == [14, 14, 13, 10, 10, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == [20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == [20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [5, 5, 5, 5, 5, 9, 9, 9, 9, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [5, 5, 5, 5, 5, 9, 9, 9, 9, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-7, -8, 7, 5, 7, 1, 6, 0, 1, 2, -7, -8, -2, -2, 0, 5, 0, 1, 2, -1, -4, -2, -1, -2, 4, 1, -5, 0, -7, -1, 10, 1, -6, 5, -8, 9, 10, 3, -4, -5, -9, -9, -3, -9, -8, -7, 7, -1, -7, -6, -6, 7, 0, 1, 4, 5, -5, -5, 2, -7, 9, 7, 9, 8, -9, -2, -5, -8, 2, -8, -6, -6, -6, 0, 1, 4, -8, -5, -6, -6, 6, -8, -8, -5, -6, -6, -7, -7, 7, -8, -6, -4, -6, -5, -8, -9, -6, -9, -7, -7, -8, -6, -7, -7, 7, -8, -5, -5, -5, 7, -7, 7, -7, -8, -6, -4, -6, -5, -8, -9, -6, -9, -7, -7, -8, -6, -7, -7, 7, -8, -5, -5, -5, 7, -7, 7, -7, -8, -6, -4, -6, -5],k = 25) == [7, 7, 7, 7, 7, 6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-7, -8, 7, 5, 7, 1, 6, 0, 1, 2, -7, -8, -2, -2, 0, 5, 0, 1, 2, -1, -4, -2, -1, -2, 4, 1, -5, 0, -7, -1, 10, 1, -6, 5, -8, 9, 10, 3, -4, -5, -9, -9, -3, -9, -8, -7, 7, -1, -7, -6, -6, 7, 0, 1, 4, 5, -5, -5, 2, -7, 9, 7, 9, 8, -9, -2, -5, -8, 2, -8, -6, -6, -6, 0, 1, 4, -8, -5, -6, -6, 6, -8, -8, -5, -6, -6, -7, -7, 7, -8, -6, -4, -6, -5, -8, -9, -6, -9, -7, -7, -8, -6, -7, -7, 7, -8, -5, -5, -5, 7, -7, 7, -7, -8, -6, -4, -6, -5, -8, -9, -6, -9, -7, -7, -8, -6, -7, -7, 7, -8, -5, -5, -5, 7, -7, 7, -7, -8, -6, -4, -6, -5],k = 25) == [7, 7, 7, 7, 7, 6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 6) == [3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 6) == [3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13],k = 3) == [10, 10, 10, 9, 15, 15, 90, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13],k = 3) == [10, 10, 10, 9, 15, 15, 90, 90]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 8) == [25, 23, 21, 19, 17, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 8) == [25, 23, 21, 19, 17, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1],k = 5) == [10000, 5000, 5000, 2500, 2500, 1250, 1250, 625, 625, 312, 312, 156, 156, 78, 78, 39, 39, 19, 19, 9, 9, 4, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1],k = 5) == [10000, 5000, 5000, 2500, 2500, 1250, 1250, 625, 625, 312, 312, 156, 156, 78, 78, 39, 39, 19, 19, 9, 9, 4, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == [1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == [1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 4) == [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 4) == [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == [8, 8, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == [8, 8, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7, 8, 1, 2, 3, 4, 5],k = 4) == [3, 5, 5, 6, 7, 8, 8, 8, 8, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7, 8, 1, 2, 3, 4, 5],k = 4) == [3, 5, 5, 6, 7, 8, 8, 8, 8, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == [3, 4, 5, 5, 5, 4, 3, 2, 3, 4, 5, 5, 5, 4, 3, 2, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == [3, 4, 5, 5, 5, 4, 3, 2, 3, 4, 5, 5, 5, 4, 3, 2, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3],k = 5) == [4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3],k = 5) == [4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 4) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 4) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 7) == [13, 15, 17, 19, 21, 23, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 7) == [13, 15, 17, 19, 21, 23, 25]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == [-10, -20, -30, -40, -50, -60, -70, -80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == [-10, -20, -30, -40, -50, -60, -70, -80]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 2, 3, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 6) == [5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 2, 3, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 6) == [5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 2, 1, 4, 7, 6, 9],k = 4) == [8, 8, 8, 7, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 2, 1, 4, 7, 6, 9],k = 4) == [8, 8, 8, 7, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == [40, 50, 60, 70, 80, 90, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == [40, 50, 60, 70, 80, 90, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],k = 4) == [3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],k = 4) == [3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10],k = 4) == [5, 4, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10],k = 4) == [5, 4, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 3) == [10000, 10000, 10000, 10000, 10000, 10000, 10000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 3) == [10000, 10000, 10000, 10000, 10000, 10000, 10000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 2) == [1, 2, 2, 3, 3, 4, 4, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 2) == [1, 2, 2, 3, 3, 4, 4, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == [-1, -2, -3, -4, -5, -6, -7, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == [-1, -2, -3, -4, -5, -6, -7, -8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5],k = 3) == [5, 4, 3, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5],k = 3) == [5, 4, 3, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 3) == [10, 9, 5, 7, 101, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 3) == [10, 9, 5, 7, 101, 101]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 12) == [20, 19, 18, 17, 16, 15, 14, 13, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 12) == [20, 19, 18, 17, 16, 15, 14, 13, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 6, 1, 8, 9, 7],k = 4) == [5, 6, 6, 8, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 6, 1, 8, 9, 7],k = 4) == [5, 6, 6, 8, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11, 8, 9, 10, 1, 7, 3, 8, 9],k = 4) == [11, 11, 10, 10, 10, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11, 8, 9, 10, 1, 7, 3, 8, 9],k = 4) == [11, 11, 10, 10, 10, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == [14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == [14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],k = 5) == [5, 5, 5, 5, 5, 4, 3, 4, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],k = 5) == [5, 5, 5, 5, 5, 4, 3, 4, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],k = 3) == [5, 4, 3, 2, 3, 4, 5, 5, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],k = 3) == [5, 4, 3, 2, 3, 4, 5, 5, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == [9, 8, 7, 6, 5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == [9, 8, 7, 6, 5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == [2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == [2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 11, 8, 9, 10, 7, 10, 5, 6],k = 4) == [11, 11, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 11, 8, 9, 10, 7, 10, 5, 6],k = 4) == [11, 11, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == [100, 90, 80, 70, 60, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == [100, 90, 80, 70, 60, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == [6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == [6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 2, 4, 1, 6, 1, 3, 2, 5, 2, 2, 4, 6, 1, 6, 3, 3, 5, 2, 1, 1, 4, 6, 3, 2, 1, 1, 5, 6, 1, 3, 5, 6, 3, 5, 6, 3, 6, 5, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 2, 4, 1, 6, 1, 3, 2, 5, 2, 2, 4, 6, 1, 6, 3, 3, 5, 2, 1, 1, 4, 6, 3, 2, 1, 1, 5, 6, 1, 3, 5, 6, 3, 5, 6, 3, 6, 5, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == [15, 14, 13, 12, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == [15, 14, 13, 12, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7],k = 3) == [3, 3, 5, 5, 6, 7]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == [5, 5, 5, 5, 5]
    assert candidate(nums = [4, -2],k = 2) == [4]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == [9, 8, 7, 6, 5, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == [2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [1],k = 1) == [1]
    assert candidate(nums = [1, 3, 1, 2, 0, 5],k = 3) == [3, 3, 2, 5]
    assert candidate(nums = [7, 2, 4],k = 2) == [7, 4]
    assert candidate(nums = [9, 11],k = 2) == [11]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 4, 2, 3, 1, 5, 6, 7, 8, 9, 10],k = 4) == [4, 5, 6, 6, 6, 6, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80, 70, 60, 50, 40, 30]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == [3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == [100, 90, 80, 70, 60, 50]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == [-1, -2, -3, -4, -5, -6, -7]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == [1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == [5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 2) == [10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7, 1, 2, 4, 5, 6],k = 4) == [3, 5, 5, 6, 7, 7, 7, 7, 5, 6]
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11],k = 6) == [5, 6, 6, 7, 8, 8, 9, 10, 10, 11]
    assert candidate(nums = [5, 3, 5, 2, 8, 1, 9, 6, 4, 7],k = 5) == [8, 8, 9, 9, 9, 9]
    assert candidate(nums = [5, 3, 4, 4, 1, 5, 3, 6, 9, 5, 12, 2, 8, 7],k = 5) == [5, 5, 5, 6, 9, 9, 12, 12, 12, 12]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == [3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [5, 3, 4, 2, 1, 8, 7, 6, 9, 10, 11],k = 5) == [5, 8, 8, 8, 9, 10, 11]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == [10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],k = 2) == [2, 3, 4, 5, 5, 4, 3, 2]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    assert candidate(nums = [2, 1, 3, 5, 4, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 5) == [5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 5]
    assert candidate(nums = [1, -1, 3, -3, 5, -5, 6, -6, 7, -7],k = 5) == [5, 5, 6, 6, 7, 7]
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 5) == [-6, -5, -4, -3, -2, -1]
    assert candidate(nums = [5, 3, 8, 1, 9, 2, 7, 4, 6, 0],k = 3) == [8, 8, 9, 9, 9, 7, 7, 6]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 10) == [10, 9, 8, 7, 6, 5]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 4) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [10, -5, 3, 8, 2, -9, 15, 11, 1],k = 4) == [10, 8, 8, 15, 15, 15]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4],k = 4) == [4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 3, 4]
    assert candidate(nums = [9, 11, 8, 9, 10, 7, 12],k = 4) == [11, 11, 10, 12]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 5) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [9, 11, 8, 9, 10, 7, 9, 6, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [11, 11, 10, 10, 12, 12, 12, 12, 12, 11, 10, 9, 8, 7, 6, 5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == [5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == [10, 9, 8, 7, 6, 5, 4]
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 2) == [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [9, 11, 8, 5, 7, 10, 6],k = 4) == [11, 11, 10, 10]
    assert candidate(nums = [10, 14, 13, 7, 10, 6, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1],k = 4) == [14, 14, 13, 10, 10, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == [20]
    assert candidate(nums = [1, 3, 2, 1, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [5, 5, 5, 5, 5, 9, 9, 9, 9, 9, 8, 7, 6, 5]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [-7, -8, 7, 5, 7, 1, 6, 0, 1, 2, -7, -8, -2, -2, 0, 5, 0, 1, 2, -1, -4, -2, -1, -2, 4, 1, -5, 0, -7, -1, 10, 1, -6, 5, -8, 9, 10, 3, -4, -5, -9, -9, -3, -9, -8, -7, 7, -1, -7, -6, -6, 7, 0, 1, 4, 5, -5, -5, 2, -7, 9, 7, 9, 8, -9, -2, -5, -8, 2, -8, -6, -6, -6, 0, 1, 4, -8, -5, -6, -6, 6, -8, -8, -5, -6, -6, -7, -7, 7, -8, -6, -4, -6, -5, -8, -9, -6, -9, -7, -7, -8, -6, -7, -7, 7, -8, -5, -5, -5, 7, -7, 7, -7, -8, -6, -4, -6, -5, -8, -9, -6, -9, -7, -7, -8, -6, -7, -7, 7, -8, -5, -5, -5, 7, -7, 7, -7, -8, -6, -4, -6, -5],k = 25) == [7, 7, 7, 7, 7, 6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 6) == [3, 3, 3, 3, 3]
    assert candidate(nums = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13],k = 3) == [10, 10, 10, 9, 15, 15, 90, 90]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 8) == [25, 23, 21, 19, 17, 15]
    assert candidate(nums = [10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1],k = 5) == [10000, 5000, 5000, 2500, 2500, 1250, 1250, 625, 625, 312, 312, 156, 156, 78, 78, 39, 39, 19, 19, 9, 9, 4, 4, 2]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 4) == [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [5, 3, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == [8, 8, 8, 7, 6, 5, 4, 3]
    assert candidate(nums = [1, 3, -1, -3, 5, 3, 6, 7, 8, 1, 2, 3, 4, 5],k = 4) == [3, 5, 5, 6, 7, 8, 8, 8, 8, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == [3, 4, 5, 5, 5, 4, 3, 2, 3, 4, 5, 5, 5, 4, 3, 2, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3],k = 5) == [4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3]
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 4) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 7) == [13, 15, 17, 19, 21, 23, 25]
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == [-10, -20, -30, -40, -50, -60, -70, -80]
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [3, 2, 2, 3, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 6) == [5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(nums = [5, 3, 8, 2, 1, 4, 7, 6, 9],k = 4) == [8, 8, 8, 7, 7, 9]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == [40, 50, 60, 70, 80, 90, 100]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],k = 4) == [3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 5, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10],k = 4) == [5, 4, 6, 7, 8, 9, 10]
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 3) == [10000, 10000, 10000, 10000, 10000, 10000, 10000]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 2) == [1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == [-1, -2, -3, -4, -5, -6, -7, -8]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5],k = 3) == [5, 4, 3, 2, 3, 4, 5]
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 3) == [10, 9, 5, 7, 101, 101]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 12) == [20, 19, 18, 17, 16, 15, 14, 13, 12]
    assert candidate(nums = [5, 3, 4, 2, 6, 1, 8, 9, 7],k = 4) == [5, 6, 6, 8, 9, 9]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [9, 11, 8, 9, 10, 1, 7, 3, 8, 9],k = 4) == [11, 11, 10, 10, 10, 8, 9]
    assert candidate(nums = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == [14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == [10, 9, 8, 7, 6, 5]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],k = 5) == [5, 5, 5, 5, 5, 4, 3, 4, 5, 5, 5, 5, 5]
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],k = 3) == [5, 4, 3, 2, 3, 4, 5, 5, 5, 4, 3]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == [9, 8, 7, 6, 5, 4, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [9, 11, 8, 9, 10, 7, 10, 5, 6],k = 4) == [11, 11, 10, 10, 10, 10]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == [100, 90, 80, 70, 60, 50]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == [6, 7, 8, 9, 10]
    assert candidate(nums = [5, 2, 2, 4, 1, 6, 1, 3, 2, 5, 2, 2, 4, 6, 1, 6, 3, 3, 5, 2, 1, 1, 4, 6, 3, 2, 1, 1, 5, 6, 1, 3, 5, 6, 3, 5, 6, 3, 6, 5, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == [15, 14, 13, 12, 11, 10, 9, 8]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == [0]
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]


