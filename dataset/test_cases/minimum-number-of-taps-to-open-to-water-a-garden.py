def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,ranges = [3, 4, 1, 1, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,ranges = [3, 4, 1, 1, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,ranges = [0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,ranges = [0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,ranges = [1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,ranges = [1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,ranges = [1, 2, 3, 4, 5, 6, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,ranges = [1, 2, 3, 4, 5, 6, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [4, 0, 0, 0, 0, 0, 1, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [4, 0, 0, 0, 0, 0, 1, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [1, 2, 1, 0, 2, 1, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [1, 2, 1, 0, 2, 1, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,ranges = [1, 2, 1, 0, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,ranges = [1, 2, 1, 0, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,ranges = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,ranges = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,ranges = [1, 2, 2, 1, 0, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,ranges = [1, 2, 2, 1, 0, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [0, 2, 1, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [0, 2, 1, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [1, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [1, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 1, 0, 1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 1, 0, 1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 3, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 3, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [3, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [3, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [3, 2, 2, 3, 2, 2, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [3, 2, 2, 3, 2, 2, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 3, 0, 2, 1, 0, 1, 0, 1, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 3, 0, 2, 1, 0, 1, 0, 1, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,ranges = [4, 2, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,ranges = [4, 2, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [0, 1, 0, 0, 1, 0, 1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [0, 1, 0, 0, 1, 0, 1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [1, 2, 2, 3, 1, 2, 3, 0, 1, 2, 1, 0, 1, 2, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [1, 2, 2, 3, 1, 2, 3, 0, 1, 2, 1, 0, 1, 2, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,ranges = [0, 0, 2, 0, 0, 0, 2, 0, 0, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,ranges = [0, 0, 2, 0, 0, 0, 2, 0, 0, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,ranges = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,ranges = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,ranges = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,ranges = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 2, 0, 2, 2, 0, 1, 0, 1, 2, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 2, 0, 2, 2, 0, 1, 0, 1, 2, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,ranges = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,ranges = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [3, 1, 4, 2, 1, 0, 1, 0, 0, 2, 3, 0, 1, 0, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [3, 1, 4, 2, 1, 0, 1, 0, 0, 2, 3, 0, 1, 0, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,ranges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,ranges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [3, 1, 0, 0, 0, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [3, 1, 0, 0, 0, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [3, 2, 1, 0, 0, 0, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [3, 2, 1, 0, 0, 0, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [3, 0, 1, 2, 0, 1, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [3, 0, 1, 2, 0, 1, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [0, 1, 0, 0, 0, 2, 1, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [0, 1, 0, 0, 0, 2, 1, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [3, 0, 1, 1, 0, 2, 1, 0, 0, 2, 3, 1, 0, 1, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [3, 0, 1, 1, 0, 2, 1, 0, 0, 2, 3, 1, 0, 1, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [2, 3, 0, 1, 0, 3, 0, 1, 0, 0, 1, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [2, 3, 0, 1, 0, 3, 0, 1, 0, 0, 1, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [3, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [3, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [0, 0, 3, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [0, 0, 3, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,ranges = [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,ranges = [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,ranges = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,ranges = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [3, 0, 2, 1, 1, 0, 2, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [3, 0, 2, 1, 1, 0, 2, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [0, 0, 2, 0, 0, 0, 2, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [0, 0, 2, 0, 0, 0, 2, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,ranges = [5, 0, 3, 0, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,ranges = [5, 0, 3, 0, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,ranges = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,ranges = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 3, 1, 4, 0, 1, 2, 0, 3, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 3, 1, 4, 0, 1, 2, 0, 3, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,ranges = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,ranges = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,ranges = [1, 0, 1, 1, 0, 0, 0, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,ranges = [1, 0, 1, 1, 0, 0, 0, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [3, 0, 0, 0, 3, 2, 0, 1, 0, 0, 2, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [3, 0, 0, 0, 3, 2, 0, 1, 0, 0, 2, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,ranges = [4, 0, 0, 0, 4, 0, 0, 0, 4, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,ranges = [4, 0, 0, 0, 4, 0, 0, 0, 4, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 3, 1, 4, 0, 0, 2, 0, 1, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 3, 1, 4, 0, 0, 2, 0, 1, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [3, 0, 1, 1, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 0, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [3, 0, 1, 1, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 0, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,ranges = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,ranges = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,ranges = [0, 2, 1, 3, 1, 2, 0, 1, 0, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,ranges = [0, 2, 1, 3, 1, 2, 0, 1, 0, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,ranges = [3, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,ranges = [3, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,ranges = [3, 2, 0, 0, 1, 0, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,ranges = [3, 2, 0, 0, 1, 0, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,ranges = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,ranges = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,ranges = [1, 2, 2, 3, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,ranges = [1, 2, 2, 3, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,ranges = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,ranges = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [4, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [4, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,ranges = [2, 3, 1, 0, 0, 1, 2, 1, 0, 2, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,ranges = [2, 3, 1, 0, 0, 1, 2, 1, 0, 2, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,ranges = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,ranges = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 5,ranges = [3, 4, 1, 1, 0, 0]) == 1
    assert candidate(n = 8,ranges = [4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2
    assert candidate(n = 3,ranges = [0, 0, 0, 0]) == -1
    assert candidate(n = 2,ranges = [1, 0, 1]) == 2
    assert candidate(n = 6,ranges = [1, 2, 3, 4, 5, 6, 7]) == 1
    assert candidate(n = 8,ranges = [4, 0, 0, 0, 0, 0, 1, 0, 1]) == -1
    assert candidate(n = 7,ranges = [1, 2, 1, 0, 2, 1, 0, 1]) == 3
    assert candidate(n = 10,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(n = 6,ranges = [1, 2, 1, 0, 2, 1, 0]) == 2
    assert candidate(n = 1,ranges = [1, 1]) == 1
    assert candidate(n = 6,ranges = [1, 2, 2, 1, 0, 1, 0]) == 2
    assert candidate(n = 20,ranges = [0, 2, 1, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0]) == 8
    assert candidate(n = 7,ranges = [1, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(n = 12,ranges = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2]) == 6
    assert candidate(n = 20,ranges = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(n = 20,ranges = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 20,ranges = [4, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 1, 0, 1, 0]) == -1
    assert candidate(n = 10,ranges = [2, 3, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3
    assert candidate(n = 20,ranges = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == -1
    assert candidate(n = 15,ranges = [3, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0]) == -1
    assert candidate(n = 14,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 7,ranges = [3, 2, 2, 3, 2, 2, 1, 1]) == 2
    assert candidate(n = 10,ranges = [2, 3, 0, 2, 1, 0, 1, 0, 1, 0, 1]) == 5
    assert candidate(n = 14,ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == 1
    assert candidate(n = 25,ranges = [4, 2, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 7,ranges = [0, 1, 0, 0, 1, 0, 1, 0]) == -1
    assert candidate(n = 12,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(n = 12,ranges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 2
    assert candidate(n = 15,ranges = [1, 2, 2, 3, 1, 2, 3, 0, 1, 2, 1, 0, 1, 2, 1, 0]) == 4
    assert candidate(n = 9,ranges = [0, 0, 2, 0, 0, 0, 2, 0, 0, 2]) == 3
    assert candidate(n = 11,ranges = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5
    assert candidate(n = 12,ranges = [4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]) == -1
    assert candidate(n = 12,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
    assert candidate(n = 9,ranges = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
    assert candidate(n = 10,ranges = [2, 2, 0, 2, 2, 0, 1, 0, 1, 2, 0]) == 4
    assert candidate(n = 12,ranges = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 3
    assert candidate(n = 10,ranges = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(n = 9,ranges = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1]) == -1
    assert candidate(n = 25,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 8,ranges = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(n = 15,ranges = [3, 1, 4, 2, 1, 0, 1, 0, 0, 2, 3, 0, 1, 0, 1, 0]) == 4
    assert candidate(n = 8,ranges = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == 1
    assert candidate(n = 13,ranges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(n = 12,ranges = [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4]) == -1
    assert candidate(n = 20,ranges = [3, 1, 0, 0, 0, 0, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]) == -1
    assert candidate(n = 7,ranges = [3, 2, 1, 0, 0, 0, 2, 1]) == -1
    assert candidate(n = 7,ranges = [3, 0, 1, 2, 0, 1, 0, 1]) == 4
    assert candidate(n = 12,ranges = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]) == 1
    assert candidate(n = 20,ranges = [10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 8,ranges = [0, 1, 0, 0, 0, 2, 1, 0, 1]) == -1
    assert candidate(n = 15,ranges = [3, 0, 1, 1, 0, 2, 1, 0, 0, 2, 3, 1, 0, 1, 0, 1]) == 5
    assert candidate(n = 9,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
    assert candidate(n = 15,ranges = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(n = 12,ranges = [2, 3, 0, 1, 0, 3, 0, 1, 0, 0, 1, 0, 1]) == -1
    assert candidate(n = 10,ranges = [3, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1]) == 3
    assert candidate(n = 12,ranges = [0, 0, 3, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 25,ranges = [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 20,ranges = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]) == 2
    assert candidate(n = 11,ranges = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 6
    assert candidate(n = 8,ranges = [3, 0, 2, 1, 1, 0, 2, 1, 1]) == 2
    assert candidate(n = 10,ranges = [2, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1]) == 3
    assert candidate(n = 18,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
    assert candidate(n = 10,ranges = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1]) == 2
    assert candidate(n = 8,ranges = [0, 0, 2, 0, 0, 0, 2, 1, 1]) == 2
    assert candidate(n = 18,ranges = [5, 0, 3, 0, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 4]) == 6
    assert candidate(n = 14,ranges = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]) == -1
    assert candidate(n = 10,ranges = [2, 3, 1, 4, 0, 1, 2, 0, 3, 1, 2]) == 2
    assert candidate(n = 11,ranges = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
    assert candidate(n = 8,ranges = [1, 0, 1, 1, 0, 0, 0, 1, 1]) == -1
    assert candidate(n = 15,ranges = [3, 0, 0, 0, 3, 2, 0, 1, 0, 0, 2, 0, 0, 0, 1]) == -1
    assert candidate(n = 10,ranges = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 3
    assert candidate(n = 13,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 9,ranges = [4, 0, 0, 0, 4, 0, 0, 0, 4, 0]) == 2
    assert candidate(n = 10,ranges = [2, 3, 1, 4, 0, 0, 2, 0, 1, 0, 1]) == 3
    assert candidate(n = 15,ranges = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(n = 18,ranges = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == -1
    assert candidate(n = 15,ranges = [3, 0, 1, 1, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 0, 3]) == -1
    assert candidate(n = 14,ranges = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1]) == 1
    assert candidate(n = 9,ranges = [0, 2, 1, 3, 1, 2, 0, 1, 0, 2]) == 3
    assert candidate(n = 14,ranges = [3, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]) == -1
    assert candidate(n = 20,ranges = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]) == -1
    assert candidate(n = 7,ranges = [3, 2, 0, 0, 1, 0, 1, 1]) == 3
    assert candidate(n = 12,ranges = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1
    assert candidate(n = 50,ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == -1
    assert candidate(n = 12,ranges = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]) == -1
    assert candidate(n = 15,ranges = [1, 2, 2, 3, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(n = 20,ranges = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(n = 25,ranges = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(n = 20,ranges = [4, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(n = 10,ranges = [2, 3, 1, 0, 0, 1, 2, 1, 0, 2, 0]) == 3
    assert candidate(n = 20,ranges = [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]) == -1
    assert candidate(n = 20,ranges = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 2


