def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1]],k = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1]],k = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9, 1], [7, 2], [5, 3], [3, 4], [1, 5]],k = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9, 1], [7, 2], [5, 3], [3, 4], [1, 5]],k = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 3) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 3) == 129: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [6, 2], [7, 3], [8, 4]],k = 4) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [6, 2], [7, 3], [8, 4]],k = 4) == 42: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]],k = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]],k = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 5) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 5) == 175: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 5) == 1525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 5) == 1525: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [7, 2], [3, 2], [8, 3], [6, 3]],k = 3) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [7, 2], [3, 2], [8, 3], [6, 3]],k = 3) == 29: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 3]],k = 4) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 3]],k = 4) == 29: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5]],k = 5) == 5000000025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5]],k = 5) == 5000000025: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],k = 3) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],k = 3) == 33: {e}')
    
    total += 1
    try:
        result = candidate(items = [[3, 2], [5, 1], [10, 1]],k = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[3, 2], [5, 1], [10, 1]],k = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1]],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1]],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 4) == 1416
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 4) == 1416: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],k = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],k = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 5], [10, 5], [10, 5], [10, 5], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]],k = 5) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 5], [10, 5], [10, 5], [10, 5], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]],k = 5) == 75: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000]],k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000]],k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(items = [[3, 1], [3, 1], [2, 2], [5, 3]],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[3, 1], [3, 1], [2, 2], [5, 3]],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 5], [5, 5], [5, 5], [5, 5]],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 5], [5, 5], [5, 5], [5, 5]],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],k = 5) == 4025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],k = 5) == 4025: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 1], [80, 2], [70, 2], [60, 3], [50, 3], [40, 3], [30, 4], [20, 4], [10, 4]],k = 3) == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 1], [80, 2], [70, 2], [60, 3], [50, 3], [40, 3], [30, 4], [20, 4], [10, 4]],k = 3) == 274: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2]],k = 5) == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2]],k = 5) == 401: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 5) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 5) == 65: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 10], [90, 9], [80, 8], [70, 7], [60, 6], [50, 5], [40, 4], [30, 3], [20, 2], [10, 1], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],k = 8) == 584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 10], [90, 9], [80, 8], [70, 7], [60, 6], [50, 5], [40, 4], [30, 3], [20, 2], [10, 1], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],k = 8) == 584: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15]],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15]],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [2000000000, 2], [3000000000, 3], [4000000000, 4], [5000000000, 5], [6000000000, 6], [7000000000, 7], [8000000000, 8], [9000000000, 9], [10000000000, 10]],k = 5) == 40000000025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [2000000000, 2], [3000000000, 3], [4000000000, 4], [5000000000, 5], [6000000000, 6], [7000000000, 7], [8000000000, 8], [9000000000, 9], [10000000000, 10]],k = 5) == 40000000025: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4]],k = 10) == 661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4]],k = 10) == 661: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 10) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 10) == 650: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 2], [3, 2], [2, 2], [1, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3], [10, 4]],k = 10) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 2], [3, 2], [2, 2], [1, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3], [10, 4]],k = 10) == 94: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 15) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 15) == 160: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 3], [10, 2], [15, 1], [20, 3], [25, 2], [30, 1], [35, 4]],k = 4) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 3], [10, 2], [15, 1], [20, 3], [25, 2], [30, 1], [35, 4]],k = 4) == 126: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2]],k = 5) == 5000000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2]],k = 5) == 5000000004: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4]],k = 7) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4]],k = 7) == 98: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 1], [400, 2], [500, 3], [600, 3], [700, 4], [800, 4], [900, 5]],k = 6) == 3916
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 1], [400, 2], [500, 3], [600, 3], [700, 4], [800, 4], [900, 5]],k = 6) == 3916: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 15) == 1074
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 15) == 1074: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]],k = 10) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]],k = 10) == 155: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],k = 5) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],k = 5) == 65: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [900000000, 1], [800000000, 2], [700000000, 2], [600000000, 3], [500000000, 3], [400000000, 3], [300000000, 4], [200000000, 4], [100000000, 4]],k = 3) == 2700000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [900000000, 1], [800000000, 2], [700000000, 2], [600000000, 3], [500000000, 3], [400000000, 3], [300000000, 4], [200000000, 4], [100000000, 4]],k = 3) == 2700000004: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2]],k = 5) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2]],k = 5) == 43: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2], [5, 2], [5, 3], [5, 3], [5, 3], [5, 3], [5, 3]],k = 10) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2], [5, 2], [5, 3], [5, 3], [5, 3], [5, 3], [5, 3]],k = 10) == 59: {e}')
    
    total += 1
    try:
        result = candidate(items = [[50, 1], [40, 1], [30, 1], [20, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [50, 3], [40, 3], [30, 3], [20, 3], [10, 3]],k = 5) == 214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[50, 1], [40, 1], [30, 1], [20, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [50, 3], [40, 3], [30, 3], [20, 3], [10, 3]],k = 5) == 214: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [10, 1], [10, 1], [10, 2], [10, 2], [10, 2], [10, 3], [10, 3], [10, 3], [10, 4]],k = 4) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [10, 1], [10, 1], [10, 2], [10, 2], [10, 2], [10, 3], [10, 3], [10, 3], [10, 4]],k = 4) == 56: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 1], [3, 2], [2, 3], [1, 4], [9, 5]],k = 7) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 1], [3, 2], [2, 3], [1, 4], [9, 5]],k = 7) == 73: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5], [1000000000, 6], [1000000000, 7], [1000000000, 8], [1000000000, 9], [1000000000, 10]],k = 5) == 5000000025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5], [1000000000, 6], [1000000000, 7], [1000000000, 8], [1000000000, 9], [1000000000, 10]],k = 5) == 5000000025: {e}')
    
    total += 1
    try:
        result = candidate(items = [[50, 1], [40, 2], [30, 3], [20, 4], [10, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],k = 5) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[50, 1], [40, 2], [30, 3], [20, 4], [10, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],k = 5) == 175: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [7, 2], [9, 3], [10, 2], [12, 1], [15, 4], [18, 5], [20, 1]],k = 5) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [7, 2], [9, 3], [10, 2], [12, 1], [15, 4], [18, 5], [20, 1]],k = 5) == 97: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [10, 2], [10, 2], [10, 2], [10, 2], [10, 2], [15, 3], [15, 3], [15, 3], [15, 3], [15, 3]],k = 5) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [10, 2], [10, 2], [10, 2], [10, 2], [10, 2], [15, 3], [15, 3], [15, 3], [15, 3], [15, 3]],k = 5) == 76: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [10, 1], [15, 1], [20, 1], [25, 1], [30, 1], [35, 1], [40, 1], [45, 1], [50, 1], [5, 2], [10, 2], [15, 2], [20, 2], [25, 2], [30, 2], [35, 2], [40, 2], [45, 2], [50, 2]],k = 10) == 404
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [10, 1], [15, 1], [20, 1], [25, 1], [30, 1], [35, 1], [40, 1], [45, 1], [50, 1], [5, 2], [10, 2], [15, 2], [20, 2], [25, 2], [30, 2], [35, 2], [40, 2], [45, 2], [50, 2]],k = 10) == 404: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],k = 10) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],k = 10) == 155: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 1], [70, 1], [80, 1], [90, 1], [100, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 15) == 594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 1], [70, 1], [80, 1], [90, 1], [100, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 15) == 594: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 1], [700, 2], [800, 3], [900, 4], [1000, 5]],k = 7) == 4925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 1], [700, 2], [800, 3], [900, 4], [1000, 5]],k = 7) == 4925: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],k = 6) == 454
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],k = 6) == 454: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 10], [65, 20], [75, 30], [85, 40], [95, 50]],k = 6) == 445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 10], [65, 20], [75, 30], [85, 40], [95, 50]],k = 6) == 445: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],k = 3) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],k = 3) == 39: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],k = 7) == 539
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],k = 7) == 539: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4], [11, 4], [12, 4], [13, 5], [14, 5], [15, 5]],k = 7) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4], [11, 4], [12, 4], [13, 5], [14, 5], [15, 5]],k = 7) == 97: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4], [11, 4], [12, 4], [13, 5], [14, 5], [15, 5], [16, 6], [17, 6], [18, 6], [19, 7], [20, 7], [21, 7]],k = 10) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4], [11, 4], [12, 4], [13, 5], [14, 5], [15, 5], [16, 6], [17, 6], [18, 6], [19, 7], [20, 7], [21, 7]],k = 10) == 189: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 1], [30, 1], [40, 2], [50, 2], [60, 2], [70, 3], [80, 3], [90, 3], [100, 4]],k = 7) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 1], [30, 1], [40, 2], [50, 2], [60, 2], [70, 3], [80, 3], [90, 3], [100, 4]],k = 7) == 499: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4]],k = 4) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4]],k = 4) == 44: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2]],k = 5) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2]],k = 5) == 43: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],k = 6) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],k = 6) == 45: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 15) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 15) == 345: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [10, 1], [9, 2], [8, 3], [7, 4], [6, 5]],k = 8) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [10, 1], [9, 2], [8, 3], [7, 4], [6, 5]],k = 8) == 116: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 1], [400, 1], [300, 1], [200, 1], [100, 1], [500, 2], [400, 2], [300, 2], [200, 2], [100, 2], [500, 3], [400, 3], [300, 3], [200, 3], [100, 3]],k = 8) == 3309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 1], [400, 1], [300, 1], [200, 1], [100, 1], [500, 2], [400, 2], [300, 2], [200, 2], [100, 2], [500, 3], [400, 3], [300, 3], [200, 3], [100, 3]],k = 8) == 3309: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3]],k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3]],k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 1], [30, 2], [40, 2], [50, 3], [60, 3], [70, 4], [80, 4], [90, 5], [100, 5], [110, 6], [120, 6], [130, 7], [140, 7], [150, 8], [160, 8], [170, 9], [180, 9], [190, 10], [200, 10]],k = 15) == 2014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 1], [30, 2], [40, 2], [50, 3], [60, 3], [70, 4], [80, 4], [90, 5], [100, 5], [110, 6], [120, 6], [130, 7], [140, 7], [150, 8], [160, 8], [170, 9], [180, 9], [190, 10], [200, 10]],k = 15) == 2014: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2]],k = 4) == 341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2]],k = 4) == 341: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2], [5, 2]],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2], [5, 2]],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 10) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 10) == 110: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 10], [12, 9], [13, 8], [14, 7], [15, 6], [16, 5], [17, 4], [18, 3], [19, 2], [20, 1]],k = 15) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 10], [12, 9], [13, 8], [14, 7], [15, 6], [16, 5], [17, 4], [18, 3], [19, 2], [20, 1]],k = 15) == 295: {e}')
    
    total += 1
    try:
        result = candidate(items = [[3, 1], [5, 2], [7, 3], [9, 4], [11, 5], [13, 1], [15, 2], [17, 3], [19, 4], [21, 5]],k = 5) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[3, 1], [5, 2], [7, 3], [9, 4], [11, 5], [13, 1], [15, 2], [17, 3], [19, 4], [21, 5]],k = 5) == 110: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 5) == 425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 5) == 425: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],k = 3) == 279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],k = 3) == 279: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 1], [40, 1], [30, 1], [20, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 15) == 594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 1], [40, 1], [30, 1], [20, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 15) == 594: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 1], [50, 2], [60, 3], [70, 4], [80, 5], [90, 4], [100, 5], [110, 6], [120, 7], [130, 8], [140, 9], [150, 10]],k = 8) == 969
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 1], [50, 2], [60, 3], [70, 4], [80, 5], [90, 4], [100, 5], [110, 6], [120, 7], [130, 8], [140, 9], [150, 10]],k = 8) == 969: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 10) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 10) == 155: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],k = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],k = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [999999999, 2], [888888888, 3], [777777777, 4], [666666666, 5], [555555555, 6], [444444444, 7], [333333333, 8], [222222222, 9], [111111111, 10]],k = 5) == 4333333355
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [999999999, 2], [888888888, 3], [777777777, 4], [666666666, 5], [555555555, 6], [444444444, 7], [333333333, 8], [222222222, 9], [111111111, 10]],k = 5) == 4333333355: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 10) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 10) == 205: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 10) == 674
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 10) == 674: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],k = 8) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],k = 8) == 58: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 6) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 6) == 49: {e}')
    
    total += 1
    try:
        result = candidate(items = [[90, 1], [80, 2], [70, 3], [60, 4], [50, 5], [40, 6], [30, 7], [20, 8], [10, 9]],k = 5) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[90, 1], [80, 2], [70, 3], [60, 4], [50, 5], [40, 6], [30, 7], [20, 8], [10, 9]],k = 5) == 375: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 1], [70, 2], [80, 3], [90, 4], [100, 5], [110, 6], [120, 7], [130, 8], [140, 9], [150, 10], [160, 11], [170, 12], [180, 13], [190, 14], [200, 15]],k = 10) == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 1], [70, 2], [80, 3], [90, 4], [100, 5], [110, 6], [120, 7], [130, 8], [140, 9], [150, 10], [160, 11], [170, 12], [180, 13], [190, 14], [200, 15]],k = 10) == 1650: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 100000], [900000000, 100000], [800000000, 100000], [700000000, 100000], [600000000, 100000]],k = 3) == 2700000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 100000], [900000000, 100000], [800000000, 100000], [700000000, 100000], [600000000, 100000]],k = 3) == 2700000001: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1]],k = 10) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1]],k = 10) == 106: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 1], [8, 2], [7, 2], [6, 3], [5, 3], [4, 3], [3, 4], [2, 4], [1, 4], [100, 5], [99, 5], [98, 5], [97, 5], [96, 5]],k = 10) == 551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 1], [8, 2], [7, 2], [6, 3], [5, 3], [4, 3], [3, 4], [2, 4], [1, 4], [100, 5], [99, 5], [98, 5], [97, 5], [96, 5]],k = 10) == 551: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 2], [5, 2], [5, 3], [5, 3], [5, 4], [5, 4], [5, 5], [5, 5]],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 2], [5, 2], [5, 3], [5, 3], [5, 4], [5, 4], [5, 5], [5, 5]],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 7) == 5000000051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 7) == 5000000051: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 7) == 539
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 7) == 539: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 5) == 2109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 5) == 2109: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [110, 1], [120, 2], [130, 3], [140, 4], [150, 5]],k = 12) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [110, 1], [120, 2], [130, 3], [140, 4], [150, 5]],k = 12) == 1240: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 2], [70, 2], [80, 2], [90, 2], [100, 2], [110, 3], [120, 3], [130, 3], [140, 3], [150, 3]],k = 10) == 1054
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 2], [70, 2], [80, 2], [90, 2], [100, 2], [110, 3], [120, 3], [130, 3], [140, 3], [150, 3]],k = 10) == 1054: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [10, 6], [9, 7], [8, 8], [7, 9], [6, 10], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],k = 5) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [10, 6], [9, 7], [8, 8], [7, 9], [6, 10], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],k = 5) == 65: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 4) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 4) == 36: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],k = 10) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],k = 10) == 155: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 2], [70, 2], [80, 2], [90, 2], [100, 2]],k = 5) == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 2], [70, 2], [80, 2], [90, 2], [100, 2]],k = 5) == 401: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [500000000, 1], [250000000, 1], [125000000, 1], [62500000, 1], [31250000, 2], [15625000, 2], [7812500, 2], [3906250, 2], [1953125, 2]],k = 4) == 1875000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [500000000, 1], [250000000, 1], [125000000, 1], [62500000, 1], [31250000, 2], [15625000, 2], [7812500, 2], [3906250, 2], [1953125, 2]],k = 4) == 1875000001: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000000000, 1], [900000000, 2], [800000000, 3], [700000000, 4], [600000000, 5], [500000000, 6], [400000000, 7], [300000000, 8], [200000000, 9], [100000000, 10]],k = 5) == 4000000025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000000000, 1], [900000000, 2], [800000000, 3], [700000000, 4], [600000000, 5], [500000000, 6], [400000000, 7], [300000000, 8], [200000000, 9], [100000000, 10]],k = 5) == 4000000025: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9]],k = 10) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9]],k = 10) == 84: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15]],k = 7) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15]],k = 7) == 84: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [99, 2], [98, 3], [97, 4], [96, 5], [95, 1], [94, 2], [93, 3], [92, 4], [91, 5]],k = 3) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [99, 2], [98, 3], [97, 4], [96, 5], [95, 1], [94, 2], [93, 3], [92, 4], [91, 5]],k = 3) == 306: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 7], [14, 7], [15, 8], [16, 8], [17, 9], [18, 9], [19, 10], [20, 10]],k = 5) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 7], [14, 7], [15, 8], [16, 8], [17, 9], [18, 9], [19, 10], [20, 10]],k = 5) == 105: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 1], [30, 2], [40, 2], [50, 3], [60, 3], [70, 4], [80, 4], [90, 5], [100, 5], [110, 6], [120, 6], [130, 7], [140, 7], [150, 8], [160, 8]],k = 8) == 1016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 1], [30, 2], [40, 2], [50, 3], [60, 3], [70, 4], [80, 4], [90, 5], [100, 5], [110, 6], [120, 6], [130, 7], [140, 7], [150, 8], [160, 8]],k = 8) == 1016: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1]],k = 2) == 20
    assert candidate(items = [[9, 1], [7, 2], [5, 3], [3, 4], [1, 5]],k = 4) == 40
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 3) == 129
    assert candidate(items = [[5, 1], [6, 2], [7, 3], [8, 4]],k = 4) == 42
    assert candidate(items = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]],k = 4) == 30
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 5) == 175
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 5) == 1525
    assert candidate(items = [[5, 1], [7, 2], [3, 2], [8, 3], [6, 3]],k = 3) == 29
    assert candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],k = 3) == 12
    assert candidate(items = [[5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 3]],k = 4) == 29
    assert candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5]],k = 5) == 5000000025
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],k = 3) == 33
    assert candidate(items = [[3, 2], [5, 1], [10, 1]],k = 2) == 17
    assert candidate(items = [[1, 1], [2, 1], [3, 1]],k = 3) == 7
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 4) == 1416
    assert candidate(items = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],k = 3) == 21
    assert candidate(items = [[10, 5], [10, 5], [10, 5], [10, 5], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]],k = 5) == 75
    assert candidate(items = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]],k = 2) == 10
    assert candidate(items = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000]],k = 3) == 13
    assert candidate(items = [[3, 1], [3, 1], [2, 2], [5, 3]],k = 3) == 19
    assert candidate(items = [[5, 5], [5, 5], [5, 5], [5, 5]],k = 2) == 11
    assert candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],k = 3) == 12
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],k = 5) == 4025
    assert candidate(items = [[100, 1], [90, 1], [80, 2], [70, 2], [60, 3], [50, 3], [40, 3], [30, 4], [20, 4], [10, 4]],k = 3) == 274
    assert candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2]],k = 5) == 401
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 5) == 65
    assert candidate(items = [[100, 10], [90, 9], [80, 8], [70, 7], [60, 6], [50, 5], [40, 4], [30, 3], [20, 2], [10, 1], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],k = 8) == 584
    assert candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15]],k = 5) == 30
    assert candidate(items = [[1000000000, 1], [2000000000, 2], [3000000000, 3], [4000000000, 4], [5000000000, 5], [6000000000, 6], [7000000000, 7], [8000000000, 8], [9000000000, 9], [10000000000, 10]],k = 5) == 40000000025
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4]],k = 10) == 661
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 10) == 650
    assert candidate(items = [[9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 2], [3, 2], [2, 2], [1, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3], [10, 4]],k = 10) == 94
    assert candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 15) == 160
    assert candidate(items = [[5, 3], [10, 2], [15, 1], [20, 3], [25, 2], [30, 1], [35, 4]],k = 4) == 126
    assert candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2], [1000000000, 1], [1000000000, 2]],k = 5) == 5000000004
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4]],k = 7) == 98
    assert candidate(items = [[100, 1], [200, 2], [300, 1], [400, 2], [500, 3], [600, 3], [700, 4], [800, 4], [900, 5]],k = 6) == 3916
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 15) == 1074
    assert candidate(items = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]],k = 10) == 155
    assert candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],k = 5) == 65
    assert candidate(items = [[1000000000, 1], [900000000, 1], [800000000, 2], [700000000, 2], [600000000, 3], [500000000, 3], [400000000, 3], [300000000, 4], [200000000, 4], [100000000, 4]],k = 3) == 2700000004
    assert candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2]],k = 5) == 43
    assert candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2], [5, 2], [5, 3], [5, 3], [5, 3], [5, 3], [5, 3]],k = 10) == 59
    assert candidate(items = [[50, 1], [40, 1], [30, 1], [20, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [50, 3], [40, 3], [30, 3], [20, 3], [10, 3]],k = 5) == 214
    assert candidate(items = [[10, 1], [10, 1], [10, 1], [10, 2], [10, 2], [10, 2], [10, 3], [10, 3], [10, 3], [10, 4]],k = 4) == 56
    assert candidate(items = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 1], [3, 2], [2, 3], [1, 4], [9, 5]],k = 7) == 73
    assert candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5], [1000000000, 6], [1000000000, 7], [1000000000, 8], [1000000000, 9], [1000000000, 10]],k = 5) == 5000000025
    assert candidate(items = [[50, 1], [40, 2], [30, 3], [20, 4], [10, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],k = 5) == 175
    assert candidate(items = [[5, 1], [7, 2], [9, 3], [10, 2], [12, 1], [15, 4], [18, 5], [20, 1]],k = 5) == 97
    assert candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [10, 2], [10, 2], [10, 2], [10, 2], [10, 2], [15, 3], [15, 3], [15, 3], [15, 3], [15, 3]],k = 5) == 76
    assert candidate(items = [[5, 1], [10, 1], [15, 1], [20, 1], [25, 1], [30, 1], [35, 1], [40, 1], [45, 1], [50, 1], [5, 2], [10, 2], [15, 2], [20, 2], [25, 2], [30, 2], [35, 2], [40, 2], [45, 2], [50, 2]],k = 10) == 404
    assert candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],k = 10) == 155
    assert candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 1], [70, 1], [80, 1], [90, 1], [100, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 15) == 594
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 1], [700, 2], [800, 3], [900, 4], [1000, 5]],k = 7) == 4925
    assert candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]],k = 6) == 454
    assert candidate(items = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 10], [65, 20], [75, 30], [85, 40], [95, 50]],k = 6) == 445
    assert candidate(items = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],k = 3) == 39
    assert candidate(items = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],k = 7) == 539
    assert candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4], [11, 4], [12, 4], [13, 5], [14, 5], [15, 5]],k = 7) == 97
    assert candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4], [11, 4], [12, 4], [13, 5], [14, 5], [15, 5], [16, 6], [17, 6], [18, 6], [19, 7], [20, 7], [21, 7]],k = 10) == 189
    assert candidate(items = [[10, 1], [20, 1], [30, 1], [40, 2], [50, 2], [60, 2], [70, 3], [80, 3], [90, 3], [100, 4]],k = 7) == 499
    assert candidate(items = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 3], [8, 3], [9, 3], [10, 4]],k = 4) == 44
    assert candidate(items = [[5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2]],k = 5) == 43
    assert candidate(items = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]],k = 6) == 45
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 15) == 345
    assert candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [10, 1], [9, 2], [8, 3], [7, 4], [6, 5]],k = 8) == 116
    assert candidate(items = [[500, 1], [400, 1], [300, 1], [200, 1], [100, 1], [500, 2], [400, 2], [300, 2], [200, 2], [100, 2], [500, 3], [400, 3], [300, 3], [200, 3], [100, 3]],k = 8) == 3309
    assert candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3]],k = 3) == 15
    assert candidate(items = [[10, 1], [20, 1], [30, 2], [40, 2], [50, 3], [60, 3], [70, 4], [80, 4], [90, 5], [100, 5], [110, 6], [120, 6], [130, 7], [140, 7], [150, 8], [160, 8], [170, 9], [180, 9], [190, 10], [200, 10]],k = 15) == 2014
    assert candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 2], [40, 2], [30, 2], [20, 2], [10, 2]],k = 4) == 341
    assert candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 5) == 30
    assert candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2], [5, 2]],k = 3) == 19
    assert candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 10) == 110
    assert candidate(items = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 10], [12, 9], [13, 8], [14, 7], [15, 6], [16, 5], [17, 4], [18, 3], [19, 2], [20, 1]],k = 15) == 295
    assert candidate(items = [[3, 1], [5, 2], [7, 3], [9, 4], [11, 5], [13, 1], [15, 2], [17, 3], [19, 4], [21, 5]],k = 5) == 110
    assert candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],k = 10) == 11
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 5) == 425
    assert candidate(items = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],k = 3) == 279
    assert candidate(items = [[100, 1], [90, 1], [80, 1], [70, 1], [60, 1], [50, 1], [40, 1], [30, 1], [20, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 15) == 594
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 1], [50, 2], [60, 3], [70, 4], [80, 5], [90, 4], [100, 5], [110, 6], [120, 7], [130, 8], [140, 9], [150, 10]],k = 8) == 969
    assert candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],k = 3) == 7
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 10) == 155
    assert candidate(items = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],k = 10) == 120
    assert candidate(items = [[1000000000, 1], [999999999, 2], [888888888, 3], [777777777, 4], [666666666, 5], [555555555, 6], [444444444, 7], [333333333, 8], [222222222, 9], [111111111, 10]],k = 5) == 4333333355
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 10) == 205
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],k = 10) == 674
    assert candidate(items = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],k = 8) == 58
    assert candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 6) == 49
    assert candidate(items = [[90, 1], [80, 2], [70, 3], [60, 4], [50, 5], [40, 6], [30, 7], [20, 8], [10, 9]],k = 5) == 375
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 1], [70, 2], [80, 3], [90, 4], [100, 5], [110, 6], [120, 7], [130, 8], [140, 9], [150, 10], [160, 11], [170, 12], [180, 13], [190, 14], [200, 15]],k = 10) == 1650
    assert candidate(items = [[1000000000, 100000], [900000000, 100000], [800000000, 100000], [700000000, 100000], [600000000, 100000]],k = 3) == 2700000001
    assert candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1]],k = 10) == 106
    assert candidate(items = [[10, 1], [9, 1], [8, 2], [7, 2], [6, 3], [5, 3], [4, 3], [3, 4], [2, 4], [1, 4], [100, 5], [99, 5], [98, 5], [97, 5], [96, 5]],k = 10) == 551
    assert candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],k = 5) == 50
    assert candidate(items = [[5, 1], [5, 1], [5, 2], [5, 2], [5, 3], [5, 3], [5, 4], [5, 4], [5, 5], [5, 5]],k = 5) == 50
    assert candidate(items = [[1000000000, 1], [1000000000, 2], [1000000000, 3], [1000000000, 4], [1000000000, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],k = 7) == 5000000051
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 7) == 539
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],k = 5) == 2109
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [110, 1], [120, 2], [130, 3], [140, 4], [150, 5]],k = 12) == 1240
    assert candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],k = 3) == 24
    assert candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 2], [70, 2], [80, 2], [90, 2], [100, 2], [110, 3], [120, 3], [130, 3], [140, 3], [150, 3]],k = 10) == 1054
    assert candidate(items = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [10, 6], [9, 7], [8, 8], [7, 9], [6, 10], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],k = 5) == 65
    assert candidate(items = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],k = 4) == 36
    assert candidate(items = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],k = 10) == 155
    assert candidate(items = [[10, 1], [20, 1], [30, 1], [40, 1], [50, 1], [60, 2], [70, 2], [80, 2], [90, 2], [100, 2]],k = 5) == 401
    assert candidate(items = [[1000000000, 1], [500000000, 1], [250000000, 1], [125000000, 1], [62500000, 1], [31250000, 2], [15625000, 2], [7812500, 2], [3906250, 2], [1953125, 2]],k = 4) == 1875000001
    assert candidate(items = [[1000000000, 1], [900000000, 2], [800000000, 3], [700000000, 4], [600000000, 5], [500000000, 6], [400000000, 7], [300000000, 8], [200000000, 9], [100000000, 10]],k = 5) == 4000000025
    assert candidate(items = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9]],k = 10) == 84
    assert candidate(items = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15]],k = 7) == 84
    assert candidate(items = [[100, 1], [99, 2], [98, 3], [97, 4], [96, 5], [95, 1], [94, 2], [93, 3], [92, 4], [91, 5]],k = 3) == 306
    assert candidate(items = [[1, 1], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 7], [14, 7], [15, 8], [16, 8], [17, 9], [18, 9], [19, 10], [20, 10]],k = 5) == 105
    assert candidate(items = [[10, 1], [20, 1], [30, 2], [40, 2], [50, 3], [60, 3], [70, 4], [80, 4], [90, 5], [100, 5], [110, 6], [120, 6], [130, 7], [140, 7], [150, 8], [160, 8]],k = 8) == 1016


