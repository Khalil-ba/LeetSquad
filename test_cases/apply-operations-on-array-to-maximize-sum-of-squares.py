def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10],k = 4) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10],k = 4) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000],k = 2) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000],k = 2) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10],k = 2) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10],k = 2) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3],k = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3],k = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 5, 8],k = 2) == 261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 5, 8],k = 2) == 261: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 4, 7],k = 3) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 4, 7],k = 3) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 888888888, 777777777],k = 2) == 976625502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 888888888, 777777777],k = 2) == 976625502: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 1) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 1) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1],k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1],k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 20) == 1280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 20) == 1280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 10) == 73676282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 10) == 73676282: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 234567890, 876543210, 456789012, 765432109, 654321098, 543210987, 432109876, 321098765],k = 10) == 686045577
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 234567890, 876543210, 456789012, 765432109, 654321098, 543210987, 432109876, 321098765],k = 10) == 686045577: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937],k = 5) == 24500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937],k = 5) == 24500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 3) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 3) == 147: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217728, 268435456, 536870912, 1073741824, 67108864, 134217728, 268435456, 536870912, 1073741824, 67108864],k = 10) == 214664351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217728, 268435456, 536870912, 1073741824, 67108864, 134217728, 268435456, 536870912, 1073741824, 67108864],k = 10) == 214664351: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73],k = 20) == 65732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73],k = 20) == 65732: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 64660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 64660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1024, 2048, 4096, 8192, 16384],k = 15) == 74023771
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1024, 2048, 4096, 8192, 16384],k = 15) == 74023771: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32],k = 6) == 7938
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32],k = 6) == 7938: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111222333, 333222111, 444555666],k = 4) == 54499332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111222333, 333222111, 444555666],k = 4) == 54499332: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 16) == 4624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 16) == 4624: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 509522932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 509522932: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 11) == 4190209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 11) == 4190209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 10) == 9610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 10) == 9610: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 4186116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 4186116: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 10) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 10) == 640: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 2890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 2890: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512],k = 10) == 1046529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512],k = 10) == 1046529: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111],k = 5) == 847975472
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111],k = 5) == 847975472: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 128, 64, 32, 16, 8],k = 10) == 66221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 128, 64, 32, 16, 8],k = 10) == 66221: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23456789, 987654321, 34567890, 876543210, 45678901, 765432109],k = 3) == 500137909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23456789, 987654321, 34567890, 876543210, 45678901, 765432109],k = 3) == 500137909: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 10) == 10971971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 10) == 10971971: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 10) == 509522932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 10) == 509522932: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 25) == 24025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 25) == 24025: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 242976
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 242976: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643],k = 3) == 551856212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643],k = 3) == 551856212: {e}')
    
    total += 1
    try:
        result = candidate(nums = [314159, 271828, 161803, 414159, 926535, 897932, 384626, 433832, 795028, 841971],k = 5) == 410299793
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [314159, 271828, 161803, 414159, 926535, 897932, 384626, 433832, 795028, 841971],k = 5) == 410299793: {e}')
    
    total += 1
    try:
        result = candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728],k = 10) == 94637808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728],k = 10) == 94637808: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],k = 5) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],k = 5) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233],k = 20) == 1085780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233],k = 20) == 1085780: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005],k = 4) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005],k = 4) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 15) == 11297913
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 15) == 11297913: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],k = 10) == 790321908
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],k = 10) == 790321908: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [256, 128, 64, 32, 16, 8, 4, 2, 1],k = 9) == 261121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [256, 128, 64, 32, 16, 8, 4, 2, 1],k = 9) == 261121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 20) == 509522932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 20) == 509522932: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 10) == 351846767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 10) == 351846767: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 65534, 65533, 65532, 65531, 65530, 65529, 65528, 65527, 65526, 65525, 65524, 65523, 65522, 65521],k = 10) == 944430306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 65534, 65533, 65532, 65531, 65530, 65529, 65528, 65527, 65526, 65525, 65524, 65523, 65522, 65521],k = 10) == 944430306: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 701237477
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 701237477: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 17, 15, 13, 11, 7, 5, 3, 2],k = 5) == 2421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 17, 15, 13, 11, 7, 5, 3, 2],k = 5) == 2421: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 21) == 42286015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 21) == 42286015: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 10) == 506187364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 10) == 506187364: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 5) == 108685633
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 5) == 108685633: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644],k = 4) == 632671383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644],k = 4) == 632671383: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 7) == 57663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 7) == 57663: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000],k = 5) == 757777593
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000],k = 5) == 757777593: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],k = 15) == 420002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],k = 15) == 420002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009],k = 5) == 89965549
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009],k = 5) == 89965549: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384],k = 3) == 7681529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384],k = 3) == 7681529: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],k = 5) == 216111556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],k = 5) == 216111556: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 5) == 53085
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 5) == 53085: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 135792468, 246813579, 864204680, 975318642, 789456123, 654321987, 321654987, 456789123],k = 5) == 103639635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 135792468, 246813579, 864204680, 975318642, 789456123, 654321987, 321654987, 456789123],k = 5) == 103639635: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 30) == 192245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 30) == 192245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000],k = 6) == 785975284
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000],k = 6) == 785975284: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191],k = 8) == 272556040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191],k = 8) == 272556040: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638, 2147483637],k = 11) == 133607314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638, 2147483637],k = 11) == 133607314: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 8) == 1394008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 8) == 1394008: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 2) == 701237477
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 2) == 701237477: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 5) == 1445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 5) == 1445: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 5) == 3461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 5) == 3461: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],k = 10) == 6250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],k = 10) == 6250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 1392773
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 1392773: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 5) == 704657727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 5) == 704657727: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 8) == 179344781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 8) == 179344781: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 11) == 8380418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 11) == 8380418: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 123456789, 987654321, 123456789, 987654321, 123456789, 987654321, 123456789, 987654321],k = 5) == 925171582
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 123456789, 987654321, 123456789, 987654321, 123456789, 987654321, 123456789, 987654321],k = 5) == 925171582: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 5) == 460740093
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 5) == 460740093: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 27, 39, 45, 51, 63, 75, 87, 99, 111, 123, 135, 147, 159, 171],k = 10) == 286506
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 27, 39, 45, 51, 63, 75, 87, 99, 111, 123, 135, 147, 159, 171],k = 10) == 286506: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79],k = 10) == 80842
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79],k = 10) == 80842: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 5) == 5579013
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 5) == 5579013: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024],k = 10) == 10485760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024],k = 10) == 10485760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824],k = 30) == 850618742
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824],k = 30) == 850618742: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 0],k = 4) == 1244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 0],k = 4) == 1244: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 15) == 2535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 15) == 2535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872],k = 5) == 357400917
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872],k = 5) == 357400917: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647],k = 4) == 402474947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647],k = 4) == 402474947: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 7) == 912482192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 7) == 912482192: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 99
    assert candidate(nums = [10, 10, 10, 10],k = 4) == 400
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 2) == 98
    assert candidate(nums = [10, 10, 10, 10],k = 2) == 200
    assert candidate(nums = [1, 1, 1, 1],k = 4) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3],k = 3) == 27
    assert candidate(nums = [2, 6, 5, 8],k = 2) == 261
    assert candidate(nums = [4, 5, 4, 7],k = 3) == 90
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777],k = 2) == 976625502
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 49
    assert candidate(nums = [1, 1, 1, 1, 1, 1],k = 6) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 20) == 1280
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 10) == 73676282
    assert candidate(nums = [123456789, 987654321, 234567890, 876543210, 456789012, 765432109, 654321098, 543210987, 432109876, 321098765],k = 10) == 686045577
    assert candidate(nums = [999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937, 999999937],k = 5) == 24500
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 3) == 147
    assert candidate(nums = [134217728, 268435456, 536870912, 1073741824, 67108864, 134217728, 268435456, 536870912, 1073741824, 67108864],k = 10) == 214664351
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73],k = 20) == 65732
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 64660
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1024, 2048, 4096, 8192, 16384],k = 15) == 74023771
    assert candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32],k = 6) == 7938
    assert candidate(nums = [123456789, 987654321, 111222333, 333222111, 444555666],k = 4) == 54499332
    assert candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 16) == 4624
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 509522932
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 11) == 4190209
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 10) == 9610
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 4186116
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 10) == 640
    assert candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 2890
    assert candidate(nums = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512],k = 10) == 1046529
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111],k = 5) == 847975472
    assert candidate(nums = [31, 15, 7, 3, 1, 128, 64, 32, 16, 8],k = 10) == 66221
    assert candidate(nums = [23456789, 987654321, 34567890, 876543210, 45678901, 765432109],k = 3) == 500137909
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 10) == 10971971
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 10) == 509522932
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 25) == 24025
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 242976
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643],k = 3) == 551856212
    assert candidate(nums = [314159, 271828, 161803, 414159, 926535, 897932, 384626, 433832, 795028, 841971],k = 5) == 410299793
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728],k = 10) == 94637808
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],k = 5) == 320
    assert candidate(nums = [233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233, 233],k = 20) == 1085780
    assert candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005],k = 4) == 43
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 15) == 11297913
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],k = 10) == 790321908
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [256, 128, 64, 32, 16, 8, 4, 2, 1],k = 9) == 261121
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 20) == 509522932
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 10) == 351846767
    assert candidate(nums = [65535, 65534, 65533, 65532, 65531, 65530, 65529, 65528, 65527, 65526, 65525, 65524, 65523, 65522, 65521],k = 10) == 944430306
    assert candidate(nums = [2147483647, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 701237477
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
    assert candidate(nums = [31, 17, 15, 13, 11, 7, 5, 3, 2],k = 5) == 2421
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 21) == 42286015
    assert candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 10) == 506187364
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 5) == 108685633
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644],k = 4) == 632671383
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 7) == 57663
    assert candidate(nums = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000],k = 5) == 757777593
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],k = 15) == 420002
    assert candidate(nums = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009],k = 5) == 89965549
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384],k = 3) == 7681529
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],k = 5) == 216111556
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 5) == 53085
    assert candidate(nums = [123456789, 987654321, 135792468, 246813579, 864204680, 975318642, 789456123, 654321987, 321654987, 456789123],k = 5) == 103639635
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 245
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 30) == 192245
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000],k = 6) == 785975284
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 500
    assert candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191],k = 8) == 272556040
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641, 2147483640, 2147483639, 2147483638, 2147483637],k = 11) == 133607314
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 8) == 1394008
    assert candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 2) == 701237477
    assert candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 5) == 1445
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 245
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 5) == 3461
    assert candidate(nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],k = 10) == 6250
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 1392773
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 5) == 704657727
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 8) == 179344781
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 11) == 8380418
    assert candidate(nums = [123456789, 987654321, 123456789, 987654321, 123456789, 987654321, 123456789, 987654321, 123456789, 987654321],k = 5) == 925171582
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 5) == 460740093
    assert candidate(nums = [13, 27, 39, 45, 51, 63, 75, 87, 99, 111, 123, 135, 147, 159, 171],k = 10) == 286506
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79],k = 10) == 80842
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047],k = 5) == 5579013
    assert candidate(nums = [1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024],k = 10) == 10485760
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824],k = 30) == 850618742
    assert candidate(nums = [31, 15, 7, 3, 1, 0],k = 4) == 1244
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 15) == 2535
    assert candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872],k = 5) == 357400917
    assert candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647],k = 4) == 402474947
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 7) == 912482192


