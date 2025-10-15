def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [3, 1], [2, 0], [4, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [3, 1], [2, 0], [4, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [2, 0], [1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [2, 0], [1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [3, 1], [4, 1], [2, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [3, 1], [4, 1], [2, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [5, 2], [4, 2], [6, 3], [7, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [5, 2], [4, 2], [6, 3], [7, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [5, 1], [6, 1], [3, 2], [4, 2], [7, 3], [8, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [5, 1], [6, 1], [3, 2], [4, 2], [7, 3], [8, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [2, 0], [3, 2], [4, 2], [1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [2, 0], [3, 2], [4, 2], [1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [3, 1], [2, 1], [4, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [3, 1], [2, 1], [4, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [4, 2], [5, 2], [3, 1], [6, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [4, 2], [5, 2], [3, 1], [6, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [2, 0], [1, 0], [4, 2], [3, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [2, 0], [1, 0], [4, 2], [3, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 6], [12, 6], [13, 7], [14, 7], [15, 8], [16, 8], [17, 11], [18, 11], [19, 12], [20, 12], [21, 13], [22, 13]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 6], [12, 6], [13, 7], [14, 7], [15, 8], [16, 8], [17, 11], [18, 11], [19, 12], [20, 12], [21, 13], [22, 13]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 6], [9, 6], [10, 5], [11, 5], [12, 4], [13, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 6], [9, 6], [10, 5], [11, 5], [12, 4], [13, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [6, 3], [2, 0], [4, 2], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [6, 3], [2, 0], [4, 2], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 3], [10, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 3], [10, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3], [11, 4], [12, 4], [13, 5], [14, 5], [15, 6], [16, 6], [17, 7], [18, 7], [19, 8], [20, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3], [11, 4], [12, 4], [13, 5], [14, 5], [15, 6], [16, 6], [17, 7], [18, 7], [19, 8], [20, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3], [11, 4], [12, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3], [11, 4], [12, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8], [13, 10], [14, 10]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8], [13, 10], [14, 10]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 5], [8, 5], [9, 1], [10, 1], [11, 9], [12, 9], [13, 4], [14, 4], [15, 12], [16, 12]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 5], [8, 5], [9, 1], [10, 1], [11, 9], [12, 9], [13, 4], [14, 4], [15, 12], [16, 12]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 2], [7, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 2], [7, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12], [16, 3], [17, 3], [18, 16], [19, 16], [20, 17], [21, 17]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12], [16, 3], [17, 3], [18, 16], [19, 16], [20, 17], [21, 17]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3], [5, 3], [6, 2], [7, 6], [8, 6], [9, 1], [10, 1], [11, 9], [12, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3], [5, 3], [6, 2], [7, 6], [8, 6], [9, 1], [10, 1], [11, 9], [12, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 1], [14, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 1], [14, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 4], [6, 4], [7, 6], [8, 6], [9, 3], [10, 3], [11, 9], [12, 9], [13, 2], [14, 2], [15, 13], [16, 13]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 4], [6, 4], [7, 6], [8, 6], [9, 3], [10, 3], [11, 9], [12, 9], [13, 2], [14, 2], [15, 13], [16, 13]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4], [8, 5], [9, 5], [10, 0], [11, 10], [12, 10]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4], [8, 5], [9, 5], [10, 0], [11, 10], [12, 10]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [7, 5], [9, 7], [11, 9], [2, 0], [4, 2], [6, 4], [8, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [7, 5], [9, 7], [11, 9], [2, 0], [4, 2], [6, 4], [8, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3], [11, 4], [12, 4], [13, 5], [14, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3], [11, 4], [12, 4], [13, 5], [14, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [5, 2], [6, 2], [3, 1], [4, 1], [7, 3], [8, 3], [9, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [5, 2], [6, 2], [3, 1], [4, 1], [7, 3], [8, 3], [9, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 1], [8, 7], [9, 7], [10, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 1], [8, 7], [9, 7], [10, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16], [21, 19], [22, 19], [23, 20], [24, 20]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16], [21, 19], [22, 19], [23, 20], [24, 20]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [5, 1], [6, 1], [2, 0], [3, 2], [4, 2], [7, 3], [8, 3], [9, 4], [10, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [5, 1], [6, 1], [2, 0], [3, 2], [4, 2], [7, 3], [8, 3], [9, 4], [10, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 6], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 6], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2], [9, 7], [10, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2], [9, 7], [10, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 6], [10, 6], [11, 8], [12, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 6], [10, 6], [11, 8], [12, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5], [11, 5], [12, 6], [13, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5], [11, 5], [12, 6], [13, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 7], [12, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 7], [12, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 5], [11, 1], [12, 1], [13, 0], [14, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 5], [11, 1], [12, 1], [13, 0], [14, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 7], [14, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 7], [14, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 3], [12, 3], [13, 4], [14, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 3], [12, 3], [13, 4], [14, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 7], [12, 7], [13, 8], [14, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 7], [12, 7], [13, 8], [14, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8], [13, 5], [14, 5], [15, 6], [16, 6], [17, 9], [18, 9], [19, 10], [20, 10], [21, 11], [22, 11], [23, 12], [24, 12]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8], [13, 5], [14, 5], [15, 6], [16, 6], [17, 9], [18, 9], [19, 10], [20, 10], [21, 11], [22, 11], [23, 12], [24, 12]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 7], [10, 7], [11, 8], [12, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 7], [10, 7], [11, 8], [12, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 5], [11, 1], [12, 1], [13, 0], [14, 15]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 5], [11, 1], [12, 1], [13, 0], [14, 15]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 2], [7, 2], [8, 6], [9, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 2], [7, 2], [8, 6], [9, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 4], [6, 4], [7, 2], [8, 2], [9, 7], [10, 7], [11, 8], [12, 8], [13, 0], [14, 0], [15, 13], [16, 13]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 4], [6, 4], [7, 2], [8, 2], [9, 7], [10, 7], [11, 8], [12, 8], [13, 0], [14, 0], [15, 13], [16, 13]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 3], [10, 2], [11, 2], [12, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 3], [10, 2], [11, 2], [12, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 9]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 9]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3], [5, 4], [6, 4], [7, 3], [8, 2], [9, 1], [10, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3], [5, 4], [6, 4], [7, 3], [8, 2], [9, 1], [10, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2], [9, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2], [9, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 2], [10, 1], [11, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 2], [10, 1], [11, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16], [21, 19], [22, 19], [23, 20], [24, 20], [25, 23], [26, 23], [27, 24], [28, 24]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16], [21, 19], [22, 19], [23, 20], [24, 20], [25, 23], [26, 23], [27, 24], [28, 24]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [7, 5], [8, 5], [9, 3], [11, 9], [12, 9], [2, 0], [4, 2], [6, 4], [10, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [7, 5], [8, 5], [9, 3], [11, 9], [12, 9], [2, 0], [4, 2], [6, 4], [10, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 5], [8, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 5], [8, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 6], [8, 6], [9, 3], [10, 3], [11, 4], [12, 4], [13, 1], [14, 1], [15, 13], [16, 13], [17, 14], [18, 14]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 6], [8, 6], [9, 3], [10, 3], [11, 4], [12, 4], [13, 1], [14, 1], [15, 13], [16, 13], [17, 14], [18, 14]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6], [15, 7], [16, 7], [17, 8], [18, 8], [19, 9], [20, 9], [21, 10], [22, 10]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6], [15, 7], [16, 7], [17, 8], [18, 8], [19, 9], [20, 9], [21, 10], [22, 10]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 6], [10, 6], [11, 0], [12, 11], [13, 12], [14, 12]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 6], [10, 6], [11, 0], [12, 11], [13, 12], [14, 12]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 6], [8, 6], [9, 8], [10, 8]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 6], [8, 6], [9, 8], [10, 8]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 5], [7, 5], [8, 3], [9, 8], [10, 8], [11, 10], [12, 10], [13, 2], [14, 13], [15, 13], [16, 14], [17, 14], [18, 14]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 5], [7, 5], [8, 3], [9, 8], [10, 8], [11, 10], [12, 10], [13, 2], [14, 13], [15, 13], [16, 14], [17, 14], [18, 14]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 6], [9, 6], [10, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 6], [9, 6], [10, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 2], [10, 2], [11, 9], [12, 9], [13, 11], [14, 11]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 2], [10, 2], [11, 9], [12, 9], [13, 11], [14, 11]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12], [16, 3], [17, 3], [18, 16], [19, 16]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12], [16, 3], [17, 3], [18, 16], [19, 16]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 5], [8, 5], [9, 4], [10, 4], [11, 9], [12, 9], [13, 10], [14, 10]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 5], [8, 5], [9, 4], [10, 4], [11, 9], [12, 9], [13, 10], [14, 10]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 2]]) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [3, 1], [2, 0], [4, 2]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 0]]) == True
    assert candidate(nodes = [[0, -1], [2, 0], [1, 0]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [3, 1], [4, 1], [2, 0]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [5, 2], [4, 2], [6, 3], [7, 3]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [5, 1], [6, 1], [3, 2], [4, 2], [7, 3], [8, 3]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1]]) == False
    assert candidate(nodes = [[0, -1], [2, 0], [3, 2], [4, 2], [1, 0]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [3, 1], [2, 1], [4, 2]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [4, 2], [5, 2], [3, 1], [6, 1]]) == False
    assert candidate(nodes = [[0, -1], [2, 0], [1, 0], [4, 2], [3, 2]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 3]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 6], [12, 6], [13, 7], [14, 7], [15, 8], [16, 8], [17, 11], [18, 11], [19, 12], [20, 12], [21, 13], [22, 13]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 6], [9, 6], [10, 5], [11, 5], [12, 4], [13, 2]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [6, 3], [2, 0], [4, 2], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 2], [9, 3], [10, 3]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3], [11, 4], [12, 4], [13, 5], [14, 5], [15, 6], [16, 6], [17, 7], [18, 7], [19, 8], [20, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3], [11, 4], [12, 4]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8], [13, 10], [14, 10]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 5], [8, 5], [9, 1], [10, 1], [11, 9], [12, 9], [13, 4], [14, 4], [15, 12], [16, 12]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 2], [7, 2]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12], [16, 3], [17, 3], [18, 16], [19, 16], [20, 17], [21, 17]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3], [5, 3], [6, 2], [7, 6], [8, 6], [9, 1], [10, 1], [11, 9], [12, 9]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 1], [14, 1]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 4], [6, 4], [7, 6], [8, 6], [9, 3], [10, 3], [11, 9], [12, 9], [13, 2], [14, 2], [15, 13], [16, 13]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4], [8, 5], [9, 5], [10, 0], [11, 10], [12, 10]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [7, 5], [9, 7], [11, 9], [2, 0], [4, 2], [6, 4], [8, 6]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3], [11, 4], [12, 4], [13, 5], [14, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [5, 2], [6, 2], [3, 1], [4, 1], [7, 3], [8, 3], [9, 4]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 1], [8, 7], [9, 7], [10, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16], [21, 19], [22, 19], [23, 20], [24, 20]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [5, 1], [6, 1], [2, 0], [3, 2], [4, 2], [7, 3], [8, 3], [9, 4], [10, 9]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 6], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2], [9, 7], [10, 7]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 6], [10, 6], [11, 8], [12, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5], [11, 5], [12, 6], [13, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 7], [12, 7]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 5], [11, 1], [12, 1], [13, 0], [14, 0]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 1]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [8, 4], [9, 5], [10, 5], [11, 6], [12, 6], [13, 7], [14, 7]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 3], [12, 3], [13, 4], [14, 4]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 6], [10, 6], [11, 7], [12, 7], [13, 8], [14, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [12, 8], [13, 5], [14, 5], [15, 6], [16, 6], [17, 9], [18, 9], [19, 10], [20, 10], [21, 11], [22, 11], [23, 12], [24, 12]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 7], [10, 7], [11, 8], [12, 8]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 5], [11, 1], [12, 1], [13, 0], [14, 15]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 2], [7, 2], [8, 6], [9, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 4], [6, 4], [7, 2], [8, 2], [9, 7], [10, 7], [11, 8], [12, 8], [13, 0], [14, 0], [15, 13], [16, 13]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 3], [10, 2], [11, 2], [12, 0]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 2], [4, 2], [5, 1], [6, 5], [7, 6], [8, 6], [9, 5], [10, 9]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 3], [5, 4], [6, 4], [7, 3], [8, 2], [9, 1], [10, 1]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 2], [8, 2], [9, 7]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 2], [10, 1], [11, 1]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [15, 10], [16, 10], [17, 13], [18, 13], [19, 16], [20, 16], [21, 19], [22, 19], [23, 20], [24, 20], [25, 23], [26, 23], [27, 24], [28, 24]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [3, 1], [5, 3], [7, 5], [8, 5], [9, 3], [11, 9], [12, 9], [2, 0], [4, 2], [6, 4], [10, 6]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 5], [8, 0]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 0], [6, 5], [7, 6], [8, 6], [9, 3], [10, 3], [11, 4], [12, 4], [13, 1], [14, 1], [15, 13], [16, 13], [17, 14], [18, 14]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6], [15, 7], [16, 7], [17, 8], [18, 8], [19, 9], [20, 9], [21, 10], [22, 10]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 6], [10, 6], [11, 0], [12, 11], [13, 12], [14, 12]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 6], [8, 6], [9, 8], [10, 8]]) == True
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 5], [7, 5], [8, 3], [9, 8], [10, 8], [11, 10], [12, 10], [13, 2], [14, 13], [15, 13], [16, 14], [17, 14], [18, 14]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 6], [9, 6], [10, 5]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 5], [8, 5], [9, 2], [10, 2], [11, 9], [12, 9], [13, 11], [14, 11]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [8, 5], [9, 2]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 6], [8, 6], [9, 5], [10, 5], [11, 0], [12, 11], [13, 11], [14, 12], [15, 12], [16, 3], [17, 3], [18, 16], [19, 16]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 0], [3, 2], [4, 2], [5, 3], [6, 3], [7, 5], [8, 5], [9, 4], [10, 4], [11, 9], [12, 9], [13, 10], [14, 10]]) == False
    assert candidate(nodes = [[0, -1], [1, 0], [2, 1], [3, 1], [4, 3], [5, 3], [6, 4], [7, 4], [8, 2]]) == False


