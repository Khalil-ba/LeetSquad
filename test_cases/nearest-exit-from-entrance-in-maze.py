def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(maze = [['.', '+']],entrance = [0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '+']],entrance = [0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['+)', '+)', '+'], ['.', '.', '.'], ['+)', '+)', '+']],entrance = [1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['+)', '+)', '+'], ['.', '.', '.'], ['+)', '+)', '+']],entrance = [1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['+)', '+)', '.'], ['.', '.', '.', '+'], ['+)', '+)', '+)', '.']],entrance = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['+)', '+)', '.'], ['.', '.', '.', '+'], ['+)', '+)', '+)', '.']],entrance = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['+', '.', '+'], ['.', '.', '.'], ['+', '.', '+']],entrance = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['+', '.', '+'], ['.', '.', '.'], ['+', '.', '+']],entrance = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['.', '.', '+', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '.', '+', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['.', '.', '.', '.'], ['.', '+', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '.', '.', '.'], ['.', '+', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [1, 1]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(maze = [['.', '+']],entrance = [0, 0]) == -1
    assert candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [0, 1]) == 1
    assert candidate(maze = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 0]) == 1
    assert candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [2, 2]) == 1
    assert candidate(maze = [['+)', '+)', '+'], ['.', '.', '.'], ['+)', '+)', '+']],entrance = [1, 0]) == 2
    assert candidate(maze = [['+)', '+)', '.'], ['.', '.', '.', '+'], ['+)', '+)', '+)', '.']],entrance = [1, 2]) == 1
    assert candidate(maze = [['+', '.', '+'], ['.', '.', '.'], ['+', '.', '+']],entrance = [1, 1]) == 1
    assert candidate(maze = [['.', '.', '+', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 3]) == 1
    assert candidate(maze = [['.', '.', '.', '.'], ['.', '+', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [1, 1]) == 1
    assert candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [1, 1]) == 1


