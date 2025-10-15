def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 1, 12, 3, 7]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 1, 12, 3, 7]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 25, 25, 10]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 25, 25, 10]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 2, 3, 5, 4, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 2, 3, 5, 4, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 2, 3, 5, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 2, 3, 5, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 12, 1, 2, 5, 50, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 12, 1, 2, 5, 50, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 2, 3, 5, 4]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 2, 3, 5, 4]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 211: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000]) == 5500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000]) == 5500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 300000000, 200000000, 100000000]) == 2100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 300000000, 200000000, 100000000]) == 2100000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 5, 8, 9, 6, 4, 2, 3, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 5, 8, 9, 6, 4, 2, 3, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1810: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]) == 503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]) == 503: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1]) == 3000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1]) == 3000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 2, 3, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 2, 3, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 70, 80, 90, 100, 110]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 70, 80, 90, 100, 110]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) == 247: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 10500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 10500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 2, 3, 5, 4, 1, 8, 7, 9]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 2, 3, 5, 4, 1, 8, 7, 9]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 2325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 2325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 7000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 7000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1000000000, 1000000000]) == 3000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1000000000, 1000000000]) == 3000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4999999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4999999990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 17710
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 17710: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 100, 200, 300, 400, 500]) == 1515
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 100, 200, 300, 400, 500]) == 1515: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 5, 3, 1]) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 5, 3, 1]) == 159: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 10, 18, 33, 59, 107, 198, 374, 699, 1302, 2441, 4537, 8380, 15619, 29036, 54256, 100901]) == 217982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 10, 18, 33, 59, 107, 198, 374, 699, 1302, 2441, 4537, 8380, 15619, 29036, 54256, 100901]) == 217982: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33]) == 660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33]) == 660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 5, 8, 6, 9, 3, 4, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 5, 8, 6, 9, 3, 4, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 6000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 6000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 14, 21, 28, 35, 42, 49, 56, 63]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 14, 21, 28, 35, 42, 49, 56, 63]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 9, 7, 8, 6, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 9, 7, 8, 6, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == 5500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == 5500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 5, 1, 12, 3, 7]) == 38
    assert candidate(nums = [5, 5, 50]) == -1
    assert candidate(nums = [5, 5, 5]) == 15
    assert candidate(nums = [10, 5, 25, 25, 10]) == 75
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(nums = [3, 6, 2, 3, 5, 4, 1]) == 24
    assert candidate(nums = [3, 6, 2, 3, 5, 10]) == 29
    assert candidate(nums = [10, 20, 30, 40, 50]) == 150
    assert candidate(nums = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(nums = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30
    assert candidate(nums = [1, 12, 1, 2, 5, 50, 3]) == 12
    assert candidate(nums = [3, 6, 2, 3, 5, 4]) == 23
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [10, 5, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 31
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 211
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == -1
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(nums = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000]) == 5500000000
    assert candidate(nums = [1000000000, 500000000, 300000000, 200000000, 100000000]) == 2100000000
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 84
    assert candidate(nums = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [7, 10, 5, 8, 9, 6, 4, 2, 3, 1]) == 55
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1810
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 42
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 165
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 625
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]) == 503
    assert candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 143
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1]) == 3000000001
    assert candidate(nums = [100, 200, 300, 400, 500]) == 1500
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 209
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 275
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 165
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 225
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 240
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955
    assert candidate(nums = [3, 6, 2, 3, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 33
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110]) == 560
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 180
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
    assert candidate(nums = [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) == 247
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 10500
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(nums = [3, 6, 2, 3, 5, 4, 1, 8, 7, 9]) == 48
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 2325
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 32
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 7000000000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 12000
    assert candidate(nums = [100, 200, 300, 400, 500, 600]) == 2100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [1, 1000000000, 1000000000, 1000000000]) == 3000000001
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 209
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4999999990
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 17710
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 100, 200, 300, 400, 500]) == 1515
    assert candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 225
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 3, 1]) == 159
    assert candidate(nums = [1, 2, 3, 6, 10, 18, 33, 59, 107, 198, 374, 699, 1302, 2441, 4537, 8380, 15619, 29036, 54256, 100901]) == 217982
    assert candidate(nums = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33]) == 660
    assert candidate(nums = [7, 10, 5, 8, 6, 9, 3, 4, 2, 1]) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 1050
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(nums = [1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 6000000001
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1000
    assert candidate(nums = [7, 10, 14, 21, 28, 35, 42, 49, 56, 63]) == 325
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(nums = [1, 3, 2, 4, 5, 9, 7, 8, 6, 10]) == 55
    assert candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == 5500000000
    assert candidate(nums = [1, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1]) == 9


