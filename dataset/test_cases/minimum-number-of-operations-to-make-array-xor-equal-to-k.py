def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1],k = 63) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1],k = 63) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000],k = 125000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000],k = 125000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 127) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 127) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000],k = 1000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000],k = 1000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, 2, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, 2, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000],k = 1250000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000],k = 1250000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 7654321, 9876543, 3214567, 6543219],k = 1357924) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 7654321, 9876543, 3214567, 6543219],k = 1357924) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 27, 33, 45],k = 58) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 27, 33, 45],k = 58) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 100000],k = 999998) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 100000],k = 999998) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224],k = 112) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224],k = 112) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 16777215, 33554431, 67108863, 134217727],k = 268435455) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 16777215, 33554431, 67108863, 134217727],k = 268435455) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1022) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1022) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85],k = 255) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85],k = 255) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 345678, 901234],k = 67890) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 345678, 901234],k = 67890) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 1000001) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 1000001) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1023) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1023) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 13, 15, 21],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 13, 15, 21],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383],k = 1073741823) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383],k = 1073741823) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 7, 3, 1],k = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 7, 3, 1],k = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1048574) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1048574) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191],k = 16383) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191],k = 16383) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63],k = 2097151) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63],k = 2097151) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 2047) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 2047) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2047) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2047) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 7654321, 111222333, 333222111, 444555666],k = 987654321) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 7654321, 111222333, 333222111, 444555666],k = 987654321) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444],k = 555555) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444],k = 555555) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 12],k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 12],k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234, 9012345, 1012345],k = 5000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234, 9012345, 1012345],k = 5000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 100000],k = 555555) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 100000],k = 555555) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 7, 15, 8, 2],k = 31) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 7, 15, 8, 2],k = 31) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 321098, 654321, 123456, 789012],k = 1234567) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 321098, 654321, 123456, 789012],k = 1234567) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 28) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 28) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 112) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 112) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],k = 16383) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],k = 16383) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 255) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 255) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 4294967295) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 4294967295) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111],k = 6666666) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111],k = 6666666) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 101010],k = 123456789) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 101010],k = 123456789) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876, 98765],k = 1000000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876, 98765],k = 1000000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],k = 1000000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],k = 1000000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 1048575) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 1048575) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 123456) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 123456) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000],k = 1048575) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000],k = 1048575) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [63, 31, 15, 7, 3, 1],k = 64) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [63, 31, 15, 7, 3, 1],k = 64) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 990) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 990) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 254) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 254) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 2047) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 2047) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4294967295, 0, 1, 2, 3, 4, 5, 6, 7, 8],k = 4294967295) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4294967295, 0, 1, 2, 3, 4, 5, 6, 7, 8],k = 4294967295) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15],k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15],k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 8388607) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 8388607) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303],k = 8589934591) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303],k = 8589934591) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 1048575) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 1048575) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1048575) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1048575) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2048) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2048) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 256) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 256) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 192837465, 567890123, 246813579],k = 1234567890) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 192837465, 567890123, 246813579],k = 1234567890) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996],k = 1000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996],k = 1000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2097151) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2097151) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11],k = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11],k = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 254) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 254) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],k = 2048) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],k = 2048) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20],k = 14) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20],k = 14) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1023) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1023) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111],k = 123456) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111],k = 123456) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [64, 32, 16, 8, 4, 2, 1],k = 127) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [64, 32, 16, 8, 4, 2, 1],k = 127) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2047) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2047) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 536870911) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 536870911) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 16777214) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 16777214) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31],k = 63) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31],k = 63) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 65534) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 65534) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9],k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9],k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 15, 8],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 15, 8],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 31, 63, 127, 255],k = 255) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 31, 63, 127, 255],k = 255) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1024) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1024) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 8, 4, 2, 1, 8, 4, 2, 1, 8, 4, 2, 1],k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 8, 4, 2, 1, 8, 4, 2, 1, 8, 4, 2, 1],k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250],k = 2187500) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250],k = 2187500) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 16777215) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 16777215) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],k = 512) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],k = 512) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000],k = 1000000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000],k = 1000000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047],k = 1023) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047],k = 1023) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 789012, 345678, 901234, 234567, 876543, 456789, 543210, 123456],k = 999999) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 789012, 345678, 901234, 234567, 876543, 456789, 543210, 123456],k = 999999) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 4095) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 4095) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [135792468, 246813579, 357924681, 468135792, 579246813, 681357924, 792468135, 813579246, 924681357, 1035792468],k = 999999999) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [135792468, 246813579, 357924681, 468135792, 579246813, 681357924, 792468135, 813579246, 924681357, 1035792468],k = 999999999) == 16: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 0, 0, 0],k = 2) == 1
    assert candidate(nums = [1, 1, 1, 1],k = 0) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1],k = 63) == 6
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1
    assert candidate(nums = [2, 1, 3, 4],k = 1) == 2
    assert candidate(nums = [1000000, 500000, 250000],k = 125000) == 12
    assert candidate(nums = [1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [1, 3, 5, 7, 9],k = 15) == 2
    assert candidate(nums = [3, 3, 3, 3],k = 3) == 2
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 127) == 0
    assert candidate(nums = [1000000],k = 1000000) == 0
    assert candidate(nums = [0, 0, 0, 0],k = 1) == 1
    assert candidate(nums = [0, 0, 0, 0],k = 15) == 4
    assert candidate(nums = [1, 2, 3, 4, 5],k = 7) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [2, 0, 2, 0],k = 0) == 0
    assert candidate(nums = [1000000, 500000, 250000],k = 1250000) == 5
    assert candidate(nums = [0, 0, 0, 0],k = 0) == 0
    assert candidate(nums = [1234567, 7654321, 9876543, 3214567, 6543219],k = 1357924) == 15
    assert candidate(nums = [15, 27, 33, 45],k = 58) == 2
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 100000],k = 999998) == 8
    assert candidate(nums = [7, 14, 28, 56, 112, 224],k = 112) == 5
    assert candidate(nums = [8388607, 16777215, 33554431, 67108863, 134217727],k = 268435455) == 3
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1022) == 4
    assert candidate(nums = [17, 34, 51, 68, 85],k = 255) == 6
    assert candidate(nums = [123456, 789012, 345678, 901234],k = 67890) == 10
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 1000001) == 8
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1023) == 5
    assert candidate(nums = [7, 13, 15, 21],k = 10) == 3
    assert candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383],k = 1073741823) == 25
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 0
    assert candidate(nums = [15, 7, 3, 1],k = 14) == 1
    assert candidate(nums = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1048574) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [1023, 2047, 4095, 8191],k = 16383) == 12
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63],k = 2097151) == 8
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 2047) == 0
    assert candidate(nums = [1, 3, 5, 7, 9],k = 15) == 2
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 8) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2047) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [1234567, 7654321, 111222333, 333222111, 444555666],k = 987654321) == 20
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 0) == 0
    assert candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444],k = 555555) == 9
    assert candidate(nums = [3, 5, 6, 12],k = 7) == 3
    assert candidate(nums = [1234567, 2345678, 3456789, 4567890, 5678901, 6789012, 7890123, 8901234, 9012345, 1012345],k = 5000000) == 10
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 100000],k = 555555) == 12
    assert candidate(nums = [13, 7, 15, 8, 2],k = 31) == 1
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 0) == 5
    assert candidate(nums = [987654, 321098, 654321, 123456, 789012],k = 1234567) == 12
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 28) == 2
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 112) == 4
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],k = 16383) == 3
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 255) == 8
    assert candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 4294967295) == 16
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 8) == 1
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111],k = 6666666) == 16
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111, 101010],k = 123456789) == 12
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 10) == 6
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876, 98765],k = 1000000) == 12
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],k = 1000000) == 8
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 1048575) == 6
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 123456) == 13
    assert candidate(nums = [1000000, 500000, 250000, 125000],k = 1048575) == 8
    assert candidate(nums = [63, 31, 15, 7, 3, 1],k = 64) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 990) == 7
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 254) == 7
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 2047) == 6
    assert candidate(nums = [4294967295, 0, 1, 2, 3, 4, 5, 6, 7, 8],k = 4294967295) == 1
    assert candidate(nums = [15, 15, 15, 15],k = 15) == 4
    assert candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 8388607) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 31) == 5
    assert candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303],k = 8589934591) == 28
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 1048575) == 1
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1048575) == 1
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2048) == 12
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 256) == 1
    assert candidate(nums = [987654321, 123456789, 192837465, 567890123, 246813579],k = 1234567890) == 13
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996],k = 1000000) == 0
    assert candidate(nums = [1048575, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2097151) == 21
    assert candidate(nums = [3, 5, 7, 9, 11],k = 15) == 2
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 254) == 3
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],k = 2048) == 10
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20],k = 14) == 3
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 1023) == 1
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111],k = 123456) == 13
    assert candidate(nums = [64, 32, 16, 8, 4, 2, 1],k = 127) == 0
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2047) == 0
    assert candidate(nums = [268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 536870911) == 15
    assert candidate(nums = [16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 16777214) == 11
    assert candidate(nums = [1, 3, 7, 15, 31],k = 63) == 3
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 65534) == 7
    assert candidate(nums = [3, 5, 7, 9],k = 15) == 3
    assert candidate(nums = [5, 3, 15, 8],k = 10) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 0) == 0
    assert candidate(nums = [15, 31, 63, 127, 255],k = 255) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 31) == 5
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1024) == 6
    assert candidate(nums = [8, 4, 2, 1, 8, 4, 2, 1, 8, 4, 2, 1, 8, 4, 2, 1],k = 15) == 4
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250],k = 2187500) == 11
    assert candidate(nums = [8388607, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 16777215) == 24
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 23) == 0
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],k = 0) == 0
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],k = 512) == 2
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],k = 1000000) == 8
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047],k = 1023) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1023) == 10
    assert candidate(nums = [123456, 654321, 789012, 345678, 901234, 234567, 876543, 456789, 543210, 123456],k = 999999) == 10
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 1023) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 4095) == 12
    assert candidate(nums = [7, 7, 7, 7, 7],k = 7) == 0
    assert candidate(nums = [135792468, 246813579, 357924681, 468135792, 579246813, 681357924, 792468135, 813579246, 924681357, 1035792468],k = 999999999) == 16


