def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 3, 4, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 3, 4, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 3, 0, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 3, 0, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 8, 4, 9]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 8, 4, 9]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9, 8, 9]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9, 8, 9]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 4, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 4, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 3, 10, 2, 5, 8, 12]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 3, 10, 2, 5, 8, 12]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 28, 25, 22, 20, 18, 15, 13, 10, 8, 5, 3, 1, 0, 2, 4, 6, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 28, 25, 22, 20, 18, 15, 13, 10, 8, 5, 3, 1, 0, 2, 4, 6, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 101, 102, 98, 97, 96, 100, 105, 110, 108, 107, 109, 112, 115, 118, 120, 119, 117, 116, 115, 114, 113, 112, 111, 110, 109]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 101, 102, 98, 97, 96, 100, 105, 110, 108, 107, 109, 112, 115, 118, 120, 119, 117, 116, 115, 114, 113, 112, 111, 110, 109]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 10, 8, 12, 15, 10, 18, 14, 20, 25, 22, 27, 30]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 10, 8, 12, 15, 10, 18, 14, 20, 25, 22, 27, 30]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 4, 9, 8, 10, 3, 2, 6, 4, 8]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 4, 9, 8, 10, 3, 2, 6, 4, 8]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 6, 8, 7, 4, 12, 14, 13, 11, 10, 8, 6, 4, 2, 0]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 6, 8, 7, 4, 12, 14, 13, 11, 10, 8, 6, 4, 2, 0]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 3, 8, 12, 4, 7, 15, 10, 18, 14, 20, 25, 22, 27, 30]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 3, 8, 12, 4, 7, 15, 10, 18, 14, 20, 25, 22, 27, 30]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 2, 6, 7, 8, 4, 5, 6, 1, 2, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 2, 6, 7, 8, 4, 5, 6, 1, 2, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 3, 7, 6, 1, 8, 4, 9]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 3, 7, 6, 1, 8, 4, 9]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 7, 5, 8, 11, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 7, 5, 8, 11, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 12, 14, 16]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 12, 14, 16]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 1, 8]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 1, 8]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 5, 7, 8, 9, 10, 12, 11, 13, 15, 14, 16, 17]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 5, 7, 8, 9, 10, 12, 11, 13, 15, 14, 16, 17]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 2, 3, 6, 8, 5, 8, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 2, 3, 6, 8, 5, 8, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 5, 10, 4, 8, 2, 6, 7, 2, 3, 1, 5, 9, 10, 3, 2, 1, 5, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 5, 10, 4, 8, 2, 6, 7, 2, 3, 1, 5, 9, 10, 3, 2, 1, 5, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 7, 5, 8, 11, 9, 12, 10, 14, 13, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 7, 5, 8, 11, 9, 12, 10, 14, 13, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 9]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 9]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 3, 4, 6, 2, 5, 7, 8, 1, 9, 11, 13, 10]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 3, 4, 6, 2, 5, 7, 8, 1, 9, 11, 13, 10]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 1, 3, 1, 5, 1, 3, 1, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 1, 3, 1, 5, 1, 3, 1, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 3, 0, 1, 2, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 3, 0, 1, 2, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 4, 5, 2, 3, 0, 4, 2, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 4, 5, 2, 3, 0, 4, 2, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16, 12, 17, 13, 18, 14, 19, 15, 20]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16, 12, 17, 13, 18, 14, 19, 15, 20]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 5, 7, 9, 10, 8, 11, 13, 12, 15, 17]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 5, 7, 9, 10, 8, 11, 13, 12, 15, 17]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 14, 15]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 14, 15]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 7, 15, 8, 12, 9, 20, 18, 25, 17]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 7, 15, 8, 12, 9, 20, 18, 25, 17]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 2, 5, 3, 10, 1, 3, 8, 1, 9, 2, 6]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 2, 5, 3, 10, 1, 3, 8, 1, 9, 2, 6]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 10, 8, 6, 8, 12, 10, 8, 10, 14, 12, 10, 12, 16, 14, 12, 14, 18, 16, 14, 16]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 10, 8, 6, 8, 12, 10, 8, 10, 14, 12, 10, 12, 16, 14, 12, 14, 18, 16, 14, 16]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 3, 8, 12, 10, 14, 18, 22, 20, 25, 28, 26, 30, 32, 31, 35, 38]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 3, 8, 12, 10, 14, 18, 22, 20, 25, 28, 26, 30, 32, 31, 35, 38]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 5, 8, 2, 9, 1, 5, 7, 3, 8]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 5, 8, 2, 9, 1, 5, 7, 3, 8]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 12, 4, 6, 10, 3, 12, 7, 9, 8]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 12, 4, 6, 10, 3, 12, 7, 9, 8]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 10, 20, 10, 15, 10, 25, 15, 30, 20, 35, 25, 40, 30]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 10, 20, 10, 15, 10, 25, 15, 30, 20, 35, 25, 40, 30]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 101]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 101]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 6, 7, 4, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 6, 7, 4, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 5, 0, 1, 5, 0, 3, 1, 2, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 5, 0, 1, 5, 0, 3, 1, 2, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 7, 5, 8, 11, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 7, 5, 8, 11, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 14, 13, 15]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 14, 13, 15]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 6, 3, 5, 4, 8, 7, 9, 10, 11, 10, 12, 13, 14, 15, 16]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 6, 3, 5, 4, 8, 7, 9, 10, 11, 10, 12, 13, 14, 15, 16]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15, 16, 14, 22, 25, 30, 35, 40]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15, 16, 14, 22, 25, 30, 35, 40]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 3, 9, 7, 8, 4, 10, 1, 12, 11, 13]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 3, 9, 7, 8, 4, 10, 1, 12, 11, 13]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 5, 2, 8, 4, 9, 10, 1, 11, 13, 12, 14, 15, 13, 16, 18, 17, 20, 22]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 5, 2, 8, 4, 9, 10, 1, 11, 13, 12, 14, 15, 13, 16, 18, 17, 20, 22]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 7, 5, 8, 11, 9, 12, 15, 13, 17, 20, 18]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 7, 5, 8, 11, 9, 12, 15, 13, 17, 20, 18]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [1, 2, 2, 3, 4, 4, 5]) == 4
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1]) == 3
    assert candidate(prices = [6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9]) == 25
    assert candidate(prices = [1, 2, 2, 3, 0, 4]) == 6
    assert candidate(prices = [1, 2]) == 1
    assert candidate(prices = [1]) == 0
    assert candidate(prices = [1, 3, 2, 8, 4, 9]) == 13
    assert candidate(prices = [7, 1, 5, 3, 6, 4]) == 7
    assert candidate(prices = [3, 2, 6, 5, 0, 3]) == 7
    assert candidate(prices = [1, 2, 2, 3, 4, 5]) == 4
    assert candidate(prices = [10, 9, 8, 2]) == 0
    assert candidate(prices = [1, 100]) == 99
    assert candidate(prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9, 8, 9]) == 26
    assert candidate(prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 7
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8
    assert candidate(prices = [1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 3, 10, 2, 5, 8, 12]) == 30
    assert candidate(prices = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 16
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [30, 28, 25, 22, 20, 18, 15, 13, 10, 8, 5, 3, 1, 0, 2, 4, 6, 8]) == 8
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 12
    assert candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 15
    assert candidate(prices = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 26
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(prices = [100, 101, 102, 98, 97, 96, 100, 105, 110, 108, 107, 109, 112, 115, 118, 120, 119, 117, 116, 115, 114, 113, 112, 111, 110, 109]) == 29
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 10, 8, 12, 15, 10, 18, 14, 20, 25, 22, 27, 30]) == 47
    assert candidate(prices = [5, 2, 4, 9, 8, 10, 3, 2, 6, 4, 8]) == 17
    assert candidate(prices = [8, 6, 4, 6, 8, 7, 4, 12, 14, 13, 11, 10, 8, 6, 4, 2, 0]) == 14
    assert candidate(prices = [1, 5, 3, 8, 12, 4, 7, 15, 10, 18, 14, 20, 25, 22, 27, 30]) == 51
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 48
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 8
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [5, 3, 2, 6, 7, 8, 4, 5, 6, 1, 2, 3]) == 10
    assert candidate(prices = [5, 2, 3, 7, 6, 1, 8, 4, 9]) == 17
    assert candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [10, 7, 5, 8, 11, 9]) == 6
    assert candidate(prices = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 12, 14, 16]) == 16
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 1, 8]) == 11
    assert candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 10
    assert candidate(prices = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]) == 0
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
    assert candidate(prices = [1, 3, 2, 5, 7, 8, 9, 10, 12, 11, 13, 15, 14, 16, 17]) == 19
    assert candidate(prices = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 8
    assert candidate(prices = [10, 9, 8, 2, 3, 6, 8, 5, 8, 10]) == 11
    assert candidate(prices = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 8
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [5, 3, 5, 10, 4, 8, 2, 6, 7, 2, 3, 1, 5, 9, 10, 3, 2, 1, 5, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [10, 7, 5, 8, 11, 9, 12, 10, 14, 13, 15]) == 15
    assert candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14]) == 26
    assert candidate(prices = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 9]) == 17
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(prices = [7, 1, 3, 4, 6, 2, 5, 7, 8, 1, 9, 11, 13, 10]) == 23
    assert candidate(prices = [2, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 26
    assert candidate(prices = [1, 5, 1, 3, 1, 5, 1, 3, 1, 5]) == 16
    assert candidate(prices = [1, 2, 2, 3, 0, 1, 2, 1, 2, 3]) == 6
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 4, 5, 2, 3, 0, 4, 2, 3]) == 15
    assert candidate(prices = [1, 3, 2, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16, 12, 17, 13, 18, 14, 19, 15, 20]) == 68
    assert candidate(prices = [10, 9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1]) == 64
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 23
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 28
    assert candidate(prices = [8, 6, 4, 3, 3, 5, 7, 9, 10, 8, 11, 13, 12, 15, 17]) == 17
    assert candidate(prices = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 27
    assert candidate(prices = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 5
    assert candidate(prices = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12]) == 11
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0
    assert candidate(prices = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]) == 9
    assert candidate(prices = [1, 2, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 14, 15]) == 16
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [10, 7, 15, 8, 12, 9, 20, 18, 25, 17]) == 30
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30]) == 30
    assert candidate(prices = [7, 2, 5, 3, 10, 1, 3, 8, 1, 9, 2, 6]) == 29
    assert candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 12
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 18
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 10, 8, 6, 8, 12, 10, 8, 10, 14, 12, 10, 12, 16, 14, 12, 14, 18, 16, 14, 16]) == 39
    assert candidate(prices = [1, 5, 3, 8, 12, 10, 14, 18, 22, 20, 25, 28, 26, 30, 32, 31, 35, 38]) == 46
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 5, 8, 2, 9, 1, 5, 7, 3, 8]) == 29
    assert candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 9
    assert candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 8
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 14
    assert candidate(prices = [8, 12, 4, 6, 10, 3, 12, 7, 9, 8]) == 21
    assert candidate(prices = [1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 13
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 0
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 5
    assert candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 26
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(prices = [10, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17
    assert candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 15
    assert candidate(prices = [10, 5, 10, 20, 10, 15, 10, 25, 15, 30, 20, 35, 25, 40, 30]) == 80
    assert candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 101]) == 1
    assert candidate(prices = [5, 3, 6, 7, 4, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 21
    assert candidate(prices = [1, 3, 2, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16]) == 48
    assert candidate(prices = [2, 2, 5, 0, 1, 5, 0, 3, 1, 2, 5]) == 15
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50]) == 50
    assert candidate(prices = [10, 7, 5, 8, 11, 9]) == 6
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8
    assert candidate(prices = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 14, 13, 15]) == 18
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 990
    assert candidate(prices = [1, 2, 2, 6, 3, 5, 4, 8, 7, 9, 10, 11, 10, 12, 13, 14, 15, 16]) == 21
    assert candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1]) == 12
    assert candidate(prices = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 4
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 15, 16, 14, 22, 25, 30, 35, 40]) == 46
    assert candidate(prices = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 23
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(prices = [1, 5, 3, 9, 7, 8, 4, 10, 1, 12, 11, 13]) == 30
    assert candidate(prices = [5, 3, 5, 2, 8, 4, 9, 10, 1, 11, 13, 12, 14, 15, 13, 16, 18, 17, 20, 22]) == 39
    assert candidate(prices = [10, 7, 5, 8, 11, 9, 12, 15, 13, 17, 20, 18]) == 19
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 36
    assert candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16]) == 23
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14


