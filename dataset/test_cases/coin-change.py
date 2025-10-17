def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(coins = [186, 419, 83, 408],amount = 6249) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [186, 419, 83, 408],amount = 6249) == 20: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 7, 405, 436],amount = 8839) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 7, 405, 436],amount = 8839) == 25: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 7, 405],amount = 8839) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 7, 405],amount = 8839) == 71: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 1],amount = 27) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 1],amount = 27) == 4: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5],amount = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5],amount = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4, 5],amount = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4, 5],amount = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1],amount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1],amount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 7, 8],amount = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 7, 8],amount = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4],amount = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4],amount = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(coins = [4, 2, 1],amount = 11) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [4, 2, 1],amount = 11) == 4: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4],amount = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4],amount = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5],amount = 11) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5],amount = 11) == 3: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5],amount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5],amount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2],amount = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2],amount = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [70, 171, 358, 439, 286],amount = 9963) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [70, 171, 358, 439, 286],amount = 9963) == 27: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 7, 405, 88, 43],amount = 6803) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 7, 405, 88, 43],amount = 6803) == 24: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 7],amount = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 7],amount = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(coins = [18, 27, 41],amount = 987) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [18, 27, 41],amount = 987) == 26: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 4095) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 4095) == 12: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 15, 25, 50],amount = 3000) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 15, 25, 50],amount = 3000) == 60: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 4, 8, 16],amount = 2048) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 4, 8, 16],amount = 2048) == 128: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 20, 30, 40, 50, 60],amount = 1234) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 20, 30, 40, 50, 60],amount = 1234) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 5, 7, 9, 11],amount = 9876) == 898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 5, 7, 9, 11],amount = 9876) == 898: {e}')
    
    total += 1
    try:
        result = candidate(coins = [18, 24, 28],amount = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [18, 24, 28],amount = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(coins = [17, 29, 31, 37, 41, 43],amount = 5000) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [17, 29, 31, 37, 41, 43],amount = 5000) == 118: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 5],amount = 11) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 5],amount = 11) == 3: {e}')
    
    total += 1
    try:
        result = candidate(coins = [17, 29, 41, 53, 65],amount = 8300) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [17, 29, 41, 53, 65],amount = 8300) == 136: {e}')
    
    total += 1
    try:
        result = candidate(coins = [11, 22, 33, 44, 55],amount = 6600) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [11, 22, 33, 44, 55],amount = 6600) == 120: {e}')
    
    total += 1
    try:
        result = candidate(coins = [34, 7, 23, 32, 5, 62],amount = 9999) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [34, 7, 23, 32, 5, 62],amount = 9999) == 164: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 25, 50],amount = 9999) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 25, 50],amount = 9999) == 208: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 7, 10],amount = 500) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 7, 10],amount = 500) == 50: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 14, 21, 28, 35, 42, 49, 56],amount = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 14, 21, 28, 35, 42, 49, 56],amount = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 6, 9, 12, 15],amount = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 6, 9, 12, 15],amount = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 25, 50],amount = 78) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 25, 50],amount = 78) == 5: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 20, 30, 40, 50],amount = 9999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 20, 30, 40, 50],amount = 9999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 7, 11],amount = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 7, 11],amount = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 6, 12, 24, 48],amount = 500) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 6, 12, 24, 48],amount = 500) == 13: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 4, 8, 16, 32, 64],amount = 1023) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 4, 8, 16, 32, 64],amount = 1023) == 21: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1],amount = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1],amount = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 14, 30, 50, 80],amount = 287) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 14, 30, 50, 80],amount = 287) == 6: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 4, 8, 16, 32, 64, 128],amount = 1023) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 4, 8, 16, 32, 64, 128],amount = 1023) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 10002) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 10002) == 51: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 5, 7, 11, 13],amount = 5000) == 386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 5, 7, 11, 13],amount = 5000) == 386: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 5, 7, 9, 11],amount = 10000) == 910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 5, 7, 9, 11],amount = 10000) == 910: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7],amount = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7],amount = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 25, 50, 100],amount = 99999) == 1007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 25, 50, 100],amount = 99999) == 1007: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 3, 5, 10],amount = 5000) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 3, 5, 10],amount = 5000) == 500: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 6, 9, 12, 15],amount = 444) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 6, 9, 12, 15],amount = 444) == 30: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 5, 7, 11, 13],amount = 997) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 5, 7, 11, 13],amount = 997) == 77: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],amount = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],amount = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 15, 23, 31],amount = 750) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 15, 23, 31],amount = 750) == 26: {e}')
    
    total += 1
    try:
        result = candidate(coins = [23, 14, 5, 12],amount = 5000) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [23, 14, 5, 12],amount = 5000) == 220: {e}')
    
    total += 1
    try:
        result = candidate(coins = [11, 23, 37, 41, 43, 47, 53],amount = 12345) == 235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [11, 23, 37, 41, 43, 47, 53],amount = 12345) == 235: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 25, 50, 100],amount = 357) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 25, 50, 100],amount = 357) == 7: {e}')
    
    total += 1
    try:
        result = candidate(coins = [18, 24, 27, 36, 50],amount = 999) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [18, 24, 27, 36, 50],amount = 999) == 21: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 25, 50],amount = 9999) == 206
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 25, 50],amount = 9999) == 206: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 9999) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 9999) == 56: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 25],amount = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 25],amount = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 1048575) == 522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 1048575) == 522: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 15, 23, 42],amount = 999) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 15, 23, 42],amount = 999) == 27: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 17, 23, 29, 31],amount = 1000) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 17, 23, 29, 31],amount = 1000) == 34: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4, 6, 8, 10],amount = 450) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4, 6, 8, 10],amount = 450) == 45: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 20, 50, 100],amount = 10001) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 20, 50, 100],amount = 10001) == 101: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 7],amount = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 7],amount = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 11, 23, 37, 41, 43, 61, 71, 73, 79, 83, 89],amount = 999) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 11, 23, 37, 41, 43, 61, 71, 73, 79, 83, 89],amount = 999) == 13: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 10, 100, 1000],amount = 9999) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 10, 100, 1000],amount = 9999) == 36: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 10, 25, 50, 100],amount = 12345) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 10, 25, 50, 100],amount = 12345) == 126: {e}')
    
    total += 1
    try:
        result = candidate(coins = [186, 419, 83, 408],amount = 6249) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [186, 419, 83, 408],amount = 6249) == 20: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 7],amount = 27) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 7],amount = 27) == 5: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 6, 9, 12, 15],amount = 9000) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 6, 9, 12, 15],amount = 9000) == 600: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10, 20, 50, 100],amount = 9999) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10, 20, 50, 100],amount = 9999) == 105: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 9, 12, 27, 31],amount = 1276) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 9, 12, 27, 31],amount = 1276) == 42: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 7, 11, 19, 23],amount = 987) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 7, 11, 19, 23],amount = 987) == 44: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 25, 50, 100],amount = 9876) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 25, 50, 100],amount = 9876) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 6, 10, 14],amount = 9999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 6, 10, 14],amount = 9999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 22, 35],amount = 1000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 22, 35],amount = 1000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 11, 17, 23],amount = 1000) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 11, 17, 23],amount = 1000) == 44: {e}')
    
    total += 1
    try:
        result = candidate(coins = [23, 37, 41, 53, 67, 71],amount = 8675309) == 122189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [23, 37, 41, 53, 67, 71],amount = 8675309) == 122189: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],amount = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],amount = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 6, 10],amount = 111) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 6, 10],amount = 111) == 12: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 14, 33, 19, 100],amount = 12345) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 14, 33, 19, 100],amount = 12345) == 126: {e}')
    
    total += 1
    try:
        result = candidate(coins = [13, 21, 34, 55, 89, 144],amount = 6765) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [13, 21, 34, 55, 89, 144],amount = 6765) == 51: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10],amount = 27) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10],amount = 27) == 4: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],amount = 8000) == 277
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],amount = 8000) == 277: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 25],amount = 99) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 25],amount = 99) == 9: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 15, 20],amount = 120) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 15, 20],amount = 120) == 6: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 3, 4, 5],amount = 10000) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 3, 4, 5],amount = 10000) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 11, 21, 31],amount = 10000) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 11, 21, 31],amount = 10000) == 330: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 5, 7, 9],amount = 10000) == 1112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 5, 7, 9],amount = 10000) == 1112: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 399) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 399) == 8: {e}')
    
    total += 1
    try:
        result = candidate(coins = [13, 19, 23, 29, 31, 37, 41],amount = 9998) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [13, 19, 23, 29, 31, 37, 41],amount = 9998) == 246: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 6, 13, 37, 150],amount = 9999) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 6, 13, 37, 150],amount = 9999) == 71: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 20, 50, 100, 200],amount = 10000) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 20, 50, 100, 200],amount = 10000) == 50: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 5, 10, 25, 50],amount = 87) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 5, 10, 25, 50],amount = 87) == 5: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],amount = 10000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],amount = 10000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(coins = [100, 200, 300, 400, 500],amount = 9999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [100, 200, 300, 400, 500],amount = 9999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4, 5],amount = 150) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4, 5],amount = 150) == 30: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 20],amount = 98) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 20],amount = 98) == 9: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10, 25],amount = 9999) == 403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10, 25],amount = 9999) == 403: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 25, 50],amount = 9999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 25, 50],amount = 9999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [11, 17, 29, 31],amount = 10000) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [11, 17, 29, 31],amount = 10000) == 324: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 14, 28, 29],amount = 10000) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 14, 28, 29],amount = 10000) == 345: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 25, 50],amount = 99) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 25, 50],amount = 99) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4, 5, 7],amount = 10000) == 1429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4, 5, 7],amount = 10000) == 1429: {e}')
    
    total += 1
    try:
        result = candidate(coins = [100, 50, 20, 10, 5, 1],amount = 19876) == 202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [100, 50, 20, 10, 5, 1],amount = 19876) == 202: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 3, 4, 5],amount = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 3, 4, 5],amount = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 20, 50, 100],amount = 9999) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 20, 50, 100],amount = 9999) == 105: {e}')
    
    total += 1
    try:
        result = candidate(coins = [13, 17, 19],amount = 1234) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [13, 17, 19],amount = 1234) == 66: {e}')
    
    total += 1
    try:
        result = candidate(coins = [1, 2, 5, 10, 20, 50, 100],amount = 3689) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [1, 2, 5, 10, 20, 50, 100],amount = 3689) == 42: {e}')
    
    total += 1
    try:
        result = candidate(coins = [335, 23, 102, 75, 402],amount = 9783) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [335, 23, 102, 75, 402],amount = 9783) == 30: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 20, 50],amount = 399) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 20, 50],amount = 399) == 12: {e}')
    
    total += 1
    try:
        result = candidate(coins = [17, 29, 31, 37, 41, 43],amount = 8942) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [17, 29, 31, 37, 41, 43],amount = 8942) == 208: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 20, 50, 100],amount = 363) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 20, 50, 100],amount = 363) == 9: {e}')
    
    total += 1
    try:
        result = candidate(coins = [12, 25, 50, 100, 200],amount = 3678) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [12, 25, 50, 100, 200],amount = 3678) == 37: {e}')
    
    total += 1
    try:
        result = candidate(coins = [13, 23, 33, 43, 53],amount = 888) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [13, 23, 33, 43, 53],amount = 888) == 26: {e}')
    
    total += 1
    try:
        result = candidate(coins = [3, 6, 9, 12, 15, 18],amount = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [3, 6, 9, 12, 15, 18],amount = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [11, 17, 23],amount = 457) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [11, 17, 23],amount = 457) == 23: {e}')
    
    total += 1
    try:
        result = candidate(coins = [2, 5, 10, 25],amount = 9999) == 403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [2, 5, 10, 25],amount = 9999) == 403: {e}')
    
    total += 1
    try:
        result = candidate(coins = [29, 81, 135, 50, 1],amount = 2101) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [29, 81, 135, 50, 1],amount = 2101) == 19: {e}')
    
    total += 1
    try:
        result = candidate(coins = [33, 37, 41, 43, 47, 53, 59],amount = 10000) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [33, 37, 41, 43, 47, 53, 59],amount = 10000) == 170: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 11, 13],amount = 10000) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 11, 13],amount = 10000) == 770: {e}')
    
    total += 1
    try:
        result = candidate(coins = [10, 20, 50, 100],amount = 345) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [10, 20, 50, 100],amount = 345) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [5, 10, 20, 50, 100],amount = 4321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [5, 10, 20, 50, 100],amount = 4321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(coins = [13, 112, 197, 84, 205],amount = 4873) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [13, 112, 197, 84, 205],amount = 4873) == 26: {e}')
    
    total += 1
    try:
        result = candidate(coins = [33, 77, 111, 155],amount = 8500) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [33, 77, 111, 155],amount = 8500) == 60: {e}')
    
    total += 1
    try:
        result = candidate(coins = [7, 15, 23],amount = 1000) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(coins = [7, 15, 23],amount = 1000) == 48: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(coins = [186, 419, 83, 408],amount = 6249) == 20
    assert candidate(coins = [3, 7, 405, 436],amount = 8839) == 25
    assert candidate(coins = [3, 7, 405],amount = 8839) == 71
    assert candidate(coins = [2, 5, 10, 1],amount = 27) == 4
    assert candidate(coins = [1, 2, 5],amount = 1) == 1
    assert candidate(coins = [1, 3, 4, 5],amount = 7) == 2
    assert candidate(coins = [1],amount = 0) == 0
    assert candidate(coins = [5, 7, 8],amount = 100) == 13
    assert candidate(coins = [1, 3, 4],amount = 6) == 2
    assert candidate(coins = [4, 2, 1],amount = 11) == 4
    assert candidate(coins = [1, 3, 4],amount = 6) == 2
    assert candidate(coins = [1, 2, 5],amount = 11) == 3
    assert candidate(coins = [1, 2, 5],amount = 0) == 0
    assert candidate(coins = [2],amount = 3) == -1
    assert candidate(coins = [70, 171, 358, 439, 286],amount = 9963) == 27
    assert candidate(coins = [3, 7, 405, 88, 43],amount = 6803) == 24
    assert candidate(coins = [5, 7],amount = 15) == 3
    assert candidate(coins = [18, 27, 41],amount = 987) == 26
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 4095) == 12
    assert candidate(coins = [5, 15, 25, 50],amount = 3000) == 60
    assert candidate(coins = [1, 2, 4, 8, 16],amount = 2048) == 128
    assert candidate(coins = [10, 20, 30, 40, 50, 60],amount = 1234) == -1
    assert candidate(coins = [3, 5, 7, 9, 11],amount = 9876) == 898
    assert candidate(coins = [18, 24, 28],amount = 100) == 4
    assert candidate(coins = [17, 29, 31, 37, 41, 43],amount = 5000) == 118
    assert candidate(coins = [3, 5],amount = 11) == 3
    assert candidate(coins = [17, 29, 41, 53, 65],amount = 8300) == 136
    assert candidate(coins = [11, 22, 33, 44, 55],amount = 6600) == 120
    assert candidate(coins = [34, 7, 23, 32, 5, 62],amount = 9999) == 164
    assert candidate(coins = [1, 5, 25, 50],amount = 9999) == 208
    assert candidate(coins = [2, 3, 7, 10],amount = 500) == 50
    assert candidate(coins = [7, 14, 21, 28, 35, 42, 49, 56],amount = 1000) == -1
    assert candidate(coins = [3, 6, 9, 12, 15],amount = 1000) == -1
    assert candidate(coins = [1, 5, 10, 25, 50],amount = 78) == 5
    assert candidate(coins = [10, 20, 30, 40, 50],amount = 9999) == -1
    assert candidate(coins = [1, 7, 11],amount = 100) == 10
    assert candidate(coins = [2, 3, 6, 12, 24, 48],amount = 500) == 13
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64],amount = 1023) == 21
    assert candidate(coins = [1],amount = 10000) == 10000
    assert candidate(coins = [7, 14, 30, 50, 80],amount = 287) == 6
    assert candidate(coins = [2, 4, 8, 16, 32, 64, 128],amount = 1023) == -1
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 10002) == 51
    assert candidate(coins = [2, 3, 5, 7, 11, 13],amount = 5000) == 386
    assert candidate(coins = [3, 5, 7, 9, 11],amount = 10000) == 910
    assert candidate(coins = [7],amount = 100) == -1
    assert candidate(coins = [1, 5, 10, 25, 50, 100],amount = 99999) == 1007
    assert candidate(coins = [1, 2, 3, 5, 10],amount = 5000) == 500
    assert candidate(coins = [3, 6, 9, 12, 15],amount = 444) == 30
    assert candidate(coins = [3, 5, 7, 11, 13],amount = 997) == 77
    assert candidate(coins = [1, 3, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],amount = 100) == 4
    assert candidate(coins = [7, 15, 23, 31],amount = 750) == 26
    assert candidate(coins = [23, 14, 5, 12],amount = 5000) == 220
    assert candidate(coins = [11, 23, 37, 41, 43, 47, 53],amount = 12345) == 235
    assert candidate(coins = [1, 5, 10, 25, 50, 100],amount = 357) == 7
    assert candidate(coins = [18, 24, 27, 36, 50],amount = 999) == 21
    assert candidate(coins = [1, 5, 10, 25, 50],amount = 9999) == 206
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 9999) == 56
    assert candidate(coins = [2, 5, 10, 25],amount = 100) == 4
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 1048575) == 522
    assert candidate(coins = [7, 15, 23, 42],amount = 999) == 27
    assert candidate(coins = [7, 17, 23, 29, 31],amount = 1000) == 34
    assert candidate(coins = [1, 3, 4, 6, 8, 10],amount = 450) == 45
    assert candidate(coins = [1, 5, 10, 20, 50, 100],amount = 10001) == 101
    assert candidate(coins = [2, 3, 7],amount = 100) == 15
    assert candidate(coins = [5, 11, 23, 37, 41, 43, 61, 71, 73, 79, 83, 89],amount = 999) == 13
    assert candidate(coins = [1, 10, 100, 1000],amount = 9999) == 36
    assert candidate(coins = [1, 10, 25, 50, 100],amount = 12345) == 126
    assert candidate(coins = [186, 419, 83, 408],amount = 6249) == 20
    assert candidate(coins = [2, 3, 7],amount = 27) == 5
    assert candidate(coins = [3, 6, 9, 12, 15],amount = 9000) == 600
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100],amount = 9999) == 105
    assert candidate(coins = [5, 9, 12, 27, 31],amount = 1276) == 42
    assert candidate(coins = [2, 3, 7, 11, 19, 23],amount = 987) == 44
    assert candidate(coins = [10, 25, 50, 100],amount = 9876) == -1
    assert candidate(coins = [2, 6, 10, 14],amount = 9999) == -1
    assert candidate(coins = [10, 22, 35],amount = 1000) == 30
    assert candidate(coins = [2, 5, 11, 17, 23],amount = 1000) == 44
    assert candidate(coins = [23, 37, 41, 53, 67, 71],amount = 8675309) == 122189
    assert candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],amount = 12) == 12
    assert candidate(coins = [1, 6, 10],amount = 111) == 12
    assert candidate(coins = [7, 14, 33, 19, 100],amount = 12345) == 126
    assert candidate(coins = [13, 21, 34, 55, 89, 144],amount = 6765) == 51
    assert candidate(coins = [1, 2, 5, 10],amount = 27) == 4
    assert candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],amount = 8000) == 277
    assert candidate(coins = [1, 5, 10, 25],amount = 99) == 9
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],amount = 1023) == 10
    assert candidate(coins = [10, 15, 20],amount = 120) == 6
    assert candidate(coins = [1, 2, 3, 4, 5],amount = 10000) == 2000
    assert candidate(coins = [1, 11, 21, 31],amount = 10000) == 330
    assert candidate(coins = [1, 3, 5, 7, 9],amount = 10000) == 1112
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200],amount = 399) == 8
    assert candidate(coins = [13, 19, 23, 29, 31, 37, 41],amount = 9998) == 246
    assert candidate(coins = [1, 6, 13, 37, 150],amount = 9999) == 71
    assert candidate(coins = [10, 20, 50, 100, 200],amount = 10000) == 50
    assert candidate(coins = [1, 5, 10, 25, 50],amount = 87) == 5
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],amount = 10000) == 1000
    assert candidate(coins = [100, 200, 300, 400, 500],amount = 9999) == -1
    assert candidate(coins = [1, 3, 4, 5],amount = 150) == 30
    assert candidate(coins = [2, 5, 10, 20],amount = 98) == 9
    assert candidate(coins = [1, 2, 5, 10, 25],amount = 9999) == 403
    assert candidate(coins = [10, 25, 50],amount = 9999) == -1
    assert candidate(coins = [11, 17, 29, 31],amount = 10000) == 324
    assert candidate(coins = [7, 14, 28, 29],amount = 10000) == 345
    assert candidate(coins = [10, 25, 50],amount = 99) == -1
    assert candidate(coins = [1, 3, 4, 5, 7],amount = 10000) == 1429
    assert candidate(coins = [100, 50, 20, 10, 5, 1],amount = 19876) == 202
    assert candidate(coins = [1, 3, 4, 5],amount = 15) == 3
    assert candidate(coins = [2, 5, 10, 20, 50, 100],amount = 9999) == 105
    assert candidate(coins = [13, 17, 19],amount = 1234) == 66
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100],amount = 3689) == 42
    assert candidate(coins = [335, 23, 102, 75, 402],amount = 9783) == 30
    assert candidate(coins = [2, 5, 10, 20, 50],amount = 399) == 12
    assert candidate(coins = [17, 29, 31, 37, 41, 43],amount = 8942) == 208
    assert candidate(coins = [2, 5, 10, 20, 50, 100],amount = 363) == 9
    assert candidate(coins = [12, 25, 50, 100, 200],amount = 3678) == 37
    assert candidate(coins = [13, 23, 33, 43, 53],amount = 888) == 26
    assert candidate(coins = [3, 6, 9, 12, 15, 18],amount = 100) == -1
    assert candidate(coins = [11, 17, 23],amount = 457) == 23
    assert candidate(coins = [2, 5, 10, 25],amount = 9999) == 403
    assert candidate(coins = [29, 81, 135, 50, 1],amount = 2101) == 19
    assert candidate(coins = [33, 37, 41, 43, 47, 53, 59],amount = 10000) == 170
    assert candidate(coins = [5, 11, 13],amount = 10000) == 770
    assert candidate(coins = [10, 20, 50, 100],amount = 345) == -1
    assert candidate(coins = [5, 10, 20, 50, 100],amount = 4321) == -1
    assert candidate(coins = [13, 112, 197, 84, 205],amount = 4873) == 26
    assert candidate(coins = [33, 77, 111, 155],amount = 8500) == 60
    assert candidate(coins = [7, 15, 23],amount = 1000) == 48


