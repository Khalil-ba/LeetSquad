def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1], [1, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1], [1, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0], [1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0], [1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 0, 0, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 0, 0, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [1, 0, 1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [1, 0, 1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 1], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 1], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0], [1, 1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0], [1, 1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1]]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(matrix = [[0, 1], [1, 0]]) == 1
    assert candidate(matrix = [[1, 1, 0], [1, 0, 1]]) == 2
    assert candidate(matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 12
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(matrix = [[1, 0, 1, 0, 1]]) == 3
    assert candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 9
    assert candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0]]) == 6
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1]]) == 4
    assert candidate(matrix = [[1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 12
    assert candidate(matrix = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 4
    assert candidate(matrix = [[1, 0, 0, 0, 0, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 15
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 20
    assert candidate(matrix = [[1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]) == 6
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1]]) == 4
    assert candidate(matrix = [[1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]) == 4
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0]]) == 8
    assert candidate(matrix = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 1, 1]]) == 4
    assert candidate(matrix = [[1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1]]) == 5
    assert candidate(matrix = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [1, 0, 1, 1, 1]]) == 4
    assert candidate(matrix = [[0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 16
    assert candidate(matrix = [[1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1]]) == 12
    assert candidate(matrix = [[1, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]) == 9
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 10
    assert candidate(matrix = [[1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0]]) == 6
    assert candidate(matrix = [[1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1]]) == 6
    assert candidate(matrix = [[0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1]]) == 4
    assert candidate(matrix = [[0, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 0]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 12
    assert candidate(matrix = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1]]) == 5
    assert candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 15
    assert candidate(matrix = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 0, 1], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1]]) == 6
    assert candidate(matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1]]) == 8
    assert candidate(matrix = [[0, 0, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]) == 4
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 5
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1]]) == 10
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 10
    assert candidate(matrix = [[1, 1, 0, 0, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 9
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 30
    assert candidate(matrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) == 1
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]) == 6
    assert candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 3
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 4
    assert candidate(matrix = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]) == 6
    assert candidate(matrix = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]) == 6
    assert candidate(matrix = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]]) == 4
    assert candidate(matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]]) == 12
    assert candidate(matrix = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 12
    assert candidate(matrix = [[1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 0, 1]]) == 6
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]]) == 3
    assert candidate(matrix = [[1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 10
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 9
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 8
    assert candidate(matrix = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0], [1, 1, 1, 1]]) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 20
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 12
    assert candidate(matrix = [[1, 0, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]]) == 10
    assert candidate(matrix = [[0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1]]) == 9
    assert candidate(matrix = [[0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 1]]) == 6
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]]) == 12
    assert candidate(matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1]]) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]) == 7
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1]]) == 9
    assert candidate(matrix = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]]) == 10
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1]]) == 12
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 5
    assert candidate(matrix = [[0, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1]]) == 5


