def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],start = [0, 4],destination = [4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],start = [0, 4],destination = [4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],start = [4, 3],destination = [0, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],start = [4, 3],destination = [0, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]],start = [0, 0],destination = [2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]],start = [0, 0],destination = [2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],start = [0, 4],destination = [3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],start = [0, 4],destination = [3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],start = [0, 0],destination = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],start = [0, 0],destination = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],start = [2, 0],destination = [0, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],start = [2, 0],destination = [0, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0]],start = [0, 4],destination = [5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0]],start = [0, 4],destination = [5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0]],start = [2, 2],destination = [5, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0]],start = [2, 2],destination = [5, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [4, 5],destination = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [4, 5],destination = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]],start = [5, 0],destination = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]],start = [5, 0],destination = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]],start = [3, 4],destination = [1, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]],start = [3, 4],destination = [1, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],start = [0, 0],destination = [5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],start = [0, 0],destination = [5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]],start = [5, 0],destination = [0, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]],start = [5, 0],destination = [0, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [4, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [4, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]],start = [3, 3],destination = [6, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]],start = [3, 3],destination = [6, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [6, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [6, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0]],start = [0, 5],destination = [5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0]],start = [0, 5],destination = [5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],start = [1, 1],destination = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],start = [1, 1],destination = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [4, 0],destination = [0, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [4, 0],destination = [0, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [6, 9],destination = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [6, 9],destination = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]],start = [2, 0],destination = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]],start = [2, 0],destination = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],start = [0, 0],destination = [4, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],start = [0, 0],destination = [4, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 1],destination = [6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 1],destination = [6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0]],start = [0, 5],destination = [5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0]],start = [0, 5],destination = [5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0]],start = [4, 7],destination = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0]],start = [4, 7],destination = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [1, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [1, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [0, 6],destination = [4, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [0, 6],destination = [4, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]],start = [0, 0],destination = [4, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]],start = [0, 0],destination = [4, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 1],destination = [6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 1],destination = [6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [1, 1],destination = [5, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [1, 1],destination = [5, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]],start = [2, 3],destination = [3, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]],start = [2, 3],destination = [3, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [5, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [5, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [4, 0],destination = [0, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [4, 0],destination = [0, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]],start = [0, 5],destination = [5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]],start = [0, 5],destination = [5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [6, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [6, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]],start = [5, 0],destination = [3, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]],start = [5, 0],destination = [3, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]],start = [0, 4],destination = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]],start = [0, 4],destination = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [4, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [4, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0]],start = [1, 1],destination = [4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0]],start = [1, 1],destination = [4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0]],start = [2, 0],destination = [2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0]],start = [2, 0],destination = [2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [0, 4],destination = [5, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [0, 4],destination = [5, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [1, 2],destination = [6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [1, 2],destination = [6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 2],destination = [2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 2],destination = [2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [0, 4],destination = [2, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [0, 4],destination = [2, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0]],start = [0, 4],destination = [4, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0]],start = [0, 4],destination = [4, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],start = [0, 0],destination = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],start = [0, 0],destination = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0]],start = [0, 0],destination = [5, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0]],start = [0, 0],destination = [5, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [6, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [6, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [0, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [0, 8]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],start = [0, 4],destination = [4, 4]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],start = [4, 3],destination = [0, 1]) == False
    assert candidate(maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]],start = [0, 0],destination = [2, 2]) == True
    assert candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],start = [0, 4],destination = [3, 2]) == False
    assert candidate(maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],start = [0, 0],destination = [1, 1]) == False
    assert candidate(maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],start = [2, 0],destination = [0, 2]) == True
    assert candidate(maze = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0]],start = [0, 4],destination = [5, 6]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0]],start = [2, 2],destination = [5, 0]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [4, 5],destination = [0, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 7]) == True
    assert candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 4]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 7]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]],start = [5, 0],destination = [0, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [1, 1]) == False
    assert candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]],start = [3, 4],destination = [1, 4]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],start = [0, 0],destination = [5, 4]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 8]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 8]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [6, 6]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 9]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]],start = [5, 0],destination = [0, 5]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [4, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [8, 9]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]],start = [3, 3],destination = [6, 4]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [6, 10]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0]],start = [0, 5],destination = [5, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 6]) == True
    assert candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],start = [1, 1],destination = [5, 5]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 9]) == True
    assert candidate(maze = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 5]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [4, 0],destination = [0, 7]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 8]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [6, 9],destination = [0, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [2, 4]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]],start = [2, 0],destination = [5, 5]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],start = [0, 0],destination = [4, 7]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [8, 9]) == True
    assert candidate(maze = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 1],destination = [6, 6]) == False
    assert candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0]],start = [0, 5],destination = [5, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0]],start = [4, 7],destination = [0, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [1, 7]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [0, 6],destination = [4, 0]) == False
    assert candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]],start = [0, 0],destination = [4, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 1],destination = [6, 7]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 5]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [1, 1],destination = [5, 7]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]],start = [2, 3],destination = [3, 0]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [5, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [4, 6]) == True
    assert candidate(maze = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [4, 0],destination = [0, 4]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 8]) == True
    assert candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]],start = [0, 5],destination = [5, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [6, 5]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [2, 3]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [5, 0],destination = [0, 5]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 5],destination = [5, 5]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]],start = [5, 0],destination = [3, 4]) == False
    assert candidate(maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]],start = [0, 4],destination = [6, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [4, 7]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0]],start = [1, 1],destination = [4, 5]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [6, 9]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0]],start = [2, 0],destination = [2, 4]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [0, 4],destination = [5, 0]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],start = [1, 2],destination = [6, 6]) == False
    assert candidate(maze = [[0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],start = [0, 2],destination = [2, 4]) == True
    assert candidate(maze = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]],start = [0, 4],destination = [2, 5]) == False
    assert candidate(maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0]],start = [0, 4],destination = [4, 0]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 10]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],start = [0, 0],destination = [6, 6]) == True
    assert candidate(maze = [[0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0]],start = [0, 0],destination = [5, 2]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]],start = [2, 3],destination = [6, 4]) == False
    assert candidate(maze = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],start = [0, 0],destination = [4, 4]) == True
    assert candidate(maze = [[0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],start = [3, 0],destination = [0, 8]) == True


