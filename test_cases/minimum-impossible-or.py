def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 10, 14, 18]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 10, 14, 18]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 15, 31, 63]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 15, 31, 63]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 15, 31]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 15, 31]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 2097152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 2097152: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 2097152, 4194304, 8388608, 16777216, 33554432]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 2097152, 4194304, 8388608, 16777216, 33554432]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 2147483648: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189, 16381, 32765, 65533, 131077]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189, 16381, 32765, 65533, 131077]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094, 8190, 16382, 32766, 65534]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094, 8190, 16382, 32766, 65534]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100, 108, 116, 124]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100, 108, 116, 124]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 63, 127, 255, 511, 1023, 2047, 4095]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 63, 127, 255, 511, 1023, 2047, 4095]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002, 999999997, 1000000003, 999999996, 1000000004, 999999995]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002, 999999997, 1000000003, 999999996, 1000000004, 999999995]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584, 7168]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584, 7168]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 131072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 131072: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741824, 2147483648, 4294967296, 8589934592, 17179869184]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741824, 2147483648, 4294967296, 8589934592, 17179869184]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 24, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 24, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 8192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 8192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 524288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 524288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 11, 43, 171, 683, 2731, 10923, 43691, 174763, 699051, 2796203, 11184811, 44739243, 178956971, 715827883]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 11, 43, 171, 683, 2731, 10923, 43691, 174763, 699051, 2796203, 11184811, 44739243, 178956971, 715827883]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304, 4608, 9216]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304, 4608, 9216]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 3, 2]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16]) == 32
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 2048
    assert candidate(nums = [2, 1]) == 4
    assert candidate(nums = [7, 14, 21, 28]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9]) == 2
    assert candidate(nums = [3, 6, 9, 12]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
    assert candidate(nums = [6, 10, 14, 18]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50]) == 1
    assert candidate(nums = [1024, 2048, 4096, 8192]) == 1
    assert candidate(nums = [7, 14, 28, 56]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [3, 7, 15, 31, 63]) == 1
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 16
    assert candidate(nums = [7, 14, 28]) == 1
    assert candidate(nums = [3, 6, 9]) == 1
    assert candidate(nums = [3, 7, 15, 31]) == 1
    assert candidate(nums = [10, 20, 30, 40]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 32
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 2097152
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1024
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048576
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 2
    assert candidate(nums = [1048576, 2097152, 4194304, 8388608, 16777216, 33554432]) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 2
    assert candidate(nums = [1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471]) == 1
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864]) == 1
    assert candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]) == 2
    assert candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 2147483648
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 2
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 2
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 65536
    assert candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366]) == 1
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118]) == 1
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143]) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 2
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 1
    assert candidate(nums = [8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296]) == 1
    assert candidate(nums = [5, 13, 29, 61, 125, 253, 509, 1021, 2045, 4093, 8189, 16381, 32765, 65533, 131077]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == 1
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == 1
    assert candidate(nums = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125]) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048
    assert candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32768
    assert candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120]) == 1
    assert candidate(nums = [2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094, 8190, 16382, 32766, 65534]) == 1
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 1
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == 1
    assert candidate(nums = [4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100, 108, 116, 124]) == 1
    assert candidate(nums = [31, 63, 127, 255, 511, 1023, 2047, 4095]) == 1
    assert candidate(nums = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400]) == 1
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 4096
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
    assert candidate(nums = [3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385]) == 1
    assert candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1
    assert candidate(nums = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 2
    assert candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002, 999999997, 1000000003, 999999996, 1000000004, 999999995]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 2
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584, 7168]) == 1
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62]) == 1
    assert candidate(nums = [1, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097]) == 2
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33]) == 4
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 131072
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1
    assert candidate(nums = [2, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 32
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 1
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 2
    assert candidate(nums = [1073741824, 2147483648, 4294967296, 8589934592, 17179869184]) == 1
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(nums = [255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1
    assert candidate(nums = [3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 24, 30]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 8192
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 524288
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152]) == 1
    assert candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32
    assert candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096]) == 1
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30]) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048
    assert candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576]) == 1
    assert candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191]) == 1
    assert candidate(nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [3, 11, 43, 171, 683, 2731, 10923, 43691, 174763, 699051, 2796203, 11184811, 44739243, 178956971, 715827883]) == 1
    assert candidate(nums = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48]) == 1
    assert candidate(nums = [31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 1
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61]) == 2
    assert candidate(nums = [7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071]) == 1
    assert candidate(nums = [9, 18, 36, 72, 144, 288, 576, 1152, 2304, 4608, 9216]) == 1
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 2
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 1


