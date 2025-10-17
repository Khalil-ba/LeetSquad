def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr1 = [1, -2, -5, 0, 10],arr2 = [0, -2, -1, -7, -4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -2, -5, 0, 10],arr2 = [0, -2, -1, -7, -4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7],arr2 = [2, 4, 6, 8]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7],arr2 = [2, 4, 6, 8]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1, -2, -3, -4, -5],arr2 = [1, 2, 3, 4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1, -2, -3, -4, -5],arr2 = [1, 2, 3, 4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [9, 7, 5, 3, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [9, 7, 5, 3, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0, 0, 0],arr2 = [0, 0, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0, 0, 0],arr2 = [0, 0, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1000000, 1000000],arr2 = [1000000, -1000000]) == 4000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1000000, 1000000],arr2 = [1000000, -1000000]) == 4000001: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0],arr2 = [0, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0],arr2 = [0, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4],arr2 = [-1, 4, 5, 6]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4],arr2 = [-1, 4, 5, 6]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, -1000000],arr2 = [-1000000, 1000000]) == 4000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, -1000000],arr2 = [-1000000, 1000000]) == 4000001: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 5, 5, 5],arr2 = [5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 5, 5, 5],arr2 = [5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 918
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 918: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1000000, -900000, -800000, -700000, -600000, -500000, -400000, -300000, -200000, -100000],arr2 = [-100000, -200000, -300000, -400000, -500000, -600000, -700000, -800000, -900000, -1000000]) == 1800009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1000000, -900000, -800000, -700000, -600000, -500000, -400000, -300000, -200000, -100000],arr2 = [-100000, -200000, -300000, -400000, -500000, -600000, -700000, -800000, -900000, -1000000]) == 1800009: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -2, 3, -4, 5],arr2 = [-5, 4, -3, 2, -1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -2, 3, -4, 5],arr2 = [-5, 4, -3, 2, -1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5],arr2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5],arr2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],arr2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],arr2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],arr2 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 18009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],arr2 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 18009: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500],arr2 = [-1000, 1000, -900, 900, -800, 800, -700, 700, -600, 600]) == 2209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500],arr2 = [-1000, 1000, -900, 900, -800, 800, -700, 700, -600, 600]) == 2209: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1, 1, -2, 2, -3, 3],arr2 = [-3, 3, -2, 2, -1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1, 1, -2, 2, -3, 3],arr2 = [-3, 3, -2, 2, -1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [123456, -234567, 345678, -456789, 567890],arr2 = [567890, -456789, 345678, -234567, 123456]) == 1382713
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [123456, -234567, 345678, -456789, 567890],arr2 = [567890, -456789, 345678, -234567, 123456]) == 1382713: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],arr2 = [-512, -256, -128, -64, -32, -16, -8, -4, -2, -1]) == 1031
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],arr2 = [-512, -256, -128, -64, -32, -16, -8, -4, -2, -1]) == 1031: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [1000, -1000, 900, -900, 800, -800, 700, -700, 600, -600]) == 2003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [1000, -1000, 900, -900, 800, -800, 700, -700, 600, -600]) == 2003: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 999999, 999998, 999997, 999996],arr2 = [0, 1, 2, 3, 4]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 999999, 999998, 999997, 999996],arr2 = [0, 1, 2, 3, 4]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [5, -5, 4, -4, 3, -3, 2, -2, 1, -1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [5, -5, 4, -4, 3, -3, 2, -2, 1, -1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],arr2 = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],arr2 = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-100000, 100000, -50000, 50000, -25000, 25000],arr2 = [25000, -25000, 50000, -50000, 100000, -100000]) == 250005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-100000, 100000, -50000, 50000, -25000, 25000],arr2 = [25000, -25000, 50000, -50000, 100000, -100000]) == 250005: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 0, -1000000, 500000, -500000],arr2 = [-1000000, 1000000, 0, -500000, 500000]) == 3000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 0, -1000000, 500000, -500000],arr2 = [-1000000, 1000000, 0, -500000, 500000]) == 3000004: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, -1000000, 500000, -500000],arr2 = [-1000000, 1000000, -500000, 500000]) == 4000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, -1000000, 500000, -500000],arr2 = [-1000000, 1000000, -500000, 500000]) == 4000001: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],arr2 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],arr2 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],arr2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],arr2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [5, 6, 8, 10, 15, 20, 30, 40, 50, 60],arr2 = [60, 50, 40, 30, 20, 15, 10, 8, 6, 5]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [5, 6, 8, 10, 15, 20, 30, 40, 50, 60],arr2 = [60, 50, 40, 30, 20, 15, 10, 8, 6, 5]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],arr2 = [999991, 999992, 999993, 999994, 999995, 999996, 999997, 999998, 999999, 1000000]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],arr2 = [999991, 999992, 999993, 999994, 999995, 999996, 999997, 999998, 999999, 1000000]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1000000, 0, 1000000, -500000, 500000],arr2 = [500000, -500000, 0, 1000000, -1000000]) == 3000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1000000, 0, 1000000, -500000, 500000],arr2 = [500000, -500000, 0, 1000000, -1000000]) == 3000004: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [500000, 400000, 300000, 200000, 100000, 0, -100000, -200000, -300000, -400000],arr2 = [-500000, -400000, -300000, -200000, -100000, 0, 100000, 200000, 300000, 400000]) == 1800009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [500000, 400000, 300000, 200000, 100000, 0, -100000, -200000, -300000, -400000],arr2 = [-500000, -400000, -300000, -200000, -100000, 0, 100000, 200000, 300000, 400000]) == 1800009: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -1, 2, -2, 3, -3],arr2 = [1, 2, 3, -1, -2, -3]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -1, 2, -2, 3, -3],arr2 = [1, 2, 3, -1, -2, -3]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],arr2 = [-1000000, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],arr2 = [-1000000, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, -10, 20, -20, 30, -30],arr2 = [-30, 30, -20, 20, -10, 10]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, -10, 20, -20, 30, -30],arr2 = [-30, 30, -20, 20, -10, 10]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10000, -10000, 20000, -20000, 30000, -30000],arr2 = [-30000, 30000, -20000, 20000, -10000, 10000]) == 80005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10000, -10000, 20000, -20000, 30000, -30000],arr2 = [-30000, 30000, -20000, 20000, -10000, 10000]) == 80005: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000],arr2 = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000]) == 4000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000],arr2 = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000]) == 4000009: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 500000, -500000, -1000000],arr2 = [-1000000, 500000, 1000000, -500000]) == 3500002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 500000, -500000, -1000000],arr2 = [-1000000, 500000, 1000000, -500000]) == 3500002: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0, 0],arr2 = [-1, 1, -1, 1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0, 0],arr2 = [-1, 1, -1, 1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [-100, -200, -300, -400, -500]) == 804
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [-100, -200, -300, -400, -500]) == 804: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, -1000000, 500000, -500000],arr2 = [-500000, 500000, -1000000, 1000000]) == 3000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, -1000000, 500000, -500000],arr2 = [-500000, 500000, -1000000, 1000000]) == 3000003: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1809
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1809: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [900, 800, 700, 600, 500]) == 804
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [900, 800, 700, 600, 500]) == 804: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],arr2 = [5, -5, 4, -4, 3, -3, 2, -2, 1, -1, 0]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],arr2 = [5, -5, 4, -4, 3, -3, 2, -2, 1, -1, 0]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [42, 17, 9, 23, 5, 6, 8],arr2 = [3, 8, 1, 4, 7, 2, 9]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [42, 17, 9, 23, 5, 6, 8],arr2 = [3, 8, 1, 4, 7, 2, 9]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [-10, -20, -30, -40, -50]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [-10, -20, -30, -40, -50]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 500000, 0, -500000, -1000000],arr2 = [-1000000, -500000, 0, 500000, 1000000]) == 4000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 500000, 0, -500000, -1000000],arr2 = [-1000000, -500000, 0, 500000, 1000000]) == 4000004: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -100, 100, 0, 50, -50, 25, -25, 75, -75],arr2 = [100, 1, -1, 50, -50, 100, -100, 0, 75, -75]) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -100, 100, 0, 50, -50, 25, -25, 75, -75],arr2 = [100, 1, -1, 50, -50, 100, -100, 0, 75, -75]) == 301: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1000000, 0, 1000000, -1000000, 0, 1000000],arr2 = [0, 1000000, -1000000, 0, 1000000, -1000000]) == 3000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1000000, 0, 1000000, -1000000, 0, 1000000],arr2 = [0, 1000000, -1000000, 0, 1000000, -1000000]) == 3000005: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],arr2 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],arr2 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [-1000000, 1000000, -1000000, 1000000, -1000000]) == 4000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [-1000000, 1000000, -1000000, 1000000, -1000000]) == 4000003: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],arr2 = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],arr2 = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 10, 100, 1000, 10000, 100000, 1000000, -1, -10, -100],arr2 = [1000000, 100000, 10000, 1000, 100, 10, 1, -1000000, -100000, -10000]) == 2000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 10, 100, 1000, 10000, 100000, 1000000, -1, -10, -100],arr2 = [1000000, 100000, 10000, 1000, 100, 10, 1, -1000000, -100000, -10000]) == 2000009: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1000000, -500000, 0, 500000, 1000000],arr2 = [1000000, 500000, 0, -500000, -1000000]) == 4000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1000000, -500000, 0, 500000, 1000000],arr2 = [1000000, 500000, 0, -500000, -1000000]) == 4000004: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [123456, -123456, 234567, -234567, 345678, -345678],arr2 = [-345678, 345678, -234567, 234567, -123456, 123456]) == 938273
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [123456, -123456, 234567, -234567, 345678, -345678],arr2 = [-345678, 345678, -234567, 234567, -123456, 123456]) == 938273: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [123456, -123456, 654321, -654321, 234567, -234567],arr2 = [234567, -234567, 123456, -123456, 654321, -654321]) == 1777777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [123456, -123456, 654321, -654321, 234567, -234567],arr2 = [234567, -234567, 123456, -123456, 654321, -654321]) == 1777777: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1, 0, 1, -2, 2, -3, 3],arr2 = [3, -3, 2, -2, 1, -1, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1, 0, 1, -2, 2, -3, 3],arr2 = [3, -3, 2, -2, 1, -1, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [1000000, 500000, 0, -500000, -1000000, -1500000, -2000000, -2500000, -3000000, -3500000]) == 4500009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [1000000, 500000, 0, -500000, -1000000, -1500000, -2000000, -2500000, -3000000, -3500000]) == 4500009: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 1, 0, 1, 0, 1, 0],arr2 = [1, 0, 1, 0, 1, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 1, 0, 1, 0, 1, 0],arr2 = [1, 0, 1, 0, 1, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [0, 1000000, 0, 1000000, 0]) == 3000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [0, 1000000, 0, 1000000, 0]) == 3000003: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],arr2 = [8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 14007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],arr2 = [8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 14007: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1000000, 500000, -500000, -1000000, 0],arr2 = [0, 1000000, -1000000, 500000, -500000]) == 3000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1000000, 500000, -500000, -1000000, 0],arr2 = [0, 1000000, -1000000, 500000, -500000]) == 3000001: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5],arr2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5],arr2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],arr2 = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],arr2 = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000]) == 4000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000]) == 4000005: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [50, 40, 30, 20, 10]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [50, 40, 30, 20, 10]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [100000, 200000, 300000, 400000, 500000],arr2 = [500000, 400000, 300000, 200000, 100000]) == 800004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [100000, 200000, 300000, 400000, 500000],arr2 = [500000, 400000, 300000, 200000, 100000]) == 800004: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [-5, -4, -3, -2, -1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [-5, -4, -3, -2, -1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr1 = [1, -2, -5, 0, 10],arr2 = [0, -2, -1, -7, -4]) == 20
    assert candidate(arr1 = [1, 3, 5, 7],arr2 = [2, 4, 6, 8]) == 15
    assert candidate(arr1 = [-1, -2, -3, -4, -5],arr2 = [1, 2, 3, 4, 5]) == 12
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [9, 7, 5, 3, 1]) == 20
    assert candidate(arr1 = [0, 0, 0, 0, 0, 0],arr2 = [0, 0, 0, 0, 0, 0]) == 5
    assert candidate(arr1 = [-1000000, 1000000],arr2 = [1000000, -1000000]) == 4000001
    assert candidate(arr1 = [0, 0, 0, 0],arr2 = [0, 0, 0, 0]) == 3
    assert candidate(arr1 = [1, 2, 3, 4],arr2 = [-1, 4, 5, 6]) == 13
    assert candidate(arr1 = [1000000, -1000000],arr2 = [-1000000, 1000000]) == 4000001
    assert candidate(arr1 = [5, 5, 5, 5],arr2 = [5, 5, 5, 5]) == 3
    assert candidate(arr1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 918
    assert candidate(arr1 = [-1000000, -900000, -800000, -700000, -600000, -500000, -400000, -300000, -200000, -100000],arr2 = [-100000, -200000, -300000, -400000, -500000, -600000, -700000, -800000, -900000, -1000000]) == 1800009
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
    assert candidate(arr1 = [1, -2, 3, -4, 5],arr2 = [-5, 4, -3, 2, -1]) == 15
    assert candidate(arr1 = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5],arr2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 23
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 45
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 108
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 57
    assert candidate(arr1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],arr2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 11
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 189
    assert candidate(arr1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],arr2 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 18009
    assert candidate(arr1 = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500],arr2 = [-1000, 1000, -900, 900, -800, 800, -700, 700, -600, 600]) == 2209
    assert candidate(arr1 = [-1, 1, -2, 2, -3, 3],arr2 = [-3, 3, -2, 2, -1, 1]) == 13
    assert candidate(arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 30
    assert candidate(arr1 = [123456, -234567, 345678, -456789, 567890],arr2 = [567890, -456789, 345678, -234567, 123456]) == 1382713
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 27
    assert candidate(arr1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],arr2 = [-512, -256, -128, -64, -32, -16, -8, -4, -2, -1]) == 1031
    assert candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [1000, -1000, 900, -900, 800, -800, 700, -700, 600, -600]) == 2003
    assert candidate(arr1 = [1000000, 999999, 999998, 999997, 999996],arr2 = [0, 1, 2, 3, 4]) == 12
    assert candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [5, -5, 4, -4, 3, -3, 2, -2, 1, -1]) == 21
    assert candidate(arr1 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],arr2 = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == 31
    assert candidate(arr1 = [-100000, 100000, -50000, 50000, -25000, 25000],arr2 = [25000, -25000, 50000, -50000, 100000, -100000]) == 250005
    assert candidate(arr1 = [1000000, 0, -1000000, 500000, -500000],arr2 = [-1000000, 1000000, 0, -500000, 500000]) == 3000004
    assert candidate(arr1 = [1000000, -1000000, 500000, -500000],arr2 = [-1000000, 1000000, -500000, 500000]) == 4000001
    assert candidate(arr1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],arr2 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 23
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],arr2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(arr1 = [5, 6, 8, 10, 15, 20, 30, 40, 50, 60],arr2 = [60, 50, 40, 30, 20, 15, 10, 8, 6, 5]) == 119
    assert candidate(arr1 = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],arr2 = [999991, 999992, 999993, 999994, 999995, 999996, 999997, 999998, 999999, 1000000]) == 27
    assert candidate(arr1 = [-1000000, 0, 1000000, -500000, 500000],arr2 = [500000, -500000, 0, 1000000, -1000000]) == 3000004
    assert candidate(arr1 = [500000, 400000, 300000, 200000, 100000, 0, -100000, -200000, -300000, -400000],arr2 = [-500000, -400000, -300000, -200000, -100000, 0, 100000, 200000, 300000, 400000]) == 1800009
    assert candidate(arr1 = [1, -1, 2, -2, 3, -3],arr2 = [1, 2, 3, -1, -2, -3]) == 14
    assert candidate(arr1 = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],arr2 = [-1000000, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991]) == 27
    assert candidate(arr1 = [10, -10, 20, -20, 30, -30],arr2 = [-30, 30, -20, 20, -10, 10]) == 85
    assert candidate(arr1 = [10000, -10000, 20000, -20000, 30000, -30000],arr2 = [-30000, 30000, -20000, 20000, -10000, 10000]) == 80005
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1]) == 10
    assert candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000],arr2 = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000]) == 4000009
    assert candidate(arr1 = [1000000, 500000, -500000, -1000000],arr2 = [-1000000, 500000, 1000000, -500000]) == 3500002
    assert candidate(arr1 = [0, 0, 0, 0, 0],arr2 = [-1, 1, -1, 1, -1]) == 5
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [-100, -200, -300, -400, -500]) == 804
    assert candidate(arr1 = [1000000, -1000000, 500000, -500000],arr2 = [-500000, 500000, -1000000, 1000000]) == 3000003
    assert candidate(arr1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],arr2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1809
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [900, 800, 700, 600, 500]) == 804
    assert candidate(arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27
    assert candidate(arr1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(arr1 = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],arr2 = [5, -5, 4, -4, 3, -3, 2, -2, 1, -1, 0]) == 21
    assert candidate(arr1 = [42, 17, 9, 23, 5, 6, 8],arr2 = [3, 8, 1, 4, 7, 2, 9]) == 46
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [-10, -20, -30, -40, -50]) == 84
    assert candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 108
    assert candidate(arr1 = [1000000, 500000, 0, -500000, -1000000],arr2 = [-1000000, -500000, 0, 500000, 1000000]) == 4000004
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 189
    assert candidate(arr1 = [1, -100, 100, 0, 50, -50, 25, -25, 75, -75],arr2 = [100, 1, -1, 50, -50, 100, -100, 0, 75, -75]) == 301
    assert candidate(arr1 = [-1000000, 0, 1000000, -1000000, 0, 1000000],arr2 = [0, 1000000, -1000000, 0, 1000000, -1000000]) == 3000005
    assert candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 9
    assert candidate(arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 19
    assert candidate(arr1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],arr2 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 10
    assert candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [-1000000, 1000000, -1000000, 1000000, -1000000]) == 4000003
    assert candidate(arr1 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],arr2 = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 189
    assert candidate(arr1 = [1, 10, 100, 1000, 10000, 100000, 1000000, -1, -10, -100],arr2 = [1000000, 100000, 10000, 1000, 100, 10, 1, -1000000, -100000, -10000]) == 2000009
    assert candidate(arr1 = [-1000000, -500000, 0, 500000, 1000000],arr2 = [1000000, 500000, 0, -500000, -1000000]) == 4000004
    assert candidate(arr1 = [123456, -123456, 234567, -234567, 345678, -345678],arr2 = [-345678, 345678, -234567, 234567, -123456, 123456]) == 938273
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 27
    assert candidate(arr1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],arr2 = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 21
    assert candidate(arr1 = [123456, -123456, 654321, -654321, 234567, -234567],arr2 = [234567, -234567, 123456, -123456, 654321, -654321]) == 1777777
    assert candidate(arr1 = [-1, 0, 1, -2, 2, -3, 3],arr2 = [3, -3, 2, -2, 1, -1, 0]) == 13
    assert candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [1000000, 500000, 0, -500000, -1000000, -1500000, -2000000, -2500000, -3000000, -3500000]) == 4500009
    assert candidate(arr1 = [0, 1, 0, 1, 0, 1, 0],arr2 = [1, 0, 1, 0, 1, 0, 1]) == 7
    assert candidate(arr1 = [1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [0, 1000000, 0, 1000000, 0]) == 3000003
    assert candidate(arr1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],arr2 = [8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 14007
    assert candidate(arr1 = [1000000, 500000, -500000, -1000000, 0],arr2 = [0, 1000000, -1000000, 500000, -500000]) == 3000001
    assert candidate(arr1 = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5],arr2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 23
    assert candidate(arr1 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],arr2 = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 13
    assert candidate(arr1 = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]) == 30
    assert candidate(arr1 = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000],arr2 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000]) == 4000005
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [50, 40, 30, 20, 10]) == 84
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],arr2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 57
    assert candidate(arr1 = [100000, 200000, 300000, 400000, 500000],arr2 = [500000, 400000, 300000, 200000, 100000]) == 800004
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [-5, -4, -3, -2, -1]) == 12
    assert candidate(arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [-1, -1, -1, -1, -1]) == 4


