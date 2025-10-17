def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(hours = [9, 7, 9, 7, 9, 7, 9, 7]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 7, 9, 7, 9, 7, 9, 7]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 16, 16, 16]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 16, 16, 16]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hours = [12, 13, 14, 15, 16, 0, 0, 0, 0, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [12, 13, 14, 15, 16, 0, 0, 0, 0, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 9, 2, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 9, 2, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [12, 8, 9, 9, 9, 10, 8, 8, 9, 10, 12]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [12, 8, 9, 9, 9, 10, 8, 8, 9, 10, 12]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 6, 0, 6, 6, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 6, 0, 6, 6, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [7, 7, 7, 9, 9, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [7, 7, 7, 9, 9, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 9, 2, 1, 0, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 9, 2, 1, 0, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 8, 10, 8, 10, 8, 10, 8, 10, 8]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 8, 10, 8, 10, 8, 10, 8, 10, 8]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 9, 6, 9, 6, 9, 6, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 9, 6, 9, 6, 9, 6, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 7, 8, 6, 4, 9, 8, 9, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 7, 8, 6, 4, 9, 8, 9, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [7, 7, 7, 7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [7, 7, 7, 7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 7, 9, 6, 11, 4, 5, 12, 3, 14, 1, 2, 8, 9, 15, 0, 1, 6, 7, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 7, 9, 6, 11, 4, 5, 12, 3, 14, 1, 2, 8, 9, 15, 0, 1, 6, 7, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 1, 8, 12, 8, 9, 5, 6, 7, 10, 3, 11, 4, 8, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 1, 8, 12, 8, 9, 5, 6, 7, 10, 3, 11, 4, 8, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(hours = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 6, 7, 8, 5, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 0, 8, 8, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 6, 7, 8, 5, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 0, 8, 8, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 10, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 10, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 7, 8, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 7, 8, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 5, 8, 10, 4, 6, 9, 11, 7, 3, 12, 8, 10, 9, 11, 13, 14, 6, 7, 8]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 5, 8, 10, 4, 6, 9, 11, 7, 3, 12, 8, 10, 9, 11, 13, 14, 6, 7, 8]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hours = [8, 9, 9, 10, 8, 8, 8, 8, 8, 9, 9, 10, 11, 12, 7, 6, 5, 4, 3, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [8, 9, 9, 10, 8, 8, 8, 8, 8, 9, 9, 10, 11, 12, 7, 6, 5, 4, 3, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(hours = [6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(hours = [9, 7, 9, 7, 9, 7, 9, 7]) == 7
    assert candidate(hours = [8, 9, 9, 10]) == 4
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9]) == 7
    assert candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 9
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(hours = [16, 16, 16, 16]) == 4
    assert candidate(hours = [12, 13, 14, 15, 16, 0, 0, 0, 0, 0]) == 9
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9]) == 1
    assert candidate(hours = [5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(hours = [8, 9, 9, 2, 5]) == 3
    assert candidate(hours = [12, 8, 9, 9, 9, 10, 8, 8, 9, 10, 12]) == 11
    assert candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10]) == 8
    assert candidate(hours = [9, 9, 6, 0, 6, 6, 9]) == 3
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15
    assert candidate(hours = [10, 10, 10, 10]) == 4
    assert candidate(hours = [6, 6, 6]) == 0
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8]) == 0
    assert candidate(hours = [7, 7, 7, 9, 9, 9]) == 5
    assert candidate(hours = [8, 9, 9, 2, 1, 0, 7]) == 3
    assert candidate(hours = [10, 8, 10, 8, 10, 8, 10, 8, 10, 8]) == 9
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 10
    assert candidate(hours = [6, 9, 6, 9, 6, 9, 6, 9]) == 7
    assert candidate(hours = [8, 9, 7, 8, 6, 4, 9, 8, 9, 8]) == 3
    assert candidate(hours = [7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(hours = [16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0]) == 25
    assert candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 27
    assert candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == 19
    assert candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 31
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 15
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 32
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 17
    assert candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4, 5]) == 15
    assert candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 101
    assert candidate(hours = [10, 7, 9, 6, 11, 4, 5, 12, 3, 14, 1, 2, 8, 9, 15, 0, 1, 6, 7, 10]) == 5
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 27
    assert candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 48
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 19
    assert candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12]) == 9
    assert candidate(hours = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 21
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == 1
    assert candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == 15
    assert candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 15
    assert candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 15
    assert candidate(hours = [16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3]) == 17
    assert candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]) == 1
    assert candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 27
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12]) == 20
    assert candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]) == 15
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]) == 21
    assert candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 33
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 31
    assert candidate(hours = [9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 20
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10]) == 1
    assert candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 15
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == 1
    assert candidate(hours = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 19
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31
    assert candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 10]) == 1
    assert candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 11
    assert candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 65
    assert candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 20
    assert candidate(hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8]) == 15
    assert candidate(hours = [10, 1, 8, 12, 8, 9, 5, 6, 7, 10, 3, 11, 4, 8, 10]) == 3
    assert candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 51
    assert candidate(hours = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1]) == 25
    assert candidate(hours = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]) == 32
    assert candidate(hours = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 19
    assert candidate(hours = [9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6]) == 19
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4]) == 15
    assert candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 31
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 20
    assert candidate(hours = [10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8]) == 19
    assert candidate(hours = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 16, 15, 14, 13, 12, 11]) == 11
    assert candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0
    assert candidate(hours = [1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8]) == 0
    assert candidate(hours = [8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]) == 19
    assert candidate(hours = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 20
    assert candidate(hours = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 19
    assert candidate(hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]) == 15
    assert candidate(hours = [9, 6, 7, 8, 5, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 0, 8, 8, 9]) == 15
    assert candidate(hours = [9, 10, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 20
    assert candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 9
    assert candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19
    assert candidate(hours = [9, 7, 8, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]) == 17
    assert candidate(hours = [10, 5, 8, 10, 4, 6, 9, 11, 7, 3, 12, 8, 10, 9, 11, 13, 14, 6, 7, 8]) == 19
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 29
    assert candidate(hours = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]) == 11
    assert candidate(hours = [8, 9, 9, 10, 8, 8, 8, 8, 8, 9, 9, 10, 11, 12, 7, 6, 5, 4, 3, 2]) == 15
    assert candidate(hours = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9]) == 3
    assert candidate(hours = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 51
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]) == 15
    assert candidate(hours = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == 33
    assert candidate(hours = [6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9, 6, 9]) == 21
    assert candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1


