def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(perm = [3, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(perm = [4, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [4, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 3, 1, 2, 4]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 3, 1, 2, 4]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(perm = [4, 1, 3, 2, 5]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [4, 1, 3, 2, 5]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 4, 3, 2, 1]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 4, 3, 2, 1]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628799: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 2, 1, 6, 5, 4]) == 269
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 2, 1, 6, 5, 4]) == 269: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 4, 1, 3, 5, 7, 6, 8, 10, 9, 11]) == 4354682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 4, 1, 3, 5, 7, 6, 8, 10, 9, 11]) == 4354682: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 4, 3, 2]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 4, 3, 2]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 4, 3, 5, 6, 2, 1]) == 4745
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 4, 3, 5, 6, 2, 1]) == 4745: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 5, 3, 1, 2, 6, 4]) == 4849
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 5, 3, 1, 2, 6, 4]) == 4849: {e}')
    
    total += 1
    try:
        result = candidate(perm = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 2903040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 2903040: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1583280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1583280: {e}')
    
    total += 1
    try:
        result = candidate(perm = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 437918129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 437918129: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 5, 4, 3, 2, 1]) == 719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 5, 4, 3, 2, 1]) == 719: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 1, 2, 3, 4, 5]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 1, 2, 3, 4, 5]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 5, 4, 2, 7, 6]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 5, 4, 2, 7, 6]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(perm = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]) == 560080235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]) == 560080235: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 5, 3, 4, 2]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 5, 3, 4, 2]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 5, 4, 3]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 5, 4, 3]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 409113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 409113: {e}')
    
    total += 1
    try:
        result = candidate(perm = [8, 7, 6, 5, 4, 3, 2, 1, 10, 9]) == 2810575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [8, 7, 6, 5, 4, 3, 2, 1, 10, 9]) == 2810575: {e}')
    
    total += 1
    try:
        result = candidate(perm = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 146326062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 146326062: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 3, 2, 4]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 3, 2, 4]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 2, 5, 1, 4]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 2, 5, 1, 4]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 3, 4, 2]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 3, 4, 2]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 3, 4, 5, 1]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 3, 4, 5, 1]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 6, 5, 4, 3, 2, 1]) == 5039
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 6, 5, 4, 3, 2, 1]) == 5039: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 2, 5, 4, 7, 6, 8, 10, 9]) == 41065
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 2, 5, 4, 7, 6, 8, 10, 9]) == 41065: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 4, 2, 3, 6, 8, 7, 10, 9]) == 1461607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 4, 2, 3, 6, 8, 7, 10, 9]) == 1461607: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1583280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1583280: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 4, 3, 2, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 4, 3, 2, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 5, 4, 2, 1]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 5, 4, 2, 1]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 4, 3, 2]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 4, 3, 2]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11]) == 15690086
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11]) == 15690086: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 5, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 5, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 5, 2, 4, 3]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 5, 2, 4, 3]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(perm = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 3301819
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 3301819: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]) == 2401464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]) == 2401464: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 5, 1, 2, 3, 4]) == 696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 5, 1, 2, 3, 4]) == 696: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 2, 3, 4]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 2, 3, 4]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 5, 3, 4, 2]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 5, 3, 4, 2]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(perm = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 437918129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 437918129: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 5, 4, 1, 2]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 5, 4, 1, 2]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 1, 4, 2, 3]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 1, 4, 2, 3]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(perm = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == 31840974
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == 31840974: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 368047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 368047: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 3, 5, 1, 2, 4, 7, 8, 10, 9]) == 1910161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 3, 5, 1, 2, 4, 7, 8, 10, 9]) == 1910161: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 3, 5, 1, 4, 2, 6, 8, 10, 9, 11]) == 22620242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 3, 5, 1, 4, 2, 6, 8, 10, 9, 11]) == 22620242: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 4, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 4, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 4, 3, 2, 1]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 4, 3, 2, 1]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 4, 3, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 4, 3, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(perm = [8, 7, 6, 5, 4, 3, 2, 1]) == 40319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [8, 7, 6, 5, 4, 3, 2, 1]) == 40319: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 5, 4, 1, 2]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 5, 4, 1, 2]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 5, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 5, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 4, 3, 5]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 4, 3, 5]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9]) == 721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9]) == 721: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 5, 1, 4, 2]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 5, 1, 4, 2]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 725760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 725760: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 6, 5, 4, 3, 2, 1]) == 5039
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 6, 5, 4, 3, 2, 1]) == 5039: {e}')
    
    total += 1
    try:
        result = candidate(perm = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 39916799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 39916799: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 1, 2, 3, 4, 5]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 1, 2, 3, 4, 5]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7]) == 215274239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7]) == 215274239: {e}')
    
    total += 1
    try:
        result = candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628799: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(perm = [7, 1, 2, 3, 4, 5, 6]) == 4320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [7, 1, 2, 3, 4, 5, 6]) == 4320: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 3, 1, 5, 4, 6]) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 3, 1, 5, 4, 6]) == 146: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 1, 4, 5, 3, 2]) == 617
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 1, 4, 5, 3, 2]) == 617: {e}')
    
    total += 1
    try:
        result = candidate(perm = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3265920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3265920: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 2, 1, 3, 4]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 2, 1, 3, 4]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 5, 4, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 5, 4, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 4, 3, 2, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 4, 3, 2, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 4, 2, 5, 1]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 4, 2, 5, 1]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(perm = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 1992360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 1992360: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 4, 1, 3, 5, 7, 6, 8, 10, 9]) == 443545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 4, 1, 3, 5, 7, 6, 8, 10, 9]) == 443545: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 5, 2, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 5, 2, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(perm = [8, 9, 7, 6, 5, 4, 3, 2, 1]) == 322559
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [8, 9, 7, 6, 5, 4, 3, 2, 1]) == 322559: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 3, 1, 4, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 3, 1, 4, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(perm = [5, 2, 1, 4, 3]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [5, 2, 1, 4, 3]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 53040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 53040: {e}')
    
    total += 1
    try:
        result = candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 35878886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 35878886: {e}')
    
    total += 1
    try:
        result = candidate(perm = [2, 1, 5, 4, 3]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [2, 1, 5, 4, 3]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(perm = [9, 5, 7, 3, 8, 2, 6, 4, 1]) == 346667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [9, 5, 7, 3, 8, 2, 6, 4, 1]) == 346667: {e}')
    
    total += 1
    try:
        result = candidate(perm = [3, 6, 5, 4, 1, 2, 8, 9, 7, 10]) == 903608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [3, 6, 5, 4, 1, 2, 8, 9, 7, 10]) == 903608: {e}')
    
    total += 1
    try:
        result = candidate(perm = [1, 3, 5, 2, 4, 7, 6, 8, 10, 9, 11]) == 443642
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(perm = [1, 3, 5, 2, 4, 7, 6, 8, 10, 9, 11]) == 443642: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(perm = [3, 1, 2]) == 4
    assert candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(perm = [4, 3, 2, 1]) == 23
    assert candidate(perm = [5, 3, 1, 2, 4]) == 108
    assert candidate(perm = [4, 1, 3, 2, 5]) == 74
    assert candidate(perm = [1, 2, 3, 4, 5]) == 0
    assert candidate(perm = [1, 3, 2]) == 1
    assert candidate(perm = [5, 4, 3, 2, 1]) == 119
    assert candidate(perm = [1, 2]) == 0
    assert candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628799
    assert candidate(perm = [3, 2, 1, 6, 5, 4]) == 269
    assert candidate(perm = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]) == 120
    assert candidate(perm = [2, 4, 1, 3, 5, 7, 6, 8, 10, 9, 11]) == 4354682
    assert candidate(perm = [5, 1, 4, 3, 2]) == 101
    assert candidate(perm = [7, 4, 3, 5, 6, 2, 1]) == 4745
    assert candidate(perm = [7, 5, 3, 1, 2, 6, 4]) == 4849
    assert candidate(perm = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 2903040
    assert candidate(perm = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1583280
    assert candidate(perm = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 437918129
    assert candidate(perm = [6, 5, 4, 3, 2, 1]) == 719
    assert candidate(perm = [6, 1, 2, 3, 4, 5]) == 600
    assert candidate(perm = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == 5040
    assert candidate(perm = [1, 3, 5, 4, 2, 7, 6]) == 175
    assert candidate(perm = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]) == 560080235
    assert candidate(perm = [1, 5, 3, 4, 2]) == 21
    assert candidate(perm = [2, 1, 5, 4, 3]) == 29
    assert candidate(perm = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 409113
    assert candidate(perm = [8, 7, 6, 5, 4, 3, 2, 1, 10, 9]) == 2810575
    assert candidate(perm = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 146326062
    assert candidate(perm = [5, 1, 3, 2, 4]) == 98
    assert candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == 1
    assert candidate(perm = [3, 2, 5, 1, 4]) == 58
    assert candidate(perm = [5, 1, 3, 4, 2]) == 99
    assert candidate(perm = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 362880
    assert candidate(perm = [2, 3, 4, 5, 1]) == 33
    assert candidate(perm = [7, 6, 5, 4, 3, 2, 1]) == 5039
    assert candidate(perm = [1, 3, 2, 5, 4, 7, 6, 8, 10, 9]) == 41065
    assert candidate(perm = [5, 1, 4, 2, 3, 6, 8, 7, 10, 9]) == 1461607
    assert candidate(perm = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1583280
    assert candidate(perm = [1, 4, 3, 2, 5]) == 14
    assert candidate(perm = [3, 5, 4, 2, 1]) == 71
    assert candidate(perm = [5, 1, 4, 3, 2]) == 101
    assert candidate(perm = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11]) == 15690086
    assert candidate(perm = [1, 2, 3, 5, 4]) == 1
    assert candidate(perm = [1, 5, 2, 4, 3]) == 19
    assert candidate(perm = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 3301819
    assert candidate(perm = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]) == 2401464
    assert candidate(perm = [6, 5, 1, 2, 3, 4]) == 696
    assert candidate(perm = [5, 1, 2, 3, 4]) == 96
    assert candidate(perm = [1, 5, 3, 4, 2]) == 21
    assert candidate(perm = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 437918129
    assert candidate(perm = [3, 5, 4, 1, 2]) == 70
    assert candidate(perm = [5, 1, 4, 2, 3]) == 100
    assert candidate(perm = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == 31840974
    assert candidate(perm = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 368047
    assert candidate(perm = [6, 3, 5, 1, 2, 4, 7, 8, 10, 9]) == 1910161
    assert candidate(perm = [7, 3, 5, 1, 4, 2, 6, 8, 10, 9, 11]) == 22620242
    assert candidate(perm = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 362880
    assert candidate(perm = [2, 1, 4, 3]) == 7
    assert candidate(perm = [5, 4, 3, 2, 1]) == 119
    assert candidate(perm = [1, 2, 4, 3, 5]) == 2
    assert candidate(perm = [8, 7, 6, 5, 4, 3, 2, 1]) == 40319
    assert candidate(perm = [3, 5, 4, 1, 2]) == 70
    assert candidate(perm = [1, 2, 3, 5, 4]) == 1
    assert candidate(perm = [2, 1, 4, 3, 5]) == 26
    assert candidate(perm = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9]) == 721
    assert candidate(perm = [3, 5, 1, 4, 2]) == 67
    assert candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(perm = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 725760
    assert candidate(perm = [7, 6, 5, 4, 3, 2, 1]) == 5039
    assert candidate(perm = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 39916799
    assert candidate(perm = [6, 1, 2, 3, 4, 5]) == 600
    assert candidate(perm = [6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7]) == 215274239
    assert candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628799
    assert candidate(perm = [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]) == 2
    assert candidate(perm = [7, 1, 2, 3, 4, 5, 6]) == 4320
    assert candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(perm = [2, 3, 1, 5, 4, 6]) == 146
    assert candidate(perm = [6, 1, 4, 5, 3, 2]) == 617
    assert candidate(perm = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3265920
    assert candidate(perm = [5, 2, 1, 3, 4]) == 102
    assert candidate(perm = [1, 3, 5, 4, 2]) == 11
    assert candidate(perm = [1, 4, 3, 2, 5]) == 14
    assert candidate(perm = [3, 4, 2, 5, 1]) == 63
    assert candidate(perm = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 1992360
    assert candidate(perm = [2, 4, 1, 3, 5, 7, 6, 8, 10, 9]) == 443545
    assert candidate(perm = [1, 3, 5, 2, 4]) == 10
    assert candidate(perm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
    assert candidate(perm = [8, 9, 7, 6, 5, 4, 3, 2, 1]) == 322559
    assert candidate(perm = [2, 3, 1, 4, 5]) == 30
    assert candidate(perm = [5, 2, 1, 4, 3]) == 103
    assert candidate(perm = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 53040
    assert candidate(perm = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 35878886
    assert candidate(perm = [2, 1, 5, 4, 3]) == 29
    assert candidate(perm = [9, 5, 7, 3, 8, 2, 6, 4, 1]) == 346667
    assert candidate(perm = [3, 6, 5, 4, 1, 2, 8, 9, 7, 10]) == 903608
    assert candidate(perm = [1, 3, 5, 2, 4, 7, 6, 8, 10, 9, 11]) == 443642


