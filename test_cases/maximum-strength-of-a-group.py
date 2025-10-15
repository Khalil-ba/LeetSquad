def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9]) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9]) == -9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-4, -5, -4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-4, -5, -4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 4]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 4]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, 0, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, 0, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 6227020800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 6227020800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 0, -10, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 0, -10, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 4]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 4]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 3125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 3125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, 0, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, 0, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -1, -2, -3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -1, -2, -3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]) == 6227020800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]) == 6227020800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, -5, 2, 5, -9]) == 1350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, -5, 2, 5, -9]) == 1350: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3]) == 10973491200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3]) == 10973491200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6]) == 1097349120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6]) == 1097349120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, -2, -5, 0, 1, 4, -6]) == 2520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, -2, -5, 0, 1, 4, -6]) == 2520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 531441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 531441: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, 9, 0, -1, 1, -2, 2]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, 9, 0, -1, 1, -2, 2]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 223092870
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 223092870: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, -5, 2, 5, -9, 7]) == 9450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, -5, 2, 5, -9, 7]) == 9450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1220703125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1220703125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, -9]) == 1632960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, -9]) == 1632960: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 2, -2, 3, -3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 2, -2, 3, -3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, -1, -3, -5, -7, -9]) == 893025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, -1, -3, -5, -7, -9]) == 893025: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -3, -5, -7, -9]) == 945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -3, -5, -7, -9]) == 945: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]) == 21772800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]) == 21772800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-8, -6, -4, -2, 0, 2, 4, 6, 8]) == 147456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-8, -6, -4, -2, 0, 2, 4, 6, 8]) == 147456: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 131681894400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 131681894400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 2177280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 2177280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -8, 9, -2, 3, 0, 4, -5, 6, -1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -8, 9, -2, 3, 0, 4, -5, 6, -1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2]) == 725760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2]) == 725760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -9, 8, -8, 7, -7]) == 36288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -9, 8, -8, 7, -7]) == 36288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 14400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 14400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -3, -3, -3, -3, -3, -3, -3, -3]) == 6561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -3, -3, -3, -3, -3, -3, -3, -3]) == 6561: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4]) == 576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4]) == 576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, 0, -5, 2, 5, -9, 0, 4, -2, 6, -8, 7]) == 3628800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, 0, -5, 2, 5, -9, 0, 4, -2, 6, -8, 7]) == 3628800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 1, -1, 2, -2, 3, -3, 4]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 1, -1, 2, -2, 3, -3, 4]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 131681894400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 131681894400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 518400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 518400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7]) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7]) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 2520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 2520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8]) == 101606400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8]) == 101606400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 0, 0, 0, 0, -2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 0, 0, 0, 0, -2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, -5, 2, 5, -9, 7, -8]) == 75600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, -5, 2, 5, -9, 7, -8]) == 75600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2177280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2177280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3]) == 1594323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3]) == 1594323: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3]) == 2177280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3]) == 2177280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 0, -9, 0, 9, -9, 9, -9, 9]) == 531441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 0, -9, 0, 9, -9, 9, -9, 9]) == 531441: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -5, 0, 2, 4, 6, 8, 10]) == 57600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -5, 0, 2, 4, 6, 8, 10]) == 57600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4]) == 8709120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4]) == 8709120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, 0, 5, -2, 4, -6]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, 0, 5, -2, 4, -6]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]) == 531441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]) == 531441: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, -6, 8, -10, 12, -14, 16, -18]) == 185794560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, -6, 8, -10, 12, -14, 16, -18]) == 185794560: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -3, -4, 0, 0, 0, 0, 0, 0]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -3, -4, 0, 0, 0, 0, 0, 0]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == 2177280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == 2177280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7]) == 3628800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7]) == 3628800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == 14400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == 14400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, 3, -2, 0, 4, -3]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, 3, -2, 0, 4, -3]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3]) == 531441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3]) == 531441: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 14400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 14400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 131681894400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 131681894400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8]) == 609638400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8]) == 609638400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1594323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1594323: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -3, 4, -5, 6, -7, 8, -9, 1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -3, 4, -5, 6, -7, 8, -9, 1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -3, -4, -5, -6, -7, -8, -9]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -3, -4, -5, -6, -7, -8, -9]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3]) == 3657830400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3]) == 3657830400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -3, -5, 0, 0, 0, 0, 0, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -3, -5, 0, 0, 0, 0, 0, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, -1, 0]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, -1, 0]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, 8, -7, 6, -5, 4, -3, 2, -1]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, 8, -7, 6, -5, 4, -3, 2, -1]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == 8709120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == 8709120: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == 36
    assert candidate(nums = [-9]) == -9
    assert candidate(nums = [0, 0, 0, 1, -1]) == 1
    assert candidate(nums = [-4, -5, -4]) == 20
    assert candidate(nums = [0, 2, 3, 4]) == 24
    assert candidate(nums = [0, 1, -1]) == 1
    assert candidate(nums = [-1]) == -1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 362880
    assert candidate(nums = [-3, 0, 3]) == 3
    assert candidate(nums = [9]) == 9
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, -1, 1, -1]) == 1
    assert candidate(nums = [1, -1]) == 1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 6227020800
    assert candidate(nums = [10, 0, -10, 0]) == 10
    assert candidate(nums = [1, 2, 0, 3, 4]) == 24
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 120
    assert candidate(nums = [5, 5, 5, 5, 5]) == 3125
    assert candidate(nums = [1, 2, 3, 4, 5]) == 120
    assert candidate(nums = [0, 1, -1, 2, -2]) == 4
    assert candidate(nums = [0, 0, 0]) == 0
    assert candidate(nums = [-1, -1, 0, 1, 1]) == 1
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9]) == 362880
    assert candidate(nums = [2, 3, -1, -2, -3]) == 36
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [-1, -2, -3, -4]) == 24
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]) == 6227020800
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1]) == 362880
    assert candidate(nums = [3, -1, -5, 2, 5, -9]) == 1350
    assert candidate(nums = [-1, 1, 0]) == 1
    assert candidate(nums = [-1, 0, 1]) == 1
    assert candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3]) == 10973491200
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == 362880
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -8, -7, -6]) == 1097349120
    assert candidate(nums = [7, 3, -2, -5, 0, 1, 4, -6]) == 2520
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 531441
    assert candidate(nums = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]) == 4096
    assert candidate(nums = [-9, 9, 0, -1, 1, -2, 2]) == 324
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 223092870
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [3, -1, -5, 2, 5, -9, 7]) == 9450
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1220703125
    assert candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, -9]) == 1632960
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(nums = [1, -2, 3, -4, 5, -6]) == 360
    assert candidate(nums = [0, 1, -1, 2, -2, 3]) == 12
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1]) == 362880
    assert candidate(nums = [0, -1, 2, -2, 3, -3]) == 36
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 36
    assert candidate(nums = [-1, 0, 1]) == 1
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [9, 7, 5, 3, 1, -1, -3, -5, -7, -9]) == 893025
    assert candidate(nums = [-1, -3, -5, -7, -9]) == 945
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]) == 21772800
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [-8, -6, -4, -2, 0, 2, 4, 6, 8]) == 147456
    assert candidate(nums = [0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 131681894400
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 2177280
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [7, -8, 9, -2, 3, 0, 4, -5, 6, -1]) == 362880
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2]) == 725760
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [9, -9, 8, -8, 7, -7]) == 36288
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 14400
    assert candidate(nums = [-3, -3, -3, -3, -3, -3, -3, -3, -3]) == 6561
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362880
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4]) == 576
    assert candidate(nums = [3, -1, 0, -5, 2, 5, -9, 0, 4, -2, 6, -8, 7]) == 3628800
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 1, -1, 2, -2, 3, -3, 4]) == 144
    assert candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 131681894400
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 518400
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 36
    assert candidate(nums = [-5, 0, 5]) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 120
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7]) == 5040
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 2520
    assert candidate(nums = [-2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8]) == 101606400
    assert candidate(nums = [-1, 0, 0, 0, 0, 0, -2]) == 2
    assert candidate(nums = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [3, -1, -5, 2, 5, -9, 7, -8]) == 75600
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2177280
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8192
    assert candidate(nums = [3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3]) == 1594323
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0]) == 1
    assert candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3]) == 2177280
    assert candidate(nums = [9, 0, -9, 0, 9, -9, 9, -9, 9]) == 531441
    assert candidate(nums = [-3, -5, 0, 2, 4, 6, 8, 10]) == 57600
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4]) == 8709120
    assert candidate(nums = [3, -1, 0, 5, -2, 4, -6]) == 720
    assert candidate(nums = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]) == 531441
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [2, 4, -6, 8, -10, 12, -14, 16, -18]) == 185794560
    assert candidate(nums = [-2, -3, -4, 0, 0, 0, 0, 0, 0]) == 12
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == 2177280
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [-1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7]) == 3628800
    assert candidate(nums = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == 14400
    assert candidate(nums = [5, -1, 3, -2, 0, 4, -3]) == 360
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362880
    assert candidate(nums = [-3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3, 3, -3]) == 531441
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 14400
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 362880
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 131681894400
    assert candidate(nums = [5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8]) == 609638400
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 362880
    assert candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1]) == 362880
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1594323
    assert candidate(nums = [2, -3, 4, -5, 6, -7, 8, -9, 1]) == 362880
    assert candidate(nums = [-2, -3, -4, -5, -6, -7, -8, -9]) == 362880
    assert candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3]) == 3657830400
    assert candidate(nums = [-2, -3, -5, 0, 0, 0, 0, 0, 0]) == 15
    assert candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, -1, 0]) == 362880
    assert candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3]) == 36
    assert candidate(nums = [-9, 8, -7, 6, -5, 4, -3, 2, -1]) == 362880
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == 8709120


