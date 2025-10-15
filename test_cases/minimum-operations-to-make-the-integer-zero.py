def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 7,num2 = -3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 7,num2 = -3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 15,num2 = -3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 15,num2 = -3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 10,num2 = -3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 10,num2 = -3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 15,num2 = -5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 15,num2 = -5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 31,num2 = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 31,num2 = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = 987654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = 987654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = -10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = -10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 64,num2 = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 64,num2 = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = -1000000000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = -1000000000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 5,num2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 5,num2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 3,num2 = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 3,num2 = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 10,num2 = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 10,num2 = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = -3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = -3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -512) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -512) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = -536870912) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = -536870912) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = 10000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = 10000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -1024) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -1024) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1024,num2 = -255) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1024,num2 = -255) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 127,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 127,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = -987654321) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = -987654321) == 16: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = -500000000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = -500000000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 511,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 511,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 536870912,num2 = 268435456) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 536870912,num2 = 268435456) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = -999999998) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = -999999998) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 32767,num2 = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 32767,num2 = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 63,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 63,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = 1) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = 1) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 262143,num2 = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 262143,num2 = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = -10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = -10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = -999999999) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = -999999999) == 19: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 0) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 0) == 21: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048575,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048575,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2047,num2 = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2047,num2 = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 513,num2 = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 513,num2 = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 16383,num2 = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 16383,num2 = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 100000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 100000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2,num2 = -2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2,num2 = -2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 682,num2 = -1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 682,num2 = -1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4095,num2 = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4095,num2 = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 63,num2 = -31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 63,num2 = -31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4503599627370496,num2 = -1024) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4503599627370496,num2 = -1024) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = 268435456) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = 268435456) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741823,num2 = 1) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741823,num2 = 1) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -65536) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -65536) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 98765,num2 = -49382) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 98765,num2 = -49382) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2048,num2 = -1024) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2048,num2 = -1024) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 511,num2 = -255) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 511,num2 = -255) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4095,num2 = -10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4095,num2 = -10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2048,num2 = 512) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2048,num2 = 512) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = 2147483648) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = 2147483648) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = -3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = -3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = -2147483647) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = -2147483647) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1024,num2 = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1024,num2 = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 15,num2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 15,num2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 524287,num2 = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 524287,num2 = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 15,num2 = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 15,num2 = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 131071,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 131071,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048575,num2 = 3) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048575,num2 = 3) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = 1073741823) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = 1073741823) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741823,num2 = 2) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741823,num2 = 2) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1024,num2 = -128) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1024,num2 = -128) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 128,num2 = -32) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 128,num2 = -32) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2048,num2 = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2048,num2 = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2048,num2 = -512) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2048,num2 = -512) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 549755813888,num2 = 1000000) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 549755813888,num2 = 1000000) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 255,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 255,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = 1048576) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = 1048576) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 987654321,num2 = -98765432) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 987654321,num2 = -98765432) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 65535,num2 = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 65535,num2 = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 42,num2 = -21) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 42,num2 = -21) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = 1048575) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = 1048575) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1024,num2 = -100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1024,num2 = -100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = -100000000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = -100000000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 512,num2 = -512) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 512,num2 = -512) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 127,num2 = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 127,num2 = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000,num2 = 333) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000,num2 = 333) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 500000000,num2 = 250000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 500000000,num2 = 250000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -262144) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -262144) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -524288) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -524288) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 31,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 31,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 68719476736,num2 = 1) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 68719476736,num2 = 1) == 32: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2,num2 = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2,num2 = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100000,num2 = 10000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100000,num2 = 10000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 15,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 15,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 1000000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 1000000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = 1024) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = 1024) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = -512) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = -512) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 268435456,num2 = -33554432) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 268435456,num2 = -33554432) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = -1073741824) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = -1073741824) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = -999999999) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = -999999999) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = -1000000000) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = -1000000000) == 21: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -1048576) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -1048576) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = -1000000000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = -1000000000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4294967295,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4294967295,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 512,num2 = -256) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 512,num2 = -256) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 63,num2 = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 63,num2 = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 255,num2 = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 255,num2 = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = -1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = -1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048576,num2 = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048576,num2 = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1024,num2 = 512) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1024,num2 = 512) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 500000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 500000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = -511) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = -511) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = 123456789) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = 123456789) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8191,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8191,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048575,num2 = 1) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048575,num2 = 1) == 18: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 134217727,num2 = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 134217727,num2 = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 100000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 100000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 500000000,num2 = 500000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 500000000,num2 = 500000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = -98765432) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = -98765432) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num1 = 8,num2 = 2) == 2
    assert candidate(num1 = 8,num2 = -1) == 2
    assert candidate(num1 = 7,num2 = -3) == 3
    assert candidate(num1 = 1,num2 = 0) == 1
    assert candidate(num1 = 15,num2 = -3) == 3
    assert candidate(num1 = 10,num2 = -3) == 2
    assert candidate(num1 = 1,num2 = 1) == -1
    assert candidate(num1 = 15,num2 = -5) == 4
    assert candidate(num1 = 31,num2 = -2) == 3
    assert candidate(num1 = 123456789,num2 = 987654321) == -1
    assert candidate(num1 = 100,num2 = -10) == 3
    assert candidate(num1 = 64,num2 = -1) == 2
    assert candidate(num1 = 1000000000,num2 = -1000000000) == 12
    assert candidate(num1 = 5,num2 = 7) == -1
    assert candidate(num1 = 3,num2 = -2) == 3
    assert candidate(num1 = 10,num2 = -1) == 2
    assert candidate(num1 = 8,num2 = -3) == 3
    assert candidate(num1 = 1048576,num2 = -512) == 2
    assert candidate(num1 = 1000000000,num2 = 1) == 19
    assert candidate(num1 = 1,num2 = 2) == -1
    assert candidate(num1 = 1073741824,num2 = -536870912) == 2
    assert candidate(num1 = 123456789,num2 = 10000000) == -1
    assert candidate(num1 = 1048576,num2 = -1024) == 2
    assert candidate(num1 = 1024,num2 = -255) == 8
    assert candidate(num1 = 127,num2 = -1) == 1
    assert candidate(num1 = 123456789,num2 = -987654321) == 16
    assert candidate(num1 = 1000000000,num2 = -500000000) == 11
    assert candidate(num1 = 511,num2 = -1) == 1
    assert candidate(num1 = 536870912,num2 = 268435456) == 1
    assert candidate(num1 = 999999999,num2 = -999999998) == 17
    assert candidate(num1 = 32767,num2 = -2) == 3
    assert candidate(num1 = 63,num2 = -1) == 1
    assert candidate(num1 = 2147483647,num2 = 1) == 27
    assert candidate(num1 = 262143,num2 = 1) == 15
    assert candidate(num1 = 1023,num2 = -10) == 5
    assert candidate(num1 = 1000000000,num2 = -999999999) == 19
    assert candidate(num1 = 999999999,num2 = 0) == 21
    assert candidate(num1 = 1023,num2 = 1) == 7
    assert candidate(num1 = 1048575,num2 = -1) == 1
    assert candidate(num1 = 2047,num2 = -2) == 3
    assert candidate(num1 = 513,num2 = 2) == 7
    assert candidate(num1 = 16383,num2 = 1) == 11
    assert candidate(num1 = 1000000000,num2 = 100000000) == -1
    assert candidate(num1 = 2,num2 = -2) == 1
    assert candidate(num1 = 682,num2 = -1) == 6
    assert candidate(num1 = 1023,num2 = -1) == 1
    assert candidate(num1 = 4095,num2 = 3) == 9
    assert candidate(num1 = 63,num2 = -31) == 5
    assert candidate(num1 = 4503599627370496,num2 = -1024) == 2
    assert candidate(num1 = 1073741824,num2 = 268435456) == 2
    assert candidate(num1 = 1073741823,num2 = 1) == 27
    assert candidate(num1 = 1048576,num2 = -65536) == 2
    assert candidate(num1 = 98765,num2 = -49382) == 9
    assert candidate(num1 = 2048,num2 = -1024) == 2
    assert candidate(num1 = 511,num2 = -255) == 7
    assert candidate(num1 = 4095,num2 = -10) == 5
    assert candidate(num1 = 2048,num2 = 512) == 2
    assert candidate(num1 = 100,num2 = 50) == -1
    assert candidate(num1 = 1073741824,num2 = 2147483648) == -1
    assert candidate(num1 = 1023,num2 = -3) == 3
    assert candidate(num1 = 2147483647,num2 = -2147483647) == 31
    assert candidate(num1 = 1024,num2 = 0) == 1
    assert candidate(num1 = 15,num2 = 1) == 3
    assert candidate(num1 = 524287,num2 = -2) == 3
    assert candidate(num1 = 15,num2 = 3) == 2
    assert candidate(num1 = 131071,num2 = -1) == 1
    assert candidate(num1 = 1048575,num2 = 3) == 17
    assert candidate(num1 = 1073741824,num2 = 1073741823) == 1
    assert candidate(num1 = 1073741823,num2 = 2) == 27
    assert candidate(num1 = 1024,num2 = -128) == 2
    assert candidate(num1 = 128,num2 = -32) == 2
    assert candidate(num1 = 2048,num2 = 1024) == 1
    assert candidate(num1 = 2048,num2 = -512) == 2
    assert candidate(num1 = 549755813888,num2 = 1000000) == 22
    assert candidate(num1 = 255,num2 = -1) == 1
    assert candidate(num1 = 1048576,num2 = 1048576) == -1
    assert candidate(num1 = 987654321,num2 = -98765432) == 12
    assert candidate(num1 = 65535,num2 = 3) == 13
    assert candidate(num1 = 999999999,num2 = 1) == 19
    assert candidate(num1 = 42,num2 = -21) == 5
    assert candidate(num1 = 1048576,num2 = 1048575) == 1
    assert candidate(num1 = 1024,num2 = -100) == 4
    assert candidate(num1 = 1000000000,num2 = -100000000) == 12
    assert candidate(num1 = 512,num2 = -512) == 1
    assert candidate(num1 = 127,num2 = -2) == 3
    assert candidate(num1 = 1000,num2 = 333) == -1
    assert candidate(num1 = 500000000,num2 = 250000000) == -1
    assert candidate(num1 = 1048576,num2 = -262144) == 2
    assert candidate(num1 = 1048576,num2 = -524288) == 2
    assert candidate(num1 = 31,num2 = -1) == 1
    assert candidate(num1 = 68719476736,num2 = 1) == 32
    assert candidate(num1 = 1048576,num2 = -1) == 2
    assert candidate(num1 = 2,num2 = 1) == 1
    assert candidate(num1 = 100000,num2 = 10000) == 6
    assert candidate(num1 = 15,num2 = -1) == 1
    assert candidate(num1 = 999999999,num2 = 1000000000) == -1
    assert candidate(num1 = 1048576,num2 = 1024) == 8
    assert candidate(num1 = 1023,num2 = -512) == 11
    assert candidate(num1 = 268435456,num2 = -33554432) == 2
    assert candidate(num1 = 1073741824,num2 = -1073741824) == 1
    assert candidate(num1 = 999999999,num2 = -999999999) == 17
    assert candidate(num1 = 2147483647,num2 = -1000000000) == 21
    assert candidate(num1 = 1048576,num2 = -1048576) == 1
    assert candidate(num1 = 1,num2 = -1000000000) == 13
    assert candidate(num1 = 4294967295,num2 = -1) == 1
    assert candidate(num1 = 512,num2 = -256) == 2
    assert candidate(num1 = 63,num2 = 1) == 5
    assert candidate(num1 = 1048576,num2 = 1) == 16
    assert candidate(num1 = 255,num2 = 3) == 5
    assert candidate(num1 = 1048576,num2 = -1000) == 8
    assert candidate(num1 = 1048576,num2 = 0) == 1
    assert candidate(num1 = 1024,num2 = 512) == 1
    assert candidate(num1 = 1000000000,num2 = 500000000) == -1
    assert candidate(num1 = 1,num2 = -1) == 1
    assert candidate(num1 = 1023,num2 = -511) == 7
    assert candidate(num1 = 123456789,num2 = 123456789) == -1
    assert candidate(num1 = 8191,num2 = -1) == 1
    assert candidate(num1 = 1048575,num2 = 1) == 18
    assert candidate(num1 = 134217727,num2 = -1) == 1
    assert candidate(num1 = 999999999,num2 = 100000000) == -1
    assert candidate(num1 = 500000000,num2 = 500000000) == -1
    assert candidate(num1 = 123456789,num2 = -98765432) == 12


