def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 10],requests = [[0, 2], [1, 3], [1, 1]]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 10],requests = [[0, 2], [1, 3], [1, 1]]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 2], [2, 3], [3, 4]]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 2], [2, 3], [3, 4]]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],requests = [[0, 2], [0, 1], [1, 2]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],requests = [[0, 2], [0, 1], [1, 2]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 4, 1, 3],requests = [[0, 4], [2, 3], [1, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 4, 1, 3],requests = [[0, 4], [2, 3], [1, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996],requests = [[0, 2], [2, 4], [0, 4]]) == 1099980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996],requests = [[0, 2], [2, 4], [0, 4]]) == 1099980: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 4], [4, 8], [0, 9]]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 4], [4, 8], [0, 9]]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],requests = [[1, 3], [0, 1]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],requests = [[1, 3], [0, 1]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 4, 1, 3],requests = [[0, 4], [1, 3], [0, 0], [3, 4]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 4, 1, 3],requests = [[0, 4], [1, 3], [0, 0], [3, 4]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6],requests = [[0, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6],requests = [[0, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 4, 1],requests = [[0, 1], [1, 2], [2, 3]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 4, 1],requests = [[0, 1], [1, 2], [2, 3]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105],requests = [[0, 5], [1, 4], [2, 3]]) == 1238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105],requests = [[0, 5], [1, 4], [2, 3]]) == 1238: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 9, 7, 6, 5],requests = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 9, 7, 6, 5],requests = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 7, 2, 1],requests = [[0, 2], [1, 4], [2, 3]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 7, 2, 1],requests = [[0, 2], [1, 4], [2, 3]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]) == 570: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 2050000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 2050000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 2], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 8], [7, 8], [0, 8]]) == 206
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 2], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 8], [7, 8], [0, 8]]) == 206: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [5, 14], [9, 14]]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [5, 14], [9, 14]]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 4]]) == 3499885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 4]]) == 3499885: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [1, 2], [3, 4], [5, 6], [7, 8], [0, 9]]) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [1, 2], [3, 4], [5, 6], [7, 8], [0, 9]]) == 296: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],requests = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]) == 5050000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],requests = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]) == 5050000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 2860
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 2860: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1025: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 0],requests = [[0, 9], [1, 5], [3, 7], [2, 8], [4, 6]]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 0],requests = [[0, 9], [1, 5], [3, 7], [2, 8], [4, 6]]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],requests = [[0, 3], [2, 5], [1, 4], [3, 7]]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],requests = [[0, 3], [2, 5], [1, 4], [3, 7]]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2, 1, 4],requests = [[0, 2], [1, 4], [0, 3], [2, 4]]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2, 1, 4],requests = [[0, 2], [1, 4], [0, 3], [2, 4]]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 2050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 2050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 19]]) == 799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 19]]) == 799: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 4, 7],requests = [[0, 5], [2, 4], [1, 3]]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 4, 7],requests = [[0, 5], [2, 4], [1, 3]]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 26000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 26000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],requests = [[0, 2], [1, 4], [0, 5], [2, 3]]) == 1499972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],requests = [[0, 2], [1, 4], [0, 5], [2, 3]]) == 1499972: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 9], [0, 4], [5, 9], [2, 7]]) == 1550000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 9], [0, 4], [5, 9], [2, 7]]) == 1550000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19]]) == 627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19]]) == 627: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [5, 15], [10, 20], [1, 2], [3, 4], [7, 8], [12, 13], [17, 18]]) == 1175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [5, 15], [10, 20], [1, 2], [3, 4], [7, 8], [12, 13], [17, 18]]) == 1175: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],requests = [[0, 19], [5, 15], [10, 10], [15, 15], [0, 9], [10, 19]]) == 6240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],requests = [[0, 19], [5, 15], [10, 10], [15, 15], [0, 9], [10, 19]]) == 6240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],requests = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7]]) == 6520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],requests = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7]]) == 6520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 5, 4],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 5, 4],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 3], [3, 6], [6, 9]]) == 275000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 3], [3, 6], [6, 9]]) == 275000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 9], [0, 9], [0, 9], [0, 9]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 9], [0, 9], [0, 9], [0, 9]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 9], [1, 2], [3, 4], [5, 6], [7, 8], [0, 4], [5, 9]]) == 16200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 9], [1, 2], [3, 4], [5, 6], [7, 8], [0, 4], [5, 9]]) == 16200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],requests = [[0, 10], [10, 20], [20, 30], [0, 20], [10, 30], [0, 30]]) == 17290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],requests = [[0, 10], [10, 20], [20, 30], [0, 20], [10, 30], [0, 30]]) == 17290: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 9], [0, 0], [9, 9], [2, 2], [5, 5], [1, 8], [3, 7]]) == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 9], [0, 0], [9, 9], [2, 2], [5, 5], [1, 8], [3, 7]]) == 1650: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 4], [5, 9], [0, 5], [4, 9], [0, 9]]) == 1840000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 4], [5, 9], [0, 5], [4, 9], [0, 9]]) == 1840000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],requests = [[0, 9], [10, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 8475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],requests = [[0, 9], [10, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 8475: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],requests = [[0, 9], [1, 3], [2, 5], [4, 7], [0, 5], [3, 8]]) == 1533
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],requests = [[0, 9], [1, 3], [2, 5], [4, 7], [0, 5], [3, 8]]) == 1533: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 430: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],requests = [[0, 4], [5, 9], [0, 9], [2, 7], [3, 8]]) == 398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],requests = [[0, 4], [5, 9], [0, 9], [2, 7], [3, 8]]) == 398: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 2], [2, 4], [4, 6], [6, 8], [0, 9], [1, 8], [3, 7], [5, 5]]) == 1165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 2], [2, 4], [4, 6], [6, 8], [0, 9], [1, 8], [3, 7], [5, 5]]) == 1165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35],requests = [[0, 6], [1, 4], [2, 3], [0, 2], [4, 5]]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35],requests = [[0, 6], [1, 4], [2, 3], [0, 2], [4, 5]]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 0],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1944425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 0],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1944425: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [5, 15], [3, 17], [7, 13]]) == 899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [5, 15], [3, 17], [7, 13]]) == 899: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],requests = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 3430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],requests = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 3430: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 5, 3, 7, 2, 8, 4, 6, 0],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 5, 3, 7, 2, 8, 4, 6, 0],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],requests = [[0, 5], [3, 7], [1, 4], [6, 9], [0, 2], [8, 10]]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],requests = [[0, 5], [3, 7], [1, 4], [6, 9], [0, 2], [8, 10]]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 3], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [0, 9]]) == 2510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 3], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [0, 9]]) == 2510: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],requests = [[0, 4], [5, 9], [2, 6], [3, 7], [1, 5], [6, 10]]) == 3380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],requests = [[0, 4], [5, 9], [2, 6], [3, 7], [1, 5], [6, 10]]) == 3380: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],requests = [[0, 19], [0, 9], [10, 19], [5, 14], [9, 14], [0, 5], [5, 10], [10, 15]]) == 1828
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],requests = [[0, 19], [0, 9], [10, 19], [5, 14], [9, 14], [0, 5], [5, 10], [10, 15]]) == 1828: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],requests = [[0, 10], [5, 15], [10, 20], [0, 20], [1, 19], [2, 18], [3, 17], [4, 16], [5, 15], [6, 14]]) == 8216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],requests = [[0, 10], [5, 15], [10, 20], [0, 20], [1, 19], [2, 18], [3, 17], [4, 16], [5, 15], [6, 14]]) == 8216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4]]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4]]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 7, 9, 1, 6, 4, 8, 2, 10],requests = [[0, 9], [2, 5], [3, 7], [1, 8], [0, 4], [5, 9]]) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 7, 9, 1, 6, 4, 8, 2, 10],requests = [[0, 9], [2, 5], [3, 7], [1, 8], [0, 4], [5, 9]]) == 234: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [0, 10], [10, 20]]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [0, 10], [10, 20]]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [1, 3], [2, 4]]) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [1, 3], [2, 4]]) == 530: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 17, 54, 32, 45, 67, 89, 101, 120, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34],requests = [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18]]) == 7390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 17, 54, 32, 45, 67, 89, 101, 120, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34],requests = [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18]]) == 7390: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 179
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 179: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 417: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14]]) == 1135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14]]) == 1135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 4], [1, 3], [2, 2], [3, 9], [4, 8], [5, 7], [6, 6], [7, 9], [0, 9], [0, 0], [9, 9]]) == 23600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 4], [1, 3], [2, 2], [3, 9], [4, 8], [5, 7], [6, 6], [7, 9], [0, 9], [0, 0], [9, 9]]) == 23600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 4], [1, 3], [2, 2], [0, 0], [4, 4], [3, 3]]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 4], [1, 3], [2, 2], [0, 0], [4, 4], [3, 3]]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [0, 4], [5, 9], [10, 14], [15, 19]]) == 630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [0, 4], [5, 9], [10, 14], [15, 19]]) == 630: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],requests = [[0, 19], [0, 0], [19, 19], [5, 15], [10, 10]]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],requests = [[0, 19], [0, 0], [19, 19], [5, 15], [10, 10]]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 19], [0, 18], [0, 17], [0, 16], [0, 15], [0, 14], [0, 13], [0, 12], [0, 11], [0, 10]]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 19], [0, 18], [0, 17], [0, 16], [0, 15], [0, 14], [0, 13], [0, 12], [0, 11], [0, 10]]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],requests = [[0, 12], [2, 5], [6, 9], [1, 4], [7, 10]]) == 449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],requests = [[0, 12], [2, 5], [6, 9], [1, 4], [7, 10]]) == 449: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 9], [10, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 3260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 9], [10, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 3260: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13], [15, 14], [16, 15], [17, 16], [18, 17], [19, 18]]) == 627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13], [15, 14], [16, 15], [17, 16], [18, 17], [19, 18]]) == 627: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [0, 5], [5, 9], [3, 7], [2, 8]]) == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [0, 5], [5, 9], [3, 7], [2, 8]]) == 221: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],requests = [[0, 4], [1, 3], [2, 2], [0, 0], [4, 4]]) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],requests = [[0, 4], [1, 3], [2, 2], [0, 0], [4, 4]]) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],requests = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 9350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],requests = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 9350: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5, 10],requests = [[0, 2], [1, 3], [1, 1]]) == 47
    assert candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 2], [2, 3], [3, 4]]) == 240
    assert candidate(nums = [0, 0, 0, 0, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 0
    assert candidate(nums = [1, 2, 3],requests = [[0, 2], [0, 1], [1, 2]]) == 15
    assert candidate(nums = [5, 2, 4, 1, 3],requests = [[0, 4], [2, 3], [1, 2]]) == 32
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],requests = [[0, 2], [2, 4], [0, 4]]) == 1099980
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 4], [4, 8], [0, 9]]) == 119
    assert candidate(nums = [1, 2, 3, 4, 5],requests = [[1, 3], [0, 1]]) == 19
    assert candidate(nums = [5, 2, 4, 1, 3],requests = [[0, 4], [1, 3], [0, 0], [3, 4]]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6],requests = [[0, 1]]) == 11
    assert candidate(nums = [5, 2, 4, 1],requests = [[0, 1], [1, 2], [2, 3]]) == 21
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4]]) == 155
    assert candidate(nums = [100, 101, 102, 103, 104, 105],requests = [[0, 5], [1, 4], [2, 3]]) == 1238
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1]]) == 54
    assert candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 150
    assert candidate(nums = [8, 9, 7, 6, 5],requests = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 59
    assert candidate(nums = [5, 3, 7, 2, 1],requests = [[0, 2], [1, 4], [2, 3]]) == 40
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]) == 570
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 2050000
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 2], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 8], [7, 8], [0, 8]]) == 206
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 5500
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [5, 14], [9, 14]]) == 680
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [2, 4]]) == 3499885
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [1, 2], [3, 4], [5, 6], [7, 8], [0, 9]]) == 296
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],requests = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]) == 5050000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 2860
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1025
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 0],requests = [[0, 9], [1, 5], [3, 7], [2, 8], [4, 6]]) == 175
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],requests = [[0, 3], [2, 5], [1, 4], [3, 7]]) == 95
    assert candidate(nums = [5, 3, 2, 1, 4],requests = [[0, 2], [1, 4], [0, 3], [2, 4]]) == 47
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 2050
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 19]]) == 799
    assert candidate(nums = [5, 3, 8, 1, 4, 7],requests = [[0, 5], [2, 4], [1, 3]]) == 67
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 26000
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],requests = [[0, 2], [1, 4], [0, 5], [2, 3]]) == 1499972
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 9], [0, 4], [5, 9], [2, 7]]) == 1550000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19]]) == 627
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 19], [5, 15], [10, 20], [1, 2], [3, 4], [7, 8], [12, 13], [17, 18]]) == 1175
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],requests = [[0, 19], [5, 15], [10, 10], [15, 15], [0, 9], [10, 19]]) == 6240
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],requests = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7]]) == 6520
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9]]) == 20
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1]]) == 54
    assert candidate(nums = [2, 3, 1, 5, 4],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]) == 42
    assert candidate(nums = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 3], [3, 6], [6, 9]]) == 275000
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 210
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [0, 9], [0, 9], [0, 9], [0, 9]]) == 50
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 9], [1, 2], [3, 4], [5, 6], [7, 8], [0, 4], [5, 9]]) == 16200
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],requests = [[0, 10], [10, 20], [20, 30], [0, 20], [10, 30], [0, 30]]) == 17290
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 9], [0, 0], [9, 9], [2, 2], [5, 5], [1, 8], [3, 7]]) == 1650
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],requests = [[0, 4], [5, 9], [0, 5], [4, 9], [0, 9]]) == 1840000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],requests = [[0, 9], [10, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 8475
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],requests = [[0, 9], [1, 3], [2, 5], [4, 7], [0, 5], [3, 8]]) == 1533
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 430
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],requests = [[0, 4], [5, 9], [0, 9], [2, 7], [3, 8]]) == 398
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 50
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 1485
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 2], [2, 4], [4, 6], [6, 8], [0, 9], [1, 8], [3, 7], [5, 5]]) == 1165
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35],requests = [[0, 6], [1, 4], [2, 3], [0, 2], [4, 5]]) == 420
    assert candidate(nums = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 0],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1944425
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [5, 15], [3, 17], [7, 13]]) == 899
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],requests = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 3430
    assert candidate(nums = [9, 1, 5, 3, 7, 2, 8, 4, 6, 0],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 175
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],requests = [[0, 5], [3, 7], [1, 4], [6, 9], [0, 2], [8, 10]]) == 1728
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 3], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [0, 9]]) == 2510
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],requests = [[0, 4], [5, 9], [2, 6], [3, 7], [1, 5], [6, 10]]) == 3380
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],requests = [[0, 19], [0, 9], [10, 19], [5, 14], [9, 14], [0, 5], [5, 10], [10, 15]]) == 1828
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 1300
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],requests = [[0, 10], [5, 15], [10, 20], [0, 20], [1, 19], [2, 18], [3, 17], [4, 16], [5, 15], [6, 14]]) == 8216
    assert candidate(nums = [100, 200, 300, 400, 500],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4]]) == 3000
    assert candidate(nums = [5, 3, 7, 9, 1, 6, 4, 8, 2, 10],requests = [[0, 9], [2, 5], [3, 7], [1, 8], [0, 4], [5, 9]]) == 234
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [0, 10], [10, 20]]) == 650
    assert candidate(nums = [50, 40, 30, 20, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [1, 3], [2, 4]]) == 530
    assert candidate(nums = [23, 17, 54, 32, 45, 67, 89, 101, 120, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34],requests = [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18]]) == 7390
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 179
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 417
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14]]) == 1135
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],requests = [[0, 4], [1, 3], [2, 2], [3, 9], [4, 8], [5, 7], [6, 6], [7, 9], [0, 9], [0, 0], [9, 9]]) == 23600
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 4], [1, 3], [2, 2], [0, 0], [4, 4], [3, 3]]) == 87
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 760
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 550
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 19], [0, 9], [10, 19], [0, 4], [5, 9], [10, 14], [15, 19]]) == 630
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],requests = [[0, 19], [0, 0], [19, 19], [5, 15], [10, 10]]) == 170
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 19], [0, 18], [0, 17], [0, 16], [0, 15], [0, 14], [0, 13], [0, 12], [0, 11], [0, 10]]) == 155
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == 110
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],requests = [[0, 12], [2, 5], [6, 9], [1, 4], [7, 10]]) == 449
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],requests = [[0, 9], [10, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == 3260
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13], [15, 14], [16, 15], [17, 16], [18, 17], [19, 18]]) == 627
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 9], [0, 5], [5, 9], [3, 7], [2, 8]]) == 221
    assert candidate(nums = [100, 200, 300, 400, 500],requests = [[0, 4], [1, 3], [2, 2], [0, 0], [4, 4]]) == 3500
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],requests = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 9350


