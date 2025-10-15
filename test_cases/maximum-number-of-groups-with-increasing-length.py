def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1000000000, 1000000000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1000000000, 1000000000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1000000000, 1, 1000000000, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1000000000, 1, 1000000000, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [3, 3, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [3, 3, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [20, 1, 20, 2, 20, 3, 20, 4, 20, 5, 20, 6, 20, 7, 20, 8, 20, 9, 20, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [20, 1, 20, 2, 20, 3, 20, 4, 20, 5, 20, 6, 20, 7, 20, 8, 20, 9, 20, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 3, 6, 10, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 3, 6, 10, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [15, 10, 6, 3, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [15, 10, 6, 3, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 10, 10, 10, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 10, 10, 10, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [100, 50, 25, 12, 6, 3, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [100, 50, 25, 12, 6, 3, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 2, 3, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 2, 3, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 2, 4, 1, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 2, 4, 1, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [100, 50, 25, 10, 5, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [100, 50, 25, 10, 5, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [20, 10, 30, 5, 15, 25, 5, 35, 40, 10, 5, 15, 20, 5, 25, 30, 5, 40, 5, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [20, 10, 30, 5, 15, 25, 5, 35, 40, 10, 5, 15, 20, 5, 25, 30, 5, 40, 5, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [10, 10, 10, 10, 10, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [10, 10, 10, 10, 10, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(usageLimits = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(usageLimits = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(usageLimits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(usageLimits = [1000000000, 1000000000, 1000000000]) == 3
    assert candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
    assert candidate(usageLimits = [1, 2, 5]) == 3
    assert candidate(usageLimits = [1, 2, 3, 4, 5]) == 5
    assert candidate(usageLimits = [3, 3, 3]) == 3
    assert candidate(usageLimits = [1, 1]) == 1
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(usageLimits = [1]) == 1
    assert candidate(usageLimits = [1, 1000000000, 1, 1000000000, 1]) == 4
    assert candidate(usageLimits = [3, 3, 3, 3]) == 4
    assert candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5
    assert candidate(usageLimits = [2, 1, 2]) == 2
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 5
    assert candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
    assert candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 19
    assert candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 14
    assert candidate(usageLimits = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(usageLimits = [20, 1, 20, 2, 20, 3, 20, 4, 20, 5, 20, 6, 20, 7, 20, 8, 20, 9, 20, 10]) == 20
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(usageLimits = [1, 3, 6, 10, 15]) == 5
    assert candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 20
    assert candidate(usageLimits = [5, 3, 2, 1]) == 4
    assert candidate(usageLimits = [15, 10, 6, 3, 1]) == 5
    assert candidate(usageLimits = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 10
    assert candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(usageLimits = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(usageLimits = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 15
    assert candidate(usageLimits = [10, 10, 10, 10, 10]) == 5
    assert candidate(usageLimits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10
    assert candidate(usageLimits = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 10
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(usageLimits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(usageLimits = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == 6
    assert candidate(usageLimits = [100, 50, 25, 12, 6, 3, 1]) == 7
    assert candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 20
    assert candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7
    assert candidate(usageLimits = [5, 4, 3, 2, 1]) == 5
    assert candidate(usageLimits = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
    assert candidate(usageLimits = [1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5
    assert candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10
    assert candidate(usageLimits = [1, 2, 2, 3, 3, 3]) == 4
    assert candidate(usageLimits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 16
    assert candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(usageLimits = [1000000000, 1000000000, 1000000000, 1000000000]) == 4
    assert candidate(usageLimits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 4
    assert candidate(usageLimits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(usageLimits = [5, 2, 4, 1, 3]) == 5
    assert candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(usageLimits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 10
    assert candidate(usageLimits = [5, 4, 3, 2, 1]) == 5
    assert candidate(usageLimits = [100, 50, 25, 10, 5, 1]) == 6
    assert candidate(usageLimits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5
    assert candidate(usageLimits = [1, 2, 3, 4, 5]) == 5
    assert candidate(usageLimits = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == 10
    assert candidate(usageLimits = [20, 10, 30, 5, 15, 25, 5, 35, 40, 10, 5, 15, 20, 5, 25, 30, 5, 40, 5, 10]) == 20
    assert candidate(usageLimits = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 7
    assert candidate(usageLimits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(usageLimits = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 14
    assert candidate(usageLimits = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10
    assert candidate(usageLimits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 7
    assert candidate(usageLimits = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11
    assert candidate(usageLimits = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(usageLimits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(usageLimits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(usageLimits = [10, 10, 10, 10, 10, 10]) == 6
    assert candidate(usageLimits = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 15


