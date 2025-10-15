def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(label = 14) == [1, 3, 4, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 14) == [1, 3, 4, 14]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1023) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1023) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023]: {e}')
    
    total += 1
    try:
        result = candidate(label = 3) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 3) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1000000) == [1, 3, 4, 15, 17, 61, 69, 244, 279, 976, 1118, 3906, 4475, 15625, 17901, 62500, 71607, 250000, 286431, 1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1000000) == [1, 3, 4, 15, 17, 61, 69, 244, 279, 976, 1118, 3906, 4475, 15625, 17901, 62500, 71607, 250000, 286431, 1000000]: {e}')
    
    total += 1
    try:
        result = candidate(label = 255) == [1, 3, 4, 15, 16, 63, 64, 255]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 255) == [1, 3, 4, 15, 16, 63, 64, 255]: {e}')
    
    total += 1
    try:
        result = candidate(label = 4) == [1, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 4) == [1, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(label = 13) == [1, 3, 5, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 13) == [1, 3, 5, 13]: {e}')
    
    total += 1
    try:
        result = candidate(label = 15) == [1, 3, 4, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 15) == [1, 3, 4, 15]: {e}')
    
    total += 1
    try:
        result = candidate(label = 6) == [1, 2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 6) == [1, 2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(label = 11) == [1, 2, 6, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 11) == [1, 2, 6, 11]: {e}')
    
    total += 1
    try:
        result = candidate(label = 2) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 2) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(label = 64) == [1, 3, 4, 15, 16, 63, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 64) == [1, 3, 4, 15, 16, 63, 64]: {e}')
    
    total += 1
    try:
        result = candidate(label = 8) == [1, 2, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 8) == [1, 2, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1048575) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1048575) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(label = 9) == [1, 2, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 9) == [1, 2, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(label = 26) == [1, 2, 6, 10, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 26) == [1, 2, 6, 10, 26]: {e}')
    
    total += 1
    try:
        result = candidate(label = 12) == [1, 3, 5, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 12) == [1, 3, 5, 12]: {e}')
    
    total += 1
    try:
        result = candidate(label = 10) == [1, 2, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 10) == [1, 2, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(label = 7) == [1, 2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 7) == [1, 2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(label = 5) == [1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 5) == [1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(label = 16) == [1, 3, 4, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 16) == [1, 3, 4, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(label = 5000) == [1, 3, 4, 14, 19, 56, 78, 227, 312, 910, 1250, 3643, 5000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 5000) == [1, 3, 4, 14, 19, 56, 78, 227, 312, 910, 1250, 3643, 5000]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1024) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1024) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024]: {e}')
    
    total += 1
    try:
        result = candidate(label = 31) == [1, 2, 7, 8, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 31) == [1, 2, 7, 8, 31]: {e}')
    
    total += 1
    try:
        result = candidate(label = 32768) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 32768) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768]: {e}')
    
    total += 1
    try:
        result = candidate(label = 524288) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 524288) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288]: {e}')
    
    total += 1
    try:
        result = candidate(label = 8192) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 8192) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192]: {e}')
    
    total += 1
    try:
        result = candidate(label = 768) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 768) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768]: {e}')
    
    total += 1
    try:
        result = candidate(label = 786432) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608, 393215, 786432]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 786432) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608, 393215, 786432]: {e}')
    
    total += 1
    try:
        result = candidate(label = 789012) == [1, 3, 5, 12, 23, 48, 95, 192, 382, 770, 1530, 3082, 6123, 12328, 24495, 49313, 97981, 197253, 391925, 789012]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 789012) == [1, 3, 5, 12, 23, 48, 95, 192, 382, 770, 1530, 3082, 6123, 12328, 24495, 49313, 97981, 197253, 391925, 789012]: {e}')
    
    total += 1
    try:
        result = candidate(label = 65536) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 65536) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536]: {e}')
    
    total += 1
    try:
        result = candidate(label = 4095) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 4095) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095]: {e}')
    
    total += 1
    try:
        result = candidate(label = 511) == [1, 2, 7, 8, 31, 32, 127, 128, 511]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 511) == [1, 2, 7, 8, 31, 32, 127, 128, 511]: {e}')
    
    total += 1
    try:
        result = candidate(label = 524287) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 524287) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287]: {e}')
    
    total += 1
    try:
        result = candidate(label = 98304) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 98304) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304]: {e}')
    
    total += 1
    try:
        result = candidate(label = 393216) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304, 196607, 393216]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 393216) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304, 196607, 393216]: {e}')
    
    total += 1
    try:
        result = candidate(label = 18) == [1, 3, 4, 14, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 18) == [1, 3, 4, 14, 18]: {e}')
    
    total += 1
    try:
        result = candidate(label = 16383) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 16383) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383]: {e}')
    
    total += 1
    try:
        result = candidate(label = 512) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 512) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512]: {e}')
    
    total += 1
    try:
        result = candidate(label = 16384) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 16384) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384]: {e}')
    
    total += 1
    try:
        result = candidate(label = 131072) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 131072) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072]: {e}')
    
    total += 1
    try:
        result = candidate(label = 262143) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 262143) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143]: {e}')
    
    total += 1
    try:
        result = candidate(label = 127) == [1, 2, 7, 8, 31, 32, 127]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 127) == [1, 2, 7, 8, 31, 32, 127]: {e}')
    
    total += 1
    try:
        result = candidate(label = 4096) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 4096) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096]: {e}')
    
    total += 1
    try:
        result = candidate(label = 32) == [1, 2, 7, 8, 31, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 32) == [1, 2, 7, 8, 31, 32]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1572864) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304, 196607, 393216, 786431, 1572864]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1572864) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304, 196607, 393216, 786431, 1572864]: {e}')
    
    total += 1
    try:
        result = candidate(label = 777777) == [1, 2, 6, 11, 24, 47, 97, 189, 388, 759, 1552, 3038, 6211, 12152, 24846, 48611, 99385, 194444, 397543, 777777]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 777777) == [1, 2, 6, 11, 24, 47, 97, 189, 388, 759, 1552, 3038, 6211, 12152, 24846, 48611, 99385, 194444, 397543, 777777]: {e}')
    
    total += 1
    try:
        result = candidate(label = 262144) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 262144) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144]: {e}')
    
    total += 1
    try:
        result = candidate(label = 500000) == [1, 2, 7, 8, 30, 34, 122, 139, 488, 559, 1953, 2237, 7812, 8950, 31250, 35803, 125000, 143215, 500000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 500000) == [1, 2, 7, 8, 30, 34, 122, 139, 488, 559, 1953, 2237, 7812, 8950, 31250, 35803, 125000, 143215, 500000]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1234567) == [1, 3, 4, 14, 18, 58, 75, 233, 301, 933, 1205, 3732, 4822, 14930, 19290, 59723, 77160, 238895, 308641, 955580, 1234567]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1234567) == [1, 3, 4, 14, 18, 58, 75, 233, 301, 933, 1205, 3732, 4822, 14930, 19290, 59723, 77160, 238895, 308641, 955580, 1234567]: {e}')
    
    total += 1
    try:
        result = candidate(label = 2048) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 2048) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048]: {e}')
    
    total += 1
    try:
        result = candidate(label = 150) == [1, 2, 7, 9, 29, 37, 116, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 150) == [1, 2, 7, 9, 29, 37, 116, 150]: {e}')
    
    total += 1
    try:
        result = candidate(label = 999999) == [1, 3, 4, 15, 17, 61, 69, 244, 279, 976, 1118, 3906, 4475, 15624, 17902, 62499, 71608, 249999, 286432, 999999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 999999) == [1, 3, 4, 15, 17, 61, 69, 244, 279, 976, 1118, 3906, 4475, 15624, 17902, 62499, 71608, 249999, 286432, 999999]: {e}')
    
    total += 1
    try:
        result = candidate(label = 888888) == [1, 3, 5, 13, 20, 54, 83, 217, 333, 868, 1335, 3472, 5343, 13888, 21374, 55555, 85496, 222222, 341987, 888888]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 888888) == [1, 3, 5, 13, 20, 54, 83, 217, 333, 868, 1335, 3472, 5343, 13888, 21374, 55555, 85496, 222222, 341987, 888888]: {e}')
    
    total += 1
    try:
        result = candidate(label = 8191) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 8191) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191]: {e}')
    
    total += 1
    try:
        result = candidate(label = 196608) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 196608) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608]: {e}')
    
    total += 1
    try:
        result = candidate(label = 2147483647) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607, 8388608, 33554431, 33554432, 134217727, 134217728, 536870911, 536870912, 2147483647]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 2147483647) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607, 8388608, 33554431, 33554432, 134217727, 134217728, 536870911, 536870912, 2147483647]: {e}')
    
    total += 1
    try:
        result = candidate(label = 128) == [1, 2, 7, 8, 31, 32, 127, 128]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 128) == [1, 2, 7, 8, 31, 32, 127, 128]: {e}')
    
    total += 1
    try:
        result = candidate(label = 2047) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 2047) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047]: {e}')
    
    total += 1
    try:
        result = candidate(label = 2097151) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 2097151) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151]: {e}')
    
    total += 1
    try:
        result = candidate(label = 67108864) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576, 4194303, 4194304, 16777215, 16777216, 67108863, 67108864]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 67108864) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576, 4194303, 4194304, 16777215, 16777216, 67108863, 67108864]: {e}')
    
    total += 1
    try:
        result = candidate(label = 8388607) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 8388607) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607]: {e}')
    
    total += 1
    try:
        result = candidate(label = 65535) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 65535) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535]: {e}')
    
    total += 1
    try:
        result = candidate(label = 983041) == [1, 3, 4, 15, 17, 60, 71, 240, 287, 960, 1151, 3840, 4607, 15360, 18431, 61440, 73727, 245760, 294911, 983041]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 983041) == [1, 3, 4, 15, 17, 60, 71, 240, 287, 960, 1151, 3840, 4607, 15360, 18431, 61440, 73727, 245760, 294911, 983041]: {e}')
    
    total += 1
    try:
        result = candidate(label = 393215) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608, 393215]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 393215) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608, 393215]: {e}')
    
    total += 1
    try:
        result = candidate(label = 32767) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 32767) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767]: {e}')
    
    total += 1
    try:
        result = candidate(label = 200000) == [1, 3, 5, 12, 23, 48, 94, 195, 377, 781, 1509, 3125, 6037, 12500, 24151, 50000, 96607, 200000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 200000) == [1, 3, 5, 12, 23, 48, 94, 195, 377, 781, 1509, 3125, 6037, 12500, 24151, 50000, 96607, 200000]: {e}')
    
    total += 1
    try:
        result = candidate(label = 131071) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 131071) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071]: {e}')
    
    total += 1
    try:
        result = candidate(label = 100000) == [1, 2, 6, 11, 24, 47, 97, 188, 390, 754, 1562, 3018, 6250, 12075, 25000, 48303, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 100000) == [1, 2, 6, 11, 24, 47, 97, 188, 390, 754, 1562, 3018, 6250, 12075, 25000, 48303, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(label = 33554431) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607, 8388608, 33554431]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 33554431) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607, 8388608, 33554431]: {e}')
    
    total += 1
    try:
        result = candidate(label = 800000) == [1, 3, 5, 12, 23, 48, 94, 195, 377, 781, 1509, 3125, 6037, 12500, 24151, 50000, 96607, 200000, 386431, 800000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 800000) == [1, 3, 5, 12, 23, 48, 94, 195, 377, 781, 1509, 3125, 6037, 12500, 24151, 50000, 96607, 200000, 386431, 800000]: {e}')
    
    total += 1
    try:
        result = candidate(label = 123456) == [1, 2, 7, 8, 30, 35, 120, 142, 482, 571, 1929, 2285, 7716, 9143, 30864, 36575, 123456]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 123456) == [1, 2, 7, 8, 30, 35, 120, 142, 482, 571, 1929, 2285, 7716, 9143, 30864, 36575, 123456]: {e}')
    
    total += 1
    try:
        result = candidate(label = 1048576) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 1048576) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576]: {e}')
    
    total += 1
    try:
        result = candidate(label = 63) == [1, 3, 4, 15, 16, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 63) == [1, 3, 4, 15, 16, 63]: {e}')
    
    total += 1
    try:
        result = candidate(label = 16777215) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576, 4194303, 4194304, 16777215]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 16777215) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576, 4194303, 4194304, 16777215]: {e}')
    
    total += 1
    try:
        result = candidate(label = 256) == [1, 3, 4, 15, 16, 63, 64, 255, 256]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 256) == [1, 3, 4, 15, 16, 63, 64, 255, 256]: {e}')
    
    total += 1
    try:
        result = candidate(label = 17) == [1, 3, 4, 15, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(label = 17) == [1, 3, 4, 15, 17]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(label = 14) == [1, 3, 4, 14]
    assert candidate(label = 1023) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023]
    assert candidate(label = 3) == [1, 3]
    assert candidate(label = 1000000) == [1, 3, 4, 15, 17, 61, 69, 244, 279, 976, 1118, 3906, 4475, 15625, 17901, 62500, 71607, 250000, 286431, 1000000]
    assert candidate(label = 255) == [1, 3, 4, 15, 16, 63, 64, 255]
    assert candidate(label = 4) == [1, 3, 4]
    assert candidate(label = 13) == [1, 3, 5, 13]
    assert candidate(label = 15) == [1, 3, 4, 15]
    assert candidate(label = 6) == [1, 2, 6]
    assert candidate(label = 11) == [1, 2, 6, 11]
    assert candidate(label = 2) == [1, 2]
    assert candidate(label = 64) == [1, 3, 4, 15, 16, 63, 64]
    assert candidate(label = 8) == [1, 2, 7, 8]
    assert candidate(label = 1048575) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575]
    assert candidate(label = 1) == [1]
    assert candidate(label = 9) == [1, 2, 7, 9]
    assert candidate(label = 26) == [1, 2, 6, 10, 26]
    assert candidate(label = 12) == [1, 3, 5, 12]
    assert candidate(label = 10) == [1, 2, 6, 10]
    assert candidate(label = 7) == [1, 2, 7]
    assert candidate(label = 5) == [1, 3, 5]
    assert candidate(label = 16) == [1, 3, 4, 15, 16]
    assert candidate(label = 5000) == [1, 3, 4, 14, 19, 56, 78, 227, 312, 910, 1250, 3643, 5000]
    assert candidate(label = 1024) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024]
    assert candidate(label = 31) == [1, 2, 7, 8, 31]
    assert candidate(label = 32768) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768]
    assert candidate(label = 524288) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288]
    assert candidate(label = 8192) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192]
    assert candidate(label = 768) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768]
    assert candidate(label = 786432) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608, 393215, 786432]
    assert candidate(label = 789012) == [1, 3, 5, 12, 23, 48, 95, 192, 382, 770, 1530, 3082, 6123, 12328, 24495, 49313, 97981, 197253, 391925, 789012]
    assert candidate(label = 65536) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536]
    assert candidate(label = 4095) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095]
    assert candidate(label = 511) == [1, 2, 7, 8, 31, 32, 127, 128, 511]
    assert candidate(label = 524287) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287]
    assert candidate(label = 98304) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304]
    assert candidate(label = 393216) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304, 196607, 393216]
    assert candidate(label = 18) == [1, 3, 4, 14, 18]
    assert candidate(label = 16383) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383]
    assert candidate(label = 512) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512]
    assert candidate(label = 16384) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384]
    assert candidate(label = 131072) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072]
    assert candidate(label = 262143) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143]
    assert candidate(label = 127) == [1, 2, 7, 8, 31, 32, 127]
    assert candidate(label = 4096) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096]
    assert candidate(label = 32) == [1, 2, 7, 8, 31, 32]
    assert candidate(label = 1572864) == [1, 2, 6, 11, 24, 47, 96, 191, 384, 767, 1536, 3071, 6144, 12287, 24576, 49151, 98304, 196607, 393216, 786431, 1572864]
    assert candidate(label = 777777) == [1, 2, 6, 11, 24, 47, 97, 189, 388, 759, 1552, 3038, 6211, 12152, 24846, 48611, 99385, 194444, 397543, 777777]
    assert candidate(label = 262144) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144]
    assert candidate(label = 500000) == [1, 2, 7, 8, 30, 34, 122, 139, 488, 559, 1953, 2237, 7812, 8950, 31250, 35803, 125000, 143215, 500000]
    assert candidate(label = 1234567) == [1, 3, 4, 14, 18, 58, 75, 233, 301, 933, 1205, 3732, 4822, 14930, 19290, 59723, 77160, 238895, 308641, 955580, 1234567]
    assert candidate(label = 2048) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048]
    assert candidate(label = 150) == [1, 2, 7, 9, 29, 37, 116, 150]
    assert candidate(label = 999999) == [1, 3, 4, 15, 17, 61, 69, 244, 279, 976, 1118, 3906, 4475, 15624, 17902, 62499, 71608, 249999, 286432, 999999]
    assert candidate(label = 888888) == [1, 3, 5, 13, 20, 54, 83, 217, 333, 868, 1335, 3472, 5343, 13888, 21374, 55555, 85496, 222222, 341987, 888888]
    assert candidate(label = 8191) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191]
    assert candidate(label = 196608) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608]
    assert candidate(label = 2147483647) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607, 8388608, 33554431, 33554432, 134217727, 134217728, 536870911, 536870912, 2147483647]
    assert candidate(label = 128) == [1, 2, 7, 8, 31, 32, 127, 128]
    assert candidate(label = 2047) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047]
    assert candidate(label = 2097151) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151]
    assert candidate(label = 67108864) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576, 4194303, 4194304, 16777215, 16777216, 67108863, 67108864]
    assert candidate(label = 8388607) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607]
    assert candidate(label = 65535) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535]
    assert candidate(label = 983041) == [1, 3, 4, 15, 17, 60, 71, 240, 287, 960, 1151, 3840, 4607, 15360, 18431, 61440, 73727, 245760, 294911, 983041]
    assert candidate(label = 393215) == [1, 3, 5, 12, 23, 48, 95, 192, 383, 768, 1535, 3072, 6143, 12288, 24575, 49152, 98303, 196608, 393215]
    assert candidate(label = 32767) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767]
    assert candidate(label = 200000) == [1, 3, 5, 12, 23, 48, 94, 195, 377, 781, 1509, 3125, 6037, 12500, 24151, 50000, 96607, 200000]
    assert candidate(label = 131071) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071]
    assert candidate(label = 100000) == [1, 2, 6, 11, 24, 47, 97, 188, 390, 754, 1562, 3018, 6250, 12075, 25000, 48303, 100000]
    assert candidate(label = 33554431) == [1, 2, 7, 8, 31, 32, 127, 128, 511, 512, 2047, 2048, 8191, 8192, 32767, 32768, 131071, 131072, 524287, 524288, 2097151, 2097152, 8388607, 8388608, 33554431]
    assert candidate(label = 800000) == [1, 3, 5, 12, 23, 48, 94, 195, 377, 781, 1509, 3125, 6037, 12500, 24151, 50000, 96607, 200000, 386431, 800000]
    assert candidate(label = 123456) == [1, 2, 7, 8, 30, 35, 120, 142, 482, 571, 1929, 2285, 7716, 9143, 30864, 36575, 123456]
    assert candidate(label = 1048576) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576]
    assert candidate(label = 63) == [1, 3, 4, 15, 16, 63]
    assert candidate(label = 16777215) == [1, 3, 4, 15, 16, 63, 64, 255, 256, 1023, 1024, 4095, 4096, 16383, 16384, 65535, 65536, 262143, 262144, 1048575, 1048576, 4194303, 4194304, 16777215]
    assert candidate(label = 256) == [1, 3, 4, 15, 16, 63, 64, 255, 256]
    assert candidate(label = 17) == [1, 3, 4, 15, 17]


