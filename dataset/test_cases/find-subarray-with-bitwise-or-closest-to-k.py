def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1000000000],k = 500000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000],k = 500000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40],k = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40],k = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000],k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 7, 9],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 7, 9],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3],k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3],k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000],k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 65) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 65) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 255) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 255) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32],k = 31) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32],k = 31) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 9, 11, 13],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 9, 11, 13],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 5],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 5],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431],k = 10000000) == 1611393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431],k = 10000000) == 1611393: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 500) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 500) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 100) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 100) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],k = 110) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],k = 110) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 128, 64, 32, 16, 8, 4, 2, 1],k = 127) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 128, 64, 32, 16, 8, 4, 2, 1],k = 127) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728],k = 268435456) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728],k = 268435456) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 511) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 511) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575],k = 1048574) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575],k = 1048574) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 10, 15, 20],k = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 10, 15, 20],k = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 135792468, 246813579, 1112131415],k = 333333333) == 85994358
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 135792468, 246813579, 1112131415],k = 333333333) == 85994358: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 20, 40, 80, 160, 320, 640, 1280],k = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 20, 40, 80, 160, 320, 640, 1280],k = 1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 100000) == 1696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 100000) == 1696: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999994) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999994) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216],k = 10000000) == 1611392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216],k = 10000000) == 1611392: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 500) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 500) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 64) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 64) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 40) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 40) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 100) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 100) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1],k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1],k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999994) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999994) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31],k = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31],k = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 256, 512, 1024, 2048, 4096],k = 1000) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 256, 512, 1024, 2048, 4096],k = 1000) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 2, 5, 10, 14],k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 2, 5, 10, 14],k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 512) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 512) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256],k = 200) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256],k = 200) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 750) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 750) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1023) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1023) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61],k = 42) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61],k = 42) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 77) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 77) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 1, 8, 9, 10, 5],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 1, 8, 9, 10, 5],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 1048576) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 1048576) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 127) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 127) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 33) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 33) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 15, 8, 5, 2, 7, 11, 6, 4],k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 15, 8, 5, 2, 7, 11, 6, 4],k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 2, 5, 6, 1, 4, 8, 9],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 2, 5, 6, 1, 4, 8, 9],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 550) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 550) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 15, 7, 3, 1],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 15, 7, 3, 1],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 1073741824) == 1071644673
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 1073741824) == 1071644673: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 42) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 42) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 85) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 85) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 1) == 2147483646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 1) == 2147483646: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643],k = 2147483640) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643],k = 2147483640) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1024) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1024) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 2048) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 2048) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 28) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 28) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],k = 16384) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],k = 16384) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1023) == 1022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1023) == 1022: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 159) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 159) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 7, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 27, 29, 30, 31],k = 28) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 7, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 27, 29, 30, 31],k = 28) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1000000000],k = 500000000) == 500000000
    assert candidate(nums = [10, 20, 30, 40],k = 25) == 5
    assert candidate(nums = [1],k = 10) == 9
    assert candidate(nums = [5, 6, 7, 8, 9],k = 7) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 1000000000) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 0
    assert candidate(nums = [3, 5, 7, 9],k = 8) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],k = 25) == 5
    assert candidate(nums = [1, 1, 1, 1, 1],k = 2) == 1
    assert candidate(nums = [7, 8, 9],k = 5) == 2
    assert candidate(nums = [1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [5, 3, 6, 7, 9],k = 4) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3],k = 0) == 1
    assert candidate(nums = [2, 4, 6, 8, 10],k = 7) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 0
    assert candidate(nums = [1000000000],k = 1000000000) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 65) == 3
    assert candidate(nums = [1, 3, 1, 3],k = 2) == 1
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [3, 3, 3, 3, 3],k = 3) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 255) == 0
    assert candidate(nums = [2, 4, 8, 16, 32],k = 31) == 1
    assert candidate(nums = [5, 7, 9, 11, 13],k = 8) == 1
    assert candidate(nums = [1, 2, 4, 5],k = 3) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431],k = 10000000) == 1611393
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 500) == 11
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 100) == 27
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5],k = 3) == 2
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],k = 1000000000) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000) == 8
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1) == 1
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180],k = 110) == 1
    assert candidate(nums = [31, 15, 7, 3, 1, 128, 64, 32, 16, 8, 4, 2, 1],k = 127) == 0
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728],k = 268435456) == 256
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 511) == 0
    assert candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575],k = 1048574) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 0
    assert candidate(nums = [3, 5, 7, 10, 15, 20],k = 12) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [123456789, 987654321, 135792468, 246813579, 1112131415],k = 333333333) == 85994358
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 1
    assert candidate(nums = [1, 5, 10, 20, 40, 80, 160, 320, 640, 1280],k = 1000) == 8
    assert candidate(nums = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048],k = 100000) == 1696
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 14) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 3
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999994) == 1
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 20) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216],k = 10000000) == 1611392
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 3
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 500) == 11
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 64) == 1
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 1000000000) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 40) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 16) == 1
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35],k = 20) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 5
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 3
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 100) == 27
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1024) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 4
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 30) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 10) == 3
    assert candidate(nums = [8, 4, 2, 1, 16, 8, 4, 2, 1],k = 10) == 2
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],k = 500) == 4
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999994) == 1
    assert candidate(nums = [31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31],k = 16) == 1
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 256, 512, 1024, 2048, 4096],k = 1000) == 23
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000) == 8
    assert candidate(nums = [3, 7, 2, 5, 10, 14],k = 6) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 1) == 6
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000001) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 512) == 1
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 25) == 2
    assert candidate(nums = [8, 16, 32, 64, 128, 256],k = 200) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 750) == 14
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 50) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 20) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1023) == 1
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 10) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61],k = 42) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 77) == 2
    assert candidate(nums = [3, 6, 1, 8, 9, 10, 5],k = 7) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 0
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 1048576) == 1024
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 127) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 33) == 2
    assert candidate(nums = [9, 3, 15, 8, 5, 2, 7, 11, 6, 4],k = 13) == 0
    assert candidate(nums = [3, 7, 2, 5, 6, 1, 4, 8, 9],k = 12) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 550) == 42
    assert candidate(nums = [31, 15, 7, 3, 1],k = 4) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 1073741824) == 1071644673
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 500) == 4
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 500) == 4
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 42) == 3
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 85) == 6
    assert candidate(nums = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647],k = 1) == 2147483646
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 1000000000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 10) == 1
    assert candidate(nums = [2147483647, 2147483646, 2147483645, 2147483644, 2147483643],k = 2147483640) == 3
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1024) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 2048) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 28) == 1
    assert candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],k = 20) == 0
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],k = 16384) == 0
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 9) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 100) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1023) == 1022
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 1
    assert candidate(nums = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 159) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 27, 29, 30, 31],k = 28) == 1
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0


