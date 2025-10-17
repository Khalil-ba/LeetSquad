def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 20, 20, 30, 30, 30, 30]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 20, 20, 30, 30, 30, 30]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 300, 300, 300, 300, 300]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 300, 300, 300, 300, 300]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000, 1000000000, 1000000000, 1000000000, 2000000000, 2000000000, 3000000000, 3000000000, 3000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000, 1000000000, 1000000000, 1000000000, 2000000000, 2000000000, 3000000000, 3000000000, 3000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [400, 400, 400, 400, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [400, 400, 400, 400, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 100, 100, 101, 101, 101, 101, 101, 102, 102, 102, 103, 103, 103, 103, 103, 103, 104, 104]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 100, 100, 101, 101, 101, 101, 101, 102, 102, 102, 103, 103, 103, 103, 103, 103, 104, 104]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 5
    assert candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 5
    assert candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 7
    assert candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 4
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 5
    assert candidate(tasks = [1]) == -1
    assert candidate(tasks = [2, 3, 3]) == -1
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(tasks = [2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 7
    assert candidate(tasks = [1, 1, 1, 1, 1, 1]) == 2
    assert candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8
    assert candidate(tasks = [10, 10, 10, 20, 20, 30, 30, 30, 30]) == 4
    assert candidate(tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5]) == -1
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(tasks = [5, 5, 5, 5, 5, 5]) == 2
    assert candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]) == 6
    assert candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 3]) == -1
    assert candidate(tasks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 4
    assert candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 15
    assert candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == -1
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
    assert candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 9
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 11
    assert candidate(tasks = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13
    assert candidate(tasks = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 300, 300, 300, 300, 300]) == 10
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 14
    assert candidate(tasks = [1000000000, 1000000000, 1000000000, 1000000000, 2000000000, 2000000000, 3000000000, 3000000000, 3000000000]) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 16
    assert candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 15
    assert candidate(tasks = [400, 400, 400, 400, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700]) == 9
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13
    assert candidate(tasks = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 17
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 16
    assert candidate(tasks = [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 14
    assert candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == -1
    assert candidate(tasks = [100, 100, 100, 101, 101, 101, 101, 101, 102, 102, 102, 103, 103, 103, 103, 103, 103, 104, 104]) == 7
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 16
    assert candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 13
    assert candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == -1
    assert candidate(tasks = [7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 11
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 8
    assert candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 19
    assert candidate(tasks = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 15
    assert candidate(tasks = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 13
    assert candidate(tasks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 12
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == -1
    assert candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 10
    assert candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 14
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7
    assert candidate(tasks = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 14
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9


