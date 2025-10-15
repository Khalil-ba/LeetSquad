def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['B', 'W', 'B'], ['W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['B', 'W', 'B'], ['W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'B', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'B', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'B', 'W']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'B', 'W']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'B']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'B']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'W', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'W', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W', 'B']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W', 'B']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['B', 'B', 'B'], ['W', 'W', 'W'], ['B', 'B', 'B'], ['W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['B', 'B', 'B'], ['W', 'W', 'W'], ['B', 'B', 'B'], ['W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W', 'W']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W', 'W']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W']]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']]) == 3
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'B']]) == 0
    assert candidate(picture = [['W']]) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == 2
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']]) == 3
    assert candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == 1
    assert candidate(picture = [['B']]) == 1
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 2
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B']]) == 6
    assert candidate(picture = [['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B']]) == 4
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W']]) == 3
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['B', 'W', 'B'], ['W', 'W', 'W']]) == 1
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'B', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 4
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 2
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 1
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 3
    assert candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 1
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'B', 'W']]) == 7
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 4
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 4
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 3
    assert candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B']]) == 2
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W']]) == 5
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B']]) == 2
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 2
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W']]) == 4
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'B']]) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 4
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 5
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 3
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'B']]) == 4
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W']]) == 2
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'W', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'W', 'B']]) == 1
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['W', 'W', 'W'], ['B', 'B', 'B'], ['W', 'W', 'W'], ['B', 'B', 'B'], ['W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 5
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']]) == 1
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'B', 'W', 'W', 'W']]) == 5
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 7
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'B']]) == 6
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 3
    assert candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'W']]) == 1
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]) == 5
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']]) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'B'], ['W', 'W', 'W', 'W', 'W']]) == 3


