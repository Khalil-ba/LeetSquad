def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 2, 2],bottoms = [1, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 2, 2],bottoms = [1, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 2, 1, 2],bottoms = [1, 2, 3, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 2, 1, 2],bottoms = [1, 2, 3, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 5, 1, 2, 3],bottoms = [3, 6, 3, 3, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 5, 1, 2, 3],bottoms = [3, 6, 3, 3, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1],bottoms = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1],bottoms = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 1, 2, 4, 2, 2],bottoms = [5, 2, 6, 2, 3, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 1, 2, 4, 2, 2],bottoms = [5, 2, 6, 2, 3, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 1],bottoms = [2, 1, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 1],bottoms = [2, 1, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 2],bottoms = [2, 1, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 2],bottoms = [2, 1, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2],bottoms = [2, 2, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2],bottoms = [2, 2, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 2, 4, 2],bottoms = [3, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 2, 4, 2],bottoms = [3, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 1, 1, 2, 2, 2],bottoms = [2, 1, 2, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 1, 1, 2, 2, 2],bottoms = [2, 1, 2, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 3, 4, 1, 4, 3, 4, 1, 4, 3],bottoms = [3, 1, 1, 3, 1, 4, 1, 3, 1, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 3, 4, 1, 4, 3, 4, 1, 4, 3],bottoms = [3, 1, 1, 3, 1, 4, 1, 3, 1, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 5, 5, 5, 5, 5],bottoms = [5, 5, 1, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 5, 5, 5, 5, 5],bottoms = [5, 5, 1, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 1, 1],bottoms = [2, 2, 1, 1, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 1, 1],bottoms = [2, 2, 1, 1, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 1, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 1, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bottoms = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bottoms = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4],bottoms = [4, 4, 3, 3, 2, 2, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4],bottoms = [4, 4, 3, 3, 2, 2, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9],bottoms = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9],bottoms = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 4, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 4, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 6, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 6, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 1, 1, 2, 1, 2],bottoms = [2, 1, 1, 2, 2, 1, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 1, 1, 2, 1, 2],bottoms = [2, 1, 1, 2, 2, 1, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],bottoms = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],bottoms = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [4, 5, 6, 6, 5, 4],bottoms = [4, 5, 6, 6, 5, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [4, 5, 6, 6, 5, 4],bottoms = [4, 5, 6, 6, 5, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],bottoms = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],bottoms = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 1],bottoms = [1, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 1],bottoms = [1, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 3, 3, 3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 3, 3, 3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 1, 2],bottoms = [2, 3, 4, 1, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 1, 2],bottoms = [2, 3, 4, 1, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2],bottoms = [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2],bottoms = [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bottoms = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bottoms = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 1, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 1, 3, 3, 3, 3, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 1, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 1, 3, 3, 3, 3, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],bottoms = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],bottoms = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],bottoms = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],bottoms = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 6, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 6, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],bottoms = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],bottoms = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],bottoms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],bottoms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 2, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 2, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8],bottoms = [8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8],bottoms = [8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],bottoms = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],bottoms = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 3, 3, 3],bottoms = [3, 3, 3, 2, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 3, 3, 3],bottoms = [3, 3, 3, 2, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4],bottoms = [4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4],bottoms = [4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],bottoms = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],bottoms = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 6, 5, 5, 6, 5, 6, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 6, 5, 5],bottoms = [5, 5, 6, 5, 5, 6, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 6, 5, 5, 6, 5, 6, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 6, 5, 5],bottoms = [5, 5, 6, 5, 5, 6, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tops = [4, 1, 4, 1, 4, 1, 4, 1, 4, 1],bottoms = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [4, 1, 4, 1, 4, 1, 4, 1, 4, 1],bottoms = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 3, 1, 2, 1, 1],bottoms = [2, 1, 2, 1, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 3, 1, 2, 1, 1],bottoms = [2, 1, 2, 1, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],bottoms = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],bottoms = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 2, 2, 2, 1, 1, 1],bottoms = [1, 2, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 2, 2, 2, 1, 1, 1],bottoms = [1, 2, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 4, 5, 6, 1, 2, 3, 4, 5],bottoms = [5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 4, 5, 6, 1, 2, 3, 4, 5],bottoms = [5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],bottoms = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],bottoms = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 6, 1, 6, 1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1, 6, 1, 6, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 6, 1, 6, 1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1, 6, 1, 6, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 2, 5, 3, 3, 3, 3, 3, 3],bottoms = [5, 3, 3, 5, 3, 3, 3, 3, 3, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 2, 5, 3, 3, 3, 3, 3, 3],bottoms = [5, 3, 3, 5, 3, 3, 3, 3, 3, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [5, 5, 5, 5, 5, 1],bottoms = [1, 1, 1, 1, 1, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [5, 5, 5, 5, 5, 1],bottoms = [1, 1, 1, 1, 1, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],bottoms = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],bottoms = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 3, 5, 3, 5, 3, 5, 3, 5, 3],bottoms = [3, 1, 3, 5, 3, 5, 3, 5, 3, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 3, 5, 3, 5, 3, 5, 3, 5, 3],bottoms = [3, 1, 3, 5, 3, 5, 3, 5, 3, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 2, 3, 2, 3],bottoms = [3, 2, 3, 2, 3, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 2, 3, 2, 3],bottoms = [3, 2, 3, 2, 3, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 1, 2, 3],bottoms = [3, 2, 1, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 1, 2, 3],bottoms = [3, 2, 1, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 2, 2, 2],bottoms = [2, 2, 2, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 2, 2, 2],bottoms = [2, 2, 2, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],bottoms = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],bottoms = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],bottoms = [4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],bottoms = [4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tops = [2, 3, 4, 2, 3, 4],bottoms = [4, 3, 2, 4, 3, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [2, 3, 4, 2, 3, 4],bottoms = [4, 3, 2, 4, 3, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 6, 1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1, 6, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 6, 1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1, 6, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(tops = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],bottoms = [6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tops = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],bottoms = [6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tops = [2, 3, 2, 2],bottoms = [1, 2, 2, 2]) == 1
    assert candidate(tops = [2, 3, 2, 1, 2],bottoms = [1, 2, 3, 2, 2]) == 2
    assert candidate(tops = [6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6]) == 0
    assert candidate(tops = [3, 5, 1, 2, 3],bottoms = [3, 6, 3, 3, 4]) == -1
    assert candidate(tops = [1, 1, 1, 1],bottoms = [1, 1, 1, 1]) == 0
    assert candidate(tops = [1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [2, 1, 2, 4, 2, 2],bottoms = [5, 2, 6, 2, 3, 2]) == 2
    assert candidate(tops = [1, 2, 1, 1],bottoms = [2, 1, 2, 2]) == 1
    assert candidate(tops = [3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 2]) == 0
    assert candidate(tops = [3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3]) == 0
    assert candidate(tops = [1, 2, 1, 2],bottoms = [2, 1, 2, 1]) == 2
    assert candidate(tops = [1, 1, 2, 2],bottoms = [2, 2, 1, 1]) == 2
    assert candidate(tops = [2, 3, 2, 4, 2],bottoms = [3, 2, 2, 2, 2]) == 1
    assert candidate(tops = [1, 2, 1, 1, 1, 2, 2, 2],bottoms = [2, 1, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(tops = [1, 3, 4, 1, 4, 3, 4, 1, 4, 3],bottoms = [3, 1, 1, 3, 1, 4, 1, 3, 1, 4]) == -1
    assert candidate(tops = [1, 5, 5, 5, 5, 5],bottoms = [5, 5, 1, 5, 5, 5]) == 1
    assert candidate(tops = [1, 1, 2, 2, 1, 1],bottoms = [2, 2, 1, 1, 2, 2]) == 2
    assert candidate(tops = [2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2]) == -1
    assert candidate(tops = [6, 1, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 1
    assert candidate(tops = [1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1]) == 3
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bottoms = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4],bottoms = [4, 4, 3, 3, 2, 2, 1, 1]) == -1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9],bottoms = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 44
    assert candidate(tops = [3, 3, 3, 4, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(tops = [5, 5, 6, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [1, 2, 2, 1, 1, 2, 1, 2],bottoms = [2, 1, 1, 2, 2, 1, 2, 1]) == 4
    assert candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],bottoms = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1
    assert candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]) == 0
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(tops = [4, 5, 6, 6, 5, 4],bottoms = [4, 5, 6, 6, 5, 4]) == -1
    assert candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],bottoms = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [5, 5, 5, 5, 5, 1],bottoms = [1, 5, 5, 5, 5, 5]) == 1
    assert candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5]) == 0
    assert candidate(tops = [3, 3, 3, 3, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 3, 3, 3, 3]) == 4
    assert candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3]) == -1
    assert candidate(tops = [1, 2, 3, 4, 1, 2],bottoms = [2, 3, 4, 1, 2, 3]) == -1
    assert candidate(tops = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2],bottoms = [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 7
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bottoms = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [3, 1, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 1, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(tops = [1, 1, 1, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 1, 1, 1, 1, 1]) == 3
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],bottoms = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(tops = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(tops = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],bottoms = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1
    assert candidate(tops = [3, 6, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 6]) == 1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],bottoms = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]) == 0
    assert candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1
    assert candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1]) == 0
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],bottoms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1
    assert candidate(tops = [5, 5, 2, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 2]) == 1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 7, 8],bottoms = [8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],bottoms = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == -1
    assert candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(tops = [1, 2, 2, 3, 3, 3],bottoms = [3, 3, 3, 2, 2, 1]) == 3
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4],bottoms = [4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],bottoms = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 10
    assert candidate(tops = [5, 6, 5, 5, 6, 5, 6, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 6, 5, 5],bottoms = [5, 5, 6, 5, 5, 6, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 5, 5, 5, 6]) == 6
    assert candidate(tops = [4, 1, 4, 1, 4, 1, 4, 1, 4, 1],bottoms = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4]) == 5
    assert candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [1, 3, 1, 2, 1, 1],bottoms = [2, 1, 2, 1, 2, 2]) == 2
    assert candidate(tops = [5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],bottoms = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(tops = [1, 1, 1, 2, 2, 2, 1, 1, 1],bottoms = [1, 2, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(tops = [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]) == 0
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],bottoms = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(tops = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == -1
    assert candidate(tops = [2, 3, 4, 5, 6, 1, 2, 3, 4, 5],bottoms = [5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == -1
    assert candidate(tops = [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],bottoms = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6]) == 10
    assert candidate(tops = [1, 6, 1, 6, 1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1, 6, 1, 6, 1]) == 5
    assert candidate(tops = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(tops = [3, 3, 2, 5, 3, 3, 3, 3, 3, 3],bottoms = [5, 3, 3, 5, 3, 3, 3, 3, 3, 3]) == -1
    assert candidate(tops = [2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1]) == 1
    assert candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
    assert candidate(tops = [5, 5, 5, 5, 5, 1],bottoms = [1, 1, 1, 1, 1, 5]) == 1
    assert candidate(tops = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bottoms = [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1
    assert candidate(tops = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],bottoms = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
    assert candidate(tops = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5],bottoms = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == -1
    assert candidate(tops = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],bottoms = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4]) == -1
    assert candidate(tops = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(tops = [1, 3, 5, 3, 5, 3, 5, 3, 5, 3],bottoms = [3, 1, 3, 5, 3, 5, 3, 5, 3, 5]) == 5
    assert candidate(tops = [2, 3, 2, 3, 2, 3],bottoms = [3, 2, 3, 2, 3, 2]) == 3
    assert candidate(tops = [1, 2, 3, 1, 2, 3],bottoms = [3, 2, 1, 3, 2, 1]) == -1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(tops = [1, 1, 1, 1, 1, 1, 1, 1],bottoms = [1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
    assert candidate(tops = [1, 1, 1, 2, 2, 2],bottoms = [2, 2, 2, 1, 1, 1]) == 3
    assert candidate(tops = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],bottoms = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 0
    assert candidate(tops = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],bottoms = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(tops = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],bottoms = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == -1
    assert candidate(tops = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],bottoms = [4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == -1
    assert candidate(tops = [1, 2, 2, 3, 4, 5, 6],bottoms = [6, 5, 4, 3, 2, 1, 2]) == -1
    assert candidate(tops = [3, 3, 3, 3, 3, 3],bottoms = [3, 3, 3, 3, 3, 3]) == 0
    assert candidate(tops = [2, 3, 4, 2, 3, 4],bottoms = [4, 3, 2, 4, 3, 2]) == -1
    assert candidate(tops = [1, 6, 1, 6, 1, 6, 1, 6],bottoms = [6, 1, 6, 1, 6, 1, 6, 1]) == 4
    assert candidate(tops = [1, 2, 2, 3, 3, 4, 4, 5, 5],bottoms = [5, 5, 4, 4, 3, 3, 2, 2, 1]) == -1
    assert candidate(tops = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],bottoms = [6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6]) == -1


