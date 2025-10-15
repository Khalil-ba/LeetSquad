def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 0, 1, -1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 0, 1, -1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 4, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 4, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 0, -1, -2, -3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 0, -1, -2, -3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 3, 5, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 3, 5, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 7, 9, 2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 7, 9, 2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 500000000, 500000000, 500000000, 500000000, 500000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 500000000, 500000000, 500000000, 500000000, 500000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -1000000001, -1000000002, -1000000003, -1000000004, -1000000005]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -1000000001, -1000000002, -1000000003, -1000000004, -1000000005]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15, 12, 14, 16, 18, 17, 19, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15, 12, 14, 16, 18, 17, 19, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 4, 3, 8, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 4, 3, 8, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 2147483646, -2147483647, 2147483645]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 2147483646, -2147483647, 2147483645]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 10, 20, 1, 8, 15, 6, 11]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 10, 20, 1, 8, 15, 6, 11]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, 1, 3, 5, -4, -2, 0, 2, 4, 6, -3, -1, 1, 3, 5, 7]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, 1, 3, 5, -4, -2, 0, 2, 4, 6, -3, -1, 1, 3, 5, 7]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 1073741823, -1073741824, 536870911, -536870912]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 1073741823, -1073741824, 536870911, -536870912]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2147483648, -2147483647, -2147483646, -2147483645, -2147483644, -2147483643, -2147483642, -2147483641]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2147483648, -2147483647, -2147483646, -2147483645, -2147483644, -2147483643, -2147483642, -2147483641]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 2, 2, 3, 1, 2, 3, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 2, 2, 3, 1, 2, 3, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 185: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -500000000, -250000000, -125000000, -62500000, -31250000, -15625000, -7812500, -3906250, -1953125]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -500000000, -250000000, -125000000, -62500000, -31250000, -15625000, -7812500, -3906250, -1953125]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 4, 2, 8, 6, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 4, 2, 8, 6, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 2, 10, 7, 3, 8, 1, 5, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 2, 10, 7, 3, 8, 1, 5, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, -3, -4, 0, 1, 2, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, -3, -4, 0, 1, 2, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 10, 9, 8, 7, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 10, 9, 8, 7, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 8, 7, 3, 4, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 8, 7, 3, 4, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907]) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907]) == 176: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 4, 8, 12, 16, 20]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 4, 8, 12, 16, 20]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2147483648, 2147483647, -2147483647, 2147483646, -2147483646, 2147483645, -2147483645, 2147483644, -2147483644, 2147483643]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2147483648, 2147483647, -2147483647, 2147483646, -2147483646, 2147483645, -2147483645, 2147483644, -2147483644, 2147483643]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 9, 4, 3, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 9, 4, 3, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 4, 5, 6, 7, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 4, 5, 6, 7, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 40, 35, 30, 25, 20, 15, 10, 5, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 40, 35, 30, 25, 20, 15, 10, 5, 0]) == 25: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9]) == 6
    assert candidate(nums = [2147483647, -2147483648, 0, 1, -1]) == 6
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [1, 5, 3, 4, 2]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [1, 3, 2, 3, 1]) == 2
    assert candidate(nums = [1, 2, 3, 0, -1, -2, -3]) == 18
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50]) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 10
    assert candidate(nums = [-5, -4, -3, -2, -1]) == 4
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648]) == 4
    assert candidate(nums = [5, 2, 6, 1]) == 3
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [2, 4, 3, 5, 1]) == 3
    assert candidate(nums = [-5, -4, -3, -2, -1]) == 4
    assert candidate(nums = [1, 5, 3, 7, 9, 2, 4, 6, 8]) == 4
    assert candidate(nums = [2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [50, 40, 30, 20, 10]) == 4
    assert candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35]) == 16
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 500000000, 500000000, 500000000, 500000000, 500000000]) == 0
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 25
    assert candidate(nums = [-1000000000, -1000000001, -1000000002, -1000000003, -1000000004, -1000000005]) == 15
    assert candidate(nums = [1, 4, 2, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15, 12, 14, 16, 18, 17, 19, 20]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 13
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [5, 2, 6, 1, 4, 3, 8, 7]) == 3
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 25
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19
    assert candidate(nums = [2147483647, -2147483648, 2147483646, -2147483647, 2147483645]) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 24
    assert candidate(nums = [1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 12
    assert candidate(nums = [5, 3, 10, 20, 1, 8, 15, 6, 11]) == 7
    assert candidate(nums = [-5, -3, -1, 1, 3, 5, -4, -2, 0, 2, 4, 6, -3, -1, 1, 3, 5, 7]) == 40
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 5, 15, 25, 35, 45]) == 6
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [2147483647, -2147483648, 1073741823, -1073741824, 536870911, -536870912]) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == 22
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5]) == 60
    assert candidate(nums = [-2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647, -2147483648, 2147483647]) == 20
    assert candidate(nums = [-2147483648, -2147483647, -2147483646, -2147483645, -2147483644, -2147483643, -2147483642, -2147483641]) == 28
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19]) == 190
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0]) == 13
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 36
    assert candidate(nums = [3, 1, 2, 2, 2, 3, 1, 2, 3, 1]) == 6
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 185
    assert candidate(nums = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [-1000000000, -500000000, -250000000, -125000000, -62500000, -31250000, -15625000, -7812500, -3906250, -1953125]) == 0
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 36
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 0
    assert candidate(nums = [-1, 1, -1, 1, -1, 1]) == 6
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12]) == 5
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 49
    assert candidate(nums = [1, 5, 3, 4, 2, 8, 6, 7]) == 1
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 100
    assert candidate(nums = [9, 4, 2, 10, 7, 3, 8, 1, 5, 6]) == 11
    assert candidate(nums = [0, -1, -2, -3, -4, 0, 1, 2, 3, 4]) == 10
    assert candidate(nums = [38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]) == 100
    assert candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [3, 1, 2, 4, 5, 10, 9, 8, 7, 6]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 0
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4]) == 6
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 0
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 90
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 49
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) == 40
    assert candidate(nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
    assert candidate(nums = [5, 2, 6, 1, 8, 7, 3, 4, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 20
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907]) == 176
    assert candidate(nums = [9, 18, 27, 36, 45, 4, 8, 12, 16, 20]) == 15
    assert candidate(nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == 6
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [-2147483648, 2147483647, -2147483647, 2147483646, -2147483646, 2147483645, -2147483645, 2147483644, -2147483644, 2147483643]) == 20
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 25
    assert candidate(nums = [5, 2, 6, 1, 9, 4, 3, 7]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 25
    assert candidate(nums = [1, 3, 2, 3, 1, 4, 5, 6, 7, 8]) == 2
    assert candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2]) == 12
    assert candidate(nums = [5, 2, 6, 1, 3, 4]) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 25
    assert candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095]) == 190
    assert candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]) == 2
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 7
    assert candidate(nums = [45, 40, 35, 30, 25, 20, 15, 10, 5, 0]) == 25


