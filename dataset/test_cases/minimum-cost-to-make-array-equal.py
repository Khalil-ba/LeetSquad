def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [6, 1, 3, 9, 3],cost = [2, 1, 2, 1, 2]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 1, 3, 9, 3],cost = [2, 1, 2, 1, 2]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 2],cost = [2, 3, 1, 14]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 2],cost = [2, 3, 1, 14]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2],cost = [4, 2, 8, 1, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2],cost = [4, 2, 8, 1, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 1, 9],cost = [2, 5, 7]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 1, 9],cost = [2, 5, 7]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],cost = [1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],cost = [1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10],cost = [1, 100, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10],cost = [1, 100, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 1, 9, 8, 2],cost = [4, 2, 8, 1, 3]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 1, 9, 8, 2],cost = [4, 2, 8, 1, 3]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000],cost = [1000000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000],cost = [1000000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],cost = [10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],cost = [10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],cost = [1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],cost = [1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15],cost = [1, 10, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15],cost = [1, 10, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],cost = [9, 3, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],cost = [9, 3, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 1000000],cost = [100, 1]) == 900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 1000000],cost = [100, 1]) == 900000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000],cost = [1000000, 1000000, 1000000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000],cost = [1000000, 1000000, 1000000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],cost = [5, 4, 3, 2, 1]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],cost = [5, 4, 3, 2, 1]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7],cost = [100, 200, 300, 400, 500, 600]) == 3900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7],cost = [100, 200, 300, 400, 500, 600]) == 3900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 4, 7, 3],cost = [100, 10, 1000, 10000, 100000]) == 41620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 4, 7, 3],cost = [100, 10, 1000, 10000, 100000]) == 41620: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 9],cost = [10, 20, 30, 40, 50]) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 9],cost = [10, 20, 30, 40, 50]) == 460: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],cost = [1000000, 1000000, 1000000, 1000000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],cost = [1000000, 1000000, 1000000, 1000000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],cost = [1, 2, 3, 4, 5, 6]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],cost = [1, 2, 3, 4, 5, 6]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],cost = [3, 2, 1, 1, 2, 3, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],cost = [3, 2, 1, 1, 2, 3, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20],cost = [5, 1, 10, 1, 5]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20],cost = [5, 1, 10, 1, 5]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],cost = [1, 1, 1, 1, 1000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],cost = [1, 1, 1, 1, 1000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000],cost = [5, 5, 5, 5, 5]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000],cost = [5, 5, 5, 5, 5]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 7, 9, 11],cost = [1, 10, 100, 1000, 10000]) == 2470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 7, 9, 11],cost = [1, 10, 100, 1000, 10000]) == 2470: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],cost = [1000000, 1000000, 1000000, 1000000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],cost = [1000000, 1000000, 1000000, 1000000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 50000, 50000, 50000, 50000],cost = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 50000, 50000, 50000, 50000],cost = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],cost = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],cost = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 49999750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 49999750: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 4, 6, 2],cost = [5, 3, 8, 6, 7]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 4, 6, 2],cost = [5, 3, 8, 6, 7]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 390: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 112000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 112000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000],cost = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000],cost = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],cost = [1, 2, 3, 4, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],cost = [1, 2, 3, 4, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],cost = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],cost = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000],cost = [999, 888, 777, 666, 555]) == 4662000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000],cost = [999, 888, 777, 666, 555]) == 4662000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],cost = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 11200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],cost = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 11200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 1000000, 999998],cost = [10, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 1000000, 999998],cost = [10, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300],cost = [1, 2, 3, 4, 5]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300],cost = [1, 2, 3, 4, 5]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 5],cost = [1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 5],cost = [1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],cost = [1, 2, 3, 4, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],cost = [1, 2, 3, 4, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2],cost = [5, 10, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2],cost = [5, 10, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5],cost = [1, 1000, 1000, 100, 1, 1]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5],cost = [1, 1000, 1000, 100, 1, 1]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 7],cost = [2, 5, 3, 7, 4]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 7],cost = [2, 5, 3, 7, 4]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 112000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 112000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 2, 4],cost = [2, 3, 1, 14, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 2, 4],cost = [2, 3, 1, 14, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 5, 3, 7, 6],cost = [10, 1, 5, 2, 8, 3]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 5, 3, 7, 6],cost = [10, 1, 5, 2, 8, 3]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2767: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],cost = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],cost = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 123456, 123456, 123456],cost = [100000, 200000, 300000, 400000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 123456, 123456, 123456],cost = [100000, 200000, 300000, 400000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],cost = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],cost = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100000, 50000, 75000, 25000],cost = [1000, 1, 100, 10, 100]) == 8349789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100000, 50000, 75000, 25000],cost = [1000, 1, 100, 10, 100]) == 8349789: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000, 500000],cost = [1000000, 1, 1]) == 1499998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000, 500000],cost = [1000000, 1, 1]) == 1499998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7],cost = [1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7],cost = [1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],cost = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 101009989899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],cost = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 101009989899: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],cost = [10, 20, 30, 40, 50]) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],cost = [10, 20, 30, 40, 50]) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 25000, 12500, 6250],cost = [1, 2, 4, 8, 16]) == 306250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 25000, 12500, 6250],cost = [1, 2, 4, 8, 16]) == 306250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 3, 10, 8],cost = [1, 5, 7, 2, 6]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 3, 10, 8],cost = [1, 5, 7, 2, 6]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 1000000, 1, 1000000],cost = [1, 1000000, 1, 1000000, 1]) == 2999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 1000000, 1, 1000000],cost = [1, 1000000, 1, 1000000, 1]) == 2999997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 10, 1],cost = [1, 2, 3, 4, 5]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 10, 1],cost = [1, 2, 3, 4, 5]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 111111, 222222, 333333],cost = [1000, 2000, 3000, 4000, 5000]) == 1851852000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 111111, 222222, 333333],cost = [1000, 2000, 3000, 4000, 5000]) == 1851852000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],cost = [10, 20, 30, 40, 50]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],cost = [10, 20, 30, 40, 50]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 448: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17],cost = [10, 20, 30, 40, 50]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17],cost = [10, 20, 30, 40, 50]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],cost = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],cost = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000],cost = [100000, 1]) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000],cost = [100000, 1]) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],cost = [10000, 1000, 100, 10, 1]) == 38889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],cost = [10000, 1000, 100, 10, 1]) == 38889: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [6, 1, 3, 9, 3],cost = [2, 1, 2, 1, 2]) == 14
    assert candidate(nums = [1, 3, 5, 2],cost = [2, 3, 1, 14]) == 8
    assert candidate(nums = [2, 2, 2, 2, 2],cost = [4, 2, 8, 1, 3]) == 0
    assert candidate(nums = [6, 1, 9],cost = [2, 5, 7]) == 46
    assert candidate(nums = [1, 2, 3],cost = [1, 2, 3]) == 4
    assert candidate(nums = [10, 1, 10],cost = [1, 100, 1]) == 18
    assert candidate(nums = [6, 1, 9, 8, 2],cost = [4, 2, 8, 1, 3]) == 48
    assert candidate(nums = [100000, 100000],cost = [1000000, 1000000]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],cost = [10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [1, 2, 3],cost = [1, 1, 1]) == 2
    assert candidate(nums = [10, 5, 15],cost = [1, 10, 1]) == 15
    assert candidate(nums = [1, 2, 3],cost = [9, 3, 5]) == 13
    assert candidate(nums = [100000, 1000000],cost = [100, 1]) == 900000
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000],cost = [1000000, 1000000, 1000000, 1000000]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],cost = [5, 4, 3, 2, 1]) == 1500
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7],cost = [100, 200, 300, 400, 500, 600]) == 3900
    assert candidate(nums = [9, 1, 4, 7, 3],cost = [100, 10, 1000, 10000, 100000]) == 41620
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 82
    assert candidate(nums = [5, 3, 8, 1, 9],cost = [10, 20, 30, 40, 50]) == 460
    assert candidate(nums = [5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [5, 5, 5, 5, 5],cost = [1000000, 1000000, 1000000, 1000000, 1000000]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 250
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995],cost = [1, 2, 3, 4, 5, 6]) == 26
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],cost = [3, 2, 1, 1, 2, 3, 3, 2, 1]) == 12
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
    assert candidate(nums = [1, 5, 10, 15, 20],cost = [5, 1, 10, 1, 5]) == 105
    assert candidate(nums = [1, 2, 3, 4, 5],cost = [1, 1, 1, 1, 1000000]) == 10
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],cost = [5, 5, 5, 5, 5]) == 30000
    assert candidate(nums = [1, 5, 7, 9, 11],cost = [1, 10, 100, 1000, 10000]) == 2470
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29
    assert candidate(nums = [1, 1, 1, 1, 1],cost = [1000000, 1000000, 1000000, 1000000, 1000000]) == 0
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000],cost = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],cost = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 49999750
    assert candidate(nums = [9, 1, 4, 6, 2],cost = [5, 3, 8, 6, 7]) == 60
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 390
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 112000
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000],cost = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9],cost = [1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],cost = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5600
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 102
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],cost = [999, 888, 777, 666, 555]) == 4662000
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],cost = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 11200
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 12
    assert candidate(nums = [999999, 1000000, 999998],cost = [10, 1, 1]) == 2
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [100, 150, 200, 250, 300],cost = [1, 2, 3, 4, 5]) == 750
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5],cost = [1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(nums = [50, 40, 30, 20, 10],cost = [1, 2, 3, 4, 5]) == 150
    assert candidate(nums = [10, 20, 30, 40, 50],cost = [1, 2, 3, 4, 5]) == 150
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1],cost = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [3, 1, 2],cost = [5, 10, 15]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 200
    assert candidate(nums = [1, 2, 2, 3, 4, 5],cost = [1, 1000, 1000, 100, 1, 1]) == 106
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 2500
    assert candidate(nums = [5, 3, 8, 6, 7],cost = [2, 5, 3, 7, 4]) == 27
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1120
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 112000
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(nums = [1, 3, 5, 2, 4],cost = [2, 3, 1, 14, 5]) == 18
    assert candidate(nums = [9, 1, 5, 3, 7, 6],cost = [10, 1, 5, 2, 8, 3]) == 47
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2767
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],cost = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 840
    assert candidate(nums = [123456, 123456, 123456, 123456],cost = [100000, 200000, 300000, 400000]) == 0
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],cost = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]) == 40
    assert candidate(nums = [1, 100000, 50000, 75000, 25000],cost = [1000, 1, 100, 10, 100]) == 8349789
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000]) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 720
    assert candidate(nums = [1, 1000000, 500000],cost = [1000000, 1, 1]) == 1499998
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1120
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 840
    assert candidate(nums = [7, 7, 7, 7, 7, 7],cost = [1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],cost = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 101009989899
    assert candidate(nums = [10, 10, 10, 10, 10, 10],cost = [1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(nums = [100, 200, 300, 400, 500],cost = [10, 20, 30, 40, 50]) == 15000
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250],cost = [1, 2, 4, 8, 16]) == 306250
    assert candidate(nums = [5, 7, 3, 10, 8],cost = [1, 5, 7, 2, 6]) == 42
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11200
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(nums = [1000000, 1, 1000000, 1, 1000000],cost = [1, 1000000, 1, 1000000, 1]) == 2999997
    assert candidate(nums = [5, 3, 8, 10, 1],cost = [1, 2, 3, 4, 5]) == 53
    assert candidate(nums = [123456, 654321, 111111, 222222, 333333],cost = [1000, 2000, 3000, 4000, 5000]) == 1851852000
    assert candidate(nums = [10, 20, 30, 40, 50],cost = [10, 20, 30, 40, 50]) == 1500
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 448
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112
    assert candidate(nums = [1, 5, 9, 13, 17],cost = [10, 20, 30, 40, 50]) == 600
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],cost = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(nums = [1, 1000000],cost = [100000, 1]) == 999999
    assert candidate(nums = [1, 10, 100, 1000, 10000],cost = [10000, 1000, 100, 10, 1]) == 38889


