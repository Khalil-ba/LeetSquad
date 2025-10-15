def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(memory1 = 0,memory2 = 0) == [1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 0,memory2 = 0) == [1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483647,memory2 = 2147483647) == [92681, 88047, 41707]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483647,memory2 = 2147483647) == [92681, 88047, 41707]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000000,memory2 = 1000000000) == [63245, 49116, 17494]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000000,memory2 = 1000000000) == [63245, 49116, 17494]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 15,memory2 = 10) == [7, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 15,memory2 = 10) == [7, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 100,memory2 = 100) == [20, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 100,memory2 = 100) == [20, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 10,memory2 = 10) == [6, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 10,memory2 = 10) == [6, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1073741823,memory2 = 1073741823) == [65535, 65534, 32767]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1073741823,memory2 = 1073741823) == [65535, 65534, 32767]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 1) == [2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 1) == [2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 8,memory2 = 11) == [6, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 8,memory2 = 11) == [6, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1073741824,memory2 = 1073741824) == [65536, 0, 32768]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1073741824,memory2 = 1073741824) == [65536, 0, 32768]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 15,memory2 = 15) == [7, 6, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 15,memory2 = 15) == [7, 6, 3]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 2) == [2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 2) == [2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 15,memory2 = 5) == [6, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 15,memory2 = 5) == [6, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 100,memory2 = 50) == [17, 3, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 100,memory2 = 50) == [17, 3, 11]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2,memory2 = 2) == [3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2,memory2 = 2) == [3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000000,memory2 = 500000000) == [54772, 3472, 37922]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000000,memory2 = 500000000) == [54772, 3472, 37922]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 0,memory2 = 1000000) == [1414, 0, 1009]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 0,memory2 = 1000000) == [1414, 0, 1009]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1024,memory2 = 512) == [55, 12, 39]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1024,memory2 = 512) == [55, 12, 39]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 123456789,memory2 = 987654321) == [47140, 11258, 33622]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 123456789,memory2 = 987654321) == [47140, 11258, 33622]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 256,memory2 = 255) == [32, 15, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 256,memory2 = 255) == [32, 15, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000000,memory2 = 999999999) == [63245, 17493, 49116]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000000,memory2 = 999999999) == [63245, 17493, 49116]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2048,memory2 = 512) == [71, 67, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2048,memory2 = 512) == [71, 67, 8]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 5,memory2 = 1) == [3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 5,memory2 = 1) == [3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 500000000,memory2 = 499999999) == [44721, 8039, 30400]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 500000000,memory2 = 499999999) == [44721, 8039, 30400]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 100000,memory2 = 100001) == [632, 460, 145]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 100000,memory2 = 100001) == [632, 460, 145]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1073741823,memory2 = 1073741824) == [65536, 32767, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1073741823,memory2 = 1073741824) == [65536, 32767, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483647,memory2 = 1073741824) == [80264, 34153, 76602]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483647,memory2 = 1073741824) == [80264, 34153, 76602]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000,memory2 = 0) == [1414, 1009, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000,memory2 = 0) == [1414, 1009, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 5,memory2 = 5) == [4, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 5,memory2 = 5) == [4, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 0,memory2 = 100) == [14, 0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 0,memory2 = 100) == [14, 0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000000,memory2 = 2000000000) == [77459, 17790, 72599]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000000,memory2 = 2000000000) == [77459, 17790, 72599]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 500000000,memory2 = 500000001) == [44721, 8040, 30401]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 500000000,memory2 = 500000001) == [44721, 8040, 30401]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 500000,memory2 = 500000) == [1414, 151, 858]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 500000,memory2 = 500000) == [1414, 151, 858]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2000000000,memory2 = 1000000000) == [77459, 72599, 17790]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2000000000,memory2 = 1000000000) == [77459, 72599, 17790]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 0) == [2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 0) == [2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 4000000000,memory2 = 3000000000) == [118321, 102440, 27200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 4000000000,memory2 = 3000000000) == [118321, 102440, 27200]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000,memory2 = 1000000) == [2000, 0, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000,memory2 = 1000000) == [2000, 0, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 3000000000,memory2 = 1000000000) == [89442, 62751, 46288]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 3000000000,memory2 = 1000000000) == [89442, 62751, 46288]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483647,memory2 = 0) == [65536, 32767, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483647,memory2 = 0) == [65536, 32767, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 500000000,memory2 = 500000000) == [44721, 30400, 8040]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 500000000,memory2 = 500000000) == [44721, 30400, 8040]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1234567890,memory2 = 1234567890) == [70272, 29394, 64530]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1234567890,memory2 = 1234567890) == [70272, 29394, 64530]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1024,memory2 = 1023) == [64, 31, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1024,memory2 = 1023) == [64, 31, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1023,memory2 = 1024) == [64, 31, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1023,memory2 = 1024) == [64, 31, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1048576,memory2 = 1048576) == [2048, 0, 1024]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1048576,memory2 = 1048576) == [2048, 0, 1024]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 512,memory2 = 1024) == [55, 39, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 512,memory2 = 1024) == [55, 39, 12]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000000,memory2 = 1000000001) == [63245, 17494, 49117]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000000,memory2 = 1000000001) == [63245, 17494, 49117]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 4,memory2 = 5) == [4, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 4,memory2 = 5) == [4, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 0,memory2 = 2147483647) == [65536, 0, 32767]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 0,memory2 = 2147483647) == [65536, 0, 32767]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 512,memory2 = 2048) == [71, 8, 67]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 512,memory2 = 2048) == [71, 8, 67]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000,memory2 = 999999) == [2000, 999, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000,memory2 = 999999) == [2000, 999, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483647,memory2 = 2147483646) == [92681, 41706, 88047]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483647,memory2 = 2147483646) == [92681, 41706, 88047]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 4,memory2 = 4) == [4, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 4,memory2 = 4) == [4, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 4096,memory2 = 2048) == [110, 102, 47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 4096,memory2 = 2048) == [110, 102, 47]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1024,memory2 = 1024) == [64, 0, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1024,memory2 = 1024) == [64, 0, 32]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483646,memory2 = 1) == [65536, 32766, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483646,memory2 = 1) == [65536, 32766, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 234567890,memory2 = 234567890) == [30631, 18665, 3350]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 234567890,memory2 = 234567890) == [30631, 18665, 3350]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483646,memory2 = 2147483646) == [92681, 88046, 41706]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483646,memory2 = 2147483646) == [92681, 88046, 41706]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 1000000000) == [44721, 1, 38440]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 1000000000) == [44721, 1, 38440]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 999999999,memory2 = 1) == [44721, 38439, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 999999999,memory2 = 1) == [44721, 38439, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 500,memory2 = 500) == [44, 16, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 500,memory2 = 500) == [44, 16, 38]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2,memory2 = 1) == [2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2,memory2 = 1) == [2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 128,memory2 = 256) == [27, 23, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 128,memory2 = 256) == [27, 23, 10]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 1073741823) == [46341, 1, 20853]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 1073741823) == [46341, 1, 20853]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 100000,memory2 = 100000) == [632, 144, 460]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 100000,memory2 = 100000) == [632, 144, 460]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 4294967295,memory2 = 4294967295) == [131071, 131070, 65535]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 4294967295,memory2 = 4294967295) == [131071, 131070, 65535]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 0,memory2 = 1000) == [45, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 0,memory2 = 1000) == [45, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483646,memory2 = 2147483645) == [92681, 41705, 88046]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483646,memory2 = 2147483645) == [92681, 41705, 88046]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 10,memory2 = 1) == [5, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 10,memory2 = 1) == [5, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 0,memory2 = 1) == [2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 0,memory2 = 1) == [2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000001,memory2 = 1000000000) == [63245, 17494, 49117]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000001,memory2 = 1000000000) == [63245, 17494, 49117]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 2147483647) == [65536, 1, 32767]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 2147483647) == [65536, 1, 32767]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 100,memory2 = 0) == [14, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 100,memory2 = 0) == [14, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2147483646,memory2 = 2147483647) == [92681, 41706, 88047]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2147483646,memory2 = 2147483647) == [92681, 41706, 88047]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1073741823,memory2 = 1073741825) == [65536, 0, 32768]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1073741823,memory2 = 1073741825) == [65536, 0, 32768]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 10,memory2 = 15) == [7, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 10,memory2 = 15) == [7, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 9,memory2 = 9) == [6, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 9,memory2 = 9) == [6, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000,memory2 = 1000) == [63, 39, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000,memory2 = 1000) == [63, 39, 8]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 2048,memory2 = 4096) == [110, 47, 102]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 2048,memory2 = 4096) == [110, 47, 102]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000,memory2 = 0) == [45, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000,memory2 = 0) == [45, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1,memory2 = 5) == [3, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1,memory2 = 5) == [3, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(memory1 = 1000000000,memory2 = 1) == [44721, 38440, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(memory1 = 1000000000,memory2 = 1) == [44721, 38440, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(memory1 = 0,memory2 = 0) == [1, 0, 0]
    assert candidate(memory1 = 2147483647,memory2 = 2147483647) == [92681, 88047, 41707]
    assert candidate(memory1 = 1000000000,memory2 = 1000000000) == [63245, 49116, 17494]
    assert candidate(memory1 = 15,memory2 = 10) == [7, 4, 0]
    assert candidate(memory1 = 100,memory2 = 100) == [20, 0, 10]
    assert candidate(memory1 = 10,memory2 = 10) == [6, 1, 4]
    assert candidate(memory1 = 1073741823,memory2 = 1073741823) == [65535, 65534, 32767]
    assert candidate(memory1 = 1,memory2 = 1) == [2, 0, 1]
    assert candidate(memory1 = 8,memory2 = 11) == [6, 0, 4]
    assert candidate(memory1 = 1073741824,memory2 = 1073741824) == [65536, 0, 32768]
    assert candidate(memory1 = 15,memory2 = 15) == [7, 6, 3]
    assert candidate(memory1 = 1,memory2 = 2) == [2, 1, 1]
    assert candidate(memory1 = 15,memory2 = 5) == [6, 0, 5]
    assert candidate(memory1 = 100,memory2 = 50) == [17, 3, 11]
    assert candidate(memory1 = 2,memory2 = 2) == [3, 1, 0]
    assert candidate(memory1 = 1000000000,memory2 = 500000000) == [54772, 3472, 37922]
    assert candidate(memory1 = 0,memory2 = 1000000) == [1414, 0, 1009]
    assert candidate(memory1 = 1024,memory2 = 512) == [55, 12, 39]
    assert candidate(memory1 = 123456789,memory2 = 987654321) == [47140, 11258, 33622]
    assert candidate(memory1 = 256,memory2 = 255) == [32, 15, 0]
    assert candidate(memory1 = 1000000000,memory2 = 999999999) == [63245, 17493, 49116]
    assert candidate(memory1 = 2048,memory2 = 512) == [71, 67, 8]
    assert candidate(memory1 = 5,memory2 = 1) == [3, 2, 1]
    assert candidate(memory1 = 500000000,memory2 = 499999999) == [44721, 8039, 30400]
    assert candidate(memory1 = 100000,memory2 = 100001) == [632, 460, 145]
    assert candidate(memory1 = 1073741823,memory2 = 1073741824) == [65536, 32767, 0]
    assert candidate(memory1 = 2147483647,memory2 = 1073741824) == [80264, 34153, 76602]
    assert candidate(memory1 = 1000000,memory2 = 0) == [1414, 1009, 0]
    assert candidate(memory1 = 5,memory2 = 5) == [4, 1, 3]
    assert candidate(memory1 = 0,memory2 = 100) == [14, 0, 9]
    assert candidate(memory1 = 1000000000,memory2 = 2000000000) == [77459, 17790, 72599]
    assert candidate(memory1 = 500000000,memory2 = 500000001) == [44721, 8040, 30401]
    assert candidate(memory1 = 500000,memory2 = 500000) == [1414, 151, 858]
    assert candidate(memory1 = 2000000000,memory2 = 1000000000) == [77459, 72599, 17790]
    assert candidate(memory1 = 1,memory2 = 0) == [2, 0, 0]
    assert candidate(memory1 = 4000000000,memory2 = 3000000000) == [118321, 102440, 27200]
    assert candidate(memory1 = 1000000,memory2 = 1000000) == [2000, 0, 1000]
    assert candidate(memory1 = 3000000000,memory2 = 1000000000) == [89442, 62751, 46288]
    assert candidate(memory1 = 2147483647,memory2 = 0) == [65536, 32767, 0]
    assert candidate(memory1 = 500000000,memory2 = 500000000) == [44721, 30400, 8040]
    assert candidate(memory1 = 1234567890,memory2 = 1234567890) == [70272, 29394, 64530]
    assert candidate(memory1 = 1024,memory2 = 1023) == [64, 31, 0]
    assert candidate(memory1 = 1023,memory2 = 1024) == [64, 31, 0]
    assert candidate(memory1 = 1048576,memory2 = 1048576) == [2048, 0, 1024]
    assert candidate(memory1 = 512,memory2 = 1024) == [55, 39, 12]
    assert candidate(memory1 = 1000000000,memory2 = 1000000001) == [63245, 17494, 49117]
    assert candidate(memory1 = 4,memory2 = 5) == [4, 2, 1]
    assert candidate(memory1 = 0,memory2 = 2147483647) == [65536, 0, 32767]
    assert candidate(memory1 = 512,memory2 = 2048) == [71, 8, 67]
    assert candidate(memory1 = 1000000,memory2 = 999999) == [2000, 999, 0]
    assert candidate(memory1 = 2147483647,memory2 = 2147483646) == [92681, 41706, 88047]
    assert candidate(memory1 = 4,memory2 = 4) == [4, 0, 2]
    assert candidate(memory1 = 4096,memory2 = 2048) == [110, 102, 47]
    assert candidate(memory1 = 1024,memory2 = 1024) == [64, 0, 32]
    assert candidate(memory1 = 2147483646,memory2 = 1) == [65536, 32766, 1]
    assert candidate(memory1 = 234567890,memory2 = 234567890) == [30631, 18665, 3350]
    assert candidate(memory1 = 2147483646,memory2 = 2147483646) == [92681, 88046, 41706]
    assert candidate(memory1 = 1,memory2 = 1000000000) == [44721, 1, 38440]
    assert candidate(memory1 = 999999999,memory2 = 1) == [44721, 38439, 1]
    assert candidate(memory1 = 500,memory2 = 500) == [44, 16, 38]
    assert candidate(memory1 = 2,memory2 = 1) == [2, 1, 1]
    assert candidate(memory1 = 128,memory2 = 256) == [27, 23, 10]
    assert candidate(memory1 = 1,memory2 = 1073741823) == [46341, 1, 20853]
    assert candidate(memory1 = 100000,memory2 = 100000) == [632, 144, 460]
    assert candidate(memory1 = 4294967295,memory2 = 4294967295) == [131071, 131070, 65535]
    assert candidate(memory1 = 0,memory2 = 1000) == [45, 0, 10]
    assert candidate(memory1 = 2147483646,memory2 = 2147483645) == [92681, 41705, 88046]
    assert candidate(memory1 = 10,memory2 = 1) == [5, 0, 1]
    assert candidate(memory1 = 0,memory2 = 1) == [2, 0, 0]
    assert candidate(memory1 = 1000000001,memory2 = 1000000000) == [63245, 17494, 49117]
    assert candidate(memory1 = 1,memory2 = 2147483647) == [65536, 1, 32767]
    assert candidate(memory1 = 100,memory2 = 0) == [14, 9, 0]
    assert candidate(memory1 = 2147483646,memory2 = 2147483647) == [92681, 41706, 88047]
    assert candidate(memory1 = 1073741823,memory2 = 1073741825) == [65536, 0, 32768]
    assert candidate(memory1 = 10,memory2 = 15) == [7, 0, 4]
    assert candidate(memory1 = 9,memory2 = 9) == [6, 0, 3]
    assert candidate(memory1 = 1000,memory2 = 1000) == [63, 39, 8]
    assert candidate(memory1 = 2048,memory2 = 4096) == [110, 47, 102]
    assert candidate(memory1 = 1000,memory2 = 0) == [45, 10, 0]
    assert candidate(memory1 = 1,memory2 = 5) == [3, 1, 2]
    assert candidate(memory1 = 1000000000,memory2 = 1) == [44721, 38440, 1]


