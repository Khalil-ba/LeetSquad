def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 8, 7, -2, 6]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 8, 7, -2, 6]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 2, 7, -6, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 2, 7, -6, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 2, -4, 6]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 2, -4, 6]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -8, -7, -2, -6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -8, -7, -2, -6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 3, -2, 7, -6, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 3, -2, 7, -6, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 164: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, -5, 2, -3, 3, 9, -1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, -5, 2, -3, 3, 9, -1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == 4000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == 4000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 10, -5, 10, -5, 10, -5, 10, -5, 10, -5]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 10, -5, 10, -5, 10, -5, 10, -5, 10, -5]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14]) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14]) == 194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 6000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 6000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, -2, -4, -6, 7, 9, -11, 13]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, -2, -4, -6, 7, 9, -11, 13]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000, 1000000000, 1000000000, -1000000000, -1000000000]) == 4000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000, 1000000000, 1000000000, -1000000000, -1000000000]) == 4000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -1, 3, -4, 5, -6, 7, -8]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -1, 3, -4, 5, -6, 7, -8]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 4, -3, 2, -1, 0, 1, -2, 3, -4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 4, -3, 2, -1, 0, 1, -2, 3, -4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -999999999, 999999998, -999999997, 999999996, -999999995]) == 5999999985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -999999999, 999999998, -999999997, 999999996, -999999995]) == 5999999985: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 820: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 530: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, 3, -2, 15, -8, 7, -6, 5, -4]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, 3, -2, 15, -8, 7, -6, 5, -4]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 134: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20, 21, -22, 23, -24, 25, -26, 27, -28, 29, -30, 31]) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20, 21, -22, 23, -24, 25, -26, 27, -28, 29, -30, 31]) == 496: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -3, 2, -4, 3, -5, 4, -6, 5, -7, 6, -8, 7, -9, 8, -10]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -3, 2, -4, 3, -5, 4, -6, 5, -7, 6, -8, 7, -9, 8, -10]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99]) == 1592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99]) == 1592: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 999999999, -999999998, 999999997, -999999996, 999999995]) == 3999999985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 999999999, -999999998, 999999997, -999999996, 999999995]) == 3999999985: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 55000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 55000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -3, 5, -7, 9, -11, 13, -15, 17]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -3, 5, -7, 9, -11, 13, -15, 17]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -30, 20, -10, 0, 10, -20, 30, -40, 50]) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -30, 20, -10, 0, 10, -20, 30, -40, 50]) == 260: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000]) == 7500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000]) == 7500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 3, -8, 2, 1, -4, 6, -7, 9]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 3, -8, 2, 1, -4, 6, -7, 9]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, 100, -10, 1000, -100, 10000, -1000, 100000, -10000]) == 122221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, 100, -10, 1000, -100, 10000, -1000, 100000, -10000]) == 122221: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, -500000000, 250000000, -250000000, 125000000, -125000000, 62500000, -62500000, 31250000]) == 2906250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, -500000000, 250000000, -250000000, 125000000, -125000000, 62500000, -62500000, 31250000]) == 2906250000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 530: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, -5, 7, -9, 11, -13, 15, -17, 19]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, -5, 7, -9, 11, -13, 15, -17, 19]) == 100: {e}')
    
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
        result = candidate(nums = [1000000000, 2000000000, -3000000000, 4000000000, -5000000000, 6000000000]) == 21000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, -3000000000, 4000000000, -5000000000, 6000000000]) == 21000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 8, 7, -2, 6, -1, 4, 3, -5, 2, -8, 9, -4, 7, -6, 1, -2, 3, -10]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 8, 7, -2, 6, -1, 4, 3, -5, 2, -8, 9, -4, 7, -6, 1, -2, 3, -10]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000, 1000000000, 1000000000]) == 4000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000, 1000000000, 1000000000]) == 4000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 50, -50, 50, -50, 50, -50, 50, -50]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 50, -50, 50, -50, 50, -50, 50, -50]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000]) == 6000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000]) == 6000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600, 1700, -1800, 1900, -2000]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600, 1700, -1800, 1900, -2000]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -7, 5, -3, 1, -8, 6, -4, 2, -9, 7, -5, 3, -1, 0]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -7, 5, -3, 1, -8, 6, -4, 2, -9, 7, -5, 3, -1, 0]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 40: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, -3, 8, 7, -2, 6]) == 31
    assert candidate(nums = [5, -3, 2, 7, -6, 1]) == 24
    assert candidate(nums = [5, -3, 2, -4, 6]) == 20
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, -1, 1, -1]) == 4
    assert candidate(nums = [1, -2, 3, 4]) == 10
    assert candidate(nums = [1, -1]) == 2
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 5000000000
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 1
    assert candidate(nums = [-5, -3, -8, -7, -2, -6]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [-5, 3, -2, 7, -6, 1]) == 14
    assert candidate(nums = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 164
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [5, 3, -5, 2, -3, 3, 9, -1]) == 31
    assert candidate(nums = [-1, -2, -3, -4]) == 2
    assert candidate(nums = [1, 2]) == 3
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == 4000000000
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 100
    assert candidate(nums = [10, -5, 10, -5, 10, -5, 10, -5, 10, -5, 10, -5]) == 90
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14]) == 194
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 10
    assert candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 6000000000
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 140
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 9000000000
    assert candidate(nums = [5, 3, 1, -2, -4, -6, 7, 9, -11, 13]) == 53
    assert candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000, 1000000000, 1000000000, -1000000000, -1000000000]) == 4000000000
    assert candidate(nums = [1, 2, -1, 3, -4, 5, -6, 7, -8]) == 37
    assert candidate(nums = [-5, 4, -3, 2, -1, 0, 1, -2, 3, -4]) == 15
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == 5500
    assert candidate(nums = [1000000000, -999999999, 999999998, -999999997, 999999996, -999999995]) == 5999999985
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 44
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 36
    assert candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1, 0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 20
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 820
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 530
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 208
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 20
    assert candidate(nums = [10, -1, 3, -2, 15, -8, 7, -6, 5, -4]) == 61
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 300
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 134
    assert candidate(nums = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]) == 6
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20, 21, -22, 23, -24, 25, -26, 27, -28, 29, -30, 31]) == 496
    assert candidate(nums = [1, -3, 2, -4, 3, -5, 4, -6, 5, -7, 6, -8, 7, -9, 8, -10]) == 88
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 18
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955
    assert candidate(nums = [100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99]) == 1592
    assert candidate(nums = [-1000000000, 999999999, -999999998, 999999997, -999999996, 999999995]) == 3999999985
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 55000000000
    assert candidate(nums = [1, -3, 5, -7, 9, -11, 13, -15, 17]) == 81
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [50, -30, 20, -10, 0, 10, -20, 30, -40, 50]) == 260
    assert candidate(nums = [1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000, 1000000000, -500000000]) == 7500000000
    assert candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39]) == 20
    assert candidate(nums = [10, -5, 3, -8, 2, 1, -4, 6, -7, 9]) == 55
    assert candidate(nums = [10, -1, 100, -10, 1000, -100, 10000, -1000, 100000, -10000]) == 122221
    assert candidate(nums = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == 6000
    assert candidate(nums = [100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 5500
    assert candidate(nums = [1000000000, 500000000, -500000000, 250000000, -250000000, 125000000, -125000000, 62500000, -62500000, 31250000]) == 2906250000
    assert candidate(nums = [-10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 530
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 15
    assert candidate(nums = [1, 3, -5, 7, -9, 11, -13, 15, -17, 19]) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1000000000, 2000000000, -3000000000, 4000000000, -5000000000, 6000000000]) == 21000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 60
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 55
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12]) == 76
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100]) == 6000
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 12
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [5, -3, 8, 7, -2, 6, -1, 4, 3, -5, 2, -8, 9, -4, 7, -6, 1, -2, 3, -10]) == 96
    assert candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000, 1000000000, 1000000000]) == 4000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -5
    assert candidate(nums = [1, 2, -3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14]) == 99
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550
    assert candidate(nums = [100, -50, 50, -50, 50, -50, 50, -50, 50, -50]) == 550
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000]) == 6000000000
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 6
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600, 1700, -1800, 1900, -2000]) == 21000
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 18
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 250
    assert candidate(nums = [500000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000]) == 5000000000
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 5
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
    assert candidate(nums = [9, -7, 5, -3, 1, -8, 6, -4, 2, -9, 7, -5, 3, -1, 0]) == 70
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 11
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 16
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 120
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 50
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 40


