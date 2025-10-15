def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [3, 3, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [3, 3, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 5, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 5, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [5, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [5, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 1000000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 1000000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1000000000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1000000000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1000000000, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1000000000, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 1333333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 1333333333: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 999999999, 1, 2, 3, 4, 5]) == 2000000014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 999999999, 1, 2, 3, 4, 5]) == 2000000014: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 200, 300, 400]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 200, 300, 400]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 999999999, 888888888]) == 2888888887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 999999999, 888888888]) == 2888888887: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 1596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 1596: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [500000000, 500000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [500000000, 500000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000000009: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 100]) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 100]) == 181: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 10, 10, 10, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 10, 10, 10, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [999999999, 1, 1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [999999999, 1, 1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1000000000, 1000000000, 1]) == 3000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1000000000, 1000000000, 1]) == 3000000001: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5000000001: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 10000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 10000000001: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 99, 98, 97, 96, 95]) == 585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 99, 98, 97, 96, 95]) == 585: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [999999999, 999999999, 1]) == 1999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [999999999, 999999999, 1]) == 1999999999: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 500000000, 250000000, 125000000]) == 1750000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 500000000, 250000000, 125000000]) == 1750000001: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9999999945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9999999945: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 4000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 4000000001: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [500000000, 500000000, 1]) == 1000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [500000000, 500000000, 1]) == 1000000001: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [999999999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [999999999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 150, 200, 250]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 150, 200, 250]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 1597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 1597: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 4000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 4000000003: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [500000000, 500000000, 500000000, 500000000]) == 2000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [500000000, 500000000, 500000000, 500000000]) == 2000000000: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 2, 4, 8, 16, 32, 64]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 2, 4, 8, 16, 32, 64]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == 46365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == 46365: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333]) == 3333333330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333]) == 3333333330: {e}')
    
    total += 1
    try:
        result = candidate(milestones = [100, 1, 100, 1, 100, 1]) == 303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(milestones = [100, 1, 100, 1, 100, 1]) == 303: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(milestones = [3, 3, 3]) == 9
    assert candidate(milestones = [1, 1, 1, 1, 1]) == 5
    assert candidate(milestones = [10, 5, 1]) == 13
    assert candidate(milestones = [1000000000, 1, 1]) == 5
    assert candidate(milestones = [1, 2, 3]) == 6
    assert candidate(milestones = [5, 2, 1]) == 7
    assert candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(milestones = [1, 1, 1000000000]) == 5
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(milestones = [1]) == 1
    assert candidate(milestones = [1, 1000000000]) == 3
    assert candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30
    assert candidate(milestones = [10, 1, 1]) == 5
    assert candidate(milestones = [1, 1000000000, 1]) == 5
    assert candidate(milestones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
    assert candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 200
    assert candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
    assert candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(milestones = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 1333333333
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(milestones = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 10000
    assert candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(milestones = [1000000000, 999999999, 1, 2, 3, 4, 5]) == 2000000014
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(milestones = [100, 200, 300, 400]) == 1000
    assert candidate(milestones = [1000000000, 999999999, 888888888]) == 2888888887
    assert candidate(milestones = [1, 2, 3, 4, 5]) == 15
    assert candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 1596
    assert candidate(milestones = [500000000, 500000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000000009
    assert candidate(milestones = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000
    assert candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 100]) == 181
    assert candidate(milestones = [10, 10, 10, 10, 10]) == 50
    assert candidate(milestones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
    assert candidate(milestones = [999999999, 1, 1, 1]) == 7
    assert candidate(milestones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1]) == 3000000001
    assert candidate(milestones = [10, 20, 30, 40, 50]) == 150
    assert candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5000000001
    assert candidate(milestones = [10, 20, 30, 40, 50]) == 150
    assert candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(milestones = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 10000000001
    assert candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(milestones = [100, 99, 98, 97, 96, 95]) == 585
    assert candidate(milestones = [999999999, 999999999, 1]) == 1999999999
    assert candidate(milestones = [1000000000, 500000000, 250000000, 125000000]) == 1750000001
    assert candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767
    assert candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 90
    assert candidate(milestones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(milestones = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500
    assert candidate(milestones = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9999999945
    assert candidate(milestones = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 4000000001
    assert candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 101
    assert candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40
    assert candidate(milestones = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1]) == 35
    assert candidate(milestones = [500000000, 500000000, 1]) == 1000000001
    assert candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 80
    assert candidate(milestones = [999999999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
    assert candidate(milestones = [100, 150, 200, 250]) == 700
    assert candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(milestones = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77
    assert candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 110
    assert candidate(milestones = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 1597
    assert candidate(milestones = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 4000000003
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(milestones = [500000000, 500000000, 500000000, 500000000]) == 2000000000
    assert candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(milestones = [1, 2, 4, 8, 16, 32, 64]) == 127
    assert candidate(milestones = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == 46365
    assert candidate(milestones = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 680
    assert candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376
    assert candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 30
    assert candidate(milestones = [333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333]) == 3333333330
    assert candidate(milestones = [100, 1, 100, 1, 100, 1]) == 303


