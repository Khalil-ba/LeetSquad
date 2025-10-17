def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 4, 3, 2],pattern = [1, -1, 1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 4, 3, 2],pattern = [1, -1, 1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5],pattern = [1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5],pattern = [1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 4, 1, 3, 5, 5, 3],pattern = [1, 0, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 4, 1, 3, 5, 5, 3],pattern = [1, 0, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5],pattern = [0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5],pattern = [0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4],pattern = [1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4],pattern = [1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4],pattern = [1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4],pattern = [1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6],pattern = [1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6],pattern = [1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],pattern = [-1, -1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],pattern = [-1, -1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 4, 5],pattern = [1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 4, 5],pattern = [1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5],pattern = [1, 0, 0, 1, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5],pattern = [1, 0, 0, 1, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5],pattern = [1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5],pattern = [1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10],pattern = [0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10],pattern = [0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5],pattern = [-1, -1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5],pattern = [-1, -1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],pattern = [1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],pattern = [1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, 1, 1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, 1, 1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 10, 8, 10, 5, 6, 7, 8, 9],pattern = [1, 0, -1, 1, 1, -1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 10, 8, 10, 5, 6, 7, 8, 9],pattern = [1, 0, -1, 1, 1, -1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 9, 10, 11, 10, 9, 8, 9, 10],pattern = [-1, -1, 1, 1, -1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 9, 10, 11, 10, 9, 8, 9, 10],pattern = [-1, -1, 1, 1, -1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 5, 5, 6],pattern = [1, 0, 1, 0, 1, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 5, 5, 6],pattern = [1, 0, 1, 0, 1, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6],pattern = [1, 0, 0, 1, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6],pattern = [1, 0, 0, 1, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6],pattern = [1, -1, 1, -1, 1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6],pattern = [1, -1, 1, -1, 1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],pattern = [0, 1, 0, 1, 0, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, 0, 1, -1, 0, -1, 0, -1, 0, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],pattern = [0, 1, 0, 1, 0, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, 0, 1, -1, 0, -1, 0, -1, 0, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3],pattern = [1, 0, 0, -1, -1, 0, 0, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3],pattern = [1, 0, 0, -1, -1, 0, 0, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8],pattern = [1, 1, -1, 1, 1, -1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8],pattern = [1, 1, -1, 1, 1, -1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, 0, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, 0, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],pattern = [1, 1, -1, -1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],pattern = [1, 1, -1, -1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3],pattern = [1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3],pattern = [1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1],pattern = [0, 1, 0, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1],pattern = [0, 1, 0, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6],pattern = [1, -1, 1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6],pattern = [1, -1, 1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1],pattern = [1, 0, 1, 0, -1, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1],pattern = [1, 0, 1, 0, -1, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],pattern = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],pattern = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],pattern = [0, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],pattern = [0, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50],pattern = [1, -1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50],pattern = [1, -1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],pattern = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],pattern = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 0, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 0, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4],pattern = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4],pattern = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],pattern = [0, 0, 0, 1, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],pattern = [0, 0, 0, 1, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2],pattern = [1, 1, 1, -1, -1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2],pattern = [1, 1, 1, -1, -1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 11, 12, 13, 13, 12, 11, 12, 13, 13, 12, 10],pattern = [0, 1, 1, 1, 0, -1, -1, 1, 1, 0, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 11, 12, 13, 13, 12, 11, 12, 13, 13, 12, 10],pattern = [0, 1, 1, 1, 0, -1, -1, 1, 1, 0, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],pattern = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],pattern = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],pattern = [1, 0, -1, 1, 0, -1, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],pattern = [1, 0, -1, 1, 0, -1, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5],pattern = [1, 1, 1, -1, -1, -1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5],pattern = [1, 1, 1, -1, -1, -1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6, 7, 8],pattern = [1, -1, 1, -1, 1, 0, 1, 0, 0, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6, 7, 8],pattern = [1, -1, 1, -1, 1, 0, 1, 0, 0, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],pattern = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],pattern = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12],pattern = [1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12],pattern = [1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],pattern = [1, 0, 1, 0, 1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],pattern = [1, 0, 1, 0, 1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 8, 9, 10, 9, 8, 7, 8, 9, 10],pattern = [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 8, 9, 10, 9, 8, 7, 8, 9, 10],pattern = [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8],pattern = [1, 0, 1, 0, 1, 0, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8],pattern = [1, 0, 1, 0, 1, 0, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 11, 10, 12, 13, 14, 13, 15, 16],pattern = [1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 11, 10, 12, 13, 14, 13, 15, 16],pattern = [1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 11, 10, 12, 13, 14, 13, 15, 16, 15, 17, 18, 17, 19, 20, 19, 21, 22],pattern = [1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 11, 10, 12, 13, 14, 13, 15, 16, 15, 17, 18, 17, 19, 20, 19, 21, 22],pattern = [1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2],pattern = [-1, 1, -1, 1, -1, 1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2],pattern = [-1, 1, -1, 1, -1, 1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10],pattern = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10],pattern = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, 0, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, 0, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],pattern = [1, 1, 1, -1, -1, -1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],pattern = [1, 1, 1, -1, -1, -1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1],pattern = [1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1],pattern = [1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 4, 6, 7, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 4, 6, 7, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6],pattern = [1, -1, 1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6],pattern = [1, -1, 1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, -1, -1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, -1, -1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 7, 6, 7, 8, 9, 10],pattern = [1, 1, -1, -1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 7, 6, 7, 8, 9, 10],pattern = [1, 1, -1, -1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3],pattern = [0, 1, 0, -1, 0, 1, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3],pattern = [0, 1, 0, -1, 0, 1, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 2, 3, 1, 4, 3, 2],pattern = [1, -1, 1, -1]) == 2
    assert candidate(nums = [1, 2, 2, 3, 4, 5],pattern = [1, 0, 1]) == 1
    assert candidate(nums = [1, 4, 4, 1, 3, 5, 5, 3],pattern = [1, 0, -1]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5],pattern = [0, 0, 0]) == 3
    assert candidate(nums = [1, 2, 2, 3, 4],pattern = [1, 0, 1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4],pattern = [1, 0, 1, 0]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6],pattern = [1, 1]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0, 0]) == 2
    assert candidate(nums = [5, 4, 3, 2, 1],pattern = [-1, -1, -1]) == 2
    assert candidate(nums = [1, 3, 2, 3, 4, 5],pattern = [1, -1, 1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0]) == 3
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5],pattern = [1, 0, 0, 1, 0, 0]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5],pattern = [1, -1, 1]) == 2
    assert candidate(nums = [10, 10, 10, 10],pattern = [0, 0]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5],pattern = [-1, -1, -1]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],pattern = [1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, 1, 1, -1, -1]) == 0
    assert candidate(nums = [7, 10, 10, 8, 10, 5, 6, 7, 8, 9],pattern = [1, 0, -1, 1, 1, -1, 1, 1]) == 0
    assert candidate(nums = [10, 9, 8, 9, 10, 11, 10, 9, 8, 9, 10],pattern = [-1, -1, 1, 1, -1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 5, 5, 6],pattern = [1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6],pattern = [1, 0, 0, 1, 0, 0, 1]) == 0
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6],pattern = [1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1],pattern = [0, 1, 0, 1, 0, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, 0, 1, -1, 0, -1, 0, -1, 0, -1, 0]) == 0
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1]) == 5
    assert candidate(nums = [1, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3],pattern = [1, 0, 0, -1, -1, 0, 0, 1, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8],pattern = [1, 1, -1, 1, 1, -1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0]) == 3
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, 0, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],pattern = [1, 1, -1, -1, 1, 1]) == 0
    assert candidate(nums = [100, 200, 150, 250, 200, 300, 250, 350, 300, 400],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3],pattern = [1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0]) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1],pattern = [0, 1, 0, -1, 0]) == 0
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6],pattern = [1, -1, 1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1],pattern = [1, 0, 1, 0, -1, 0, -1]) == 0
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],pattern = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(nums = [1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],pattern = [0, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50],pattern = [1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],pattern = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 4
    assert candidate(nums = [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 0, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4],pattern = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],pattern = [0, 0, 0, 1, 0, 0, 0]) == 1
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2],pattern = [1, 1, 1, -1, -1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [10, 10, 11, 12, 13, 13, 12, 11, 12, 13, 13, 12, 10],pattern = [0, 1, 1, 1, 0, -1, -1, 1, 1, 0, -1, -1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],pattern = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],pattern = [1, 0, -1, 1, 0, -1, 1, 0]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5],pattern = [1, 1, 1, -1, -1, -1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, -1]) == 1
    assert candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6, 7, 8],pattern = [1, -1, 1, -1, 1, 0, 1, 0, 0, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],pattern = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 0
    assert candidate(nums = [1, 3, 5, 4, 6, 5, 7, 8, 7, 9, 10, 9, 11, 12],pattern = [1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],pattern = [1, 0, 1, 0, 1, 0, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [9, 8, 7, 8, 9, 10, 9, 8, 7, 8, 9, 10],pattern = [-1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 4
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0]) == 2
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8],pattern = [1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(nums = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [3, 1, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 11, 10, 12, 13, 14, 13, 15, 16],pattern = [1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 11, 10, 12, 13, 14, 13, 15, 16, 15, 17, 18, 17, 19, 20, 19, 21, 22],pattern = [1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]) == 0
    assert candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2],pattern = [-1, 1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10],pattern = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1]) == 3
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1]) == 5
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, 0, 1, 1, 1, 1]) == 1
    assert candidate(nums = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],pattern = [1, 1, 1, -1, -1, -1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1],pattern = [1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 3, 5, 4, 6, 7, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6],pattern = [1, -1, 1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, -1, -1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 6, 7, 8, 7, 6, 7, 8, 9, 10],pattern = [1, 1, -1, -1, 1, 1, 1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 3
    assert candidate(nums = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3],pattern = [0, 1, 0, -1, 0, 1, 0, -1]) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1]) == 3


