def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 4, 5, 6],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 4, 5, 6],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 4],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 4],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1, 3],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1, 3],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 3, 4],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 3, 4],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 3],k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 3],k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 2, 3, 1, 2, 3],k = 3) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 2, 3, 1, 2, 3],k = 3) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],k = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],k = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 253: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9],k = 5) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9],k = 5) == 143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 1, 4, 2],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 1, 4, 2],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],k = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],k = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 66: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 237: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],k = 2) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],k = 2) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20],k = 10) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20],k = 10) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 4],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 4],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 2, 3, 1, 4],k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 2, 3, 1, 4],k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 2, 1, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 2, 1, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 2, 3, 3, 4, 4, 4, 4, 4],k = 3) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 2, 3, 3, 4, 4, 4, 4, 4],k = 3) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],k = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],k = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 4, 3, 2, 1],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 4, 3, 2, 1],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 20, 30, 10, 40],k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 20, 30, 10, 40],k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 7) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 7) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],k = 4) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],k = 4) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 136: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9],k = 3) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9],k = 3) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 378: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1],k = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1],k = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 253: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 136: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1, 3, 4, 3, 2, 1],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1, 3, 4, 3, 2, 1],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2],k = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2],k = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 3) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 3) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 2, 4, 5, 3],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 2, 4, 5, 3],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8],k = 3) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8],k = 3) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],k = 2) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],k = 2) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 2, 3, 1, 1, 2, 3, 3, 3, 2, 1],k = 2) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 2, 3, 1, 1, 2, 3, 3, 3, 2, 1],k = 2) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 66: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 4, 4, 2, 2, 3, 1, 1, 4],k = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 4, 4, 2, 2, 3, 1, 1, 4],k = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 93: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],k = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],k = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 3, 2, 1, 4, 4, 5, 5, 5, 5, 5],k = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 3, 2, 1, 4, 4, 5, 5, 5, 5, 5],k = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 2, 2, 3, 3],k = 4) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 2, 2, 3, 3],k = 4) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],k = 3) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],k = 3) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 5) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 5) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1],k = 3) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1],k = 3) == 162: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1],k = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1],k = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],k = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],k = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 3) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 3) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1, 5, 5, 4, 3, 2, 1, 6, 6, 5, 4, 3, 2, 1, 7, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 541
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1, 5, 5, 4, 3, 2, 1, 6, 6, 5, 4, 3, 2, 1, 7, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 541: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 2],k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 2],k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],k = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],k = 5) == 21: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [4, 2, 4, 5, 6],k = 2) == 5
    assert candidate(nums = [1, 2, 1, 3, 4],k = 3) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 55
    assert candidate(nums = [1, 2, 2, 1, 1, 3],k = 2) == 10
    assert candidate(nums = [1, 2, 3],k = 2) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6],k = 3) == 4
    assert candidate(nums = [1, 2],k = 1) == 2
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 3, 4],k = 3) == 9
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
    assert candidate(nums = [1],k = 1) == 1
    assert candidate(nums = [1, 2, 1, 2, 3],k = 2) == 7
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1) == 15
    assert candidate(nums = [1, 2, 2, 1, 1],k = 2) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 6
    assert candidate(nums = [1, 2, 2, 1, 3],k = 2) == 6
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 15
    assert candidate(nums = [1, 2, 2, 1, 2],k = 2) == 9
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],k = 2) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3],k = 2) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 55
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 1, 2, 3],k = 3) == 22
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],k = 2) == 18
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 5
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 253
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 21
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9],k = 5) == 143
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 11
    assert candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 91
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 210
    assert candidate(nums = [1, 2, 2, 1, 3, 1, 4, 2],k = 3) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 26
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],k = 2) == 13
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 3) == 18
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 19
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 35
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 66
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 237
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],k = 2) == 42
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20],k = 10) == 44
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 4],k = 2) == 9
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 2, 3, 1, 4],k = 3) == 14
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 2, 1, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 29
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 4) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 6
    assert candidate(nums = [1, 1, 2, 3, 2, 3, 3, 4, 4, 4, 4, 4],k = 3) == 23
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],k = 4) == 18
    assert candidate(nums = [1, 2, 2, 1, 3, 4, 3, 2, 1],k = 2) == 11
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 100
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 14
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 5) == 0
    assert candidate(nums = [1, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 75
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 20, 30, 10, 40],k = 3) == 14
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 7) == 24
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 16
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],k = 4) == 36
    assert candidate(nums = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 2) == 8
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 136
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 7
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9],k = 3) == 63
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 378
    assert candidate(nums = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1],k = 2) == 21
    assert candidate(nums = [1, 2, 1, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 120
    assert candidate(nums = [5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 253
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 136
    assert candidate(nums = [1, 2, 2, 1, 1, 3, 4, 3, 2, 1],k = 2) == 15
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 190
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 4) == 20
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 16
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 190
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2],k = 2) == 28
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 3) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 0
    assert candidate(nums = [1, 2, 2, 1, 3, 2, 4, 5, 3],k = 3) == 10
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8],k = 3) == 48
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],k = 2) == 36
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 1, 1, 2, 3, 3, 3, 2, 1],k = 2) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 3) == 13
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 24
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 66
    assert candidate(nums = [4, 2, 4, 4, 2, 2, 3, 1, 1, 4],k = 2) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 4) == 20
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 93
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 4) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 16
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 29
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],k = 5) == 32
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1],k = 2) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 22
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 3, 2, 1, 4, 4, 5, 5, 5, 5, 5],k = 3) == 27
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 11
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 2, 2, 3, 3],k = 4) == 72
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],k = 3) == 72
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 5) == 106
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1],k = 3) == 162
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1],k = 2) == 16
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],k = 5) == 80
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 4) == 24
    assert candidate(nums = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 6
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 3) == 36
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 45
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1, 5, 5, 4, 3, 2, 1, 6, 6, 5, 4, 3, 2, 1, 7, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 541
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 21
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 2],k = 3) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],k = 5) == 21


