def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W'], ['W', 'B']],target = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W'], ['W', 'B']],target = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']],target = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']],target = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B'], ['B', 'W', 'B'], ['B', 'W', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B'], ['B', 'W', 'B'], ['B', 'W', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B'], ['B', 'W']],target = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B'], ['B', 'W']],target = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'B', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'B', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'W', 'W'], ['B', 'B', 'W', 'W'], ['W', 'W', 'B', 'B'], ['W', 'W', 'B', 'B']],target = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'W', 'W'], ['B', 'B', 'W', 'W'], ['W', 'W', 'B', 'B'], ['W', 'W', 'B', 'B']],target = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W']],target = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W']],target = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W']],target = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W']],target = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'B']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'B']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'W', 'B'], ['B', 'B', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'W', 'B'], ['B', 'B', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'B'], ['B', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'B'], ['B', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'W', 'B', 'B', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'W', 'B', 'B', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'B', 'W']],target = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'B', 'W']],target = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'B']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'B']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B']],target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B']],target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']],target = 6) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']],target = 6) == 36: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(picture = [['W', 'W', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W']],target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(picture = [['W', 'W', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W']],target = 2) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(picture = [['B', 'W'], ['W', 'B']],target = 1) == 2
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0
    assert candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9
    assert candidate(picture = [['W', 'B', 'W'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 0
    assert candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']],target = 1) == 3
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0
    assert candidate(picture = [['B', 'W', 'B'], ['B', 'W', 'B'], ['B', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0
    assert candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 1
    assert candidate(picture = [['W', 'B'], ['B', 'W']],target = 1) == 2
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9
    assert candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']],target = 3) == 9
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B', 'B']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['B', 'B', 'W', 'W'], ['B', 'B', 'W', 'W'], ['W', 'W', 'B', 'B'], ['W', 'W', 'B', 'B']],target = 2) == 8
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']],target = 4) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 2) == 4
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 5) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W']],target = 2) == 2
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 9
    assert candidate(picture = [['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W']],target = 2) == 8
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 5) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'B']],target = 3) == 9
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'W', 'B'], ['B', 'B', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W']],target = 4) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'B'], ['B', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'W', 'B', 'B', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 3) == 9
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'B', 'W']],target = 2) == 8
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 5) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 3) == 6
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B']],target = 3) == 9
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B']],target = 5) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']],target = 6) == 36
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 4) == 16
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 4) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 3) == 9
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W']],target = 2) == 0


