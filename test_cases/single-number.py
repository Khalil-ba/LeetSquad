def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -1, -2, 2]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -1, -2, 2]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 7, 7, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 7, 7, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 5, 7, 5, 7, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 5, 7, 5, 7, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 50000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 50000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 5, 7, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 5, 7, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 2, 2, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 2, 2, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, -2147483648, 2147483647, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, -2147483648, 2147483647, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, -100000]) == -100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, -100000]) == -100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000]) == -100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000]) == -100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 99]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 99]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8]) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8]) == -8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 123, 456, 456, 789, 789, 101, 101, 202, 202, 303, 303, 404]) == 404
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 123, 456, 456, 789, 789, 101, 101, 202, 202, 303, 303, 404]) == 404: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 30, 50, 50]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 30, 50, 50]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 12345, 67890, 67890, 24680, 55555, 24680, 77777, 77777, 99999, 99999]) == 55555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 12345, 67890, 67890, 24680, 55555, 24680, 77777, 77777, 99999, 99999]) == 55555: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 123456, 789012, 789012, 345678, 345678, 901234]) == 901234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 123456, 789012, 789012, 345678, 345678, 901234]) == 901234: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, 10000, -10000, 20000, 20000, 30000, 30000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, 10000, -10000, 20000, 20000, 30000, 30000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 200000, 200000, 300000, 300000, 400000]) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 200000, 200000, 300000, 300000, 400000]) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 20000, -20000, 20000, -20000, 30000]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 20000, -20000, 20000, -20000, 30000]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 500, -1000, 500, 10000, 9999, 10000, 9999, 8888]) == 8888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 500, -1000, 500, 10000, 9999, 10000, 9999, 8888]) == 8888: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 1000, 3000, 4000, 3000, 5000, 6000, 5000, 7000, 8000, 6000, 7000, 8000, 9000]) == 11096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 1000, 3000, 4000, 3000, 5000, 6000, 5000, 7000, 8000, 6000, 7000, 8000, 9000]) == 11096: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1100]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1100]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 5, 7, 9, 10, 11, 11, 10, 12, 12, 13, 13, 14, 14, 15, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 5, 7, 9, 10, 11, 11, 10, 12, 12, 13, 13, 14, 14, 15, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5, 100000]) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5, 100000]) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99999, 88888, 88888, 77777, 77777]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99999, 88888, 88888, 77777, 77777]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, -50000, -50000, 23456, 23456, 78901]) == 78901
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, -50000, -50000, 23456, 23456, 78901]) == 78901: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 5000, 5000, 7, 7, 3, 3, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 5000, 5000, 7, 7, 3, 3, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, -1000, 2000, 2000, 3000, 3000, 4000]) == 3144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, -1000, 2000, 2000, 3000, 3000, 4000]) == 3144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -100, -50, -50, 1, 1, 2, 2, 3, 3, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -100, -50, -50, 1, 1, 2, 2, 3, 3, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7]) == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7]) == -7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 888, 888, 777, 777, 666, 666, 555, 555, 444, 444, 333, 333, 222, 222, 111, 111, 101]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 888, 888, 777, 777, 666, 666, 555, 555, 444, 444, 333, 333, 222, 222, 111, 111, 101]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 10000, 10000, 10001]) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 10000, 10000, 10001]) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987, 98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098, 987, 876, 765, 654, 543, 432, 321, 210, 109, 98, 87, 76, 65, 54, 43, 32, 21, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987, 98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098, 987, 876, 765, 654, 543, 432, 321, 210, 109, 98, 87, 76, 65, 54, 43, 32, 21, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1898: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, -9999, 8888, -8888, 7777, -7777, 6666, -6666, 5555]) == 5567
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, -9999, 8888, -8888, 7777, -7777, 6666, -6666, 5555]) == 5567: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 7, 7, 5, 5, 2, 2, 8, 8, 4, 4, 6, 6, 9, 9, 1, 1, 11, 11, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 7, 7, 5, 5, 2, 2, 8, 8, 4, 4, 6, 6, 9, 9, 1, 1, 11, 11, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -10000, -9999, -9999, -9998, -9998, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -10000, -9999, -9999, -9998, -9998, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -10000, 0, 0, 5000, 5000, 7000, 8000, 8000]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -10000, 0, 0, 5000, 5000, 7000, 8000, 8000]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, -12345, 12345, -12345, 6789]) == 6789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, -12345, 12345, -12345, 6789]) == 6789: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-30000, -30000, -20000, -20000, -10000, -10000, 0, 0, 10000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-30000, -30000, -20000, -20000, -10000, -10000, 0, 0, 10000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, 200000, -200000, 200000, 300000, -300000, 300000, 400000]) == -768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, 200000, -200000, 200000, 300000, -300000, 300000, 400000]) == -768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 123, 456, 789, 101112, -101112, -101112, 131415, 131415]) == 101112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 123, 456, 789, 101112, -101112, -101112, 131415, 131415]) == 101112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23456, 23456, 78901, 22222, 22222, 11111, 11111, 33333, 33333, 44444, 44444, 55555, 55555, 66666, 66666, 77777]) == 7140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23456, 23456, 78901, 22222, 22222, 11111, 11111, 33333, 33333, 44444, 44444, 55555, 55555, 66666, 66666, 77777]) == 7140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 200000, 300000, 200000, 300000, 400000]) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 200000, 300000, 200000, 300000, 400000]) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 30, 40, 50, 40, 50, 60, 70, 60, 70]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 30, 40, 50, 40, 50, 60, 70, 60, 70]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 2, 2, 30, 30]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 2, 2, 30, 30]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, -12345, 6789, -6789, 11111]) == 11111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, -12345, 6789, -6789, 11111]) == 11111: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 1234, 5678, 5678, 91011, 91011, 121314]) == 121314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 1234, 5678, 5678, 91011, 91011, 121314]) == 121314: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100, 110]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100, 110]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 9999]) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 9999]) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 100000, 200000]) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 100000, 200000]) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 20000, 20000, 3000, 3000, 40]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 20000, 20000, 3000, 3000, 40]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 7, 5, 3, 9, 3, 8, 8, 6, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 7, 5, 3, 9, 3, 8, 8, 6, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-30000, -30000, -29999, -29999, -29998, -29998, 0, 0, 1, 1, 2, 2, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-30000, -30000, -29999, -29999, -29998, -29998, 0, 0, 1, 1, 2, 2, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 10000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 10000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 100, 200, 300, 400]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 100, 200, 300, 400]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 30, 30, 40]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 30, 30, 40]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 5, 7, 8, 8, 9, 10, 9, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 5, 7, 8, 8, 9, 10, 9, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -1000, -2000, -2000, -3000, -3000, -4000, -4000, -5000, -5000, -6000]) == -6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -1000, -2000, -2000, -3000, -3000, -4000, -4000, -5000, -5000, -6000]) == -6000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 1000, 4000, 2000, 5000, 3000, 4000]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 1000, 4000, 2000, 5000, 3000, 4000]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0, 0, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0, 0, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 98765, 87654, 87654, 76543, 76543, 65432, 65432, 54321, 54321, 12345]) == 12345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 98765, 87654, 87654, 76543, 76543, 65432, 65432, 54321, 54321, 12345]) == 12345: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9]) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9]) == -9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 12345, 67890, 67890, -1, -1, -2, -2, -3, -3, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 12345, 67890, 67890, -1, -1, -2, -2, -3, -3, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -100, -300, -200, -400, -300]) == -400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -100, -300, -200, -400, -300]) == -400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 12345, 67890, -11111, -22222, -11111, -33333, -22222, -33333, 44444]) == 44444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 12345, 67890, -11111, -22222, -11111, -33333, -22222, -33333, 44444]) == 44444: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1, 2, -1, -2, 2]) == -2
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [10, 1, 10, 2, 2]) == 1
    assert candidate(nums = [3, 3, 7, 7, 10]) == 10
    assert candidate(nums = [10, 10, 20, 20, 30]) == 30
    assert candidate(nums = [3, 3, 5, 7, 5, 7, 9]) == 9
    assert candidate(nums = [-1, -1, -2]) == -2
    assert candidate(nums = [100000, 100000, 50000]) == 50000
    assert candidate(nums = [5, 7, 5, 7, 9]) == 9
    assert candidate(nums = [3, 3, 2, 2, 5]) == 5
    assert candidate(nums = [2147483647, -2147483648, -2147483648, 2147483647, 0]) == 0
    assert candidate(nums = [0, 1, 0, 1, 2]) == 2
    assert candidate(nums = [100000, 100000, -100000]) == -100000
    assert candidate(nums = [100000, -100000, 100000]) == -100000
    assert candidate(nums = [0, 1, 0, 1, 99]) == 99
    assert candidate(nums = [2, 2, 1]) == 1
    assert candidate(nums = [4, 1, 2, 1, 2]) == 4
    assert candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600]) == 600
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 21
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8]) == -8
    assert candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]) == 14
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 100]) == 100
    assert candidate(nums = [123, 123, 456, 456, 789, 789, 101, 101, 202, 202, 303, 303, 404]) == 404
    assert candidate(nums = [10, 20, 10, 30, 30, 50, 50]) == 20
    assert candidate(nums = [12345, 12345, 67890, 67890, 24680, 55555, 24680, 77777, 77777, 99999, 99999]) == 55555
    assert candidate(nums = [123456, 123456, 789012, 789012, 345678, 345678, 901234]) == 901234
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [-10000, 10000, -10000, 20000, 20000, 30000, 30000]) == 10000
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 0
    assert candidate(nums = [100000, 100000, 200000, 200000, 300000, 300000, 400000]) == 400000
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16]) == 17
    assert candidate(nums = [10000, -10000, 10000, -10000, 20000, -20000, 20000, -20000, 30000]) == 30000
    assert candidate(nums = [-1000, 500, -1000, 500, 10000, 9999, 10000, 9999, 8888]) == 8888
    assert candidate(nums = [1000, 2000, 1000, 3000, 4000, 3000, 5000, 6000, 5000, 7000, 8000, 6000, 7000, 8000, 9000]) == 11096
    assert candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1100]) == 1100
    assert candidate(nums = [5, 7, 5, 7, 9, 10, 11, 11, 10, 12, 12, 13, 13, 14, 14, 15, 15]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21]) == 21
    assert candidate(nums = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5, 100000]) == 100000
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 20
    assert candidate(nums = [99999, 99999, 88888, 88888, 77777, 77777]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [100000, 100000, -50000, -50000, 23456, 23456, 78901]) == 78901
    assert candidate(nums = [10000, 10000, 5000, 5000, 7, 7, 3, 3, 2]) == 2
    assert candidate(nums = [-1000, 1000, -1000, 2000, 2000, 3000, 3000, 4000]) == 3144
    assert candidate(nums = [-100, -100, -50, -50, 1, 1, 2, 2, 3, 3, 4]) == 4
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7]) == -7
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13]) == 13
    assert candidate(nums = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]) == 11
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [999, 999, 888, 888, 777, 777, 666, 666, 555, 555, 444, 444, 333, 333, 222, 222, 111, 111, 101]) == 101
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 15
    assert candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 10000, 10000, 10001]) == 10001
    assert candidate(nums = [98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987, 98765, 87654, 76543, 65432, 54321, 43210, 32109, 21098, 10987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098, 987, 876, 765, 654, 543, 432, 321, 210, 109, 98, 87, 76, 65, 54, 43, 32, 21, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1898
    assert candidate(nums = [9999, -9999, 8888, -8888, 7777, -7777, 6666, -6666, 5555]) == 5567
    assert candidate(nums = [0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7
    assert candidate(nums = [3, 3, 7, 7, 5, 5, 2, 2, 8, 8, 4, 4, 6, 6, 9, 9, 1, 1, 11, 11, 10]) == 10
    assert candidate(nums = [-10000, -10000, -9999, -9999, -9998, -9998, 0]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1
    assert candidate(nums = [-10000, -10000, 0, 0, 5000, 5000, 7000, 8000, 8000]) == 7000
    assert candidate(nums = [12345, -12345, 12345, -12345, 6789]) == 6789
    assert candidate(nums = [-30000, -30000, -20000, -20000, -10000, -10000, 0, 0, 10000]) == 10000
    assert candidate(nums = [100000, -100000, 100000, 200000, -200000, 200000, 300000, -300000, 300000, 400000]) == -768
    assert candidate(nums = [123, 456, 789, 123, 456, 789, 101112, -101112, -101112, 131415, 131415]) == 101112
    assert candidate(nums = [23456, 23456, 78901, 22222, 22222, 11111, 11111, 33333, 33333, 44444, 44444, 55555, 55555, 66666, 66666, 77777]) == 7140
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10]) == -10
    assert candidate(nums = [100000, 100000, 200000, 300000, 200000, 300000, 400000]) == 400000
    assert candidate(nums = [10, 20, 10, 20, 30, 40, 50, 40, 50, 60, 70, 60, 70]) == 30
    assert candidate(nums = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 8
    assert candidate(nums = [100000, 100000, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60]) == 60
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert candidate(nums = [100000, -100000, 100000, -100000, 1]) == 1
    assert candidate(nums = [10, 20, 10, 2, 2, 30, 30]) == 20
    assert candidate(nums = [12345, -12345, 6789, -6789, 11111]) == 11111
    assert candidate(nums = [1234, 1234, 5678, 5678, 91011, 91011, 121314]) == 121314
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400]) == 500
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5]) == -5
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100, 110]) == 110
    assert candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 9999]) == 9999
    assert candidate(nums = [100000, 200000, 300000, 100000, 200000]) == 300000
    assert candidate(nums = [100000, 100000, 20000, 20000, 3000, 3000, 40]) == 40
    assert candidate(nums = [5, 7, 7, 5, 3, 9, 3, 8, 8, 6, 6]) == 9
    assert candidate(nums = [-30000, -30000, -29999, -29999, -29998, -29998, 0, 0, 1, 1, 2, 2, 3, 3]) == 0
    assert candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10, 11]) == 11
    assert candidate(nums = [1000, 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, 5000, 6000, 6000, 7000, 7000, 8000, 8000, 9000, 9000, 10000]) == 10000
    assert candidate(nums = [100, 200, 300, 100, 200, 300, 400]) == 400
    assert candidate(nums = [10, 20, 10, 20, 30, 30, 40]) == 40
    assert candidate(nums = [5, 7, 5, 7, 8, 8, 9, 10, 9, 10, 11]) == 11
    assert candidate(nums = [-1000, -1000, -2000, -2000, -3000, -3000, -4000, -4000, -5000, -5000, -6000]) == -6000
    assert candidate(nums = [1000, 2000, 3000, 1000, 4000, 2000, 5000, 3000, 4000]) == 5000
    assert candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0, 0, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]) == 9999
    assert candidate(nums = [98765, 98765, 87654, 87654, 76543, 76543, 65432, 65432, 54321, 54321, 12345]) == 12345
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9]) == -9
    assert candidate(nums = [12345, 12345, 67890, 67890, -1, -1, -2, -2, -3, -3, 5]) == 5
    assert candidate(nums = [-100, -200, -100, -300, -200, -400, -300]) == -400
    assert candidate(nums = [12345, 67890, 12345, 67890, -11111, -22222, -11111, -33333, -22222, -33333, 44444]) == 44444
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 6


