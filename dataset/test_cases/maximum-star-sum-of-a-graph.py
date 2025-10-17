def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(vals = [5, -2, 3, 1],edges = [[0, 1], [0, 2], [0, 3]],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, -2, 3, 1],edges = [[0, 1], [0, 2], [0, 3]],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 10, -10, -20],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]],k = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 10, -10, -20],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]],k = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 4) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 4) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-5],edges = [],k = 0) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-5],edges = [],k = 0) == -5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 6, 7, 8, 9],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],k = 3) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 6, 7, 8, 9],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],k = 3) == 29: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 3, -2, 5],edges = [[0, 1], [1, 2], [2, 3]],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 3, -2, 5],edges = [[0, 1], [1, 2], [2, 3]],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, -1, 1, -1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, -1, 1, -1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 5) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 5) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-1, -2, -3, -4, -5],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-1, -2, -3, -4, -5],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3]],k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3]],k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, -200, 300, 400, -500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 1) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, -200, 300, 400, -500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 1) == 700: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, -10, 20, -20, 30, -30],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, -10, 20, -20, 30, -30],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 30: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 0]],k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 0]],k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40],edges = [[0, 1], [1, 2], [2, 3]],k = 1) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40],edges = [[0, 1], [1, 2], [2, 3]],k = 1) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, -1, 2, 3, -4],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, -1, 2, 3, -4],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, -40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2]],k = 3) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, -40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2]],k = 3) == 110: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]],k = 5) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]],k = 5) == 350: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500, 600],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500, 600],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [2, 3], [3, 4]],k = 4) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [2, 3], [3, 4]],k = 4) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, -1, 3, 9, 2, -6, 7],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]],k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, -1, 3, 9, 2, -6, 7],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]],k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, -50, 20, -10, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 3) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, -50, 20, -10, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 3) == 125: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-5, -3, -10, -4, -1],edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4]],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-5, -3, -10, -4, -1],edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4]],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 10) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 10) == 27: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, 20, -30, 40, -50, 60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, 20, -30, 40, -50, 60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 70: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2]],k = 3) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2]],k = 3) == 140: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 270: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, -1, 3, 7, 9, -2],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4], [4, 5]],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, -1, 3, 7, 9, -2],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4], [4, 5]],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],k = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],k = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 2) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 2) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],k = 7) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],k = 7) == 42: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, -3, 8, 0, 2],edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, -3, 8, 0, 2],edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 1, 3, 7, 9, 2, 8, 6],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],k = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 1, 3, 7, 9, 2, 8, 6],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],k = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4]],k = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4]],k = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 4) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 4) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 15, 25, 35, 45, 55],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 15, 25, 35, 45, 55],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 135: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9]],k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9]],k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],k = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],k = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10000, -10000, 5000, -5000, 2500, -2500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 3) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10000, -10000, 5000, -5000, 2500, -2500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 3) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [4, 6], [5, 7], [8, 0], [9, 1], [2, 4], [3, 5], [6, 8], [7, 9]],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [4, 6], [5, 7], [8, 0], [9, 1], [2, 4], [3, 5], [6, 8], [7, 9]],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 5) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 5) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == 2700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == 2700: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, -50, 20, -30, 60, 10],edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 5]],k = 3) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, -50, 20, -30, 60, 10],edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 5]],k = 3) == 180: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 27000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 27000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],k = 3) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],k = 3) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, -5, 15, -15, 25, -25],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, -5, 15, -15, 25, -25],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 25: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000, 6000, -6000, 7000, -7000, 8000, -8000, 9000, -9000, 10000, -10000],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15], [16, 18], [17, 19]],k = 4) == 19000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000, 6000, -6000, 7000, -7000, 8000, -8000, 9000, -9000, 10000, -10000],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15], [16, 18], [17, 19]],k = 4) == 19000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500, 600, 700, 800, 900],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],k = 5) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500, 600, 700, 800, 900],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],k = 5) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 9) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 9) == 50: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [],k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [],k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 5) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 5) == 41: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 9]],k = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 9]],k = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, 20, 30, -40, 50, -60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, 20, 30, -40, 50, -60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 50: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 5]],k = 3) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 5]],k = 3) == 130: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [],k = 4) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [],k = 4) == 100: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, -100, 200, -200, 300, -300],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [1, 4], [2, 5]],k = 4) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, -100, 200, -200, 300, -300],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [1, 4], [2, 5]],k = 4) == 500: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, -1, 1, -1, 1, -1, 1, -1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, -1, 1, -1, 1, -1, 1, -1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],k = 1) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],k = 1) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],k = 2) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],k = 2) == 270: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [1, 3], [2, 4]],k = 3) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [1, 3], [2, 4]],k = 3) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, -1, 2, 4, 6, -3],edges = [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5]],k = 3) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, -1, 2, 4, 6, -3],edges = [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5]],k = 3) == 17: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 500: {e}')
    
    total += 1
    try:
        result = candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 0) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 0) == 500: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]],k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]],k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],k = 7) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],k = 7) == 42: {e}')
    
    total += 1
    try:
        result = candidate(vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 6) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 6) == 24: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, -20, -30, -40, -50, -60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 0) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, -20, -30, -40, -50, -60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 0) == -10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 4) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 4) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-1000, -2000, -3000, -4000, -5000],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 3) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-1000, -2000, -3000, -4000, -5000],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 3) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10, 20, 30, -40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 2], [1, 3]],k = 2) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10, 20, 30, -40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 2], [1, 3]],k = 2) == 50: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9]],k = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9]],k = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == 270: {e}')
    
    total += 1
    try:
        result = candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],k = 4) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],k = 4) == 25: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3]],k = 3) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3]],k = 3) == 140: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, -10, 20, -20, 30, -30, 40, -40],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7]],k = 2) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, -10, 20, -20, 30, -30, 40, -40],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7]],k = 2) == 70: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, -5, 20, 0, 15],edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],k = 3) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, -5, 20, 0, 15],edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],k = 3) == 35: {e}')
    
    total += 1
    try:
        result = candidate(vals = [50, 30, 10, -10, -30, -50, -70, 90, 110],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 3], [2, 4], [5, 7]],k = 6) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [50, 30, 10, -10, -30, -50, -70, 90, 110],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 3], [2, 4], [5, 7]],k = 6) == 250: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 15, 25, 35, 45, 55, 65],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [0, 3], [1, 4], [2, 5]],k = 5) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 15, 25, 35, 45, 55, 65],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [0, 3], [1, 4], [2, 5]],k = 5) == 190: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 7], [7, 8], [8, 9]],k = 5) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 7], [7, 8], [8, 9]],k = 5) == 320: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 270: {e}')
    
    total += 1
    try:
        result = candidate(vals = [5, 10, 15, 20, 25, 30],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 2) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [5, 10, 15, 20, 25, 30],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 2) == 75: {e}')
    
    total += 1
    try:
        result = candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [-10000, 10000, -9000, 9000, -8000, 8000, -7000, 7000, -6000, 6000],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 2) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [-10000, 10000, -9000, 9000, -8000, 8000, -7000, 7000, -6000, 6000],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 2) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],k = 5) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],k = 5) == 310: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(vals = [5, -2, 3, 1],edges = [[0, 1], [0, 2], [0, 3]],k = 3) == 9
    assert candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 0) == 3
    assert candidate(vals = [1, 2, 3, 4, 10, -10, -20],edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]],k = 2) == 16
    assert candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 4) == 1200
    assert candidate(vals = [-5],edges = [],k = 0) == -5
    assert candidate(vals = [5, 6, 7, 8, 9],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],k = 3) == 29
    assert candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 0) == 3
    assert candidate(vals = [1, 3, -2, 5],edges = [[0, 1], [1, 2], [2, 3]],k = 1) == 5
    assert candidate(vals = [1, -1, 1, -1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 1) == 1
    assert candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 5) == 1200
    assert candidate(vals = [-1, -2, -3, -4, -5],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 2) == -1
    assert candidate(vals = [1, 2, 3],edges = [[0, 1], [1, 2]],k = 1) == 5
    assert candidate(vals = [5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3]],k = 3) == 15
    assert candidate(vals = [100, -200, 300, 400, -500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 1) == 700
    assert candidate(vals = [10, -10, 20, -20, 30, -30],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 30
    assert candidate(vals = [5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 0]],k = 3) == 15
    assert candidate(vals = [-10, -20, -30, -40],edges = [[0, 1], [1, 2], [2, 3]],k = 1) == -10
    assert candidate(vals = [5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 3) == 20
    assert candidate(vals = [10, -1, 2, 3, -4],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 2) == 15
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 3
    assert candidate(vals = [10, 20, 30, -40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2]],k = 3) == 110
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]],k = 5) == 350
    assert candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == -1
    assert candidate(vals = [100, 200, 300, 400, 500, 600],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 1500
    assert candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],k = 4) == 0
    assert candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [2, 3], [3, 4]],k = 4) == 1500
    assert candidate(vals = [5, -1, 3, 9, 2, -6, 7],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]],k = 3) == 13
    assert candidate(vals = [100, -50, 20, -10, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4]],k = 3) == 125
    assert candidate(vals = [-5, -3, -10, -4, -1],edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4]],k = 2) == -1
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 10) == 27
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 3
    assert candidate(vals = [-10, 20, -30, 40, -50, 60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 70
    assert candidate(vals = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2]],k = 3) == 140
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 270
    assert candidate(vals = [5, -1, 3, 7, 9, -2],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4], [4, 5]],k = 3) == 19
    assert candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],k = 2) == 120
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 5) == 6
    assert candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 2) == -10
    assert candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 5) == 0
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],k = 7) == 42
    assert candidate(vals = [5, -3, 8, 0, 2],edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],k = 3) == 13
    assert candidate(vals = [5, 1, 3, 7, 9, 2, 8, 6],edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],k = 3) == 20
    assert candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4]],k = 2) == 120
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 5) == 3
    assert candidate(vals = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == -10
    assert candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 4) == -10
    assert candidate(vals = [5, 15, 25, 35, 45, 55],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 135
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9]],k = 3) == 24
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],k = 2) == 210
    assert candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 2) == 0
    assert candidate(vals = [10000, -10000, 5000, -5000, 2500, -2500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 3) == 10000
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 4) == 35
    assert candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [4, 6], [5, 7], [8, 0], [9, 1], [2, 4], [3, 5], [6, 8], [7, 9]],k = 3) == 12
    assert candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],k = 5) == 1200
    assert candidate(vals = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == 2700
    assert candidate(vals = [100, -50, 20, -30, 60, 10],edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 5]],k = 3) == 180
    assert candidate(vals = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 27000
    assert candidate(vals = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],k = 3) == -10
    assert candidate(vals = [5, -5, 15, -15, 25, -25],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 25
    assert candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000, 6000, -6000, 7000, -7000, 8000, -8000, 9000, -9000, 10000, -10000],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15], [16, 18], [17, 19]],k = 4) == 19000
    assert candidate(vals = [100, 200, 300, 400, 500, 600, 700, 800, 900],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],k = 5) == 2400
    assert candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 9) == 50
    assert candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [],k = 3) == -1
    assert candidate(vals = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 50
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 5) == 41
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 9]],k = 4) == 21
    assert candidate(vals = [-10, 20, 30, -40, 50, -60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 4) == 50
    assert candidate(vals = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 5]],k = 3) == 130
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [],k = 4) == 100
    assert candidate(vals = [100, -100, 200, -200, 300, -300],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [1, 4], [2, 5]],k = 4) == 500
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],k = 10) == 3
    assert candidate(vals = [1, -1, 1, -1, 1, -1, 1, -1, 1],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]],k = 3) == 2
    assert candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],k = 1) == 5000
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],k = 2) == 270
    assert candidate(vals = [-10, -20, -30, -40, -50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [1, 3], [2, 4]],k = 3) == -10
    assert candidate(vals = [5, -1, 2, 4, 6, -3],edges = [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5]],k = 3) == 17
    assert candidate(vals = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 500
    assert candidate(vals = [100, 200, 300, 400, 500],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 0) == 500
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 0) == 10
    assert candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]],k = 4) == 12
    assert candidate(vals = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 3) == -1
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],k = 7) == 42
    assert candidate(vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 6) == 24
    assert candidate(vals = [-10, -20, -30, -40, -50, -60],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],k = 0) == -10
    assert candidate(vals = [10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 4) == 10000
    assert candidate(vals = [-1000, -2000, -3000, -4000, -5000],edges = [[0, 1], [1, 2], [2, 3], [3, 4]],k = 3) == -1000
    assert candidate(vals = [-10, 20, 30, -40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 2], [1, 3]],k = 2) == 50
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9]],k = 2) == 21
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 3) == 270
    assert candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 0
    assert candidate(vals = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],k = 4) == 25
    assert candidate(vals = [10, 20, 30, 40, 50],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3]],k = 3) == 140
    assert candidate(vals = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],k = 5) == 12
    assert candidate(vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 4) == 5
    assert candidate(vals = [10, -10, 20, -20, 30, -30, 40, -40],edges = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7]],k = 2) == 70
    assert candidate(vals = [10, -5, 20, 0, 15],edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],k = 3) == 35
    assert candidate(vals = [50, 30, 10, -10, -30, -50, -70, 90, 110],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 3], [2, 4], [5, 7]],k = 6) == 250
    assert candidate(vals = [5, 15, 25, 35, 45, 55, 65],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [0, 3], [1, 4], [2, 5]],k = 5) == 190
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 7], [7, 8], [8, 9]],k = 5) == 320
    assert candidate(vals = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],edges = [],k = 2) == -1
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],k = 10) == 270
    assert candidate(vals = [5, 10, 15, 20, 25, 30],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],k = 2) == 75
    assert candidate(vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 3) == 0
    assert candidate(vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],edges = [],k = 5) == 10
    assert candidate(vals = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],k = 5) == 5000
    assert candidate(vals = [-10000, 10000, -9000, 9000, -8000, 8000, -7000, 7000, -6000, 6000],edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],k = 2) == 10000
    assert candidate(vals = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],k = 5) == 310


