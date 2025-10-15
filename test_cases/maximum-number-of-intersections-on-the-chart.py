def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 1, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 1, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [2, 1, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [2, 1, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [3, 5, 3, 7, 3, 5, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [3, 5, 3, 7, 3, 5, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 2, 1, 3, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 2, 1, 3, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 45, 35, 25, 15, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 45, 35, 25, 15, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 200, 150, 300, 250, 350, 400, 350, 400, 350, 400, 350, 400, 350, 400]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 200, 150, 300, 250, 350, 400, 350, 400, 350, 400, 350, 400, 350, 400]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 1, 6, 2, 7, 3, 8, 4, 9, 5, 10, 6, 9, 5, 8, 4, 7, 3, 6, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 1, 6, 2, 7, 3, 8, 4, 9, 5, 10, 6, 9, 5, 8, 4, 7, 3, 6, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 1000000000, 999999999, 1, 999999998, 2, 999999997, 3, 999999996, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 1000000000, 999999999, 1, 999999998, 2, 999999997, 3, 999999996, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 4, 6, 7, 8, 6, 4, 2, 3, 5, 7, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 4, 6, 7, 8, 6, 4, 2, 3, 5, 7, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100, 200, 300, 400, 500, 600, 500, 400, 300, 200]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100, 200, 300, 400, 500, 600, 500, 400, 300, 200]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 30, 20, 10, 30, 20, 10, 30, 20, 10, 30, 20, 10, 30, 20, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 30, 20, 10, 30, 20, 10, 30, 20, 10, 30, 20, 10, 30, 20, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 6, 3, 7, 2, 8, 1, 9, 10, 8, 9, 7, 10, 6, 11, 5, 12, 4, 13]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 6, 3, 7, 2, 8, 1, 9, 10, 8, 9, 7, 10, 6, 11, 5, 12, 4, 13]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500, 450, 550, 500, 600, 550, 650]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500, 450, 550, 500, 600, 550, 650]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 15, 25, 20, 30, 25, 35, 30]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 15, 25, 20, 30, 25, 35, 30]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 999999999, 1000000000, 999999999]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 999999999, 1000000000, 999999999]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 10, 30, 20, 40, 30, 50, 40]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 10, 30, 20, 40, 30, 50, 40]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 3, 8, 6, 7, 4, 2, 9, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 3, 8, 6, 7, 4, 2, 9, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 10, 30, 20, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 10, 30, 20, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 3, 2, 1, 4, 3, 2, 3, 4, 3, 2, 1, 2, 1, 3, 2, 1, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 3, 2, 1, 4, 3, 2, 3, 4, 3, 2, 1, 2, 1, 3, 2, 1, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 3, 6, 3, 7, 3, 8, 3, 9, 3, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 3, 6, 3, 7, 3, 8, 3, 9, 3, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 1, 2, 3, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 1, 2, 3, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 5, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 5, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 1, 4, 3, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 1, 4, 3, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [3, 5, 4, 6, 7, 8, 6, 5, 4, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [3, 5, 4, 6, 7, 8, 6, 5, 4, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 3, 8, 6, 7, 2, 9, 4, 1, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 3, 8, 6, 7, 2, 9, 4, 1, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(y = [999999999, 1, 999999998, 2, 999999997, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [999999999, 1, 999999998, 2, 999999997, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 1, 1000000000, 1, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 10, 3, 9, 5, 8, 7, 6, 2, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 10, 3, 9, 5, 8, 7, 6, 2, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 1, 5, 2, 5, 3, 5, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 1, 5, 2, 5, 3, 5, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 15, 25, 30, 25, 35, 40]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 15, 25, 30, 25, 35, 40]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 1, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 1, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 2, 1, 3, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 2, 1, 3, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 1, 1000000000, 1, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 1, 3, 2, 1, 3, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 1, 3, 2, 1, 3, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 1, 3, 1, 2, 1, 4, 1, 3, 1, 2, 1, 5, 1, 4, 1, 3, 1, 2]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 1, 3, 1, 2, 1, 4, 1, 3, 1, 2, 1, 5, 1, 4, 1, 3, 1, 2]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 30, 40, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 30, 40, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 1000000000, 1, 1000000000, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 1000000000, 1, 1000000000, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [2, 1, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [2, 1, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 9, 10, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 9, 10, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [1000000000, 999999999, 1000000000, 999999999]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1000000000, 999999999, 1000000000, 999999999]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(y = [10, 20, 10, 20, 10, 20, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [10, 20, 10, 20, 10, 20, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(y = [1, 3, 2, 3, 4, 3, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(y = [1, 3, 2, 3, 4, 3, 5]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(y = [1, 3, 2, 3, 1, 4, 3, 2, 1]) == 6
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
    assert candidate(y = [2, 1, 3, 4, 5]) == 2
    assert candidate(y = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(y = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 3
    assert candidate(y = [3, 5, 3, 7, 3, 5, 3]) == 6
    assert candidate(y = [1, 2, 1, 2, 1, 3, 2]) == 5
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6]) == 3
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(y = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 9
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 19
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 10
    assert candidate(y = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 19
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 45, 35, 25, 15, 5]) == 4
    assert candidate(y = [1, 3, 2, 4, 3, 2, 5, 4, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(y = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
    assert candidate(y = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(y = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 2
    assert candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 4
    assert candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6
    assert candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 6
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
    assert candidate(y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(y = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 15
    assert candidate(y = [100, 200, 150, 300, 250, 350, 400, 350, 400, 350, 400, 350, 400, 350, 400]) == 9
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(y = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 7
    assert candidate(y = [5, 1, 6, 2, 7, 3, 8, 4, 9, 5, 10, 6, 9, 5, 8, 4, 7, 3, 6, 2, 1]) == 16
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 6
    assert candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(y = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 4
    assert candidate(y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 3
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(y = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19
    assert candidate(y = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 2
    assert candidate(y = [1, 3, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5]) == 13
    assert candidate(y = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 19
    assert candidate(y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 17
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 3
    assert candidate(y = [5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3, 5, 3, 1, 3]) == 10
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 10
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 18
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 3
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(y = [1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]) == 9
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 2
    assert candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 15
    assert candidate(y = [1, 1000000000, 999999999, 1, 999999998, 2, 999999997, 3, 999999996, 4]) == 8
    assert candidate(y = [1, 3, 5, 4, 6, 7, 8, 6, 4, 2, 3, 5, 7, 9]) == 5
    assert candidate(y = [1, 3, 2, 4, 3, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 29
    assert candidate(y = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500]) == 3
    assert candidate(y = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100, 200, 300, 400, 500, 600, 500, 400, 300, 200]) == 4
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 9
    assert candidate(y = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9]) == 3
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(y = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 19
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 19
    assert candidate(y = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 23
    assert candidate(y = [10, 20, 30, 20, 10, 30, 20, 10, 30, 20, 10, 30, 20, 10, 30, 20, 10]) == 10
    assert candidate(y = [1, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]) == 3
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 7
    assert candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 2
    assert candidate(y = [5, 4, 6, 3, 7, 2, 8, 1, 9, 10, 8, 9, 7, 10, 6, 11, 5, 12, 4, 13]) == 11
    assert candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 5
    assert candidate(y = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6]) == 3
    assert candidate(y = [1, 2, 3, 2, 1, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9]) == 3
    assert candidate(y = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500, 450, 550, 500, 600, 550, 650]) == 3
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == 3
    assert candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
    assert candidate(y = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 18
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]) == 3
    assert candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 7
    assert candidate(y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 6
    assert candidate(y = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2
    assert candidate(y = [10, 20, 15, 25, 20, 30, 25, 35, 30]) == 3
    assert candidate(y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 3
    assert candidate(y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 3
    assert candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 9
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4]) == 3
    assert candidate(y = [1000000000, 999999999, 1000000000, 999999999]) == 3
    assert candidate(y = [10, 20, 10, 30, 20, 40, 30, 50, 40]) == 3
    assert candidate(y = [5, 3, 8, 6, 7, 4, 2, 9, 1]) == 6
    assert candidate(y = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 9
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 3
    assert candidate(y = [10, 20, 10, 30, 20, 10]) == 4
    assert candidate(y = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1
    assert candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
    assert candidate(y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    assert candidate(y = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 9
    assert candidate(y = [1, 2, 1, 3, 2, 1, 4, 3, 2, 3, 4, 3, 2, 1, 2, 1, 3, 2, 1, 4]) == 11
    assert candidate(y = [5, 3, 6, 3, 7, 3, 8, 3, 9, 3, 10]) == 10
    assert candidate(y = [1, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1, 3, 2, 3, 1, 2, 3, 1]) == 6
    assert candidate(y = [1, 3, 2, 4, 5, 3, 4]) == 3
    assert candidate(y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 3
    assert candidate(y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 1
    assert candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 4
    assert candidate(y = [5, 4, 3, 2, 1]) == 1
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4
    assert candidate(y = [1, 3, 2, 3, 1, 4, 3, 5]) == 5
    assert candidate(y = [3, 5, 4, 6, 7, 8, 6, 5, 4, 3]) == 4
    assert candidate(y = [5, 3, 8, 6, 7, 2, 9, 4, 1, 10]) == 7
    assert candidate(y = [999999999, 1, 999999998, 2, 999999997, 3]) == 5
    assert candidate(y = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70]) == 3
    assert candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 3
    assert candidate(y = [1, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1000000000, 1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000, 5]) == 9
    assert candidate(y = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 3
    assert candidate(y = [1000000000, 999999999, 1000000000, 999999999, 1000000000]) == 4
    assert candidate(y = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 19
    assert candidate(y = [5, 4, 3, 2, 1]) == 1
    assert candidate(y = [1, 10, 3, 9, 5, 8, 7, 6, 2, 4]) == 6
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4
    assert candidate(y = [5, 1, 5, 2, 5, 3, 5, 4, 5]) == 8
    assert candidate(y = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [10, 20, 15, 25, 30, 25, 35, 40]) == 3
    assert candidate(y = [1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9]) == 3
    assert candidate(y = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(y = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 5
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4]) == 3
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [1, 3, 2, 3, 1, 4, 3, 2, 1]) == 6
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6
    assert candidate(y = [1, 2, 1, 2, 1, 3, 2]) == 5
    assert candidate(y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 1
    assert candidate(y = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
    assert candidate(y = [1, 3, 2, 1, 3, 2, 1, 3, 2]) == 6
    assert candidate(y = [1, 2, 1, 3, 1, 2, 1, 4, 1, 3, 1, 2, 1, 5, 1, 4, 1, 3, 1, 2]) == 19
    assert candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 6
    assert candidate(y = [1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5
    assert candidate(y = [5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 8]) == 3
    assert candidate(y = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
    assert candidate(y = [10, 20, 30, 40, 50]) == 1
    assert candidate(y = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [1, 1000000000, 1, 1000000000, 1]) == 4
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 3
    assert candidate(y = [2, 1, 3, 4, 5]) == 2
    assert candidate(y = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5]) == 8
    assert candidate(y = [10, 9, 10, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 3, 2, 1]) == 4
    assert candidate(y = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 9
    assert candidate(y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(y = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 9
    assert candidate(y = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 3
    assert candidate(y = [1000000000, 999999999, 1000000000, 999999999]) == 3
    assert candidate(y = [10, 20, 10, 20, 10, 20, 10]) == 6
    assert candidate(y = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 8
    assert candidate(y = [1, 3, 2, 3, 4, 3, 5]) == 3


