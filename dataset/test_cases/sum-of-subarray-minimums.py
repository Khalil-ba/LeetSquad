def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9]) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9]) == 157: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 4, 3]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 4, 3]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 4, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 4, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 81, 94, 43, 3]) == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 81, 94, 43, 3]) == 444: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 2, 4, 6]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 2, 4, 6]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10000, 9000, 8000, 7000, 6000]) == 110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10000, 9000, 8000, 7000, 6000]) == 110000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 4]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 4]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10000, 20000, 30000, 40000, 50000]) == 350000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10000, 20000, 30000, 40000, 50000]) == 350000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30000, 1, 30000, 2, 30000]) == 90016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30000, 1, 30000, 2, 30000]) == 90016: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1, 4, 5]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1, 4, 5]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1, 5, 4]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1, 5, 4]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 485: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30230: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 550000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 550000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10]) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10]) == 183: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 305: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 199: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 4960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 4960: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30000, 29999, 29998, 29997, 29996, 29995, 29994, 29993, 29992, 29991]) == 1649670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30000, 29999, 29998, 29997, 29996, 29995, 29994, 29993, 29992, 29991]) == 1649670: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 22100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 22100: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 2285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 2285: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 715: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 0]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 0]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 100000, 100000, 100000, 100000]) == 1500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 100000, 100000, 100000, 100000]) == 1500000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 4, 3, 2, 1]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 4, 3, 2, 1]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 3, 1, 6, 2, 8, 4, 5]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 3, 1, 6, 2, 8, 4, 5]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 8116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 8116: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 204: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29]) == 4561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29]) == 4561: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 1, 3, 2, 2, 1, 3, 1]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 1, 3, 2, 2, 1, 3, 1]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 7, 1, 6, 8, 2, 4, 9, 10]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 7, 1, 6, 8, 2, 4, 9, 10]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1555: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 2, 6, 2, 8, 2, 10]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 2, 6, 2, 8, 2, 10]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 6, 5, 4, 3, 2, 1]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 6, 5, 4, 3, 2, 1]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 197: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 4, 2, 1, 6, 7, 8, 9, 10]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 4, 2, 1, 6, 7, 8, 9, 10]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 2200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 2200000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 6800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 6800: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 516
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 516: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1]) == 50050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1]) == 50050: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 330: {e}')
    
    total += 1
    try:
        result = candidate(arr = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 3, 1, 2, 1, 3, 2, 1]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 3, 1, 2, 1, 3, 2, 1]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30000, 15000, 10000, 5000, 1, 5000, 10000, 15000, 30000]) == 220025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30000, 15000, 10000, 5000, 1, 5000, 10000, 15000, 30000]) == 220025: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]) == 9400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]) == 9400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2870
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2870: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 131: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 22000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30000, 29999, 29998, 29997, 29996, 29995]) == 629930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30000, 29999, 29998, 29997, 29996, 29995]) == 629930: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30000, 1, 30000, 1, 30000, 1, 30000, 1, 30000, 1]) == 150050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30000, 1, 30000, 1, 30000, 1, 30000, 1, 30000, 1]) == 150050: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, 1, 200000, 2, 300000, 3, 400000, 4]) == 1000060
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, 1, 200000, 2, 300000, 3, 400000, 4]) == 1000060: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15000, 10000, 20000, 5000, 25000, 22500, 17500, 27500, 30000, 12500]) == 602500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15000, 10000, 20000, 5000, 25000, 22500, 17500, 27500, 30000, 12500]) == 602500: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [5, 4, 3, 2, 1]) == 35
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165
    assert candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9]) == 157
    assert candidate(arr = [9, 7, 5, 3, 1]) == 55
    assert candidate(arr = [10, 20, 30, 40, 50]) == 350
    assert candidate(arr = [1, 2, 2, 1]) == 13
    assert candidate(arr = [3, 1, 2, 4, 3]) == 27
    assert candidate(arr = [3, 1, 2, 4, 5]) == 30
    assert candidate(arr = [11, 81, 94, 43, 3]) == 444
    assert candidate(arr = [1]) == 1
    assert candidate(arr = [1, 1, 1, 1, 1]) == 15
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220
    assert candidate(arr = [1, 3, 5, 2, 4, 6]) == 49
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 110
    assert candidate(arr = [10000, 9000, 8000, 7000, 6000]) == 110000
    assert candidate(arr = [1, 2, 3, 4, 5]) == 35
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 385
    assert candidate(arr = [3, 1, 2, 4]) == 17
    assert candidate(arr = [3, 3, 3, 3, 3]) == 45
    assert candidate(arr = [10000, 20000, 30000, 40000, 50000]) == 350000
    assert candidate(arr = [1, 3, 5, 7, 9]) == 55
    assert candidate(arr = [30000, 1, 30000, 2, 30000]) == 90016
    assert candidate(arr = [3, 2, 1, 4, 5]) == 29
    assert candidate(arr = [1, 2, 1, 2, 1]) == 17
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 275
    assert candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == 700
    assert candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 155
    assert candidate(arr = [3, 2, 1, 5, 4]) == 29
    assert candidate(arr = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 485
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 680
    assert candidate(arr = [30000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30230
    assert candidate(arr = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 550000
    assert candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 94
    assert candidate(arr = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10]) == 183
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 210
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 305
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540
    assert candidate(arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 199
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 4960
    assert candidate(arr = [5, 4, 3, 2, 1]) == 35
    assert candidate(arr = [30000, 29999, 29998, 29997, 29996, 29995, 29994, 29993, 29992, 29991]) == 1649670
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 22100
    assert candidate(arr = [10, 20, 10, 30, 10, 40, 10, 50, 10]) == 550
    assert candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10]) == 140
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 2285
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 715
    assert candidate(arr = [5, 4, 3, 2, 1, 0]) == 35
    assert candidate(arr = [100000, 100000, 100000, 100000, 100000]) == 1500000
    assert candidate(arr = [1, 3, 2, 4, 5, 4, 3, 2, 1]) == 91
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1]) == 36
    assert candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 95
    assert candidate(arr = [9, 7, 3, 1, 6, 2, 8, 4, 5]) == 107
    assert candidate(arr = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 8116
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 204
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 240
    assert candidate(arr = [2, 3, 1, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29]) == 4561
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(arr = [2, 3, 1, 1, 3, 2, 2, 1, 3, 1]) == 68
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2200
    assert candidate(arr = [5, 3, 7, 1, 6, 8, 2, 4, 9, 10]) == 136
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
    assert candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 100
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1555
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 540
    assert candidate(arr = [2, 4, 2, 6, 2, 8, 2, 10]) == 92
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1]) == 84
    assert candidate(arr = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 197
    assert candidate(arr = [3, 5, 4, 2, 1, 6, 7, 8, 9, 10]) == 170
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1540
    assert candidate(arr = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 2200000
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 6800
    assert candidate(arr = [1, 3, 2, 4, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 516
    assert candidate(arr = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1]) == 50050
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 330
    assert candidate(arr = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1240
    assert candidate(arr = [1, 3, 2, 3, 1, 2, 1, 3, 2, 1]) == 68
    assert candidate(arr = [5, 3, 8, 6, 2, 7, 4, 1]) == 96
    assert candidate(arr = [30000, 15000, 10000, 5000, 1, 5000, 10000, 15000, 30000]) == 220025
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 170
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1240
    assert candidate(arr = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]) == 9400
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 125
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2870
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 131
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 22000
    assert candidate(arr = [30000, 29999, 29998, 29997, 29996, 29995]) == 629930
    assert candidate(arr = [30000, 1, 30000, 1, 30000, 1, 30000, 1, 30000, 1]) == 150050
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 600
    assert candidate(arr = [100000, 1, 200000, 2, 300000, 3, 400000, 4]) == 1000060
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 550
    assert candidate(arr = [15000, 10000, 20000, 5000, 25000, 22500, 17500, 27500, 30000, 12500]) == 602500


