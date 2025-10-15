def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 4, 3, 2, 1]) == [6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 4, 3, 2, 1]) == [6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 2]) == [1, 2, 3, 2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 2]) == [1, 2, 3, 2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 0, 0, 1, 1, 1]) == [4, 2, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 0, 0, 1, 1, 1]) == [4, 2, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 0, 0, 10, 10, 10]) == [20, 20, 10, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 0, 0, 10, 10, 10]) == [20, 20, 10, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 1]) == [1, 6, 3, 4, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 1]) == [1, 6, 3, 4, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2]) == [1, 2, 3, 2, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2]) == [1, 2, 3, 2, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 0, 0, 10, 10, 0, 0, 10, 10]) == [20, 20, 20, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 0, 0, 10, 10, 0, 0, 10, 10]) == [20, 20, 20, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 0, 0]) == [1, 6, 3, 4, 2, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 0, 0]) == [1, 6, 3, 4, 2, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1]) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1]) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2]) == [4, 4, 4, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2]) == [4, 4, 4, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0]) == [1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0]) == [1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30]) == [20, 40, 60, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30]) == [20, 40, 60, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 0, 0, 1000, 1000]) == [2000, 2000, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 0, 0, 1000, 1000]) == [2000, 2000, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 0, 1]) == [1, 2, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 0, 1]) == [1, 2, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 0, 0, 1, 1]) == [2, 2, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 0, 0, 1, 1]) == [2, 2, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5]) == [10, 10, 10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5]) == [10, 10, 10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 0, 0, 0, 0, 0, 0]) == [10, 10, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 0, 0, 0, 0, 0, 0]) == [10, 10, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 5, 5, 4, 4]) == [12, 10, 8, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 5, 5, 4, 4]) == [12, 10, 8, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 0, 0, 1, 1]) == [4, 2, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 0, 0, 1, 1]) == [4, 2, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 4, 6, 8, 10, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 4, 6, 8, 10, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1]) == [2, 2, 2, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1]) == [2, 2, 2, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 2, 0, 0, 3, 3, 0, 0, 4, 4]) == [4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 2, 0, 0, 3, 3, 0, 0, 4, 4]) == [4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == [4, 4, 2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == [4, 4, 2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 0, 0, 2, 2]) == [4, 4, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 0, 0, 2, 2]) == [4, 4, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 0, 0, 0]) == [20, 20, 20, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 0, 0, 0]) == [20, 20, 20, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]) == [20, 20, 10, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]) == [20, 20, 10, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [2, 4, 4, 6, 6, 3, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [2, 4, 4, 6, 6, 3, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == [100, 100, 100, 100, 100, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == [100, 100, 100, 100, 100, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 10, 20, 20]) == [10, 40, 20, 40, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 10, 20, 20]) == [10, 40, 20, 40, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 0, 999, 999, 999, 0, 0, 999, 999, 999]) == [1998, 1998, 999, 1998, 999, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 0, 999, 999, 999, 0, 0, 999, 999, 999]) == [1998, 1998, 999, 1998, 999, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 0, 6, 0, 6, 0, 6, 6, 6, 0, 6, 6, 0]) == [12, 6, 6, 12, 6, 12, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 0, 6, 0, 6, 0, 6, 6, 6, 0, 6, 6, 0]) == [12, 6, 6, 12, 6, 12, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 2, 2, 1, 1]) == [1, 4, 1, 6, 4, 2, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 2, 2, 1, 1]) == [1, 4, 1, 6, 4, 2, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 1000, 1000, 500, 500, 0, 0, 0, 0]) == [1000, 2000, 1000, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 1000, 1000, 500, 500, 0, 0, 0, 0]) == [1000, 2000, 1000, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0]) == [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0]) == [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 0, 5, 5, 0, 0, 5, 5, 5, 0]) == [5, 10, 10, 5, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 0, 5, 5, 0, 0, 5, 5, 5, 0]) == [5, 10, 10, 5, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == [20, 40, 60, 80, 100, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == [20, 40, 60, 80, 100, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 0, 0, 2, 2, 0, 0, 2, 2]) == [4, 4, 4, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 0, 0, 2, 2, 0, 0, 2, 2]) == [4, 4, 4, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 999, 999, 888, 888, 777, 777]) == [2000, 1998, 1776, 1554, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 999, 999, 888, 888, 777, 777]) == [2000, 1998, 1776, 1554, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 0, 2, 2, 0, 2, 2, 0, 2]) == [4, 4, 4, 2, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 0, 2, 2, 0, 2, 2, 0, 2]) == [4, 4, 4, 2, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 4, 6, 3, 8, 8, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 4, 6, 3, 8, 8, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 2, 6, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 2, 6, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0]) == [6, 3, 6, 6, 3, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0]) == [6, 3, 6, 6, 3, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == [2, 1, 4, 2, 6, 3, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == [2, 1, 4, 2, 6, 3, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 2, 2, 2, 2, 2, 5, 5]) == [10, 5, 4, 4, 2, 10, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 2, 2, 2, 2, 2, 5, 5]) == [10, 5, 4, 4, 2, 10, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 0, 0, 0, 0, 6, 6]) == [12, 12, 12, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 0, 0, 0, 0, 6, 6]) == [12, 12, 12, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0, 3, 0, 3]) == [6, 3, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0, 3, 0, 3]) == [6, 3, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [2000, 2000, 2000, 2000, 2000, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [2000, 2000, 2000, 2000, 2000, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 4, 6, 8, 10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 4, 6, 8, 10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 10, 9, 10, 9, 10, 9, 10, 9, 10]) == [9, 10, 9, 10, 9, 10, 9, 10, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 10, 9, 10, 9, 10, 9, 10, 9, 10]) == [9, 10, 9, 10, 9, 10, 9, 10, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == [999, 999, 999, 999, 999, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == [999, 999, 999, 999, 999, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2]) == [4, 2, 4, 2, 4, 2, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2]) == [4, 2, 4, 2, 4, 2, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 0, 10, 10, 0, 10, 0, 10, 10, 10]) == [10, 20, 10, 20, 10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 0, 10, 10, 0, 10, 0, 10, 10, 10]) == [10, 20, 10, 20, 10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0]) == [1, 4, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0]) == [1, 4, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3, 2, 1, 2, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3, 2, 1, 2, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [18, 18, 18, 18, 18, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [18, 18, 18, 18, 18, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 0, 0, 5, 5, 5, 0]) == [10, 10, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 0, 0, 5, 5, 5, 0]) == [10, 10, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 0, 1, 1, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 0, 1, 1, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]) == [1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]) == [1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 4, 4, 8, 8, 16, 16, 32]) == [1, 4, 8, 16, 32, 32, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 4, 4, 8, 8, 16, 16, 32]) == [1, 4, 8, 16, 32, 32, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 0, 3, 3, 0, 0, 3, 3, 0, 3]) == [3, 6, 6, 3, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 0, 3, 3, 0, 0, 3, 3, 0, 3]) == [3, 6, 6, 3, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == [2, 2, 1, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == [2, 2, 1, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [2000, 2000, 2000, 2000, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [2000, 2000, 2000, 2000, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]) == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]) == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 0, 0, 1000, 1000, 1000, 0, 0, 1000]) == [2000, 2000, 1000, 1000, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 0, 0, 1000, 1000, 1000, 0, 0, 1000]) == [2000, 2000, 1000, 1000, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 0, 0, 5, 5, 0, 0, 5, 5]) == [10, 10, 10, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 0, 0, 5, 5, 0, 0, 5, 5]) == [10, 10, 10, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0, 0, 0, 0]) == [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0, 0, 0, 0]) == [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 0, 0, 9, 0, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9]) == [18, 9, 18, 9, 18, 18, 9, 18, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 0, 0, 9, 0, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9]) == [18, 9, 18, 9, 18, 18, 9, 18, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1]) == [1, 4, 2, 2, 1, 4, 2, 2, 4, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1]) == [1, 4, 2, 2, 1, 4, 2, 2, 4, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40]) == [20, 40, 60, 80, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40]) == [20, 40, 60, 80, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 2, 2, 0, 3, 3, 0, 4, 4, 0]) == [2, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 2, 2, 0, 3, 3, 0, 4, 4, 0]) == [2, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 0, 0, 0]) == [2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 0, 0, 0]) == [2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 0, 7, 0, 7, 0, 7, 0, 7, 0]) == [7, 7, 7, 7, 7, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 0, 7, 0, 7, 0, 7, 0, 7, 0]) == [7, 7, 7, 7, 7, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 0, 10, 0, 10, 0, 10, 0, 10]) == [10, 10, 10, 10, 10, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 0, 10, 0, 10, 0, 10, 0, 10]) == [10, 10, 10, 10, 10, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 0, 5, 5, 0, 0, 5, 5]) == [10, 5, 10, 10, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 0, 5, 5, 0, 0, 5, 5]) == [10, 5, 10, 10, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 0, 0, 5, 5, 5, 5]) == [10, 10, 10, 10, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 0, 0, 5, 5, 5, 5]) == [10, 10, 10, 10, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 0, 8, 8, 0, 8, 8, 8]) == [16, 8, 16, 16, 8, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 0, 8, 8, 0, 8, 8, 8]) == [16, 8, 16, 16, 8, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 0, 0, 0, 0, 7, 7]) == [14, 14, 14, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 0, 0, 0, 0, 7, 7]) == [14, 14, 14, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 200, 100, 100, 200, 200, 100]) == [100, 400, 200, 400, 100, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 200, 100, 100, 200, 200, 100]) == [100, 400, 200, 400, 100, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 0, 5, 5, 5, 0, 0, 5, 5]) == [10, 10, 5, 10, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 0, 5, 5, 5, 0, 0, 5, 5]) == [10, 10, 5, 10, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 0, 500, 500, 0, 250, 250, 0]) == [2000, 1000, 500, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 0, 500, 500, 0, 250, 250, 0]) == [2000, 1000, 500, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == [2, 4, 2, 6, 8, 8, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == [2, 4, 2, 6, 8, 8, 0, 0, 0, 0, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [6, 5, 4, 3, 2, 1]) == [6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 2, 3, 2]) == [1, 2, 3, 2, 3, 2]
    assert candidate(nums = [2, 2, 0, 0, 1, 1, 1]) == [4, 2, 1, 0, 0, 0, 0]
    assert candidate(nums = [10, 10, 0, 0, 10, 10, 10]) == [20, 20, 10, 0, 0, 0, 0]
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1]) == [1, 6, 3, 4, 1, 0, 0]
    assert candidate(nums = [1, 2, 3, 2, 1, 2]) == [1, 2, 3, 2, 1, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert candidate(nums = [10, 10, 0, 0, 10, 10, 0, 0, 10, 10]) == [20, 20, 20, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 0, 0]) == [1, 6, 3, 4, 2, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1]) == [1, 0]
    assert candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [2, 2, 2, 2, 2, 2]) == [4, 4, 4, 0, 0, 0]
    assert candidate(nums = [1, 0, 1, 0, 1, 0]) == [1, 1, 1, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert candidate(nums = [10, 10, 20, 20, 30, 30]) == [20, 40, 60, 0, 0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000, 1000, 0, 0, 1000, 1000]) == [2000, 2000, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 2, 0, 0, 1]) == [1, 2, 1, 0, 0, 0]
    assert candidate(nums = [1, 1, 0, 0, 1, 1]) == [2, 2, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5]) == [10, 10, 10, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 0, 0, 0, 0, 0, 0]) == [10, 10, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]
    assert candidate(nums = [6, 6, 5, 5, 4, 4]) == [12, 10, 8, 0, 0, 0]
    assert candidate(nums = [2, 2, 0, 0, 1, 1]) == [4, 2, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 4, 6, 8, 10, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == [2, 2, 2, 0, 0, 0]
    assert candidate(nums = [0, 2, 2, 0, 0, 3, 3, 0, 0, 4, 4]) == [4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [2, 2, 2, 2, 2]) == [4, 4, 2, 0, 0]
    assert candidate(nums = [2, 2, 0, 0, 2, 2]) == [4, 4, 0, 0, 0, 0]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 0, 0, 0]) == [20, 20, 20, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
    assert candidate(nums = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]) == [20, 20, 10, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [2, 4, 4, 6, 6, 3, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == [100, 100, 100, 100, 100, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 20, 20, 10, 10, 20, 20]) == [10, 40, 20, 40, 0, 0, 0]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert candidate(nums = [999, 999, 0, 999, 999, 999, 0, 0, 999, 999, 999]) == [1998, 1998, 999, 1998, 999, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [6, 6, 0, 6, 0, 6, 0, 6, 6, 6, 0, 6, 6, 0]) == [12, 6, 6, 12, 6, 12, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 2, 2, 1, 1]) == [1, 4, 1, 6, 4, 2, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [500, 500, 1000, 1000, 500, 500, 0, 0, 0, 0]) == [1000, 2000, 1000, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0]) == [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 0, 5, 5, 0, 0, 5, 5, 5, 0]) == [5, 10, 10, 5, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == [20, 40, 60, 80, 100, 0, 0, 0, 0, 0]
    assert candidate(nums = [2, 2, 0, 0, 2, 2, 0, 0, 2, 2]) == [4, 4, 4, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 4, 3, 2, 1]
    assert candidate(nums = [1000, 1000, 999, 999, 888, 888, 777, 777]) == [2000, 1998, 1776, 1554, 0, 0, 0, 0]
    assert candidate(nums = [2, 2, 0, 2, 2, 0, 2, 2, 0, 2]) == [4, 4, 4, 2, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 4, 6, 3, 8, 8, 0, 0, 0, 0]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 2, 6, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [3, 3, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0]) == [6, 3, 6, 6, 3, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == [2, 1, 4, 2, 6, 3, 0, 0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 2, 2, 2, 2, 2, 5, 5]) == [10, 5, 4, 4, 2, 10, 0, 0, 0, 0]
    assert candidate(nums = [6, 6, 6, 6, 0, 0, 0, 0, 6, 6]) == [12, 12, 12, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [3, 3, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0, 3, 0, 3]) == [6, 3, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [2000, 2000, 2000, 2000, 2000, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 4, 6, 8, 10, 0, 0, 0, 0, 0]
    assert candidate(nums = [9, 10, 9, 10, 9, 10, 9, 10, 9, 10]) == [9, 10, 9, 10, 9, 10, 9, 10, 9, 10]
    assert candidate(nums = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == [999, 999, 999, 999, 999, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2]) == [4, 2, 4, 2, 4, 2, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 0, 10, 10, 0, 10, 0, 10, 10, 10]) == [10, 20, 10, 20, 10, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate(nums = [1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0]) == [1, 4, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3, 2, 1, 2, 3, 2, 1]
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [18, 18, 18, 18, 18, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 0, 0, 5, 5, 5, 0]) == [10, 10, 5, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 0, 1, 1, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]) == [1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 4, 4, 8, 8, 16, 16, 32]) == [1, 4, 8, 16, 32, 32, 0, 0, 0, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [3, 0, 3, 3, 0, 0, 3, 3, 0, 3]) == [3, 6, 6, 3, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == [2, 2, 1, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [2000, 2000, 2000, 2000, 0, 0, 0, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]) == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000, 1000, 0, 0, 1000, 1000, 1000, 0, 0, 1000]) == [2000, 2000, 1000, 1000, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
    assert candidate(nums = [5, 5, 0, 0, 5, 5, 0, 0, 5, 5]) == [10, 10, 10, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == [2, 2, 2, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0, 0, 0, 0]) == [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0, 0, 0, 0]
    assert candidate(nums = [9, 9, 0, 0, 9, 0, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9]) == [18, 9, 18, 9, 18, 18, 9, 18, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1]) == [1, 4, 2, 2, 1, 4, 2, 2, 4, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40]) == [20, 40, 60, 80, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 1, 2, 2, 0, 3, 3, 0, 4, 4, 0]) == [2, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 0, 0, 0]) == [2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [7, 0, 7, 0, 7, 0, 7, 0, 7, 0]) == [7, 7, 7, 7, 7, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 0, 10, 0, 10, 0, 10, 0, 10]) == [10, 10, 10, 10, 10, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 0, 5, 5, 0, 0, 5, 5]) == [10, 5, 10, 10, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 0, 0, 5, 5, 5, 5]) == [10, 10, 10, 10, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [8, 8, 8, 0, 8, 8, 0, 8, 8, 8]) == [16, 8, 16, 16, 8, 0, 0, 0, 0, 0]
    assert candidate(nums = [7, 7, 7, 7, 0, 0, 0, 0, 7, 7]) == [14, 14, 14, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate(nums = [100, 200, 200, 100, 100, 200, 200, 100]) == [100, 400, 200, 400, 100, 0, 0, 0]
    assert candidate(nums = [5, 5, 0, 5, 5, 5, 0, 0, 5, 5]) == [10, 10, 5, 10, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000, 1000, 0, 500, 500, 0, 250, 250, 0]) == [2000, 1000, 500, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == [2, 4, 2, 6, 8, 8, 0, 0, 0, 0, 0]


