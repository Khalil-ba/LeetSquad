def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(ratings = [50, 40, 30, 20, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [50, 40, 30, 20, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 4, 5, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 4, 5, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 20, 30, 40, 50, 45, 35, 25, 15, 5]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 20, 30, 40, 50, 45, 35, 25, 15, 5]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 2, 3, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 2, 3, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 4, 3, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 4, 3, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 6, 10, 8, 7, 3, 2]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 6, 10, 8, 7, 3, 2]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 20, 30, 40, 50]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 20, 30, 40, 50]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 4, 5, 6]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 4, 5, 6]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 20, 15, 10, 15, 20, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 20, 15, 10, 15, 20, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 0, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 0, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 3, 4, 5, 5, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 3, 4, 5, 5, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 6, 10, 8, 7, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 6, 10, 8, 7, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 2, 1, 2, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 2, 1, 2, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 2, 2, 3, 2, 2, 1, 2, 2, 3, 2, 2, 1, 2, 2]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 2, 2, 3, 2, 2, 1, 2, 2, 3, 2, 2, 1, 2, 2]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 10, 10, 10, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 10, 10, 10, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 8]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 8]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 259
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 259: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 3, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 4, 3, 2, 1]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 3, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 4, 3, 2, 1]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 20, 10, 50, 20, 30, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 20, 10, 50, 20, 30, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 154: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 3, 8, 6, 7, 2, 4, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 3, 8, 6, 7, 2, 4, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 3, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 3, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [20, 19, 20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [20, 19, 20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 193: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 2, 3, 1, 4, 6, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 2, 3, 1, 4, 6, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 3, 4, 4, 3, 2, 1, 1, 2, 3, 3, 4, 4]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 3, 4, 4, 3, 2, 1, 1, 2, 3, 3, 4, 4]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 3, 3, 2, 1, 2, 3, 3, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 3, 3, 2, 1, 2, 3, 3, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 3, 8, 6, 7, 2, 4, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 3, 8, 6, 7, 2, 4, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 2, 1, 4, 3, 5, 4, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 2, 1, 4, 3, 5, 4, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 3, 3, 2, 1, 2, 3, 4, 4, 3, 2, 1]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 3, 3, 2, 1, 2, 3, 4, 4, 3, 2, 1]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [7, 3, 5, 4, 6, 5, 4, 3, 5, 6, 7]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [7, 3, 5, 4, 6, 5, 4, 3, 5, 6, 7]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 2, 3, 1, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 2, 3, 1, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 3, 8, 6, 7, 9, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 3, 8, 6, 7, 9, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 2, 3, 4, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 2, 3, 4, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [10, 20, 15, 10, 5, 10, 20, 30, 25, 20, 15, 10, 5]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [10, 20, 15, 10, 5, 10, 20, 30, 25, 20, 15, 10, 5]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 7, 8, 9]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 7, 8, 9]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 3, 2, 3, 1, 5, 2, 4, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 3, 2, 3, 1, 5, 2, 4, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 3, 4, 2, 1, 6, 7, 8, 9, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 3, 4, 2, 1, 6, 7, 8, 9, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [5, 3, 1, 2, 5, 4, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [5, 3, 1, 2, 5, 4, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 207: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(ratings = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ratings = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(ratings = [50, 40, 30, 20, 10]) == 15
    assert candidate(ratings = [1]) == 1
    assert candidate(ratings = [1, 3, 4, 5, 2]) == 11
    assert candidate(ratings = [1, 1, 1, 1]) == 4
    assert candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 24
    assert candidate(ratings = [5, 4, 3, 2, 1]) == 15
    assert candidate(ratings = [10, 20, 30, 40, 50, 45, 35, 25, 15, 5]) == 31
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 66
    assert candidate(ratings = [1, 3, 2, 2, 3, 1]) == 8
    assert candidate(ratings = [1, 3, 4, 3, 2]) == 9
    assert candidate(ratings = [1, 6, 10, 8, 7, 3, 2]) == 18
    assert candidate(ratings = [10, 20, 30, 40, 50]) == 15
    assert candidate(ratings = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 22
    assert candidate(ratings = [1, 1, 1, 1, 1]) == 5
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(ratings = [1, 3, 2, 4, 5, 6]) == 13
    assert candidate(ratings = [1, 2, 2]) == 4
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(ratings = [1, 3, 2, 2, 1]) == 7
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(ratings = [10, 20, 15, 10, 15, 20, 10]) == 13
    assert candidate(ratings = [1, 2, 3, 4, 5]) == 15
    assert candidate(ratings = [1, 0, 2]) == 5
    assert candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 31
    assert candidate(ratings = [1, 2, 2, 3, 3, 4, 5, 5, 6]) == 15
    assert candidate(ratings = [1, 6, 10, 8, 7, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 123
    assert candidate(ratings = [1, 2, 2, 2, 1, 2, 3, 2, 1]) == 15
    assert candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 16
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 66
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109
    assert candidate(ratings = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(ratings = [1, 2, 2, 3, 2, 2, 3, 2, 2, 1, 2, 2, 3, 2, 2, 1, 2, 2]) == 26
    assert candidate(ratings = [10, 10, 10, 10, 10]) == 5
    assert candidate(ratings = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 8]) == 31
    assert candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 48
    assert candidate(ratings = [1, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 84
    assert candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(ratings = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 259
    assert candidate(ratings = [1, 2, 2, 2, 1]) == 7
    assert candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 47
    assert candidate(ratings = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 33
    assert candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 28
    assert candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 3, 2, 1]) == 23
    assert candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 124
    assert candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(ratings = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 45
    assert candidate(ratings = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 60
    assert candidate(ratings = [1, 3, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 57
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(ratings = [3, 3, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 4, 3, 2, 1]) == 37
    assert candidate(ratings = [10, 20, 10, 50, 20, 30, 10]) == 10
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 154
    assert candidate(ratings = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(ratings = [5, 3, 8, 6, 7, 2, 4, 1]) == 12
    assert candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]) == 66
    assert candidate(ratings = [1, 2, 2, 3, 3, 3, 2, 1]) == 13
    assert candidate(ratings = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 20
    assert candidate(ratings = [20, 19, 20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 193
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 41
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 90
    assert candidate(ratings = [5, 2, 3, 1, 4, 6, 1]) == 12
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 69
    assert candidate(ratings = [1, 2, 2, 3, 3, 4, 4, 3, 2, 1, 1, 2, 3, 3, 4, 4]) == 29
    assert candidate(ratings = [3, 3, 3, 2, 1, 2, 3, 3, 3]) == 15
    assert candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7]) == 33
    assert candidate(ratings = [5, 3, 8, 6, 7, 2, 4, 1]) == 12
    assert candidate(ratings = [1, 3, 2, 2, 3, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 43
    assert candidate(ratings = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 46
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(ratings = [3, 2, 1, 4, 3, 5, 4, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 66
    assert candidate(ratings = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 22
    assert candidate(ratings = [1, 2, 2, 3, 3, 3, 2, 1, 2, 3, 4, 4, 3, 2, 1]) == 32
    assert candidate(ratings = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
    assert candidate(ratings = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 28
    assert candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49
    assert candidate(ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225
    assert candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(ratings = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 21
    assert candidate(ratings = [7, 3, 5, 4, 6, 5, 4, 3, 5, 6, 7]) == 25
    assert candidate(ratings = [1, 3, 2, 2, 3, 1, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
    assert candidate(ratings = [5, 3, 8, 6, 7, 9, 2]) == 12
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 400
    assert candidate(ratings = [1, 2, 2, 2, 3, 4, 4, 3, 2, 1]) == 20
    assert candidate(ratings = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 38
    assert candidate(ratings = [10, 20, 15, 10, 5, 10, 20, 30, 25, 20, 15, 10, 5]) == 37
    assert candidate(ratings = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 28
    assert candidate(ratings = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 7, 8, 9]) == 56
    assert candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 38
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(ratings = [3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 41
    assert candidate(ratings = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 106
    assert candidate(ratings = [1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4]) == 34
    assert candidate(ratings = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]) == 16
    assert candidate(ratings = [1, 3, 2, 3, 1, 5, 2, 4, 1]) == 13
    assert candidate(ratings = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21
    assert candidate(ratings = [5, 3, 4, 2, 1, 6, 7, 8, 9, 1]) == 24
    assert candidate(ratings = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 15
    assert candidate(ratings = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10
    assert candidate(ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 56
    assert candidate(ratings = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 60
    assert candidate(ratings = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 26
    assert candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 29
    assert candidate(ratings = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 29
    assert candidate(ratings = [5, 3, 1, 2, 5, 4, 3, 2, 1]) == 23
    assert candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 48
    assert candidate(ratings = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 207
    assert candidate(ratings = [3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == 32
    assert candidate(ratings = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(ratings = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 12


