def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 1, 0, 1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 1, 0, 1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 1, 0, 0, 0, 0, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 1, 0, 0, 0, 0, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 1, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 1, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 1, 0, 1, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 1, 0, 1, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 1, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 1, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(seats = [0, 0, 0, 1, 0, 1, 0, 0, 0]) == 3
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1]) == 2
    assert candidate(seats = [0, 0, 0, 1, 0, 0, 0]) == 3
    assert candidate(seats = [1, 0, 0, 0]) == 3
    assert candidate(seats = [0, 1]) == 1
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]) == 2
    assert candidate(seats = [1, 1, 0, 0, 0, 0, 1, 1]) == 2
    assert candidate(seats = [0, 0, 0, 1]) == 3
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 1]) == 4
    assert candidate(seats = [1, 0, 0, 1, 0, 0, 1]) == 1
    assert candidate(seats = [1, 0, 0, 0, 1, 0, 1]) == 2
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [0, 0, 1, 0, 1, 0, 1, 0, 0]) == 2
    assert candidate(seats = [0, 0, 1, 0, 1, 0, 0, 0]) == 3
    assert candidate(seats = [1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2
    assert candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [1, 0, 0, 1, 0, 0, 0, 1]) == 2
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 18
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 5
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19
    assert candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 4
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 27
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 29
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 22
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]) == 3
    assert candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]) == 10
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13
    assert candidate(seats = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
    assert candidate(seats = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == 6
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
    assert candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(seats = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 6
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 15
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]) == 3
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 9
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) == 9
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 51
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 19
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 16
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 4
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
    assert candidate(seats = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
    assert candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 18
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 33
    assert candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 11
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 31
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
    assert candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 7
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 13
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
    assert candidate(seats = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) == 17
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 4
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 5
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 23
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 13
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
    assert candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 25
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 14
    assert candidate(seats = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 1
    assert candidate(seats = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]) == 2
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 71
    assert candidate(seats = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12
    assert candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
    assert candidate(seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 11
    assert candidate(seats = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(seats = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) == 8
    assert candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3
    assert candidate(seats = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]) == 8
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
    assert candidate(seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(seats = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == 6
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 20
    assert candidate(seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 30
    assert candidate(seats = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]) == 3
    assert candidate(seats = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12
    assert candidate(seats = [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == 3


