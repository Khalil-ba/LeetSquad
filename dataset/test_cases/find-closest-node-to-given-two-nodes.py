def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(edges = [5, -1, 3, 4, 5, 6, -1, -1, 4, 3],node1 = 0,node2 = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, -1, 3, 4, 5, 6, -1, -1, 4, 3],node1 = 0,node2 = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 3, 0, 5, 3, -1],node1 = 4,node2 = 0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 3, 0, 5, 3, -1],node1 = 4,node2 = 0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, -1],node1 = 0,node2 = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, -1],node1 = 0,node2 = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 5, 1, 2],node1 = 0,node2 = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 5, 1, 2],node1 = 0,node2 = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 8, -1, 9, 8, 4, 4, 1, 1],node1 = 5,node2 = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 8, -1, 9, 8, 4, 4, 1, 1],node1 = 5,node2 = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, -1],node1 = 1,node2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, -1],node1 = 1,node2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, -1],node1 = 0,node2 = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, -1],node1 = 0,node2 = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 2, 4, 3],node1 = 0,node2 = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 2, 4, 3],node1 = 0,node2 = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 3, -1],node1 = 0,node2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 3, -1],node1 = 0,node2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, -1],node1 = 0,node2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, -1],node1 = 0,node2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],node1 = 0,node2 = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],node1 = 0,node2 = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 1, 3, 4, 5, -1, 2, 2, 3, 0],node1 = 2,node2 = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 1, 3, 4, 5, -1, 2, 2, 3, 0],node1 = 2,node2 = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 2, 4, 3, -1, 5, 5, -1, -1, 6, 6, -1, -1],node1 = 2,node2 = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 2, 4, 3, -1, 5, 5, -1, -1, 6, 6, -1, -1],node1 = 2,node2 = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 3, 0, 5, 3, 9, 8, 5, 4, 6],node1 = 0,node2 = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 3, 0, 5, 3, 9, 8, 5, 4, 6],node1 = 0,node2 = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 8, 5, 9, 8, 4, 4, 1, 1],node1 = 5,node2 = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 8, 5, 9, 8, 4, 4, 1, 1],node1 = 5,node2 = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 5, 5, 5, 3, 2, 0],node1 = 1,node2 = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 5, 5, 5, 3, 2, 0],node1 = 1,node2 = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, -1],node1 = 0,node2 = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, -1],node1 = 0,node2 = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, -1, -1, -1],node1 = 2,node2 = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, -1, -1, -1],node1 = 2,node2 = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 5, 3, 5, 0, 2, 5, 3, 5],node1 = 1,node2 = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 5, 3, 5, 0, 2, 5, 3, 5],node1 = 1,node2 = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 3, 5, 6, 4, -1, -1],node1 = 1,node2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 3, 5, 6, 4, -1, -1],node1 = 1,node2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 1, 2, -1, -1],node1 = 0,node2 = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 1, 2, -1, -1],node1 = 0,node2 = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 0, 0, 3, -1, 4, 5, 5, -1],node1 = 0,node2 = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 0, 0, 3, -1, 4, 5, 5, -1],node1 = 0,node2 = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, -1, -1, -1, -1, -1, -1, -1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],node1 = 0,node2 = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, -1, -1, -1, -1, -1, -1, -1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],node1 = 0,node2 = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 3, 1, 5, 2, 3],node1 = 1,node2 = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 3, 1, 5, 2, 3],node1 = 1,node2 = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 2, 5, 1, 4, -1, 0, 3],node1 = 6,node2 = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 2, 5, 1, 4, -1, 0, 3],node1 = 6,node2 = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 3, -1, 4, 5, 3],node1 = 0,node2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 3, -1, 4, 5, 3],node1 = 0,node2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 1, 4, -1, 5, -1],node1 = 0,node2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 1, 4, -1, 5, -1],node1 = 0,node2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 5, 5, 5, 5, -1, -1, -1, -1, -1],node1 = 0,node2 = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 5, 5, 5, 5, -1, -1, -1, -1, -1],node1 = 0,node2 = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],node1 = 0,node2 = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],node1 = 0,node2 = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 0, 0, 2, 0, 5, 6, -1, 9, 8, 7],node1 = 6,node2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 0, 0, 2, 0, 5, 6, -1, 9, 8, 7],node1 = 6,node2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 1, 0, 2, -1, -1, -1],node1 = 2,node2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 1, 0, 2, -1, -1, -1],node1 = 2,node2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 3, 4, 2, -1, -1, 1],node1 = 0,node2 = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 3, 4, 2, -1, -1, 1],node1 = 0,node2 = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, -1],node1 = 0,node2 = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, -1],node1 = 0,node2 = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],node1 = 0,node2 = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],node1 = 0,node2 = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 2, -1, 1, 2],node1 = 0,node2 = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 2, -1, 1, 2],node1 = 0,node2 = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 0, 0, 2, 5, 4, 4],node1 = 3,node2 = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 0, 0, 2, 5, 4, 4],node1 = 3,node2 = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 1, 1, 4, 1],node1 = 1,node2 = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 1, 1, 4, 1],node1 = 1,node2 = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 3, 0, 5, 3, -1],node1 = 0,node2 = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 3, 0, 5, 3, -1],node1 = 0,node2 = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 3, 4, 3, -1, -1, -1, -1, -1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 40) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 3, 4, 3, -1, -1, -1, -1, -1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 40) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 3, 1, 4, 3, 5, 2, -1],node1 = 1,node2 = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 3, 1, 4, 3, 5, 2, -1],node1 = 1,node2 = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, -1, 0],node1 = 5,node2 = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, -1, 0],node1 = 5,node2 = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 8, -1, 9, 8, 4, 4, 1, 11, 4, 4, 4, 8, 11, 2, 10, 4, 10, 1],node1 = 0,node2 = 13) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 8, -1, 9, 8, 4, 4, 1, 11, 4, 4, 4, 8, 11, 2, 10, 4, 10, 1],node1 = 0,node2 = 13) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 5, 3, 5, 3, 4, -1, 0, 1],node1 = 5,node2 = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 5, 3, 5, 3, 4, -1, 0, 1],node1 = 5,node2 = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [6, 3, 4, 5, 5, 6, 7, 1, 0, -1],node1 = 0,node2 = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [6, 3, 4, 5, 5, 6, 7, 1, 0, -1],node1 = 0,node2 = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, -1, 3, -1, -1, -1, -1, 7, 4, 5, 6, 1],node1 = 0,node2 = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, -1, 3, -1, -1, -1, -1, 7, 4, 5, 6, 1],node1 = 0,node2 = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 1, 3, 4, 2],node1 = 2,node2 = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 1, 3, 4, 2],node1 = 2,node2 = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 1, 5, 4, 3, 6, 5, 7, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 1, 5, 4, 3, 6, 5, 7, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 0, 0, 2, 1, 4],node1 = 3,node2 = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 0, 0, 2, 1, 4],node1 = 3,node2 = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0, -1],node1 = 0,node2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0, -1],node1 = 0,node2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1],node1 = 18,node2 = 19) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1],node1 = 18,node2 = 19) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 8, 5, 9, 8, 4, 4, 1, 4],node1 = 0,node2 = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 8, 5, 9, 8, 4, 4, 1, 4],node1 = 0,node2 = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0],node1 = 0,node2 = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0],node1 = 0,node2 = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 1, 2, -1, 0],node1 = 2,node2 = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 1, 2, -1, 0],node1 = 2,node2 = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 5, -1, 5],node1 = 3,node2 = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 5, -1, 5],node1 = 3,node2 = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 0, -1, -1, 0],node1 = 1,node2 = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 0, -1, -1, 0],node1 = 1,node2 = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10],node1 = 0,node2 = 19) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10],node1 = 0,node2 = 19) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 5, 2, 1, 3, 4, 6, 7, -1],node1 = 8,node2 = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 5, 2, 1, 3, 4, 6, 7, -1],node1 = 8,node2 = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, -1, 3, -1, -1, -1, -1, 5, 8, 9, 7, -1, 1, 10, 3, 7, -1, 14, 1, 13, 11, 13, 10],node1 = 1,node2 = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, -1, 3, -1, -1, -1, -1, 5, 8, 9, 7, -1, 1, 10, 3, 7, -1, 14, 1, 13, 11, 13, 10],node1 = 1,node2 = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, -1],node1 = 19,node2 = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, -1],node1 = 19,node2 = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 4, 4, 5, 1, 6, 5, 5, 6, 8, 8, 1, 7, 9, 8, 8, 8, 8, 8, 8],node1 = 0,node2 = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 4, 4, 5, 1, 6, 5, 5, 6, 8, 8, 1, 7, 9, 8, 8, 8, 8, 8, 8],node1 = 0,node2 = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 2, -1, 3, 3, 4, 5, 5, -1],node1 = 0,node2 = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 2, -1, 3, 3, 4, 5, 5, -1],node1 = 0,node2 = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0],node1 = 1,node2 = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0],node1 = 1,node2 = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],node1 = 0,node2 = 19) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],node1 = 0,node2 = 19) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 5, 1, 3, 2, 4, 2, 2, -1],node1 = 1,node2 = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 5, 1, 3, 2, 4, 2, 2, -1],node1 = 1,node2 = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],node1 = 0,node2 = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],node1 = 0,node2 = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1],node1 = 11,node2 = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1],node1 = 11,node2 = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 4, 4],node1 = 0,node2 = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 4, 4],node1 = 0,node2 = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, -1, 3, 5, -1, 2],node1 = 0,node2 = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, -1, 3, 5, -1, 2],node1 = 0,node2 = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 5, 1, 2],node1 = 0,node2 = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 5, 1, 2],node1 = 0,node2 = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 0, 4, 1, 0, -1, -1, 0, 3],node1 = 6,node2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 0, 4, 1, 0, -1, -1, 0, 3],node1 = 6,node2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 0, 3, 5, 2, 3, -1],node1 = 2,node2 = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 0, 3, 5, 2, 3, -1],node1 = 2,node2 = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 0,node2 = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 0,node2 = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 1, 4, -1, -1, -1, 7, -1, -1, 5, 6],node1 = 0,node2 = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 1, 4, -1, -1, -1, 7, -1, -1, 5, 6],node1 = 0,node2 = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 18) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 18) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1],node1 = 0,node2 = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1],node1 = 0,node2 = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 3, 4, 5, 3, 2, -1],node1 = 1,node2 = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 3, 4, 5, 3, 2, -1],node1 = 1,node2 = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 1, 2, 3, -1, -1],node1 = 5,node2 = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 1, 2, 3, -1, -1],node1 = 5,node2 = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 0, 4, 1],node1 = 0,node2 = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 0, 4, 1],node1 = 0,node2 = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, -1, 3, 1],node1 = 0,node2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, -1, 3, 1],node1 = 0,node2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [10, 15, 11, 14, 13, 12, 5, 15, 9, 12, 15, 9, 10, 11, 13, -1, 12, 14, 15, 8, 5],node1 = 0,node2 = 14) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [10, 15, 11, 14, 13, 12, 5, 15, 9, 12, 15, 9, 10, 11, 13, -1, 12, 14, 15, 8, 5],node1 = 0,node2 = 14) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 0, 2, 3, 0, 2, 4, 0, 3, 2, 3, 2, 2, 3, 0, 2, 1, 0, 1],node1 = 0,node2 = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 0, 2, 3, 0, 2, 4, 0, 3, 2, 3, 2, 2, 3, 0, 2, 1, 0, 1],node1 = 0,node2 = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [6, 3, 0, 5, 8, 5, 8, 3, -1, 6],node1 = 5,node2 = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [6, 3, 0, 5, 8, 5, 8, 3, -1, 6],node1 = 5,node2 = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 0, 5, 5, 2, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 18) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 0, 5, 5, 2, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 18) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 0, 3, 2, 1, 4, 5, -1, -1, -1, 8, 9, 7, 10, 11, 12, 13, -1],node1 = 1,node2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 0, 3, 2, 1, 4, 5, -1, -1, -1, 8, 9, 7, 10, 11, 12, 13, -1],node1 = 1,node2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],node1 = 0,node2 = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],node1 = 0,node2 = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1],node1 = 0,node2 = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1],node1 = 0,node2 = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 3, 4, 5, -1, 2, 6, 7, -1, -1],node1 = 0,node2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 3, 4, 5, -1, 2, 6, 7, -1, -1],node1 = 0,node2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 3, 3, 2],node1 = 0,node2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 3, 3, 2],node1 = 0,node2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 4, 0, 2, 3, 0, 2, 4, 0, 3, 2, 3, 2, 2, 3, -1, 2],node1 = 0,node2 = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 4, 0, 2, 3, 0, 2, 4, 0, 3, 2, 3, 2, 2, 3, -1, 2],node1 = 0,node2 = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, 3, 1, 4, 2, 6, 3, 2],node1 = 0,node2 = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, 3, 1, 4, 2, 6, 3, 2],node1 = 0,node2 = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1, -1, -1, 13, -1, 14, -1, 15],node1 = 0,node2 = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1, -1, -1, 13, -1, 14, -1, 15],node1 = 0,node2 = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [2, 2, 3, 4, 5, -1, -1, 5, 5, 5],node1 = 0,node2 = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [2, 2, 3, 4, 5, -1, -1, 5, 5, 5],node1 = 0,node2 = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [1, 2, 0, 1, 3, -1, -1, -1],node1 = 0,node2 = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [1, 2, 0, 1, 3, -1, -1, -1],node1 = 0,node2 = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [3, 3, 0, 5, -1, 2, 0, -1, -1, 3, 1],node1 = 3,node2 = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [3, 3, 0, 5, -1, 2, 0, -1, -1, 3, 1],node1 = 3,node2 = 10) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(edges = [5, -1, 3, 4, 5, 6, -1, -1, 4, 3],node1 = 0,node2 = 0) == 0
    assert candidate(edges = [4, 3, 0, 5, 3, -1],node1 = 4,node2 = 0) == 4
    assert candidate(edges = [1, 2, 0, -1],node1 = 0,node2 = 2) == 0
    assert candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 1) == 1
    assert candidate(edges = [4, 4, 4, 5, 1, 2],node1 = 0,node2 = 1) == 4
    assert candidate(edges = [4, 4, 8, -1, 9, 8, 4, 4, 1, 1],node1 = 5,node2 = 6) == 1
    assert candidate(edges = [1, 2, 0, -1],node1 = 1,node2 = 2) == 2
    assert candidate(edges = [1, 2, 3, 4, -1],node1 = 0,node2 = 4) == 4
    assert candidate(edges = [3, 3, 2, 4, 3],node1 = 0,node2 = 4) == 3
    assert candidate(edges = [2, 2, 3, -1],node1 = 0,node2 = 1) == 2
    assert candidate(edges = [1, 2, -1],node1 = 0,node2 = 2) == 2
    assert candidate(edges = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],node1 = 0,node2 = 19) == 3
    assert candidate(edges = [3, 1, 3, 4, 5, -1, 2, 2, 3, 0],node1 = 2,node2 = 8) == 3
    assert candidate(edges = [3, 3, 2, 4, 3, -1, 5, 5, -1, -1, 6, 6, -1, -1],node1 = 2,node2 = 10) == -1
    assert candidate(edges = [4, 3, 0, 5, 3, 9, 8, 5, 4, 6],node1 = 0,node2 = 8) == 4
    assert candidate(edges = [4, 4, 8, 5, 9, 8, 4, 4, 1, 1],node1 = 5,node2 = 6) == 1
    assert candidate(edges = [3, 0, 5, 5, 5, 3, 2, 0],node1 = 1,node2 = 7) == 0
    assert candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, -1],node1 = 0,node2 = 8) == -1
    assert candidate(edges = [1, 2, 0, -1, -1, -1],node1 = 2,node2 = 3) == -1
    assert candidate(edges = [3, 0, 5, 3, 5, 0, 2, 5, 3, 5],node1 = 1,node2 = 7) == 0
    assert candidate(edges = [1, 2, 0, 3, 5, 6, 4, -1, -1],node1 = 1,node2 = 7) == -1
    assert candidate(edges = [2, 1, 2, -1, -1],node1 = 0,node2 = 1) == -1
    assert candidate(edges = [2, 0, 0, 3, -1, 4, 5, 5, -1],node1 = 0,node2 = 6) == -1
    assert candidate(edges = [1, 0, -1, -1, -1, -1, -1, -1, -1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],node1 = 0,node2 = 10) == -1
    assert candidate(edges = [5, 3, 1, 5, 2, 3],node1 = 1,node2 = 0) == 3
    assert candidate(edges = [3, 2, 5, 1, 4, -1, 0, 3],node1 = 6,node2 = 4) == -1
    assert candidate(edges = [2, 2, 3, -1, 4, 5, 3],node1 = 0,node2 = 5) == -1
    assert candidate(edges = [2, 3, 1, 4, -1, 5, -1],node1 = 0,node2 = 5) == -1
    assert candidate(edges = [5, 5, 5, 5, 5, -1, -1, -1, -1, -1],node1 = 0,node2 = 5) == 5
    assert candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],node1 = 0,node2 = 19) == 1
    assert candidate(edges = [2, 0, 0, 2, 0, 5, 6, -1, 9, 8, 7],node1 = 6,node2 = 5) == -1
    assert candidate(edges = [3, 1, 0, 2, -1, -1, -1],node1 = 2,node2 = 5) == -1
    assert candidate(edges = [2, 2, 3, 4, 2, -1, -1, 1],node1 = 0,node2 = 6) == -1
    assert candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, -1],node1 = 0,node2 = 10) == -1
    assert candidate(edges = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],node1 = 0,node2 = 9) == 0
    assert candidate(edges = [3, 0, 2, -1, 1, 2],node1 = 0,node2 = 3) == 3
    assert candidate(edges = [2, 0, 0, 2, 5, 4, 4],node1 = 3,node2 = 4) == -1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 5) == 0
    assert candidate(edges = [3, 1, 1, 4, 1],node1 = 1,node2 = 2) == 1
    assert candidate(edges = [4, 3, 0, 5, 3, -1],node1 = 0,node2 = 4) == 4
    assert candidate(edges = [3, 3, 3, 4, 3, -1, -1, -1, -1, -1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 40) == -1
    assert candidate(edges = [5, 3, 1, 4, 3, 5, 2, -1],node1 = 1,node2 = 6) == 1
    assert candidate(edges = [9, 8, 7, 6, 5, 4, 3, 2, 1, -1, 0],node1 = 5,node2 = 0) == -1
    assert candidate(edges = [4, 4, 8, -1, 9, 8, 4, 4, 1, 11, 4, 4, 4, 8, 11, 2, 10, 4, 10, 1],node1 = 0,node2 = 13) == 4
    assert candidate(edges = [3, 0, 5, 3, 5, 3, 4, -1, 0, 1],node1 = 5,node2 = 4) == 5
    assert candidate(edges = [6, 3, 4, 5, 5, 6, 7, 1, 0, -1],node1 = 0,node2 = 5) == 6
    assert candidate(edges = [2, -1, 3, -1, -1, -1, -1, 7, 4, 5, 6, 1],node1 = 0,node2 = 9) == -1
    assert candidate(edges = [1, 2, 0, 1, 3, 4, 2],node1 = 2,node2 = 5) == 1
    assert candidate(edges = [2, 3, 1, 5, 4, 3, 6, 5, 7, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 7) == 3
    assert candidate(edges = [2, 0, 0, 2, 1, 4],node1 = 3,node2 = 5) == 0
    assert candidate(edges = [1, 2, 3, 4, 0, -1],node1 = 0,node2 = 5) == -1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1],node1 = 18,node2 = 19) == -1
    assert candidate(edges = [4, 4, 8, 5, 9, 8, 4, 4, 1, 4],node1 = 0,node2 = 7) == 4
    assert candidate(edges = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0],node1 = 0,node2 = 5) == 0
    assert candidate(edges = [3, 1, 2, -1, 0],node1 = 2,node2 = 4) == -1
    assert candidate(edges = [1, 2, 0, 5, -1, 5],node1 = 3,node2 = 4) == -1
    assert candidate(edges = [3, 3, 0, -1, -1, 0],node1 = 1,node2 = 5) == 3
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10],node1 = 0,node2 = 19) == -1
    assert candidate(edges = [1, 2, 0, 5, 2, 1, 3, 4, 6, 7, -1],node1 = 8,node2 = 9) == 1
    assert candidate(edges = [2, -1, 3, -1, -1, -1, -1, 5, 8, 9, 7, -1, 1, 10, 3, 7, -1, 14, 1, 13, 11, 13, 10],node1 = 1,node2 = 10) == -1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, -1],node1 = 19,node2 = 20) == -1
    assert candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 0) == 4
    assert candidate(edges = [3, 4, 4, 5, 1, 6, 5, 5, 6, 8, 8, 1, 7, 9, 8, 8, 8, 8, 8, 8],node1 = 0,node2 = 10) == 5
    assert candidate(edges = [1, 2, 2, -1, 3, 3, 4, 5, 5, -1],node1 = 0,node2 = 8) == -1
    assert candidate(edges = [1, 2, 3, 4, 0],node1 = 1,node2 = 4) == 1
    assert candidate(edges = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],node1 = 0,node2 = 19) == -1
    assert candidate(edges = [3, 0, 5, 1, 3, 2, 4, 2, 2, -1],node1 = 1,node2 = 8) == -1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],node1 = 0,node2 = 19) == 0
    assert candidate(edges = [7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1],node1 = 11,node2 = 2) == -1
    assert candidate(edges = [4, 4, 4, 4, 4],node1 = 0,node2 = 2) == 4
    assert candidate(edges = [2, -1, 3, 5, -1, 2],node1 = 0,node2 = 5) == 2
    assert candidate(edges = [4, 4, 4, 5, 1, 2],node1 = 0,node2 = 3) == 4
    assert candidate(edges = [2, 2, 0, 4, 1, 0, -1, -1, 0, 3],node1 = 6,node2 = 7) == -1
    assert candidate(edges = [5, 4, 0, 3, 5, 2, 3, -1],node1 = 2,node2 = 5) == 2
    assert candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 0,node2 = 3) == 4
    assert candidate(edges = [2, 3, 1, 4, -1, -1, -1, 7, -1, -1, 5, 6],node1 = 0,node2 = 8) == -1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 19) == 0
    assert candidate(edges = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 18) == -1
    assert candidate(edges = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 7) == -1
    assert candidate(edges = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1],node1 = 0,node2 = 20) == -1
    assert candidate(edges = [5, 3, 4, 5, 3, 2, -1],node1 = 1,node2 = 4) == 3
    assert candidate(edges = [3, 1, 2, 3, -1, -1],node1 = 5,node2 = 0) == -1
    assert candidate(edges = [4, 4, 4, 5, 1, 2, 2],node1 = 1,node2 = 5) == 4
    assert candidate(edges = [1, 0, 0, 4, 1],node1 = 0,node2 = 3) == 1
    assert candidate(edges = [2, -1, 3, 1],node1 = 0,node2 = 2) == 2
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],node1 = 0,node2 = 9) == 0
    assert candidate(edges = [10, 15, 11, 14, 13, 12, 5, 15, 9, 12, 15, 9, 10, 11, 13, -1, 12, 14, 15, 8, 5],node1 = 0,node2 = 14) == 10
    assert candidate(edges = [5, 4, 0, 2, 3, 0, 2, 4, 0, 3, 2, 3, 2, 2, 3, 0, 2, 1, 0, 1],node1 = 0,node2 = 1) == 0
    assert candidate(edges = [6, 3, 0, 5, 8, 5, 8, 3, -1, 6],node1 = 5,node2 = 6) == -1
    assert candidate(edges = [3, 0, 5, 5, 2, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],node1 = 0,node2 = 18) == -1
    assert candidate(edges = [1, 0, 3, 2, 1, 4, 5, -1, -1, -1, 8, 9, 7, 10, 11, 12, 13, -1],node1 = 1,node2 = 7) == -1
    assert candidate(edges = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],node1 = 0,node2 = 9) == 1
    assert candidate(edges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1],node1 = 0,node2 = 10) == 10
    assert candidate(edges = [2, 2, 3, 4, 5, -1, 2, 6, 7, -1, -1],node1 = 0,node2 = 1) == 2
    assert candidate(edges = [2, 3, 3, 2],node1 = 0,node2 = 1) == 2
    assert candidate(edges = [5, 4, 0, 2, 3, 0, 2, 4, 0, 3, 2, 3, 2, 2, 3, -1, 2],node1 = 0,node2 = 2) == 0
    assert candidate(edges = [5, 3, 1, 4, 2, 6, 3, 2],node1 = 0,node2 = 5) == 5
    assert candidate(edges = [5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1, -1, -1, 13, -1, 14, -1, 15],node1 = 0,node2 = 15) == -1
    assert candidate(edges = [2, 2, 3, 4, 5, -1, -1, 5, 5, 5],node1 = 0,node2 = 9) == 5
    assert candidate(edges = [1, 2, 0, 1, 3, -1, -1, -1],node1 = 0,node2 = 1) == 1
    assert candidate(edges = [3, 3, 0, 5, -1, 2, 0, -1, -1, 3, 1],node1 = 3,node2 = 10) == 3


