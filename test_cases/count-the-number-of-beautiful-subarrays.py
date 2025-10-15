def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2, 12, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2, 12, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 10, 14, 16]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 10, 14, 16]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 14, 4, 8, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 14, 4, 8, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 1, 2, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 1, 2, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 33, 45, 57, 69, 81, 93, 105, 117, 129]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 33, 45, 57, 69, 81, 93, 105, 117, 129]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 15, 6, 9, 2, 8, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 15, 6, 9, 2, 8, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1023, 511, 511, 255, 255, 127, 127, 63, 63, 31, 31, 15, 15, 7, 7, 3, 3, 1, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1023, 511, 511, 255, 255, 127, 127, 63, 63, 31, 31, 15, 15, 7, 7, 3, 3, 1, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 10, 14, 12, 6, 4, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 10, 14, 12, 6, 4, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1023, 511, 255]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1023, 511, 255]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 1, 3, 9, 6, 2, 8, 4, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 1, 3, 9, 6, 2, 8, 4, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 255]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 255]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 11, 7, 3, 5, 11, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 11, 7, 3, 5, 11, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104729, 209458, 418916, 837832, 1675664, 3351328, 6702656, 13405312, 26810624, 53621248]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104729, 209458, 418916, 837832, 1675664, 3351328, 6702656, 13405312, 26810624, 53621248]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 15, 31]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 15, 31]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 17, 5, 10, 14, 6, 9, 3, 11, 15, 2, 7, 13]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 17, 5, 10, 14, 6, 9, 3, 11, 15, 2, 7, 13]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 1, 2, 4, 8, 16, 32]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 1, 2, 4, 8, 16, 32]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 28, 19, 5, 11, 23, 17, 7, 9, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 28, 19, 5, 11, 23, 17, 7, 9, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 3, 2, 5, 3, 7, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 3, 2, 5, 3, 7, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 14, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 14, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 15, 28, 21, 24, 13, 26, 19]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 15, 28, 21, 24, 13, 26, 19]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 17, 15, 23, 29, 31, 19, 23, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 17, 15, 23, 29, 31, 19, 23, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3, 1, 0, 1, 3, 7, 14, 31]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3, 1, 0, 1, 3, 7, 14, 31]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 5, 12, 6, 3, 15, 8, 4, 10, 2, 7, 11, 1, 13, 14]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 5, 12, 6, 3, 15, 8, 4, 10, 2, 7, 11, 1, 13, 14]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 25, 21, 17, 13, 9, 5, 1, 1, 5, 9, 13, 17, 21, 25, 29]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 25, 21, 17, 13, 9, 5, 1, 1, 5, 9, 13, 17, 21, 25, 29]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104729, 209458, 418916, 837832, 1675664, 3351328, 6702656]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104729, 209458, 418916, 837832, 1675664, 3351328, 6702656]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 7, 2, 1, 10, 6, 8, 4, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 7, 2, 1, 10, 6, 8, 4, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 7, 15, 31, 15, 7, 3, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 7, 15, 31, 15, 7, 3, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 7, 2, 4, 6, 8, 10, 12]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 7, 2, 4, 6, 8, 10, 12]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 11, 7, 5, 3, 2, 1, 1, 2, 3, 5, 7, 11, 13]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 11, 7, 5, 3, 2, 1, 1, 2, 3, 5, 7, 11, 13]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 14, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 14, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 68, 136, 272, 544, 1088, 2176, 4352, 8704, 17408, 34816, 69632, 139264, 278528]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 68, 136, 272, 544, 1088, 2176, 4352, 8704, 17408, 34816, 69632, 139264, 278528]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 12, 5, 3, 6, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 12, 5, 3, 6, 12]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 25
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 0
    assert candidate(nums = [1, 0, 1, 0, 1]) == 6
    assert candidate(nums = [2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [8, 1, 2, 12, 7]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5]) == 6
    assert candidate(nums = [8, 8, 8, 8, 8]) == 6
    assert candidate(nums = [0, 0, 0, 0, 0]) == 15
    assert candidate(nums = [5, 5, 5, 5]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [1, 10, 4]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1]) == 6
    assert candidate(nums = [8, 12, 10, 14, 16]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 2
    assert candidate(nums = [8, 14, 4, 8, 7]) == 0
    assert candidate(nums = [0, 0, 0, 0]) == 10
    assert candidate(nums = [2, 2, 2, 2]) == 4
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 0
    assert candidate(nums = [4, 3, 1, 2, 4]) == 2
    assert candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 6
    assert candidate(nums = [1024, 512, 256, 128, 64]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 25
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2]) == 6
    assert candidate(nums = [15, 15, 15, 15, 15]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 16
    assert candidate(nums = [21, 33, 45, 57, 69, 81, 93, 105, 117, 129]) == 2
    assert candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575]) == 12
    assert candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == 5
    assert candidate(nums = [32, 16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1]) == 1
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 25
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 10
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35]) == 4
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 0
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 0
    assert candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 45
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 16
    assert candidate(nums = [5, 3, 15, 6, 9, 2, 8, 12]) == 2
    assert candidate(nums = [1023, 1023, 511, 511, 255, 255, 127, 127, 63, 63, 31, 31, 15, 15, 7, 7, 3, 3, 1, 1]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 210
    assert candidate(nums = [5, 3, 8, 10, 14, 12, 6, 4, 2, 1]) == 5
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 6
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 100
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1023, 511, 255]) == 0
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 56
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61]) == 0
    assert candidate(nums = [4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095]) == 64
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == 56
    assert candidate(nums = [13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 6
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 100
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 7
    assert candidate(nums = [5, 7, 1, 3, 9, 6, 2, 8, 4, 10]) == 2
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 0
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31]) == 5
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 255]) == 2
    assert candidate(nums = [3, 5, 11, 7, 3, 5, 11, 7]) == 1
    assert candidate(nums = [104729, 209458, 418916, 837832, 1675664, 3351328, 6702656, 13405312, 26810624, 53621248]) == 0
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 15, 31]) == 2
    assert candidate(nums = [23, 17, 5, 10, 14, 6, 9, 3, 11, 15, 2, 7, 13]) == 2
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210]) == 12
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == 1
    assert candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 100
    assert candidate(nums = [32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 1, 2, 4, 8, 16, 32]) == 7
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(nums = [31, 28, 19, 5, 11, 23, 17, 7, 9, 3]) == 2
    assert candidate(nums = [7, 5, 3, 2, 5, 3, 7, 2]) == 2
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023]) == 25
    assert candidate(nums = [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8]) == 16
    assert candidate(nums = [31, 14, 7, 14, 31]) == 0
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 16
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 0
    assert candidate(nums = [3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 45
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [31, 14, 7, 15, 28, 21, 24, 13, 26, 19]) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 49
    assert candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 16
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 25
    assert candidate(nums = [31, 17, 15, 23, 29, 31, 19, 23, 29]) == 0
    assert candidate(nums = [65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535]) == 16
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 4
    assert candidate(nums = [31, 14, 7, 3, 1, 0, 1, 3, 7, 14, 31]) == 6
    assert candidate(nums = [9, 5, 12, 6, 3, 15, 8, 4, 10, 2, 7, 11, 1, 13, 14]) == 8
    assert candidate(nums = [29, 25, 21, 17, 13, 9, 5, 1, 1, 5, 9, 13, 17, 21, 25, 29]) == 20
    assert candidate(nums = [104729, 209458, 418916, 837832, 1675664, 3351328, 6702656]) == 0
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135]) == 4
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 0
    assert candidate(nums = [5, 3, 7, 2, 1, 10, 6, 8, 4, 12]) == 3
    assert candidate(nums = [1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1]) == 70
    assert candidate(nums = [9, 3, 7, 15, 31, 15, 7, 3, 9]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 4
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 4
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 56
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [64, 32, 16, 8, 4, 2, 1, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [3, 1, 5, 7, 2, 4, 6, 8, 10, 12]) == 6
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255]) == 8
    assert candidate(nums = [13, 11, 7, 5, 3, 2, 1, 1, 2, 3, 5, 7, 11, 13]) == 9
    assert candidate(nums = [31, 14, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 27
    assert candidate(nums = [17, 34, 68, 136, 272, 544, 1088, 2176, 4352, 8704, 17408, 34816, 69632, 139264, 278528]) == 0
    assert candidate(nums = [5, 3, 6, 12, 5, 3, 6, 12]) == 4


