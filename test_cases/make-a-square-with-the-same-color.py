def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['B', 'B', 'W'], ['B', 'B', 'W'], ['B', 'B', 'W']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['B', 'B', 'W'], ['B', 'B', 'W'], ['B', 'B', 'W']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'B']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'B']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['B', 'B', 'B'], ['B', 'W', 'B'], ['B', 'B', 'B']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['B', 'B', 'B'], ['B', 'W', 'B'], ['B', 'B', 'B']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'B', 'W'], ['B', 'W', 'B'], ['W', 'B', 'W']]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'B', 'W'], ['B', 'W', 'B'], ['W', 'B', 'W']]) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'W']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'W']]) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['W', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'W']]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['W', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'W']]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == False
    assert candidate(grid = [['B', 'B', 'W'], ['B', 'B', 'W'], ['B', 'B', 'W']]) == True
    assert candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'B']]) == True
    assert candidate(grid = [['B', 'B', 'B'], ['B', 'W', 'B'], ['B', 'B', 'B']]) == True
    assert candidate(grid = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']]) == True
    assert candidate(grid = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']]) == True
    assert candidate(grid = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == True
    assert candidate(grid = [['W', 'B', 'W'], ['B', 'W', 'B'], ['W', 'B', 'W']]) == False
    assert candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'W']]) == True
    assert candidate(grid = [['W', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'W']]) == True


