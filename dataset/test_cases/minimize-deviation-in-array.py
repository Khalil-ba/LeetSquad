def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000]) == 1953123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000]) == 1953123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 6, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 6, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 7, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 7, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 10, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 10, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 11, 24, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 11, 24, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1000000000]) == 1953123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1000000000]) == 1953123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 1, 3, 4, 2, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 1, 3, 4, 2, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 24, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 24, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 10, 18, 24]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 10, 18, 24]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 5, 20, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 5, 20, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 4, 1, 8, 12]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 4, 1, 8, 12]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 10, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 10, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 4, 3, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 4, 3, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 4, 3, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 4, 3, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 9, 16]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 9, 16]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 17, 100, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 17, 100, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == 1717
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == 1717: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 1000000000, 999999998, 1000000001, 999999997, 1000000002]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 1000000000, 999999998, 1000000001, 999999997, 1000000002]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 23, 31, 37, 41, 43, 47, 53, 59, 61]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 23, 31, 37, 41, 43, 47, 53, 59, 61]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 765432099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 765432099: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 14, 18, 26, 34, 42, 50, 58, 66, 74]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 14, 18, 26, 34, 42, 50, 58, 66, 74]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [64, 32, 16, 8, 4, 2, 1, 2, 4, 8, 16, 32, 64]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [64, 32, 16, 8, 4, 2, 1, 2, 4, 8, 16, 32, 64]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 500000000, 3, 333333333, 4, 250000000, 5, 200000000]) == 333333331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 500000000, 3, 333333333, 4, 250000000, 5, 200000000]) == 333333331: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == 187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == 187: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000]) == 31250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000]) == 31250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 456789123, 321987654, 654321987, 789123456]) == 740740743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 456789123, 321987654, 654321987, 789123456]) == 740740743: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 2000000000, 3, 3000000000, 4, 4000000000, 5, 5000000000, 6, 6000000000, 7, 7000000000, 8, 8000000000, 9, 9000000000]) == 17578123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 2000000000, 3, 3000000000, 4, 4000000000, 5, 5000000000, 6, 6000000000, 7, 7000000000, 8, 8000000000, 9, 9000000000]) == 17578123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 500000000, 3, 1500000000]) == 5859373
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 500000000, 3, 1500000000]) == 5859373: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]) == 169: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646, 9565938]) == 4782967
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646, 9565938]) == 4782967: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13579, 24681, 35791, 46813, 57915, 68137, 79159, 81379, 91591, 113791]) == 86633
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13579, 24681, 35791, 46813, 57915, 68137, 79159, 81379, 91591, 113791]) == 86633: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]) == 525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]) == 525: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 14337
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 14337: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625]) == 9765615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625]) == 9765615: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 59043
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 59043: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 522241
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 522241: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 999999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 999999997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 1953123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 1953123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 512, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 512, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 1953123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 1953123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2046, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1021
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2046, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1021: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 707
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 707: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 65: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 1000000000]) == 1953123
    assert candidate(nums = [3, 9, 6, 12]) == 3
    assert candidate(nums = [3, 9, 7, 3]) == 3
    assert candidate(nums = [2, 10, 8]) == 3
    assert candidate(nums = [5, 3, 11, 24, 2]) == 9
    assert candidate(nums = [1000000000, 1, 1000000000]) == 1953123
    assert candidate(nums = [1, 3, 5, 7, 9]) == 7
    assert candidate(nums = [15, 15, 15, 15]) == 0
    assert candidate(nums = [1, 2, 3, 4]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50]) == 15
    assert candidate(nums = [6, 1, 3, 4, 2, 8]) == 1
    assert candidate(nums = [8, 12, 24, 6]) == 1
    assert candidate(nums = [6, 10, 18, 24]) == 4
    assert candidate(nums = [4, 1, 5, 20, 3]) == 3
    assert candidate(nums = [7, 4, 1, 8, 12]) == 5
    assert candidate(nums = [10, 10, 10]) == 0
    assert candidate(nums = [3, 5, 6, 10, 15]) == 9
    assert candidate(nums = [10, 4, 3, 5]) == 2
    assert candidate(nums = [7, 4, 3, 7]) == 3
    assert candidate(nums = [1, 2, 9, 16]) == 7
    assert candidate(nums = [5, 17, 100, 1]) == 23
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 29
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 29
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 275
    assert candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919, 2020]) == 1717
    assert candidate(nums = [999999999, 1000000000, 999999998, 1000000001, 999999997, 1000000002]) == 5
    assert candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 4
    assert candidate(nums = [17, 23, 31, 37, 41, 43, 47, 53, 59, 61]) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 13
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 27
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 765432099
    assert candidate(nums = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 12500
    assert candidate(nums = [2, 14, 18, 26, 34, 42, 50, 58, 66, 74]) == 35
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 135
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 105
    assert candidate(nums = [64, 32, 16, 8, 4, 2, 1, 2, 4, 8, 16, 32, 64]) == 0
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 3
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78]) == 37
    assert candidate(nums = [1, 1000000000, 2, 500000000, 3, 333333333, 4, 250000000, 5, 200000000]) == 333333331
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == 187
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 17
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000]) == 31250
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 69
    assert candidate(nums = [123456789, 987654321, 456789123, 321987654, 654321987, 789123456]) == 740740743
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 143
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 0
    assert candidate(nums = [1, 1000000000, 2, 2000000000, 3, 3000000000, 4, 4000000000, 5, 5000000000, 6, 6000000000, 7, 7000000000, 8, 8000000000, 9, 9000000000]) == 17578123
    assert candidate(nums = [1, 1000000000, 2, 500000000, 3, 1500000000]) == 5859373
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 51
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]) == 169
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == 13
    assert candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646, 9565938]) == 4782967
    assert candidate(nums = [13579, 24681, 35791, 46813, 57915, 68137, 79159, 81379, 91591, 113791]) == 86633
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]) == 525
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 14337
    assert candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625]) == 9765615
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 17
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 59043
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 275
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 39
    assert candidate(nums = [13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 71
    assert candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 9
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 65
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 522241
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 21
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 999999997
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 85
    assert candidate(nums = [5, 15, 25, 35, 45, 55]) == 45
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 37
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 4
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995]) == 4
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 1953123
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 63
    assert candidate(nums = [1024, 2048, 512, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 1953123
    assert candidate(nums = [1023, 2046, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1021
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54]) == 27
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]) == 84
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 9
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]) == 0
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 707
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 65


