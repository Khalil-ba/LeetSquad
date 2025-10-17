def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]) == 1654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]) == 1654: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 7, 4, 5, 5, 5, 4]) == 2886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 7, 4, 5, 5, 5, 4]) == 2886: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 8]) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 8]) == 167: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 76, 66, 18, 49, 79, 11, 31, 2, 83, 45, 12, 50, 88, 67, 34, 73, 39, 100, 87, 30, 6, 41, 72, 84, 17, 29, 63, 52, 75, 58, 92, 37, 35, 61, 43, 89, 64, 55, 19, 32, 62, 57, 90, 91, 33, 44, 27, 3, 76, 65, 68, 42, 8, 54, 60, 10, 80, 70, 12, 3, 5, 82, 46, 30, 81, 13, 26, 93, 14, 20, 78, 86, 25, 56, 1, 36, 59, 74, 15, 95, 16, 4, 7, 22, 69, 51, 38, 85, 23, 40, 94, 48, 6, 97, 24, 53, 9, 96, 21, 47, 77, 99, 31, 28, 45, 32]) == 35112384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 76, 66, 18, 49, 79, 11, 31, 2, 83, 45, 12, 50, 88, 67, 34, 73, 39, 100, 87, 30, 6, 41, 72, 84, 17, 29, 63, 52, 75, 58, 92, 37, 35, 61, 43, 89, 64, 55, 19, 32, 62, 57, 90, 91, 33, 44, 27, 3, 76, 65, 68, 42, 8, 54, 60, 10, 80, 70, 12, 3, 5, 82, 46, 30, 81, 13, 26, 93, 14, 20, 78, 86, 25, 56, 1, 36, 59, 74, 15, 95, 16, 4, 7, 22, 69, 51, 38, 85, 23, 40, 94, 48, 6, 97, 24, 53, 9, 96, 21, 47, 77, 99, 31, 28, 45, 32]) == 35112384: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10]) == 2110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10]) == 2110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 76, 64, 21, 97, 60]) == 1086136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 76, 64, 21, 97, 60]) == 1086136: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 3, 8, 3, 8]) == 968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 3, 8, 3, 8]) == 968: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 7, 3]) == 2107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 7, 3]) == 2107: {e}')
    
    total += 1
    try:
        result = candidate(nums = [35, 16, 83, 87, 52, 15, 24, 91, 36, 80, 59, 27, 9, 81, 33, 17, 5, 74, 40, 85, 23, 47, 89, 69]) == 6802248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [35, 16, 83, 87, 52, 15, 24, 91, 36, 80, 59, 27, 9, 81, 33, 17, 5, 74, 40, 85, 23, 47, 89, 69]) == 6802248: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 5700600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 5700600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 10120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 10120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 6, 2, 3, 7, 4, 1, 9]) == 1704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 6, 2, 3, 7, 4, 1, 9]) == 1704: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 32339900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 32339900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 99]) == 474000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 99]) == 474000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 0, 3, 0, 1]) == 23783
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 0, 3, 0, 1]) == 23783: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2427280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2427280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 1010101200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 1010101200000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]) == 15717
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]) == 15717: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11]) == 1510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11]) == 1510: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1, 2, 5, 10, 20, 30, 40, 50]) == 309374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1, 2, 5, 10, 20, 30, 40, 50]) == 309374: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 14636200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 14636200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 243660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 243660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 43888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 43888: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4830: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 13150200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 13150200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 2010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 2010: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 75, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 2737551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 75, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 2737551: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3050100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3050100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 13680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 13680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 15284100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 15284100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5]) == 2906611
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5]) == 2906611: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 741
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 741: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40, 60, 70, 80, 90, 10]) == 1428550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40, 60, 70, 80, 90, 10]) == 1428550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 40, 60, 10, 80, 30, 90]) == 1779840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 40, 60, 10, 80, 30, 90]) == 1779840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 72420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 72420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]) == 98801200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]) == 98801200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 20, 80, 15, 85, 10, 90, 5, 95, 40, 60, 35, 65, 30, 70, 45, 55, 2]) == 4854150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 20, 80, 15, 85, 10, 90, 5, 95, 40, 60, 35, 65, 30, 70, 45, 55, 2]) == 4854150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [82, 9, 60, 27, 69, 64, 53, 80, 74, 97, 22, 5, 35, 46, 91, 16, 51, 86, 58, 3, 53, 29, 37, 24, 36, 72, 39, 68, 55, 76, 59, 79, 85, 43, 87, 66, 89, 25, 47, 20, 90, 83, 33, 38, 92, 48, 57, 93, 95, 70, 56, 88, 45, 26, 75, 98, 65, 4, 42, 77, 18, 23, 31, 19, 94, 49, 32, 21, 100, 30, 17, 28, 40, 11, 63, 67, 7, 62, 13, 73, 12, 14, 78, 2, 54, 71, 15, 6, 41, 81, 52, 96, 34, 44, 99, 84, 50, 8, 39]) == 35359128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [82, 9, 60, 27, 69, 64, 53, 80, 74, 97, 22, 5, 35, 46, 91, 16, 51, 86, 58, 3, 53, 29, 37, 24, 36, 72, 39, 68, 55, 76, 59, 79, 85, 43, 87, 66, 89, 25, 47, 20, 90, 83, 33, 38, 92, 48, 57, 93, 95, 70, 56, 88, 45, 26, 75, 98, 65, 4, 42, 77, 18, 23, 31, 19, 94, 49, 32, 21, 100, 30, 17, 28, 40, 11, 63, 67, 7, 62, 13, 73, 12, 14, 78, 2, 54, 71, 15, 6, 41, 81, 52, 96, 34, 44, 99, 84, 50, 8, 39]) == 35359128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 4, 2, 3, 2]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 4, 2, 3, 2]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 5, 1, 3]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 5, 1, 3]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 243603300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 243603300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]) == 82507800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]) == 82507800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2401100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2401100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 6, 5, 4, 3, 2, 1]) == 1026
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 6, 5, 4, 3, 2, 1]) == 1026: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 940: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1]) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1]) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000]) == 1010110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000]) == 1010110000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 88180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 88180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 243660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 243660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 100, 1, 99, 1, 100]) == 2019700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 100, 1, 99, 1, 100]) == 2019700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2401100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2401100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5820: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 13680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 13680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50]) == 13005100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50]) == 13005100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 11, 77, 32, 45, 62, 88, 12, 56, 78, 91, 29, 48, 50, 65, 73, 82, 90, 18, 27]) == 5732245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 11, 77, 32, 45, 62, 88, 12, 56, 78, 91, 29, 48, 50, 65, 73, 82, 90, 18, 27]) == 5732245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 24, 31, 29, 96, 9, 18, 45, 32, 27, 95, 38, 57, 47, 52, 56, 83, 40, 87, 91, 30, 72, 4, 36, 66, 6, 1, 49, 59, 27, 9, 81, 33, 17, 5, 74, 40, 85, 23, 47, 89, 69, 35, 16, 83, 87, 52, 15, 24, 91, 36, 80, 59, 27, 9, 81, 33, 17, 5, 74]) == 17249443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 24, 31, 29, 96, 9, 18, 45, 32, 27, 95, 38, 57, 47, 52, 56, 83, 40, 87, 91, 30, 72, 4, 36, 66, 6, 1, 49, 59, 27, 9, 81, 33, 17, 5, 74, 40, 85, 23, 47, 89, 69, 35, 16, 83, 87, 52, 15, 24, 91, 36, 80, 59, 27, 9, 81, 33, 17, 5, 74]) == 17249443: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 45602200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 45602200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 7, 5, 4, 1, 9, 6, 8, 2]) == 1723
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 7, 5, 4, 1, 9, 6, 8, 2]) == 1723: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1]) == 617
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1]) == 617: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 49060
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 49060: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 45640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 45640: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2382100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2382100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2670380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2670380: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5820: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 3520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 3520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20]) == 1676050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20]) == 1676050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 1, 3, 4, 6, 8, 7, 10, 9, 12, 11, 14, 13, 15]) == 13653
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 1, 3, 4, 6, 8, 7, 10, 9, 12, 11, 14, 13, 15]) == 13653: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 24, 30, 98, 99, 5, 91, 41, 72, 7, 42, 62, 95, 69, 32, 24, 38, 80, 44, 79, 9, 26, 6, 47, 93, 64, 39, 87, 63, 77, 85, 48, 52, 82, 35, 73, 12, 23, 59, 3, 78, 54, 75, 94, 19, 13, 71, 68, 28, 31, 5, 46, 89, 37, 90, 8, 60, 25, 97, 10, 30, 67, 49, 81, 20, 76, 61, 34, 14, 88, 17, 22, 4, 51, 15, 70, 18, 43, 40, 96, 36, 65, 83, 29, 57, 56, 21, 53, 92, 27, 33, 84, 45, 86, 16, 58, 74]) == 33856230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 24, 30, 98, 99, 5, 91, 41, 72, 7, 42, 62, 95, 69, 32, 24, 38, 80, 44, 79, 9, 26, 6, 47, 93, 64, 39, 87, 63, 77, 85, 48, 52, 82, 35, 73, 12, 23, 59, 3, 78, 54, 75, 94, 19, 13, 71, 68, 28, 31, 5, 46, 89, 37, 90, 8, 60, 25, 97, 10, 30, 67, 49, 81, 20, 76, 61, 34, 14, 88, 17, 22, 4, 51, 15, 70, 18, 43, 40, 96, 36, 65, 83, 29, 57, 56, 21, 53, 92, 27, 33, 84, 45, 86, 16, 58, 74]) == 33856230: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 8, 6, 4, 2, 1, 3, 10]) == 2474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 8, 6, 4, 2, 1, 3, 10]) == 2474: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 8010100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 8010100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 9, 1, 4, 7, 10, 11, 13, 12, 15, 14]) == 13102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 9, 1, 4, 7, 10, 11, 13, 12, 15, 14]) == 13102: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9530: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 1260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 1260: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 22, 44, 66, 88, 10, 30, 50]) == 5055964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 22, 44, 66, 88, 10, 30, 50]) == 5055964: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 40, 50, 10]) == 99330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 40, 50, 10]) == 99330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2401100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2401100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 100, 5, 10]) == 16110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 100, 5, 10]) == 16110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 10, 20, 30]) == 37940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 10, 20, 30]) == 37940: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 3, 4, 6, 1, 2, 8, 5]) == 1614
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 3, 4, 6, 1, 2, 8, 5]) == 1614: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 2630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 2630: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 3, 1, 8, 6, 5, 4, 2]) == 1677
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 3, 1, 8, 6, 5, 4, 2]) == 1677: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1]) == 110
    assert candidate(nums = [1, 5]) == 10
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]) == 1654
    assert candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 7, 4, 5, 5, 5, 4]) == 2886
    assert candidate(nums = [3, 1, 5, 8]) == 167
    assert candidate(nums = [0, 0, 0]) == 0
    assert candidate(nums = [9, 76, 66, 18, 49, 79, 11, 31, 2, 83, 45, 12, 50, 88, 67, 34, 73, 39, 100, 87, 30, 6, 41, 72, 84, 17, 29, 63, 52, 75, 58, 92, 37, 35, 61, 43, 89, 64, 55, 19, 32, 62, 57, 90, 91, 33, 44, 27, 3, 76, 65, 68, 42, 8, 54, 60, 10, 80, 70, 12, 3, 5, 82, 46, 30, 81, 13, 26, 93, 14, 20, 78, 86, 25, 56, 1, 36, 59, 74, 15, 95, 16, 4, 7, 22, 69, 51, 38, 85, 23, 40, 94, 48, 6, 97, 24, 53, 9, 96, 21, 47, 77, 99, 31, 28, 45, 32]) == 35112384
    assert candidate(nums = [10, 10, 10, 10]) == 2110
    assert candidate(nums = [100]) == 100
    assert candidate(nums = [9, 76, 64, 21, 97, 60]) == 1086136
    assert candidate(nums = [8, 3, 8, 3, 8]) == 968
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 110
    assert candidate(nums = [7, 9, 8, 0, 7, 1, 3, 5, 5, 7, 3]) == 2107
    assert candidate(nums = [35, 16, 83, 87, 52, 15, 24, 91, 36, 80, 59, 27, 9, 81, 33, 17, 5, 74, 40, 85, 23, 47, 89, 69]) == 6802248
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 5700600
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 10120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2420
    assert candidate(nums = [5, 8, 6, 2, 3, 7, 4, 1, 9]) == 1704
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 32339900
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 99]) == 474000
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 0, 3, 0, 1]) == 23783
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2427280
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 1010101200000
    assert candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]) == 15717
    assert candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11]) == 1510
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1, 2, 5, 10, 20, 30, 40, 50]) == 309374
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 14636200
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 243660
    assert candidate(nums = [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 43888
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4830
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 13150200
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 2010
    assert candidate(nums = [9, 75, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 2737551
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3050100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 13680
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 15284100
    assert candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5]) == 2906611
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 741
    assert candidate(nums = [50, 20, 30, 10, 40, 60, 70, 80, 90, 10]) == 1428550
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(nums = [50, 25, 75, 40, 60, 10, 80, 30, 90]) == 1779840
    assert candidate(nums = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 72420
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 2100
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]) == 98801200
    assert candidate(nums = [50, 25, 75, 20, 80, 15, 85, 10, 90, 5, 95, 40, 60, 35, 65, 30, 70, 45, 55, 2]) == 4854150
    assert candidate(nums = [82, 9, 60, 27, 69, 64, 53, 80, 74, 97, 22, 5, 35, 46, 91, 16, 51, 86, 58, 3, 53, 29, 37, 24, 36, 72, 39, 68, 55, 76, 59, 79, 85, 43, 87, 66, 89, 25, 47, 20, 90, 83, 33, 38, 92, 48, 57, 93, 95, 70, 56, 88, 45, 26, 75, 98, 65, 4, 42, 77, 18, 23, 31, 19, 94, 49, 32, 21, 100, 30, 17, 28, 40, 11, 63, 67, 7, 62, 13, 73, 12, 14, 78, 2, 54, 71, 15, 6, 41, 81, 52, 96, 34, 44, 99, 84, 50, 8, 39]) == 35359128
    assert candidate(nums = [2, 3, 2, 4, 2, 3, 2]) == 120
    assert candidate(nums = [1, 3, 1, 5, 1, 3]) == 90
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 243603300
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]) == 82507800
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2401100
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2420
    assert candidate(nums = [9, 7, 6, 5, 4, 3, 2, 1]) == 1026
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 940
    assert candidate(nums = [9, 7, 5, 3, 1]) == 495
    assert candidate(nums = [10, 100, 1000, 10000]) == 1010110000
    assert candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 88180
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 243660
    assert candidate(nums = [99, 1, 100, 1, 99, 1, 100]) == 2019700
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2401100
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5820
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 13680
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2420
    assert candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50]) == 13005100
    assert candidate(nums = [23, 11, 77, 32, 45, 62, 88, 12, 56, 78, 91, 29, 48, 50, 65, 73, 82, 90, 18, 27]) == 5732245
    assert candidate(nums = [50, 24, 31, 29, 96, 9, 18, 45, 32, 27, 95, 38, 57, 47, 52, 56, 83, 40, 87, 91, 30, 72, 4, 36, 66, 6, 1, 49, 59, 27, 9, 81, 33, 17, 5, 74, 40, 85, 23, 47, 89, 69, 35, 16, 83, 87, 52, 15, 24, 91, 36, 80, 59, 27, 9, 81, 33, 17, 5, 74]) == 17249443
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 45602200
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15220
    assert candidate(nums = [2, 3, 7, 5, 4, 1, 9, 6, 8, 2]) == 1723
    assert candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1]) == 617
    assert candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 49060
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 45640
    assert candidate(nums = [20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2382100
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2670380
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5820
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 3520
    assert candidate(nums = [50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20, 50, 20]) == 1676050
    assert candidate(nums = [2, 5, 1, 3, 4, 6, 8, 7, 10, 9, 12, 11, 14, 13, 15]) == 13653
    assert candidate(nums = [50, 24, 30, 98, 99, 5, 91, 41, 72, 7, 42, 62, 95, 69, 32, 24, 38, 80, 44, 79, 9, 26, 6, 47, 93, 64, 39, 87, 63, 77, 85, 48, 52, 82, 35, 73, 12, 23, 59, 3, 78, 54, 75, 94, 19, 13, 71, 68, 28, 31, 5, 46, 89, 37, 90, 8, 60, 25, 97, 10, 30, 67, 49, 81, 20, 76, 61, 34, 14, 88, 17, 22, 4, 51, 15, 70, 18, 43, 40, 96, 36, 65, 83, 29, 57, 56, 21, 53, 92, 27, 33, 84, 45, 86, 16, 58, 74]) == 33856230
    assert candidate(nums = [9, 7, 5, 8, 6, 4, 2, 1, 3, 10]) == 2474
    assert candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 8010100
    assert candidate(nums = [5, 3, 8, 6, 2, 9, 1, 4, 7, 10, 11, 13, 12, 15, 14]) == 13102
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9530
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 1260
    assert candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 22, 44, 66, 88, 10, 30, 50]) == 5055964
    assert candidate(nums = [30, 20, 40, 50, 10]) == 99330
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2401100
    assert candidate(nums = [10, 1, 100, 5, 10]) == 16110
    assert candidate(nums = [30, 20, 10, 5, 1, 2, 3, 4, 5, 10, 20, 30]) == 37940
    assert candidate(nums = [9, 7, 3, 4, 6, 1, 2, 8, 5]) == 1614
    assert candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 2630
    assert candidate(nums = [9, 7, 3, 1, 8, 6, 5, 4, 2]) == 1677


