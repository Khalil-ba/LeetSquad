def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [7, 4, 7, 4, 7]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [7, 4, 7, 4, 7]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 2, 5, 5, 2, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 2, 5, 5, 2, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [7, 4, 4, 4, 10, 6]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [7, 4, 4, 4, 10, 6]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 4, 8, 7, 5, 3, 2, 6, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 4, 8, 7, 5, 3, 2, 6, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 2, 5, 3, 7, 20]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 2, 5, 3, 7, 20]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(heights = [8, 6, 5, 7, 9]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [8, 6, 5, 7, 9]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 3, 3, 3, 3, 3, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 3, 3, 3, 3, 3, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 3, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 3, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 20, 10]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 20, 10]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 3, 4, 1, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 3, 4, 1, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [6, 5, 3, 9, 2, 7]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [6, 5, 3, 9, 2, 7]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 1, 5, 10, 15, 10, 5, 1, 5]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 1, 5, 10, 15, 10, 5, 1, 5]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 10, 10, 10, 5, 4, 3, 2, 1]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 10, 10, 10, 5, 4, 3, 2, 1]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 215: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 761
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 761: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 330: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000018: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 605: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 9, 9, 10, 9, 9, 9, 10, 9, 9, 9, 10, 9, 9, 9]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 9, 9, 10, 9, 9, 9, 10, 9, 9, 9, 10, 9, 9, 9]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9000000020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9000000020: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 374: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 25, 35, 40, 30, 20, 10]) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 25, 35, 40, 30, 20, 10]) == 215: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(heights = [7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 7]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 7]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 207: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 2, 3, 4, 3, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 2, 3, 4, 3, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 820: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 129: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 10999999945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 10999999945: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4999999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4999999990: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 15, 10, 15, 20, 10, 5, 10, 15, 20, 25]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 15, 10, 15, 20, 10, 5, 10, 15, 20, 25]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 100, 5, 4, 3, 2, 1, 2, 3, 4, 5, 100, 5, 4, 3, 2, 1]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 100, 5, 4, 3, 2, 1, 2, 3, 4, 5, 100, 5, 4, 3, 2, 1]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 460: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1010: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 10, 1, 100, 10, 1, 100, 10, 1, 100, 10, 1, 100, 10, 1, 100]) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 10, 1, 100, 10, 1, 100, 10, 1, 100, 10, 1, 100, 10, 1, 100]) == 124: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 10, 1, 1, 1, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 10, 1, 1, 1, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 3, 4, 5, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 3, 4, 5, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(heights = [6, 5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [6, 5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 5, 3, 7, 5, 3, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 5, 3, 7, 5, 3, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 6000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 6000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 10, 10, 10, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 10, 10, 10, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 4, 8, 7, 5, 6, 3, 2, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 4, 8, 7, 5, 6, 3, 2, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 8, 9]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 8, 9]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 6, 5, 7, 6]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 6, 5, 7, 6]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 6, 7, 8, 9, 8, 7, 6, 5]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 6, 7, 8, 9, 8, 7, 6, 5]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 4, 2, 1, 3, 5, 7, 6, 8, 10]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 4, 2, 1, 3, 5, 7, 6, 8, 10]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 2, 1, 3, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 2, 1, 3, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 2, 3, 1, 2, 3, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 2, 3, 1, 2, 3, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 3, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 3, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2, 1, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2, 1, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1, 1000000000, 1, 1000000000]) == 1000000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1, 1000000000, 1, 1000000000]) == 1000000004: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 30, 10, 40, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 30, 10, 40, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 2, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 2, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 4, 4, 7, 2]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 4, 4, 7, 2]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 4, 7, 5, 6, 4, 3, 8, 9, 1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 4, 7, 5, 6, 4, 3, 8, 9, 1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 5, 3, 5, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 5, 3, 5, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000]) == 4000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000]) == 4000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 7, 5, 3, 1, 3, 5, 7, 9]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 7, 5, 3, 1, 3, 5, 7, 9]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 4, 4, 5]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 4, 4, 5]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 110: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(heights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(heights = [7, 4, 7, 4, 7]) == 23
    assert candidate(heights = [3, 2, 5, 5, 2, 3]) == 18
    assert candidate(heights = [1, 2, 3, 4, 5]) == 15
    assert candidate(heights = [1, 2, 3, 2, 1]) == 9
    assert candidate(heights = [7, 4, 4, 4, 10, 6]) == 32
    assert candidate(heights = [1, 2, 1, 2, 1]) == 6
    assert candidate(heights = [9, 4, 8, 7, 5, 3, 2, 6, 1]) == 36
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(heights = [10, 9, 2, 5, 3, 7, 20]) == 39
    assert candidate(heights = [8, 6, 5, 7, 9]) == 31
    assert candidate(heights = [1, 3, 3, 3, 3, 3, 3, 2, 1]) == 22
    assert candidate(heights = [1, 3, 2, 3, 1]) == 9
    assert candidate(heights = [10, 20, 10, 20, 10]) == 60
    assert candidate(heights = [1, 1, 1, 1, 1]) == 5
    assert candidate(heights = [5, 3, 4, 1, 1]) == 13
    assert candidate(heights = [10, 20, 10]) == 40
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 13
    assert candidate(heights = [6, 5, 3, 9, 2, 7]) == 22
    assert candidate(heights = [5, 4, 3, 2, 1]) == 15
    assert candidate(heights = [5, 5, 5, 5, 5, 5]) == 30
    assert candidate(heights = [10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109
    assert candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 36
    assert candidate(heights = [5, 1, 5, 10, 15, 10, 5, 1, 5]) == 49
    assert candidate(heights = [1, 2, 3, 4, 5, 10, 10, 10, 5, 4, 3, 2, 1]) == 60
    assert candidate(heights = [2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 108
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 104
    assert candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 83
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1]) == 24
    assert candidate(heights = [1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1]) == 27
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 70
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 215
    assert candidate(heights = [1, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1]) == 59
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(heights = [3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3]) == 36
    assert candidate(heights = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 56
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 761
    assert candidate(heights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 330
    assert candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 58
    assert candidate(heights = [1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1]) == 20
    assert candidate(heights = [1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5]) == 30
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 46
    assert candidate(heights = [3, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 93
    assert candidate(heights = [1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 20
    assert candidate(heights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000018
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == 70
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 605
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 40
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
    assert candidate(heights = [9, 9, 9, 10, 9, 9, 9, 10, 9, 9, 9, 10, 9, 9, 9]) == 136
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9000000020
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 46
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75
    assert candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 112
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 17
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 112
    assert candidate(heights = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 374
    assert candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26
    assert candidate(heights = [10, 20, 30, 25, 35, 40, 30, 20, 10]) == 215
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 400
    assert candidate(heights = [7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 7]) == 37
    assert candidate(heights = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5]) == 150
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 207
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 42
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 2, 3, 4, 3, 2, 1]) == 26
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 820
    assert candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0]) == 82
    assert candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 129
    assert candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650
    assert candidate(heights = [5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 43
    assert candidate(heights = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 201
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 109
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 125
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(heights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 49
    assert candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 24
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 33
    assert candidate(heights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 210
    assert candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 10999999945
    assert candidate(heights = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 385
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 4999999990
    assert candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(heights = [10, 20, 15, 10, 15, 20, 10, 5, 10, 15, 20, 25]) == 110
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == 75
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 210
    assert candidate(heights = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 109
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(heights = [1, 2, 3, 4, 5, 100, 5, 4, 3, 2, 1, 2, 3, 4, 5, 100, 5, 4, 3, 2, 1]) == 140
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 560
    assert candidate(heights = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 33
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 460
    assert candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 87
    assert candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(heights = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1010
    assert candidate(heights = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 45
    assert candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60
    assert candidate(heights = [100, 10, 1, 100, 10, 1, 100, 10, 1, 100, 10, 1, 100, 10, 1, 100]) == 124
    assert candidate(heights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]) == 45
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 57
    assert candidate(heights = [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 71
    assert candidate(heights = [1, 1, 1, 1, 10, 1, 1, 1, 1]) == 18
    assert candidate(heights = [2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 31
    assert candidate(heights = [1, 3, 2, 3, 4, 5, 3, 2, 1]) == 23
    assert candidate(heights = [6, 5, 4, 3, 2, 1]) == 21
    assert candidate(heights = [1, 5, 3, 7, 5, 3, 1]) == 23
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 6000000000
    assert candidate(heights = [10, 10, 10, 10, 10]) == 50
    assert candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20
    assert candidate(heights = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30
    assert candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 9999999955
    assert candidate(heights = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(heights = [9, 4, 8, 7, 5, 6, 3, 2, 1]) == 39
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 19
    assert candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 11
    assert candidate(heights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250
    assert candidate(heights = [9, 8, 7, 8, 9]) == 38
    assert candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 109
    assert candidate(heights = [1, 3, 2, 5, 4, 6, 5, 7, 6]) == 36
    assert candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 99
    assert candidate(heights = [5, 6, 7, 8, 9, 8, 7, 6, 5]) == 61
    assert candidate(heights = [9, 4, 2, 1, 3, 5, 7, 6, 8, 10]) == 42
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
    assert candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30
    assert candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5]) == 25
    assert candidate(heights = [1, 3, 2, 1, 2, 1, 3, 1]) == 11
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(heights = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]) == 20
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 13
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
    assert candidate(heights = [1, 3, 2, 1, 2, 3, 1, 2, 3, 1]) == 13
    assert candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(heights = [1, 3, 2, 3, 1]) == 9
    assert candidate(heights = [1, 2, 1, 2, 1, 2]) == 7
    assert candidate(heights = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 13
    assert candidate(heights = [1, 2, 1]) == 4
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(heights = [1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 23
    assert candidate(heights = [1000000000, 1, 1000000000, 1, 1000000000]) == 1000000004
    assert candidate(heights = [2, 1, 2]) == 4
    assert candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36
    assert candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 62
    assert candidate(heights = [10, 20, 10, 30, 10, 40, 10]) == 100
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1]) == 16
    assert candidate(heights = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(heights = [1, 1, 1, 1, 1, 5, 4, 3, 2, 1]) == 20
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(heights = [1, 3, 2, 1, 2, 3, 2, 1]) == 12
    assert candidate(heights = [9, 4, 4, 7, 2]) == 23
    assert candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 52
    assert candidate(heights = [1, 3, 2, 1]) == 7
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(heights = [1, 3, 5, 4, 7, 5, 6, 4, 3, 8, 9, 1]) == 43
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10000000000
    assert candidate(heights = [1, 5, 3, 5, 1]) == 13
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000]) == 4000000000
    assert candidate(heights = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(heights = [9, 7, 5, 3, 1, 3, 5, 7, 9]) == 29
    assert candidate(heights = [5, 4, 4, 4, 5]) == 21
    assert candidate(heights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 110


