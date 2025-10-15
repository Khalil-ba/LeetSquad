def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 8, 5, 9, 11, 6, 8],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 8, 5, 9, 11, 6, 8],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 12, 9, 8, 9, 15],k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 12, 9, 8, 9, 15],k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 12, 1, 11, 4, 5],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 12, 1, 11, 4, 5],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 3) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 3) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22],k = 5) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22],k = 5) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32, 64, 128, 256, 512, 1024, 2048, 4096],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32, 64, 128, 256, 512, 1024, 2048, 4096],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555],k = 2) == 536870879
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555],k = 2) == 536870879: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444],k = 3) == 534769557
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444],k = 3) == 534769557: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 6) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 6) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5],k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5],k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 10) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 10) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 28, 15, 13, 29],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 28, 15, 13, 29],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4294967295, 4294967294, 4294967293, 4294967292, 4294967291],k = 3) == 4294967295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4294967295, 4294967294, 4294967293, 4294967292, 4294967291],k = 3) == 4294967295: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 3) == 262143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 3) == 262143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 17, 2, 3, 1, 6, 8, 16, 10, 4],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 17, 2, 3, 1, 6, 8, 16, 10, 4],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 29, 53, 79, 101, 131, 157, 181, 211, 239],k = 5) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 29, 53, 79, 101, 131, 157, 181, 211, 239],k = 5) == 157: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 28, 15, 23, 11, 9],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 28, 15, 23, 11, 9],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32, 16, 8, 4, 2, 1, 64, 128, 256, 512, 1024],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32, 16, 8, 4, 2, 1, 64, 128, 256, 512, 1024],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 5) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 5) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 2) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 2) == 511: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 4) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 4) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 6) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 6) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8388607, 8388606, 8388605, 8388604, 8388603, 8388602, 8388601, 8388600],k = 4) == 8388607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8388607, 8388606, 8388605, 8388604, 8388603, 8388602, 8388601, 8388600],k = 4) == 8388607: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 28, 15, 24, 29, 30],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 28, 15, 24, 29, 30],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 38, 47, 56, 65, 74, 83, 92, 101, 110],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 38, 47, 56, 65, 74, 83, 92, 101, 110],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192],k = 10) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192],k = 10) == 254: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 33, 51, 48, 47, 38, 21, 50, 49, 23],k = 5) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 33, 51, 48, 47, 38, 21, 50, 49, 23],k = 5) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 7, 10, 12, 15],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 7, 10, 12, 15],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 124, 248, 496, 992, 1984],k = 4) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 124, 248, 496, 992, 1984],k = 4) == 248: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 28, 15, 23, 29, 27, 19],k = 5) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 28, 15, 23, 29, 27, 19],k = 5) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 25) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 25) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 4) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 4) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 28, 15, 29, 10],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 28, 15, 29, 10],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229],k = 10) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229],k = 10) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823],k = 5) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823],k = 5) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 8) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 8) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035],k = 7) == 2097088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035],k = 7) == 2097088: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248],k = 4) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248],k = 4) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 10) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 10) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [63, 37, 19, 31, 15, 7, 1, 3, 11],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [63, 37, 19, 31, 15, 7, 1, 3, 11],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727],k = 4) == 536870911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727],k = 4) == 536870911: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 5) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 5) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0],k = 4) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0],k = 4) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 5) == 2044
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 5) == 2044: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],k = 2) == 1000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],k = 2) == 1000000003: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642],k = 3) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642],k = 3) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 134217727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 134217727: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 1) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 1) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 17, 14, 19, 28, 15, 30],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 17, 14, 19, 28, 15, 30],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1020: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400],k = 7) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400],k = 7) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431],k = 15) == 33554431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431],k = 15) == 33554431: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 28, 19, 14, 23, 15, 27],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 28, 19, 14, 23, 15, 27],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 28, 15, 21, 19],k = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 28, 15, 21, 19],k = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824],k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824],k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 25) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 25) == 127: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 8, 5, 9, 11, 6, 8],k = 1) == 15
    assert candidate(nums = [7, 12, 9, 8, 9, 15],k = 4) == 9
    assert candidate(nums = [2, 12, 1, 11, 4, 5],k = 6) == 0
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 3) == 63
    assert candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22],k = 5) == 23
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384],k = 7) == 0
    assert candidate(nums = [32, 64, 128, 256, 512, 1024, 2048, 4096],k = 4) == 0
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 3) == 31
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 6) == 0
    assert candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555],k = 2) == 536870879
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444],k = 3) == 534769557
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 6) == 31
    assert candidate(nums = [5, 5, 5, 5, 5, 5],k = 6) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 10) == 63
    assert candidate(nums = [31, 14, 7, 28, 15, 13, 29],k = 3) == 31
    assert candidate(nums = [4294967295, 4294967294, 4294967293, 4294967292, 4294967291],k = 3) == 4294967295
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 3) == 262143
    assert candidate(nums = [5, 17, 2, 3, 1, 6, 8, 16, 10, 4],k = 5) == 0
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 2) == 0
    assert candidate(nums = [13, 29, 53, 79, 101, 131, 157, 181, 211, 239],k = 5) == 157
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 1
    assert candidate(nums = [31, 14, 7, 28, 15, 23, 11, 9],k = 3) == 31
    assert candidate(nums = [32, 16, 8, 4, 2, 1, 64, 128, 256, 512, 1024],k = 7) == 0
    assert candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],k = 10) == 17
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 5) == 31
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 2) == 511
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535],k = 4) == 8191
    assert candidate(nums = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 6) == 127
    assert candidate(nums = [8388607, 8388606, 8388605, 8388604, 8388603, 8388602, 8388601, 8388600],k = 4) == 8388607
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 6) == 0
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 8) == 0
    assert candidate(nums = [31, 14, 7, 28, 15, 24, 29, 30],k = 5) == 30
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 10) == 0
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 5) == 24
    assert candidate(nums = [29, 38, 47, 56, 65, 74, 83, 92, 101, 110],k = 7) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192],k = 10) == 254
    assert candidate(nums = [18, 33, 51, 48, 47, 38, 21, 50, 49, 23],k = 5) == 51
    assert candidate(nums = [3, 5, 6, 7, 10, 12, 15],k = 4) == 7
    assert candidate(nums = [31, 62, 124, 248, 496, 992, 1984],k = 4) == 248
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 10) == 1
    assert candidate(nums = [31, 14, 28, 15, 23, 29, 27, 19],k = 5) == 31
    assert candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152],k = 3) == 0
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 2) == 0
    assert candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 25) == 2147483647
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 10) == 15
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 4) == 127
    assert candidate(nums = [31, 14, 7, 28, 15, 29, 10],k = 3) == 31
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229],k = 10) == 255
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 5) == 31
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 5) == 0
    assert candidate(nums = [1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823, 1073741823],k = 5) == 1073741823
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 8) == 31
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035],k = 7) == 2097088
    assert candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248],k = 4) == 255
    assert candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 10) == 2147483647
    assert candidate(nums = [63, 37, 19, 31, 15, 7, 1, 3, 11],k = 3) == 31
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 20) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 7) == 0
    assert candidate(nums = [4294967295, 2147483647, 1073741823, 536870911, 268435455, 134217727],k = 4) == 536870911
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1],k = 5) == 0
    assert candidate(nums = [3, 6, 12, 24, 48, 96],k = 3) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 30) == 1
    assert candidate(nums = [1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 15) == 0
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],k = 5) == 2047
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 1000000000
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0],k = 4) == 31
    assert candidate(nums = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 31
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 5) == 2044
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],k = 2) == 1000000003
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642],k = 3) == 2147483647
    assert candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 134217727
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 15) == 0
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 5) == 63
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64],k = 1) == 127
    assert candidate(nums = [31, 17, 14, 19, 28, 15, 30],k = 3) == 31
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1020
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400],k = 7) == 127
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],k = 8) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
    assert candidate(nums = [33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431, 33554431],k = 15) == 33554431
    assert candidate(nums = [31, 28, 19, 14, 23, 15, 27],k = 3) == 31
    assert candidate(nums = [31, 14, 7, 28, 15, 21, 19],k = 3) == 31
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824],k = 30) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],k = 2) == 0
    assert candidate(nums = [2147483647, 1073741823, 536870911, 268435455, 134217727, 67108863, 33554431, 16777215, 8388607, 4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 25) == 127


