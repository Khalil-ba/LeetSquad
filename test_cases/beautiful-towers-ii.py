def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 10, 10, 10, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 10, 10, 10, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 3, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 3, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 1, 2, 3, 1, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 1, 2, 3, 1, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 2, 5, 5, 2, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 2, 5, 5, 2, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [7, 8, 9, 10, 9, 8, 7]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [7, 8, 9, 10, 9, 8, 7]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 3, 4, 1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 3, 4, 1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [4, 4, 4, 4, 4, 4, 4]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [4, 4, 4, 4, 4, 4, 4]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [6, 5, 3, 9, 2, 7]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [6, 5, 3, 9, 2, 7]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 5, 5, 5, 9, 5, 5, 5, 5]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 5, 5, 5, 9, 5, 5, 5, 5]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 10, 2, 8, 3, 7, 4, 6, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 10, 2, 8, 3, 7, 4, 6, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 6, 6]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 6, 6]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 6, 7, 8, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 6, 7, 8, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 111: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 118: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 5, 4, 6, 5, 7, 6, 8]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 5, 4, 6, 5, 7, 6, 8]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 3, 3, 3, 3, 5, 5, 5, 5, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 3, 3, 3, 3, 5, 5, 5, 5, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [7, 7, 7, 7, 1, 7, 7, 7, 7, 7]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [7, 7, 7, 7, 1, 7, 7, 7, 7, 7]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 4, 4, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 4, 4, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 9, 7, 5, 3, 1]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 9, 7, 5, 3, 1]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 2, 2]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 2, 2]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 5, 5, 5, 6, 5, 5, 5, 5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 5, 5, 5, 6, 5, 5, 5, 5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 5, 5, 5, 1, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 5, 5, 5, 1, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 1, 3, 1, 3, 1, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 1, 3, 1, 3, 1, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 5, 3, 8, 7, 2, 6, 4, 9, 0]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 5, 3, 8, 7, 2, 6, 4, 9, 0]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [3, 3, 3, 3, 10, 3, 3, 3, 3, 10, 3, 3, 3, 3]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [3, 3, 3, 3, 10, 3, 3, 3, 3, 10, 3, 3, 3, 3]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 2, 3, 4, 3, 2, 3, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 2, 3, 4, 3, 2, 3, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 113: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [2, 2, 3, 4, 5, 6, 5, 5, 5, 5, 6, 7, 8, 9, 10]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [2, 2, 3, 4, 5, 6, 5, 5, 5, 5, 6, 7, 8, 9, 10]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7]) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7]) == 111: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [9, 9, 9, 9, 9, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [9, 9, 9, 9, 9, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [9, 7, 5, 3, 1, 1, 3, 5, 7, 9]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [9, 7, 5, 3, 1, 1, 3, 5, 7, 9]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [100, 50, 50, 100, 50, 50, 100, 50, 50, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [100, 50, 50, 100, 50, 50, 100, 50, 50, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000008: {e}')
    
    total += 1
    try:
        result = candidate(maxHeights = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxHeights = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1]) == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(maxHeights = [1, 2, 3, 4, 5]) == 15
    assert candidate(maxHeights = [5, 4, 3, 2, 1]) == 15
    assert candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30
    assert candidate(maxHeights = [10, 10, 10, 10, 10]) == 50
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(maxHeights = [1, 3, 2, 3, 1]) == 9
    assert candidate(maxHeights = [1, 3, 2, 1, 2, 3, 1, 2, 1]) == 12
    assert candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(maxHeights = [3, 2, 5, 5, 2, 3]) == 18
    assert candidate(maxHeights = [7, 8, 9, 10, 9, 8, 7]) == 58
    assert candidate(maxHeights = [5, 3, 4, 1, 1]) == 13
    assert candidate(maxHeights = [4, 4, 4, 4, 4, 4, 4]) == 28
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(maxHeights = [1, 1, 1, 1, 1]) == 5
    assert candidate(maxHeights = [6, 5, 3, 9, 2, 7]) == 22
    assert candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 114
    assert candidate(maxHeights = [5, 5, 5, 5, 9, 5, 5, 5, 5]) == 49
    assert candidate(maxHeights = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 70
    assert candidate(maxHeights = [1, 10, 2, 8, 3, 7, 4, 6, 5]) == 30
    assert candidate(maxHeights = [3, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 6, 6]) == 54
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 34
    assert candidate(maxHeights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40
    assert candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3]) == 44
    assert candidate(maxHeights = [5, 6, 7, 8, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]) == 114
    assert candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 26
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 46
    assert candidate(maxHeights = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 111
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 118
    assert candidate(maxHeights = [1, 3, 2, 5, 4, 6, 5, 7, 6, 8]) == 43
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 5, 5, 5, 5, 5]) == 40
    assert candidate(maxHeights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 500
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 44
    assert candidate(maxHeights = [7, 7, 7, 7, 1, 7, 7, 7, 7, 7]) == 40
    assert candidate(maxHeights = [5, 4, 4, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7]) == 85
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(maxHeights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1]) == 39
    assert candidate(maxHeights = [1, 5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 9, 7, 5, 3, 1]) == 98
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10]) == 300
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(maxHeights = [3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3]) == 68
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45
    assert candidate(maxHeights = [2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 2, 2]) == 73
    assert candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 19
    assert candidate(maxHeights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(maxHeights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250
    assert candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 65
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5]) == 69
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 3, 2, 1]) == 41
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 35
    assert candidate(maxHeights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]) == 42
    assert candidate(maxHeights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(maxHeights = [5, 5, 5, 5, 6, 5, 5, 5, 5]) == 46
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(maxHeights = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 51
    assert candidate(maxHeights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19
    assert candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 110
    assert candidate(maxHeights = [1, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 1]) == 22
    assert candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 29
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 360
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 104
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 70
    assert candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7]) == 68
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
    assert candidate(maxHeights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(maxHeights = [5, 5, 5, 5, 1, 5, 5, 5, 5]) == 25
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
    assert candidate(maxHeights = [5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]) == 90
    assert candidate(maxHeights = [3, 1, 3, 1, 3, 1, 3]) == 9
    assert candidate(maxHeights = [1, 5, 3, 8, 7, 2, 6, 4, 9, 0]) == 30
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
    assert candidate(maxHeights = [3, 3, 3, 3, 10, 3, 3, 3, 3, 10, 3, 3, 3, 3]) == 49
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 65
    assert candidate(maxHeights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650
    assert candidate(maxHeights = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 20
    assert candidate(maxHeights = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 20
    assert candidate(maxHeights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150
    assert candidate(maxHeights = [1, 3, 2, 3, 4, 3, 2, 3, 1]) == 20
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 113
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
    assert candidate(maxHeights = [2, 2, 3, 4, 5, 6, 5, 5, 5, 5, 6, 7, 8, 9, 10]) == 81
    assert candidate(maxHeights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 101
    assert candidate(maxHeights = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7]) == 111
    assert candidate(maxHeights = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 103
    assert candidate(maxHeights = [9, 9, 9, 9, 9, 1, 1, 1, 1, 1]) == 50
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(maxHeights = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100]) == 700
    assert candidate(maxHeights = [9, 7, 5, 3, 1, 1, 3, 5, 7, 9]) == 30
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 50
    assert candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1]) == 27
    assert candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 53
    assert candidate(maxHeights = [100, 50, 50, 100, 50, 50, 100, 50, 50, 100]) == 550
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(maxHeights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 19
    assert candidate(maxHeights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000008
    assert candidate(maxHeights = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1]) == 28


