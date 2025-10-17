def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mat = [[0, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0], [0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0], [0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1], [1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1], [1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 1]]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 1]]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 1]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 1]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0]]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0]]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1]]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1]]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 141: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1]]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1]]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1]]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1]]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1]]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1]]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 233: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 0]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 0]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0]]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0]]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1]]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1]]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]]) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]]) == 196: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1]]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1]]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 0]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 0]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1]]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1]]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 0, 0]]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 0, 0]]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1]]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1]]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 117: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1]]) == 56: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mat = [[0, 0], [0, 0]]) == 0
    assert candidate(mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 13
    assert candidate(mat = [[1, 0], [0, 1]]) == 2
    assert candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 60
    assert candidate(mat = [[0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
    assert candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 36
    assert candidate(mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]) == 24
    assert candidate(mat = [[1, 1], [1, 1]]) == 9
    assert candidate(mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(mat = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1]]) == 28
    assert candidate(mat = [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 1]]) == 89
    assert candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) == 36
    assert candidate(mat = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]) == 15
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]) == 32
    assert candidate(mat = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]) == 29
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 126
    assert candidate(mat = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]) == 69
    assert candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]]) == 18
    assert candidate(mat = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0]]) == 43
    assert candidate(mat = [[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 1, 1]]) == 40
    assert candidate(mat = [[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0]]) == 59
    assert candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 31
    assert candidate(mat = [[1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1]]) == 85
    assert candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 50
    assert candidate(mat = [[1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0]]) == 18
    assert candidate(mat = [[1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]]) == 50
    assert candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 420
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 28
    assert candidate(mat = [[1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1]]) == 25
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1]]) == 105
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 13
    assert candidate(mat = [[1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1]]) == 105
    assert candidate(mat = [[1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1]]) == 30
    assert candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == 36
    assert candidate(mat = [[1, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]) == 37
    assert candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0]]) == 60
    assert candidate(mat = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1]]) == 48
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 128
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 270
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 141
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1]]) == 93
    assert candidate(mat = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1]]) == 71
    assert candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]]) == 21
    assert candidate(mat = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1]]) == 114
    assert candidate(mat = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1]]) == 41
    assert candidate(mat = [[1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]) == 29
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 233
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 44
    assert candidate(mat = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]) == 9
    assert candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 0]]) == 34
    assert candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1]]) == 36
    assert candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0]]) == 18
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 57
    assert candidate(mat = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0]]) == 76
    assert candidate(mat = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1]]) == 51
    assert candidate(mat = [[1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]]) == 18
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]]) == 196
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 210
    assert candidate(mat = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]) == 23
    assert candidate(mat = [[1, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 62
    assert candidate(mat = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]) == 54
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 540
    assert candidate(mat = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]) == 25
    assert candidate(mat = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]]) == 74
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 112
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 315
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 10
    assert candidate(mat = [[1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0]]) == 52
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 56
    assert candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 71
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1]]) == 87
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 89
    assert candidate(mat = [[1, 0, 1, 0, 1], [1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 0]]) == 45
    assert candidate(mat = [[1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0]]) == 30
    assert candidate(mat = [[1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1]]) == 51
    assert candidate(mat = [[0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]]) == 14
    assert candidate(mat = [[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]]) == 45
    assert candidate(mat = [[1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 0, 0]]) == 67
    assert candidate(mat = [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 68
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 110
    assert candidate(mat = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]) == 45
    assert candidate(mat = [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1]]) == 91
    assert candidate(mat = [[1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1]]) == 28
    assert candidate(mat = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]) == 56
    assert candidate(mat = [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1]]) == 50
    assert candidate(mat = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 58
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 117
    assert candidate(mat = [[1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1]]) == 56


