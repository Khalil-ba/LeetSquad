def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 7, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 7, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 0, 1, 4]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 0, 1, 4]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 32, 48, 64]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 32, 48, 64]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 631: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255]) == 817
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255]) == 817: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 258: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1261: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224]) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224]) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 16231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 16231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 943: {e}')
    
    total += 1
    try:
        result = candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0]) == 6760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0]) == 6760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 29, 17, 5, 23, 31, 47, 19, 2, 7, 11, 13, 17, 19, 23, 29, 31]) == 546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 29, 17, 5, 23, 31, 47, 19, 2, 7, 11, 13, 17, 19, 23, 29, 31]) == 546: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == 3036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == 3036: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 13830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 13830: {e}')
    
    total += 1
    try:
        result = candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 217: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 240, 240, 15, 240, 15, 240, 15, 240]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 240, 240, 15, 240, 15, 240, 15, 240]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 744: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 631: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 7, 3, 1, 0, 31, 14, 6, 2, 0, 255, 127]) == 872
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 7, 3, 1, 0, 31, 14, 6, 2, 0, 255, 127]) == 872: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 1320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 1320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 20, 25, 30, 35, 40]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 20, 25, 30, 35, 40]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 3360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 3360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == 672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == 672: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == 684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == 684: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 128, 64, 32, 16, 8]) == 3751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 128, 64, 32, 16, 8]) == 3751: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2401: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1015: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1440: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 4896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 4896: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 3360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 3360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5064: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2401: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 17, 85, 257, 681, 2049, 5121, 13633, 34609, 88417]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 17, 85, 257, 681, 2049, 5121, 13633, 34609, 88417]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 14, 7, 3, 1, 12, 6, 3, 1, 10, 5, 2, 1]) == 2868
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 14, 7, 3, 1, 12, 6, 3, 1, 10, 5, 2, 1]) == 2868: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 3420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 3420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 331: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 547
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 547: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 240, 10, 100, 5, 60]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 240, 10, 100, 5, 60]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(nums = [85, 170, 51, 204, 68, 136, 34, 0, 255, 128, 64, 32, 16, 8, 4, 2, 1]) == 4285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [85, 170, 51, 204, 68, 136, 34, 0, 255, 128, 64, 32, 16, 8, 4, 2, 1]) == 4285: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 192, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 192]) == 1897
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 192, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 192]) == 1897: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208]) == 1638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208]) == 1638: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 28791
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 28791: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 2352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 2352: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 217: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 469: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 0, 0]) == 27
    assert candidate(nums = [5, 3, 7, 10]) == 18
    assert candidate(nums = [15, 15, 15, 15]) == 0
    assert candidate(nums = [5, 3, 0, 1, 4]) == 91
    assert candidate(nums = [1, 2, 3, 4]) == 48
    assert candidate(nums = [5, 10, 15, 20]) == 30
    assert candidate(nums = [1, 0, 1, 0, 1, 0]) == 189
    assert candidate(nums = [1, 2, 4, 8]) == 60
    assert candidate(nums = [2, 1, 3]) == 12
    assert candidate(nums = [16, 32, 48, 64]) == 48
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
    assert candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 631
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255]) == 817
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == 210
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 258
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 990
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 1261
    assert candidate(nums = [255, 254, 253, 252, 251, 250, 249, 248]) == 0
    assert candidate(nums = [7, 14, 28, 56, 112, 224]) == 132
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 16231
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1680
    assert candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 0
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0]) == 943
    assert candidate(nums = [128, 64, 32, 16, 8, 4, 2, 1, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0]) == 6760
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 432
    assert candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 0
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128]) == 2400
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1680
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 180
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56]) == 216
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [13, 29, 17, 5, 23, 31, 47, 19, 2, 7, 11, 13, 17, 19, 23, 29, 31]) == 546
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 990
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35]) == 30
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220]) == 3036
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 13830
    assert candidate(nums = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127]) == 0
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 217
    assert candidate(nums = [15, 240, 240, 15, 240, 15, 240, 15, 240]) == 540
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 744
    assert candidate(nums = [16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 631
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 504
    assert candidate(nums = [15, 7, 3, 1, 0, 31, 14, 6, 2, 0, 255, 127]) == 872
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 1320
    assert candidate(nums = [15, 20, 25, 30, 35, 40]) == 84
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105]) == 0
    assert candidate(nums = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 990
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 3360
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 720
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1]) == 672
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == 684
    assert candidate(nums = [255, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 128, 64, 32, 16, 8]) == 3751
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2401
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 180
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1015
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1440
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 4896
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 3360
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5064
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2401
    assert candidate(nums = [1, 5, 17, 85, 257, 681, 2049, 5121, 13633, 34609, 88417]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 504
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]) == 0
    assert candidate(nums = [8, 4, 2, 1, 14, 7, 3, 1, 12, 6, 3, 1, 10, 5, 2, 1]) == 2868
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 3420
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 331
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == 0
    assert candidate(nums = [8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 547
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 240
    assert candidate(nums = [15, 240, 10, 100, 5, 60]) == 114
    assert candidate(nums = [85, 170, 51, 204, 68, 136, 34, 0, 255, 128, 64, 32, 16, 8, 4, 2, 1]) == 4285
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 432
    assert candidate(nums = [255, 192, 128, 64, 32, 16, 8, 4, 2, 1, 0, 255, 192]) == 1897
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208]) == 1638
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 1998
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 28791
    assert candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 2352
    assert candidate(nums = [21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845, 21845]) == 0
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1, 0]) == 217
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0]) == 469


