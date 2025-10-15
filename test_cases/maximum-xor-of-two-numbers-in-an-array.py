def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [3, 10, 5, 25, 2, 8]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 10, 5, 25, 2, 8]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2147483647, 0, 1]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2147483647, 0, 1]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 7, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 7, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3000000000, 2147483647, 1, 0]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3000000000, 2147483647, 1, 0]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 1]) == 1036069302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 1]) == 1036069302: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 17, 24, 32, 41, 50, 58, 67, 75, 82, 91, 99]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 17, 24, 32, 41, 50, 58, 67, 75, 82, 91, 99]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 1572864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 1572864: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 1, 2, 3, 4, 5]) == 2000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 1, 2, 3, 4, 5]) == 2000000005: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 12288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 12288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655]) == 2017140294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655]) == 2017140294: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1048574
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1048574: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0, 1, 2147483646, 2]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0, 1, 2147483646, 2]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2, 12, 7, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2, 12, 7, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 1036069302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 1036069302: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 1, 3, 127, 255, 2, 5, 7, 15, 31, 63]) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 1, 3, 127, 255, 2, 5, 7, 15, 31, 63]) == 254: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 16777214, 33554431, 67108862, 134217727, 268435454, 536870911, 1073741822]) == 1065353217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 16777214, 33554431, 67108862, 134217727, 268435454, 536870911, 1073741822]) == 1065353217: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655, 5544332211, 1111111111, 2222222222, 3333333333, 4444444444]) == 2087766500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655, 5544332211, 1111111111, 2222222222, 3333333333, 4444444444]) == 2087766500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 1047438080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 1047438080: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 1572864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 1572864: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 2, 14, 7, 3, 9, 1, 13, 5, 11, 6, 4, 12, 0, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 2, 14, 7, 3, 9, 1, 13, 5, 11, 6, 4, 12, 0, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 1032168868
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 1032168868: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207]) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207]) == 254: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0, 1073741823, 1, 536870911, 2, 268435455, 3, 134217727, 4, 67108863, 5, 33554431, 6, 16777215, 7, 8388607, 8, 4194303, 9, 2097151, 10, 1048575, 11, 524287, 12, 262143, 13, 131071, 14, 65535, 15, 32767, 16]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0, 1073741823, 1, 536870911, 2, 268435455, 3, 134217727, 4, 67108863, 5, 33554431, 6, 16777215, 7, 8388607, 8, 4194303, 9, 2097151, 10, 1048575, 11, 524287, 12, 262143, 13, 131071, 14, 65535, 15, 32767, 16]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1047552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1047552: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 234567890, 345678901, 456789012, 567890123, 678901234, 789012345, 890123456, 901234567]) == 1022202311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 234567890, 345678901, 456789012, 567890123, 678901234, 789012345, 890123456, 901234567]) == 1022202311: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1022: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 65534, 65533, 65532, 65531, 65530, 65529, 65528, 65527, 65526, 65525, 65524, 65523, 65522, 65521, 65520]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 65534, 65533, 65532, 65531, 65530, 65529, 65528, 65527, 65526, 65525, 65524, 65523, 65522, 65521, 65520]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 196608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 196608: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 100311872
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 100311872: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 10, 5, 25, 2, 8, 12, 17, 20, 23, 28, 31]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 10, 5, 25, 2, 8, 12, 17, 20, 23, 28, 31]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1048574
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1048574: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777]) == 1036069302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777]) == 1036069302: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == 1036069302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == 1036069302: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144]) == 201326592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144]) == 201326592: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 1, 7, 3, 9, 2, 8, 4, 6, 10, 5, 11, 12, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 1, 7, 3, 9, 2, 8, 4, 6, 10, 5, 11, 12, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 2114852352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 2114852352: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312]) == 14592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312]) == 14592: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071]) == 130048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071]) == 130048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16777214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16777214: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152]) == 1610612736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152]) == 1610612736: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 1992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 1992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2000000000, 1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250]) == 2043881088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2000000000, 1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250]) == 2043881088: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == 1021940544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == 1021940544: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 10, 1, 8, 3, 4, 9, 7, 2, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 10, 1, 8, 3, 4, 9, 7, 2, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 999999999, 111111111, 888888888, 222222222, 777777777, 333333333]) == 1032171812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 999999999, 111111111, 888888888, 222222222, 777777777, 333333333]) == 1032171812: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 456789123, 321987654, 789123456, 654321987, 891234567, 219876543]) == 1032168868
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 456789123, 321987654, 789123456, 654321987, 891234567, 219876543]) == 1032168868: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 7, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 7, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483647, 0]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483647, 0]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320]) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320]) == 496: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1022: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 29, 31, 45, 66, 78, 90, 103, 114, 129, 143, 155]) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 29, 31, 45, 66, 78, 90, 103, 114, 129, 143, 155]) == 253: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 15, 17, 3, 5, 18, 12]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 15, 17, 3, 5, 18, 12]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [234, 567, 890, 1234, 5678, 9012, 3456, 7890, 12345, 67890]) == 80139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [234, 567, 890, 1234, 5678, 9012, 3456, 7890, 12345, 67890]) == 80139: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0, 1, 2147483646, 1073741823, 1073741824, 536870911, 536870912]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0, 1, 2147483646, 1073741823, 1073741824, 536870911, 536870912]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == 1047472896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == 1047472896: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 98304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 98304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151]) == 1071644672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151]) == 1071644672: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 9, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191]) == 8188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 9, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191]) == 8188: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]) == 261454
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]) == 261454: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 254: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 8, 4, 2, 1, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 8, 4, 2, 1, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 5, 2, 7, 6, 8, 4, 1, 3, 10, 15, 20]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 5, 2, 7, 6, 8, 4, 1, 3, 10, 15, 20]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 29, 18, 23, 56, 78, 99, 101, 112, 134, 156, 178]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 29, 18, 23, 56, 78, 99, 101, 112, 134, 156, 178]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666]) == 1036069302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666]) == 1036069302: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 1, 24, 31, 29, 2, 7, 0, 30, 19]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 1, 24, 31, 29, 2, 7, 0, 30, 19]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999]) == 1036069302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999]) == 1036069302: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 0, 1, 2147483646]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 0, 1, 2147483646]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 1073741822, 1073741821, 1073741820, 1073741819, 1073741818, 1073741817, 1073741816]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 1073741822, 1073741821, 1073741820, 1073741819, 1073741818, 1073741817, 1073741816]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111222333, 444555666, 777888999, 101010101, 202020202, 303030303, 404040404, 505050505]) == 1032168868
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111222333, 444555666, 777888999, 101010101, 202020202, 303030303, 404040404, 505050505]) == 1032168868: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1073741823, 2147483647, 1073741824, 1073741825, 1073741826, 1073741827, 1073741828, 1073741829, 1073741830]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1073741823, 2147483647, 1073741824, 1073741825, 1073741826, 1073741827, 1073741828, 1073741829, 1073741830]) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32, 16, 8, 4, 2, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32, 16, 8, 4, 2, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 201326592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 201326592: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 234567891, 198765432, 345678912, 298765431, 456789123, 398765432, 567891234, 498765431, 678912345, 598765432, 789123456, 698765431, 891234567, 798765432, 912345678, 898765431, 1234567890, 9876543210, 1122334455, 2233445566, 3344556677, 4455667788, 5566778899]) == 2146912412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 234567891, 198765432, 345678912, 298765431, 456789123, 398765432, 567891234, 498765431, 678912345, 598765432, 789123456, 698765431, 891234567, 798765432, 912345678, 898765431, 1234567890, 9876543210, 1122334455, 2233445566, 3344556677, 4455667788, 5566778899]) == 2146912412: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]) == 3145728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]) == 3145728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 1073741824, 1073741822, 1073741825]) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 1073741824, 1073741822, 1073741825]) == 2147483647: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [3, 10, 5, 25, 2, 8]) == 28
    assert candidate(nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15
    assert candidate(nums = [1000000000, 2147483647, 0, 1]) == 2147483647
    assert candidate(nums = [4, 6, 7, 2, 1]) == 7
    assert candidate(nums = [0, 1]) == 1
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [3000000000, 2147483647, 1, 0]) == 2147483647
    assert candidate(nums = [8, 10, 2]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 1]) == 1036069302
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 31
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 30
    assert candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) == 240
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125
    assert candidate(nums = [8, 17, 24, 32, 41, 50, 58, 67, 75, 82, 91, 99]) == 123
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 1572864
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 1, 2, 3, 4, 5]) == 2000000005
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
    assert candidate(nums = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 12288
    assert candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655]) == 2017140294
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638]) == 15
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1048574
    assert candidate(nums = [2147483647, 0, 1, 2147483646, 2]) == 2147483647
    assert candidate(nums = [8, 1, 2, 12, 7, 6]) == 15
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 1036069302
    assert candidate(nums = [8, 10, 1, 3, 127, 255, 2, 5, 7, 15, 31, 63]) == 254
    assert candidate(nums = [8388607, 16777214, 33554431, 67108862, 134217727, 268435454, 536870911, 1073741822]) == 1065353217
    assert candidate(nums = [123456789, 987654321, 1122334455, 5566778899, 9988776655, 5544332211, 1111111111, 2222222222, 3333333333, 4444444444]) == 2087766500
    assert candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 1047438080
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 62
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006]) == 7
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 1572864
    assert candidate(nums = [8, 10, 2, 14, 7, 3, 9, 1, 13, 5, 11, 6, 4, 12, 0, 15]) == 15
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 1032168868
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207]) == 254
    assert candidate(nums = [2147483647, 0, 1073741823, 1, 536870911, 2, 268435455, 3, 134217727, 4, 67108863, 5, 33554431, 6, 16777215, 7, 8388607, 8, 4194303, 9, 2097151, 10, 1048575, 11, 524287, 12, 262143, 13, 131071, 14, 65535, 15, 32767, 16]) == 2147483647
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1047552
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 255
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004]) == 7
    assert candidate(nums = [123456789, 234567890, 345678901, 456789012, 567890123, 678901234, 789012345, 890123456, 901234567]) == 1022202311
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1022
    assert candidate(nums = [2147483647, 0]) == 2147483647
    assert candidate(nums = [65535, 65534, 65533, 65532, 65531, 65530, 65529, 65528, 65527, 65526, 65525, 65524, 65523, 65522, 65521, 65520]) == 15
    assert candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240]) == 15
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 196608
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 100311872
    assert candidate(nums = [3, 10, 5, 25, 2, 8, 12, 17, 20, 23, 28, 31]) == 31
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 1048574
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777]) == 1036069302
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111, 0]) == 1036069302
    assert candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144]) == 201326592
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 15
    assert candidate(nums = [13, 1, 7, 3, 9, 2, 8, 4, 6, 10, 5, 11, 12, 14, 15]) == 15
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 2114852352
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656, 13312]) == 14592
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]) == 62
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640]) == 7
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071]) == 130048
    assert candidate(nums = [2147483647, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2147483647
    assert candidate(nums = [16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16777214
    assert candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152]) == 1610612736
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 1992
    assert candidate(nums = [2000000000, 1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250]) == 2043881088
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000]) == 1021940544
    assert candidate(nums = [6, 10, 1, 8, 3, 4, 9, 7, 2, 5]) == 15
    assert candidate(nums = [987654321, 123456789, 999999999, 111111111, 888888888, 222222222, 777777777, 333333333]) == 1032171812
    assert candidate(nums = [123456789, 987654321, 456789123, 321987654, 789123456, 654321987, 891234567, 219876543]) == 1032168868
    assert candidate(nums = [4, 6, 7, 2, 1]) == 7
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483647, 0]) == 2147483647
    assert candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320]) == 496
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 1022
    assert candidate(nums = [13, 29, 31, 45, 66, 78, 90, 103, 114, 129, 143, 155]) == 253
    assert candidate(nums = [8, 10, 15, 17, 3, 5, 18, 12]) == 30
    assert candidate(nums = [234, 567, 890, 1234, 5678, 9012, 3456, 7890, 12345, 67890]) == 80139
    assert candidate(nums = [2147483647, 0, 1, 2147483646, 1073741823, 1073741824, 536870911, 536870912]) == 2147483647
    assert candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000]) == 1047472896
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 98304
    assert candidate(nums = [1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151]) == 1071644672
    assert candidate(nums = [5, 3, 9, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191]) == 8188
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]) == 261454
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 31
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 254
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 62
    assert candidate(nums = [16, 8, 4, 2, 1, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643]) == 7
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003]) == 3
    assert candidate(nums = [9, 5, 2, 7, 6, 8, 4, 1, 3, 10, 15, 20]) == 30
    assert candidate(nums = [13, 29, 18, 23, 56, 78, 99, 101, 112, 134, 156, 178]) == 255
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666]) == 1036069302
    assert candidate(nums = [13, 1, 24, 31, 29, 2, 7, 0, 30, 19]) == 31
    assert candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999]) == 1036069302
    assert candidate(nums = [2147483647, 0, 1, 2147483646]) == 2147483647
    assert candidate(nums = [1073741823, 1073741822, 1073741821, 1073741820, 1073741819, 1073741818, 1073741817, 1073741816]) == 7
    assert candidate(nums = [123456789, 987654321, 111222333, 444555666, 777888999, 101010101, 202020202, 303030303, 404040404, 505050505]) == 1032168868
    assert candidate(nums = [1, 1073741823, 2147483647, 1073741824, 1073741825, 1073741826, 1073741827, 1073741828, 1073741829, 1073741830]) == 2147483647
    assert candidate(nums = [32, 16, 8, 4, 2, 1]) == 48
    assert candidate(nums = [134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 201326592
    assert candidate(nums = [123456789, 987654321, 234567891, 198765432, 345678912, 298765431, 456789123, 398765432, 567891234, 498765431, 678912345, 598765432, 789123456, 698765431, 891234567, 798765432, 912345678, 898765431, 1234567890, 9876543210, 1122334455, 2233445566, 3344556677, 4455667788, 5566778899]) == 2146912412
    assert candidate(nums = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]) == 3145728
    assert candidate(nums = [1073741823, 1073741824, 1073741822, 1073741825]) == 2147483647


