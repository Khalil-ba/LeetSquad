def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 5, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 5, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, -3, 8]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, -3, 8]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91]) == -91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91]) == -91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 1, 100, -3]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 1, 100, -3]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996]) == -999999996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996]) == -999999996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 375: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 1, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, 11]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 1, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, 11]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000, -999999999, 999999999, -999999998, 999999998, -999999997, 999999997, -999999996, 999999996]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000, -999999999, 999999999, -999999998, 999999998, -999999997, 999999997, -999999996, 999999996]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996, -999999995, -999999994, -999999993, -999999992, -999999991]) == -999999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996, -999999995, -999999994, -999999993, -999999992, -999999991]) == -999999991: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, -999999999, 999999998, -999999998, 999999997, -999999997, 999999996, -999999996, 999999995, -999999995]) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, -999999999, 999999998, -999999998, 999999997, -999999997, 999999996, -999999996, 999999995, -999999995]) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000000, 600000000, 700000000, 800000000, 900000000, 1000000000, 1100000000, 1200000000, 1300000000, 1400000000]) == 9500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000000, 600000000, 700000000, 800000000, 900000000, 1000000000, 1100000000, 1200000000, 1300000000, 1400000000]) == 9500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609]) == 23248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609]) == 23248: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 4179
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 4179: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 55000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 55000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 289: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 5, 6, 8, 10, 13, 16, 20, 25]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 5, 6, 8, 10, 13, 16, 20, 25]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 11, 20, 30, 31, 40, 50, 51, 60]) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 11, 20, 30, 31, 40, 50, 51, 60]) == 304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 16384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 16384: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996]) == -999999996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996]) == -999999996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000, -6000000000, -7000000000, -8000000000, -9000000000, -10000000000]) == -1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000, -6000000000, -7000000000, -8000000000, -9000000000, -10000000000]) == -1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 0, 1000000000, -1000000000, 0, 1000000000, -1000000000, 0, 1000000000, -1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 0, 1000000000, -1000000000, 0, 1000000000, -1000000000, 0, 1000000000, -1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 50, 55, 60, 65, 70, 75, 80]) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 50, 55, 60, 65, 70, 75, 80]) == 615: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 1045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 1045: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 8, 8, 8, 8, 7, 6, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 8, 8, 8, 8, 7, 6, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 21, 2, 32, 3, 43, 4, 54, 5, 65, 6, 76, 7, 87, 8, 98, 9, 109, 10]) == 595
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 21, 2, 32, 3, 43, 4, 54, 5, 65, 6, 76, 7, 87, 8, 98, 9, 109, 10]) == 595: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [40, 35, 30, 25, 20, 15, 10, 5, 1, -5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [40, 35, 30, 25, 20, 15, 10, 5, 1, -5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 2310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 2310: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 150, 250, 350, 450, 550]) == 2050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 150, 250, 350, 450, 550]) == 2050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997, 5, -999999996]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997, 5, -999999996]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 524288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 524288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 26, 24, 29, 27, 30, 25]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 26, 24, 29, 27, 30, 25]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 11, 2, 12, 3, 13, 4, 14, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 11, 2, 12, 3, 13, 4, 14, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 5, 10, 15, 20, 25, 30, 35, 40]) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 5, 10, 15, 20, 25, 30, 35, 40]) == 183: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5]) == 17: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-2, -1]) == -1
    assert candidate(nums = [3, 3, 5, 6]) == 14
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 115
    assert candidate(nums = [1, 2, 3, 5, 8, 13]) == 32
    assert candidate(nums = [-1, 0, 1, 0, -1]) == 1
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000
    assert candidate(nums = [10, 20, 30, 40, 50]) == 150
    assert candidate(nums = [-5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [5, -1, -3, 8]) == 13
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91]) == -91
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 231
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 11
    assert candidate(nums = [5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [-10, -20, -30, -40, -50]) == -10
    assert candidate(nums = [10, -5, 1, 100, -3]) == 110
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 1000000000
    assert candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996]) == -999999996
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5
    assert candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 29
    assert candidate(nums = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]) == 100
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 256
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 375
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [1, 2, 0, 3, 1, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, 11]) == 19
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 225
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 18
    assert candidate(nums = [33, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7]) == 33
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
    assert candidate(nums = [-1000000000, 1000000000, -999999999, 999999999, -999999998, 999999998, -999999997, 999999997, -999999996, 999999996]) == 1000000000
    assert candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996, -999999995, -999999994, -999999993, -999999992, -999999991]) == -999999991
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
    assert candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]) == 175
    assert candidate(nums = [999999999, -999999999, 999999998, -999999998, 999999997, -999999997, 999999996, -999999996, 999999995, -999999995]) == 999999999
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 300
    assert candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 150
    assert candidate(nums = [500000000, 600000000, 700000000, 800000000, 900000000, 1000000000, 1100000000, 1200000000, 1300000000, 1400000000]) == 9500000000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 275
    assert candidate(nums = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609]) == 23248
    assert candidate(nums = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25]) == 150
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 4179
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 150
    assert candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]) == 165
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 220
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 150
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 1000000000
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 10
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 100
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 1000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]) == 115
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 55000000000
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
    assert candidate(nums = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 289
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 325
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000]) == 1000000000
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 64
    assert candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 150
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 8
    assert candidate(nums = [1, 4, 5, 6, 8, 10, 13, 16, 20, 25]) == 108
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 231
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 10
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 15
    assert candidate(nums = [1, 10, 11, 20, 30, 31, 40, 50, 51, 60]) == 304
    assert candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 16384
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == 19
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996]) == -999999996
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000000
    assert candidate(nums = [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000, -6000000000, -7000000000, -8000000000, -9000000000, -10000000000]) == -1000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1000
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 150
    assert candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -5
    assert candidate(nums = [-1000000000, 0, 1000000000, -1000000000, 0, 1000000000, -1000000000, 0, 1000000000, -1000000000]) == 1000000000
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 15
    assert candidate(nums = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 109
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 50, 55, 60, 65, 70, 75, 80]) == 615
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 11
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 1000000000
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 1045
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1000000000
    assert candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5]) == 5
    assert candidate(nums = [10, 9, 8, 8, 8, 8, 8, 7, 6, 5]) == 10
    assert candidate(nums = [10, 1, 21, 2, 32, 3, 43, 4, 54, 5, 65, 6, 76, 7, 87, 8, 98, 9, 109, 10]) == 595
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 39
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 10
    assert candidate(nums = [0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5
    assert candidate(nums = [40, 35, 30, 25, 20, 15, 10, 5, 1, -5]) == 40
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 2310
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 400
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 150, 250, 350, 450, 550]) == 2050
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 30
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == -1
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11
    assert candidate(nums = [1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997, 5, -999999996]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000]) == 1000000000
    assert candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -5
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 1540
    assert candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 524288
    assert candidate(nums = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 26, 24, 29, 27, 30, 25]) == 165
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 100
    assert candidate(nums = [10, 1, 11, 2, 12, 3, 13, 4, 14, 5]) == 18
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(nums = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13]) == 36
    assert candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == -100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 10
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 64
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 6
    assert candidate(nums = [5, 3, 5, 10, 15, 20, 25, 30, 35, 40]) == 183
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5]) == 17


