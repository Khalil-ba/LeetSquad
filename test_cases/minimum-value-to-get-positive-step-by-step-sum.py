def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, 2, -3, 4, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, 2, -3, 4, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, -3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, -3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -100, 100]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -100, 100]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -50, -25, -12, -6, -3, -1]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -50, -25, -12, -6, -3, -1]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 50, -50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 50, -50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -50, -50]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -50, -50]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, -30, 40, -50, 60, -70, 80]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, -30, 40, -50, 60, -70, 80]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, -4, 2, 0, 1, -2, -3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, -4, 2, 0, 1, -2, -3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, -15, 20, -10, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, -15, 20, -10, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, -3, -4, -5, 6]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, -3, -4, -5, 6]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100, 100, -100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100, 100, -100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -150, 60]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -150, 60]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -12, 62, -31, 15, -7, 3, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -12, 62, -31, 15, -7, 3, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 2, -8, 6, -1, 4, -7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 2, -8, 6, -1, 4, -7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -100, 100, -200, 200, -300, 300]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -100, 100, -200, 200, -300, 300]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, -50, 50, -25, 25, -12, 12]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, -50, 50, -25, 25, -12, 12]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == 946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == 946: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -15, 20, -25, 30, -35, 40]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -15, 20, -25, 30, -35, 40]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -100, 100, -100, 100, -100, 100, -100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -100, 100, -100, 100, -100, 100, -100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 50, -25, 25, -12, 12, -6, 6, -3, 3]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 50, -25, 25, -12, 12, -6, 6, -3, 3]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 50, -50, 50, -50, 50]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 50, -50, 50, -50, 50]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, -20, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, -20, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700]) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700]) == 301: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -15, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -15, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -10, 15, -20, 25, -30, 35, -40, 45, -50]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -10, 15, -20, 25, -30, 35, -40, 45, -50]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 10]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 10]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -1, 1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -1, 1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10, -20, 20, -30, 30]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10, -20, 20, -30, 30]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 15]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 15]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, 40, 50, -15]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, 40, 50, -15]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 15, -1, -1, -1, -1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 15, -1, -1, -1, -1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, 10, 0, -10, 20, 0, -10, 0, 20]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, 10, 0, -10, 20, 0, -10, 0, 20]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -20, -30, 100, -10, 20]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -20, -30, 100, -10, 20]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -150]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -150]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 50, -50, 50, -50, 50, -50, 50, -50, 50]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 50, -50, 50, -50, 50, -50, 50, -50, 50]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 100]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 100]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, -10, 20, -15, 5, -5, 10, -10, 15, -20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, -10, 20, -15, 5, -5, 10, -10, 15, -20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, -50, 40, -10, -20, -30, 50]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, -50, 40, -10, -20, -30, 50]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -5, 2, -1, 4, -6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -5, 2, -1, 4, -6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -50, -50, 50, 50]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -50, -50, 50, 50]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, 10, -1, 10, -1, 10, -1, 10, -1, 10, -1, 10, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, 10, -1, 10, -1, 10, -1, 10, -1, 10, -1, 10, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -15, 10, 20, -50, 100]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -15, 10, 20, -50, 100]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 0, -2, 0, -3, 0, -4, 0, -5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 0, -2, 0, -3, 0, -4, 0, -5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, 20, -5, -5, -5, -5]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, 20, -5, -5, -5, -5]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -75, 10, -10, 5, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -75, 10, -10, 5, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, -50, -50, -50, 200]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, -50, -50, -50, 200]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -20, 10, -5, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -20, 10, -5, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 551: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1, 1, -1, 1]) == 2
    assert candidate(nums = [100, 100, 100]) == 1
    assert candidate(nums = [-3, 2, -3, 4, 2]) == 5
    assert candidate(nums = [1, -2, -3]) == 5
    assert candidate(nums = [-1]) == 2
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [100]) == 1
    assert candidate(nums = [-100, 100, -100, 100]) == 101
    assert candidate(nums = [50, 50, 50]) == 1
    assert candidate(nums = [-100, -50, -25, -12, -6, -3, -1]) == 198
    assert candidate(nums = [0, 0, 0]) == 1
    assert candidate(nums = [-1, -2, -3, -4]) == 11
    assert candidate(nums = [-100]) == 101
    assert candidate(nums = [1, 2]) == 1
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 1
    assert candidate(nums = [50, -50, 50, -50]) == 1
    assert candidate(nums = [-50, -50, -50]) == 151
    assert candidate(nums = [-1, 0, 1]) == 2
    assert candidate(nums = [10, 20, 30, 40]) == 1
    assert candidate(nums = [10, 20, -30, 40, -50, 60, -70, 80]) == 21
    assert candidate(nums = [5, -3, -4, 2, 0, 1, -2, -3, 4, 5]) == 5
    assert candidate(nums = [10, -5, -15, 20, -10, 5]) == 11
    assert candidate(nums = [0, -1, -2, -3, -4, -5, 6]) == 16
    assert candidate(nums = [-1, -1, -1, -1, -1, 10]) == 6
    assert candidate(nums = [100, -100, 100, -100, 100, -100]) == 1
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 51
    assert candidate(nums = [0, 0, 0, 0, 0, -1, 1]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, -150, 60]) == 1
    assert candidate(nums = [100, -50, 25, -12, 62, -31, 15, -7, 3, -1]) == 1
    assert candidate(nums = [5, -3, 2, -8, 6, -1, 4, -7]) == 5
    assert candidate(nums = [1, -100, 100, -200, 200, -300, 300]) == 300
    assert candidate(nums = [10, -20, 30, -40, 50, -60]) == 31
    assert candidate(nums = [100, -50, -50, 50, -25, 25, -12, 12]) == 1
    assert candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == 946
    assert candidate(nums = [5, -15, 20, -25, 30, -35, 40]) == 21
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 11
    assert candidate(nums = [1, -100, 100, -100, 100, -100, 100, -100]) == 100
    assert candidate(nums = [-50, 50, -25, 25, -12, 12, -6, 6, -3, 3]) == 51
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 6
    assert candidate(nums = [-10, 20, -30, 40, -50, 60]) == 31
    assert candidate(nums = [-50, 50, -50, 50, -50, 50]) == 51
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 16
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3]) == 4
    assert candidate(nums = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == 1
    assert candidate(nums = [5, 5, 5, 5, -20, 5, 5, 5, 5]) == 1
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700]) == 301
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [5, -10, 15, -20, 25, -30, 35, -40, 45, -50]) == 26
    assert candidate(nums = [10, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 10]) == 41
    assert candidate(nums = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25]) == 1
    assert candidate(nums = [0, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [-10, 0, 10, -20, 20, -30, 30]) == 31
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, 15]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [-10, -20, -30, 40, 50, -15]) == 61
    assert candidate(nums = [0, 0, 0, 0, 0, 0, -1]) == 2
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]) == 7
    assert candidate(nums = [-1, -2, -3, -4, -5, 15, -1, -1, -1, -1]) == 16
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 1
    assert candidate(nums = [-20, 10, 0, -10, 20, 0, -10, 0, 20]) == 21
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 41
    assert candidate(nums = [-50, -20, -30, 100, -10, 20]) == 101
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, -150]) == 1
    assert candidate(nums = [-50, 50, -50, 50, -50, 50, -50, 50, -50, 50]) == 51
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70]) == 31
    assert candidate(nums = [-10, -20, -30, -40, -50, 100]) == 151
    assert candidate(nums = [30, -10, 20, -15, 5, -5, 10, -10, 15, -20]) == 1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 6
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 1
    assert candidate(nums = [10, 20, 30, -50, 40, -10, -20, -30, 50]) == 11
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [3, -5, 2, -1, 4, -6]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3]) == 4
    assert candidate(nums = [-50, -50, -50, 50, 50]) == 151
    assert candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 36
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [10, -1, 10, -1, 10, -1, 10, -1, 10, -1, 10, -1, 10, -1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 10, 20, -50, 100]) == 21
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 151
    assert candidate(nums = [0, -1, 0, -2, 0, -3, 0, -4, 0, -5]) == 16
    assert candidate(nums = [-5, -5, -5, -5, 20, -5, -5, -5, -5]) == 21
    assert candidate(nums = [100, -50, 25, -75, 10, -10, 5, -5]) == 1
    assert candidate(nums = [100, -50, -50, -50, -50, 200]) == 101
    assert candidate(nums = [0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [100, -50, 25, -20, 10, -5, 1]) == 1
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 551
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1]) == 46
    assert candidate(nums = [-5, -4, -3, -2, -1]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 1


