def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 5, 4, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 5, 4, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 3, 40, 5, 60, 7, 80, 9, 10]) == 4240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 3, 40, 5, 60, 7, 80, 9, 10]) == 4240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 6, 1, 2, 7]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 6, 1, 2, 7]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 4, 2, 10, 9, 7, 5, 3, 1]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 4, 2, 10, 9, 7, 5, 3, 1]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 3, 4, 19]) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 3, 4, 19]) == 133: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 9702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 9702: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 25]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 25]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 5, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 5, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 200, 300, 400]) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 200, 300, 400]) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500]) == 125000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500]) == 125000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 10, 25, 20, 35, 30, 45, 40, 55, 50]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 10, 25, 20, 35, 30, 45, 40, 55, 50]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]) == 999996000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]) == 999996000004: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 125000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 125000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 1000000, 1, 1000000]) == 999999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 1000000, 1, 1000000]) == 999999000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 9702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 9702: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 101, 102, 103, 104, 105]) == 42000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 101, 102, 103, 104, 105]) == 42000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 1, 2, 3, 4, 5, 6, 7, 8]) == 7999992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 1, 2, 3, 4, 5, 6, 7, 8]) == 7999992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 200000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 200000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996]) == 999997000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996]) == 999997000002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100, 90, 80, 70, 60]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100, 90, 80, 70, 60]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 1000000, 1, 1000000, 1, 1000000]) == 999999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 1000000, 1, 1000000, 1, 1000000]) == 999999000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 200, 20, 300, 30, 400, 40, 500, 50]) == 180000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 200, 20, 300, 30, 400, 40, 500, 50]) == 180000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1, 2, 3, 1000000, 4, 5, 6, 1000000]) == 999999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1, 2, 3, 1000000, 4, 5, 6, 1000000]) == 999999000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 12, 25, 30, 5, 35, 40]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 12, 25, 30, 5, 35, 40]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 25, 15, 45, 35, 65, 55, 75, 60, 85]) == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 25, 15, 45, 35, 65, 55, 75, 60, 85]) == 1275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 20, 200, 30, 300, 40, 400, 50, 500]) == 175000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 20, 200, 30, 300, 40, 400, 50, 500]) == 175000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1000000, 1000000, 1000000, 1, 2, 3, 1]) == 2999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1000000, 1000000, 1000000, 1, 2, 3, 1]) == 2999997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 10, 5, 2, 1]) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 10, 5, 2, 1]) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 15, 25, 35, 40, 5, 45, 50, 55, 60]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 15, 25, 35, 40, 5, 45, 50, 55, 60]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 200, 3, 300, 4, 400, 5, 500]) == 197500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 200, 3, 300, 4, 400, 5, 500]) == 197500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 7999928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 7999928: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 9702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 9702: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 15, 40, 25, 50, 35, 60, 45, 70, 55, 80, 65, 90, 75, 100, 85, 95]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 15, 40, 25, 50, 35, 60, 45, 70, 55, 80, 65, 90, 75, 100, 85, 95]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1980: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 40, 50, 60, 5, 15, 25, 35]) == 1925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 40, 50, 60, 5, 15, 25, 35]) == 1925: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 100000, 10000, 1000]) == 9000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 100000, 10000, 1000]) == 9000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 50000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 50000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500]) == 2500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500]) == 2500000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 3, 6, 4, 7, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 3, 6, 4, 7, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 1500, 2000, 2500, 3000, 3500]) == 1750000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 1500, 2000, 2500, 3000, 3500]) == 1750000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9, 90]) == 9702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9, 90]) == 9702: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 18, 25, 15, 30, 10, 35, 5, 40, 0, 45, 2, 50, 1, 55, 3, 60, 4, 65, 6]) == 3640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 18, 25, 15, 30, 10, 35, 5, 40, 0, 45, 2, 50, 1, 55, 3, 60, 4, 65, 6]) == 3640: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 9, 1, 7, 4, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 9, 1, 7, 4, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105]) == 840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105]) == 840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 9900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 9900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 100, 50, 200, 150, 300, 250, 400, 350]) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 100, 50, 200, 150, 300, 250, 400, 350]) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 20, 15, 25, 30, 35, 40, 45, 50]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 20, 15, 25, 30, 35, 40, 45, 50]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 198000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 198000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999999, 2, 999998, 3, 999997, 4, 999996, 5, 999995]) == 999995000006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999999, 2, 999998, 3, 999997, 4, 999996, 5, 999995]) == 999995000006: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 3, 15, 20, 2, 25, 1, 30]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 3, 15, 20, 2, 25, 1, 30]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]) == 2250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]) == 2250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 200000, 2, 199999, 3, 199998, 4, 199997, 5, 199996, 6, 199995, 7, 199994, 8, 199993, 9, 199992, 10, 199991]) == 39999400002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 200000, 2, 199999, 3, 199998, 4, 199997, 5, 199996, 6, 199995, 7, 199994, 8, 199993, 9, 199992, 10, 199991]) == 39999400002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 2, 3, 8, 4, 6]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 2, 3, 8, 4, 6]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 750, 250, 300, 600, 400, 800, 900, 100]) == 675000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 750, 250, 300, 600, 400, 800, 900, 100]) == 675000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0, -1, -2]) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0, -1, -2]) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 25, 10, 20, 15, 30, 2, 28, 29, 3]) == 812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 25, 10, 20, 15, 30, 2, 28, 29, 3]) == 812: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 8, 6, 4, 7, 9, 2, 10]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 8, 6, 4, 7, 9, 2, 10]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 10, 100, 20, 150, 30, 200, 40, 250, 50]) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 10, 100, 20, 150, 30, 200, 40, 250, 50]) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [3, 2, 1, 5, 4, 6]) == 12
    assert candidate(nums = [10, 20, 3, 40, 5, 60, 7, 80, 9, 10]) == 4240
    assert candidate(nums = [12, 6, 1, 2, 7]) == 77
    assert candidate(nums = [8, 6, 4, 2, 10, 9, 7, 5, 3, 1]) == 60
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 42
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 10, 3, 4, 19]) == 133
    assert candidate(nums = [10, 9, 8, 7, 6]) == 18
    assert candidate(nums = [100, 90, 80, 70, 60]) == 1800
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 9702
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500]) == 0
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [10, 5, 15, 20, 25]) == 125
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 80
    assert candidate(nums = [3, 2, 1, 4, 5, 6]) == 12
    assert candidate(nums = [5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [3, 2, 1, 5, 4]) == 10
    assert candidate(nums = [100, 50, 200, 300, 400]) == 20000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 0
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500]) == 125000000000
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [100, 100, 100]) == 0
    assert candidate(nums = [5, 15, 10, 25, 20, 35, 30, 45, 40, 55, 50]) == 275
    assert candidate(nums = [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]) == 999996000004
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953]) == 125000000000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0
    assert candidate(nums = [1000000, 1, 1000000, 1, 1000000]) == 999999000000
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 9702
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6]) == 81
    assert candidate(nums = [500, 400, 300, 200, 100, 101, 102, 103, 104, 105]) == 42000
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 63
    assert candidate(nums = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50]) == 250
    assert candidate(nums = [1000000, 500000, 1, 2, 3, 4, 5, 6, 7, 8]) == 7999992
    assert candidate(nums = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 200000000000
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996]) == 999997000002
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 140
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100, 90, 80, 70, 60]) == 9000
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 500
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 0
    assert candidate(nums = [1000000, 1, 1000000, 1, 1000000, 1, 1000000]) == 999999000000
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [100, 10, 200, 20, 300, 30, 400, 40, 500, 50]) == 180000
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == 600
    assert candidate(nums = [1000000, 1000000, 1, 2, 3, 1000000, 4, 5, 6, 1000000]) == 999999000000
    assert candidate(nums = [10, 5, 15, 20, 12, 25, 30, 5, 35, 40]) == 1000
    assert candidate(nums = [5, 25, 15, 45, 35, 65, 55, 75, 60, 85]) == 1275
    assert candidate(nums = [1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10]) == 90
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(nums = [10, 100, 20, 200, 30, 300, 40, 400, 50, 500]) == 175000
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 0
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 80
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(nums = [1, 2, 3, 1000000, 1000000, 1000000, 1, 2, 3, 1]) == 2999997
    assert candidate(nums = [100, 50, 25, 10, 5, 2, 1]) == 1250
    assert candidate(nums = [10, 20, 30, 15, 25, 35, 40, 5, 45, 50, 55, 60]) == 2100
    assert candidate(nums = [1, 100, 2, 200, 3, 300, 4, 400, 5, 500]) == 197500
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 7999928
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 9702
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 0
    assert candidate(nums = [10, 20, 10, 30, 15, 40, 25, 50, 35, 60, 45, 70, 55, 80, 65, 90, 75, 100, 85, 95]) == 1500
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1980
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 6
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [30, 20, 10, 40, 50, 60, 5, 15, 25, 35]) == 1925
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == 80
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 90
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 100000, 10000, 1000]) == 9000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 200000
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 81
    assert candidate(nums = [1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 50000000000
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 1]) == 2000
    assert candidate(nums = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500]) == 2500000
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 42
    assert candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 997002
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 0
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 4, 7, 5]) == 14
    assert candidate(nums = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 50000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [1000, 500, 1500, 2000, 2500, 3000, 3500]) == 1750000
    assert candidate(nums = [100, 99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9, 90]) == 9702
    assert candidate(nums = [20, 18, 25, 15, 30, 10, 35, 5, 40, 0, 45, 2, 50, 1, 55, 3, 60, 4, 65, 6]) == 3640
    assert candidate(nums = [5, 3, 8, 6, 2, 9, 1, 7, 4, 10]) == 80
    assert candidate(nums = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105]) == 840
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 9900
    assert candidate(nums = [5, 100, 50, 200, 150, 300, 250, 400, 350]) == 20000
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
    assert candidate(nums = [10, 5, 20, 15, 25, 30, 35, 40, 45, 50]) == 250
    assert candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 198000
    assert candidate(nums = [1, 999999, 2, 999998, 3, 999997, 4, 999996, 5, 999995]) == 999995000006
    assert candidate(nums = [10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]) == 9000
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 90
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 11
    assert candidate(nums = [5, 10, 3, 15, 20, 2, 25, 1, 30]) == 720
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]) == 2250
    assert candidate(nums = [1, 200000, 2, 199999, 3, 199998, 4, 199997, 5, 199996, 6, 199995, 7, 199994, 8, 199993, 9, 199992, 10, 199991]) == 39999400002
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 2, 3, 8, 4, 6]) == 81
    assert candidate(nums = [1000, 500, 750, 250, 300, 600, 400, 800, 900, 100]) == 675000
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0, -1, -2]) == 1250
    assert candidate(nums = [5, 25, 10, 20, 15, 30, 2, 28, 29, 3]) == 812
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
    assert candidate(nums = [5, 3, 1, 8, 6, 4, 7, 9, 2, 10]) == 70
    assert candidate(nums = [50, 10, 100, 20, 150, 30, 200, 40, 250, 50]) == 40000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
    assert candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10]) == 20


