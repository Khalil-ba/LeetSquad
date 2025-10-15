def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 14, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 14, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 7, 9, 10, 11, 12]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 7, 9, 10, 11, 12]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 14, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 14, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111222333, 444555666, 777888999]) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111222333, 444555666, 777888999]) == 152: {e}')
    
    total += 1
    try:
        result = candidate(nums = [536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217727, 134217726, 134217725, 134217724, 134217723, 134217722, 134217721, 134217720]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217727, 134217726, 134217725, 134217724, 134217723, 134217722, 134217721, 134217720]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000]) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000]) == 228: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [67305985, 134611970, 269223940, 538447880, 1076895760, 2153791520]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [67305985, 134611970, 269223940, 538447880, 1076895760, 2153791520]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655]) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655]) == 154: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990, 999999989, 999999988, 999999987, 999999986, 999999985, 999999984, 999999983, 999999982, 999999981, 999999980]) == 456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990, 999999989, 999999988, 999999987, 999999986, 999999985, 999999984, 999999983, 999999982, 999999981, 999999980]) == 456: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000001, 1000010, 1000011, 1000100, 1000101, 1000110, 1000111]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000001, 1000010, 1000011, 1000100, 1000101, 1000110, 1000111]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 464: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 112233445, 556677889, 998877665, 543216789, 876543210]) == 322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 112233445, 556677889, 998877665, 543216789, 876543210]) == 322: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(nums = [131071, 131072, 131073, 131074, 131075, 131076, 131077]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [131071, 131072, 131073, 131074, 131075, 131076, 131077]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666]) == 411
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666]) == 411: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [536870911, 536870910, 536870909, 536870908, 536870907, 536870906]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [536870911, 536870910, 536870909, 536870908, 536870907, 536870906]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 1122334455, 5544332211, 1357924680, 2468013579]) == 239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 1122334455, 5544332211, 1357924680, 2468013579]) == 239: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 2024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 2024: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 100000001, 100000002, 100000003, 100000004, 100000005, 100000006, 100000007, 100000008, 100000009, 100000010]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 100000001, 100000002, 100000003, 100000004, 100000005, 100000006, 100000007, 100000008, 100000009, 100000010]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 3071, 4095, 5119]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 3071, 4095, 5119]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 686
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 686: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570, 1048569, 1048568]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570, 1048569, 1048568]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777, 77777777, 777777777, 7777777777]) == 557
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777, 77777777, 777777777, 7777777777]) == 557: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 4495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 4495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 634
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 634: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 512: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4, 2, 1]) == 406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4, 2, 1]) == 406: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655, 4433221100]) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655, 4433221100]) == 248: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 8388606, 8388605, 8388604, 8388603, 8388602]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 8388606, 8388605, 8388604, 8388603, 8388602]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005, 500000006, 500000007]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005, 500000006, 500000007]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5318008, 4618459, 4646774, 8777780, 8777736, 6218305, 4649788, 1048585, 4649456, 4618459]) == 459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5318008, 4618459, 4646774, 8777780, 8777736, 6218305, 4649788, 1048585, 4649456, 4618459]) == 459: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 756: {e}')
    
    total += 1
    try:
        result = candidate(nums = [268435455, 268435454, 268435453, 268435452, 268435451, 268435450, 268435449, 268435448, 268435447, 268435446, 268435445]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [268435455, 268435454, 268435453, 268435452, 268435451, 268435450, 268435449, 268435448, 268435447, 268435446, 268435445]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 548
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 548: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 2300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 2300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 392: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 234567891, 1234567890, 9876543210]) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 234567891, 1234567890, 9876543210]) == 158: {e}')
    
    total += 1
    try:
        result = candidate(nums = [135792468, 246813579, 357924681, 468135792, 579246813, 681357924, 792468135, 813579246, 924681357]) == 542
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [135792468, 246813579, 357924681, 468135792, 579246813, 681357924, 792468135, 813579246, 924681357]) == 542: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 470: {e}')
    
    total += 1
    try:
        result = candidate(nums = [536870911, 536870910, 536870909, 536870908, 536870907, 536870906, 536870905, 536870904]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [536870911, 536870910, 536870909, 536870908, 536870907, 536870906, 536870905, 536870904]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 381
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 381: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 240: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 48
    assert candidate(nums = [4, 14, 4]) == 4
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
    assert candidate(nums = [31, 14, 7, 3, 1]) == 24
    assert candidate(nums = [1, 3, 5]) == 4
    assert candidate(nums = [1, 2, 4, 8, 16]) == 20
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9]) == 16
    assert candidate(nums = [1, 2, 3, 4]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5]) == 18
    assert candidate(nums = [0, 1, 2, 3, 4]) == 16
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [0, 0, 0]) == 0
    assert candidate(nums = [1, 0, 1, 0, 1, 0]) == 9
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [3, 5, 6, 7, 9, 10, 11, 12]) == 62
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 128
    assert candidate(nums = [31, 14, 7, 3]) == 13
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 32
    assert candidate(nums = [4, 14, 2]) == 6
    assert candidate(nums = [0, 1, 2, 3]) == 8
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 90
    assert candidate(nums = [123456789, 987654321, 111222333, 444555666, 777888999]) == 152
    assert candidate(nums = [536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575]) == 165
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 210
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 304
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 56
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 25
    assert candidate(nums = [134217727, 134217726, 134217725, 134217724, 134217723, 134217722, 134217721, 134217720]) == 48
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000]) == 228
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 90
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 250
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 84
    assert candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 180
    assert candidate(nums = [67305985, 134611970, 269223940, 538447880, 1076895760, 2153791520]) == 140
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 156
    assert candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655]) == 154
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990, 999999989, 999999988, 999999987, 999999986, 999999985, 999999984, 999999983, 999999982, 999999981, 999999980]) == 456
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 16
    assert candidate(nums = [1000000, 1000001, 1000010, 1000011, 1000100, 1000101, 1000110, 1000111]) == 112
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 464
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 20
    assert candidate(nums = [123456789, 987654321, 112233445, 556677889, 998877665, 543216789, 876543210]) == 322
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644]) == 8
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 455
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 420
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 90
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638]) == 89
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 324
    assert candidate(nums = [131071, 131072, 131073, 131074, 131075, 131076, 131077]) == 126
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666]) == 411
    assert candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]) == 900
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1330
    assert candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 121
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 48
    assert candidate(nums = [536870911, 536870910, 536870909, 536870908, 536870907, 536870906]) == 25
    assert candidate(nums = [123456789, 987654321, 1122334455, 5544332211, 1357924680, 2468013579]) == 239
    assert candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 2024
    assert candidate(nums = [100000000, 100000001, 100000002, 100000003, 100000004, 100000005, 100000006, 100000007, 100000008, 100000009, 100000010]) == 112
    assert candidate(nums = [1023, 2047, 3071, 4095, 5119]) == 16
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 165
    assert candidate(nums = [33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143]) == 84
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 686
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 168
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642]) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 145
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 768
    assert candidate(nums = [8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823]) == 84
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 304
    assert candidate(nums = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570, 1048569, 1048568]) == 48
    assert candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777, 77777777, 777777777, 7777777777]) == 557
    assert candidate(nums = [1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 4495
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 634
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 512
    assert candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4, 2, 1]) == 406
    assert candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655, 4433221100]) == 248
    assert candidate(nums = [8388607, 8388606, 8388605, 8388604, 8388603, 8388602]) == 25
    assert candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005, 500000006, 500000007]) == 48
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 165
    assert candidate(nums = [5318008, 4618459, 4646774, 8777780, 8777736, 6218305, 4649788, 1048585, 4649456, 4618459]) == 459
    assert candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 756
    assert candidate(nums = [268435455, 268435454, 268435453, 268435452, 268435451, 268435450, 268435449, 268435448, 268435447, 268435446, 268435445]) == 112
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 548
    assert candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008]) == 55
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 120
    assert candidate(nums = [8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 2300
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 256
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 392
    assert candidate(nums = [123456789, 987654321, 234567891, 1234567890, 9876543210]) == 158
    assert candidate(nums = [135792468, 246813579, 357924681, 468135792, 579246813, 681357924, 792468135, 813579246, 924681357]) == 542
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 470
    assert candidate(nums = [536870911, 536870910, 536870909, 536870908, 536870907, 536870906, 536870905, 536870904]) == 48
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 381
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 132
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 240


