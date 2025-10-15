def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = 2,maxDoubles = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2,maxDoubles = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 6,maxDoubles = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 6,maxDoubles = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000000,maxDoubles = 100) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000000,maxDoubles = 100) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,maxDoubles = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,maxDoubles = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,maxDoubles = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,maxDoubles = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 256,maxDoubles = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 256,maxDoubles = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 3,maxDoubles = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3,maxDoubles = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 3,maxDoubles = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3,maxDoubles = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,maxDoubles = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,maxDoubles = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,maxDoubles = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,maxDoubles = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 10,maxDoubles = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,maxDoubles = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,maxDoubles = 0) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,maxDoubles = 0) == 99: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,maxDoubles = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,maxDoubles = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,maxDoubles = 0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,maxDoubles = 0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,maxDoubles = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,maxDoubles = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 1,maxDoubles = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1,maxDoubles = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 1,maxDoubles = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1,maxDoubles = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 1,maxDoubles = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1,maxDoubles = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,maxDoubles = 0) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,maxDoubles = 0) == 19: {e}')
    
    total += 1
    try:
        result = candidate(target = 19,maxDoubles = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 19,maxDoubles = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 6,maxDoubles = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 6,maxDoubles = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 1023,maxDoubles = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1023,maxDoubles = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000000,maxDoubles = 50) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000000,maxDoubles = 50) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 8193,maxDoubles = 13) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8193,maxDoubles = 13) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 4095,maxDoubles = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4095,maxDoubles = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(target = 32768,maxDoubles = 16) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 32768,maxDoubles = 16) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 123456789,maxDoubles = 30) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123456789,maxDoubles = 30) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 987654321,maxDoubles = 25) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 987654321,maxDoubles = 25) == 66: {e}')
    
    total += 1
    try:
        result = candidate(target = 34359738367,maxDoubles = 35) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 34359738367,maxDoubles = 35) == 68: {e}')
    
    total += 1
    try:
        result = candidate(target = 32767,maxDoubles = 15) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 32767,maxDoubles = 15) == 28: {e}')
    
    total += 1
    try:
        result = candidate(target = 524288,maxDoubles = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 524288,maxDoubles = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(target = 246813579,maxDoubles = 0) == 246813578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 246813579,maxDoubles = 0) == 246813578: {e}')
    
    total += 1
    try:
        result = candidate(target = 333333333,maxDoubles = 100) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 333333333,maxDoubles = 100) == 43: {e}')
    
    total += 1
    try:
        result = candidate(target = 8192,maxDoubles = 12) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8192,maxDoubles = 12) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,maxDoubles = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,maxDoubles = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 63,maxDoubles = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 63,maxDoubles = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(target = 16,maxDoubles = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16,maxDoubles = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 4294967295,maxDoubles = 32) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4294967295,maxDoubles = 32) == 62: {e}')
    
    total += 1
    try:
        result = candidate(target = 2147483647,maxDoubles = 20) == 2086
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2147483647,maxDoubles = 20) == 2086: {e}')
    
    total += 1
    try:
        result = candidate(target = 255,maxDoubles = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 255,maxDoubles = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 2,maxDoubles = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2,maxDoubles = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 8192,maxDoubles = 13) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8192,maxDoubles = 13) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 131072,maxDoubles = 18) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 131072,maxDoubles = 18) == 17: {e}')
    
    total += 1
    try:
        result = candidate(target = 4,maxDoubles = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4,maxDoubles = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 131071,maxDoubles = 17) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 131071,maxDoubles = 17) == 32: {e}')
    
    total += 1
    try:
        result = candidate(target = 17179869183,maxDoubles = 34) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 17179869183,maxDoubles = 34) == 66: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,maxDoubles = 0) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,maxDoubles = 0) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 1,maxDoubles = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1,maxDoubles = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 999999999,maxDoubles = 100) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999999999,maxDoubles = 100) == 49: {e}')
    
    total += 1
    try:
        result = candidate(target = 777777777,maxDoubles = 75) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 777777777,maxDoubles = 75) == 46: {e}')
    
    total += 1
    try:
        result = candidate(target = 95,maxDoubles = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 95,maxDoubles = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 68719476735,maxDoubles = 36) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 68719476735,maxDoubles = 36) == 70: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,maxDoubles = 9) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,maxDoubles = 9) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 999999999,maxDoubles = 0) == 999999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999999999,maxDoubles = 0) == 999999998: {e}')
    
    total += 1
    try:
        result = candidate(target = 987654321,maxDoubles = 50) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 987654321,maxDoubles = 50) == 45: {e}')
    
    total += 1
    try:
        result = candidate(target = 19,maxDoubles = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 19,maxDoubles = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 1001,maxDoubles = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1001,maxDoubles = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,maxDoubles = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,maxDoubles = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 16,maxDoubles = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16,maxDoubles = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 23,maxDoubles = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 23,maxDoubles = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 65535,maxDoubles = 16) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65535,maxDoubles = 16) == 30: {e}')
    
    total += 1
    try:
        result = candidate(target = 16,maxDoubles = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16,maxDoubles = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 31,maxDoubles = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 31,maxDoubles = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 500000,maxDoubles = 15) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500000,maxDoubles = 15) == 32: {e}')
    
    total += 1
    try:
        result = candidate(target = 47,maxDoubles = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 47,maxDoubles = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = 1023,maxDoubles = 0) == 1022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1023,maxDoubles = 0) == 1022: {e}')
    
    total += 1
    try:
        result = candidate(target = 199999999,maxDoubles = 100) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 199999999,maxDoubles = 100) == 46: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,maxDoubles = 0) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,maxDoubles = 0) == 499: {e}')
    
    total += 1
    try:
        result = candidate(target = 987654321,maxDoubles = 0) == 987654320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 987654321,maxDoubles = 0) == 987654320: {e}')
    
    total += 1
    try:
        result = candidate(target = 2048,maxDoubles = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2048,maxDoubles = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 19,maxDoubles = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 19,maxDoubles = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 123456789,maxDoubles = 50) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123456789,maxDoubles = 50) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 1023,maxDoubles = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1023,maxDoubles = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(target = 10000,maxDoubles = 100) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10000,maxDoubles = 100) == 17: {e}')
    
    total += 1
    try:
        result = candidate(target = 4,maxDoubles = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4,maxDoubles = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 15,maxDoubles = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15,maxDoubles = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 2147483647,maxDoubles = 31) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2147483647,maxDoubles = 31) == 60: {e}')
    
    total += 1
    try:
        result = candidate(target = 23456789,maxDoubles = 20) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 23456789,maxDoubles = 20) == 51: {e}')
    
    total += 1
    try:
        result = candidate(target = 1024,maxDoubles = 512) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1024,maxDoubles = 512) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,maxDoubles = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,maxDoubles = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 4095,maxDoubles = 12) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4095,maxDoubles = 12) == 22: {e}')
    
    total += 1
    try:
        result = candidate(target = 11,maxDoubles = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 11,maxDoubles = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 511,maxDoubles = 8) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 511,maxDoubles = 8) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 127,maxDoubles = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 127,maxDoubles = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000,maxDoubles = 0) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000,maxDoubles = 0) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(target = 9,maxDoubles = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 9,maxDoubles = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 32768,maxDoubles = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 32768,maxDoubles = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 8192,maxDoubles = 0) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8192,maxDoubles = 0) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(target = 123456,maxDoubles = 20) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123456,maxDoubles = 20) == 21: {e}')
    
    total += 1
    try:
        result = candidate(target = 987654321,maxDoubles = 10) == 964519
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 987654321,maxDoubles = 10) == 964519: {e}')
    
    total += 1
    try:
        result = candidate(target = 262143,maxDoubles = 18) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 262143,maxDoubles = 18) == 34: {e}')
    
    total += 1
    try:
        result = candidate(target = 128,maxDoubles = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 128,maxDoubles = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 131072,maxDoubles = 16) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 131072,maxDoubles = 16) == 17: {e}')
    
    total += 1
    try:
        result = candidate(target = 1048576,maxDoubles = 21) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1048576,maxDoubles = 21) == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = 31,maxDoubles = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 31,maxDoubles = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 987654321,maxDoubles = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 987654321,maxDoubles = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(target = 65536,maxDoubles = 17) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65536,maxDoubles = 17) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 127,maxDoubles = 6) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 127,maxDoubles = 6) == 12: {e}')
    
    total += 1
    try:
        result = candidate(target = 8589934591,maxDoubles = 33) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8589934591,maxDoubles = 33) == 64: {e}')
    
    total += 1
    try:
        result = candidate(target = 2,maxDoubles = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2,maxDoubles = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 16,maxDoubles = 0) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16,maxDoubles = 0) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 1023,maxDoubles = 9) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1023,maxDoubles = 9) == 18: {e}')
    
    total += 1
    try:
        result = candidate(target = 500000000,maxDoubles = 10) == 488291
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500000000,maxDoubles = 10) == 488291: {e}')
    
    total += 1
    try:
        result = candidate(target = 25,maxDoubles = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25,maxDoubles = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 1024,maxDoubles = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1024,maxDoubles = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 8191,maxDoubles = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8191,maxDoubles = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(target = 16384,maxDoubles = 16) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16384,maxDoubles = 16) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 678901234,maxDoubles = 50) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 678901234,maxDoubles = 50) == 45: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,maxDoubles = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,maxDoubles = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 63,maxDoubles = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 63,maxDoubles = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 999999999,maxDoubles = 1) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999999999,maxDoubles = 1) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(target = 1048575,maxDoubles = 20) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1048575,maxDoubles = 20) == 38: {e}')
    
    total += 1
    try:
        result = candidate(target = 64,maxDoubles = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 64,maxDoubles = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 137438953471,maxDoubles = 37) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 137438953471,maxDoubles = 37) == 72: {e}')
    
    total += 1
    try:
        result = candidate(target = 135792468,maxDoubles = 10) == 132623
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 135792468,maxDoubles = 10) == 132623: {e}')
    
    total += 1
    try:
        result = candidate(target = 8,maxDoubles = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8,maxDoubles = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 1048576,maxDoubles = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1048576,maxDoubles = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = 123456789,maxDoubles = 25) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123456789,maxDoubles = 25) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 888888888,maxDoubles = 88) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 888888888,maxDoubles = 88) == 46: {e}')
    
    total += 1
    try:
        result = candidate(target = 32,maxDoubles = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 32,maxDoubles = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 65535,maxDoubles = 0) == 65534
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65535,maxDoubles = 0) == 65534: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000000,maxDoubles = 1) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000000,maxDoubles = 1) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(target = 16,maxDoubles = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16,maxDoubles = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 2047,maxDoubles = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2047,maxDoubles = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = 2048,maxDoubles = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2048,maxDoubles = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 16,maxDoubles = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16,maxDoubles = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,maxDoubles = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,maxDoubles = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000000,maxDoubles = 0) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000000,maxDoubles = 0) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(target = 999999999,maxDoubles = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999999999,maxDoubles = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(target = 65535,maxDoubles = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65535,maxDoubles = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(target = 7,maxDoubles = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7,maxDoubles = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 31,maxDoubles = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 31,maxDoubles = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = 262144,maxDoubles = 19) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 262144,maxDoubles = 19) == 18: {e}')
    
    total += 1
    try:
        result = candidate(target = 524287,maxDoubles = 19) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 524287,maxDoubles = 19) == 36: {e}')
    
    total += 1
    try:
        result = candidate(target = 19,maxDoubles = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 19,maxDoubles = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 268435456,maxDoubles = 28) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 268435456,maxDoubles = 28) == 28: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000000,maxDoubles = 30) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000000,maxDoubles = 30) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 512,maxDoubles = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 512,maxDoubles = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = 16383,maxDoubles = 14) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16383,maxDoubles = 14) == 26: {e}')
    
    total += 1
    try:
        result = candidate(target = 8973424,maxDoubles = 50) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8973424,maxDoubles = 50) == 32: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = 2,maxDoubles = 1) == 1
    assert candidate(target = 6,maxDoubles = 0) == 5
    assert candidate(target = 1000000000,maxDoubles = 100) == 41
    assert candidate(target = 8,maxDoubles = 3) == 3
    assert candidate(target = 100,maxDoubles = 10) == 8
    assert candidate(target = 256,maxDoubles = 8) == 8
    assert candidate(target = 3,maxDoubles = 1) == 2
    assert candidate(target = 3,maxDoubles = 2) == 2
    assert candidate(target = 7,maxDoubles = 1) == 4
    assert candidate(target = 100,maxDoubles = 5) == 8
    assert candidate(target = 10,maxDoubles = 4) == 4
    assert candidate(target = 100,maxDoubles = 0) == 99
    assert candidate(target = 100,maxDoubles = 1) == 50
    assert candidate(target = 5,maxDoubles = 0) == 4
    assert candidate(target = 7,maxDoubles = 0) == 6
    assert candidate(target = 1,maxDoubles = 5) == 0
    assert candidate(target = 1,maxDoubles = 1) == 0
    assert candidate(target = 1,maxDoubles = 10) == 0
    assert candidate(target = 20,maxDoubles = 0) == 19
    assert candidate(target = 19,maxDoubles = 2) == 7
    assert candidate(target = 6,maxDoubles = 1) == 3
    assert candidate(target = 1023,maxDoubles = 10) == 18
    assert candidate(target = 1000000000,maxDoubles = 50) == 41
    assert candidate(target = 8193,maxDoubles = 13) == 14
    assert candidate(target = 4095,maxDoubles = 10) == 22
    assert candidate(target = 32768,maxDoubles = 16) == 15
    assert candidate(target = 123456789,maxDoubles = 30) == 41
    assert candidate(target = 987654321,maxDoubles = 25) == 66
    assert candidate(target = 34359738367,maxDoubles = 35) == 68
    assert candidate(target = 32767,maxDoubles = 15) == 28
    assert candidate(target = 524288,maxDoubles = 20) == 19
    assert candidate(target = 246813579,maxDoubles = 0) == 246813578
    assert candidate(target = 333333333,maxDoubles = 100) == 43
    assert candidate(target = 8192,maxDoubles = 12) == 13
    assert candidate(target = 15,maxDoubles = 1) == 8
    assert candidate(target = 63,maxDoubles = 3) == 12
    assert candidate(target = 16,maxDoubles = 4) == 4
    assert candidate(target = 4294967295,maxDoubles = 32) == 62
    assert candidate(target = 2147483647,maxDoubles = 20) == 2086
    assert candidate(target = 255,maxDoubles = 7) == 14
    assert candidate(target = 2,maxDoubles = 2) == 1
    assert candidate(target = 8192,maxDoubles = 13) == 13
    assert candidate(target = 131072,maxDoubles = 18) == 17
    assert candidate(target = 4,maxDoubles = 1) == 2
    assert candidate(target = 131071,maxDoubles = 17) == 32
    assert candidate(target = 17179869183,maxDoubles = 34) == 66
    assert candidate(target = 8,maxDoubles = 0) == 7
    assert candidate(target = 1,maxDoubles = 0) == 0
    assert candidate(target = 999999999,maxDoubles = 100) == 49
    assert candidate(target = 777777777,maxDoubles = 75) == 46
    assert candidate(target = 95,maxDoubles = 6) == 11
    assert candidate(target = 68719476735,maxDoubles = 36) == 70
    assert candidate(target = 500,maxDoubles = 9) == 13
    assert candidate(target = 999999999,maxDoubles = 0) == 999999998
    assert candidate(target = 987654321,maxDoubles = 50) == 45
    assert candidate(target = 19,maxDoubles = 1) == 10
    assert candidate(target = 1001,maxDoubles = 10) == 15
    assert candidate(target = 8,maxDoubles = 4) == 3
    assert candidate(target = 16,maxDoubles = 5) == 4
    assert candidate(target = 23,maxDoubles = 3) == 7
    assert candidate(target = 65535,maxDoubles = 16) == 30
    assert candidate(target = 16,maxDoubles = 3) == 4
    assert candidate(target = 31,maxDoubles = 3) == 8
    assert candidate(target = 500000,maxDoubles = 15) == 32
    assert candidate(target = 47,maxDoubles = 5) == 9
    assert candidate(target = 1023,maxDoubles = 0) == 1022
    assert candidate(target = 199999999,maxDoubles = 100) == 46
    assert candidate(target = 500,maxDoubles = 0) == 499
    assert candidate(target = 987654321,maxDoubles = 0) == 987654320
    assert candidate(target = 2048,maxDoubles = 15) == 11
    assert candidate(target = 19,maxDoubles = 3) == 6
    assert candidate(target = 123456789,maxDoubles = 50) == 41
    assert candidate(target = 1023,maxDoubles = 5) == 40
    assert candidate(target = 10000,maxDoubles = 100) == 17
    assert candidate(target = 4,maxDoubles = 2) == 2
    assert candidate(target = 15,maxDoubles = 3) == 6
    assert candidate(target = 2147483647,maxDoubles = 31) == 60
    assert candidate(target = 23456789,maxDoubles = 20) == 51
    assert candidate(target = 1024,maxDoubles = 512) == 10
    assert candidate(target = 8,maxDoubles = 2) == 3
    assert candidate(target = 4095,maxDoubles = 12) == 22
    assert candidate(target = 11,maxDoubles = 2) == 5
    assert candidate(target = 511,maxDoubles = 8) == 16
    assert candidate(target = 127,maxDoubles = 4) == 14
    assert candidate(target = 1000000,maxDoubles = 0) == 999999
    assert candidate(target = 9,maxDoubles = 1) == 5
    assert candidate(target = 32768,maxDoubles = 15) == 15
    assert candidate(target = 8192,maxDoubles = 0) == 8191
    assert candidate(target = 123456,maxDoubles = 20) == 21
    assert candidate(target = 987654321,maxDoubles = 10) == 964519
    assert candidate(target = 262143,maxDoubles = 18) == 34
    assert candidate(target = 128,maxDoubles = 7) == 7
    assert candidate(target = 131072,maxDoubles = 16) == 17
    assert candidate(target = 1048576,maxDoubles = 21) == 20
    assert candidate(target = 31,maxDoubles = 5) == 8
    assert candidate(target = 987654321,maxDoubles = 45) == 45
    assert candidate(target = 65536,maxDoubles = 17) == 16
    assert candidate(target = 127,maxDoubles = 6) == 12
    assert candidate(target = 8589934591,maxDoubles = 33) == 64
    assert candidate(target = 2,maxDoubles = 0) == 1
    assert candidate(target = 16,maxDoubles = 0) == 15
    assert candidate(target = 1023,maxDoubles = 9) == 18
    assert candidate(target = 500000000,maxDoubles = 10) == 488291
    assert candidate(target = 25,maxDoubles = 3) == 6
    assert candidate(target = 1024,maxDoubles = 10) == 10
    assert candidate(target = 8191,maxDoubles = 10) == 26
    assert candidate(target = 16384,maxDoubles = 16) == 14
    assert candidate(target = 678901234,maxDoubles = 50) == 45
    assert candidate(target = 7,maxDoubles = 3) == 4
    assert candidate(target = 63,maxDoubles = 5) == 10
    assert candidate(target = 999999999,maxDoubles = 1) == 500000000
    assert candidate(target = 1048575,maxDoubles = 20) == 38
    assert candidate(target = 64,maxDoubles = 6) == 6
    assert candidate(target = 137438953471,maxDoubles = 37) == 72
    assert candidate(target = 135792468,maxDoubles = 10) == 132623
    assert candidate(target = 8,maxDoubles = 1) == 4
    assert candidate(target = 1048576,maxDoubles = 20) == 20
    assert candidate(target = 123456789,maxDoubles = 25) == 41
    assert candidate(target = 888888888,maxDoubles = 88) == 46
    assert candidate(target = 32,maxDoubles = 5) == 5
    assert candidate(target = 65535,maxDoubles = 0) == 65534
    assert candidate(target = 1000000000,maxDoubles = 1) == 500000000
    assert candidate(target = 16,maxDoubles = 1) == 8
    assert candidate(target = 2047,maxDoubles = 10) == 20
    assert candidate(target = 2048,maxDoubles = 10) == 11
    assert candidate(target = 16,maxDoubles = 2) == 5
    assert candidate(target = 1000,maxDoubles = 10) == 14
    assert candidate(target = 1000000000,maxDoubles = 0) == 999999999
    assert candidate(target = 999999999,maxDoubles = 50) == 49
    assert candidate(target = 65535,maxDoubles = 15) == 30
    assert candidate(target = 7,maxDoubles = 2) == 4
    assert candidate(target = 31,maxDoubles = 4) == 8
    assert candidate(target = 262144,maxDoubles = 19) == 18
    assert candidate(target = 524287,maxDoubles = 19) == 36
    assert candidate(target = 19,maxDoubles = 4) == 6
    assert candidate(target = 268435456,maxDoubles = 28) == 28
    assert candidate(target = 1000000000,maxDoubles = 30) == 41
    assert candidate(target = 512,maxDoubles = 9) == 9
    assert candidate(target = 16383,maxDoubles = 14) == 26
    assert candidate(target = 8973424,maxDoubles = 50) == 32


