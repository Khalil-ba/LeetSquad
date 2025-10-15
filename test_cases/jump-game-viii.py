def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],costs = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],costs = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2],costs = [1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2],costs = [1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 25],costs = [1, 2, 3, 4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 25],costs = [1, 2, 3, 4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],costs = [10, 10, 10, 10, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],costs = [10, 10, 10, 10, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],costs = [2, 4, 6, 8, 10]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],costs = [2, 4, 6, 8, 10]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],costs = [10, 9, 8, 7, 6]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],costs = [10, 9, 8, 7, 6]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 4, 4, 1],costs = [3, 7, 6, 4, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 4, 4, 1],costs = [3, 7, 6, 4, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],costs = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],costs = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 7, 10, 12],costs = [1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 7, 10, 12],costs = [1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],costs = [2, 2, 2, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],costs = [2, 2, 2, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7],costs = [2, 4, 6, 8]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7],costs = [2, 4, 6, 8]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1],costs = [1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1],costs = [1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1],costs = [1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1],costs = [1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6],costs = [5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6],costs = [5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],costs = [10, 9, 8, 7, 6]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],costs = [10, 9, 8, 7, 6]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 1, 2, 3, 4],costs = [2, 2, 2, 2, 2, 2, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 1, 2, 3, 4],costs = [2, 2, 2, 2, 2, 2, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 3, 12, 25, 8],costs = [3, 7, 1, 4, 6, 9, 2, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 3, 12, 25, 8],costs = [3, 7, 1, 4, 6, 9, 2, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9],costs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9],costs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 3, 2, 1, 6, 4, 3, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 3, 2, 1, 6, 4, 3, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],costs = [1, 10, 100, 1000, 10000, 100000, 1, 10, 100, 1]) == 111222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],costs = [1, 10, 100, 1000, 10000, 100000, 1, 10, 100, 1]) == 111222: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1],costs = [1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1],costs = [1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 2, 6, 7, 1, 8, 9],costs = [10, 8, 5, 4, 7, 3, 2, 6, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 2, 6, 7, 1, 8, 9],costs = [10, 8, 5, 4, 7, 3, 2, 6, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 5, 6, 2, 8, 1],costs = [2, 3, 1, 4, 5, 6, 1, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 5, 6, 2, 8, 1],costs = [2, 3, 1, 4, 5, 6, 1, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50],costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50],costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40],costs = [5, 10, 7, 15, 12, 20, 17, 25, 22, 30, 27, 35]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40],costs = [5, 10, 7, 15, 12, 20, 17, 25, 22, 30, 27, 35]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 3, 5, 3, 1, 4],costs = [1, 2, 3, 4, 5, 6, 7]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 3, 5, 3, 1, 4],costs = [1, 2, 3, 4, 5, 6, 7]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 1, 4, 5, 3, 6, 7, 2, 8],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 1, 4, 5, 3, 6, 7, 2, 8],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 8, 4, 2, 7],costs = [10, 20, 30, 40, 50, 60, 70]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 8, 4, 2, 7],costs = [10, 20, 30, 40, 50, 60, 70]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 6, 3, 8, 2, 9, 1, 4, 7],costs = [3, 5, 2, 1, 4, 7, 6, 8, 9, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 6, 3, 8, 2, 9, 1, 4, 7],costs = [3, 5, 2, 1, 4, 7, 6, 8, 9, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 3, 7, 6, 9, 8, 10, 11, 12],costs = [1, 2, 1, 3, 2, 4, 3, 1, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 3, 7, 6, 9, 8, 10, 11, 12],costs = [1, 2, 1, 3, 2, 4, 3, 1, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2, 5, 6, 1, 4, 7],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2, 5, 6, 1, 4, 7],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],costs = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],costs = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 3, 2, 1],costs = [10, 20, 30, 40, 50, 60, 70]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 3, 2, 1],costs = [10, 20, 30, 40, 50, 60, 70]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5, 1, 2, 3],costs = [3, 5, 2, 4, 1, 2, 3, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5, 1, 2, 3],costs = [3, 5, 2, 4, 1, 2, 3, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 9, 0],costs = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 9, 0],costs = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10],costs = [1, 10, 5, 7, 3, 2, 4, 6, 8, 9]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10],costs = [1, 10, 5, 7, 3, 2, 4, 6, 8, 9]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],costs = [15, 13, 11, 9, 7, 5, 3, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],costs = [15, 13, 11, 9, 7, 5, 3, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3],costs = [3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3],costs = [3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10],costs = [1, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10],costs = [1, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 6, 1, 4, 7],costs = [10, 5, 3, 1, 8, 2, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 6, 1, 4, 7],costs = [10, 5, 3, 1, 8, 2, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4, 3, 2, 1, 2],costs = [5, 4, 3, 2, 1, 6, 7, 8]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4, 3, 2, 1, 2],costs = [5, 4, 3, 2, 1, 6, 7, 8]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10],costs = [2, 3, 5, 1, 7, 8, 4, 6, 9, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10],costs = [2, 3, 5, 1, 7, 8, 4, 6, 9, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5],costs = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5],costs = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 6, 3],costs = [1, 2, 5, 3, 4, 6, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 6, 3],costs = [1, 2, 5, 3, 4, 6, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],costs = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],costs = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 6, 2, 7, 4, 8, 3, 9],costs = [5, 3, 8, 6, 2, 4, 7, 1, 9, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 6, 2, 7, 4, 8, 3, 9],costs = [5, 3, 8, 6, 2, 4, 7, 1, 9, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4],costs = [3, 7, 6, 4, 2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4],costs = [3, 7, 6, 4, 2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 2, 5, 3, 4, 8, 7, 9, 10],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 2, 5, 3, 4, 8, 7, 9, 10],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 6, 5],costs = [10, 20, 15, 25, 30, 35, 40]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 6, 5],costs = [10, 20, 15, 25, 30, 35, 40]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8],costs = [2, 3, 1, 5, 4, 2, 1, 3]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8],costs = [2, 3, 1, 5, 4, 2, 1, 3]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],costs = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],costs = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 10, 9, 8, 10, 9],costs = [1, 2, 3, 4, 5, 6, 7, 8]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 10, 9, 8, 10, 9],costs = [1, 2, 3, 4, 5, 6, 7, 8]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],costs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],costs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 10, 8, 10, 7, 10, 6, 10, 5, 10, 4, 10, 3, 10, 2, 10, 1, 10],costs = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 10, 8, 10, 7, 10, 6, 10, 5, 10, 4, 10, 3, 10, 2, 10, 1, 10],costs = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8],costs = [1, 2, 3, 4, 5, 6, 7]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8],costs = [1, 2, 3, 4, 5, 6, 7]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 4, 4, 1, 5, 3],costs = [3, 7, 6, 4, 2, 8, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 4, 4, 1, 5, 3],costs = [3, 7, 6, 4, 2, 8, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 7, 9, 2, 10],costs = [2, 5, 1, 4, 3, 6, 8, 7]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 7, 9, 2, 10],costs = [2, 5, 1, 4, 3, 6, 8, 7]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 1, 2, 3, 1, 2, 3],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 1, 2, 3, 1, 2, 3],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3],costs = [1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3],costs = [1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 4, 6, 2, 1, 3, 5, 7, 9],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 4, 6, 2, 1, 3, 5, 7, 9],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 5, 6, 4, 7],costs = [2, 3, 1, 4, 2, 5, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 5, 6, 4, 7],costs = [2, 3, 1, 4, 2, 5, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 5, 1, 5, 2, 5, 1],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 5, 1, 5, 2, 5, 1],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],costs = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],costs = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 7, 4, 8, 2, 9, 6, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 7, 4, 8, 2, 9, 6, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 9, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 9, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 4, 1, 5, 6, 4, 3, 7],costs = [10, 5, 15, 20, 25, 30, 35, 40, 45]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 4, 1, 5, 6, 4, 3, 7],costs = [10, 5, 15, 20, 25, 30, 35, 40, 45]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 1, 4, 7, 6],costs = [4, 3, 5, 2, 1, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 1, 4, 7, 6],costs = [4, 3, 5, 2, 1, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],costs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],costs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],costs = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],costs = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 52: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1],costs = [1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [0, 1, 2],costs = [1, 1, 1]) == 2
    assert candidate(nums = [10, 5, 15, 20, 25],costs = [1, 2, 3, 4, 5]) == 12
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [1, 1, 1, 1, 1],costs = [10, 10, 10, 10, 10]) == 40
    assert candidate(nums = [1, 3, 5, 7, 9],costs = [2, 4, 6, 8, 10]) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [1, 3, 5, 7, 9],costs = [10, 9, 8, 7, 6]) == 30
    assert candidate(nums = [3, 2, 4, 4, 1],costs = [3, 7, 6, 4, 2]) == 8
    assert candidate(nums = [5, 5, 5, 5, 5],costs = [1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [10, 5, 7, 10, 12],costs = [1, 2, 3, 4, 5]) == 9
    assert candidate(nums = [1, 3, 5, 7, 9],costs = [2, 2, 2, 2, 2]) == 8
    assert candidate(nums = [1, 3, 5, 7],costs = [2, 4, 6, 8]) == 18
    assert candidate(nums = [1, 2, 1, 2, 1],costs = [1, 2, 1, 2, 1]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [1, 2, 3, 2, 1],costs = [1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6],costs = [5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [5, 4, 3, 2, 1],costs = [10, 9, 8, 7, 6]) == 30
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(nums = [5, 6, 7, 8, 1, 2, 3, 4],costs = [2, 2, 2, 2, 2, 2, 2, 2]) == 8
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(nums = [10, 5, 15, 20, 3, 12, 25, 8],costs = [3, 7, 1, 4, 6, 9, 2, 5]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9],costs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 34
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8]) == 23
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 135
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [1, 3, 2, 5, 3, 2, 1, 6, 4, 3, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 44
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],costs = [1, 10, 100, 1000, 10000, 100000, 1, 10, 100, 1]) == 111222
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1],costs = [1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 19
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11
    assert candidate(nums = [3, 5, 4, 2, 6, 7, 1, 8, 9],costs = [10, 8, 5, 4, 7, 3, 2, 6, 1]) == 13
    assert candidate(nums = [5, 3, 4, 5, 6, 2, 8, 1],costs = [2, 3, 1, 4, 5, 6, 1, 2]) == 11
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50],costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 55
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [10, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40],costs = [5, 10, 7, 15, 12, 20, 17, 25, 22, 30, 27, 35]) == 135
    assert candidate(nums = [3, 2, 3, 5, 3, 1, 4],costs = [1, 2, 3, 4, 5, 6, 7]) == 15
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 22
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [0, 2, 3, 1, 4, 5, 3, 6, 7, 2, 8],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 38
    assert candidate(nums = [1, 5, 3, 8, 4, 2, 7],costs = [10, 20, 30, 40, 50, 60, 70]) == 180
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 7
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 43
    assert candidate(nums = [10, 5, 6, 3, 8, 2, 9, 1, 4, 7],costs = [3, 5, 2, 1, 4, 7, 6, 8, 9, 10]) == 40
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [1, 4, 3, 7, 6, 9, 8, 10, 11, 12],costs = [1, 2, 1, 3, 2, 4, 3, 1, 2, 1]) == 13
    assert candidate(nums = [5, 1, 4, 3, 2, 5, 6, 1, 4, 7],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1],costs = [1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 3, 5, 4, 3, 2, 1],costs = [10, 20, 30, 40, 50, 60, 70]) == 150
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [3, 2, 1, 4, 5, 1, 2, 3],costs = [3, 5, 2, 4, 1, 2, 3, 6]) == 15
    assert candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 9, 0],costs = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10],costs = [1, 10, 5, 7, 3, 2, 4, 6, 8, 9]) == 39
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],costs = [15, 13, 11, 9, 7, 5, 3, 1]) == 49
    assert candidate(nums = [3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3],costs = [3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4]) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 85
    assert candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10],costs = [1, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [3, 5, 2, 6, 1, 4, 7],costs = [10, 5, 3, 1, 8, 2, 6]) == 10
    assert candidate(nums = [2, 1, 3, 4, 3, 2, 1, 2],costs = [5, 4, 3, 2, 1, 6, 7, 8]) == 17
    assert candidate(nums = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]) == 74
    assert candidate(nums = [3, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
    assert candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10],costs = [2, 3, 5, 1, 7, 8, 4, 6, 9, 1]) == 28
    assert candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 34
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5],costs = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 31
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 3],costs = [1, 2, 5, 3, 4, 6, 2]) == 11
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],costs = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],costs = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 5, 3, 6, 2, 7, 4, 8, 3, 9],costs = [5, 3, 8, 6, 2, 4, 7, 1, 9, 10]) == 24
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [5, 2, 3, 1, 4],costs = [3, 7, 6, 4, 2]) == 13
    assert candidate(nums = [1, 6, 2, 5, 3, 4, 8, 7, 9, 10],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 5],costs = [10, 20, 15, 25, 30, 35, 40]) == 120
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 450
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8],costs = [2, 3, 1, 5, 4, 2, 1, 3]) == 14
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],costs = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 81
    assert candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9],costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [10, 9, 8, 10, 9, 8, 10, 9],costs = [1, 2, 3, 4, 5, 6, 7, 8]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],costs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 105
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [10, 9, 10, 8, 10, 7, 10, 6, 10, 5, 10, 4, 10, 3, 10, 2, 10, 1, 10],costs = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 18
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8],costs = [1, 2, 3, 4, 5, 6, 7]) == 27
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [3, 2, 4, 4, 1, 5, 3],costs = [3, 7, 6, 4, 2, 8, 1]) == 17
    assert candidate(nums = [5, 3, 8, 6, 7, 9, 2, 10],costs = [2, 5, 1, 4, 3, 6, 8, 7]) == 14
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [2, 1, 3, 1, 2, 3, 1, 2, 3],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 10
    assert candidate(nums = [3, 3, 3, 3, 3],costs = [1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [8, 10, 4, 6, 2, 1, 3, 5, 7, 9],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
    assert candidate(nums = [3, 5, 2, 5, 6, 4, 7],costs = [2, 3, 1, 4, 2, 5, 3]) == 10
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],costs = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 15
    assert candidate(nums = [1, 5, 2, 5, 1, 5, 2, 5, 1],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 280
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 71
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],costs = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1]) == 91
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [1, 5, 3, 7, 4, 8, 2, 9, 6, 10],costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 9, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 39
    assert candidate(nums = [3, 2, 4, 1, 5, 6, 4, 3, 7],costs = [10, 5, 15, 20, 25, 30, 35, 40, 45]) == 115
    assert candidate(nums = [3, 5, 2, 1, 4, 7, 6],costs = [4, 3, 5, 2, 1, 3, 4]) == 10
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],costs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 36
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],costs = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 220
    assert candidate(nums = [5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 52


