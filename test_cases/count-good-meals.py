def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048576, 1048576, 524288, 524288, 262144, 262144]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048576, 1048576, 524288, 524288, 262144, 262144]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048576, 1048576]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048576, 1048576]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [13, 100, 13]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [13, 100, 13]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 3, 5, 7, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 3, 5, 7, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 1, 3, 3, 3, 7]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 1, 3, 3, 3, 7]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 0, 0, 0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 0, 0, 0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048576, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048576, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1048575, 1048575, 1048576]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1048575, 1048575, 1048576]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 100000, 200000, 300000, 400000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 100000, 200000, 300000, 400000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048576, 1048576]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048576, 1048576]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2, 2, 2, 2, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2, 2, 2, 2, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1048575]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1048575]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [31, 1, 4, 3, 12, 13, 8, 16, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [31, 1, 4, 3, 12, 13, 8, 16, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048575, 1048576, 524287, 524288, 262143, 262144, 131071, 131072, 65535, 65536, 32767, 32768, 16383, 16384, 8191, 8192, 4095, 4096, 2047, 2048, 1023, 1024, 511, 512, 255, 256, 127, 128, 63, 64, 31, 32, 15, 16, 7, 8, 3, 4, 1, 2, 0, 0, 0, 0, 0, 0]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048575, 1048576, 524287, 524288, 262143, 262144, 131071, 131072, 65535, 65536, 32767, 32768, 16383, 16384, 8191, 8192, 4095, 4096, 2047, 2048, 1023, 1024, 511, 512, 255, 256, 127, 128, 63, 64, 31, 32, 15, 16, 7, 8, 3, 4, 1, 2, 0, 0, 0, 0, 0, 0]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 31, 31, 31]) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 31, 31, 31]) == 249: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [5, 1, 4, 3, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [5, 1, 4, 3, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [21, 1, 17, 3, 9, 18, 25, 33]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [21, 1, 17, 3, 9, 18, 25, 33]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 1024, 2047, 2048, 3071, 3072, 4095, 4096]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 1024, 2047, 2048, 3071, 3072, 4095, 4096]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 1024, 1025, 2047, 2048, 2049, 4095, 4096, 4097]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 1024, 1025, 2047, 2048, 2049, 4095, 4096, 4097]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 1024, 2047, 2048, 4095, 4096, 8191, 8192]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 1024, 2047, 2048, 4095, 4096, 8191, 8192]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [5, 15, 1, 3, 7, 9, 11, 13]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [5, 15, 1, 3, 7, 9, 11, 13]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048575, 1048576, 2097151, 2097152, 4194303, 4194304]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048575, 1048576, 2097151, 2097152, 4194303, 4194304]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1023, 1024, 2047, 2048, 4095, 4096]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1023, 1024, 2047, 2048, 4095, 4096]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1048575, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1048575, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [3, 5, 7, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [3, 5, 7, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 154: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [220, 440, 880, 1760, 3520, 7040, 14080, 28160, 56320, 112640, 225280, 450560, 901120, 1802240, 3604480, 7208960, 14417920, 28835840, 57671680, 115343360]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [220, 440, 880, 1760, 3520, 7040, 14080, 28160, 56320, 112640, 225280, 450560, 901120, 1802240, 3604480, 7208960, 14417920, 28835840, 57671680, 115343360]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [15, 9, 8, 7, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [15, 9, 8, 7, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [65535, 65536, 131071, 131072, 262143, 262144]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [65535, 65536, 131071, 131072, 262143, 262144]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(deliciousness = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 15
    assert candidate(deliciousness = [0, 0, 0, 0, 0, 0]) == 0
    assert candidate(deliciousness = [0, 0]) == 0
    assert candidate(deliciousness = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 6
    assert candidate(deliciousness = [1048576, 1048576, 524288, 524288, 262144, 262144]) == 3
    assert candidate(deliciousness = [1]) == 0
    assert candidate(deliciousness = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(deliciousness = [1048576, 1048576]) == 1
    assert candidate(deliciousness = [13, 100, 13]) == 0
    assert candidate(deliciousness = [1, 3, 5, 7, 9]) == 4
    assert candidate(deliciousness = [1, 1, 1, 3, 3, 3, 7]) == 15
    assert candidate(deliciousness = [1, 0, 0, 0, 0]) == 4
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32]) == 0
    assert candidate(deliciousness = [1023, 1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]) == 12
    assert candidate(deliciousness = [1048576, 1, 1, 1, 1]) == 6
    assert candidate(deliciousness = [1, 1048575, 1048575, 1048576]) == 2
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 0
    assert candidate(deliciousness = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 5
    assert candidate(deliciousness = [1, 100000, 200000, 300000, 400000]) == 0
    assert candidate(deliciousness = [220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220]) == 0
    assert candidate(deliciousness = [0, 0, 0, 0]) == 0
    assert candidate(deliciousness = [1048576, 1048576]) == 1
    assert candidate(deliciousness = [2, 2, 2, 2, 2]) == 10
    assert candidate(deliciousness = [1, 1048575]) == 1
    assert candidate(deliciousness = [0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 9]) == 10
    assert candidate(deliciousness = [31, 1, 4, 3, 12, 13, 8, 16, 7]) == 5
    assert candidate(deliciousness = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(deliciousness = [1048575, 1048576, 524287, 524288, 262143, 262144, 131071, 131072, 65535, 65536, 32767, 32768, 16383, 16384, 8191, 8192, 4095, 4096, 2047, 2048, 1023, 1024, 511, 512, 255, 256, 127, 128, 63, 64, 31, 32, 15, 16, 7, 8, 3, 4, 1, 2, 0, 0, 0, 0, 0, 0]) == 145
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(deliciousness = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(deliciousness = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570]) == 0
    assert candidate(deliciousness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 28
    assert candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 11
    assert candidate(deliciousness = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 31, 31, 31]) == 249
    assert candidate(deliciousness = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 20
    assert candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 3
    assert candidate(deliciousness = [5, 1, 4, 3, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 15
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
    assert candidate(deliciousness = [21, 1, 17, 3, 9, 18, 25, 33]) == 1
    assert candidate(deliciousness = [1023, 1024, 2047, 2048, 3071, 3072, 4095, 4096]) == 1
    assert candidate(deliciousness = [1023, 1024, 1025, 2047, 2048, 2049, 4095, 4096, 4097]) == 3
    assert candidate(deliciousness = [1, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455]) == 9
    assert candidate(deliciousness = [1023, 1024, 2047, 2048, 4095, 4096, 8191, 8192]) == 0
    assert candidate(deliciousness = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127]) == 0
    assert candidate(deliciousness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 14
    assert candidate(deliciousness = [5, 15, 1, 3, 7, 9, 11, 13]) == 7
    assert candidate(deliciousness = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047, 2047]) == 0
    assert candidate(deliciousness = [1048575, 1048576, 2097151, 2097152, 4194303, 4194304]) == 0
    assert candidate(deliciousness = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 19
    assert candidate(deliciousness = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575]) == 0
    assert candidate(deliciousness = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 10
    assert candidate(deliciousness = [1023, 1024, 2047, 2048, 4095, 4096]) == 0
    assert candidate(deliciousness = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151]) == 21
    assert candidate(deliciousness = [21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0
    assert candidate(deliciousness = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 0
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(deliciousness = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 0
    assert candidate(deliciousness = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 16
    assert candidate(deliciousness = [1, 1048575, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 1
    assert candidate(deliciousness = [0, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0
    assert candidate(deliciousness = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15
    assert candidate(deliciousness = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512]) == 10
    assert candidate(deliciousness = [1, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 13
    assert candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 3
    assert candidate(deliciousness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(deliciousness = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 100
    assert candidate(deliciousness = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128]) == 0
    assert candidate(deliciousness = [3, 5, 7, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 154
    assert candidate(deliciousness = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 5
    assert candidate(deliciousness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 90
    assert candidate(deliciousness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 0
    assert candidate(deliciousness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 12
    assert candidate(deliciousness = [220, 440, 880, 1760, 3520, 7040, 14080, 28160, 56320, 112640, 225280, 450560, 901120, 1802240, 3604480, 7208960, 14417920, 28835840, 57671680, 115343360]) == 0
    assert candidate(deliciousness = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]) == 0
    assert candidate(deliciousness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(deliciousness = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 61
    assert candidate(deliciousness = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 0
    assert candidate(deliciousness = [1, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 11
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(deliciousness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19
    assert candidate(deliciousness = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 26
    assert candidate(deliciousness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 65
    assert candidate(deliciousness = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 41
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
    assert candidate(deliciousness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 26
    assert candidate(deliciousness = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 8
    assert candidate(deliciousness = [15, 9, 8, 7, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 135
    assert candidate(deliciousness = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 1, 1]) == 6
    assert candidate(deliciousness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 190
    assert candidate(deliciousness = [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]) == 0
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0
    assert candidate(deliciousness = [524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 20
    assert candidate(deliciousness = [65535, 65536, 131071, 131072, 262143, 262144]) == 0
    assert candidate(deliciousness = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(deliciousness = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 3
    assert candidate(deliciousness = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 12
    assert candidate(deliciousness = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 0


