def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(fruits = [0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 0, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 0, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 1, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 1, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 2, 1, 2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 2, 1, 2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [10, 20, 10, 20, 30, 40, 50, 10, 20, 30, 10, 20, 10, 20, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [10, 20, 10, 20, 30, 40, 50, 10, 20, 30, 10, 20, 10, 20, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 5, 5, 6, 6, 5, 6, 5, 5, 5, 7, 7, 7, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 5, 5, 6, 6, 5, 6, 5, 5, 5, 7, 7, 7, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 3, 2, 1, 1, 2, 2, 1, 3, 3, 3, 2, 1, 1, 2, 2, 3, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 3, 2, 1, 1, 2, 2, 1, 3, 3, 3, 2, 1, 1, 2, 2, 3, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 1, 2, 2, 3, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 1, 2, 2, 3, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [3, 3, 3, 1, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [3, 3, 3, 1, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3, 3, 3, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3, 3, 3, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 1, 1, 0, 1, 2, 2, 1, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 1, 1, 0, 1, 2, 2, 1, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [3, 3, 3, 1, 2, 2, 1, 1, 1, 2, 2, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [3, 3, 3, 1, 2, 2, 1, 1, 1, 2, 2, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 3, 2, 1, 2, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 3, 2, 1, 2, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(fruits = [1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(fruits = [1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(fruits = [0]) == 1
    assert candidate(fruits = [1, 2, 3, 2, 2]) == 4
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    assert candidate(fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5
    assert candidate(fruits = [0, 0, 1, 1]) == 4
    assert candidate(fruits = [1]) == 1
    assert candidate(fruits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 7
    assert candidate(fruits = [1, 2, 3, 4, 5]) == 2
    assert candidate(fruits = [1, 2, 1]) == 3
    assert candidate(fruits = [0, 0, 0, 0, 0]) == 5
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 9
    assert candidate(fruits = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]) == 10
    assert candidate(fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert candidate(fruits = [0, 1, 2, 2]) == 3
    assert candidate(fruits = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3
    assert candidate(fruits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2]) == 6
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 22
    assert candidate(fruits = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2]) == 21
    assert candidate(fruits = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 6
    assert candidate(fruits = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1]) == 20
    assert candidate(fruits = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 3
    assert candidate(fruits = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 3
    assert candidate(fruits = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(fruits = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
    assert candidate(fruits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]) == 2
    assert candidate(fruits = [1, 2, 3, 4, 2, 1, 2, 3, 4]) == 3
    assert candidate(fruits = [10, 20, 10, 20, 30, 40, 50, 10, 20, 30, 10, 20, 10, 20, 10]) == 5
    assert candidate(fruits = [1, 2, 3, 4, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == 7
    assert candidate(fruits = [1, 2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1]) == 10
    assert candidate(fruits = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 3
    assert candidate(fruits = [5, 5, 5, 6, 6, 5, 6, 5, 5, 5, 7, 7, 7, 5, 5]) == 10
    assert candidate(fruits = [1, 2, 3, 3, 2, 1, 1, 2, 2, 1, 3, 3, 3, 2, 1, 1, 2, 2, 3, 3]) == 6
    assert candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert candidate(fruits = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]) == 2
    assert candidate(fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 3]) == 5
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3]) == 7
    assert candidate(fruits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 1, 2, 2, 3, 3]) == 5
    assert candidate(fruits = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 3
    assert candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(fruits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(fruits = [1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2]) == 12
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]) == 6
    assert candidate(fruits = [1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2]) == 20
    assert candidate(fruits = [3, 3, 3, 1, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 7
    assert candidate(fruits = [1, 2, 1, 2, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2]) == 9
    assert candidate(fruits = [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 29
    assert candidate(fruits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 10
    assert candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(fruits = [1, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3, 3, 3, 1, 2, 1]) == 5
    assert candidate(fruits = [1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2]) == 14
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 18
    assert candidate(fruits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(fruits = [0, 1, 1, 0, 1, 2, 2, 1, 0, 0]) == 5
    assert candidate(fruits = [1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1]) == 8
    assert candidate(fruits = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == 6
    assert candidate(fruits = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6]) == 15
    assert candidate(fruits = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == 16
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 46
    assert candidate(fruits = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3
    assert candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert candidate(fruits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(fruits = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2]) == 30
    assert candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert candidate(fruits = [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]) == 18
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 16
    assert candidate(fruits = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 8
    assert candidate(fruits = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2]) == 12
    assert candidate(fruits = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 62
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1]) == 10
    assert candidate(fruits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 12
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    assert candidate(fruits = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4
    assert candidate(fruits = [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2]) == 24
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(fruits = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 3
    assert candidate(fruits = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(fruits = [1, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1]) == 9
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
    assert candidate(fruits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 31
    assert candidate(fruits = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1]) == 6
    assert candidate(fruits = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4
    assert candidate(fruits = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 26
    assert candidate(fruits = [3, 3, 3, 1, 2, 2, 1, 1, 1, 2, 2, 2]) == 9
    assert candidate(fruits = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1]) == 6
    assert candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert candidate(fruits = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 3
    assert candidate(fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(fruits = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 71
    assert candidate(fruits = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3]) == 6
    assert candidate(fruits = [1, 2, 1, 3, 2, 1, 2, 1, 2]) == 5
    assert candidate(fruits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert candidate(fruits = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 12
    assert candidate(fruits = [1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 4


