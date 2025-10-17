def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(dividend = 10,divisor = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 10,divisor = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = 2) == -1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = 2) == -1073741824: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = -1) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = -1) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 2147483647,divisor = 1) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 2147483647,divisor = 1) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = 3) == 333333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = 3) == 333333333: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 7,divisor = -3) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 7,divisor = -3) == -2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = 1) == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = 1) == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -5,divisor = 2) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -5,divisor = 2) == -2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = -1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = -1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 2147483647,divisor = 2) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 2147483647,divisor = 2) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 0,divisor = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 0,divisor = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -7,divisor = 3) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -7,divisor = 3) == -2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = 1000000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = 1000000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = -2147483648) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = -2147483648) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = -5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = -5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = 500000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = 500000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 2147483647,divisor = -1) == -2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 2147483647,divisor = -1) == -2147483647: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 123456789,divisor = 987654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 123456789,divisor = 987654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = 999999998) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = 999999998) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = -6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = -6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1024,divisor = -2) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1024,divisor = -2) == 512: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = 3) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = 3) == -5: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -5,divisor = -2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -5,divisor = -2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1024,divisor = 10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1024,divisor = 10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = -1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = -1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = -987654321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = -987654321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1500000000,divisor = -4) == 375000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1500000000,divisor = -4) == 375000000: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1023,divisor = 10) == -102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1023,divisor = 10) == -102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = 3) == -333333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = 3) == -333333333: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = -5) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = -5) == -3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = -3) == 333333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = -3) == 333333333: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1023,divisor = 10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1023,divisor = 10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -10,divisor = 1) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -10,divisor = 1) == -10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = 123456789) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = 123456789) == 8: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1024,divisor = 1024) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1024,divisor = 1024) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = 2147483648) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = 2147483648) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = 5) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = 5) == -3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = 987654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = 987654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1024,divisor = -10) == -102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1024,divisor = -10) == -102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = -4) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = -4) == -3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = -6) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = -6) == -2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 5,divisor = -2) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 5,divisor = -2) == -2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = 4) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = 4) == -3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = -4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = -4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = -3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = -3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -123456789,divisor = 987654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -123456789,divisor = 987654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = -7) == -14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = -7) == -14: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 999999999,divisor = 1) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 999999999,divisor = 1) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1024,divisor = -10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1024,divisor = -10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 10,divisor = -1) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 10,divisor = -1) == -10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = 25) == 40000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = 25) == 40000000: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 123456789,divisor = -987654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 123456789,divisor = -987654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1500000000,divisor = 3) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1500000000,divisor = 3) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = 3) == -715827882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = 3) == -715827882: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1024,divisor = 10) == -102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1024,divisor = 10) == -102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = 999999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = 999999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = 7) == -14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = 7) == -14: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1024,divisor = 2) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1024,divisor = 2) == 512: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1024,divisor = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1024,divisor = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1025,divisor = 3) == 341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1025,divisor = 3) == 341: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -123456789,divisor = -987654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -123456789,divisor = -987654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1025,divisor = -3) == 341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1025,divisor = -3) == 341: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = 999999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = 999999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = -1000000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = -1000000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = -25) == 40000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = -25) == 40000000: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 2147483647,divisor = -2147483648) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 2147483647,divisor = -2147483648) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 150,divisor = 3) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 150,divisor = 3) == 50: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1023,divisor = -10) == -102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1023,divisor = -10) == -102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = 25) == -40000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = 25) == -40000000: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1023,divisor = -2) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1023,divisor = -2) == 511: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = 999999998) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = 999999998) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -999999999,divisor = 999999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -999999999,divisor = 999999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = -25) == -40000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = -25) == -40000000: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1023,divisor = -10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1023,divisor = -10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = -2147483648) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = -2147483648) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 2147483647,divisor = 2147483647) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 2147483647,divisor = 2147483647) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = -1) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = -1) == -100: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 2147483647,divisor = 3) == 715827882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 2147483647,divisor = 3) == 715827882: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = -3) == 715827882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = -3) == 715827882: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 999999999,divisor = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 999999999,divisor = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = -3) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = -3) == -5: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483648,divisor = 2147483647) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483648,divisor = 2147483647) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000000000,divisor = -3) == -333333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000000000,divisor = -3) == -333333333: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000000000,divisor = -500000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000000000,divisor = -500000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -15,divisor = 6) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -15,divisor = 6) == -2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -999999999,divisor = 1) == -999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -999999999,divisor = 1) == -999999999: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1023,divisor = 2) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1023,divisor = 2) == 511: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = -7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = -7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 5,divisor = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 5,divisor = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 10,divisor = -3) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 10,divisor = -3) == -3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -50,divisor = -10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -50,divisor = -10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000,divisor = 5) == -200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000,divisor = 5) == -200: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1000,divisor = -5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1000,divisor = -5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = -2) == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = -2) == -50: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 56,divisor = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 56,divisor = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -50,divisor = 10) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -50,divisor = 10) == -5: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -50,divisor = 5) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -50,divisor = 5) == -10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 15,divisor = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 15,divisor = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -1,divisor = -2147483648) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -1,divisor = -2147483648) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -10,divisor = 3) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -10,divisor = 3) == -3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = 33) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = 33) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 150,divisor = 6) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 150,divisor = 6) == 25: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1,divisor = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1,divisor = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = -5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = -5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -7,divisor = -3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -7,divisor = -3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = 10) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = 10) == -10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = -10) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = -10) == -10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -2147483647,divisor = 2) == -1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -2147483647,divisor = 2) == -1073741823: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -56,divisor = -7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -56,divisor = -7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = 2) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = 2) == 50: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = -2) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = -2) == 50: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = -5) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = -5) == -20: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 100,divisor = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 100,divisor = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 0,divisor = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 0,divisor = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = -10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = -10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = 2) == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = 2) == -50: {e}')
    
    total += 1
    try:
        result = candidate(dividend = -100,divisor = 5) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = -100,divisor = 5) == -20: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 0,divisor = -1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 0,divisor = -1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000,divisor = 5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000,divisor = 5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000,divisor = -5) == -200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000,divisor = -5) == -200: {e}')
    
    total += 1
    try:
        result = candidate(dividend = 1000,divisor = 3) == 333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dividend = 1000,divisor = 3) == 333: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(dividend = 10,divisor = 3) == 3
    assert candidate(dividend = -2147483648,divisor = 2) == -1073741824
    assert candidate(dividend = -2147483648,divisor = -1) == 2147483647
    assert candidate(dividend = -1,divisor = -1) == 1
    assert candidate(dividend = 2147483647,divisor = 1) == 2147483647
    assert candidate(dividend = 1,divisor = 1) == 1
    assert candidate(dividend = 1000000000,divisor = 3) == 333333333
    assert candidate(dividend = 7,divisor = -3) == -2
    assert candidate(dividend = -2147483648,divisor = 1) == -2147483648
    assert candidate(dividend = 100,divisor = 7) == 14
    assert candidate(dividend = -5,divisor = 2) == -2
    assert candidate(dividend = 1,divisor = -1) == -1
    assert candidate(dividend = 2147483647,divisor = 2) == 1073741823
    assert candidate(dividend = 0,divisor = 1) == 0
    assert candidate(dividend = 1,divisor = 2) == 0
    assert candidate(dividend = -1,divisor = 1) == -1
    assert candidate(dividend = -7,divisor = 3) == -2
    assert candidate(dividend = -1000000000,divisor = 1000000000) == -1
    assert candidate(dividend = 15,divisor = 6) == 2
    assert candidate(dividend = 1,divisor = -2147483648) == 0
    assert candidate(dividend = -15,divisor = -5) == 3
    assert candidate(dividend = 1000000000,divisor = 500000000) == 2
    assert candidate(dividend = 2147483647,divisor = -1) == -2147483647
    assert candidate(dividend = 123456789,divisor = 987654321) == 0
    assert candidate(dividend = 1,divisor = 999999998) == 0
    assert candidate(dividend = -15,divisor = -6) == 2
    assert candidate(dividend = -1024,divisor = -2) == 512
    assert candidate(dividend = -15,divisor = 3) == -5
    assert candidate(dividend = -5,divisor = -2) == 2
    assert candidate(dividend = 1024,divisor = 10) == 102
    assert candidate(dividend = -1000000000,divisor = -1000000000) == 1
    assert candidate(dividend = -1000000000,divisor = -987654321) == 1
    assert candidate(dividend = -1500000000,divisor = -4) == 375000000
    assert candidate(dividend = -1023,divisor = 10) == -102
    assert candidate(dividend = -1000000000,divisor = 3) == -333333333
    assert candidate(dividend = 15,divisor = -5) == -3
    assert candidate(dividend = -1000000000,divisor = -3) == 333333333
    assert candidate(dividend = 1023,divisor = 10) == 102
    assert candidate(dividend = -10,divisor = 1) == -10
    assert candidate(dividend = 1000000000,divisor = 123456789) == 8
    assert candidate(dividend = -1024,divisor = 1024) == -1
    assert candidate(dividend = -1,divisor = 2147483648) == 0
    assert candidate(dividend = -15,divisor = 5) == -3
    assert candidate(dividend = -1000000000,divisor = 987654321) == -1
    assert candidate(dividend = 1024,divisor = -10) == -102
    assert candidate(dividend = 15,divisor = -4) == -3
    assert candidate(dividend = 15,divisor = -6) == -2
    assert candidate(dividend = 5,divisor = -2) == -2
    assert candidate(dividend = -15,divisor = 4) == -3
    assert candidate(dividend = -15,divisor = -4) == 3
    assert candidate(dividend = -15,divisor = -3) == 5
    assert candidate(dividend = -123456789,divisor = 987654321) == 0
    assert candidate(dividend = 100,divisor = -7) == -14
    assert candidate(dividend = 999999999,divisor = 1) == 999999999
    assert candidate(dividend = -1024,divisor = -10) == 102
    assert candidate(dividend = 10,divisor = -1) == -10
    assert candidate(dividend = 1000000000,divisor = 25) == 40000000
    assert candidate(dividend = 123456789,divisor = -987654321) == 0
    assert candidate(dividend = 1500000000,divisor = 3) == 500000000
    assert candidate(dividend = 15,divisor = 4) == 3
    assert candidate(dividend = -2147483648,divisor = 3) == -715827882
    assert candidate(dividend = -1024,divisor = 10) == -102
    assert candidate(dividend = 1,divisor = 999999999) == 0
    assert candidate(dividend = -100,divisor = 7) == -14
    assert candidate(dividend = 1024,divisor = 2) == 512
    assert candidate(dividend = 1024,divisor = 1024) == 1
    assert candidate(dividend = 15,divisor = 5) == 3
    assert candidate(dividend = 1025,divisor = 3) == 341
    assert candidate(dividend = -123456789,divisor = -987654321) == 0
    assert candidate(dividend = -1025,divisor = -3) == 341
    assert candidate(dividend = -1,divisor = 999999999) == 0
    assert candidate(dividend = 1000000000,divisor = -1000000000) == -1
    assert candidate(dividend = -1000000000,divisor = -25) == 40000000
    assert candidate(dividend = 2147483647,divisor = -2147483648) == 0
    assert candidate(dividend = 150,divisor = 3) == 50
    assert candidate(dividend = 100,divisor = 1) == 100
    assert candidate(dividend = 1023,divisor = -10) == -102
    assert candidate(dividend = -1000000000,divisor = 25) == -40000000
    assert candidate(dividend = -1023,divisor = -2) == 511
    assert candidate(dividend = -1,divisor = 999999998) == 0
    assert candidate(dividend = -999999999,divisor = 999999999) == -1
    assert candidate(dividend = -1,divisor = 2147483647) == 0
    assert candidate(dividend = 15,divisor = 3) == 5
    assert candidate(dividend = 1000000000,divisor = 1000000000) == 1
    assert candidate(dividend = 1000000000,divisor = -25) == -40000000
    assert candidate(dividend = -1023,divisor = -10) == 102
    assert candidate(dividend = -2147483648,divisor = -2147483648) == 1
    assert candidate(dividend = 2147483647,divisor = 2147483647) == 1
    assert candidate(dividend = 100,divisor = -1) == -100
    assert candidate(dividend = 2147483647,divisor = 3) == 715827882
    assert candidate(dividend = -2147483648,divisor = -3) == 715827882
    assert candidate(dividend = 999999999,divisor = 999999999) == 1
    assert candidate(dividend = 15,divisor = -3) == -5
    assert candidate(dividend = -2147483648,divisor = 2147483647) == -1
    assert candidate(dividend = 1000000000,divisor = -3) == -333333333
    assert candidate(dividend = -1000000000,divisor = -500000000) == 2
    assert candidate(dividend = 1,divisor = 100) == 0
    assert candidate(dividend = -15,divisor = 6) == -2
    assert candidate(dividend = -999999999,divisor = 1) == -999999999
    assert candidate(dividend = 1023,divisor = 2) == 511
    assert candidate(dividend = -100,divisor = -7) == 14
    assert candidate(dividend = 5,divisor = 2) == 2
    assert candidate(dividend = 10,divisor = -3) == -3
    assert candidate(dividend = -50,divisor = -10) == 5
    assert candidate(dividend = 100,divisor = 10) == 10
    assert candidate(dividend = -1000,divisor = 5) == -200
    assert candidate(dividend = -1000,divisor = -5) == 200
    assert candidate(dividend = 100,divisor = -2) == -50
    assert candidate(dividend = 56,divisor = 7) == 8
    assert candidate(dividend = -50,divisor = 10) == -5
    assert candidate(dividend = -50,divisor = 5) == -10
    assert candidate(dividend = 15,divisor = 2) == 7
    assert candidate(dividend = -1,divisor = -2147483648) == 0
    assert candidate(dividend = -10,divisor = 3) == -3
    assert candidate(dividend = 100,divisor = 33) == 3
    assert candidate(dividend = 150,divisor = 6) == 25
    assert candidate(dividend = 1,divisor = 2147483647) == 0
    assert candidate(dividend = -100,divisor = -5) == 20
    assert candidate(dividend = -7,divisor = -3) == 2
    assert candidate(dividend = -100,divisor = 10) == -10
    assert candidate(dividend = 100,divisor = -10) == -10
    assert candidate(dividend = -2147483647,divisor = 2) == -1073741823
    assert candidate(dividend = -56,divisor = -7) == 8
    assert candidate(dividend = 100,divisor = 2) == 50
    assert candidate(dividend = -100,divisor = -2) == 50
    assert candidate(dividend = 100,divisor = -5) == -20
    assert candidate(dividend = 100,divisor = 5) == 20
    assert candidate(dividend = 0,divisor = 5) == 0
    assert candidate(dividend = -100,divisor = -10) == 10
    assert candidate(dividend = -100,divisor = 2) == -50
    assert candidate(dividend = -100,divisor = 5) == -20
    assert candidate(dividend = 0,divisor = -1) == 0
    assert candidate(dividend = 1000,divisor = 5) == 200
    assert candidate(dividend = 1000,divisor = -5) == -200
    assert candidate(dividend = 1000,divisor = 3) == 333


