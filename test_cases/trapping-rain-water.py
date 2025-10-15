def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(height = [3, 1, 2, 1, 4, 3, 2, 1, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 1, 2, 1, 4, 3, 2, 1, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 1, 3, 0, 1, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 1, 3, 0, 1, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 0, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 0, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 0, 1, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 0, 1, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 1, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 1, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 4, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 4, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 1, 3, 0, 1, 1, 3, 2, 1, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 1, 3, 0, 1, 1, 3, 2, 1, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(height = [4, 2, 0, 3, 2, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [4, 2, 0, 3, 2, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 0, 2, 0, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 0, 2, 0, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 2, 0, 1, 0, 3, 1, 0, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 2, 0, 1, 0, 3, 1, 0, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 2, 0, 2, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 2, 0, 2, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 1, 3, 0, 1, 2, 1, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 1, 3, 0, 1, 2, 1, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 5, 0, 5, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 5, 0, 5, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 1, 0, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 1, 0, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 0]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 0]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 0, 10, 0, 10, 0, 10, 0, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 0, 10, 0, 10, 0, 10, 0, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 80, 60, 40, 20, 0, 20, 40, 60, 80, 100]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 80, 60, 40, 20, 0, 20, 40, 60, 80, 100]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1, 5]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1, 5]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 3, 2, 1, 2, 1, 0, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 3, 2, 1, 2, 1, 0, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(height = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 1, 0, 1, 3, 1, 0, 1, 2, 1, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 1, 0, 1, 3, 1, 0, 1, 2, 1, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 3, 2, 1, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 3, 2, 1, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 2, 1, 2, 1, 5, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 2, 1, 2, 1, 5, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 1, 0, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 1, 0, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 0, 10, 0, 10, 0, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 0, 10, 0, 10, 0, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 2, 0, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 2, 0, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 8, 5, 5, 5, 9, 8, 9, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 8, 5, 5, 5, 9, 8, 9, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 7, 8, 8, 6, 4, 3, 1, 1, 0, 1, 7, 6, 5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 7, 8, 8, 6, 4, 3, 1, 1, 0, 1, 7, 6, 5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(height = [4, 2, 0, 6, 2, 3, 8, 0, 4, 4, 1, 2, 2, 2, 3, 3, 4, 0, 1, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [4, 2, 0, 6, 2, 3, 8, 0, 4, 4, 1, 2, 2, 2, 3, 3, 4, 0, 1, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 5, 4, 3, 2, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 5, 4, 3, 2, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 1, 0, 1, 2, 1, 0, 1, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 1, 0, 1, 2, 1, 0, 1, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(height = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 1, 3, 0, 1, 2, 0, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 1, 3, 0, 1, 2, 0, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 0, 3, 0, 0, 0, 2, 0, 4, 0, 0, 1, 0, 0, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 0, 3, 0, 0, 0, 2, 0, 4, 0, 0, 1, 0, 0, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 1, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 1, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 1, 2, 1, 0, 2, 1, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 1, 2, 1, 0, 2, 1, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1, 0, 5, 0, 4]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1, 0, 5, 0, 4]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [4, 2, 0, 3, 2, 5, 0, 5, 2, 3, 0, 2, 4, 0, 5]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [4, 2, 0, 3, 2, 5, 0, 5, 2, 3, 0, 2, 4, 0, 5]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 2, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 2, 1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(height = [4, 2, 3, 0, 3, 5, 3, 2, 1, 5, 3, 0, 3, 5, 3, 0, 3, 5, 2, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [4, 2, 3, 0, 3, 5, 3, 2, 1, 5, 3, 0, 3, 5, 3, 0, 3, 5, 2, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(height = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 0, 1, 3]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 0, 1, 3]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0, 3]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0, 3]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 0, 1, 0, 2, 0, 4, 0, 3, 0, 5, 0]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 0, 1, 0, 2, 0, 4, 0, 3, 0, 5, 0]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 1, 0, 1, 3, 2, 1, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 1, 0, 1, 3, 2, 1, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 2, 1, 2, 1, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 2, 1, 2, 1, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 0, 2, 0, 2, 0, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 0, 2, 0, 2, 0, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 5]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 5]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(height = [6, 4, 2, 0, 3, 0, 1, 4, 6, 2, 3, 5, 1, 0, 5, 4, 3, 2, 1, 0]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [6, 4, 2, 0, 3, 0, 1, 4, 6, 2, 3, 5, 1, 0, 5, 4, 3, 2, 1, 0]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 0, 3, 0, 0, 5, 0, 0, 2, 4]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 0, 3, 0, 0, 5, 0, 0, 2, 4]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(height = [3, 1, 2, 1, 4, 3, 2, 1, 5]) == 11
    assert candidate(height = [3, 0, 1, 3, 0, 1, 3]) == 10
    assert candidate(height = [5, 4, 3, 2, 1]) == 0
    assert candidate(height = [1]) == 0
    assert candidate(height = [2, 0, 2]) == 2
    assert candidate(height = [0, 0, 1, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(height = [1, 1, 1, 1, 1, 1]) == 0
    assert candidate(height = [1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 1, 2]) == 12
    assert candidate(height = [1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1]) == 10
    assert candidate(height = [0, 0, 0, 0, 0]) == 0
    assert candidate(height = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0
    assert candidate(height = [0, 0, 0, 0]) == 0
    assert candidate(height = [5, 4, 1, 2]) == 1
    assert candidate(height = [3, 0, 1, 3, 0, 1, 1, 3, 2, 1, 2, 1]) == 13
    assert candidate(height = [4, 2, 0, 3, 2, 5]) == 9
    assert candidate(height = [3, 0, 0, 2, 0, 4]) == 10
    assert candidate(height = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 16
    assert candidate(height = [1, 0, 2, 0, 1, 0, 3, 1, 0, 1, 2]) == 10
    assert candidate(height = [0, 2, 0, 2, 0]) == 2
    assert candidate(height = [1, 0, 0, 0, 1]) == 3
    assert candidate(height = [3, 0, 1, 3, 0, 1, 2, 1, 2, 1]) == 9
    assert candidate(height = [0, 5, 0, 5, 0]) == 5
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert candidate(height = [1, 0, 1, 0, 1]) == 2
    assert candidate(height = [1, 2, 3, 4, 5]) == 0
    assert candidate(height = [2, 1, 0, 2]) == 3
    assert candidate(height = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 81
    assert candidate(height = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 0]) == 36
    assert candidate(height = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]) == 60
    assert candidate(height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1]) == 52
    assert candidate(height = [10, 0, 10, 0, 10, 0, 10, 0, 10]) == 40
    assert candidate(height = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(height = [100, 80, 60, 40, 20, 0, 20, 40, 60, 80, 100]) == 500
    assert candidate(height = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(height = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1]) == 12
    assert candidate(height = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(height = [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0]) == 50
    assert candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 8
    assert candidate(height = [1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1, 5]) == 21
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 3, 2, 1, 2, 1, 0, 1]) == 13
    assert candidate(height = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 19
    assert candidate(height = [0, 1, 2, 1, 0, 1, 3, 1, 0, 1, 2, 1, 0]) == 8
    assert candidate(height = [10, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 72
    assert candidate(height = [0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(height = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5]) == 35
    assert candidate(height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 3, 2, 1, 2, 1]) == 15
    assert candidate(height = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(height = [5, 2, 1, 2, 1, 5, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5]) == 43
    assert candidate(height = [2, 1, 0, 1, 2]) == 4
    assert candidate(height = [10, 0, 10, 0, 10, 0, 10]) == 30
    assert candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 9
    assert candidate(height = [1, 0, 2, 0, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 42
    assert candidate(height = [2, 8, 5, 5, 5, 9, 8, 9, 2]) == 10
    assert candidate(height = [1, 7, 8, 8, 6, 4, 3, 1, 1, 0, 1, 7, 6, 5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1]) == 40
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(height = [1, 2, 3, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1]) == 14
    assert candidate(height = [5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0]) == 18
    assert candidate(height = [4, 2, 0, 6, 2, 3, 8, 0, 4, 4, 1, 2, 2, 2, 3, 3, 4, 0, 1, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2]) == 39
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(height = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]) == 18
    assert candidate(height = [1, 2, 3, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 9
    assert candidate(height = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 23
    assert candidate(height = [0, 5, 4, 3, 2, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 37
    assert candidate(height = [2, 1, 0, 1, 2, 1, 0, 1, 2, 1]) == 8
    assert candidate(height = [0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]) == 4
    assert candidate(height = [1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0]) == 16
    assert candidate(height = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 81
    assert candidate(height = [3, 0, 1, 3, 0, 1, 2, 0, 2]) == 10
    assert candidate(height = [5, 0, 3, 0, 0, 0, 2, 0, 4, 0, 0, 1, 0, 0, 5]) == 55
    assert candidate(height = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == 12
    assert candidate(height = [0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 50
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2]) == 11
    assert candidate(height = [3, 0, 1, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 20
    assert candidate(height = [5, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5, 1, 2, 1, 2, 1, 5]) == 86
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 1, 2, 1, 0, 2, 1, 0]) == 13
    assert candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
    assert candidate(height = [0, 1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1, 0, 5, 0, 4]) == 28
    assert candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 4]) == 10
    assert candidate(height = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1]) == 30
    assert candidate(height = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 52
    assert candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 6
    assert candidate(height = [4, 2, 0, 3, 2, 5, 0, 5, 2, 3, 0, 2, 4, 0, 5]) == 33
    assert candidate(height = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 5
    assert candidate(height = [3, 2, 1, 2, 3]) == 4
    assert candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 7
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 35
    assert candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 9
    assert candidate(height = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 12
    assert candidate(height = [4, 2, 3, 0, 3, 5, 3, 2, 1, 5, 3, 0, 3, 5, 3, 0, 3, 5, 2, 1]) == 35
    assert candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
    assert candidate(height = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 36
    assert candidate(height = [3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 6
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 0, 1, 3]) == 19
    assert candidate(height = [1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1]) == 12
    assert candidate(height = [1, 2, 3, 0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0, 3]) == 24
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]) == 49
    assert candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(height = [3, 0, 1, 0, 2, 0, 4, 0, 3, 0, 5, 0]) == 21
    assert candidate(height = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 35
    assert candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 3, 2, 1, 2, 1]) == 15
    assert candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
    assert candidate(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 1, 0, 1, 3, 2, 1, 2, 1]) == 22
    assert candidate(height = [2, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 13
    assert candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 6
    assert candidate(height = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 60
    assert candidate(height = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1]) == 8
    assert candidate(height = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]) == 12
    assert candidate(height = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 4
    assert candidate(height = [5, 2, 1, 2, 1, 5]) == 14
    assert candidate(height = [0, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 7
    assert candidate(height = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(height = [2, 0, 2, 0, 2, 0, 2]) == 6
    assert candidate(height = [0, 1, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 7
    assert candidate(height = [0, 2, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2, 0]) == 11
    assert candidate(height = [5, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 5]) == 36
    assert candidate(height = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]) == 0
    assert candidate(height = [6, 4, 2, 0, 3, 0, 1, 4, 6, 2, 3, 5, 1, 0, 5, 4, 3, 2, 1, 0]) == 42
    assert candidate(height = [5, 0, 3, 0, 0, 5, 0, 0, 2, 4]) == 27
    assert candidate(height = [3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1]) == 16
    assert candidate(height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23
    assert candidate(height = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0


