def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(vals = [2, 2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1],edges = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1],edges = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 2, 3, 3, 4, 4],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 2, 3, 3, 4, 4],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 10, 10, 10],edges = [[0, 1], [1, 2], [2, 3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 10, 10, 10],edges = [[0, 1], [1, 2], [2, 3]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 2, 2, 3],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 2, 2, 3],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, 2, 1, 3],edges = [[0, 1], [0, 2], [2, 3], [2, 4]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, 2, 1, 3],edges = [[0, 1], [0, 2], [2, 3], [2, 4]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, 3, 3, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, 3, 3, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 1, 4, 4, 3],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 1, 4, 4, 3],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, 2, 3, 1, 4, 2, 3, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [4, 7], [6, 8]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, 2, 3, 1, 4, 2, 3, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [4, 7], [6, 8]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 2, 3, 3, 3, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 2, 3, 3, 3, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, 2, 3, 1, 3, 3, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, 2, 3, 1, 3, 3, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 1, 2, 1, 2, 1, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 1, 2, 1, 2, 1, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 4, 5, 3, 4, 5, 2, 1, 5, 5, 5],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 4, 5, 3, 4, 5, 2, 1, 5, 5, 5],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 5, 10, 10, 3, 5, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [4, 6]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 5, 10, 10, 3, 5, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [4, 6]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10]]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10]]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(vals = [7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7], [6, 8], [6, 9]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7], [6, 8], [6, 9]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(vals = [4, 2, 5, 3, 1, 6, 1, 2, 4, 5],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [0, 5], [5, 6], [5, 7], [7, 8], [7, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [4, 2, 5, 3, 1, 6, 1, 2, 4, 5],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [0, 5], [5, 6], [5, 7], [7, 8], [7, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6], [6, 7], [7, 8]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6], [6, 7], [7, 8]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, 2, 3, 1, 3, 1, 3, 1, 3],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, 2, 3, 1, 3, 1, 3, 1, 3],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(vals = [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(vals = [4, 2, 3, 4, 3, 4, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [4, 2, 3, 4, 3, 4, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [4, 2, 3, 4, 4, 3, 2, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [4, 2, 3, 4, 4, 3, 2, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, 1, 2, 3, 1, 1, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, 1, 2, 3, 1, 1, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 8], [5, 9], [6, 10]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 8], [5, 9], [6, 10]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 466: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 3, 5, 3, 3, 5, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 3, 5, 3, 3, 5, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 2, 1, 3, 3, 1, 1, 2, 2],edges = [[0, 1], [0, 3], [1, 2], [3, 4], [3, 7], [4, 5], [5, 6], [7, 8], [8, 9]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 2, 1, 3, 3, 1, 1, 2, 2],edges = [[0, 1], [0, 3], [1, 2], [3, 4], [3, 7], [4, 5], [5, 6], [7, 8], [8, 9]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [3, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [3, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 3, 5, 5, 2, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 3, 5, 5, 2, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 1, 2, 3, 1, 3, 2, 1, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 1, 2, 3, 1, 3, 2, 1, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(vals = [2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 1, 2, 3, 3, 2, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 1, 2, 3, 3, 2, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(vals = [4, 3, 3, 4, 4, 4, 3, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [4, 3, 3, 4, 4, 4, 3, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(vals = [2, 2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 15
    assert candidate(vals = [1],edges = []) == 1
    assert candidate(vals = [1, 2, 3, 4, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5
    assert candidate(vals = [1, 2, 2, 3, 3, 4, 4],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 10
    assert candidate(vals = [2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3]]) == 10
    assert candidate(vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(vals = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(vals = [10, 10, 10, 10],edges = [[0, 1], [1, 2], [2, 3]]) == 10
    assert candidate(vals = [1, 1, 2, 2, 3],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 7
    assert candidate(vals = [5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5
    assert candidate(vals = [1, 3, 2, 1, 3],edges = [[0, 1], [0, 2], [2, 3], [2, 4]]) == 6
    assert candidate(vals = [1, 3, 3, 3, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 8
    assert candidate(vals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 12
    assert candidate(vals = [3, 1, 4, 4, 3],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 6
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 55
    assert candidate(vals = [1, 2, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [2, 4]]) == 5
    assert candidate(vals = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 56
    assert candidate(vals = [1, 3, 2, 3, 1, 4, 2, 3, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [4, 7], [6, 8]]) == 13
    assert candidate(vals = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 24
    assert candidate(vals = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 20
    assert candidate(vals = [1, 2, 2, 3, 3, 3, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 11
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19]]) == 20
    assert candidate(vals = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10]]) == 28
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 15
    assert candidate(vals = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 15
    assert candidate(vals = [1, 3, 2, 3, 1, 3, 3, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7]]) == 14
    assert candidate(vals = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 15
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 120
    assert candidate(vals = [1, 2, 1, 2, 1, 2, 1, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 15
    assert candidate(vals = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 37
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 15
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 20
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18]]) == 19
    assert candidate(vals = [5, 4, 5, 3, 4, 5, 2, 1, 5, 5, 5],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 26
    assert candidate(vals = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 91
    assert candidate(vals = [10, 5, 10, 10, 3, 5, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [4, 6]]) == 13
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10]]) == 66
    assert candidate(vals = [7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 43
    assert candidate(vals = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7], [6, 8], [6, 9]]) == 11
    assert candidate(vals = [4, 2, 5, 3, 1, 6, 1, 2, 4, 5],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [0, 5], [5, 6], [5, 7], [7, 8], [7, 9]]) == 10
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15]]) == 16
    assert candidate(vals = [1, 2, 3, 4, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6], [6, 7], [7, 8]]) == 10
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]]) == 45
    assert candidate(vals = [1, 3, 2, 3, 1, 3, 1, 3, 1, 3],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == 23
    assert candidate(vals = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 55
    assert candidate(vals = [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 19
    assert candidate(vals = [4, 2, 3, 4, 3, 4, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 10
    assert candidate(vals = [4, 2, 3, 4, 4, 3, 2, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]) == 15
    assert candidate(vals = [1, 3, 1, 2, 3, 1, 1, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7]]) == 12
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 28
    assert candidate(vals = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 8], [5, 9], [6, 10]]) == 32
    assert candidate(vals = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17]]) == 23
    assert candidate(vals = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 33
    assert candidate(vals = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 16
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 210
    assert candidate(vals = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 19
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 466
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 465
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 36
    assert candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19]]) == 210
    assert candidate(vals = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9]]) == 55
    assert candidate(vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 10
    assert candidate(vals = [5, 3, 5, 3, 3, 5, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 13
    assert candidate(vals = [1, 2, 2, 1, 3, 3, 1, 1, 2, 2],edges = [[0, 1], [0, 3], [1, 2], [3, 4], [3, 7], [4, 5], [5, 6], [7, 8], [8, 9]]) == 20
    assert candidate(vals = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 73
    assert candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 36
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(vals = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [3, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 31
    assert candidate(vals = [5, 3, 5, 5, 2, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]) == 30
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8]]) == 45
    assert candidate(vals = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 16
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 9
    assert candidate(vals = [3, 1, 2, 3, 1, 3, 2, 1, 3, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 19
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 210
    assert candidate(vals = [2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 49
    assert candidate(vals = [3, 1, 2, 3, 3, 2, 3],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 14
    assert candidate(vals = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20]]) == 21
    assert candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 45
    assert candidate(vals = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 210
    assert candidate(vals = [4, 3, 3, 4, 4, 4, 3, 4],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]) == 19
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 10


