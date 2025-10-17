def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 1, 0, -1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 1, 0, -1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, -1, 0, 1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, -1, 0, 1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 1, 0, -1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 1, 0, -1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 1, 0, -1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 1, 0, -1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 1, 1, -1, -1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 1, 1, -1, -1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, -1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, -1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 1, 0, -1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 1, 0, -1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, -1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, -1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 1, -1, -1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 1, -1, -1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, -1, 0, 1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, -1, 0, 1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forts = [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forts = [0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forts = [0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(forts = [1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(forts = [-1, 0, 0, 0, 0, 1]) == 4
    assert candidate(forts = [0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, -1]) == 2
    assert candidate(forts = [1, -1]) == 0
    assert candidate(forts = [0, 0, 0, 0, 0]) == 0
    assert candidate(forts = [-1]) == 0
    assert candidate(forts = [0]) == 0
    assert candidate(forts = [1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(forts = [0, 0, 0, 0]) == 0
    assert candidate(forts = [0, 1, 0, -1, 0]) == 1
    assert candidate(forts = [1, -1, 1, -1, 1, -1]) == 0
    assert candidate(forts = [-1, 1, -1, 1, -1, 1]) == 0
    assert candidate(forts = [0, 0, 1, -1]) == 0
    assert candidate(forts = [0, 1, 0, -1, 0, 1, 0]) == 1
    assert candidate(forts = [1, 1, 1, -1, -1, -1, 1]) == 0
    assert candidate(forts = [-1, 0, -1, 0, 1, 0, 1]) == 1
    assert candidate(forts = [1, 0, 0, 0, 0, -1]) == 4
    assert candidate(forts = [1, 0, 1, 0, -1, 0, -1]) == 1
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, -1]) == 6
    assert candidate(forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    assert candidate(forts = [1, 0, 0, 0, 0, 0, -1]) == 5
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(forts = [1]) == 0
    assert candidate(forts = [1, 1, -1, -1, 1, 1]) == 0
    assert candidate(forts = [-1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(forts = [1, -1, 1, -1, 1]) == 0
    assert candidate(forts = [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1]) == 1
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, -1]) == 3
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 13
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
    assert candidate(forts = [-1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1]) == 3
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1]) == 5
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 2
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 43
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 29
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1]) == 5
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
    assert candidate(forts = [-1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    assert candidate(forts = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 50
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 71
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1]) == 7
    assert candidate(forts = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
    assert candidate(forts = [-1, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 1, 0]) == 4
    assert candidate(forts = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) == 7
    assert candidate(forts = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]) == 8
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 1, -1]) == 4
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 43
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]) == 6
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1]) == 2
    assert candidate(forts = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 8
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 77
    assert candidate(forts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [-1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1]) == 5
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1]) == 3
    assert candidate(forts = [1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, -1]) == 2
    assert candidate(forts = [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1]) == 10
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 10
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 56
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 12
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1]) == 2
    assert candidate(forts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(forts = [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]) == 5
    assert candidate(forts = [0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1]) == 5


