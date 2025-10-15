def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 1, 3, 4]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 1, 3, 4]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 2, 1, 5, 4]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 2, 1, 5, 4]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 1, 2, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 1, 2, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 7, 3, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 7, 3, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 8, 4, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 8, 4, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 64594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 64594: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 15, 7, 3]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 15, 7, 3]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 64594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 64594: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 859
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 859: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 6561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 6561: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 32767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 32767: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 16203
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 16203: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 31, 15, 7, 3, 1, 31, 15, 7, 3, 1, 31]) == 61440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 31, 15, 7, 3, 1, 31, 15, 7, 3, 1, 31]) == 61440: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 32297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 32297: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0]) == 64812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0]) == 64812: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 7, 15, 3, 1, 8, 2, 4]) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 7, 15, 3, 1, 8, 2, 4]) == 205: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32297: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 64897
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 64897: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 11, 5, 1, 11, 5, 1, 11, 5, 1, 11, 5, 1]) == 14880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 11, 5, 1, 11, 5, 1, 11, 5, 1, 11, 5, 1]) == 14880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1023]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1023]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 7, 3, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 7, 3, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 511: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 64594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 64594: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 512: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 28, 29, 30, 31, 30, 29, 28]) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 28, 29, 30, 31, 30, 29, 28]) == 228: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 22336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 22336: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 257
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 257: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3, 1, 31, 14, 7, 3, 1]) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3, 1, 31, 14, 7, 3, 1]) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 62449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 62449: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 7, 3, 1, 14, 7, 3, 1]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 7, 3, 1, 14, 7, 3, 1]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 6561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 6561: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144]) == 48108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144]) == 48108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 6561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 6561: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 512: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16384: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 10, 14, 15, 1, 2, 8, 4, 6, 7, 11, 12, 13, 9]) == 32297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 10, 14, 15, 1, 2, 8, 4, 6, 7, 11, 12, 13, 9]) == 32297: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 48609
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 48609: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 59421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 59421: {e}')
    
    total += 1
    try:
        result = candidate(nums = [127, 63, 31, 15, 7, 3, 1]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [127, 63, 31, 15, 7, 3, 1]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40]) == 59922
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40]) == 59922: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000]) == 2592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000]) == 2592: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 63, 127, 255, 511, 1023, 1, 2, 4, 8, 16, 32]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 63, 127, 255, 511, 1023, 1, 2, 4, 8, 16, 32]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32767]) == 32769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32767]) == 32769: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 63775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 63775: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 32297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 32297: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3]) == 12611
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3]) == 12611: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 2, 1, 6, 5, 4, 8, 10, 9, 11, 12, 13, 14, 15, 16]) == 32297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 2, 1, 6, 5, 4, 8, 10, 9, 11, 12, 13, 14, 15, 16]) == 32297: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 14, 7, 1, 9, 3, 11]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 14, 7, 1, 9, 3, 11]) == 102: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [15, 15, 15]) == 7
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 255
    assert candidate(nums = [3, 2, 1, 5]) == 6
    assert candidate(nums = [6, 2, 1, 3, 4]) == 17
    assert candidate(nums = [6, 2, 1, 5, 4]) == 17
    assert candidate(nums = [5, 1, 1, 2, 5]) == 12
    assert candidate(nums = [1, 3, 5, 7, 9]) == 10
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [2, 2, 2]) == 7
    assert candidate(nums = [1, 3, 7, 15, 31]) == 16
    assert candidate(nums = [15, 15, 15, 15]) == 15
    assert candidate(nums = [1, 2, 4, 8]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50]) == 16
    assert candidate(nums = [5, 5, 5, 5, 5]) == 31
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65535
    assert candidate(nums = [15, 7, 3, 1]) == 8
    assert candidate(nums = [16, 8, 4, 2, 1]) == 1
    assert candidate(nums = [3, 1]) == 2
    assert candidate(nums = [1, 3, 7, 15]) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 255
    assert candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 65535
    assert candidate(nums = [10, 20, 30, 40]) == 5
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 1]) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 64594
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == 52
    assert candidate(nums = [5, 10, 15, 20, 25, 30]) == 44
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == 1
    assert candidate(nums = [8, 4, 2, 1, 15, 7, 3]) == 85
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 65535
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]) == 32768
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 64594
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 859
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 6561
    assert candidate(nums = [16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384]) == 65535
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 32767
    assert candidate(nums = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 1
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 16203
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32]) == 1
    assert candidate(nums = [31, 15, 7, 3, 1, 31, 15, 7, 3, 1, 31, 15, 7, 3, 1, 31]) == 61440
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 32297
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0]) == 64812
    assert candidate(nums = [13, 7, 15, 3, 1, 8, 2, 4]) == 205
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32297
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 64897
    assert candidate(nums = [1, 5, 11, 5, 1, 11, 5, 1, 11, 5, 1, 11, 5, 1]) == 14880
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1023]) == 32768
    assert candidate(nums = [15, 7, 3, 1]) == 8
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 255
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 511
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 1
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 65535
    assert candidate(nums = [15, 15, 15, 15, 15]) == 31
    assert candidate(nums = [31, 15, 7, 3, 1]) == 16
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 1
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 128
    assert candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 64594
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 32768
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 512
    assert candidate(nums = [31, 28, 29, 30, 31, 30, 29, 28]) == 228
    assert candidate(nums = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]) == 65535
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 171
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 109
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 65535
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384]) == 21
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) == 22336
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 255
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64]) == 109
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 257
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65535
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40]) == 150
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 1
    assert candidate(nums = [31, 14, 7, 3, 1, 31, 14, 7, 3, 1]) == 768
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31]) == 32768
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255]) == 255
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 62449
    assert candidate(nums = [14, 7, 3, 1, 14, 7, 3, 1]) == 189
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 65535
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562]) == 13
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8]) == 255
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1]) == 32768
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 6561
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144]) == 48108
    assert candidate(nums = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 32768
    assert candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 6561
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == 170
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 65535
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 512
    assert candidate(nums = [32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 16384
    assert candidate(nums = [5, 3, 10, 14, 15, 1, 2, 8, 4, 6, 7, 11, 12, 13, 9]) == 32297
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 48609
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 59421
    assert candidate(nums = [127, 63, 31, 15, 7, 3, 1]) == 64
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40]) == 59922
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000]) == 2592
    assert candidate(nums = [31, 15, 7, 3, 1, 63, 127, 255, 511, 1023, 1, 2, 4, 8, 16, 32]) == 32768
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 1
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 128
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32767]) == 32769
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72]) == 109
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535]) == 32768
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 63775
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1]) == 1
    assert candidate(nums = [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]) == 65535
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 65535
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 32297
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3]) == 12611
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127]) == 64
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 1
    assert candidate(nums = [7, 3, 2, 1, 6, 5, 4, 8, 10, 9, 11, 12, 13, 14, 15, 16]) == 32297
    assert candidate(nums = [12, 14, 7, 1, 9, 3, 11]) == 102


