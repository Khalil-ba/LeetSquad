def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 1, 5, 1, 5, 1, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 1, 5, 1, 5, 1, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 4, 5, 2, 9, 7]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 4, 5, 2, 9, 7]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 22, 5, 75, 65, 80]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 22, 5, 75, 65, 80]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 4, 2, 8, 2, 6, 7, 8, 2, 4, 5, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 4, 2, 8, 2, 6, 7, 8, 2, 4, 5, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 4, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 4, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 8, 4, 9]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 8, 4, 9]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 1, 2, 3, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 1, 2, 3, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 22, 5, 75, 65, 80, 120, 130, 110, 140, 150, 160]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 22, 5, 75, 65, 80, 120, 130, 110, 140, 150, 160]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 4, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 4, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 4, 3, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 4, 3, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 9, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 9, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 11, 3, 50, 60, 90, 30, 80, 100, 50, 80, 120]) == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 11, 3, 50, 60, 90, 30, 80, 100, 50, 80, 120]) == 177: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [31, 41, 48, 54, 37, 76, 56, 99, 1, 180]) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [31, 41, 48, 54, 37, 76, 56, 99, 1, 180]) == 247: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 10, 4]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 10, 4]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 2, 98, 3, 96, 4, 94, 5, 92, 6, 90, 7, 88, 8, 86, 9, 84, 10, 82]) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 2, 98, 3, 96, 4, 94, 5, 92, 6, 90, 7, 88, 8, 86, 9, 84, 10, 82]) == 195: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 6, 8, 2, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 6, 8, 2, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 180, 260, 40, 310, 535, 695]) == 815
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 180, 260, 40, 310, 535, 695]) == 815: {e}')
    
    total += 1
    try:
        result = candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 10, 1, 3, 12, 6, 9, 1, 15]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 10, 1, 3, 12, 6, 9, 1, 15]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 10, 5, 6, 7, 3, 10, 4, 5, 6, 1, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 10, 5, 6, 7, 3, 10, 4, 5, 6, 1, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 4, 0, 0, 3, 5, 7, 8, 2, 8]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 4, 0, 0, 3, 5, 7, 8, 2, 8]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 4, 3, 0, 5, 8, 3, 1, 5, 6, 4, 10, 2, 5, 12, 8, 9, 1, 10]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 4, 3, 0, 5, 8, 3, 1, 5, 6, 4, 10, 2, 5, 12, 8, 9, 1, 10]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 10, 8, 6, 2, 9, 5, 7, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 10, 8, 6, 2, 9, 5, 7, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 3, 5, 7, 9, 11]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 3, 5, 7, 9, 11]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 180, 260, 310, 40, 535, 695]) == 865
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 180, 260, 310, 40, 535, 695]) == 865: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9, 1, 2, 1, 3, 5, 7]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9, 1, 2, 1, 3, 5, 7]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 6, 8, 2, 5, 7, 8, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 6, 8, 2, 5, 7, 8, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 10, 12, 15, 14, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 10, 12, 15, 14, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 14]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 14]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 12, 15, 7, 3, 18, 20, 15]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 12, 15, 7, 3, 18, 20, 15]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 180, 260, 310, 40, 535, 695, 10, 5, 11, 3, 8, 10, 5, 11, 3, 8, 10, 5, 11]) == 865
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 180, 260, 310, 40, 535, 695, 10, 5, 11, 3, 8, 10, 5, 11, 3, 8, 10, 5, 11]) == 865: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 3, 0, 3, 2, 5, 4, 1, 6, 7, 8, 1, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 3, 0, 3, 2, 5, 4, 1, 6, 7, 8, 1, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 0, 3, 12, 6, 9, 21, 18, 13, 8, 12, 3, 20, 15, 18]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 0, 3, 12, 6, 9, 21, 18, 13, 8, 12, 3, 20, 15, 18]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(prices = [90, 80, 70, 60, 50, 40, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [90, 80, 70, 60, 50, 40, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 7, 5, 8, 11, 9, 1, 15]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 7, 5, 8, 11, 9, 1, 15]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 180, 260, 310, 40, 535, 695, 10, 20, 30, 100, 150]) == 865
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 180, 260, 310, 40, 535, 695, 10, 20, 30, 100, 150]) == 865: {e}')
    
    total += 1
    try:
        result = candidate(prices = [12, 14, 17, 10, 14, 13, 12, 15]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [12, 14, 17, 10, 14, 13, 12, 15]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 4, 8, 7, 2, 5, 1, 3, 5, 2, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 4, 8, 7, 2, 5, 1, 3, 5, 2, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 8, 9, 10, 8, 12, 15]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 8, 9, 10, 8, 12, 15]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 30, 15, 10, 8, 25, 80]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 30, 15, 10, 8, 25, 80]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 5, 7, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 5, 7, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, 1, 21, 1, 23, 1, 25, 1, 27]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, 1, 21, 1, 23, 1, 25, 1, 27]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 10, 11, 12, 10, 13, 14, 15, 16, 17, 18, 19]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 10, 11, 12, 10, 13, 14, 15, 16, 17, 18, 19]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 50, 10, 60, 40, 90, 55]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 50, 10, 60, 40, 90, 55]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 7, 8, 3, 6, 1, 2, 9, 10, 4, 5, 11, 12, 6, 7, 13, 14, 8, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 7, 8, 3, 6, 1, 2, 9, 10, 4, 5, 11, 12, 6, 7, 13, 14, 8, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 1, 4, 5, 2, 7, 8, 1, 9, 10, 1, 11, 12, 1, 13, 14]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 1, 4, 5, 2, 7, 8, 1, 9, 10, 1, 11, 12, 1, 13, 14]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 22, 5, 75, 65, 80, 10, 90, 50, 20, 120, 15, 8, 90]) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 22, 5, 75, 65, 80, 10, 90, 50, 20, 120, 15, 8, 90]) == 197: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 5, 8, 3, 8, 2, 6, 5, 7, 3, 8, 5, 6, 8, 9, 1, 2, 4, 5, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 5, 8, 3, 8, 2, 6, 5, 7, 3, 8, 5, 6, 8, 9, 1, 2, 4, 5, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 7, 4, 3, 8, 8, 6, 4, 10, 9, 3]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 7, 4, 3, 8, 8, 6, 4, 10, 9, 3]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 1, 2, 5, 1, 3, 7]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 1, 2, 5, 1, 3, 7]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 22, 5, 75, 65, 80]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 22, 5, 75, 65, 80]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 8, 4, 0, 5, 6, 2, 9, 8, 1, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 8, 4, 0, 5, 6, 2, 9, 8, 1, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 8, 4, 9, 3, 5, 7, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 8, 4, 9, 3, 5, 7, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [31, 41, 48, 54, 37, 44, 66, 59, 56, 78, 100]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [31, 41, 48, 54, 37, 44, 66, 59, 56, 78, 100]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 10, 15, 20, 5, 25, 30, 5, 35, 40]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 10, 15, 20, 5, 25, 30, 5, 35, 40]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 5, 1, 4, 7, 1, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 5, 1, 4, 7, 1, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 10, 1, 7, 8, 2, 9, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 10, 1, 7, 8, 2, 9, 4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 30, 15, 10, 8, 25, 80, 50, 150, 40, 60, 70, 90, 120, 130, 50, 20, 100, 140, 150]) == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 30, 15, 10, 8, 25, 80, 50, 150, 40, 60, 70, 90, 120, 130, 50, 20, 100, 140, 150]) == 272: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 0, 100, 101, 102, 103]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 0, 100, 101, 102, 103]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 10, 9, 11, 12, 8, 10, 5, 7, 3, 4, 2, 1, 5, 6, 8, 9, 10, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 10, 9, 11, 12, 8, 10, 5, 7, 3, 4, 2, 1, 5, 6, 8, 9, 10, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 10, 5, 3, 8, 20, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 10, 5, 3, 8, 20, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 9, 10, 15, 20, 2, 18, 25]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 9, 10, 15, 20, 2, 18, 25]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [80, 70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [80, 70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 180, 260, 40, 310, 535, 695]) == 815
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 180, 260, 40, 310, 535, 695]) == 815: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 10, 1, 4, 9, 2, 8, 0, 7, 3, 6, 1, 5, 2, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 10, 1, 4, 9, 2, 8, 0, 7, 3, 6, 1, 5, 2, 4]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [1, 5, 1, 5, 1, 5, 1, 5]) == 8
    assert candidate(prices = [2, 1, 4, 5, 2, 9, 7]) == 11
    assert candidate(prices = [10, 22, 5, 75, 65, 80]) == 87
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [3, 2, 6, 5, 0, 3]) == 7
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [1, 4, 2, 8, 2, 6, 7, 8, 2, 4, 5, 2, 1]) == 13
    assert candidate(prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(prices = [1, 3, 2, 8, 4, 9]) == 12
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert candidate(prices = [1, 2]) == 1
    assert candidate(prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(prices = [3, 3, 3, 3, 3]) == 0
    assert candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 1, 2, 3, 4]) == 7
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10
    assert candidate(prices = [10, 22, 5, 75, 65, 80, 120, 130, 110, 140, 150, 160]) == 175
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10
    assert candidate(prices = [7, 6, 4, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 6
    assert candidate(prices = [1, 3, 5, 4, 3, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 18
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
    assert candidate(prices = [10, 1, 9, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2, 1]) == 15
    assert candidate(prices = [5, 11, 3, 50, 60, 90, 30, 80, 100, 50, 80, 120]) == 177
    assert candidate(prices = [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19
    assert candidate(prices = [31, 41, 48, 54, 37, 76, 56, 99, 1, 180]) == 247
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 24
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 10]) == 12
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 10, 4]) == 13
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 18
    assert candidate(prices = [1, 100, 2, 98, 3, 96, 4, 94, 5, 92, 6, 90, 7, 88, 8, 86, 9, 84, 10, 82]) == 195
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 18
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(prices = [2, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 2
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 6, 8, 2, 5]) == 11
    assert candidate(prices = [100, 180, 260, 40, 310, 535, 695]) == 815
    assert candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 0
    assert candidate(prices = [8, 6, 4, 3, 3, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(prices = [5, 2, 10, 1, 3, 12, 6, 9, 1, 15]) == 25
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8, 10, 5, 6, 7, 3, 10, 4, 5, 6, 1, 10]) == 18
    assert candidate(prices = [5, 2, 4, 0, 0, 3, 5, 7, 8, 2, 8]) == 14
    assert candidate(prices = [1, 4, 3, 0, 5, 8, 3, 1, 5, 6, 4, 10, 2, 5, 12, 8, 9, 1, 10]) == 21
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 10, 8, 6, 2, 9, 5, 7, 1, 10]) == 19
    assert candidate(prices = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 3, 5, 7, 9, 11]) == 17
    assert candidate(prices = [100, 180, 260, 310, 40, 535, 695]) == 865
    assert candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9, 1, 2, 1, 3, 5, 7]) == 17
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 6, 8, 2, 5, 7, 8, 1]) == 14
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 10, 12, 15, 14, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 14]) == 22
    assert candidate(prices = [8, 12, 15, 7, 3, 18, 20, 15]) == 24
    assert candidate(prices = [100, 180, 260, 310, 40, 535, 695, 10, 5, 11, 3, 8, 10, 5, 11, 3, 8, 10, 5, 11]) == 865
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(prices = [5, 2, 3, 0, 3, 2, 5, 4, 1, 6, 7, 8, 1, 10]) == 17
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [5, 0, 3, 12, 6, 9, 21, 18, 13, 8, 12, 3, 20, 15, 18]) == 38
    assert candidate(prices = [90, 80, 70, 60, 50, 40, 30]) == 0
    assert candidate(prices = [10, 7, 5, 8, 11, 9, 1, 15]) == 20
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 11
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 18
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(prices = [100, 180, 260, 310, 40, 535, 695, 10, 20, 30, 100, 150]) == 865
    assert candidate(prices = [12, 14, 17, 10, 14, 13, 12, 15]) == 10
    assert candidate(prices = [3, 1, 4, 8, 7, 2, 5, 1, 3, 5, 2, 9]) == 15
    assert candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 8, 9, 10, 8, 12, 15]) == 16
    assert candidate(prices = [100, 30, 15, 10, 8, 25, 80]) == 72
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10]) == 18
    assert candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 5, 7, 3]) == 9
    assert candidate(prices = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, 1, 21, 1, 23, 1, 25, 1, 27]) == 50
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 10, 11, 12, 10, 13, 14, 15, 16, 17, 18, 19]) == 23
    assert candidate(prices = [30, 50, 10, 60, 40, 90, 55]) == 100
    assert candidate(prices = [8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5, 8, 6, 4, 3, 3, 5]) == 10
    assert candidate(prices = [5, 1, 7, 8, 3, 6, 1, 2, 9, 10, 4, 5, 11, 12, 6, 7, 13, 14, 8, 9]) == 20
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 135
    assert candidate(prices = [1, 2, 3, 1, 4, 5, 2, 7, 8, 1, 9, 10, 1, 11, 12, 1, 13, 14]) == 24
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 38
    assert candidate(prices = [10, 22, 5, 75, 65, 80, 10, 90, 50, 20, 120, 15, 8, 90]) == 197
    assert candidate(prices = [7, 6, 5, 8, 3, 8, 2, 6, 5, 7, 3, 8, 5, 6, 8, 9, 1, 2, 4, 5, 6]) == 12
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 10
    assert candidate(prices = [1, 7, 4, 3, 8, 8, 6, 4, 10, 9, 3]) == 13
    assert candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 1, 2, 5, 1, 3, 7]) == 11
    assert candidate(prices = [10, 22, 5, 75, 65, 80]) == 87
    assert candidate(prices = [3, 8, 4, 0, 5, 6, 2, 9, 8, 1, 10]) == 18
    assert candidate(prices = [1, 3, 2, 8, 4, 9, 3, 5, 7, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 29
    assert candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 17
    assert candidate(prices = [31, 41, 48, 54, 37, 44, 66, 59, 56, 78, 100]) == 86
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 10, 15, 20, 5, 25, 30, 5, 35, 40]) == 65
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4, 2, 5, 1, 4, 7, 1, 10]) == 16
    assert candidate(prices = [5, 3, 10, 1, 7, 8, 2, 9, 4]) == 15
    assert candidate(prices = [100, 30, 15, 10, 8, 25, 80, 50, 150, 40, 60, 70, 90, 120, 130, 50, 20, 100, 140, 150]) == 272
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 100, 101, 102, 103]) == 107
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 10, 9, 11, 12, 8, 10, 5, 7, 3, 4, 2, 1, 5, 6, 8, 9, 10, 1]) == 21
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 190
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]) == 11
    assert candidate(prices = [50, 10, 5, 3, 8, 20, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 67
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 21
    assert candidate(prices = [1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10, 1, 2, 3, 10]) == 18
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 9, 10, 15, 20, 2, 18, 25]) == 42
    assert candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 20
    assert candidate(prices = [80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(prices = [100, 180, 260, 40, 310, 535, 695]) == 815
    assert candidate(prices = [5, 3, 10, 1, 4, 9, 2, 8, 0, 7, 3, 6, 1, 5, 2, 4]) == 15


