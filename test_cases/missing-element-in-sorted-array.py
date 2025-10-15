def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20],k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20],k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 15) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 15) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 12, 13, 15, 17],k = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 12, 13, 15, 17],k = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20],k = 100) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20],k = 100) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 8, 9],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 8, 9],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 8, 10, 12],k = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 8, 10, 12],k = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 11, 14, 17],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 11, 14, 17],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40],k = 15) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40],k = 15) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 6, 7, 8, 10],k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 6, 7, 8, 10],k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 7, 9, 10],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 7, 9, 10],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 7, 9, 10],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 7, 9, 10],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 10, 12],k = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 10, 12],k = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 605: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 8, 10, 13, 17, 22, 28, 35, 43],k = 30) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 8, 10, 13, 17, 22, 28, 35, 43],k = 30) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 104, 106, 108, 110, 112, 114, 116],k = 50) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 104, 106, 108, 110, 112, 114, 116],k = 50) == 158: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],k = 80) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],k = 80) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 40) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 40) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36],k = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36],k = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 9, 15, 22, 30, 39, 49, 60, 72, 85, 99, 114, 130, 147, 165, 184, 204, 225],k = 300) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 9, 15, 22, 30, 39, 49, 60, 72, 85, 99, 114, 130, 147, 165, 184, 204, 225],k = 300) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 25) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 25) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],k = 50) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],k = 50) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225],k = 50) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225],k = 50) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 5000) == 5012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 5000) == 5012: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 150) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 150) == 176: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 100) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 100) == 116: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65],k = 100) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65],k = 100) == 111: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61],k = 30) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61],k = 30) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 116: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 69, 70, 72, 73, 75, 76, 78, 79, 81, 82, 84, 85, 87, 88, 90, 91, 93, 94, 96, 97, 99, 100],k = 500) == 568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 69, 70, 72, 73, 75, 76, 78, 79, 81, 82, 84, 85, 87, 88, 90, 91, 93, 94, 96, 97, 99, 100],k = 500) == 568: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050],k = 5000) == 5100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050],k = 5000) == 5100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 16, 23, 31, 40, 50, 61, 73, 86, 100, 115, 131, 148, 166, 185, 205, 226, 248, 271, 295, 320, 346, 373, 401, 430, 460, 491, 523, 556, 590, 625, 661, 708, 756, 805, 855, 906, 958, 1011, 1065],k = 500) == 537
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 16, 23, 31, 40, 50, 61, 73, 86, 100, 115, 131, 148, 166, 185, 205, 226, 248, 271, 295, 320, 346, 373, 401, 430, 460, 491, 523, 556, 590, 625, 661, 708, 756, 805, 855, 906, 958, 1011, 1065],k = 500) == 537: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 10, 13, 17, 20, 24, 28, 32],k = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 10, 13, 17, 20, 24, 28, 32],k = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 16, 32, 64, 128],k = 100) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 16, 32, 64, 128],k = 100) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 8, 12, 16, 22, 30, 40, 52, 66, 82, 100, 120, 142, 166, 192],k = 150) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 8, 12, 16, 22, 30, 40, 52, 66, 82, 100, 120, 142, 166, 192],k = 150) == 169: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 150) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 150) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 554: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577, 626, 677, 730, 785, 842, 901, 962, 1025],k = 500) == 523
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577, 626, 677, 730, 785, 842, 901, 962, 1025],k = 500) == 523: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 25) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 25) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22],k = 50) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22],k = 50) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190],k = 150) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190],k = 150) == 167: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 1000) == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 1000) == 1010: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 104, 105, 107, 110, 112, 115, 117, 120, 123, 125, 127, 130],k = 50) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 104, 105, 107, 110, 112, 115, 117, 120, 123, 125, 127, 130],k = 50) == 164: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 100) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 100) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 13, 22, 33, 46, 61, 78, 97, 118, 141, 166, 193, 222, 253],k = 150) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 13, 22, 33, 46, 61, 78, 97, 118, 141, 166, 193, 222, 253],k = 150) == 161: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 8, 10, 15, 18],k = 20) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 8, 10, 15, 18],k = 20) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200],k = 120) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200],k = 120) == 154: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 100) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 100) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 75) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 75) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256],k = 150) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256],k = 150) == 164: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361],k = 200) == 214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361],k = 200) == 214: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102],k = 50) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102],k = 50) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 100) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 100) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199],k = 5000) == 5100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199],k = 5000) == 5100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 11, 20, 32, 47, 65],k = 20) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 11, 20, 32, 47, 65],k = 20) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 18, 26, 35, 45, 56, 68, 81, 95, 110, 126, 143, 161, 180, 200, 221, 243, 266, 290, 315, 341, 368, 396, 425, 455, 486, 518, 551],k = 300) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 18, 26, 35, 45, 56, 68, 81, 95, 110, 126, 143, 161, 180, 200, 221, 243, 266, 290, 315, 341, 368, 396, 425, 455, 486, 518, 551],k = 300) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 89, 103, 118, 134, 151, 169, 188, 208, 229],k = 100) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 89, 103, 118, 134, 151, 169, 188, 208, 229],k = 100) == 114: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990],k = 200) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990],k = 200) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577],k = 300) == 318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577],k = 300) == 318: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 5000) == 5012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 5000) == 5012: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 30) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 30) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 100) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 100) == 117: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 8, 12, 15],k = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 8, 12, 15],k = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 19, 29, 41, 55, 71, 89, 109, 131, 155, 181, 209, 239, 271, 305],k = 250) == 268
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 19, 29, 41, 55, 71, 89, 109, 131, 155, 181, 209, 239, 271, 305],k = 250) == 268: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 105, 107, 110, 113, 116, 119],k = 50) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 105, 107, 110, 113, 116, 119],k = 50) == 157: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506, 649, 816, 1009, 1229, 1479, 1759, 2071, 2416, 2796],k = 200) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506, 649, 816, 1009, 1229, 1479, 1759, 2071, 2416, 2796],k = 200) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54],k = 50) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54],k = 50) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 25, 45, 70, 100, 135, 175, 220, 270, 325, 385, 450, 520, 595, 675, 760, 850, 945, 1045, 1150],k = 500) == 522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 25, 45, 70, 100, 135, 175, 220, 270, 325, 385, 450, 520, 595, 675, 760, 850, 945, 1045, 1150],k = 500) == 522: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90],k = 50) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90],k = 50) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197],k = 100) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197],k = 100) == 111: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 7, 9, 11, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29],k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 7, 9, 11, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29],k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 399, 440, 483],k = 100) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 399, 440, 483],k = 100) == 114: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103, 118, 134, 151, 169, 188, 208, 229, 251],k = 150) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103, 118, 134, 151, 169, 188, 208, 229, 251],k = 150) == 166: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 30) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 30) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 16, 23, 31, 40, 50, 61, 73, 86, 100, 115, 131, 148],k = 100) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 16, 23, 31, 40, 50, 61, 73, 86, 100, 115, 131, 148],k = 100) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 19, 28, 39, 52, 67, 84, 103],k = 75) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 19, 28, 39, 52, 67, 84, 103],k = 75) == 87: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],k = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],k = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20],k = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20],k = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991, 1036],k = 750) == 790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991, 1036],k = 750) == 790: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 30) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 30) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 75) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 75) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 60) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 60) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 100) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 100) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90],k = 30) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90],k = 30) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 10, 15, 20, 25, 30, 35, 40],k = 30) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 10, 15, 20, 25, 30, 35, 40],k = 30) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000],k = 10000) == 11010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000],k = 10000) == 11010: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 15, 23, 33, 44, 56, 70, 86, 104, 124, 146, 170, 196],k = 200) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 15, 23, 33, 44, 56, 70, 86, 104, 124, 146, 170, 196],k = 200) == 215: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990],k = 500) == 532
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990],k = 500) == 532: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170],k = 20) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170],k = 20) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 400, 442],k = 400) == 421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 400, 442],k = 400) == 421: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103],k = 50) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103],k = 50) == 59: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 5, 10, 15, 20],k = 10) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 11
    assert candidate(nums = [10, 20, 30, 40, 50],k = 15) == 26
    assert candidate(nums = [10, 12, 13, 15, 17],k = 5) == 19
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 10
    assert candidate(nums = [1, 5, 10, 15, 20],k = 100) == 105
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 15
    assert candidate(nums = [1, 2, 4],k = 3) == 6
    assert candidate(nums = [1, 3, 5, 7],k = 4) == 8
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9],k = 4) == 11
    assert candidate(nums = [1, 3, 5, 7, 9],k = 2) == 4
    assert candidate(nums = [5, 6, 8, 10, 12],k = 7) == 16
    assert candidate(nums = [5, 8, 11, 14, 17],k = 10) == 19
    assert candidate(nums = [1, 3, 5, 7],k = 2) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10],k = 1) == 9
    assert candidate(nums = [10, 20, 30, 40],k = 15) == 26
    assert candidate(nums = [1, 2, 3, 4, 6, 7, 8, 10],k = 4) == 12
    assert candidate(nums = [4, 7, 9, 10],k = 3) == 8
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 15
    assert candidate(nums = [4, 7, 9, 10],k = 1) == 5
    assert candidate(nums = [1, 3, 5, 7, 9],k = 5) == 10
    assert candidate(nums = [5, 8, 10, 12],k = 5) == 13
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 6
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 605
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 37
    assert candidate(nums = [5, 6, 8, 10, 13, 17, 22, 28, 35, 43],k = 30) == 44
    assert candidate(nums = [100, 102, 104, 106, 108, 110, 112, 114, 116],k = 50) == 158
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],k = 80) == 100
    assert candidate(nums = [1, 5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 40) == 49
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36],k = 20) == 26
    assert candidate(nums = [1, 2, 5, 9, 15, 22, 30, 39, 49, 60, 72, 85, 99, 114, 130, 147, 165, 184, 204, 225],k = 300) == 320
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 25) == 38
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],k = 50) == 101
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 10) == 20
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 25) == 32
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225],k = 50) == 57
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 5000) == 5012
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 150) == 176
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 100) == 116
    assert candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65],k = 100) == 111
    assert candidate(nums = [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61],k = 30) == 44
    assert candidate(nums = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 116
    assert candidate(nums = [1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 69, 70, 72, 73, 75, 76, 78, 79, 81, 82, 84, 85, 87, 88, 90, 91, 93, 94, 96, 97, 99, 100],k = 500) == 568
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050],k = 5000) == 5100
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36],k = 5) == 8
    assert candidate(nums = [10, 16, 23, 31, 40, 50, 61, 73, 86, 100, 115, 131, 148, 166, 185, 205, 226, 248, 271, 295, 320, 346, 373, 401, 430, 460, 491, 523, 556, 590, 625, 661, 708, 756, 805, 855, 906, 958, 1011, 1065],k = 500) == 537
    assert candidate(nums = [3, 6, 10, 13, 17, 20, 24, 28, 32],k = 20) == 30
    assert candidate(nums = [1, 4, 8, 16, 32, 64, 128],k = 100) == 106
    assert candidate(nums = [5, 6, 8, 12, 16, 22, 30, 40, 52, 66, 82, 100, 120, 142, 166, 192],k = 150) == 169
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 150) == 200
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 554
    assert candidate(nums = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577, 626, 677, 730, 785, 842, 901, 962, 1025],k = 500) == 523
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 25) == 125
    assert candidate(nums = [2, 6, 10, 14, 18, 22],k = 50) == 57
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190],k = 150) == 167
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 1000) == 1010
    assert candidate(nums = [100, 101, 102, 104, 105, 107, 110, 112, 115, 117, 120, 123, 125, 127, 130],k = 50) == 164
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 100) == 120
    assert candidate(nums = [1, 6, 13, 22, 33, 46, 61, 78, 97, 118, 141, 166, 193, 222, 253],k = 150) == 161
    assert candidate(nums = [1, 3, 6, 8, 10, 15, 18],k = 20) == 27
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200],k = 120) == 154
    assert candidate(nums = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 100) == 106
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 75) == 84
    assert candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256],k = 150) == 164
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361],k = 200) == 214
    assert candidate(nums = [3, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102],k = 50) == 63
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 100) == 130
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199],k = 5000) == 5100
    assert candidate(nums = [2, 5, 11, 20, 32, 47, 65],k = 20) == 25
    assert candidate(nums = [5, 11, 18, 26, 35, 45, 56, 68, 81, 95, 110, 126, 143, 161, 180, 200, 221, 243, 266, 290, 315, 341, 368, 396, 425, 455, 486, 518, 551],k = 300) == 325
    assert candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 89, 103, 118, 134, 151, 169, 188, 208, 229],k = 100) == 114
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990],k = 200) == 220
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 10
    assert candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577],k = 300) == 318
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 5000) == 5012
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 30) == 40
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 100) == 117
    assert candidate(nums = [1, 3, 6, 8, 12, 15],k = 20) == 26
    assert candidate(nums = [5, 11, 19, 29, 41, 55, 71, 89, 109, 131, 155, 181, 209, 239, 271, 305],k = 250) == 268
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 115
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 150
    assert candidate(nums = [100, 102, 105, 107, 110, 113, 116, 119],k = 50) == 157
    assert candidate(nums = [1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506, 649, 816, 1009, 1229, 1479, 1759, 2071, 2416, 2796],k = 200) == 208
    assert candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54],k = 50) == 60
    assert candidate(nums = [10, 25, 45, 70, 100, 135, 175, 220, 270, 325, 385, 450, 520, 595, 675, 760, 850, 945, 1045, 1150],k = 500) == 522
    assert candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90],k = 50) == 60
    assert candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197],k = 100) == 111
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 9, 11, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29],k = 5) == 17
    assert candidate(nums = [7, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 399, 440, 483],k = 100) == 114
    assert candidate(nums = [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103, 118, 134, 151, 169, 188, 208, 229, 251],k = 150) == 166
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 30) == 42
    assert candidate(nums = [1, 5, 10, 16, 23, 31, 40, 50, 61, 73, 86, 100, 115, 131, 148],k = 100) == 112
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 30
    assert candidate(nums = [5, 11, 19, 28, 39, 52, 67, 84, 103],k = 75) == 87
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],k = 25) == 32
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 62
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20],k = 15) == 30
    assert candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407, 436, 466, 497, 529, 562, 596, 631, 667, 704, 742, 781, 821, 862, 904, 947, 991, 1036],k = 750) == 790
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 30) == 47
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 75) == 85
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 60) == 90
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 100) == 110
    assert candidate(nums = [5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90],k = 30) == 40
    assert candidate(nums = [2, 5, 10, 15, 20, 25, 30, 35, 40],k = 30) == 39
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000],k = 10000) == 11010
    assert candidate(nums = [1, 4, 8, 15, 23, 33, 44, 56, 70, 86, 104, 124, 146, 170, 196],k = 200) == 215
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990],k = 500) == 532
    assert candidate(nums = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170],k = 20) == 124
    assert candidate(nums = [3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 400, 442],k = 400) == 421
    assert candidate(nums = [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103],k = 50) == 59


