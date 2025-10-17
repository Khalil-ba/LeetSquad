def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(operations = ['X++', '++X', '--X', 'X--']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '++X', '--X', 'X--']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', 'X--', 'X--']) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', 'X--', 'X--']) == -4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', '++X']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', '++X']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X++', 'X++']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X++', 'X++']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X']) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X']) == -4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', '--X']) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', '--X']) == -5: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', 'X++', '++X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', 'X++', '++X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', 'X++']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', 'X++']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', 'X++', '++X', '--X']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', 'X++', '++X', '--X']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X--', '--X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X--', '--X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X--', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X--', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', 'X++', 'X++', 'X--', 'X--', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', 'X++', 'X++', 'X--', 'X--', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', '++X', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--']) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', '++X', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--']) == -6: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X']) == -16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X']) == -16: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X--', '--X', 'X++', '++X', '--X', 'X--', '--X', '++X', 'X++']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X--', '--X', 'X++', '++X', '--X', 'X--', '--X', '++X', 'X++']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', 'X--', 'X++', '++X', '++X', 'X--', '--X', '++X', '--X']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', 'X--', 'X++', '++X', '++X', 'X--', '--X', '++X', '--X']) == -2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X--', '--X', 'X++', 'X--', '++X', 'X--', '--X', 'X++', '++X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X--', '--X', 'X++', 'X--', '++X', 'X--', '--X', 'X++', '++X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', '--X', 'X++']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', '--X', 'X++']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X']) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X']) == -5: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '--X', '++X', 'X--', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '--X', '++X', 'X--', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X++', '++X', '--X', 'X++', '--X', 'X--', 'X++', '--X', '++X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X++', '++X', '--X', 'X++', '--X', 'X--', 'X++', '--X', '++X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', '--X', '--X', '--X', '++X', 'X++', '--X']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', '--X', '--X', '--X', '++X', 'X++', '--X']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', 'X++', 'X--', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', 'X++', 'X--', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X--', '--X', 'X--', '--X', 'X--', '++X', 'X++', '++X', 'X++', '++X', 'X++', '++X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X--', '--X', 'X--', '--X', 'X--', '++X', 'X++', '++X', 'X++', '++X', 'X++', '++X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X--', 'X--']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X--', 'X--']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X']) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X']) == -5: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', '++X', 'X--', '++X', '--X', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', '++X', 'X--', '++X', '--X', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '++X', '--X', 'X--', 'X--', '--X', '++X', 'X--', '--X']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '++X', '--X', 'X--', 'X--', '--X', '++X', 'X--', '--X']) == -2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++']) == -2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 57: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '--X', '++X', 'X--', '++X', '--X', 'X++', '++X', '--X', 'X--']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '--X', '++X', 'X--', '++X', '--X', 'X++', '++X', '--X', 'X--']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 37: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X--', 'X--', '++X', '++X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X--', 'X--', '++X', '++X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X--', '++X', '--X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X--', '++X', '--X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '--X', '++X', '--X', 'X++', '--X', 'X--']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '--X', '++X', '--X', 'X++', '--X', 'X--']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X--', 'X--', '--X', '--X', 'X++', 'X++', '++X']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X--', 'X--', '--X', '--X', 'X++', 'X++', '++X']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', '--X', 'X++', '++X']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', '--X', 'X++', '++X']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '++X', 'X++', '++X', '--X', '--X', 'X--', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '++X', 'X++', '++X', '--X', '--X', 'X--', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X--', '--X', 'X++', '++X', 'X--', 'X--', '--X', '++X', 'X--', 'X--', 'X++', '++X']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X--', '--X', 'X++', '++X', 'X--', 'X--', '--X', '++X', 'X--', 'X--', 'X++', '++X']) == -2: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X--', 'X++', '--X', 'X++', 'X--', '++X', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X--', 'X++', '--X', 'X++', 'X--', '++X', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(operations = ['++X', '++X', '++X', '--X', 'X--', '--X', 'X--', '--X', '++X', '--X']) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(operations = ['++X', '++X', '++X', '--X', 'X--', '--X', 'X--', '--X', '++X', '--X']) == -2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(operations = ['X++', '++X', '--X', 'X--']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++']) == 5
    assert candidate(operations = ['--X', '--X', 'X--', 'X--']) == -4
    assert candidate(operations = ['++X', '++X', '++X', '++X']) == 4
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++']) == 4
    assert candidate(operations = ['--X', 'X++', 'X++']) == 1
    assert candidate(operations = ['--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X']) == -5
    assert candidate(operations = ['--X', '--X', 'X++', '++X']) == 0
    assert candidate(operations = ['++X', '++X', 'X++']) == 3
    assert candidate(operations = ['--X', '--X', 'X++', '++X', '--X']) == -1
    assert candidate(operations = ['++X', 'X--', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X--', '++X', '--X']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12
    assert candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++']) == 1
    assert candidate(operations = ['--X', '--X', 'X++', 'X++', 'X--', 'X--', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '++X', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--']) == -6
    assert candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
    assert candidate(operations = ['X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X']) == -16
    assert candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--']) == 0
    assert candidate(operations = ['X--', '--X', 'X++', '++X', '--X', 'X--', '--X', '++X', 'X++']) == -1
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 1
    assert candidate(operations = ['--X', '--X', 'X--', 'X++', '++X', '++X', 'X--', '--X', '++X', '--X']) == -2
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', 'X--', '++X', 'X--', '--X', 'X++', '++X']) == 0
    assert candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 2
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', '--X', 'X++']) == 1
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X']) == -5
    assert candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X']) == 2
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
    assert candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['X++', '--X', '++X', 'X--', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2
    assert candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
    assert candidate(operations = ['--X', 'X++', '++X', '--X', 'X++', '--X', 'X--', 'X++', '--X', '++X']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '--X', '--X', '--X', '++X', 'X++', '--X']) == 1
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1
    assert candidate(operations = ['--X', '--X', 'X++', 'X--', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 0
    assert candidate(operations = ['++X', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2
    assert candidate(operations = ['--X', 'X--', '--X', 'X--', '--X', 'X--', '++X', 'X++', '++X', 'X++', '++X', 'X++', '++X', 'X++']) == 2
    assert candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0
    assert candidate(operations = ['--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X--', 'X--']) == 0
    assert candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X']) == -5
    assert candidate(operations = ['X++', 'X++', '--X', '--X', '++X', 'X--', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['X++', 'X++', '++X', '--X', 'X--', 'X--', '--X', '++X', 'X--', '--X']) == -2
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 12
    assert candidate(operations = ['--X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++']) == -2
    assert candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 4
    assert candidate(operations = ['--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1
    assert candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 8
    assert candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 57
    assert candidate(operations = ['X++', '--X', '++X', 'X--', '++X', '--X', 'X++', '++X', '--X', 'X--']) == 0
    assert candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 37
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++']) == 2
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 0
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
    assert candidate(operations = ['--X', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X--', 'X--', '++X', '++X']) == 0
    assert candidate(operations = ['X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X']) == 0
    assert candidate(operations = ['X++', 'X--', '++X', '--X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X']) == 0
    assert candidate(operations = ['X++', '--X', '++X', '--X', 'X++', '--X', 'X--']) == -1
    assert candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 2
    assert candidate(operations = ['X--', 'X--', '--X', '--X', 'X++', 'X++', '++X']) == -1
    assert candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X']) == 1
    assert candidate(operations = ['++X', '++X', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 2
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++']) == 3
    assert candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', '--X', 'X++', '++X']) == 2
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X']) == 2
    assert candidate(operations = ['X++', '++X', 'X++', '++X', '--X', '--X', 'X--', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', '--X']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0
    assert candidate(operations = ['X--', '--X', 'X++', '++X', 'X--', 'X--', '--X', '++X', 'X--', 'X--', 'X++', '++X']) == -2
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X--', 'X++', '--X', 'X++', 'X--', '++X', '--X']) == 0
    assert candidate(operations = ['++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--']) == 0
    assert candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0
    assert candidate(operations = ['--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '--X', 'X--', '--X', 'X--', '--X', '++X', '--X']) == -2


