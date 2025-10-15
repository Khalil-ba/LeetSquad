def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(flips = [5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 3, 5, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 3, 5, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [3, 2, 4, 1, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [3, 2, 4, 1, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [4, 1, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [4, 1, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 5, 3, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 5, 3, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 1, 4, 3, 2, 7, 6, 9, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 1, 4, 3, 2, 7, 6, 9, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 3, 1, 5, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 3, 1, 5, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 4, 3, 2, 5, 8, 6, 7, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 4, 3, 2, 5, 8, 6, 7, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [3, 1, 4, 2, 5, 7, 6, 9, 8, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [3, 1, 4, 2, 5, 7, 6, 9, 8, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [3, 1, 2, 6, 5, 4, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [3, 1, 2, 6, 5, 4, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 2, 5, 4, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 2, 5, 4, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 5, 6, 1, 4, 3, 8, 9, 7, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 5, 6, 1, 4, 3, 8, 9, 7, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 7, 2, 4, 6, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 7, 2, 4, 6, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [6, 1, 3, 5, 2, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [6, 1, 3, 5, 2, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [14, 12, 10, 8, 6, 4, 2, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [14, 12, 10, 8, 6, 4, 2, 15, 13, 11, 9, 7, 5, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(flips = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [6, 3, 1, 4, 2, 5, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [6, 3, 1, 4, 2, 5, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 5, 4, 3, 6, 8, 7, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 5, 4, 3, 6, 8, 7, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 11]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 11]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 5, 3, 4, 2, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 5, 3, 4, 2, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(flips = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 2, 4, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 2, 4, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(flips = [6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 5, 4, 3, 6, 8, 7, 10, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 5, 4, 3, 6, 8, 7, 10, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(flips = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 3, 1, 2, 4, 6, 8, 7, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 3, 1, 2, 4, 6, 8, 7, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 3, 1, 5, 4, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 3, 1, 5, 4, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 1, 4, 3, 2, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 1, 4, 3, 2, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 2, 3, 1, 4, 6, 8, 7, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 2, 3, 1, 4, 6, 8, 7, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 5, 8, 7, 9, 3, 1, 2, 4, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 5, 8, 7, 9, 3, 1, 2, 4, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 2, 5, 4, 6, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 2, 5, 4, 6, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 2, 5, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 2, 5, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 5, 3, 6, 4, 7, 8, 10, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 5, 3, 6, 4, 7, 8, 10, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(flips = [7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 2, 4, 6, 8, 7, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 2, 4, 6, 8, 7, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 1, 3, 2, 6, 4, 8, 7, 10, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 1, 3, 2, 6, 4, 8, 7, 10, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 5, 8, 7, 3, 2, 9, 4, 6, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 5, 8, 7, 3, 2, 9, 4, 6, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 5, 2, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 5, 2, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 5, 2, 6, 3, 7, 4, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 5, 2, 6, 3, 7, 4, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 4, 2, 3, 7, 5, 6, 10, 8, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 4, 2, 3, 7, 5, 6, 10, 8, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [3, 1, 2, 5, 4, 6, 8, 7, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [3, 1, 2, 5, 4, 6, 8, 7, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(flips = [6, 3, 1, 5, 2, 4, 10, 7, 9, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [6, 3, 1, 5, 2, 4, 10, 7, 9, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 5, 4, 3, 8, 6, 7, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 5, 4, 3, 8, 6, 7, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 4, 3, 6, 5, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 4, 3, 6, 5, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 2, 1, 3, 4, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 2, 1, 3, 4, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 10, 5, 4, 9, 6, 7, 3, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 10, 5, 4, 9, 6, 7, 3, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 3, 1, 5, 6, 4, 8, 7, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 3, 1, 5, 6, 4, 8, 7, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(flips = [7, 1, 2, 3, 4, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [7, 1, 2, 3, 4, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 5, 3, 4, 2, 6, 7, 8, 10, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 5, 3, 4, 2, 6, 7, 8, 10, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 1, 3, 5, 4, 6, 7, 8]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 1, 3, 5, 4, 6, 7, 8]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 3, 4, 5, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 3, 4, 5, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(flips = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(flips = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [10, 5, 1, 6, 2, 7, 3, 8, 4, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [10, 5, 1, 6, 2, 7, 3, 8, 4, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(flips = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flips = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(flips = [5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [1, 2, 3, 4, 5]) == 5
    assert candidate(flips = [2, 1, 3, 5, 4]) == 3
    assert candidate(flips = [3, 2, 4, 1, 5]) == 2
    assert candidate(flips = [4, 1, 2, 3]) == 1
    assert candidate(flips = [2, 1, 5, 3, 4]) == 2
    assert candidate(flips = [5, 1, 4, 3, 2, 7, 6, 9, 8, 10]) == 4
    assert candidate(flips = [2, 3, 1, 5, 4]) == 2
    assert candidate(flips = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == 6
    assert candidate(flips = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3
    assert candidate(flips = [1, 4, 3, 2, 5, 8, 6, 7, 10, 9]) == 5
    assert candidate(flips = [3, 1, 4, 2, 5, 7, 6, 9, 8, 10]) == 5
    assert candidate(flips = [3, 1, 2, 6, 5, 4, 7, 8, 9, 10]) == 6
    assert candidate(flips = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11]) == 6
    assert candidate(flips = [1, 3, 2, 5, 4, 6]) == 4
    assert candidate(flips = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 3
    assert candidate(flips = [2, 5, 6, 1, 4, 3, 8, 9, 7, 10]) == 3
    assert candidate(flips = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 6
    assert candidate(flips = [1, 3, 5, 7, 2, 4, 6, 8, 9, 10]) == 5
    assert candidate(flips = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]) == 2
    assert candidate(flips = [6, 1, 3, 5, 2, 4]) == 1
    assert candidate(flips = [14, 12, 10, 8, 6, 4, 2, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
    assert candidate(flips = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 5
    assert candidate(flips = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10]) == 5
    assert candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(flips = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(flips = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 2
    assert candidate(flips = [6, 3, 1, 4, 2, 5, 7, 8, 9, 10]) == 5
    assert candidate(flips = [2, 1, 5, 4, 3, 6, 8, 7, 10, 9]) == 5
    assert candidate(flips = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]) == 6
    assert candidate(flips = [5, 2, 3, 4, 1, 6, 7, 8, 9, 10]) == 6
    assert candidate(flips = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 6
    assert candidate(flips = [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]) == 2
    assert candidate(flips = [10, 1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 11]) == 1
    assert candidate(flips = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [1, 5, 3, 4, 2, 6, 7, 8, 9, 10]) == 7
    assert candidate(flips = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 5
    assert candidate(flips = [1, 3, 5, 2, 4, 6]) == 3
    assert candidate(flips = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 22
    assert candidate(flips = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]) == 7
    assert candidate(flips = [6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [1, 2, 5, 4, 3, 6, 8, 7, 10, 9]) == 6
    assert candidate(flips = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 7
    assert candidate(flips = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [5, 3, 1, 2, 4, 6, 8, 7, 10, 9]) == 4
    assert candidate(flips = [2, 3, 1, 5, 4, 6, 7, 8, 9, 10]) == 7
    assert candidate(flips = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 9
    assert candidate(flips = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9]) == 7
    assert candidate(flips = [5, 1, 4, 3, 2, 6]) == 2
    assert candidate(flips = [5, 2, 3, 1, 4, 6, 8, 7, 10, 9]) == 4
    assert candidate(flips = [10, 5, 8, 7, 9, 3, 1, 2, 4, 6]) == 1
    assert candidate(flips = [1, 3, 2, 5, 4, 6, 7]) == 5
    assert candidate(flips = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]) == 2
    assert candidate(flips = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10]) == 3
    assert candidate(flips = [1, 3, 2, 5, 4]) == 3
    assert candidate(flips = [1, 2, 5, 3, 6, 4, 7, 8, 10, 9]) == 6
    assert candidate(flips = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]) == 3
    assert candidate(flips = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(flips = [7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [1, 3, 5, 2, 4, 6, 8, 7, 10, 9]) == 5
    assert candidate(flips = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(flips = [5, 1, 3, 2, 6, 4, 8, 7, 10, 9]) == 3
    assert candidate(flips = [10, 5, 8, 7, 3, 2, 9, 4, 6, 1]) == 1
    assert candidate(flips = [1, 3, 5, 2, 4]) == 2
    assert candidate(flips = [1, 5, 2, 6, 3, 7, 4, 8, 9, 10]) == 5
    assert candidate(flips = [1, 4, 2, 3, 7, 5, 6, 10, 8, 9]) == 4
    assert candidate(flips = [3, 1, 2, 5, 4, 6, 8, 7, 10, 9]) == 5
    assert candidate(flips = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]) == 7
    assert candidate(flips = [6, 3, 1, 5, 2, 4, 10, 7, 9, 8]) == 2
    assert candidate(flips = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10]) == 3
    assert candidate(flips = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]) == 9
    assert candidate(flips = [2, 1, 5, 4, 3, 8, 6, 7, 10, 9]) == 4
    assert candidate(flips = [2, 1, 4, 3, 6, 5, 7]) == 4
    assert candidate(flips = [5, 2, 1, 3, 4, 6, 7, 8, 9, 10]) == 6
    assert candidate(flips = [1, 2, 10, 5, 4, 9, 6, 7, 3, 8]) == 3
    assert candidate(flips = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]) == 1
    assert candidate(flips = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(flips = [2, 3, 1, 5, 6, 4, 8, 7, 10, 9]) == 4
    assert candidate(flips = [7, 1, 2, 3, 4, 5, 6]) == 1
    assert candidate(flips = [1, 5, 3, 4, 2, 6, 7, 8, 10, 9]) == 6
    assert candidate(flips = [2, 1, 3, 5, 4, 6, 7, 8]) == 6
    assert candidate(flips = [1, 2, 3, 4, 5, 6]) == 6
    assert candidate(flips = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]) == 8
    assert candidate(flips = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 26
    assert candidate(flips = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(flips = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
    assert candidate(flips = [10, 5, 1, 6, 2, 7, 3, 8, 4, 9]) == 1
    assert candidate(flips = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 6


