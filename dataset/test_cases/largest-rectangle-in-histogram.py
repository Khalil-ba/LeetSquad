def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(heights = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10000, 10000, 10000, 10000, 10000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10000, 10000, 10000, 10000, 10000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(heights = [4, 2, 0, 3, 2, 5, 6, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [4, 2, 0, 3, 2, 5, 6, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10000, 10000, 10000, 10000]) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10000, 10000, 10000, 10000]) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 5, 6, 2, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 5, 6, 2, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 1, 3, 1, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 1, 3, 1, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 15, 10, 20, 25, 30, 20, 15, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 15, 10, 20, 25, 30, 20, 15, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 99910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 99910: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 2, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 2, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(heights = [6, 2, 5, 4, 5, 1, 6, 2, 3, 3, 2, 6, 5, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [6, 2, 5, 4, 5, 1, 6, 2, 3, 3, 2, 6, 5, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 9, 2, 5, 6, 4, 3, 7, 8, 9, 10, 11, 12]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 9, 2, 5, 6, 4, 3, 7, 8, 9, 10, 11, 12]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 113: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10000, 0, 10000, 0, 10000, 0]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10000, 0, 10000, 0, 10000, 0]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 3, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 3, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 5, 4, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 5, 4, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(heights = [4, 2, 0, 3, 2, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [4, 2, 0, 3, 2, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 200, 300, 400, 300, 200, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 200, 300, 400, 300, 200, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(heights = [6, 2, 5, 4, 5, 1, 6, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [6, 2, 5, 4, 5, 1, 6, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 5, 6, 2, 3, 2, 1, 5, 6, 2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 5, 6, 2, 3, 2, 1, 5, 6, 2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 5, 6, 2, 3, 1, 4, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 5, 6, 2, 3, 1, 4, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [4, 2, 0, 3, 2, 5, 3, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [4, 2, 0, 3, 2, 5, 3, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 1, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 1, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 2, 3, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 2, 3, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 6, 2, 8, 9, 1, 4, 3, 7, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 6, 2, 8, 9, 1, 4, 3, 7, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 8, 6, 2, 7, 8, 5, 9, 5, 3, 8, 6, 7, 9, 5, 2, 8]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 8, 6, 2, 7, 8, 5, 9, 5, 3, 8, 6, 7, 9, 5, 2, 8]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(heights = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10000, 0, 10000, 0, 10000, 0, 10000, 0]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10000, 0, 10000, 0, 10000, 0, 10000, 0]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 5, 6, 2, 3, 2, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 5, 6, 2, 3, 2, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(heights = [6, 2, 5, 4, 5, 1, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [6, 2, 5, 4, 5, 1, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 2, 3, 1, 2, 3, 4, 3, 2, 1, 2, 3, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 2, 3, 1, 2, 3, 4, 3, 2, 1, 2, 3, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 0, 0, 1, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 0, 0, 1, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 2, 1, 2, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 2, 1, 2, 3, 2, 1]) == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(heights = [1]) == 1
    assert candidate(heights = [1, 0, 1, 0, 1]) == 1
    assert candidate(heights = [10000, 10000, 10000, 10000, 10000]) == 50000
    assert candidate(heights = [0]) == 0
    assert candidate(heights = [1, 2, 3, 4, 5]) == 9
    assert candidate(heights = [0, 1, 0, 1, 0]) == 1
    assert candidate(heights = [2, 1, 2]) == 3
    assert candidate(heights = [4, 2, 0, 3, 2, 5, 6, 0, 0, 1]) == 10
    assert candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0]) == 20
    assert candidate(heights = [3]) == 3
    assert candidate(heights = [2, 4]) == 4
    assert candidate(heights = [10000, 10000, 10000, 10000]) == 40000
    assert candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 9]) == 20
    assert candidate(heights = [0, 0, 0, 0, 0]) == 0
    assert candidate(heights = [0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1]) == 9
    assert candidate(heights = [2, 1, 5, 6, 2, 3]) == 10
    assert candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3]) == 27
    assert candidate(heights = [1, 1, 1, 1, 1]) == 5
    assert candidate(heights = [5, 4, 3, 2, 1]) == 9
    assert candidate(heights = [3, 1, 3, 1, 3]) == 5
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
    assert candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 16
    assert candidate(heights = [10, 15, 10, 20, 25, 30, 20, 15, 10]) == 90
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 9
    assert candidate(heights = [1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 14
    assert candidate(heights = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == 15
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 60
    assert candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 2]) == 20
    assert candidate(heights = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 9
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 30
    assert candidate(heights = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 99910
    assert candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 2, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(heights = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2]) == 20
    assert candidate(heights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
    assert candidate(heights = [6, 2, 5, 4, 5, 1, 6, 2, 3, 3, 2, 6, 5, 3, 2, 1]) == 18
    assert candidate(heights = [3, 6, 5, 7, 4, 8, 1, 0, 9, 2, 5, 6, 4, 3, 7, 8, 9, 10, 11, 12]) == 42
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 113
    assert candidate(heights = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60, 10]) == 110
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 66
    assert candidate(heights = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3]) == 165
    assert candidate(heights = [10000, 0, 10000, 0, 10000, 0]) == 10000
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(heights = [5, 3, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(heights = [1, 3, 2, 1, 5, 4, 2, 1]) == 8
    assert candidate(heights = [4, 2, 0, 3, 2, 5]) == 6
    assert candidate(heights = [100, 200, 300, 400, 300, 200, 100]) == 1000
    assert candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 10
    assert candidate(heights = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(heights = [6, 2, 5, 4, 5, 1, 6, 3]) == 12
    assert candidate(heights = [2, 1, 5, 6, 2, 3, 2, 1, 5, 6, 2, 3]) == 12
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(heights = [2, 1, 5, 6, 2, 3, 1, 4, 2, 1]) == 10
    assert candidate(heights = [0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(heights = [4, 2, 0, 3, 2, 5, 3, 1]) == 8
    assert candidate(heights = [5, 5, 1, 5, 5]) == 10
    assert candidate(heights = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10
    assert candidate(heights = [1, 3, 2, 1, 2, 3, 1]) == 7
    assert candidate(heights = [5, 6, 2, 8, 9, 1, 4, 3, 7, 10]) == 16
    assert candidate(heights = [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5]) == 25
    assert candidate(heights = [5, 8, 6, 2, 7, 8, 5, 9, 5, 3, 8, 6, 7, 9, 5, 2, 8]) == 34
    assert candidate(heights = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(heights = [10000, 0, 10000, 0, 10000, 0, 10000, 0]) == 10000
    assert candidate(heights = [2, 1, 5, 6, 2, 3, 2, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(heights = [1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21]) == 66
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21
    assert candidate(heights = [2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4]) == 40
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 18
    assert candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 10
    assert candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 20
    assert candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
    assert candidate(heights = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 26
    assert candidate(heights = [1, 3, 2, 1, 3, 2, 1]) == 7
    assert candidate(heights = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 12
    assert candidate(heights = [5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5]) == 25
    assert candidate(heights = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 25
    assert candidate(heights = [6, 2, 5, 4, 5, 1, 6]) == 12
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 21
    assert candidate(heights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(heights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15
    assert candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(heights = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 160
    assert candidate(heights = [1, 3, 2, 1, 2, 3, 1, 2, 3, 4, 3, 2, 1, 2, 3, 1]) == 16
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21
    assert candidate(heights = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(heights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500
    assert candidate(heights = [1, 0, 0, 0, 1, 0, 0, 0, 1]) == 1
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(heights = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 17
    assert candidate(heights = [2, 1, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 2, 1, 2, 3, 2, 1]) == 28


