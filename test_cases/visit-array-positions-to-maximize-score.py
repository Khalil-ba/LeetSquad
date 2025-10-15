def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],x = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],x = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 13, 15, 17, 19],x = 10) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 13, 15, 17, 19],x = 10) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6],x = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6],x = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 13, 14, 15, 19],x = 10) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 13, 14, 15, 19],x = 10) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2, 4, 6, 7, 8, 9],x = 4) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2, 4, 6, 7, 8, 9],x = 4) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5],x = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5],x = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30],x = 10) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30],x = 10) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],x = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],x = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 10, 11, 12],x = 7) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 10, 11, 12],x = 7) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30],x = 7) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30],x = 7) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 1, 9, 2],x = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 1, 9, 2],x = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 14, 15],x = 3) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 14, 15],x = 3) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],x = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],x = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 9, 2, 4],x = 6) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 9, 2, 4],x = 6) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8],x = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8],x = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 2) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 2) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 3) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 3) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100001, 100002, 100003, 100004, 100005, 100006, 100007, 100008, 100009],x = 50000) == 550045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100001, 100002, 100003, 100004, 100005, 100006, 100007, 100008, 100009],x = 50000) == 550045: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 150) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 150) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 3) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 3) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9],x = 3) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9],x = 3) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 8, 7, 4, 6, 9, 5, 10],x = 6) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 8, 7, 4, 6, 9, 5, 10],x = 6) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],x = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],x = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 7) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 7) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],x = 10) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],x = 10) == 520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],x = 30) == 239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],x = 30) == 239: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 1) == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 1) == 191: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 17, 18, 13, 20, 21, 16, 19, 14, 15],x = 8) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 17, 18, 13, 20, 21, 16, 19, 14, 15],x = 8) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 10) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 10) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],x = 2) == 409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],x = 2) == 409: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],x = 7) == 632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],x = 7) == 632: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 15) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 15) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 30, 20, 40, 50, 70, 60, 90, 80, 100, 120, 110, 140, 130, 160, 150, 180, 170, 200, 190],x = 20) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 30, 20, 40, 50, 70, 60, 90, 80, 100, 120, 110, 140, 130, 160, 150, 180, 170, 200, 190],x = 20) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],x = 5) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],x = 5) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11],x = 2) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11],x = 2) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],x = 100000) == 6399979
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],x = 100000) == 6399979: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],x = 20) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],x = 20) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],x = 10) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],x = 10) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],x = 1000) == 5994985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],x = 1000) == 5994985: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],x = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],x = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009],x = 100000) == 9100045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009],x = 100000) == 9100045: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 2) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 2) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],x = 500000) == 5499975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],x = 500000) == 5499975: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 1) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 1) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],x = 15) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],x = 15) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],x = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],x = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 500000) == 5499969
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 500000) == 5499969: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],x = 2) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],x = 2) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 100) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 100) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],x = 100000) == 1980468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],x = 100000) == 1980468: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1000001, 1000010, 1000100, 1001000, 1010000, 1100000],x = 1000000) == 5222221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1000001, 1000010, 1000100, 1001000, 1010000, 1100000],x = 1000000) == 5222221: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 499999, 499998, 499997, 499996, 499995, 499994, 499993, 499992, 499991, 499990, 499989, 499988, 499987, 499986, 499985, 499984, 499983, 499982, 499981],x = 100000) == 8099810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 499999, 499998, 499997, 499996, 499995, 499994, 499993, 499992, 499991, 499990, 499989, 499988, 499987, 499986, 499985, 499984, 499983, 499982, 499981],x = 100000) == 8099810: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 100000) == 9099945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 100000) == 9099945: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 3) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 3) == 159: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],x = 20) == 308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],x = 20) == 308: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62],x = 7) == 543
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62],x = 7) == 543: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],x = 25) == 675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],x = 25) == 675: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996],x = 500000) == 2999994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996],x = 500000) == 2999994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 1, 9, 2, 4, 8, 5, 7, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 5) == 424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 1, 9, 2, 4, 8, 5, 7, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 5) == 424: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],x = 5) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],x = 5) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 5) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 5) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 1) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 1) == 74: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 1) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 1) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 1) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 1) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],x = 15) == 660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],x = 15) == 660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],x = 50) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],x = 50) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 1) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 1) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],x = 1000000) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],x = 1000000) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 2) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 2) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],x = 3) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],x = 3) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 1000000, 999999, 1000000, 999999],x = 1000000) == 3000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 1000000, 999999, 1000000, 999999],x = 1000000) == 3000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],x = 100) == 923
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],x = 100) == 923: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],x = 1) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],x = 1) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 5) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 5) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],x = 1000) == 9990955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],x = 1000) == 9990955: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 1) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 1) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 1000) == 9990945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 1000) == 9990945: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],x = 10) == 629
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],x = 10) == 629: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],x = 500000) == 3499991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],x = 500000) == 3499991: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],x = 5) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],x = 5) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],x = 3) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],x = 3) == 625: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 5) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 5) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],x = 500) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],x = 500) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 2, 4, 6, 7, 9, 8, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19, 20],x = 20) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 2, 4, 6, 7, 9, 8, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19, 20],x = 20) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2],x = 15) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2],x = 15) == 158: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],x = 25) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],x = 25) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989, 999988, 999987],x = 100000) == 12711020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989, 999988, 999987],x = 100000) == 12711020: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],x = 5) == 780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],x = 5) == 780: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 10) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 10) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23],x = 10) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23],x = 10) == 90: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],x = 1) == 11
    assert candidate(nums = [10, 13, 15, 17, 19],x = 10) == 64
    assert candidate(nums = [1, 2, 3, 4, 5, 6],x = 2) == 13
    assert candidate(nums = [10, 13, 14, 15, 19],x = 10) == 48
    assert candidate(nums = [5, 3, 2, 4, 6, 7, 8, 9],x = 4) == 29
    assert candidate(nums = [5, 5, 5, 5, 5, 5],x = 1) == 30
    assert candidate(nums = [10, 15, 20, 25, 30],x = 10) == 65
    assert candidate(nums = [1, 2, 3, 4, 5],x = 2) == 9
    assert candidate(nums = [7, 8, 9, 10, 11, 12],x = 7) == 32
    assert candidate(nums = [10, 15, 20, 25, 30],x = 7) == 72
    assert candidate(nums = [2, 3, 6, 1, 9, 2],x = 5) == 13
    assert candidate(nums = [7, 11, 13, 14, 15],x = 3) == 54
    assert candidate(nums = [1, 1, 1, 1, 1],x = 10) == 5
    assert candidate(nums = [5, 3, 8, 9, 2, 4],x = 6) == 17
    assert candidate(nums = [2, 4, 6, 8],x = 3) == 20
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 2) == 420
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 3) == 420
    assert candidate(nums = [100000, 100001, 100002, 100003, 100004, 100005, 100006, 100007, 100008, 100009],x = 50000) == 550045
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 150) == 5500
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 3) == 240
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9],x = 3) == 73
    assert candidate(nums = [1, 3, 2, 8, 7, 4, 6, 9, 5, 10],x = 6) == 30
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],x = 5) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 7) == 119
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],x = 10) == 520
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],x = 30) == 239
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 1) == 191
    assert candidate(nums = [12, 17, 18, 13, 20, 21, 16, 19, 14, 15],x = 8) == 98
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 10) == 420
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],x = 2) == 409
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],x = 7) == 632
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 15) == 240
    assert candidate(nums = [10, 30, 20, 40, 50, 70, 60, 90, 80, 100, 120, 110, 140, 130, 160, 150, 180, 170, 200, 190],x = 20) == 2100
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],x = 5) == 124
    assert candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11],x = 2) == 54
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],x = 100000) == 6399979
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],x = 20) == 109
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 39
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],x = 10) == 400
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],x = 1000) == 5994985
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],x = 2) == 10
    assert candidate(nums = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009],x = 100000) == 9100045
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 2) == 100
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],x = 500000) == 5499975
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 1) == 46
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],x = 15) == 2100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == 11
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],x = 10) == 40
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 10
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 500000) == 5499969
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],x = 2) == 256
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 100) == 5500
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],x = 100000) == 1980468
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1000001, 1000010, 1000100, 1001000, 1010000, 1100000],x = 1000000) == 5222221
    assert candidate(nums = [500000, 499999, 499998, 499997, 499996, 499995, 499994, 499993, 499992, 499991, 499990, 499989, 499988, 499987, 499986, 499985, 499984, 499983, 499982, 499981],x = 100000) == 8099810
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 100000) == 9099945
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 3) == 159
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],x = 20) == 308
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 240
    assert candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62],x = 7) == 543
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 2) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 39
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],x = 25) == 675
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996],x = 500000) == 2999994
    assert candidate(nums = [2, 3, 6, 1, 9, 2, 4, 8, 5, 7, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],x = 5) == 424
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],x = 5) == 400
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 10) == 50
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 5) == 225
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 1) == 74
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 1) == 225
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 1) == 30
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 1) == 101
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 3) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],x = 15) == 660
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],x = 50) == 2200
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 1) == 101
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 15) == 30
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 1) == 20
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],x = 1000000) == 10000000
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 2) == 110
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],x = 3) == 98
    assert candidate(nums = [1000000, 999999, 1000000, 999999, 1000000, 999999],x = 1000000) == 3000000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 10
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],x = 100) == 923
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],x = 1) == 132
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 5) == 110
    assert candidate(nums = [4, 2, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 240
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],x = 1000) == 9990955
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 10) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 1) == 150
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 10) == 100
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],x = 1000) == 9990945
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 31
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],x = 10) == 629
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],x = 500000) == 3499991
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],x = 5) == 144
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],x = 3) == 625
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 5) == 73
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],x = 500) == 12000
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 7, 9, 8, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19, 20],x = 20) == 115
    assert candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2],x = 15) == 158
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],x = 25) == 2100
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 3) == 18
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989, 999988, 999987],x = 100000) == 12711020
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],x = 5) == 780
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],x = 10) == 225
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23],x = 10) == 90


