def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 4) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 4) == 93: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 10, 11, 12, 13, 14, 15],k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 10, 11, 12, 13, 14, 15],k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 4],k = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 4],k = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 9) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 9) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3],k = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3],k = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 3, 4],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 3, 4],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 1],k = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 1],k = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 3, 1, 8, 7, 2, 4],k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 3, 1, 8, 7, 2, 4],k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127],k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127],k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 4, 3, 15],k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 4, 3, 15],k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1],k = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1],k = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 6) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 6) == 76: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 10) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 10) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638],k = 30) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638],k = 30) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 5) == 348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 5) == 348: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],k = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],k = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 8, 7, 3, 1, 1, 2, 2],k = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 8, 7, 3, 1, 1, 2, 2],k = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],k = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],k = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 234567891, 198765432, 345678912, 456789123, 567891234, 678912345, 789123456, 891234567],k = 25) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 234567891, 198765432, 345678912, 456789123, 567891234, 678912345, 789123456, 891234567],k = 25) == 88: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383],k = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383],k = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385, 32769, 65537, 131073, 262145, 524289, 1048577, 2097153],k = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385, 32769, 65537, 131073, 262145, 524289, 1048577, 2097153],k = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 9) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 9) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907],k = 25) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907],k = 25) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 13, 15, 31, 7, 63],k = 8) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 13, 15, 31, 7, 63],k = 8) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 256, 512, 1024, 2048, 4096],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 256, 512, 1024, 2048, 4096],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128],k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128],k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 20) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 20) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31],k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31],k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 15, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 15, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 15) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 15) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31],k = 6) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31],k = 6) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 8) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 8) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 20) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 20) == 229: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 15, 31, 63],k = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 15, 31, 63],k = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 9) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 9) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 13, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59],k = 8) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 13, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59],k = 8) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 18) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 18) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 10) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 10) == 67: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 3) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 3) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 10) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 10) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 12) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 12) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 14, 15],k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 14, 15],k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303],k = 20) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303],k = 20) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191],k = 14) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191],k = 14) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 219: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1],k = 10) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1],k = 10) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999937, 999999938, 999999939, 999999940, 999999941, 999999942, 999999943, 999999944, 999999945, 999999946],k = 40) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999937, 999999938, 999999939, 999999940, 999999941, 999999942, 999999943, 999999944, 999999945, 999999946],k = 40) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517],k = 20) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517],k = 20) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 285: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 12) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 12) == 345: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 17, 23, 30, 14, 11, 13, 19, 21, 22],k = 6) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 17, 23, 30, 14, 11, 13, 19, 21, 22],k = 6) == 87: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 25, 27, 30, 33, 34, 36, 40, 41, 42, 45, 48, 50, 51, 54, 57, 60, 62, 65, 66, 68, 72, 73, 74, 77, 80, 81, 82, 85, 88, 90, 93, 96, 98, 101, 102, 104, 105, 106, 108, 112, 113, 114, 117, 120, 122, 125, 126, 129, 130, 132, 135, 136, 138, 140, 141, 142, 144, 145, 146, 148, 150, 153, 154, 156, 159, 160, 162, 165, 168, 170, 171, 172, 174, 177, 180, 182, 185, 186, 188, 190, 192, 193, 194, 195, 196, 198, 200, 201, 204, 205, 208, 210, 213, 216, 218, 219, 220, 222, 224, 225, 226, 228, 230, 231, 232, 234, 237, 240, 242, 243, 244, 246, 248, 249, 250, 252, 255],k = 6) == 13945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 25, 27, 30, 33, 34, 36, 40, 41, 42, 45, 48, 50, 51, 54, 57, 60, 62, 65, 66, 68, 72, 73, 74, 77, 80, 81, 82, 85, 88, 90, 93, 96, 98, 101, 102, 104, 105, 106, 108, 112, 113, 114, 117, 120, 122, 125, 126, 129, 130, 132, 135, 136, 138, 140, 141, 142, 144, 145, 146, 148, 150, 153, 154, 156, 159, 160, 162, 165, 168, 170, 171, 172, 174, 177, 180, 182, 185, 186, 188, 190, 192, 193, 194, 195, 196, 198, 200, 201, 204, 205, 208, 210, 213, 216, 218, 219, 220, 222, 224, 225, 226, 228, 230, 231, 232, 234, 237, 240, 242, 243, 244, 246, 248, 249, 250, 252, 255],k = 6) == 13945: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12],k = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12],k = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 2) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 2) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 12) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 12) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431],k = 25) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431],k = 25) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 5, 5, 5, 7, 7, 7],k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 5, 5, 5, 7, 7, 7],k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 25) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 25) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 12) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 12) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],k = 5) == 636
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],k = 5) == 636: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 9, 7, 11],k = 4) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 9, 7, 11],k = 4) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 22) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 22) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255],k = 10) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255],k = 10) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 4) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 4) == 247: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967295],k = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967295],k = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98304, 49152, 24576, 12288, 6144, 3072, 1536, 768, 384, 192, 96, 48, 24, 12, 6, 3, 1, 1, 1, 1],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98304, 49152, 24576, 12288, 6144, 3072, 1536, 768, 384, 192, 96, 48, 24, 12, 6, 3, 1, 1, 1, 1],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 12) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 12) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180],k = 4) == 239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180],k = 4) == 239: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 8) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [2, 4, 8, 16],k = 3) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 4) == 93
    assert candidate(nums = [1, 2, 4, 8, 16, 32],k = 3) == 0
    assert candidate(nums = [9, 10, 11, 12, 13, 14, 15],k = 7) == 7
    assert candidate(nums = [1, 1, 2, 3, 4],k = 2) == 16
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 9) == 72
    assert candidate(nums = [5, 1, 1],k = 10) == 0
    assert candidate(nums = [31, 14, 7, 3],k = 6) == 11
    assert candidate(nums = [1, 3, 5, 7],k = 4) == 11
    assert candidate(nums = [3, 1, 2, 5, 3, 4],k = 4) == 4
    assert candidate(nums = [7, 8, 9],k = 5) == 3
    assert candidate(nums = [1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [31, 14, 7, 1],k = 8) == 5
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 1],k = 3) == 5
    assert candidate(nums = [6, 5, 3, 1, 8, 7, 2, 4],k = 6) == 1
    assert candidate(nums = [7, 7, 7, 7],k = 5) == 1
    assert candidate(nums = [1023, 511, 255, 127],k = 10) == 16
    assert candidate(nums = [8, 8, 8, 8],k = 4) == 0
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 3) == 0
    assert candidate(nums = [7, 10, 4, 3, 15],k = 5) == 14
    assert candidate(nums = [31, 15, 7, 3, 1],k = 8) == 6
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 6) == 76
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 10) == 64
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 15) == 21
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638],k = 30) == 100
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 5) == 348
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],k = 10) == 25
    assert candidate(nums = [15, 8, 7, 3, 1, 1, 2, 2],k = 4) == 21
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 10) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],k = 4) == 22
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 209
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 200
    assert candidate(nums = [123456789, 987654321, 234567891, 198765432, 345678912, 456789123, 567891234, 678912345, 789123456, 891234567],k = 25) == 88
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383],k = 15) == 25
    assert candidate(nums = [1, 5, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385, 32769, 65537, 131073, 262145, 524289, 1048577, 2097153],k = 18) == 0
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 9) == 72
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 25) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907],k = 25) == 140
    assert candidate(nums = [5, 13, 15, 31, 7, 63],k = 8) == 19
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],k = 10) == 36
    assert candidate(nums = [128, 256, 512, 1024, 2048, 4096],k = 7) == 0
    assert candidate(nums = [31, 14, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128],k = 7) == 7
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 20) == 100
    assert candidate(nums = [1023, 511, 255, 127, 63, 31],k = 10) == 36
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [29, 15, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 12
    assert candidate(nums = [5, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 15) == 36
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31],k = 6) == 55
    assert candidate(nums = [100, 200, 300, 400, 500],k = 8) == 10
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 7) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 15) == 0
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 20) == 229
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 6) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 44
    assert candidate(nums = [3, 7, 15, 31, 63],k = 5) == 24
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 9) == 72
    assert candidate(nums = [5, 7, 13, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59],k = 8) == 73
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 18) == 120
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 10) == 67
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 3) == 48
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 10) == 64
    assert candidate(nums = [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 12) == 64
    assert candidate(nums = [7, 11, 13, 14, 15],k = 5) == 25
    assert candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303],k = 20) == 100
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191],k = 14) == 91
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 8) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 219
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1],k = 10) == 28
    assert candidate(nums = [10, 20, 30, 40, 50],k = 5) == 16
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 209
    assert candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],k = 5) == 1
    assert candidate(nums = [999999937, 999999938, 999999939, 999999940, 999999941, 999999942, 999999943, 999999944, 999999945, 999999946],k = 40) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 14) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 7) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517],k = 20) == 256
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 10) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 44
    assert candidate(nums = [2, 4, 8, 16, 32],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 285
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 12) == 345
    assert candidate(nums = [29, 17, 23, 30, 14, 11, 13, 19, 21, 22],k = 6) == 87
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 10) == 0
    assert candidate(nums = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 25, 27, 30, 33, 34, 36, 40, 41, 42, 45, 48, 50, 51, 54, 57, 60, 62, 65, 66, 68, 72, 73, 74, 77, 80, 81, 82, 85, 88, 90, 93, 96, 98, 101, 102, 104, 105, 106, 108, 112, 113, 114, 117, 120, 122, 125, 126, 129, 130, 132, 135, 136, 138, 140, 141, 142, 144, 145, 146, 148, 150, 153, 154, 156, 159, 160, 162, 165, 168, 170, 171, 172, 174, 177, 180, 182, 185, 186, 188, 190, 192, 193, 194, 195, 196, 198, 200, 201, 204, 205, 208, 210, 213, 216, 218, 219, 220, 222, 224, 225, 226, 228, 230, 231, 232, 234, 237, 240, 242, 243, 244, 246, 248, 249, 250, 252, 255],k = 6) == 13945
    assert candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513],k = 7) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 7) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12],k = 5) == 24
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 12) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 1
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],k = 15) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 2) == 100
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 12) == 45
    assert candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431],k = 25) == 49
    assert candidate(nums = [3, 3, 3, 5, 5, 5, 7, 7, 7],k = 4) == 9
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 25) == 100
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 12) == 170
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],k = 5) == 636
    assert candidate(nums = [5, 3, 9, 7, 11],k = 4) == 25
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 16
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 22) == 0
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255],k = 10) == 28
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 4) == 247
    assert candidate(nums = [33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967295],k = 30) == 15
    assert candidate(nums = [98304, 49152, 24576, 12288, 6144, 3072, 1536, 768, 384, 192, 96, 48, 24, 12, 6, 3, 1, 1, 1, 1],k = 12) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 12) == 100
    assert candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 15) == 0
    assert candidate(nums = [8, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180],k = 4) == 239
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 8) == 0


