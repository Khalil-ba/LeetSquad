def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 2, 3, 1, 0, 0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 2, 3, 1, 0, 0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 0, 2, 0, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 0, 2, 0, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 1, 0, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 1, 0, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 0, 3, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 0, 3, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 0, 2, 1, 0, 1, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 0, 2, 1, 0, 1, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 0, 0, 0, 3, 0, 0, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 0, 0, 0, 3, 0, 0, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 3, 3, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 3, 3, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 3, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 3, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 0, 1, 2, 3, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 0, 1, 2, 3, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 0, 2, 0, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 0, 2, 0, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 3, 0, 3, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 3, 0, 3, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 0, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 0, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 2, 1, 2, 3, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 2, 1, 2, 3, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 0, 3, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 0, 3, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 2, 2, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 2, 2, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 1, 2, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 1, 2, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 0, 1, 0, 3, 2, 0, 1, 0, 3, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 0, 1, 0, 3, 2, 0, 1, 0, 3, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 0, 2, 0, 3, 0, 0, 1, 0, 0, 0, 3, 0, 2, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 0, 2, 0, 3, 0, 0, 1, 0, 0, 0, 3, 0, 2, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 2, 0, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 2, 0, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 2, 1, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 2, 1, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 2, 3, 1, 2, 3, 1, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 2, 3, 1, 2, 3, 1, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 0]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 0]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 0, 2, 1, 3, 0, 1, 2, 3, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 0, 2, 1, 3, 0, 1, 2, 3, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 0, 0, 2, 3, 1, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 0, 0, 2, 3, 1, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(obstacles = [0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 1
    assert candidate(obstacles = [0, 0, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0]) == 4
    assert candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 1
    assert candidate(obstacles = [0, 1, 3, 2, 3, 1, 0, 0, 0, 0]) == 2
    assert candidate(obstacles = [0, 3, 0, 0, 2, 0, 0, 1, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 0, 0]) == 5
    assert candidate(obstacles = [0, 2, 1, 0, 3, 0]) == 2
    assert candidate(obstacles = [0, 1, 2, 0, 2, 1, 0, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 2, 0, 0, 0, 3, 0, 0, 1, 0]) == 2
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 0]) == 1
    assert candidate(obstacles = [0, 1, 1, 3, 3, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 1, 3, 0]) == 3
    assert candidate(obstacles = [0, 0, 1, 2, 3, 0]) == 2
    assert candidate(obstacles = [0, 3, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 2, 0, 2, 0, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 0, 3, 0, 3, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 3, 0]) == 2
    assert candidate(obstacles = [0, 1, 0, 0, 2, 0]) == 1
    assert candidate(obstacles = [0, 2, 3, 2, 1, 2, 3, 0]) == 3
    assert candidate(obstacles = [0, 3, 2, 1, 0, 0]) == 2
    assert candidate(obstacles = [0, 1, 2, 0, 3, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 1, 0, 0]) == 2
    assert candidate(obstacles = [0, 2, 2, 2, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 0]) == 5
    assert candidate(obstacles = [0, 3, 0, 1, 2, 0, 0, 0, 0, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 16
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 11
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 12
    assert candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 10
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 8
    assert candidate(obstacles = [0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 0]) == 2
    assert candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 20
    assert candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0]) == 7
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 4
    assert candidate(obstacles = [0, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 0]) == 5
    assert candidate(obstacles = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == 10
    assert candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 3
    assert candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10
    assert candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 0, 1, 0, 3, 2, 0, 1, 0, 3, 0]) == 4
    assert candidate(obstacles = [0, 1, 0, 0, 2, 0, 3, 0, 0, 1, 0, 0, 0, 3, 0, 2, 0]) == 3
    assert candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 0]) == 5
    assert candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10
    assert candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0]) == 10
    assert candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 4
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 18
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 13
    assert candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 12
    assert candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0]) == 7
    assert candidate(obstacles = [0, 3, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 1]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 0]) == 5
    assert candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0]) == 6
    assert candidate(obstacles = [0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 30
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 27
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1]) == 8
    assert candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 26
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1]) == 5
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11
    assert candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 25
    assert candidate(obstacles = [0, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 26
    assert candidate(obstacles = [0, 2, 2, 0, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 0]) == 5
    assert candidate(obstacles = [0, 3, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 6
    assert candidate(obstacles = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 0]) == 7
    assert candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 8
    assert candidate(obstacles = [0, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 8
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 6
    assert candidate(obstacles = [0, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 18
    assert candidate(obstacles = [0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0]) == 1
    assert candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 0]) == 4
    assert candidate(obstacles = [0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0]) == 6
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 19
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 31
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 2, 1, 0]) == 11
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0]) == 5
    assert candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 23
    assert candidate(obstacles = [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 0]) == 1
    assert candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 3
    assert candidate(obstacles = [0, 3, 2, 1, 2, 3, 1, 2, 3, 1, 0]) == 7
    assert candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1
    assert candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 17
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1
    assert candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
    assert candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 0]) == 12
    assert candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 1, 2, 3, 0, 2, 1, 3, 0, 1, 2, 3, 0]) == 6
    assert candidate(obstacles = [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3]) == 0
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11
    assert candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 17
    assert candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
    assert candidate(obstacles = [0, 0, 0, 2, 3, 1, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]) == 6
    assert candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 7
    assert candidate(obstacles = [0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0]) == 0
    assert candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 3
    assert candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1, 0]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 17
    assert candidate(obstacles = [0, 1, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 6
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 7
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 4
    assert candidate(obstacles = [0, 3, 2, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 9
    assert candidate(obstacles = [0, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 11
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9
    assert candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 11


