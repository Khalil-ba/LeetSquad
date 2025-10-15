def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0'], ['W', 'W', 'W'], ['E', 'E', 'E']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0'], ['W', 'W', 'W'], ['E', 'E', 'E']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'W', 'E'], ['E', '0', 'W', 'E'], ['E', 'E', 'E', 'E']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'W', 'E'], ['E', '0', 'W', 'E'], ['E', 'E', 'E', 'E']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', '0'], ['E', 'E', '0', 'E'], ['E', '0', 'E', 'E'], ['0', 'E', 'E', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', '0'], ['E', 'E', '0', 'E'], ['E', '0', 'E', 'E'], ['0', 'E', 'E', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', 'W'], ['0', '0', '0'], ['E', 'E', 'E']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', 'W'], ['0', '0', '0'], ['E', 'E', 'E']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', '0', '0', '0', '0']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', '0', '0', '0', '0']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'W', 'E', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E'], ['E', 'W', 'E', 'W', 'E', 'W', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E'], ['0', 'E', 'W', 'E', 'E', '0', 'E']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'W', 'E', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E'], ['E', 'W', 'E', 'W', 'E', 'W', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E'], ['0', 'E', 'W', 'E', 'E', '0', 'E']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', 'E', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', 'E', '0', '0', '0']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', 'E', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', 'E', '0', '0', '0']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'W', '0', 'W', '0', 'W', '0'], ['W', '0', 'W', '0', 'W', '0', 'W'], ['0', 'W', '0', 'W', '0', 'W', '0'], ['W', '0', 'W', '0', 'W', '0', 'W'], ['0', 'W', '0', 'W', '0', 'W', '0']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'W', '0', 'W', '0', 'W', '0'], ['W', '0', 'W', '0', 'W', '0', 'W'], ['0', 'W', '0', 'W', '0', 'W', '0'], ['W', '0', 'W', '0', 'W', '0', 'W'], ['0', 'W', '0', 'W', '0', 'W', '0']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['0', '0', '0', '0', '0', '0', '0', '0']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['0', '0', '0', '0', '0', '0', '0', '0']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', 'W', '0', '0', '0'], ['0', 'E', '0', '0', '0', 'E', '0'], ['W', '0', '0', '0', '0', '0', 'W'], ['0', 'E', '0', '0', '0', 'E', '0'], ['0', '0', '0', 'W', '0', '0', '0']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', 'W', '0', '0', '0'], ['0', 'E', '0', '0', '0', 'E', '0'], ['W', '0', '0', '0', '0', '0', 'W'], ['0', 'E', '0', '0', '0', 'E', '0'], ['0', '0', '0', 'W', '0', '0', '0']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', 'W', 'W', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', 'W', 'W', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', '0', '0'], ['0', '0', '0', 'W', '0'], ['E', 'E', 'E', 'E', '0'], ['0', '0', 'W', 'E', 'E'], ['E', '0', '0', '0', '0']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', '0', '0'], ['0', '0', '0', 'W', '0'], ['E', 'E', 'E', 'E', '0'], ['0', '0', 'W', 'E', 'E'], ['E', '0', '0', '0', '0']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', '0'], ['E', 'E', '0', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['0', '0', '0', '0', '0']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', '0'], ['E', 'E', '0', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['0', '0', '0', '0', '0']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', '0', '0', '0', '0', '0', 'E'], ['E', '0', 'W', 'W', 'W', 'W', '0', 'E'], ['E', '0', 'W', '0', '0', 'W', '0', 'E'], ['E', '0', 'W', 'W', 'W', 'W', '0', 'E'], ['E', '0', '0', '0', '0', '0', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', '0', '0', '0', '0', '0', 'E'], ['E', '0', 'W', 'W', 'W', 'W', '0', 'E'], ['E', '0', 'W', '0', '0', 'W', '0', 'E'], ['E', '0', 'W', 'W', 'W', 'W', '0', 'E'], ['E', '0', '0', '0', '0', '0', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', 'E', 'W', 'W'], ['W', 'W', '0', 'W', 'W'], ['E', '0', 'E', '0', 'E'], ['W', 'W', '0', 'W', 'W'], ['W', 'W', 'E', 'W', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', 'E', 'W', 'W'], ['W', 'W', '0', 'W', 'W'], ['E', '0', 'E', '0', 'E'], ['W', 'W', '0', 'W', 'W'], ['W', 'W', 'E', 'W', 'W']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', 'E', 'E'], ['0', 'W', 'W', 'W', 'W'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['E', 'W', 'E', '0', '0']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', 'E', 'E'], ['0', 'W', 'W', 'W', 'W'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['E', 'W', 'E', '0', '0']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'W', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0', '0'], ['E', 'W', 'E', '0', 'E', '0'], ['W', 'E', '0', 'E', 'E', 'W']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'W', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0', '0'], ['E', 'W', 'E', '0', 'E', '0'], ['W', 'E', '0', 'E', 'E', 'W']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'W', '0', '0', '0'], ['0', 'E', 'E', '0', 'W'], ['0', 'E', '0', 'E', '0'], ['W', 'E', 'E', 'E', 'W'], ['0', '0', 'E', '0', 'E']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'W', '0', '0', '0'], ['0', 'E', 'E', '0', 'W'], ['0', 'E', '0', 'E', '0'], ['W', 'E', 'E', 'E', 'W'], ['0', '0', 'E', '0', 'E']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', '0', 'E', 'E'], ['0', '0', '0', '0', '0'], ['E', 'E', '0', 'E', 'E'], ['0', '0', '0', '0', '0'], ['E', 'E', '0', 'E', 'E']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', '0', 'E', 'E'], ['0', '0', '0', '0', '0'], ['E', 'E', '0', 'E', 'E'], ['0', '0', '0', '0', '0'], ['E', 'E', '0', 'E', 'E']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', 'W', '0', 'E', '0'], ['E', '0', '0', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', '0', 'E', 'W'], ['0', '0', 'E', '0', 'E', '0', '0'], ['E', '0', '0', 'E', '0', '0', 'E'], ['0', 'E', '0', '0', 'E', 'E', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', 'W', '0', 'E', '0'], ['E', '0', '0', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', '0', 'E', 'W'], ['0', '0', 'E', '0', 'E', '0', '0'], ['E', '0', '0', 'E', '0', '0', 'E'], ['0', 'E', '0', '0', 'E', 'E', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W', '0'], ['E', '0', 'E', '0', 'E', '0', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W', '0'], ['E', '0', 'E', '0', 'E', '0', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'W', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', 'W'], ['E', '0', 'E', '0', 'E'], ['0', 'E', 'W', 'E', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'W', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', 'W'], ['E', '0', 'E', '0', 'E'], ['0', 'E', 'W', 'E', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'E'], ['E', 'W', '0', 'W', 'E'], ['E', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'E'], ['E', 'W', '0', 'W', 'E'], ['E', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'W', '0', 'W', '0'], ['W', '0', 'E', '0', 'W'], ['0', 'E', '0', 'E', '0'], ['W', '0', 'E', '0', 'W'], ['0', 'W', '0', 'W', '0']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'W', '0', 'W', '0'], ['W', '0', 'E', '0', 'W'], ['0', 'E', '0', 'E', '0'], ['W', '0', 'E', '0', 'W'], ['0', 'W', '0', 'W', '0']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', '0', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'W', 'E', 'W', 'E', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', '0', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'W', 'E', 'W', 'E', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'], ['E', 'E', 'E', '0', '0', 'E', 'E', 'E'], ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0']]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'], ['E', 'E', 'E', '0', '0', 'E', 'E', 'E'], ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0']]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'W', 'E', 'E', '0'], ['E', 'E', '0', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', 'E', 'E', 'W', 'E', 'E', 'E'], ['0', 'E', '0', '0', 'E', '0', 'E'], ['E', 'E', '0', 'E', 'E', 'E', '0']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'W', 'E', 'E', '0'], ['E', 'E', '0', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', 'E', 'E', 'W', 'E', 'E', 'E'], ['0', 'E', '0', '0', 'E', '0', 'E'], ['E', 'E', '0', 'E', 'E', 'E', '0']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', '0', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', '0', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', 'E', '0', '0'], ['E', 'W', '0', 'W', 'E'], ['0', 'E', '0', 'E', '0'], ['W', '0', '0', '0', 'W'], ['E', '0', 'E', '0', 'E']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', 'E', '0', '0'], ['E', 'W', '0', 'W', 'E'], ['0', 'E', '0', 'E', '0'], ['W', '0', '0', '0', 'W'], ['E', '0', 'E', '0', 'E']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', '0', 'W', 'E'], ['E', '0', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', '0'], ['E', 'W', 'E', '0', 'E', '0'], ['0', '0', 'E', 'E', 'E', 'W'], ['E', '0', 'E', '0', 'W', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', '0', 'W', 'E'], ['E', '0', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', '0'], ['E', 'W', 'E', '0', 'E', '0'], ['0', '0', 'E', 'E', 'E', 'W'], ['E', '0', 'E', '0', 'W', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E'], ['E', 'W', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E'], ['E', 'W', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'W', '0', 'E'], ['0', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'W', '0', 'E'], ['0', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0'], ['0', 'E', 'E', '0'], ['0', 'E', 'E', '0'], ['0', 'W', 'W', '0'], ['0', 'E', 'E', '0']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0'], ['0', 'E', 'E', '0'], ['0', 'E', 'E', '0'], ['0', 'W', 'W', '0'], ['0', 'E', 'E', '0']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', '0', '0', 'E', 'E', '0', 'W', '0'], ['0', 'E', 'E', '0', 'W', '0', 'E', '0', 'E'], ['E', '0', 'W', 'E', 'E', '0', 'W', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', 'E', 'W', 'E'], ['E', '0', 'E', '0', 'W', '0', 'E', '0', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0', 'E', '0'], ['W', '0', 'E', 'E', '0', '0', 'E', '0', 'W']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', '0', '0', 'E', 'E', '0', 'W', '0'], ['0', 'E', 'E', '0', 'W', '0', 'E', '0', 'E'], ['E', '0', 'W', 'E', 'E', '0', 'W', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', 'E', 'W', 'E'], ['E', '0', 'E', '0', 'W', '0', 'E', '0', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0', 'E', '0'], ['W', '0', 'E', 'E', '0', '0', 'E', '0', 'W']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', '0'], ['0', 'E', 'W', 'E', '0'], ['0', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', '0'], ['0', 'E', 'W', 'E', '0'], ['0', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'W', '0', 'W', '0'], ['0', '0', '0', '0', '0'], ['0', 'W', '0', 'W', '0'], ['0', '0', '0', '0', '0']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'W', '0', 'W', '0'], ['0', '0', '0', '0', '0'], ['0', 'W', '0', 'W', '0'], ['0', '0', '0', '0', '0']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0', 'E'], ['E', 'E', '0', 'E', 'E', 'E', 'E', 'E', '0', 'E', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E', '0', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', '0', 'E', '0', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0']]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0', 'E'], ['E', 'E', '0', 'E', 'E', 'E', 'E', 'E', '0', 'E', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E', '0', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', '0', 'E', '0', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0']]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E']]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E']]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0'], ['E', 'E', 'E', 'E'], ['0', 'W', 'W', '0'], ['E', 'E', 'E', 'E']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0'], ['E', 'E', 'E', 'E'], ['0', 'W', 'W', '0'], ['E', 'E', 'E', 'E']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'W', '0', 'E', '0', 'W', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', '0', '0', 'W', '0', '0', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', '0', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', '0', '0', 'E', '0', '0', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'W', '0', 'E', '0', 'W', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', '0', '0', 'W', '0', '0', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', '0', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', '0', '0', 'E', '0', '0', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', 'W', 'W', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', 'W', 'W', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'E', 'E', '0', 'W'], ['0', 'E', 'W', '0', 'E', '0'], ['W', '0', '0', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', '0'], ['0', 'W', 'E', 'E', '0', 'E']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'E', 'E', '0', 'W'], ['0', 'E', 'W', '0', 'E', '0'], ['W', '0', '0', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', '0'], ['0', 'W', 'E', 'E', '0', 'E']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', '0', 'W', '0', 'E', 'E', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E']]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', '0', 'W', '0', 'E', 'E', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E']]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', 'W', 'E', 'E', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E']]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', 'W', 'E', 'E', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E']]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', 'E', 'E', '0']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', 'E', 'E', '0']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'E'], ['E', '0', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'E'], ['E', '0', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', '0', '0', 'W', 'E'], ['0', 'E', 'E', 'E', '0'], ['W', '0', '0', 'W', 'E'], ['0', 'E', '0', '0', '0'], ['E', 'W', 'E', 'W', 'E']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', '0', '0', 'W', 'E'], ['0', 'E', 'E', 'E', '0'], ['W', '0', '0', 'W', 'E'], ['0', 'E', '0', '0', '0'], ['E', 'W', 'E', 'W', 'E']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0'], ['0', 'W', '0', '0'], ['0', '0', 'W', '0'], ['0', '0', '0', 'E'], ['E', '0', 'E', '0'], ['0', 'E', '0', 'E'], ['E', '0', '0', 'E'], ['0', 'E', '0', '0']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0'], ['0', 'W', '0', '0'], ['0', '0', 'W', '0'], ['0', '0', '0', 'E'], ['E', '0', 'E', '0'], ['0', 'E', '0', 'E'], ['E', '0', '0', 'E'], ['0', 'E', '0', '0']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['E', 'W', 'E', 'W', 'E'], ['E', 'E', '0', 'E', 'E'], ['W', 'E', 'E', 'E', 'W'], ['E', '0', 'E', '0', 'E'], ['E', 'E', 'W', 'E', 'E']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['E', 'W', 'E', 'W', 'E'], ['E', 'E', '0', 'E', 'E'], ['W', 'E', 'E', 'E', 'W'], ['E', '0', 'E', '0', 'E'], ['E', 'E', 'W', 'E', 'E']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', 'E', '0', 'E', 'W', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', '0', 'E', '0', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', '0', 'E', '0', 'E', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E']]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', 'E', '0', 'E', 'W', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', '0', 'E', '0', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', '0', 'E', '0', 'E', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E']]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['0', '0', '0', '0', '0', '0'], ['E', 'E', 'W', 'E', 'E', '0'], ['0', '0', 'E', '0', '0', '0'], ['E', 'E', '0', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', '0', '0', 'E']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['0', '0', '0', '0', '0', '0'], ['E', 'E', 'W', 'E', 'E', '0'], ['0', '0', 'E', '0', '0', '0'], ['E', 'E', '0', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', '0', '0', 'E']]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [['0', '0', '0'], ['W', 'W', 'W'], ['E', 'E', 'E']]) == 0
    assert candidate(grid = [['E', '0', 'W', 'E'], ['E', '0', 'W', 'E'], ['E', 'E', 'E', 'E']]) == 2
    assert candidate(grid = [['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']]) == 3
    assert candidate(grid = [['0', 'E', 'E', '0'], ['E', 'E', '0', 'E'], ['E', '0', 'E', 'E'], ['0', 'E', 'E', '0']]) == 6
    assert candidate(grid = [['W', 'W', 'W'], ['0', '0', '0'], ['E', 'E', 'E']]) == 1
    assert candidate(grid = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', '0', '0', '0', '0']]) == 2
    assert candidate(grid = [['0', 'E', 'W', 'E', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E'], ['E', 'W', 'E', 'W', 'E', 'W', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E'], ['0', 'E', 'W', 'E', 'E', '0', 'E']]) == 7
    assert candidate(grid = [['0', 'E', 'E', 'E', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', 'E', '0', '0', '0']]) == 7
    assert candidate(grid = [['0', 'W', '0', 'W', '0', 'W', '0'], ['W', '0', 'W', '0', 'W', '0', 'W'], ['0', 'W', '0', 'W', '0', 'W', '0'], ['W', '0', 'W', '0', 'W', '0', 'W'], ['0', 'W', '0', 'W', '0', 'W', '0']]) == 0
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 10
    assert candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['0', '0', '0', '0', '0', '0', '0', '0']]) == 1
    assert candidate(grid = [['0', '0', '0', 'W', '0', '0', '0'], ['0', 'E', '0', '0', '0', 'E', '0'], ['W', '0', '0', '0', '0', '0', 'W'], ['0', 'E', '0', '0', '0', 'E', '0'], ['0', '0', '0', 'W', '0', '0', '0']]) == 2
    assert candidate(grid = [['W', 'W', 'W', 'W', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 4
    assert candidate(grid = [['0', 'E', '0', '0', '0'], ['0', '0', '0', 'W', '0'], ['E', 'E', 'E', 'E', '0'], ['0', '0', 'W', 'E', 'E'], ['E', '0', '0', '0', '0']]) == 5
    assert candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', '0'], ['E', 'E', '0', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['0', '0', '0', '0', '0']]) == 5
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '0', '0', '0', '0', '0', '0', 'E'], ['E', '0', 'W', 'W', 'W', 'W', '0', 'E'], ['E', '0', 'W', '0', '0', 'W', '0', 'E'], ['E', '0', 'W', 'W', 'W', 'W', '0', 'E'], ['E', '0', '0', '0', '0', '0', '0', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 4
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0
    assert candidate(grid = [['W', 'W', 'E', 'W', 'W'], ['W', 'W', '0', 'W', 'W'], ['E', '0', 'E', '0', 'E'], ['W', 'W', '0', 'W', 'W'], ['W', 'W', 'E', 'W', 'W']]) == 3
    assert candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0']]) == 4
    assert candidate(grid = [['0', '0', '0', 'E', 'E'], ['0', 'W', 'W', 'W', 'W'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['E', 'W', 'E', '0', '0']]) == 4
    assert candidate(grid = [['0', 'W', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0', '0'], ['E', 'W', 'E', '0', 'E', '0'], ['W', 'E', '0', 'E', 'E', 'W']]) == 6
    assert candidate(grid = [['0', 'W', '0', '0', '0'], ['0', 'E', 'E', '0', 'W'], ['0', 'E', '0', 'E', '0'], ['W', 'E', 'E', 'E', 'W'], ['0', '0', 'E', '0', 'E']]) == 5
    assert candidate(grid = [['E', 'E', '0', 'E', 'E'], ['0', '0', '0', '0', '0'], ['E', 'E', '0', 'E', 'E'], ['0', '0', '0', '0', '0'], ['E', 'E', '0', 'E', 'E']]) == 4
    assert candidate(grid = [['0', 'E', 'E', 'W', '0', 'E', '0'], ['E', '0', '0', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', '0', 'E', 'W'], ['0', '0', 'E', '0', 'E', '0', '0'], ['E', '0', '0', 'E', '0', '0', 'E'], ['0', 'E', '0', '0', 'E', 'E', '0']]) == 6
    assert candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W', '0'], ['E', '0', 'E', '0', 'E', '0', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 9
    assert candidate(grid = [['0', 'E', 'W', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', 'W'], ['E', '0', 'E', '0', 'E'], ['0', 'E', 'W', 'E', '0']]) == 6
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['E', 'W', 'W', 'W', 'E'], ['E', 'W', '0', 'W', 'E'], ['E', 'W', 'W', 'W', 'E'], ['E', 'E', 'E', 'E', 'E']]) == 0
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0
    assert candidate(grid = [['0', 'W', '0', 'W', '0'], ['W', '0', 'E', '0', 'W'], ['0', 'E', '0', 'E', '0'], ['W', '0', 'E', '0', 'W'], ['0', 'W', '0', 'W', '0']]) == 4
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E']]) == 3
    assert candidate(grid = [['0', 'E', 'E', '0', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'W', 'E', 'W', 'E', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0']]) == 8
    assert candidate(grid = [['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'], ['E', 'E', 'E', '0', '0', 'E', 'E', 'E'], ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', '0']]) == 9
    assert candidate(grid = [['0', 'E', '0', 'W', 'E', 'E', '0'], ['E', 'E', '0', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', 'E', 'E', 'W', 'E', 'E', 'E'], ['0', 'E', '0', '0', 'E', '0', 'E'], ['E', 'E', '0', 'E', 'E', 'E', '0']]) == 8
    assert candidate(grid = [['E', 'E', 'E', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', '0', 'E', 'E'], ['0', 'W', 'W', 'W', '0'], ['E', 'E', 'E', 'E', 'E']]) == 4
    assert candidate(grid = [['0', '0', 'E', '0', '0'], ['E', 'W', '0', 'W', 'E'], ['0', 'E', '0', 'E', '0'], ['W', '0', '0', '0', 'W'], ['E', '0', 'E', '0', 'E']]) == 4
    assert candidate(grid = [['0', 'E', '0', '0', 'W', 'E'], ['E', '0', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', '0'], ['E', 'W', 'E', '0', 'E', '0'], ['0', '0', 'E', 'E', 'E', 'W'], ['E', '0', 'E', '0', 'W', '0']]) == 6
    assert candidate(grid = [['E', 'E', 'E', 'E'], ['E', 'W', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]) == 0
    assert candidate(grid = [['E', '0', 'W', '0', 'E'], ['0', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E']]) == 6
    assert candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 7
    assert candidate(grid = [['0', '0', '0', '0'], ['0', 'E', 'E', '0'], ['0', 'E', 'E', '0'], ['0', 'W', 'W', '0'], ['0', 'E', 'E', '0']]) == 2
    assert candidate(grid = [['W', 'W', '0', '0', 'E', 'E', '0', 'W', '0'], ['0', 'E', 'E', '0', 'W', '0', 'E', '0', 'E'], ['E', '0', 'W', 'E', 'E', '0', 'W', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', 'E', 'W', 'E'], ['E', '0', 'E', '0', 'W', '0', 'E', '0', 'E'], ['0', 'E', 'E', '0', 'E', 'E', '0', 'E', '0'], ['W', '0', 'E', 'E', '0', '0', 'E', '0', 'W']]) == 8
    assert candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', '0'], ['0', 'E', 'W', 'E', '0'], ['0', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0']]) == 3
    assert candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]) == 18
    assert candidate(grid = [['0', '0', '0', '0', '0'], ['0', 'W', '0', 'W', '0'], ['0', '0', '0', '0', '0'], ['0', 'W', '0', 'W', '0'], ['0', '0', '0', '0', '0']]) == 0
    assert candidate(grid = [['0', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0', 'E'], ['E', 'E', '0', 'E', 'E', 'E', 'E', 'E', '0', 'E', 'E'], ['E', 'E', 'E', '0', 'E', 'E', 'E', '0', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', '0', 'E', '0', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0']]) == 17
    assert candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E']]) == 10
    assert candidate(grid = [['0', '0', '0', '0'], ['E', 'E', 'E', 'E'], ['0', 'W', 'W', '0'], ['E', 'E', 'E', 'E']]) == 2
    assert candidate(grid = [['0', 'W', '0', 'E', '0', 'W', '0'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', '0', '0', 'W', '0', '0', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', '0', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', '0', '0', 'E', '0', '0', '0']]) == 6
    assert candidate(grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]) == 13
    assert candidate(grid = [['W', 'W', 'W', 'W', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', '0', 'E', '0', 'W'], ['W', 'E', '0', 'E', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 3
    assert candidate(grid = [['E', '0', 'E', 'E', '0', 'W'], ['0', 'E', 'W', '0', 'E', '0'], ['W', '0', '0', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', '0'], ['0', 'W', 'E', 'E', '0', 'E']]) == 7
    assert candidate(grid = [['E', '0', '0', 'W', '0', 'E', 'E', 'E', '0', 'E'], ['E', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', '0', 'E', '0', 'E', '0', 'E'], ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E']]) == 10
    assert candidate(grid = [['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E']]) == 5
    assert candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', 'W', 'E', 'E', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E', '0'], ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['0', 'E', 'E', '0', 'E', '0', 'E', '0', 'E', '0', 'E']]) == 11
    assert candidate(grid = [['0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E'], ['E', '0', 'E', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E']]) == 6
    assert candidate(grid = [['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 8
    assert candidate(grid = [['0', 'E', 'E', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', '0', 'E', '0'], ['E', 'E', 'W', 'E', 'E'], ['0', 'E', 'E', 'E', '0']]) == 5
    assert candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0']]) == 6
    assert candidate(grid = [['0', 'E', '0', 'E', '0', 'E', 'W'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', 'W', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0']]) == 7
    assert candidate(grid = [['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', 'E']]) == 7
    assert candidate(grid = [['0', 'E', '0', 'E', '0'], ['E', 'W', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0'], ['E', '0', 'E', '0', 'E'], ['0', 'E', '0', 'E', '0']]) == 6
    assert candidate(grid = [['E', 'E', 'E', 'E'], ['E', '0', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]) == 7
    assert candidate(grid = [['E', '0', '0', 'W', 'E'], ['0', 'E', 'E', 'E', '0'], ['W', '0', '0', 'W', 'E'], ['0', 'E', '0', '0', '0'], ['E', 'W', 'E', 'W', 'E']]) == 6
    assert candidate(grid = [['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]) == 0
    assert candidate(grid = [['0', '0', '0', '0'], ['0', 'W', '0', '0'], ['0', '0', 'W', '0'], ['0', '0', '0', 'E'], ['E', '0', 'E', '0'], ['0', 'E', '0', 'E'], ['E', '0', '0', 'E'], ['0', 'E', '0', '0']]) == 5
    assert candidate(grid = [['E', 'W', 'E', 'W', 'E'], ['E', 'E', '0', 'E', 'E'], ['W', 'E', 'E', 'E', 'W'], ['E', '0', 'E', '0', 'E'], ['E', 'E', 'W', 'E', 'E']]) == 7
    assert candidate(grid = [['0', '0', '0', '0', 'E', '0', 'E', 'W', 'E', '0'], ['E', '0', 'E', '0', 'E', '0', '0', 'E', '0', 'E'], ['W', 'E', '0', 'E', '0', 'E', '0', '0', 'E', '0'], ['0', 'E', '0', 'E', '0', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', '0', 'E', '0', 'E', 'E', '0', 'E'], ['0', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E']]) == 11
    assert candidate(grid = [['0', '0', '0', '0', '0', '0'], ['E', 'E', 'W', 'E', 'E', '0'], ['0', '0', 'E', '0', '0', '0'], ['E', 'E', '0', 'E', 'E', '0'], ['0', '0', '0', '0', '0', '0'], ['E', 'E', 'E', '0', '0', 'E']]) == 6


