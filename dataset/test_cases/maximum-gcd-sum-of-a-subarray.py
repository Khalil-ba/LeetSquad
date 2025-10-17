def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],k = 3) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],k = 3) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],k = 3) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],k = 3) == 375: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 3) == 4000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 3) == 4000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4, 4, 4, 2],k = 2) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4, 4, 4, 2],k = 2) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000],k = 2) == 3000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000],k = 2) == 3000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 9, 4],k = 1) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 9, 4],k = 1) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 4) == 4000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 4) == 4000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 3) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 3) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 5) == 5000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 5) == 5000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 24, 40, 60, 120],k = 4) == 1056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 24, 40, 60, 120],k = 4) == 1056: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 12) == 2100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 12) == 2100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 15) == 20000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 15) == 20000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999983, 999989, 999991, 999997, 1000003, 1000009, 1000013, 1000021, 1000033, 1000037],k = 9) == 10000076
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999983, 999989, 999991, 999997, 1000003, 1000009, 1000013, 1000021, 1000033, 1000037],k = 9) == 10000076: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 5250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 5250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 9) == 561055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 9) == 561055: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 123456, 123456, 123456, 123456, 123456, 123456, 123456],k = 3) == 121931071488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 123456, 123456, 123456, 123456, 123456, 123456, 123456],k = 3) == 121931071488: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 7) == 780000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 7) == 780000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 8) == 5880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 8) == 5880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 3) == 3025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 3) == 3025: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 5) == 810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 5) == 810: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 7) == 3520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 7) == 3520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 10) == 10000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 10) == 10000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 6) == 1836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 6) == 1836: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 2890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 2890: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 2) == 4000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 2) == 4000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 4) == 280000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 4) == 280000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 12) == 120000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 12) == 120000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 6) == 780000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 6) == 780000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 11) == 1890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 11) == 1890: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 4) == 12375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 4) == 12375: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 6) == 3520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 6) == 3520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 5) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 5) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24, 30],k = 3) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24, 30],k = 3) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256],k = 4) == 15360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256],k = 4) == 15360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 550000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 550000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],k = 9) == 7680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],k = 9) == 7680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 35, 42, 70, 105, 140],k = 2) == 11025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 35, 42, 70, 105, 140],k = 2) == 11025: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 7) == 639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 7) == 639: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 8) == 840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 8) == 840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30],k = 4) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30],k = 4) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255],k = 7) == 34680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255],k = 7) == 34680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 20) == 3380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 20) == 3380: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 5) == 5000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 5) == 5000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 7) == 2582
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 7) == 2582: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 7) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 7) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425],k = 15) == 93925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425],k = 15) == 93925: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24, 27, 30],k = 3) == 441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24, 27, 30],k = 3) == 441: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39],k = 4) == 765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39],k = 4) == 765: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230],k = 4) == 29095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230],k = 4) == 29095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375],k = 10) == 75000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375],k = 10) == 75000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],k = 5) == 550000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],k = 5) == 550000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 20, 24, 30],k = 3) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 20, 24, 30],k = 3) == 184: {e}')
    
    total += 1
    try:
        result = candidate(nums = [210, 231, 273, 308, 364, 399, 462, 504, 546, 572],k = 4) == 40131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [210, 231, 273, 308, 364, 399, 462, 504, 546, 572],k = 4) == 40131: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 6) == 561055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 6) == 561055: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23],k = 5) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23],k = 5) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36],k = 3) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36],k = 3) == 756: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240],k = 4) == 32400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240],k = 4) == 32400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 2) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 2) == 129: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 9) == 25410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 9) == 25410: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 5) == 280000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 5) == 280000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 3) == 4455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 3) == 4455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 10) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 10) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24, 27, 30],k = 3) == 441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24, 27, 30],k = 3) == 441: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 6) == 1375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 6) == 1375: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995],k = 5) == 4999985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995],k = 5) == 4999985: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 42, 60, 90, 120, 150, 180, 210, 240, 270],k = 4) == 39600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 42, 60, 90, 120, 150, 180, 210, 240, 270],k = 4) == 39600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 24, 30, 36],k = 3) == 648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 24, 30, 36],k = 3) == 648: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],k = 3) == 7920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],k = 3) == 7920: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 13) == 35490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 13) == 35490: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 639: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],k = 5) == 64304361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],k = 5) == 64304361: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 5) == 9295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 5) == 9295: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],k = 3) == 9999945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],k = 3) == 9999945: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 5) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 5) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310],k = 5) == 52855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310],k = 5) == 52855: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 8) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 8) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 3) == 7000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 3) == 7000000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 8) == 6655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 8) == 6655: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 5250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 5250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 15) == 10290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 15) == 10290: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 10, 10, 10, 10],k = 3) == 500
    assert candidate(nums = [5, 10, 15, 20, 25],k = 3) == 375
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 3) == 4000000000000
    assert candidate(nums = [2, 1, 4, 4, 4, 2],k = 2) == 48
    assert candidate(nums = [1000000, 1000000, 1000000],k = 2) == 3000000000000
    assert candidate(nums = [7, 3, 9, 4],k = 1) == 81
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 4) == 4000000000000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [5, 5, 5, 5, 5],k = 3) == 125
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 5) == 5000000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6) == 120
    assert candidate(nums = [8, 12, 24, 40, 60, 120],k = 4) == 1056
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 12) == 2100000
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 15) == 20000000000000
    assert candidate(nums = [999983, 999989, 999991, 999997, 1000003, 1000009, 1000013, 1000021, 1000033, 1000037],k = 9) == 10000076
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 5250
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 9) == 561055
    assert candidate(nums = [123456, 123456, 123456, 123456, 123456, 123456, 123456, 123456],k = 3) == 121931071488
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 7) == 780000
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 8) == 5880
    assert candidate(nums = [3, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 3) == 3025
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 5) == 810
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 7) == 3520
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 55
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 10) == 10000000000000
    assert candidate(nums = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 6) == 1836
    assert candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 2890
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 2) == 4000000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 55
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 4) == 280000
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 12) == 120000000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 6) == 780000
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 11) == 1890
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 4) == 12375
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4) == 495
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 6) == 3520
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 5) == 160
    assert candidate(nums = [12, 15, 18, 21, 24, 30],k = 3) == 360
    assert candidate(nums = [8, 16, 32, 64, 128, 256],k = 4) == 15360
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 120
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 550000
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],k = 9) == 7680
    assert candidate(nums = [21, 35, 42, 70, 105, 140],k = 2) == 11025
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 7) == 639
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 8) == 840
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30],k = 4) == 1050
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255],k = 7) == 34680
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 5500
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 20) == 3380
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 5) == 5000000000000
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 7) == 2582
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 7) == 300
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 55
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425],k = 15) == 93925
    assert candidate(nums = [12, 15, 18, 21, 24, 27, 30],k = 3) == 441
    assert candidate(nums = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39],k = 4) == 765
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 12000
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230],k = 4) == 29095
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 120
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375],k = 10) == 75000
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],k = 5) == 550000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 120
    assert candidate(nums = [12, 15, 18, 20, 24, 30],k = 3) == 184
    assert candidate(nums = [210, 231, 273, 308, 364, 399, 462, 504, 546, 572],k = 4) == 40131
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 6) == 561055
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23],k = 5) == 98
    assert candidate(nums = [6, 12, 18, 24, 30, 36],k = 3) == 756
    assert candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240],k = 4) == 32400
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 2) == 129
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 9) == 25410
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 5) == 280000
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 3) == 4455
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 10) == 1300
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4) == 495
    assert candidate(nums = [12, 15, 18, 21, 24, 27, 30],k = 3) == 441
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 6) == 1375
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995],k = 5) == 4999985
    assert candidate(nums = [30, 42, 60, 90, 120, 150, 180, 210, 240, 270],k = 4) == 39600
    assert candidate(nums = [12, 15, 18, 24, 30, 36],k = 3) == 648
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],k = 3) == 7920
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 13) == 35490
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 639
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],k = 5) == 64304361
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 5) == 9295
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],k = 3) == 9999945
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 5) == 300
    assert candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310],k = 5) == 52855
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 8) == 3000
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 3) == 7000000000000
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 8) == 6655
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 5250
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 15) == 10290


