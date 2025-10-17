def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 3071, 4095, 5119]) == 7168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 3071, 4095, 5119]) == 7168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100001, 100002, 100003]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100001, 100002, 100003]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1024, 2047, 2048]) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1024, 2047, 2048]) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 520, 2500, 3000]) == 1020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 520, 2500, 3000]) == 1020: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1023, 1048, 1071, 1094, 1117, 1140, 1163, 1186, 1209]) == 2032
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1023, 1048, 1071, 1094, 1117, 1140, 1163, 1186, 1209]) == 2032: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]) == 484
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]) == 484: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 520, 1000, 1020, 1500, 1520, 2000, 2020, 2500, 2520]) == 3644
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 520, 1000, 1020, 1500, 1520, 2000, 2020, 2500, 2520]) == 3644: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 393216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 393216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 16397, 16398, 16399, 16400, 16401, 16402, 16403, 16404, 16405, 16406, 16407, 16408, 16409, 16410, 16411, 16412, 16413, 16414, 16415]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 16397, 16398, 16399, 16400, 16401, 16402, 16403, 16404, 16405, 16406, 16407, 16408, 16409, 16410, 16411, 16412, 16413, 16414, 16415]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 29, 47, 71, 97, 131, 167, 211, 257, 307, 359, 419, 479, 541, 601]) == 1018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 29, 47, 71, 97, 131, 167, 211, 257, 307, 359, 419, 479, 541, 601]) == 1018: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968]) == 2112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968]) == 2112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987]) == 130766
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987]) == 130766: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240]) == 15360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240]) == 15360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10050, 10100, 10150, 10200, 10250, 10300, 10350, 10400, 10450]) == 4068
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10050, 10100, 10150, 10200, 10250, 10300, 10350, 10400, 10450]) == 4068: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061]) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061]) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 1992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 1992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234]) == 990651
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234]) == 990651: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570, 1048569, 1048568]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570, 1048569, 1048568]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230, 1353]) == 1963
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230, 1353]) == 1963: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 253: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000]) == 1367488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000]) == 1367488: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 393216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 393216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 968: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 21845, 21846, 21847, 21848, 21849, 21850, 21851, 21852, 21853, 21854, 21855]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 21845, 21846, 21847, 21848, 21849, 21850, 21851, 21852, 21853, 21854, 21855]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]) == 15360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]) == 15360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 7, 14, 15, 30, 31, 62, 63, 126, 127, 254, 255, 510, 511, 1022, 1023, 2046, 2047, 4094, 4095]) == 2049
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 7, 14, 15, 30, 31, 62, 63, 126, 127, 254, 255, 510, 511, 1022, 1023, 2046, 2047, 4094, 4095]) == 2049: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 24576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 24576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 123457, 123458, 123459, 123460, 123461, 123462, 123463, 123464, 123465, 123466, 123467, 123468, 123469, 123470]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 123457, 123458, 123459, 123460, 123461, 123462, 123463, 123464, 123465, 123466, 123467, 123468, 123469, 123470]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056]) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056]) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(nums = [134217727, 134217728, 134217729, 134217730, 134217731, 134217732, 134217733, 134217734, 134217735]) == 2097151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [134217727, 134217728, 134217729, 134217730, 134217731, 134217732, 134217733, 134217734, 134217735]) == 2097151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [220, 440, 880, 1760, 3520, 7040, 14080, 28160, 56320, 112640, 225280]) == 182272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [220, 440, 880, 1760, 3520, 7040, 14080, 28160, 56320, 112640, 225280]) == 182272: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191, 9215, 10239, 11263, 12287, 13311, 14335, 15359]) == 15360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191, 9215, 10239, 11263, 12287, 13311, 14335, 15359]) == 15360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8191, 8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200]) == 16383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8191, 8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200]) == 16383: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100002, 100004, 100006, 100008, 100010, 100012, 100014, 100016, 100018, 100020, 100022, 100024, 100026, 100028, 100030, 100032, 100034, 100036, 100038, 100040, 100042, 100044, 100046, 100048]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100002, 100004, 100006, 100008, 100010, 100012, 100014, 100016, 100018, 100020, 100022, 100024, 100026, 100028, 100030, 100032, 100034, 100036, 100038, 100040, 100042, 100044, 100046, 100048]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191, 9215, 10239]) == 15360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191, 9215, 10239]) == 15360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 1558208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 1558208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [150000, 150001, 150002, 150003, 150004, 150005, 150006, 150007, 150008, 150009, 150010]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [150000, 150001, 150002, 150003, 150004, 150005, 150006, 150007, 150008, 150009, 150010]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 210, 220, 230, 240, 250]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 210, 220, 230, 240, 250]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 14, 23, 37, 59, 92, 144, 233, 377]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 14, 23, 37, 59, 92, 144, 233, 377]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 23, 45, 79, 121, 177, 247, 327, 417, 517, 627, 747, 877, 1017]) == 978
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 23, 45, 79, 121, 177, 247, 327, 417, 517, 627, 747, 877, 1017]) == 978: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000]) == 1780896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000]) == 1780896: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 15752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 15752: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [268435455, 268435456, 268435457, 268435458, 268435459, 268435460, 268435461, 268435462, 268435463]) == 2097151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [268435455, 268435456, 268435457, 268435458, 268435459, 268435460, 268435461, 268435462, 268435463]) == 2097151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 795
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 795: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52, 53, 54, 60, 61, 62, 63, 64]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52, 53, 54, 60, 61, 62, 63, 64]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [314159, 271828, 141421, 161803, 707106, 353553, 414213]) == 1027891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [314159, 271828, 141421, 161803, 707106, 353553, 414213]) == 1027891: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 32768, 49152, 65536, 81920, 98304, 114688, 131072, 147456, 163840]) == 245760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 32768, 49152, 65536, 81920, 98304, 114688, 131072, 147456, 163840]) == 245760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 12463
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 12463: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 12288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 12288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]) == 1572864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]) == 1572864: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1048575, 2, 1048574, 3, 1048573, 4, 1048572, 5, 1048571]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1048575, 2, 1048574, 3, 1048573, 4, 1048572, 5, 1048571]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200, 8201, 8202]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200, 8201, 8202]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]) == 996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]) == 996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360]) == 15360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360]) == 15360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 15464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 15464: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 1558208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 1558208: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 192
    assert candidate(nums = [1023, 2047, 3071, 4095, 5119]) == 7168
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [100000, 100001, 100002, 100003]) == 3
    assert candidate(nums = [2, 4, 6, 8, 10, 12]) == 14
    assert candidate(nums = [1, 1, 1, 1]) == 0
    assert candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023]) == 0
    assert candidate(nums = [1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 768
    assert candidate(nums = [1, 3, 5, 7, 9]) == 14
    assert candidate(nums = [15, 30, 45, 60, 75, 90]) == 119
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 14
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1023, 1024, 2047, 2048]) == 4095
    assert candidate(nums = [10, 100]) == 0
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383]) == 0
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 0
    assert candidate(nums = [500, 520, 2500, 3000]) == 1020
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == 48
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1536
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000]) == 0
    assert candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [15, 30, 45, 60, 75]) == 119
    assert candidate(nums = [1000, 1023, 1048, 1071, 1094, 1117, 1140, 1163, 1186, 1209]) == 2032
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 30
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 125
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1992
    assert candidate(nums = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]) == 484
    assert candidate(nums = [500, 520, 1000, 1020, 1500, 1520, 2000, 2020, 2500, 2520]) == 3644
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 393216
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
    assert candidate(nums = [16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391]) == 7
    assert candidate(nums = [16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 16397, 16398, 16399, 16400, 16401, 16402, 16403, 16404, 16405, 16406, 16407, 16408, 16409, 16410, 16411, 16412, 16413, 16414, 16415]) == 31
    assert candidate(nums = [13, 29, 47, 71, 97, 131, 167, 211, 257, 307, 359, 419, 479, 541, 601]) == 1018
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31
    assert candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968]) == 2112
    assert candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987]) == 130766
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 61
    assert candidate(nums = [2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 62
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215]) == 0
    assert candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240]) == 15360
    assert candidate(nums = [10000, 10050, 10100, 10150, 10200, 10250, 10300, 10350, 10400, 10450]) == 4068
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
    assert candidate(nums = [127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]) == 0
    assert candidate(nums = [2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061]) == 4095
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 30
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 1992
    assert candidate(nums = [1, 2147483647, 2147483646, 2147483645, 2147483644, 2147483643, 2147483642, 2147483641]) == 7
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]) == 0
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]) == 255
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234]) == 990651
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383]) == 0
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047]) == 0
    assert candidate(nums = [1048575, 1048574, 1048573, 1048572, 1048571, 1048570, 1048569, 1048568]) == 7
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225]) == 255
    assert candidate(nums = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230, 1353]) == 1963
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]) == 62
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 253
    assert candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 126
    assert candidate(nums = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000]) == 1367488
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40]) == 61
    assert candidate(nums = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 393216
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 968
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 24576
    assert candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009]) == 15
    assert candidate(nums = [1, 21845, 21846, 21847, 21848, 21849, 21850, 21851, 21852, 21853, 21854, 21855]) == 15
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 786432
    assert candidate(nums = [1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 0
    assert candidate(nums = [1, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]) == 15360
    assert candidate(nums = [1, 2, 3, 6, 7, 14, 15, 30, 31, 62, 63, 126, 127, 254, 255, 510, 511, 1022, 1023, 2046, 2047, 4094, 4095]) == 2049
    assert candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 24576
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
    assert candidate(nums = [123456, 123457, 123458, 123459, 123460, 123461, 123462, 123463, 123464, 123465, 123466, 123467, 123468, 123469, 123470]) == 15
    assert candidate(nums = [2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056]) == 4095
    assert candidate(nums = [134217727, 134217728, 134217729, 134217730, 134217731, 134217732, 134217733, 134217734, 134217735]) == 2097151
    assert candidate(nums = [220, 440, 880, 1760, 3520, 7040, 14080, 28160, 56320, 112640, 225280]) == 182272
    assert candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191, 9215, 10239, 11263, 12287, 13311, 14335, 15359]) == 15360
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 126
    assert candidate(nums = [8191, 8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200]) == 16383
    assert candidate(nums = [100000, 100002, 100004, 100006, 100008, 100010, 100012, 100014, 100016, 100018, 100020, 100022, 100024, 100026, 100028, 100030, 100032, 100034, 100036, 100038, 100040, 100042, 100044, 100046, 100048]) == 126
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [1023, 2047, 3071, 4095, 5119, 6143, 7167, 8191, 9215, 10239]) == 15360
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 250
    assert candidate(nums = [1, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 1558208
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 250
    assert candidate(nums = [150000, 150001, 150002, 150003, 150004, 150005, 150006, 150007, 150008, 150009, 150010]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 210, 220, 230, 240, 250]) == 122
    assert candidate(nums = [5, 9, 14, 23, 37, 59, 92, 144, 233, 377]) == 400
    assert candidate(nums = [1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]) == 0
    assert candidate(nums = [7, 23, 45, 79, 121, 177, 247, 327, 417, 517, 627, 747, 877, 1017]) == 978
    assert candidate(nums = [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000]) == 1780896
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 15752
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31
    assert candidate(nums = [268435455, 268435456, 268435457, 268435458, 268435459, 268435460, 268435461, 268435462, 268435463]) == 2097151
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 795
    assert candidate(nums = [10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52, 53, 54, 60, 61, 62, 63, 64]) == 127
    assert candidate(nums = [314159, 271828, 141421, 161803, 707106, 353553, 414213]) == 1027891
    assert candidate(nums = [16384, 32768, 49152, 65536, 81920, 98304, 114688, 131072, 147456, 163840]) == 245760
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 12463
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 12288
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 62
    assert candidate(nums = [16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]) == 1572864
    assert candidate(nums = [1, 1048575, 2, 1048574, 3, 1048573, 4, 1048572, 5, 1048571]) == 7
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 6144
    assert candidate(nums = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992]) == 31
    assert candidate(nums = [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032]) == 15
    assert candidate(nums = [511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]) == 0
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1536
    assert candidate(nums = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009]) == 15
    assert candidate(nums = [8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200, 8201, 8202]) == 15
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]) == 996
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 0
    assert candidate(nums = [1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360]) == 15360
    assert candidate(nums = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 786432
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 15464
    assert candidate(nums = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 31
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == 1558208


