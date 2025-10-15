def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16],k = 3) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16],k = 3) == 143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000],k = 8) == 256554748416
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000],k = 8) == 256554748416: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9],k = 4) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9],k = 4) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5],k = 11) == 10245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5],k = 11) == 10245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15],k = 5) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15],k = 5) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8],k = 3) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8],k = 3) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1],k = 7) == 3983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1],k = 7) == 3983: {e}')
    
    total += 1
    try:
        result = candidate(nums = [127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127],k = 15) == 4161663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127],k = 15) == 4161663: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2],k = 2) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2],k = 2) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 9231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 9231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 13) == 253983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 13) == 253983: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000],k = 15) == 32768000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000],k = 15) == 32768000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 12) == 118815
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 12) == 118815: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1],k = 5) == 32000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1],k = 5) == 32000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 6) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 6) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],k = 10) == 10254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],k = 10) == 10254: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36],k = 13) == 294939
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36],k = 13) == 294939: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],k = 14) == 901183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],k = 14) == 901183: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 513: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 9],k = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 9],k = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256],k = 5) == 33536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256],k = 5) == 33536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 17],k = 7) == 2191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 17],k = 7) == 2191: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 11) == 2098174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 11) == 2098174: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3],k = 4) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3],k = 4) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63],k = 14) == 1032255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63],k = 14) == 1032255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 14, 15, 16],k = 9) == 8207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 14, 15, 16],k = 9) == 8207: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 6) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 6) == 455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 512, 256, 128, 64],k = 7) == 131008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 512, 256, 128, 64],k = 7) == 131008: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30],k = 15) == 983070
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30],k = 15) == 983070: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28],k = 12) == 114719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28],k = 12) == 114719: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000],k = 8) == 256086374272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000],k = 8) == 256086374272: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 8) == 12607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 8) == 12607: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 42, 84, 168, 336, 672, 1344, 2688, 5376, 10752],k = 7) == 1384447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 42, 84, 168, 336, 672, 1344, 2688, 5376, 10752],k = 7) == 1384447: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127],k = 10) == 67108863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127],k = 10) == 67108863: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 13) == 8590983167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 13) == 8590983167: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333],k = 10) == 3416063
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333],k = 10) == 3416063: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656],k = 15) == 218107903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656],k = 15) == 218107903: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 5) == 16895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 5) == 16895: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 876543219, 765432198, 654321987, 543219876],k = 8) == 253403069943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 876543219, 765432198, 654321987, 543219876],k = 8) == 253403069943: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 123456789, 876543210, 98765432, 8765432, 765432, 65432, 5432, 432, 32],k = 10) == 1011464798207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 123456789, 876543210, 98765432, 8765432, 765432, 65432, 5432, 432, 32],k = 10) == 1011464798207: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143],k = 10) == 268435455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143],k = 10) == 268435455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 15) == 16777727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 15) == 16777727: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 10) == 92287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 10) == 92287: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],k = 7) == 128849005055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],k = 7) == 128849005055: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 9, 15, 31, 63, 127, 255, 511, 1023],k = 10) == 1048063
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 9, 15, 31, 63, 127, 255, 511, 1023],k = 10) == 1048063: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2],k = 3) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2],k = 3) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 15) == 32768452971519
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 15) == 32768452971519: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1],k = 15) == 1015823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1],k = 15) == 1015823: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 2000000000, 3, 3000000000, 4, 4000000000, 5, 5000000000],k = 15) == 163840117440007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 2000000000, 3, 3000000000, 4, 4000000000, 5, 5000000000],k = 15) == 163840117440007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],k = 10) == 4194303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],k = 10) == 4194303: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 12) == 127007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 12) == 127007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 12) == 4296015870
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 12) == 4296015870: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000],k = 5) == 32142772737
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000],k = 5) == 32142772737: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 7) == 126701535231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 7) == 126701535231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 10) == 1011464798207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 10) == 1011464798207: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 2048, 4096, 8192, 16384],k = 13) == 134234111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 2048, 4096, 8192, 16384],k = 13) == 134234111: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 8) == 257020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 8) == 257020: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 15) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 15) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 1049599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 1049599: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 2097151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 2097151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 15) == 33555455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 15) == 33555455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 10) == 30751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 10) == 30751: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],k = 7) == 7103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],k = 7) == 7103: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 16778239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 16778239: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 47, 94, 188, 376, 752, 1504, 3008, 6016, 12032],k = 5) == 393215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 47, 94, 188, 376, 752, 1504, 3008, 6016, 12032],k = 5) == 393215: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 14) == 17180917758
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 14) == 17180917758: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 32764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 32764: {e}')
    
    total += 1
    try:
        result = candidate(nums = [131071, 262143, 524287, 1048575],k = 12) == 4294967295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [131071, 262143, 524287, 1048575],k = 12) == 4294967295: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 10) == 1024278055424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 10) == 1024278055424: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 15) == 32768016775167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 15) == 32768016775167: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 8) == 231420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 8) == 231420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 10) == 1024349700095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 10) == 1024349700095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(nums = [536870911, 268435455, 134217727, 67108863, 33554431],k = 10) == 549755813887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [536870911, 268435455, 134217727, 67108863, 33554431],k = 10) == 549755813887: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 17180392448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 17180392448: {e}')
    
    total += 1
    try:
        result = candidate(nums = [233, 322, 411, 500, 599, 688, 777, 866, 955],k = 5) == 30719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [233, 322, 411, 500, 599, 688, 777, 866, 955],k = 5) == 30719: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 1074790399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 1074790399: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 8) == 72613887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 8) == 72613887: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],k = 12) == 4096318765567
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],k = 12) == 4096318765567: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 4) == 24572
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 4) == 24572: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 15) == 3702911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 15) == 3702911: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 29, 41, 53, 67, 83, 97],k = 12) == 397439
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 29, 41, 53, 67, 83, 97],k = 12) == 397439: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 15) == 1073725439
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 15) == 1073725439: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 10) == 524799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 10) == 524799: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 8) == 262143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 8) == 262143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645],k = 5) == 68719476735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645],k = 5) == 68719476735: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 1049599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 1049599: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 335: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 3) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 3) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 12) == 67125247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 12) == 67125247: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555],k = 15) == 32768452984571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555],k = 15) == 32768452984571: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999999, 999999999, 999999999],k = 15) == 32768452971007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999999, 999999999, 999999999],k = 15) == 32768452971007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 2147614719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 2147614719: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 10) == 6930431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 10) == 6930431: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],k = 7) == 128312147936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],k = 7) == 128312147936: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191],k = 10) == 8388607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191],k = 10) == 8388607: {e}')
    
    total += 1
    try:
        result = candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 8389119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 8389119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255],k = 14) == 4178175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255],k = 14) == 4178175: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 12) == 268435455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 12) == 268435455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 5) == 32142786559
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 5) == 32142786559: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383],k = 3) == 131071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383],k = 3) == 131071: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 135792468, 246813579, 864201357],k = 5) == 32212254719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 135792468, 246813579, 864201357],k = 5) == 32212254719: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 20511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 20511: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 12) == 204863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 12) == 204863: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000],k = 10) == 1024349700088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000],k = 10) == 1024349700088: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 491535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 491535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 135792468, 246813579, 369258147],k = 15) == 32363652317183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 135792468, 246813579, 369258147],k = 15) == 32363652317183: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 38654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 38654: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872],k = 5) == 516095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872],k = 5) == 516095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 14) == 1474687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 14) == 1474687: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 13) == 55427071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 13) == 55427071: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 31
    assert candidate(nums = [1, 2, 4, 8, 16],k = 3) == 143
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 8) == 256554748416
    assert candidate(nums = [3, 5, 7, 9],k = 4) == 151
    assert candidate(nums = [5, 5, 5, 5, 5, 5],k = 11) == 10245
    assert candidate(nums = [5, 10, 15],k = 5) == 495
    assert candidate(nums = [1, 2, 4, 8],k = 3) == 71
    assert candidate(nums = [31, 15, 7, 3, 1],k = 7) == 3983
    assert candidate(nums = [127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127],k = 15) == 4161663
    assert candidate(nums = [8, 1, 2],k = 2) == 35
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 9231
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 13) == 253983
    assert candidate(nums = [1000000000],k = 15) == 32768000000000
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 12) == 118815
    assert candidate(nums = [1, 1000000000, 1],k = 5) == 32000000001
    assert candidate(nums = [1, 1, 1, 1, 1],k = 6) == 65
    assert candidate(nums = [2, 4, 6, 8, 10],k = 10) == 10254
    assert candidate(nums = [9, 18, 27, 36],k = 13) == 294939
    assert candidate(nums = [11, 22, 33, 44, 55],k = 14) == 901183
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 513
    assert candidate(nums = [12, 9],k = 1) == 30
    assert candidate(nums = [1024, 512, 256],k = 5) == 33536
    assert candidate(nums = [7, 11, 13, 17],k = 7) == 2191
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5125
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 11) == 2098174
    assert candidate(nums = [3, 3, 3, 3],k = 4) == 51
    assert candidate(nums = [63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63],k = 14) == 1032255
    assert candidate(nums = [13, 14, 15, 16],k = 9) == 8207
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 6) == 455
    assert candidate(nums = [1023, 512, 256, 128, 64],k = 7) == 131008
    assert candidate(nums = [6, 12, 18, 24, 30],k = 15) == 983070
    assert candidate(nums = [7, 14, 21, 28],k = 12) == 114719
    assert candidate(nums = [1000000000, 500000000, 250000000],k = 8) == 256086374272
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 8) == 12607
    assert candidate(nums = [21, 42, 84, 168, 336, 672, 1344, 2688, 5376, 10752],k = 7) == 1384447
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127],k = 10) == 67108863
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 13) == 8590983167
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333],k = 10) == 3416063
    assert candidate(nums = [13, 26, 52, 104, 208, 416, 832, 1664, 3328, 6656],k = 15) == 218107903
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 5) == 16895
    assert candidate(nums = [987654321, 876543219, 765432198, 654321987, 543219876],k = 8) == 253403069943
    assert candidate(nums = [987654321, 123456789, 876543210, 98765432, 8765432, 765432, 65432, 5432, 432, 32],k = 10) == 1011464798207
    assert candidate(nums = [15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143],k = 10) == 268435455
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 15) == 16777727
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 10) == 92287
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],k = 7) == 128849005055
    assert candidate(nums = [3, 5, 9, 15, 31, 63, 127, 255, 511, 1023],k = 10) == 1048063
    assert candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2],k = 3) == 255
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 15) == 32768452971519
    assert candidate(nums = [31, 15, 7, 3, 1],k = 15) == 1015823
    assert candidate(nums = [1, 1000000000, 2, 2000000000, 3, 3000000000, 4, 4000000000, 5, 5000000000],k = 15) == 163840117440007
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],k = 10) == 4194303
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 12) == 127007
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 12) == 4296015870
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000],k = 5) == 32142772737
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 7) == 126701535231
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 10) == 1011464798207
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 2048, 4096, 8192, 16384],k = 13) == 134234111
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 8) == 257020
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 15) == 2147483647
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 1049599
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 2097151
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 15) == 33555455
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 10) == 30751
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == 27
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],k = 7) == 7103
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 16778239
    assert candidate(nums = [23, 47, 94, 188, 376, 752, 1504, 3008, 6016, 12032],k = 5) == 393215
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 14) == 17180917758
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 32764
    assert candidate(nums = [131071, 262143, 524287, 1048575],k = 12) == 4294967295
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 10) == 1024278055424
    assert candidate(nums = [999999999, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 15) == 32768016775167
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 8) == 231420
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 10) == 1024349700095
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 1023
    assert candidate(nums = [536870911, 268435455, 134217727, 67108863, 33554431],k = 10) == 549755813887
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 17180392448
    assert candidate(nums = [233, 322, 411, 500, 599, 688, 777, 866, 955],k = 5) == 30719
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 1074790399
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 8) == 72613887
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],k = 12) == 4096318765567
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 4) == 24572
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 15) == 3702911
    assert candidate(nums = [13, 29, 41, 53, 67, 83, 97],k = 12) == 397439
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 15) == 1073725439
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 10) == 524799
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 8) == 262143
    assert candidate(nums = [2147483647, 2147483646, 2147483645],k = 5) == 68719476735
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 10) == 1049599
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 335
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],k = 3) == 109
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 12) == 67125247
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555],k = 15) == 32768452984571
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999],k = 15) == 32768452971007
    assert candidate(nums = [131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 2147614719
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 10) == 6930431
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],k = 7) == 128312147936
    assert candidate(nums = [1023, 2047, 4095, 8191],k = 10) == 8388607
    assert candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 14) == 8389119
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255],k = 14) == 4178175
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 12) == 268435455
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],k = 5) == 32142786559
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383],k = 3) == 131071
    assert candidate(nums = [123456789, 987654321, 135792468, 246813579, 864201357],k = 5) == 32212254719
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 20511
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 12) == 204863
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000],k = 10) == 1024349700088
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 491535
    assert candidate(nums = [123456789, 987654321, 135792468, 246813579, 369258147],k = 15) == 32363652317183
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 38654
    assert candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872],k = 5) == 516095
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 14) == 1474687
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 13) == 55427071


