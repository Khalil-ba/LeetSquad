def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 6, 8, 7]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 6, 8, 7]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 6, 8, 7, 4, 3, 2, 10, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 6, 8, 7, 4, 3, 2, 10, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 1, 2]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 1, 2]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996]) == 696500047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996]) == 696500047: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 6, 4, 2]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 6, 4, 2]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 5, 6, 4, 2]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 5, 6, 4, 2]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997]) == 817200025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997]) == 817200025: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == 643000419
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == 643000419: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2400000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 6, 7, 8, 9, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 642
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 6, 7, 8, 9, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 642: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 10, 40, 30, 20, 10]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 10, 40, 30, 20, 10]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999999, 1, 9999999, 1, 9999999, 1, 9999999, 1, 9999999, 1]) == 979300008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999999, 1, 9999999, 1, 9999999, 1, 9999999, 1, 9999999, 1]) == 979300008: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 6, 2, 8, 4, 9, 1, 3]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 6, 2, 8, 4, 9, 1, 3]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991, 9999990]) == 342300564
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991, 9999990]) == 342300564: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 756: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 10000000, 1, 1, 1, 1, 10000000, 1, 1, 1, 1]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 10000000, 1, 1, 1, 1, 10000000, 1, 1, 1, 1]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000]) == 996500007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000]) == 996500007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 238: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 999930007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 999930007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == 332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == 332: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000]) == 998320007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000]) == 998320007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 3, 2, 5, 4, 3, 6, 5, 4, 7, 6, 5, 8, 7, 6, 9, 8, 7]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 3, 2, 5, 4, 3, 6, 5, 4, 7, 6, 5, 8, 7, 6, 9, 8, 7]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994]) == 365100133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994]) == 365100133: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 6, 5, 4, 1, 3, 7, 9]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 6, 5, 4, 1, 3, 7, 9]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 24000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 24000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 980: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4, 1, 5, 1, 6, 1, 7]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4, 1, 5, 1, 6, 1, 7]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == 643000419
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == 643000419: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 3300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 3300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 5, 4, 7, 6, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 5, 4, 7, 6, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 756: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 4, 3, 6, 2, 8, 7, 9]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 4, 3, 6, 2, 8, 7, 9]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 1, 2, 8, 9, 3, 4, 7, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 1, 2, 8, 9, 3, 4, 7, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]) == 993000007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]) == 993000007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000000, 2, 9999999, 3, 9999998, 4, 9999997, 5, 9999996]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000000, 2, 9999999, 3, 9999998, 4, 9999997, 5, 9999996]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999996, 9999997, 9999998, 9999999, 10000000, 9999999, 9999998, 9999997, 9999996]) == 433700087
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999996, 9999997, 9999998, 9999999, 10000000, 9999999, 9999998, 9999997, 9999996]) == 433700087: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 24000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 24000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 999300007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 375: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 999937007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 999937007: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 9, 6, 8, 7]) == 180
    assert candidate(nums = [2, 1]) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 180
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [10000000]) == 999300007
    assert candidate(nums = [5, 9, 6, 8, 7, 4, 3, 2, 10, 1]) == 180
    assert candidate(nums = [2, 3, 3, 1, 2]) == 18
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996]) == 696500047
    assert candidate(nums = [5, 5, 5, 5, 5]) == 125
    assert candidate(nums = [7, 1, 5, 6, 4, 2]) == 60
    assert candidate(nums = [1, 2, 3, 4, 5]) == 36
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 15
    assert candidate(nums = [1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [3, 1, 5, 6, 4, 2]) == 60
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997]) == 817200025
    assert candidate(nums = [5, 4, 3, 2, 1]) == 36
    assert candidate(nums = [1, 2]) == 4
    assert candidate(nums = [1, 2, 3, 2]) == 14
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 72
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 135
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == 643000419
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2400000
    assert candidate(nums = [5, 8, 6, 7, 8, 9, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 642
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1728
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 360
    assert candidate(nums = [10, 20, 10, 30, 20, 10, 40, 30, 20, 10]) == 2100
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1728
    assert candidate(nums = [9999999, 1, 9999999, 1, 9999999, 1, 9999999, 1, 9999999, 1]) == 979300008
    assert candidate(nums = [1, 3, 2, 5, 6, 2, 8, 4, 9, 1, 3]) == 84
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991, 9999990]) == 342300564
    assert candidate(nums = [1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 756
    assert candidate(nums = [1, 1, 1, 1, 10000000, 1, 1, 1, 1, 10000000, 1, 1, 1, 1]) == 999300007
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000]) == 996500007
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 3600
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 90
    assert candidate(nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 238
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 420
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 240
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 480
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 420
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 480
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 999930007
    assert candidate(nums = [2, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == 332
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1728
    assert candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000]) == 998320007
    assert candidate(nums = [3, 2, 1, 4, 3, 2, 5, 4, 3, 6, 5, 4, 7, 6, 5, 8, 7, 6, 9, 8, 7]) == 315
    assert candidate(nums = [10, 20, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 240
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994]) == 365100133
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(nums = [8, 2, 6, 5, 4, 1, 3, 7, 9]) == 112
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 24000
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 41
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 82
    assert candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1]) == 999300007
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 980
    assert candidate(nums = [2, 1, 3, 4, 1, 5, 1, 6, 1, 7]) == 49
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 420
    assert candidate(nums = [10000000, 9999999, 9999998, 9999997, 9999996, 9999995, 9999994, 9999993, 9999992, 9999991]) == 643000419
    assert candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 3300
    assert candidate(nums = [3, 2, 5, 4, 7, 6, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 756
    assert candidate(nums = [1, 5, 4, 3, 6, 2, 8, 7, 9]) == 168
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 81
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 100
    assert candidate(nums = [5, 6, 1, 2, 8, 9, 3, 4, 7, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1728
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 180
    assert candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]) == 993000007
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 144
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 148
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
    assert candidate(nums = [1, 10000000, 2, 9999999, 3, 9999998, 4, 9999997, 5, 9999996]) == 999300007
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]) == 36
    assert candidate(nums = [9999996, 9999997, 9999998, 9999999, 10000000, 9999999, 9999998, 9999997, 9999996]) == 433700087
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 30
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 33
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 24000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 999300007
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 375
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 25
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 999937007
    assert candidate(nums = [1, 10000000, 1, 10000000, 1, 10000000, 1, 10000000]) == 999300007


