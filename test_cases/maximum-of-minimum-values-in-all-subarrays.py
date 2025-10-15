def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 50, 10]) == [50, 20, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 50, 10]) == [50, 20, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000]) == [1000000000, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000]) == [1000000000, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1]) == [9, 7, 5, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1]) == [9, 7, 5, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == [9, 7, 5, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == [9, 7, 5, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 6, 4, 5, 2]) == [6, 4, 4, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 6, 4, 5, 2]) == [6, 4, 4, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100]) == [100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100]) == [100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4]) == [4, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4]) == [4, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 4, 4, 8, 7, 3, 9, 1, 3, 7]) == [9, 7, 4, 4, 4, 3, 3, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 4, 4, 8, 7, 3, 9, 1, 3, 7]) == [9, 7, 4, 4, 4, 3, 3, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 3, 4, 3, 2, 1, 0]) == [4, 3, 3, 2, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 3, 4, 3, 2, 1, 0]) == [4, 3, 3, 2, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [105, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [105, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == [7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == [7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100, 50]) == [500, 400, 400, 300, 300, 200, 200, 100, 100, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100, 50]) == [500, 400, 400, 300, 300, 200, 200, 100, 100, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [20, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [20, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 4, 4, 3, 3, 2, 2, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 4, 4, 3, 3, 2, 2, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000]) == [1000000000, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000]) == [1000000000, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [3, 2, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 6, 4, 5, 3, 8, 2, 9, 4, 7, 3, 5, 6, 1, 8, 2, 9, 4, 7, 3, 5, 6, 1, 8, 2, 9, 4, 7]) == [9, 5, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 6, 4, 5, 3, 8, 2, 9, 4, 7, 3, 5, 6, 1, 8, 2, 9, 4, 7, 3, 5, 6, 1, 8, 2, 9, 4, 7]) == [9, 5, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 10]) == [30, 25, 20, 20, 15, 10, 10, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 10]) == [30, 25, 20, 20, 15, 10, 10, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [9, 7, 7, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [9, 7, 7, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [50, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [50, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == [100, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == [100, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [20, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [20, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 7, 2, 9, 10, 1, 4, 8]) == [10, 9, 3, 3, 2, 2, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 7, 2, 9, 10, 1, 4, 8]) == [10, 9, 3, 3, 2, 2, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000, 0]) == [1000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000, 0]) == [1000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [9, 7, 7, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [9, 7, 7, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 1, 4, 1, 5, 1, 6, 1]) == [6, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 1, 4, 1, 5, 1, 6, 1]) == [6, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == [50, 40, 40, 30, 30, 20, 20, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == [50, 40, 40, 30, 30, 20, 20, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == [12, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == [12, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 200, 100, 200, 300, 200, 100]) == [300, 200, 200, 100, 100, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 200, 100, 200, 300, 200, 100]) == [300, 200, 200, 100, 100, 100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 5, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 5, 3, 3, 2, 2, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [10, 8, 6, 4, 2, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [10, 8, 6, 4, 2, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 7, 7, 6, 4, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 7, 7, 6, 4, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 50, 10]) == [50, 20, 10, 10]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000]) == [1000000000, 0, 0, 0, 0]
    assert candidate(nums = [9, 7, 5, 3, 1]) == [9, 7, 5, 3, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [1, 3, 5, 7, 9]) == [9, 7, 5, 3, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [3, 1, 6, 4, 5, 2]) == [6, 4, 4, 2, 1, 1]
    assert candidate(nums = [1]) == [1]
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [100, 100, 100, 100]) == [100, 100, 100, 100]
    assert candidate(nums = [0, 1, 2, 4]) == [4, 2, 1, 0]
    assert candidate(nums = [7, 4, 4, 8, 7, 3, 9, 1, 3, 7]) == [9, 7, 4, 4, 4, 3, 3, 1, 1, 1]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 2, 2, 1]
    assert candidate(nums = [5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert candidate(nums = [0, 2, 1, 3, 4, 3, 2, 1, 0]) == [4, 3, 3, 2, 1, 1, 1, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [105, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == [7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]
    assert candidate(nums = [1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100, 50]) == [500, 400, 400, 300, 300, 200, 200, 100, 100, 50]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [20, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 4, 4, 3, 3, 2, 2, 1, 1, 0]
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000]) == [1000000000, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 2, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [3, 1, 6, 4, 5, 3, 8, 2, 9, 4, 7, 3, 5, 6, 1, 8, 2, 9, 4, 7, 3, 5, 6, 1, 8, 2, 9, 4, 7]) == [9, 5, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 20, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 10]) == [30, 25, 20, 20, 15, 10, 10, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [9, 7, 7, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [50, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == [100, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [20, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    assert candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 3, 6, 7, 2, 9, 10, 1, 4, 8]) == [10, 9, 3, 3, 2, 2, 2, 1, 1, 1]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    assert candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000, 0, 1000000000, 0]) == [1000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    assert candidate(nums = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [9, 7, 7, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]
    assert candidate(nums = [5, 1, 3, 1, 4, 1, 5, 1, 6, 1]) == [6, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == [50, 40, 40, 30, 30, 20, 20, 10, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2, 2, 1]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == [12, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]
    assert candidate(nums = [100, 200, 300, 200, 100, 200, 300, 200, 100]) == [300, 200, 200, 100, 100, 100, 100, 100, 100]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 5, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [10, 8, 6, 4, 2, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [10, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15]) == [15, 14, 13, 12, 11, 10, 9, 7, 7, 6, 4, 2, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == [8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == [5, 4, 4, 3, 3, 2, 2, 1, 1, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [4, 3, 3, 2, 2, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 2, 2, 1, 1, 1, 1, 1, 1, 1]


