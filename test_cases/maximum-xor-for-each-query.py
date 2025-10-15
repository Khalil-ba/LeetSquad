def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 7],maximumBit = 3) == [5, 2, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 7],maximumBit = 3) == [5, 2, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 3],maximumBit = 2) == [0, 3, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 3],maximumBit = 2) == [0, 3, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16],maximumBit = 5) == [0, 16, 24, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16],maximumBit = 5) == [0, 16, 24, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 31, 31, 31, 31],maximumBit = 5) == [0, 31, 0, 31, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 31, 31, 31, 31],maximumBit = 5) == [0, 31, 0, 31, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 2, 5, 7],maximumBit = 3) == [4, 3, 6, 4, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 2, 5, 7],maximumBit = 3) == [4, 3, 6, 4, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],maximumBit = 1) == [0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],maximumBit = 1) == [0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],maximumBit = 20) == [434696, 813064, 624904, 73608, 941512, 1039208, 1047672, 1048464, 1048564, 1048574]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],maximumBit = 20) == [434696, 813064, 624904, 73608, 941512, 1039208, 1047672, 1048464, 1048564, 1048574]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117],maximumBit = 7) == [123, 14, 127, 18, 123, 30, 127, 34, 123, 46, 127, 50, 123, 62, 127, 66, 123, 78, 127, 82, 123, 94, 127, 98, 123, 110, 127, 114, 123, 126]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117],maximumBit = 7) == [123, 14, 127, 18, 123, 30, 127, 34, 123, 46, 127, 50, 123, 62, 127, 66, 123, 78, 127, 82, 123, 94, 127, 98, 123, 110, 127, 114, 123, 126]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575],maximumBit = 20) == [1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575],maximumBit = 20) == [1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],maximumBit = 4) == [14, 7, 15, 8, 14, 11, 15, 12, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],maximumBit = 4) == [14, 7, 15, 8, 14, 11, 15, 12, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],maximumBit = 14) == [5056, 14594, 9071, 13114, 14626, 16159, 15556, 16038, 16351, 16182, 16294, 16383, 16328, 16362, 16383, 16370, 16378, 16383, 16380, 16382]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],maximumBit = 14) == [5056, 14594, 9071, 13114, 14626, 16159, 15556, 16038, 16351, 16182, 16294, 16383, 16328, 16362, 16383, 16370, 16378, 16383, 16380, 16382]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 6, 14, 30, 62, 126, 254, 510, 1022],maximumBit = 10) == [341, 683, 853, 939, 981, 1003, 1013, 1019, 1021, 1023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 6, 14, 30, 62, 126, 254, 510, 1022],maximumBit = 10) == [341, 683, 853, 939, 981, 1003, 1013, 1019, 1021, 1023]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],maximumBit = 15) == [10922, 21845, 27306, 30037, 31402, 32085, 32426, 32597, 32682, 32725, 32746, 32757, 32762, 32765, 32766]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],maximumBit = 15) == [10922, 21845, 27306, 30037, 31402, 32085, 32426, 32597, 32682, 32725, 32746, 32757, 32762, 32765, 32766]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],maximumBit = 5) == [31, 0, 29, 6, 31, 8, 29, 14, 31, 16, 29, 22, 31, 24, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],maximumBit = 5) == [31, 0, 29, 6, 31, 8, 29, 14, 31, 16, 29, 22, 31, 24, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],maximumBit = 4) == [15, 15, 14, 12, 15, 11, 14, 8, 15, 7, 14, 4, 15, 3, 14, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],maximumBit = 4) == [15, 15, 14, 12, 15, 11, 14, 8, 15, 7, 14, 4, 15, 3, 14, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],maximumBit = 6) == [29, 47, 0, 44, 5, 35, 0, 32, 61, 39, 48, 36, 53, 59, 48, 56, 61]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],maximumBit = 6) == [29, 47, 0, 44, 5, 35, 0, 32, 61, 39, 48, 36, 53, 59, 48, 56, 61]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],maximumBit = 16) == [18165, 41052, 60607, 62750, 64917, 65356, 65471, 65518, 65525, 65532]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],maximumBit = 16) == [18165, 41052, 60607, 62750, 64917, 65356, 65471, 65518, 65525, 65532]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],maximumBit = 5) == [29, 14, 31, 16, 29, 22, 31, 24, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],maximumBit = 5) == [29, 14, 31, 16, 29, 22, 31, 24, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],maximumBit = 5) == [31, 0, 30, 3, 31, 4, 30, 7, 31, 8, 30, 11, 31, 12, 30, 15, 31, 16, 30, 19, 31, 20, 30, 23, 31, 24, 30, 27, 31, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],maximumBit = 5) == [31, 0, 30, 3, 31, 4, 30, 7, 31, 8, 30, 11, 31, 12, 30, 15, 31, 16, 30, 19, 31, 20, 30, 23, 31, 24, 30, 27, 31, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],maximumBit = 6) == [61, 6, 63, 8, 61, 14, 63, 16, 61, 22, 63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],maximumBit = 6) == [61, 6, 63, 8, 61, 14, 63, 16, 61, 22, 63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],maximumBit = 20) == [0, 524288, 786432, 917504, 983040, 1015808, 1032192, 1040384, 1044480, 1046528, 1047552, 1048064, 1048320, 1048448, 1048512, 1048544, 1048560, 1048568, 1048572, 1048574]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],maximumBit = 20) == [0, 524288, 786432, 917504, 983040, 1015808, 1032192, 1040384, 1044480, 1046528, 1047552, 1048064, 1048320, 1048448, 1048512, 1048544, 1048560, 1048568, 1048572, 1048574]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maximumBit = 5) == [11, 10, 8, 11, 15, 10, 12, 11, 3, 10, 0, 11, 7, 10, 4, 11, 27, 10, 24, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maximumBit = 5) == [11, 10, 8, 11, 15, 10, 12, 11, 3, 10, 0, 11, 7, 10, 4, 11, 27, 10, 24, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],maximumBit = 3) == [7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],maximumBit = 3) == [7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],maximumBit = 6) == [63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],maximumBit = 6) == [63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61, 63]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151],maximumBit = 21) == [699051, 1398100, 1747627, 1922388, 2009771, 2053460, 2075307, 2086228, 2091691, 2094420, 2095787, 2096468, 2096811, 2096980, 2097067, 2097108, 2097131, 2097140, 2097147, 2097148]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151],maximumBit = 21) == [699051, 1398100, 1747627, 1922388, 2009771, 2053460, 2075307, 2086228, 2091691, 2094420, 2095787, 2096468, 2096811, 2096980, 2097067, 2097108, 2097131, 2097140, 2097147, 2097148]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58],maximumBit = 6) == [61, 7, 63, 9, 61, 15, 63, 17, 61, 23, 63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58],maximumBit = 6) == [61, 7, 63, 9, 61, 15, 63, 17, 61, 23, 63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61, 63]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],maximumBit = 9) == [99, 499, 154, 478, 255, 511, 286, 474, 371, 483, 410, 510, 431, 495, 478, 506, 483, 499, 506, 510]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],maximumBit = 9) == [99, 499, 154, 478, 255, 511, 286, 474, 371, 483, 410, 510, 431, 495, 478, 506, 483, 499, 506, 510]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576],maximumBit = 15) == [16382, 24574, 28670, 30718, 31742, 32254, 32510, 32638, 32702, 32734, 32750, 32758, 32762, 32764]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576],maximumBit = 15) == [16382, 24574, 28670, 30718, 31742, 32254, 32510, 32638, 32702, 32734, 32750, 32758, 32762, 32764]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],maximumBit = 13) == [6403, 878, 4923, 6435, 7966, 7365, 7847, 8158, 7991, 8103, 8190, 8137, 8171, 8190, 8179, 8187, 8190, 8189, 8191, 8190]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],maximumBit = 13) == [6403, 878, 4923, 6435, 7966, 7365, 7847, 8158, 7991, 8103, 8190, 8137, 8171, 8190, 8179, 8187, 8190, 8189, 8191, 8190]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],maximumBit = 11) == [0, 1024, 1536, 1792, 1920, 1984, 2016, 2032, 2040, 2044, 2046]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],maximumBit = 11) == [0, 1024, 1536, 1792, 1920, 1984, 2016, 2032, 2040, 2044, 2046]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015],maximumBit = 10) == [8, 1023, 7, 1022, 4, 1023, 3, 1022, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015],maximumBit = 10) == [8, 1023, 7, 1022, 4, 1023, 3, 1022, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maximumBit = 4) == [15, 0, 14, 3, 15, 4, 14, 7, 15, 8, 14, 11, 15, 12, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maximumBit = 4) == [15, 0, 14, 3, 15, 4, 14, 7, 15, 8, 14, 11, 15, 12, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],maximumBit = 7) == [63, 116, 50, 115, 79, 120, 74, 103, 79, 108, 114, 107, 127, 112, 122]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],maximumBit = 7) == [63, 116, 50, 115, 79, 120, 74, 103, 79, 108, 114, 107, 127, 112, 122]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288],maximumBit = 14) == [8187, 12283, 14331, 15355, 15867, 16123, 16251, 16315, 16347, 16363, 16371]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288],maximumBit = 14) == [8187, 12283, 14331, 15355, 15867, 16123, 16251, 16315, 16347, 16363, 16371]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],maximumBit = 6) == [1, 61, 7, 63, 9, 61, 15, 63, 17, 61, 23, 63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],maximumBit = 6) == [1, 61, 7, 63, 9, 61, 15, 63, 17, 61, 23, 63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35],maximumBit = 6) == [15, 44, 50, 43, 63, 48, 58]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35],maximumBit = 6) == [15, 44, 50, 43, 63, 48, 58]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],maximumBit = 13) == [5461, 6826, 7509, 7850, 8021, 8106, 8149, 8170, 8181, 8186, 8189, 8190]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],maximumBit = 13) == [5461, 6826, 7509, 7850, 8021, 8106, 8149, 8170, 8181, 8186, 8189, 8190]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],maximumBit = 7) == [63, 127, 71, 119, 95, 127, 103, 119]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],maximumBit = 7) == [63, 127, 71, 119, 95, 127, 103, 119]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],maximumBit = 10) == [341, 682, 853, 938, 981, 1002, 1013, 1018, 1021, 1022]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],maximumBit = 10) == [341, 682, 853, 938, 981, 1002, 1013, 1018, 1021, 1022]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 5, 6, 8, 10, 12],maximumBit = 4) == [3, 15, 5, 13, 11, 14, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 5, 6, 8, 10, 12],maximumBit = 4) == [3, 15, 5, 13, 11, 14, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],maximumBit = 5) == [31, 13, 30, 14, 31, 17, 30, 18, 31, 21, 30, 22, 31, 25, 30, 26, 31, 29, 30, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],maximumBit = 5) == [31, 13, 30, 14, 31, 17, 30, 18, 31, 21, 30, 22, 31, 25, 30, 26, 31, 29, 30, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127],maximumBit = 7) == [42, 85, 106, 117, 122, 125, 126]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127],maximumBit = 7) == [42, 85, 106, 117, 122, 125, 126]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310],maximumBit = 10) == [990, 744, 1023, 775, 990, 868, 1023, 899, 990, 992]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310],maximumBit = 10) == [990, 744, 1023, 775, 990, 868, 1023, 899, 990, 992]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],maximumBit = 1) == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],maximumBit = 1) == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95],maximumBit = 7) == [127, 32, 119, 56, 127, 64, 119, 88, 127, 96, 119, 120]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95],maximumBit = 7) == [127, 32, 119, 56, 127, 64, 119, 88, 127, 96, 119, 120]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],maximumBit = 8) == [183, 127, 193, 117, 223, 127, 233, 101, 231, 159, 241, 149, 207, 159, 217, 229, 215, 255, 225, 245]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],maximumBit = 8) == [183, 127, 193, 117, 223, 127, 233, 101, 231, 159, 241, 149, 207, 159, 217, 229, 215, 255, 225, 245]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 1) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 1) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287],maximumBit = 20) == [699050, 873813, 961194, 1004885, 1026730, 1037653, 1043114, 1045845, 1047210, 1047893, 1048234, 1048405, 1048490, 1048533, 1048554, 1048565, 1048570, 1048573, 1048574, 1048575]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287],maximumBit = 20) == [699050, 873813, 961194, 1004885, 1026730, 1037653, 1043114, 1045845, 1047210, 1047893, 1048234, 1048405, 1048490, 1048533, 1048554, 1048565, 1048570, 1048573, 1048574, 1048575]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 7, 15, 31, 63],maximumBit = 6) == [21, 42, 53, 58, 61, 62, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 7, 15, 31, 63],maximumBit = 6) == [21, 42, 53, 58, 61, 62, 63]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144],maximumBit = 18) == [0, 0, 131072, 196608, 229376, 245760, 253952, 258048, 260096, 261120, 261632, 261888, 262016, 262080, 262112, 262128, 262136, 262140, 262142, 262143]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144],maximumBit = 18) == [0, 0, 131072, 196608, 229376, 245760, 253952, 258048, 260096, 261120, 261632, 261888, 262016, 262080, 262112, 262128, 262136, 262140, 262142, 262143]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maximumBit = 4) == [15, 0, 14, 3, 15, 4, 14, 7, 15, 8, 14, 11, 15, 12, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maximumBit = 4) == [15, 0, 14, 3, 15, 4, 14, 7, 15, 8, 14, 11, 15, 12, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],maximumBit = 20) == [0, 524288, 786432, 917504, 983040, 1015808, 1032192, 1040384, 1044480, 1046528, 1047552, 1048064, 1048320, 1048448, 1048512, 1048544, 1048560, 1048568, 1048572, 1048574]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],maximumBit = 20) == [0, 524288, 786432, 917504, 983040, 1015808, 1032192, 1040384, 1044480, 1046528, 1047552, 1048064, 1048320, 1048448, 1048512, 1048544, 1048560, 1048568, 1048572, 1048574]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],maximumBit = 6) == [14, 63, 16, 61, 22, 63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],maximumBit = 6) == [14, 63, 16, 61, 22, 63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maximumBit = 7) == [113, 21, 79, 31, 89, 101, 87, 127, 97, 117]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maximumBit = 7) == [113, 21, 79, 31, 89, 101, 87, 127, 97, 117]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 4, 7, 10, 12, 15, 19, 22],maximumBit = 5) == [18, 4, 23, 24, 20, 30, 25, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 4, 7, 10, 12, 15, 19, 22],maximumBit = 5) == [18, 4, 23, 24, 20, 30, 25, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],maximumBit = 13) == [2041, 5113, 6649, 7417, 7801, 7993, 8089, 8137, 8161, 8181]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],maximumBit = 13) == [2041, 5113, 6649, 7417, 7801, 7993, 8089, 8137, 8161, 8181]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 1) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 1) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],maximumBit = 5) == [11, 31, 12, 30, 15, 31, 16, 30, 19, 31, 20, 30, 23, 31, 24, 30, 27, 31, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],maximumBit = 5) == [11, 31, 12, 30, 15, 31, 16, 30, 19, 31, 20, 30, 23, 31, 24, 30, 27, 31, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],maximumBit = 7) == [26, 126, 47, 111, 94, 122, 99, 115, 122, 126]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],maximumBit = 7) == [26, 126, 47, 111, 94, 122, 99, 115, 122, 126]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127],maximumBit = 7) == [42, 85, 106, 117, 122, 125, 126, 127]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127],maximumBit = 7) == [42, 85, 106, 117, 122, 125, 126, 127]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],maximumBit = 3) == [7, 4, 7, 4, 7, 4, 6, 4, 6, 4, 6, 7, 6, 7, 6, 7, 7, 7, 7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],maximumBit = 3) == [7, 4, 7, 4, 7, 4, 6, 4, 6, 4, 6, 7, 6, 7, 6, 7, 7, 7, 7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117],maximumBit = 7) == [11, 126, 8, 127, 7, 126, 4, 127, 3, 126, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117],maximumBit = 7) == [11, 126, 8, 127, 7, 126, 4, 127, 3, 126, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383],maximumBit = 14) == [5458, 10925, 13650, 15021, 15698, 16045, 16210, 16301, 16338, 16365, 16370, 16381, 16378]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383],maximumBit = 14) == [5458, 10925, 13650, 15021, 15698, 16045, 16210, 16301, 16338, 16365, 16370, 16381, 16378]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],maximumBit = 20) == [349525, 349524, 349527, 349520, 349535, 349504, 349567, 349440, 349695, 349184, 350207, 348160, 352255, 344064, 360447, 327680, 393215, 262144, 524287, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],maximumBit = 20) == [349525, 349524, 349527, 349520, 349535, 349504, 349567, 349440, 349695, 349184, 350207, 348160, 352255, 344064, 360447, 327680, 393215, 262144, 524287, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22],maximumBit = 5) == [31, 9, 29, 15, 31, 17, 29, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22],maximumBit = 5) == [31, 9, 29, 15, 31, 17, 29, 23]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],maximumBit = 20) == [350207, 698368, 874495, 960512, 1005567, 1026048, 1038335, 1042432, 1046527, 1046528]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],maximumBit = 20) == [350207, 698368, 874495, 960512, 1005567, 1026048, 1038335, 1042432, 1046527, 1046528]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],maximumBit = 6) == [63, 3, 58, 12, 63, 15, 34, 8, 47, 11, 42, 52, 47, 55, 34, 48, 63, 51, 58, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],maximumBit = 6) == [63, 3, 58, 12, 63, 15, 34, 8, 47, 11, 42, 52, 47, 55, 34, 48, 63, 51, 58, 60]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],maximumBit = 8) == [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],maximumBit = 8) == [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 5, 8, 13, 21, 34, 55, 89],maximumBit = 7) == [39, 126, 73, 107, 126, 115, 123, 126, 125, 127]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 5, 8, 13, 21, 34, 55, 89],maximumBit = 7) == [39, 126, 73, 107, 126, 115, 123, 126, 125, 127]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],maximumBit = 6) == [63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],maximumBit = 6) == [63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1023],maximumBit = 10) == [1023, 0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1023],maximumBit = 10) == [1023, 0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022, 1023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022, 1023]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 3, 4, 7],maximumBit = 3) == [5, 2, 6, 5]
    assert candidate(nums = [0, 1, 1, 3],maximumBit = 2) == [0, 3, 2, 3]
    assert candidate(nums = [1, 2, 4, 8, 16],maximumBit = 5) == [0, 16, 24, 28, 30]
    assert candidate(nums = [31, 31, 31, 31, 31],maximumBit = 5) == [0, 31, 0, 31, 0]
    assert candidate(nums = [0, 1, 2, 2, 5, 7],maximumBit = 3) == [4, 3, 6, 4, 6, 7]
    assert candidate(nums = [1, 1, 1, 1, 1],maximumBit = 1) == [0, 1, 0, 1, 0]
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],maximumBit = 20) == [434696, 813064, 624904, 73608, 941512, 1039208, 1047672, 1048464, 1048564, 1048574]
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117],maximumBit = 7) == [123, 14, 127, 18, 123, 30, 127, 34, 123, 46, 127, 50, 123, 62, 127, 66, 123, 78, 127, 82, 123, 94, 127, 98, 123, 110, 127, 114, 123, 126]
    assert candidate(nums = [1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575, 1048575],maximumBit = 20) == [1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0, 1048575, 0]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],maximumBit = 4) == [14, 7, 15, 8, 14, 11, 15, 12, 14, 15]
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],maximumBit = 14) == [5056, 14594, 9071, 13114, 14626, 16159, 15556, 16038, 16351, 16182, 16294, 16383, 16328, 16362, 16383, 16370, 16378, 16383, 16380, 16382]
    assert candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(nums = [0, 2, 6, 14, 30, 62, 126, 254, 510, 1022],maximumBit = 10) == [341, 683, 853, 939, 981, 1003, 1013, 1019, 1021, 1023]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767],maximumBit = 15) == [10922, 21845, 27306, 30037, 31402, 32085, 32426, 32597, 32682, 32725, 32746, 32757, 32762, 32765, 32766]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],maximumBit = 5) == [31, 0, 29, 6, 31, 8, 29, 14, 31, 16, 29, 22, 31, 24, 29, 30]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],maximumBit = 4) == [15, 15, 14, 12, 15, 11, 14, 8, 15, 7, 14, 4, 15, 3, 14, 0]
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],maximumBit = 6) == [29, 47, 0, 44, 5, 35, 0, 32, 61, 39, 48, 36, 53, 59, 48, 56, 61]
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],maximumBit = 16) == [18165, 41052, 60607, 62750, 64917, 65356, 65471, 65518, 65525, 65532]
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],maximumBit = 5) == [29, 14, 31, 16, 29, 22, 31, 24, 29, 30]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],maximumBit = 5) == [31, 0, 30, 3, 31, 4, 30, 7, 31, 8, 30, 11, 31, 12, 30, 15, 31, 16, 30, 19, 31, 20, 30, 23, 31, 24, 30, 27, 31, 28, 30]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],maximumBit = 6) == [61, 6, 63, 8, 61, 14, 63, 16, 61, 22, 63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],maximumBit = 20) == [0, 524288, 786432, 917504, 983040, 1015808, 1032192, 1040384, 1044480, 1046528, 1047552, 1048064, 1048320, 1048448, 1048512, 1048544, 1048560, 1048568, 1048572, 1048574]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maximumBit = 5) == [11, 10, 8, 11, 15, 10, 12, 11, 3, 10, 0, 11, 7, 10, 4, 11, 27, 10, 24, 11]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],maximumBit = 3) == [7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2]
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],maximumBit = 6) == [63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61, 63]
    assert candidate(nums = [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151],maximumBit = 21) == [699051, 1398100, 1747627, 1922388, 2009771, 2053460, 2075307, 2086228, 2091691, 2094420, 2095787, 2096468, 2096811, 2096980, 2097067, 2097108, 2097131, 2097140, 2097147, 2097148]
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58],maximumBit = 6) == [61, 7, 63, 9, 61, 15, 63, 17, 61, 23, 63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61, 63]
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],maximumBit = 9) == [99, 499, 154, 478, 255, 511, 286, 474, 371, 483, 410, 510, 431, 495, 478, 506, 483, 499, 506, 510]
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576],maximumBit = 15) == [16382, 24574, 28670, 30718, 31742, 32254, 32510, 32638, 32702, 32734, 32750, 32758, 32762, 32764]
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],maximumBit = 13) == [6403, 878, 4923, 6435, 7966, 7365, 7847, 8158, 7991, 8103, 8190, 8137, 8171, 8190, 8179, 8187, 8190, 8189, 8191, 8190]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],maximumBit = 11) == [0, 1024, 1536, 1792, 1920, 1984, 2016, 2032, 2040, 2044, 2046]
    assert candidate(nums = [1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015],maximumBit = 10) == [8, 1023, 7, 1022, 4, 1023, 3, 1022, 0]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maximumBit = 4) == [15, 0, 14, 3, 15, 4, 14, 7, 15, 8, 14, 11, 15, 12, 14, 15]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],maximumBit = 7) == [63, 116, 50, 115, 79, 120, 74, 103, 79, 108, 114, 107, 127, 112, 122]
    assert candidate(nums = [12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288],maximumBit = 14) == [8187, 12283, 14331, 15355, 15867, 16123, 16251, 16315, 16347, 16363, 16371]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],maximumBit = 6) == [1, 61, 7, 63, 9, 61, 15, 63, 17, 61, 23, 63, 25, 61, 31, 63, 33, 61, 39, 63, 41, 61, 47, 63, 49, 61, 55, 63, 57, 61]
    assert candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maximumBit = 1) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35],maximumBit = 6) == [15, 44, 50, 43, 63, 48, 58]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095],maximumBit = 13) == [5461, 6826, 7509, 7850, 8021, 8106, 8149, 8170, 8181, 8186, 8189, 8190]
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],maximumBit = 7) == [63, 127, 71, 119, 95, 127, 103, 119]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],maximumBit = 10) == [341, 682, 853, 938, 981, 1002, 1013, 1018, 1021, 1022]
    assert candidate(nums = [0, 2, 3, 5, 6, 8, 10, 12],maximumBit = 4) == [3, 15, 5, 13, 11, 14, 13, 15]
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],maximumBit = 5) == [31, 13, 30, 14, 31, 17, 30, 18, 31, 21, 30, 22, 31, 25, 30, 26, 31, 29, 30, 30]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127],maximumBit = 7) == [42, 85, 106, 117, 122, 125, 126]
    assert candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310],maximumBit = 10) == [990, 744, 1023, 775, 990, 868, 1023, 899, 990, 992]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],maximumBit = 1) == [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
    assert candidate(nums = [7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95],maximumBit = 7) == [127, 32, 119, 56, 127, 64, 119, 88, 127, 96, 119, 120]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],maximumBit = 8) == [183, 127, 193, 117, 223, 127, 233, 101, 231, 159, 241, 149, 207, 159, 217, 229, 215, 255, 225, 245]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 1) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]
    assert candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287],maximumBit = 20) == [699050, 873813, 961194, 1004885, 1026730, 1037653, 1043114, 1045845, 1047210, 1047893, 1048234, 1048405, 1048490, 1048533, 1048554, 1048565, 1048570, 1048573, 1048574, 1048575]
    assert candidate(nums = [0, 1, 3, 7, 15, 31, 63],maximumBit = 6) == [21, 42, 53, 58, 61, 62, 63]
    assert candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144],maximumBit = 18) == [0, 0, 131072, 196608, 229376, 245760, 253952, 258048, 260096, 261120, 261632, 261888, 262016, 262080, 262112, 262128, 262136, 262140, 262142, 262143]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maximumBit = 4) == [15, 0, 14, 3, 15, 4, 14, 7, 15, 8, 14, 11, 15, 12, 14, 15]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],maximumBit = 20) == [0, 524288, 786432, 917504, 983040, 1015808, 1032192, 1040384, 1044480, 1046528, 1047552, 1048064, 1048320, 1048448, 1048512, 1048544, 1048560, 1048568, 1048572, 1048574]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],maximumBit = 6) == [14, 63, 16, 61, 22, 63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 2) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maximumBit = 7) == [113, 21, 79, 31, 89, 101, 87, 127, 97, 117]
    assert candidate(nums = [1, 3, 4, 7, 10, 12, 15, 19, 22],maximumBit = 5) == [18, 4, 23, 24, 20, 30, 25, 29, 30]
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023],maximumBit = 10) == [1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0, 1023, 0]
    assert candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],maximumBit = 13) == [2041, 5113, 6649, 7417, 7801, 7993, 8089, 8137, 8161, 8181]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],maximumBit = 1) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],maximumBit = 5) == [11, 31, 12, 30, 15, 31, 16, 30, 19, 31, 20, 30, 23, 31, 24, 30, 27, 31, 28, 30]
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],maximumBit = 7) == [26, 126, 47, 111, 94, 122, 99, 115, 122, 126]
    assert candidate(nums = [0, 1, 3, 7, 15, 31, 63, 127],maximumBit = 7) == [42, 85, 106, 117, 122, 125, 126, 127]
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],maximumBit = 3) == [7, 4, 7, 4, 7, 4, 6, 4, 6, 4, 6, 7, 6, 7, 6, 7, 7, 7, 7, 7]
    assert candidate(nums = [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117],maximumBit = 7) == [11, 126, 8, 127, 7, 126, 4, 127, 3, 126, 0]
    assert candidate(nums = [5, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383],maximumBit = 14) == [5458, 10925, 13650, 15021, 15698, 16045, 16210, 16301, 16338, 16365, 16370, 16381, 16378]
    assert candidate(nums = [1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],maximumBit = 20) == [349525, 349524, 349527, 349520, 349535, 349504, 349567, 349440, 349695, 349184, 350207, 348160, 352255, 344064, 360447, 327680, 393215, 262144, 524287, 0]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]
    assert candidate(nums = [8, 10, 12, 14, 16, 18, 20, 22],maximumBit = 5) == [31, 9, 29, 15, 31, 17, 29, 23]
    assert candidate(nums = [2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],maximumBit = 20) == [350207, 698368, 874495, 960512, 1005567, 1026048, 1038335, 1042432, 1046527, 1046528]
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],maximumBit = 6) == [63, 3, 58, 12, 63, 15, 34, 8, 47, 11, 42, 52, 47, 55, 34, 48, 63, 51, 58, 60]
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],maximumBit = 8) == [255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0]
    assert candidate(nums = [0, 2, 3, 5, 8, 13, 21, 34, 55, 89],maximumBit = 7) == [39, 126, 73, 107, 126, 115, 123, 126, 125, 127]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],maximumBit = 6) == [63, 24, 61, 30, 63, 32, 61, 38, 63, 40, 61, 46, 63, 48, 61, 54, 63, 56, 61, 62]
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1023],maximumBit = 10) == [1023, 0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022]
    assert candidate(nums = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maximumBit = 10) == [0, 512, 768, 896, 960, 992, 1008, 1016, 1020, 1022, 1023]


