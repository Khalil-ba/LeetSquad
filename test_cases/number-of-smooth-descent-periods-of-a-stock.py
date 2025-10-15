def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 4, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 4, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 3, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 3, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 99999, 99998, 99997, 99996, 99995]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 99999, 99998, 99997, 99996, 99995]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 7, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 7, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 10, 9, 8, 7, 8, 7, 6, 5]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 10, 9, 8, 7, 8, 7, 6, 5]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 3, 3, 3, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 3, 3, 3, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 5, 4, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 5, 4, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 1, 4, 3, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 1, 4, 3, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 9, 8, 7, 6, 5, 6, 7]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 9, 8, 7, 6, 5, 6, 7]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 166: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 4, 3, 2, 1, 0, 1, 0, -1, -2, -3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 4, 3, 2, 1, 0, 1, 0, -1, -2, -3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 10, 9, 8, 7, 6, 5, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 10, 9, 8, 7, 6, 5, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 10, 9, 8, 7, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 10, 9, 8, 7, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 496: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 9, 8, 7, 8, 7, 6, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 9, 8, 7, 8, 7, 6, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 147: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]) == 211: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 6, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 6, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 10, 9, 8, 7, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 10, 9, 8, 7, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -3]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -3]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 3, 2, 1, 0, 1, 2, 1, 0, -1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 3, 2, 1, 0, 1, 2, 1, 0, -1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == 65: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(prices = [10, 9, 4, 3, 2, 1]) == 13
    assert candidate(prices = [3, 3, 3, 3, 3]) == 5
    assert candidate(prices = [100000, 99999, 99998, 99997, 99996, 99995]) == 21
    assert candidate(prices = [8, 6, 7, 7]) == 4
    assert candidate(prices = [1]) == 1
    assert candidate(prices = [10, 9, 10, 9, 8, 7, 8, 7, 6, 5]) == 23
    assert candidate(prices = [3, 3, 3, 3, 3, 3, 3]) == 7
    assert candidate(prices = [5, 4, 5, 4, 3, 2, 1]) == 18
    assert candidate(prices = [3, 2, 1, 4]) == 7
    assert candidate(prices = [1, 3, 2, 1, 4, 3, 2, 1]) == 17
    assert candidate(prices = [5, 4, 3, 4, 3, 2, 1]) == 16
    assert candidate(prices = [5]) == 1
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55
    assert candidate(prices = [10, 9, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 51
    assert candidate(prices = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 19
    assert candidate(prices = [5, 4, 3, 2, 1]) == 15
    assert candidate(prices = [1, 2, 3, 4, 5]) == 5
    assert candidate(prices = [10, 9, 8, 9, 8, 7, 6, 5, 6, 7]) == 23
    assert candidate(prices = [2, 1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 37
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 36
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 66
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 210
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 136
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
    assert candidate(prices = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 166
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11]) == 135
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 76
    assert candidate(prices = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == 210
    assert candidate(prices = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 29
    assert candidate(prices = [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 1]) == 27
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 28
    assert candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 465
    assert candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 60
    assert candidate(prices = [7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == 73
    assert candidate(prices = [5, 4, 3, 4, 3, 2, 1, 0, 1, 0, -1, -2, -3]) == 36
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 64
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 29
    assert candidate(prices = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991, 49990, 49989, 49988, 49987, 49986, 49985, 49984, 49983, 49982, 49981]) == 210
    assert candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 70
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 210
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 41
    assert candidate(prices = [1, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2]) == 40
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 44
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75]) == 325
    assert candidate(prices = [10, 9, 8, 10, 9, 8, 7, 6, 5, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(prices = [10, 9, 8, 7, 10, 9, 8, 7, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 86
    assert candidate(prices = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 33
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 75
    assert candidate(prices = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == 37
    assert candidate(prices = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 170
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 19
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 496
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(prices = [7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 231
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 231
    assert candidate(prices = [10, 9, 8, 9, 8, 7, 8, 7, 6, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 60
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) == 38
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 136
    assert candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(prices = [10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 201
    assert candidate(prices = [10, 9, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9]) == 62
    assert candidate(prices = [10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]) == 22
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 25
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 19
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19
    assert candidate(prices = [3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 80
    assert candidate(prices = [10, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 147
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 28
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 119
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 40
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 29
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 24
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5050
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 22
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 44
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 64
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20]) == 211
    assert candidate(prices = [5, 6, 5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 41
    assert candidate(prices = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980]) == 210
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 69
    assert candidate(prices = [10, 9, 10, 9, 8, 7, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 48
    assert candidate(prices = [3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -3]) == 45
    assert candidate(prices = [1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 81
    assert candidate(prices = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 66
    assert candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 14
    assert candidate(prices = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 35
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
    assert candidate(prices = [3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == 55
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0]) == 50
    assert candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 325
    assert candidate(prices = [2, 1, 3, 2, 1, 0, 1, 2, 1, 0, -1]) == 24
    assert candidate(prices = [5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 26
    assert candidate(prices = [10, 9, 8, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == 70
    assert candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 351
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 72
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 240
    assert candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 11
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(prices = [7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 79
    assert candidate(prices = [3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 66
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(prices = [10, 9, 8, 7, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == 65


