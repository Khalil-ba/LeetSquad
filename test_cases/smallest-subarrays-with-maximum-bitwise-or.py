def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907, 953, 476, 238, 119, 59, 29, 14, 7, 3, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907, 953, 476, 238, 119, 59, 29, 14, 7, 3, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128]) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128]) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1]) == [1, 2, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1]) == [1, 2, 1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 1073741823, 1073741823]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 1073741823, 1073741823]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 7, 9]) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 7, 9]) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1]) == [4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1]) == [4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [8, 7, 6, 5, 4, 3, 2, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [8, 7, 6, 5, 4, 3, 2, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 2, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 2, 1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 0]) == [4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 0]) == [4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 4, 7, 8, 5, 6, 9]) == [7, 6, 5, 4, 3, 2, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 4, 7, 8, 5, 6, 9]) == [7, 6, 5, 4, 3, 2, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == [1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == [1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1023]) == [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1023]) == [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4, 2, 1]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4, 2, 1]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]) == [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]) == [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]) == [1, 2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]) == [1, 2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]) == [1, 1, 1, 4, 3, 2, 1, 1, 1, 4, 3, 2, 1, 1, 1, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]) == [1, 1, 1, 4, 3, 2, 1, 1, 1, 4, 3, 2, 1, 1, 1, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 511, 255, 127, 63]) == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 511, 255, 127, 63]) == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == [1, 2, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == [1, 2, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == [33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == [33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014]) == [1, 2, 3, 2, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014]) == [1, 2, 3, 2, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [7, 6, 5, 4, 3, 2, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [7, 6, 5, 4, 3, 2, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 2, 3, 7, 5, 1, 4, 9, 10]) == [4, 8, 7, 6, 5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 2, 3, 7, 5, 1, 4, 9, 10]) == [4, 8, 7, 6, 5, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 0, 2047, 0, 4095, 0, 8191, 0, 16383, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 0, 2047, 0, 4095, 0, 8191, 0, 16383, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 3, 12, 7, 9, 1, 5, 11, 6, 4, 10, 2, 14, 0, 13]) == [2, 1, 2, 2, 2, 4, 3, 2, 2, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 3, 12, 7, 9, 1, 5, 11, 6, 4, 10, 2, 14, 0, 13]) == [2, 1, 2, 2, 2, 4, 3, 2, 2, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == [4, 5, 4, 4, 4, 3, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == [4, 5, 4, 4, 4, 3, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31]) == [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31]) == [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 8, 4, 2, 1, 32, 64, 128, 256, 512]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 8, 4, 2, 1, 32, 64, 128, 256, 512]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == [1, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == [1, 8, 7, 6, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 7, 4, 6, 5, 0, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 7, 4, 6, 5, 0, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 1, 7, 5, 11, 13, 15, 8, 12, 14, 6, 10, 2, 4, 0]) == [4, 5, 4, 3, 2, 2, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 1, 7, 5, 11, 13, 15, 8, 12, 14, 6, 10, 2, 4, 0]) == [4, 5, 4, 3, 2, 2, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == [8, 7, 6, 5, 4, 3, 2, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == [8, 7, 6, 5, 4, 3, 2, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 7, 3, 1, 14, 6, 2, 0, 13, 5, 1, 0, 9, 3, 1, 0, 8, 2, 0, 7]) == [1, 4, 3, 2, 5, 4, 3, 7, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 7, 3, 1, 14, 6, 2, 0, 13, 5, 1, 0, 9, 3, 1, 0, 8, 2, 0, 7]) == [1, 4, 3, 2, 5, 4, 3, 7, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 2, 9, 8, 7, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 2, 9, 8, 7, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]) == [9, 8, 7, 6, 5, 4, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]) == [9, 8, 7, 6, 5, 4, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 128, 64, 32, 16, 8, 4, 2, 1, 256, 512, 1024, 2048, 4096]) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 128, 64, 32, 16, 8, 4, 2, 1, 256, 512, 1024, 2048, 4096]) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3, 1, 0, 1, 3, 7, 14, 31, 0, 1, 3, 7, 14, 31, 0, 1, 3, 7, 14, 31]) == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3, 1, 0, 1, 3, 7, 14, 31, 0, 1, 3, 7, 14, 31, 0, 1, 3, 7, 14, 31]) == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == [1, 1, 1, 4, 3, 2, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == [1, 1, 1, 4, 3, 2, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 1, 3, 1, 0, 2, 1, 3, 1, 0, 2, 1, 3, 1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 1, 3, 1, 0, 2, 1, 3, 1, 0, 2, 1, 3, 1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 14, 23, 42, 67, 98, 132, 175, 220, 270, 325, 385, 450, 520]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 14, 23, 42, 67, 98, 132, 175, 220, 270, 325, 385, 450, 520]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 255, 128, 64, 32, 16, 8, 4, 2, 1, 255, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 255, 128, 64, 32, 16, 8, 4, 2, 1, 255, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == [1, 2, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == [1, 2, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1, 2147483647, 2, 2147483647, 3, 2147483647, 4, 2147483647, 5]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1, 2147483647, 2, 2147483647, 3, 2147483647, 4, 2147483647, 5]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907, 953, 476, 238, 119, 59, 29, 14, 7, 3, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907, 953, 476, 238, 119, 59, 29, 14, 7, 3, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 1, 2, 3, 0, 1, 2]) == [3, 2, 1, 2, 2, 2, 1, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 1, 2, 3, 0, 1, 2]) == [3, 2, 1, 2, 2, 2, 1, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 63, 31, 15, 7, 3, 1, 127, 63, 31, 15, 7, 3, 1, 255, 127, 63, 31, 15, 7, 3, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 63, 31, 15, 7, 3, 1, 127, 63, 31, 15, 7, 3, 1, 255, 127, 63, 31, 15, 7, 3, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 987654320, 987654319, 987654318, 987654317, 987654316, 987654315, 987654314, 987654313, 987654312]) == [3, 2, 1, 2, 3, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 987654320, 987654319, 987654318, 987654317, 987654316, 987654315, 987654314, 987654313, 987654312]) == [3, 2, 1, 2, 3, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == [3, 2, 1, 2, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == [3, 2, 1, 2, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0, 2147483647, 0, 2147483647, 0, 2147483647, 0, 2147483647, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0, 2147483647, 0, 2147483647, 0, 2147483647, 0, 2147483647, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]) == [1, 2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]) == [1, 2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 5, 7, 9]) == [1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 5, 7, 9]) == [1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907, 953, 476, 238, 119, 59, 29, 14, 7, 3, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1]
    assert candidate(nums = [8, 16, 32, 64, 128]) == [5, 4, 3, 2, 1]
    assert candidate(nums = [1, 0, 1, 0, 1]) == [1, 2, 1, 2, 1]
    assert candidate(nums = [1073741823, 1073741823, 1073741823]) == [1, 1, 1]
    assert candidate(nums = [3, 1, 5, 7, 9]) == [5, 4, 3, 2, 1]
    assert candidate(nums = [8, 4, 2, 1]) == [4, 3, 2, 1]
    assert candidate(nums = [1, 3, 5, 7, 9]) == [5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [8, 7, 6, 5, 4, 3, 2, 3, 2, 1]
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 2, 1, 2, 1]
    assert candidate(nums = [1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1]
    assert candidate(nums = [8, 4, 2, 1, 0]) == [4, 3, 2, 1, 1]
    assert candidate(nums = [5, 5, 5, 5, 5]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [1, 3, 2, 1, 4, 7, 8, 5, 6, 9]) == [7, 6, 5, 4, 3, 2, 3, 3, 2, 1]
    assert candidate(nums = [1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [0, 0, 0, 0]) == [1, 1, 1, 1]
    assert candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1023]) == [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2]) == [2, 1]
    assert candidate(nums = [3, 3, 3, 3, 3]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [1, 1, 1, 1, 1]
    assert candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4, 2, 1]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]) == [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]) == [1, 2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1, 1]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]) == [1, 1, 1, 4, 3, 2, 1, 1, 1, 4, 3, 2, 1, 1, 1, 4, 3, 2, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 511, 255, 127, 63]) == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1]
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == [1, 2, 3, 2, 1]
    assert candidate(nums = [1, 0, 2, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == [33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 1]
    assert candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014]) == [1, 2, 3, 2, 5, 4, 3, 2, 1, 1]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [7, 6, 5, 4, 3, 2, 4, 3, 2, 1]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 2, 1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 1, 1]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [8, 6, 2, 3, 7, 5, 1, 4, 9, 10]) == [4, 8, 7, 6, 5, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]
    assert candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1023, 0, 2047, 0, 4095, 0, 8191, 0, 16383, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    assert candidate(nums = [8, 15, 3, 12, 7, 9, 1, 5, 11, 6, 4, 10, 2, 14, 0, 13]) == [2, 1, 2, 2, 2, 4, 3, 2, 2, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [2, 3, 1, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == [4, 5, 4, 4, 4, 3, 3, 2, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 3, 2, 2, 1]
    assert candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31, 1, 1, 3, 7, 15, 31]) == [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [16, 8, 4, 2, 1, 32, 64, 128, 256, 512]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == [1, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 1, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 2, 2, 1]
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 2, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1]
    assert candidate(nums = [3, 1, 2, 7, 4, 6, 5, 0, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [9, 3, 1, 7, 5, 11, 13, 15, 8, 12, 14, 6, 10, 2, 4, 0]) == [4, 5, 4, 3, 2, 2, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1]
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == [8, 7, 6, 5, 4, 3, 2, 3, 2, 1]
    assert candidate(nums = [15, 7, 3, 1, 14, 6, 2, 0, 13, 5, 1, 0, 9, 3, 1, 0, 8, 2, 0, 7]) == [1, 4, 3, 2, 5, 4, 3, 7, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 2, 9, 8, 7, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 1, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 2, 1]
    assert candidate(nums = [268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]) == [9, 8, 7, 6, 5, 4, 3, 2, 2, 1]
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 128, 64, 32, 16, 8, 4, 2, 1, 256, 512, 1024, 2048, 4096]) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [31, 14, 7, 3, 1, 0, 1, 3, 7, 14, 31, 0, 1, 3, 7, 14, 31, 0, 1, 3, 7, 14, 31]) == [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == [1, 1, 1, 4, 3, 2, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 0, 2, 1, 3, 1, 0, 2, 1, 3, 1, 0, 2, 1, 3, 1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 2, 1]
    assert candidate(nums = [5, 8, 14, 23, 42, 67, 98, 132, 175, 220, 270, 325, 385, 450, 520]) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 255, 128, 64, 32, 16, 8, 4, 2, 1, 255, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == [1, 2, 3, 2, 1]
    assert candidate(nums = [2147483647, 1, 2147483647, 2, 2147483647, 3, 2147483647, 4, 2147483647, 5]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907, 953, 476, 238, 119, 59, 29, 14, 7, 3, 1, 0]) == [10, 9, 8, 7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]
    assert candidate(nums = [1, 0, 3, 2, 1, 2, 3, 0, 1, 2]) == [3, 2, 1, 2, 2, 2, 1, 3, 2, 1]
    assert candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [31, 15, 7, 3, 1, 63, 31, 15, 7, 3, 1, 127, 63, 31, 15, 7, 3, 1, 255, 127, 63, 31, 15, 7, 3, 1]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [987654321, 987654320, 987654319, 987654318, 987654317, 987654316, 987654315, 987654314, 987654313, 987654312]) == [3, 2, 1, 2, 3, 2, 1, 2, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [1, 0, 3, 2, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == [3, 2, 1, 2, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 1, 1]
    assert candidate(nums = [2147483647, 0, 2147483647, 0, 2147483647, 0, 2147483647, 0, 2147483647, 0]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]) == [1, 2, 3, 2, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1, 1]
    assert candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 5, 7, 9]) == [1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]


