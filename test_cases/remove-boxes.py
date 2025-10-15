def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 5]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 5]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 3, 2, 2, 3, 3, 3]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 3, 2, 2, 3, 3, 3]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [2, 1, 2, 1, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [2, 1, 2, 1, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 1, 1, 1, 2, 2, 3, 3, 3, 3]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 1, 1, 1, 2, 2, 3, 3, 3, 3]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [100, 100, 100, 99, 99, 98, 98, 98, 98]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [100, 100, 100, 99, 99, 98, 98, 98, 98]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 1, 2, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 1, 2, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 10, 10, 1, 1, 1, 10, 10, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 10, 10, 1, 1, 1, 10, 10, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3249: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 4, 4]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 4, 4]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1]) == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1]) == 131: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 2, 1, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 2, 1, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 2, 2, 1, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 1, 6, 6, 6, 6, 6, 6, 1]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 2, 2, 1, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 1, 6, 6, 6, 6, 6, 6, 1]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [18, 19, 20, 21, 22, 22, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 26, 26]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [18, 19, 20, 21, 22, 22, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 26, 26]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19]) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19]) == 142: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 2]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 2]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 9, 9]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 9, 9]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [9, 9, 9, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [9, 9, 9, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26]) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26]) == 243: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 142: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4, 5, 5, 4, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4, 5, 5, 4, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 1]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 1]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]) == 324: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(boxes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(boxes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 37: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 54
    assert candidate(boxes = [1, 1, 2, 2, 1, 1]) == 20
    assert candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 5]) == 34
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 36
    assert candidate(boxes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 30
    assert candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 23
    assert candidate(boxes = [1, 2, 3, 4, 5]) == 5
    assert candidate(boxes = [1, 1, 2, 3, 2, 2, 3, 3, 3]) == 25
    assert candidate(boxes = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 20
    assert candidate(boxes = [2, 1, 2, 1, 2]) == 11
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 30
    assert candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(boxes = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 42
    assert candidate(boxes = [1, 1, 1]) == 9
    assert candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 20
    assert candidate(boxes = [5, 5, 5, 5, 1, 1, 1, 2, 2, 3, 3, 3, 3]) == 45
    assert candidate(boxes = [5, 5, 5, 5, 5]) == 25
    assert candidate(boxes = [100, 100, 100, 99, 99, 98, 98, 98, 98]) == 29
    assert candidate(boxes = [1, 2, 2, 1, 2, 2, 1]) == 21
    assert candidate(boxes = [1]) == 1
    assert candidate(boxes = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 27
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(boxes = [10, 10, 10, 1, 1, 1, 10, 10, 10]) == 45
    assert candidate(boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
    assert candidate(boxes = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 17
    assert candidate(boxes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(boxes = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]) == 43
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 80
    assert candidate(boxes = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1]) == 74
    assert candidate(boxes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 32
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3]) == 76
    assert candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8]) == 168
    assert candidate(boxes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 62
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 40
    assert candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 64
    assert candidate(boxes = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 40
    assert candidate(boxes = [27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31]) == 95
    assert candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 39
    assert candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3249
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51
    assert candidate(boxes = [9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12]) == 106
    assert candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8]) == 64
    assert candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 400
    assert candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 256
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 63
    assert candidate(boxes = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 135
    assert candidate(boxes = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 76
    assert candidate(boxes = [1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3]) == 110
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 43
    assert candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 40
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 4, 4]) == 57
    assert candidate(boxes = [1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1]) == 131
    assert candidate(boxes = [1, 2, 3, 2, 1, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 66
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(boxes = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 40
    assert candidate(boxes = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 37
    assert candidate(boxes = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 49
    assert candidate(boxes = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 78
    assert candidate(boxes = [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8]) == 77
    assert candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 144
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 92
    assert candidate(boxes = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1]) == 57
    assert candidate(boxes = [9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15]) == 92
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 125
    assert candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 324
    assert candidate(boxes = [1, 2, 2, 1, 3, 3, 3, 2, 2, 1, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 1, 6, 6, 6, 6, 6, 6, 1]) == 130
    assert candidate(boxes = [13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17]) == 90
    assert candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 83
    assert candidate(boxes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 75
    assert candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 625
    assert candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 36
    assert candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1]) == 48
    assert candidate(boxes = [18, 19, 20, 21, 22, 22, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 26, 26]) == 62
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 37
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 99
    assert candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]) == 96
    assert candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 110
    assert candidate(boxes = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == 40
    assert candidate(boxes = [16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19]) == 142
    assert candidate(boxes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 85
    assert candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 87
    assert candidate(boxes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 110
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 2]) == 51
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]) == 27
    assert candidate(boxes = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 275
    assert candidate(boxes = [9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 9, 9]) == 57
    assert candidate(boxes = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45
    assert candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 250
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 84
    assert candidate(boxes = [4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1]) == 59
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 55
    assert candidate(boxes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1024
    assert candidate(boxes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 400
    assert candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 48
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2]) == 44
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200
    assert candidate(boxes = [20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23]) == 151
    assert candidate(boxes = [9, 9, 9, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5]) == 63
    assert candidate(boxes = [24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26]) == 243
    assert candidate(boxes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 40
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]) == 142
    assert candidate(boxes = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 62
    assert candidate(boxes = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 74
    assert candidate(boxes = [1, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3]) == 104
    assert candidate(boxes = [1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2]) == 64
    assert candidate(boxes = [1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3]) == 156
    assert candidate(boxes = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 189
    assert candidate(boxes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(boxes = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 54
    assert candidate(boxes = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 80
    assert candidate(boxes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]) == 41
    assert candidate(boxes = [1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1]) == 155
    assert candidate(boxes = [1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4, 5, 5, 4, 5]) == 45
    assert candidate(boxes = [1, 2, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 1]) == 59
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(boxes = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 57
    assert candidate(boxes = [5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 61
    assert candidate(boxes = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 84
    assert candidate(boxes = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]) == 324
    assert candidate(boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
    assert candidate(boxes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 37


