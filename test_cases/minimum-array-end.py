def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,x = 8) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,x = 8) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,x = 7) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,x = 7) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 16) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 16) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 32) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 32) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,x = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,x = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,x = 256) == 1000223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,x = 256) == 1000223: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,x = 2048) == 2077
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,x = 2048) == 2077: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,x = 2047) == 1023999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,x = 2047) == 1023999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 512) == 561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 512) == 561: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 128) == 227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 128) == 227: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 4096) == 4103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 4096) == 4103: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 8) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 8) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,x = 65535) == 6553599999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,x = 65535) == 6553599999: {e}')
    
    total += 1
    try:
        result = candidate(n = 512,x = 32768) == 33279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512,x = 32768) == 33279: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,x = 12) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,x = 12) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 8) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 8) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,x = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,x = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 16) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 16) == 51: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 3) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 3) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,x = 3) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,x = 3) == 47: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 1073741824) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 1073741824) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,x = 512) == 2023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,x = 512) == 2023: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 1023) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 1023) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,x = 1073741823) == 107374182399999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,x = 1073741823) == 107374182399999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 16) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 16) == 211: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,x = 17) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,x = 17) == 123: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,x = 64) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,x = 64) == 93: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 31) == 479
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 31) == 479: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 255) == 25599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 255) == 25599: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,x = 63) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,x = 63) == 255: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 1023) == 5119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 1023) == 5119: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 1024) == 1033
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 1024) == 1033: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 7) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 7) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,x = 31) == 1599999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,x = 31) == 1599999: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,x = 512) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,x = 512) == 520: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,x = 15) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,x = 15) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,x = 2048) == 2053
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,x = 2048) == 2053: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,x = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,x = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 100) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 100) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,x = 10) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,x = 10) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,x = 16) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,x = 16) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 2048) == 2097
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 2048) == 2097: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,x = 4096) == 5095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,x = 4096) == 5095: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 1048575) == 10485759
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 1048575) == 10485759: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 1024) == 1038
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 1024) == 1038: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 128) == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 128) == 177: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 2047) == 40959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 2047) == 40959: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,x = 2048) == 2072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,x = 2048) == 2072: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,x = 24) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,x = 24) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,x = 128) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,x = 128) == 134: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 1047552) == 1047651
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 1047552) == 1047651: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 512) == 526
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 512) == 526: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,x = 12) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,x = 12) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 512) == 531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 512) == 531: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 1023) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 1023) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,x = 1023) == 102399999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,x = 1023) == 102399999: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,x = 31) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,x = 31) == 95: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 31) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 31) == 159: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 31) == 1599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 31) == 1599: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,x = 512) == 1011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,x = 512) == 1011: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000,x = 4095) == 40959999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000,x = 4095) == 40959999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,x = 2048) == 2111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,x = 2048) == 2111: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 32) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 32) == 39: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,x = 13) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,x = 13) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 31) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 31) == 255: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,x = 64) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,x = 64) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 1024) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 1024) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024,x = 65535) == 67108863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024,x = 65535) == 67108863: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 4096) == 4195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 4096) == 4195: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,x = 1024) == 1030
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,x = 1024) == 1030: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,x = 256) == 264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,x = 256) == 264: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,x = 2048) == 3047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,x = 2048) == 3047: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 32) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 32) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 255) == 12799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 255) == 12799: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,x = 128) == 200095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,x = 128) == 200095: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,x = 1) == 199999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,x = 1) == 199999: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 255) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 255) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 15) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 15) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 256) == 355
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 256) == 355: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,x = 128) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,x = 128) == 152: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,x = 64) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,x = 64) == 69: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,x = 32) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,x = 32) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 12) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 12) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 2048) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 2048) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,x = 1073741823) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,x = 1073741823) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,x = 1023) == 14335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,x = 1023) == 14335: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 1024) == 1073
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 1024) == 1073: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,x = 8192) == 8391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,x = 8192) == 8391: {e}')
    
    total += 1
    try:
        result = candidate(n = 128,x = 16383) == 2097151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128,x = 16383) == 2097151: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 3) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 3) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,x = 512) == 522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,x = 512) == 522: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 256) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 256) == 265: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 8191) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 8191) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 1048575) == 1048575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 1048575) == 1048575: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,x = 8191) == 245759
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,x = 8191) == 245759: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,x = 17) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,x = 17) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,x = 512) == 541
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,x = 512) == 541: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 7) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 7) == 119: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,x = 255) == 2303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,x = 255) == 2303: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,x = 8) == 11
    assert candidate(n = 5,x = 1) == 9
    assert candidate(n = 10,x = 1) == 19
    assert candidate(n = 5,x = 3) == 19
    assert candidate(n = 2,x = 7) == 15
    assert candidate(n = 1,x = 10) == 10
    assert candidate(n = 10,x = 16) == 25
    assert candidate(n = 1,x = 5) == 5
    assert candidate(n = 1,x = 32) == 32
    assert candidate(n = 3,x = 4) == 6
    assert candidate(n = 500000,x = 256) == 1000223
    assert candidate(n = 30,x = 2048) == 2077
    assert candidate(n = 500000,x = 2047) == 1023999999
    assert candidate(n = 50,x = 512) == 561
    assert candidate(n = 100,x = 128) == 227
    assert candidate(n = 8,x = 4096) == 4103
    assert candidate(n = 20,x = 8) == 43
    assert candidate(n = 100000,x = 65535) == 6553599999
    assert candidate(n = 512,x = 32768) == 33279
    assert candidate(n = 7,x = 12) == 30
    assert candidate(n = 15,x = 8) == 30
    assert candidate(n = 4,x = 3) == 15
    assert candidate(n = 20,x = 16) == 51
    assert candidate(n = 8,x = 3) == 31
    assert candidate(n = 12,x = 3) == 47
    assert candidate(n = 1,x = 1073741824) == 1073741824
    assert candidate(n = 1000,x = 512) == 2023
    assert candidate(n = 8,x = 1023) == 8191
    assert candidate(n = 100000000,x = 1073741823) == 107374182399999999
    assert candidate(n = 100,x = 16) == 211
    assert candidate(n = 30,x = 17) == 123
    assert candidate(n = 30,x = 64) == 93
    assert candidate(n = 15,x = 31) == 479
    assert candidate(n = 100,x = 255) == 25599
    assert candidate(n = 4,x = 63) == 255
    assert candidate(n = 5,x = 1023) == 5119
    assert candidate(n = 10,x = 1024) == 1033
    assert candidate(n = 8,x = 7) == 63
    assert candidate(n = 5,x = 8) == 12
    assert candidate(n = 50000,x = 31) == 1599999
    assert candidate(n = 9,x = 512) == 520
    assert candidate(n = 4,x = 15) == 63
    assert candidate(n = 6,x = 2048) == 2053
    assert candidate(n = 7,x = 10) == 30
    assert candidate(n = 15,x = 100) == 126
    assert candidate(n = 6,x = 10) == 27
    assert candidate(n = 3,x = 16) == 18
    assert candidate(n = 50,x = 2048) == 2097
    assert candidate(n = 1000,x = 4096) == 5095
    assert candidate(n = 10,x = 1048575) == 10485759
    assert candidate(n = 15,x = 1024) == 1038
    assert candidate(n = 50,x = 128) == 177
    assert candidate(n = 20,x = 2047) == 40959
    assert candidate(n = 25,x = 2048) == 2072
    assert candidate(n = 6,x = 24) == 29
    assert candidate(n = 7,x = 128) == 134
    assert candidate(n = 100,x = 1047552) == 1047651
    assert candidate(n = 15,x = 512) == 526
    assert candidate(n = 3,x = 12) == 14
    assert candidate(n = 20,x = 512) == 531
    assert candidate(n = 1,x = 1023) == 1023
    assert candidate(n = 100000,x = 1023) == 102399999
    assert candidate(n = 3,x = 31) == 95
    assert candidate(n = 5,x = 31) == 159
    assert candidate(n = 50,x = 31) == 1599
    assert candidate(n = 500,x = 512) == 1011
    assert candidate(n = 10000000,x = 4095) == 40959999999
    assert candidate(n = 64,x = 2048) == 2111
    assert candidate(n = 8,x = 32) == 39
    assert candidate(n = 3,x = 13) == 29
    assert candidate(n = 8,x = 31) == 255
    assert candidate(n = 7,x = 64) == 70
    assert candidate(n = 1,x = 1024) == 1024
    assert candidate(n = 1024,x = 65535) == 67108863
    assert candidate(n = 100,x = 4096) == 4195
    assert candidate(n = 7,x = 1024) == 1030
    assert candidate(n = 9,x = 256) == 264
    assert candidate(n = 1000,x = 2048) == 3047
    assert candidate(n = 10,x = 32) == 41
    assert candidate(n = 50,x = 255) == 12799
    assert candidate(n = 100000,x = 128) == 200095
    assert candidate(n = 100000,x = 1) == 199999
    assert candidate(n = 8,x = 255) == 2047
    assert candidate(n = 5,x = 15) == 79
    assert candidate(n = 100,x = 256) == 355
    assert candidate(n = 25,x = 128) == 152
    assert candidate(n = 6,x = 64) == 69
    assert candidate(n = 7,x = 32) == 38
    assert candidate(n = 5,x = 12) == 28
    assert candidate(n = 1,x = 2048) == 2048
    assert candidate(n = 2,x = 1073741823) == 2147483647
    assert candidate(n = 14,x = 1023) == 14335
    assert candidate(n = 50,x = 1024) == 1073
    assert candidate(n = 200,x = 8192) == 8391
    assert candidate(n = 128,x = 16383) == 2097151
    assert candidate(n = 20,x = 3) == 79
    assert candidate(n = 11,x = 512) == 522
    assert candidate(n = 10,x = 256) == 265
    assert candidate(n = 1,x = 8191) == 8191
    assert candidate(n = 1,x = 1048575) == 1048575
    assert candidate(n = 30,x = 8191) == 245759
    assert candidate(n = 4,x = 17) == 23
    assert candidate(n = 5,x = 10) == 26
    assert candidate(n = 30,x = 512) == 541
    assert candidate(n = 15,x = 7) == 119
    assert candidate(n = 9,x = 255) == 2303


