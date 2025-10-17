def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, -1, 3, 2, -4, 0, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, 3, 2, -4, 0, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, 1, -4, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, 1, -4, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, 3, -2, 4, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, 3, -2, 4, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, 1, -4, 7, -1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, 1, -4, 7, -1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -3, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -3, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, 3, -2, 4, 0, -6, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, 3, -2, 4, 0, -6, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -1, 0, 1, -3, 3, -3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -1, 0, 1, -3, 3, -3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, -3, 2, -4, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, -3, 2, -4, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -500000, 500000, -250000, 250000, -125000, 125000, -62500, 62500, -31250, 31250]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -500000, 500000, -250000, 250000, -125000, 125000, -62500, 62500, -31250, 31250]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 1000000, -1999999, 2000000, -2999999, 3000000, -3999999, 4000000]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 1000000, -1999999, 2000000, -2999999, 3000000, -3999999, 4000000]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -500000, 500000, -250000, 250000, -125000, 125000]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -500000, 500000, -250000, 250000, -125000, 125000]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, -10, -20, -30, -40, -50, -60, -70, -80]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, -10, -20, -30, -40, -50, -60, -70, -80]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -5, -5, -5, -5, -5, 10, 10, 10, 10, 10, -10, -10, -10, -10, -10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -5, -5, -5, -5, -5, 10, 10, 10, 10, 10, -10, -10, -10, -10, -10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 4, -3, 2, -1, 1, -2, 3, -4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 4, -3, 2, -1, 1, -2, 3, -4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, -1000000, -999999, -999998, 0, 0, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, -1000000, -999999, -999998, 0, 0, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 90000, -90000, 80000, -80000, 70000, -70000, 60000, -60000, 50000, -50000, 40000, -40000, 30000, -30000, 20000, -20000, 10000, -10000]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 90000, -90000, 80000, -80000, 70000, -70000, 60000, -60000, 50000, -50000, 40000, -40000, 30000, -30000, 20000, -20000, 10000, -10000]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -999999, 1, -1, 0, 0, 0, 0, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -999999, 1, -1, 0, 0, 0, 0, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 2, 3, 4, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 2, 3, 4, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 400000, 300000, 200000, 100000, -100000, -200000, -300000, -400000, -500000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 400000, 300000, 200000, 100000, -100000, -200000, -300000, -400000, -500000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, -1000000, 999998, -999999, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, -1000000, 999998, -999999, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, -1000000, -999999, -999998, -999997, -999996]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, -1000000, -999999, -999998, -999997, -999996]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10, -6, -7, -8, -9, -10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10, -6, -7, -8, -9, -10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, -15000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, -15000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, -1000000, -1000000, -1000000, -1000000]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, -1000000, -1000000, -1000000, -1000000]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, -60, 40, 50, -70, 60, 70, 80, 90, -450]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, -60, 40, 50, -70, 60, 70, 80, 90, -450]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, -1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, -1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -1, 999998, -2, 999997, -3, 999996, -4, 999995, -5, 999994, -6, 999993, -7, 999992, -8]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -1, 999998, -2, 999997, -3, 999996, -4, 999995, -5, 999994, -6, 999993, -7, 999992, -8]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, -100, -200, -300, -400, -500, -600, -700, -800, -900]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, -100, -200, -300, -400, -500, -600, -700, -800, -900]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, 1000000, -2000000, 2000000, -3000000, 3000000, -1500000, 1500000]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, 1000000, -2000000, 2000000, -3000000, 3000000, -1500000, 1500000]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -15, 10, -20, 25, -30]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -15, 10, -20, 25, -30]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -999999, -999998, 1000000, 999999, 999998, 0, 0, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -999999, -999998, 1000000, 999999, 999998, 0, 0, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 0, 0, 0, 0, 0]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 0, 0, 0, 0, 0]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -1000000, -1000000, 1000000, 1000000, 1000000, 1000000]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -1000000, -1000000, 1000000, 1000000, 1000000, 1000000]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, -1000000, -2000000, -3000000, 1500000, -1500000]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, -1000000, -2000000, -3000000, 1500000, -1500000]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 1, -999999, -1, 999999, -999999]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 1, -999999, -1, 999999, -999999]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-500000, -400000, -300000, -200000, -100000, 100000, 200000, 300000, 400000, 500000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-500000, -400000, -300000, -200000, -100000, 100000, 200000, 300000, 400000, 500000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -50000, 50000, -10000, 20000, -5000, 3000, 1000, -1000, 500, 50, 5, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -50000, 50000, -10000, 20000, -5000, 3000, 1000, -1000, 500, 50, 5, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 200, -100, 300, -150, 400, -200, 500]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 200, -100, 300, -150, 400, -200, 500]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 20, -10, 30, -25, 40]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 20, -10, 30, -25, 40]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, -1, 3, 2, -4, 0, 2]) == 7
    assert candidate(nums = [-1]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == 5
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [5, -2, 3, 1, -4, 7]) == 6
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 9
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [5, -1, 3, -2, 4, 0]) == 6
    assert candidate(nums = [5, -2, 3, 1, -4, 7, -1]) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [-2, -3, 0]) == 0
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [5, -1, 3, -2, 4, 0, -6, 2]) == 8
    assert candidate(nums = [2, -1, 0, 1, -3, 3, -3]) == 6
    assert candidate(nums = [-5, 1, -3, 2, -4, 0]) == 3
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == 5
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 0]) == 4
    assert candidate(nums = [1000000, -500000, 500000, -250000, 250000, -125000, 125000, -62500, 62500, -31250, 31250]) == 11
    assert candidate(nums = [999999, 1000000, -1999999, 2000000, -2999999, 3000000, -3999999, 4000000]) == 8
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10]) == 10
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600]) == 11
    assert candidate(nums = [1000000, -500000, 500000, -250000, 250000, -125000, 125000]) == 7
    assert candidate(nums = [50, 40, 30, 20, 10, -10, -20, -30, -40, -50, -60, -70, -80]) == 9
    assert candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, -5, -5, -5, -5, -5, 10, 10, 10, 10, 10, -10, -10, -10, -10, -10]) == 17
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 19
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]) == 11
    assert candidate(nums = [-5, 4, -3, 2, -1, 1, -2, 3, -4, 5]) == 9
    assert candidate(nums = [1000000, 999999, 999998, -1000000, -999999, -999998, 0, 0, 0]) == 8
    assert candidate(nums = [100000, -100000, 90000, -90000, 80000, -80000, 70000, -70000, 60000, -60000, 50000, -50000, 40000, -40000, 30000, -30000, 20000, -20000, 10000, -10000]) == 19
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 19
    assert candidate(nums = [1000000, -999999, 1, -1, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 19
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 19
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 19
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 2, 3, 4, 5]) == 19
    assert candidate(nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == 9
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 9
    assert candidate(nums = [500000, 400000, 300000, 200000, 100000, -100000, -200000, -300000, -400000, -500000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 9
    assert candidate(nums = [1000000, 999999, -1000000, 999998, -999999, 1]) == 6
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 14
    assert candidate(nums = [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1]) == 11
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 10
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, -1000000, -999999, -999998, -999997, -999996]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10, -6, -7, -8, -9, -10]) == 19
    assert candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 15
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000]) == 9
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, -15000000]) == 5
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, -1000000, -1000000, -1000000, -1000000]) == 8
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
    assert candidate(nums = [10, 20, 30, -60, 40, 50, -70, 60, 70, 80, 90, -450]) == 11
    assert candidate(nums = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 9
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, -1]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [999999, -1, 999998, -2, 999997, -3, 999996, -4, 999995, -5, 999994, -6, 999993, -7, 999992, -8]) == 16
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, -100, -200, -300, -400, -500, -600, -700, -800, -900]) == 11
    assert candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 29
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 18
    assert candidate(nums = [-1000000, 1000000, -2000000, 2000000, -3000000, 3000000, -1500000, 1500000]) == 7
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 10, -20, 25, -30]) == 9
    assert candidate(nums = [-1000000, -999999, -999998, 1000000, 999999, 999998, 0, 0, 0]) == 8
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 0, 0, 0, 0, 0]) == 14
    assert candidate(nums = [-1000000, -1000000, -1000000, 1000000, 1000000, 1000000, 1000000]) == 7
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5]) == 20
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 16
    assert candidate(nums = [-1000000, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991]) == 0
    assert candidate(nums = [1000000, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 10
    assert candidate(nums = [1000000, 2000000, 3000000, -1000000, -2000000, -3000000, 1500000, -1500000]) == 7
    assert candidate(nums = [999999, 1, -999999, -1, 999999, -999999]) == 5
    assert candidate(nums = [-500000, -400000, -300000, -200000, -100000, 100000, 200000, 300000, 400000, 500000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
    assert candidate(nums = [-1000000, 1000000, -1000000, 1000000, -1000000, 1000000]) == 5
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 10
    assert candidate(nums = [100000, -50000, 50000, -10000, 20000, -5000, 3000, 1000, -1000, 500, 50, 5, 1]) == 13
    assert candidate(nums = [100, -50, 200, -100, 300, -150, 400, -200, 500]) == 9
    assert candidate(nums = [-1, -2, -3, -4, -5, 20, -10, 30, -25, 40]) == 10
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 9
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 15
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 19
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 0
    assert candidate(nums = [999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 10


