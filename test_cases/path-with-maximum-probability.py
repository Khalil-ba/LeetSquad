def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.2, 0.3],start_node = 0,end_node = 3) == 0.006000000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.2, 0.3],start_node = 0,end_node = 3) == 0.006000000000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.9, 0.8],start_node = 0,end_node = 3) == 0.07200000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.9, 0.8],start_node = 0,end_node = 3) == 0.07200000000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 4) == 0.0625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 4) == 0.0625: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 6) == 1.0000000000000004e-06
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 6) == 1.0000000000000004e-06: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 7) == 0.09000000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 7) == 0.09000000000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1], [1, 2], [0, 2]],succProb = [0.5, 0.5, 0.3],start_node = 0,end_node = 2) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1], [1, 2], [0, 2]],succProb = [0.5, 0.5, 0.3],start_node = 0,end_node = 2) == 0.3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 5) == 0.0012000000000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 5) == 0.0012000000000000003: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1], [1, 2], [0, 2]],succProb = [0.5, 0.5, 0.2],start_node = 0,end_node = 2) == 0.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1], [1, 2], [0, 2]],succProb = [0.5, 0.5, 0.2],start_node = 0,end_node = 2) == 0.25: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 4) == 0.12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 4) == 0.12: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.9, 0.5],start_node = 0,end_node = 3) == 0.045000000000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.9, 0.5],start_node = 0,end_node = 3) == 0.045000000000000005: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1]],succProb = [0.5],start_node = 0,end_node = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1]],succProb = [0.5],start_node = 0,end_node = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.9, 0.8, 0.7],start_node = 0,end_node = 3) == 0.504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.9, 0.8, 0.7],start_node = 0,end_node = 3) == 0.504: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.1, 0.9, 0.8, 0.2],start_node = 0,end_node = 4) == 0.014400000000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.1, 0.9, 0.8, 0.2],start_node = 0,end_node = 4) == 0.014400000000000003: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [0, 3], [3, 4]],succProb = [0.9, 0.8, 0.7, 0.6],start_node = 0,end_node = 2) == 0.7200000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [0, 3], [3, 4]],succProb = [0.9, 0.8, 0.7, 0.6],start_node = 0,end_node = 2) == 0.7200000000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [3, 4]],succProb = [0.7, 0.8, 0.9],start_node = 0,end_node = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [3, 4]],succProb = [0.7, 0.8, 0.9],start_node = 0,end_node = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.5, 0.4, 0.3, 0.2],start_node = 0,end_node = 4) == 0.012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.5, 0.4, 0.3, 0.2],start_node = 0,end_node = 4) == 0.012: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.01, 0.99, 0.02, 0.98, 0.03, 0.97, 0.04, 0.96, 0.05, 0.95, 0.06, 0.94, 0.07, 0.93],start_node = 0,end_node = 14) == 3.7815442046807046e-11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.01, 0.99, 0.02, 0.98, 0.03, 0.97, 0.04, 0.96, 0.05, 0.95, 0.06, 0.94, 0.07, 0.93],start_node = 0,end_node = 14) == 3.7815442046807046e-11: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],start_node = 1,end_node = 7) == 0.08000000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],start_node = 1,end_node = 7) == 0.08000000000000002: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 11) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 11) == 0.3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],start_node = 0,end_node = 5) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],start_node = 0,end_node = 5) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],start_node = 0,end_node = 7) == 0.06400000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],start_node = 0,end_node = 7) == 0.06400000000000002: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11], [6, 12], [7, 13], [8, 14], [9, 14]],succProb = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7],start_node = 0,end_node = 14) == 0.028000000000000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11], [6, 12], [7, 13], [8, 14], [9, 14]],succProb = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7],start_node = 0,end_node = 14) == 0.028000000000000004: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 5) == 0.03024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 5) == 0.03024: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.99],start_node = 0,end_node = 6) == 0.99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.99],start_node = 0,end_node = 6) == 0.99: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6],start_node = 0,end_node = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6],start_node = 0,end_node = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 9) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 9) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 0], [1, 4], [4, 5], [5, 6], [6, 7], [7, 4]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 6) == 0.036000000000000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 0], [1, 4], [4, 5], [5, 6], [6, 7], [7, 4]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 6) == 0.036000000000000004: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],succProb = [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5],start_node = 0,end_node = 7) == 0.015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],succProb = [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5],start_node = 0,end_node = 7) == 0.015: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 5) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 5) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],start_node = 0,end_node = 19) == 1.907348632812502e-25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],start_node = 0,end_node = 19) == 1.907348632812502e-25: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [0, 5], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],start_node = 0,end_node = 4) == 0.13999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [0, 5], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],start_node = 0,end_node = 4) == 0.13999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [0, 2], [2, 3], [3, 4], [2, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [0, 2], [2, 3], [3, 4], [2, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 5,end_node = 9) == 0.0625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 5,end_node = 9) == 0.0625: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91],start_node = 0,end_node = 9) == 0.6281565095552946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91],start_node = 0,end_node = 9) == 0.6281565095552946: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 0], [6, 1], [7, 2]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],start_node = 0,end_node = 6) == 0.5599999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 0], [6, 1], [7, 2]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],start_node = 0,end_node = 6) == 0.5599999999999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],succProb = [0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5],start_node = 0,end_node = 9) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],succProb = [0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5],start_node = 0,end_node = 9) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01],start_node = 0,end_node = 6) == 0.7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01],start_node = 0,end_node = 6) == 0.7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 5) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 5) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 19) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 19) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 9) == 0.0003628800000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 9) == 0.0003628800000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [0, 5], [5, 10], [1, 6], [6, 11], [2, 7], [7, 0], [3, 8], [8, 1], [4, 9], [9, 2]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2],start_node = 0,end_node = 11) == 0.33599999999999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [0, 5], [5, 10], [1, 6], [6, 11], [2, 7], [7, 0], [3, 8], [8, 1], [4, 9], [9, 2]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2],start_node = 0,end_node = 11) == 0.33599999999999997: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9],start_node = 0,end_node = 9) == 0.9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9],start_node = 0,end_node = 9) == 0.9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 3], [3, 5], [5, 7], [7, 9]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2],start_node = 0,end_node = 9) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 3], [3, 5], [5, 7], [7, 9]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2],start_node = 0,end_node = 9) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4],start_node = 0,end_node = 14) == 0.048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4],start_node = 0,end_node = 14) == 0.048: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],succProb = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03, 0.04, 0.05],start_node = 0,end_node = 9) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],succProb = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03, 0.04, 0.05],start_node = 0,end_node = 9) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 9) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 9) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 19) == 1.000000000000001e-19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 19) == 1.000000000000001e-19: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 3], [2, 4], [0, 4], [1, 5], [2, 5]],succProb = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.9, 0.9, 0.9, 0.9, 0.9],start_node = 0,end_node = 5) == 0.7290000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 3], [2, 4], [0, 4], [1, 5], [2, 5]],succProb = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.9, 0.9, 0.9, 0.9, 0.9],start_node = 0,end_node = 5) == 0.7290000000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 5) == 0.108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 5) == 0.108: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7], [1, 5], [2, 6], [3, 7]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3],start_node = 0,end_node = 7) == 0.8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7], [1, 5], [2, 6], [3, 7]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3],start_node = 0,end_node = 7) == 0.8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 14) == 2.6127360000000006e-06
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 14) == 2.6127360000000006e-06: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 9) == 0.001953125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 9) == 0.001953125: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [2, 5]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],start_node = 0,end_node = 5) == 0.21600000000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [2, 5]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],start_node = 0,end_node = 5) == 0.21600000000000003: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [0, 14]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 14) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [0, 14]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 14) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 6) == 0.7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 6) == 0.7: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18],start_node = 0,end_node = 14) == 2.6676557107200007e-14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18],start_node = 0,end_node = 14) == 2.6676557107200007e-14: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9],start_node = 0,end_node = 19) == 0.9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9],start_node = 0,end_node = 19) == 0.9: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 5) == 1.0000000000000004e-05
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 5) == 1.0000000000000004e-05: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 9], [0, 8], [8, 9], [1, 7], [1, 6], [6, 7], [2, 5], [2, 4], [4, 5], [3, 0], [3, 1], [3, 2]],succProb = [0.1, 0.2, 0.15, 0.3, 0.4, 0.35, 0.5, 0.6, 0.55, 0.7, 0.8, 0.85],start_node = 3,end_node = 9) == 0.06999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 9], [0, 8], [8, 9], [1, 7], [1, 6], [6, 7], [2, 5], [2, 4], [4, 5], [3, 0], [3, 1], [3, 2]],succProb = [0.1, 0.2, 0.15, 0.3, 0.4, 0.35, 0.5, 0.6, 0.55, 0.7, 0.8, 0.85],start_node = 3,end_node = 9) == 0.06999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 4) == 0.0625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 4) == 0.0625: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2],start_node = 0,end_node = 11) == 0.024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2],start_node = 0,end_node = 11) == 0.024: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 19) == 6.584094720000003e-13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 19) == 6.584094720000003e-13: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],start_node = 0,end_node = 19) == 0.8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],start_node = 0,end_node = 19) == 0.8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],start_node = 0,end_node = 19) == 1.907348632812502e-25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],start_node = 0,end_node = 19) == 1.907348632812502e-25: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01],start_node = 0,end_node = 6) == 1.0000000000000002e-12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01],start_node = 0,end_node = 6) == 1.0000000000000002e-12: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 10], [10, 15]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.3, 0.4],start_node = 0,end_node = 19) == 0.03024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 10], [10, 15]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.3, 0.4],start_node = 0,end_node = 19) == 0.03024: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.15, 0.25, 0.35, 0.45],start_node = 0,end_node = 7) == 0.2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.15, 0.25, 0.35, 0.45],start_node = 0,end_node = 7) == 0.2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.99],start_node = 0,end_node = 11) == 9.900000000000002e-21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.99],start_node = 0,end_node = 11) == 9.900000000000002e-21: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 0]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],start_node = 0,end_node = 24) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 0]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],start_node = 0,end_node = 24) == 0.3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.2, 0.3],start_node = 0,end_node = 3) == 0.006000000000000001
    assert candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.9, 0.8],start_node = 0,end_node = 3) == 0.07200000000000001
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 4) == 0.0625
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 6) == 1.0000000000000004e-06
    assert candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 7) == 0.09000000000000001
    assert candidate(n = 3,edges = [[0, 1], [1, 2], [0, 2]],succProb = [0.5, 0.5, 0.3],start_node = 0,end_node = 2) == 0.3
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 5) == 0.0012000000000000003
    assert candidate(n = 3,edges = [[0, 1], [1, 2], [0, 2]],succProb = [0.5, 0.5, 0.2],start_node = 0,end_node = 2) == 0.25
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 4) == 0.12
    assert candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.1, 0.9, 0.5],start_node = 0,end_node = 3) == 0.045000000000000005
    assert candidate(n = 3,edges = [[0, 1]],succProb = [0.5],start_node = 0,end_node = 2) == 0
    assert candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]],succProb = [0.9, 0.8, 0.7],start_node = 0,end_node = 3) == 0.504
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.1, 0.9, 0.8, 0.2],start_node = 0,end_node = 4) == 0.014400000000000003
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [0, 3], [3, 4]],succProb = [0.9, 0.8, 0.7, 0.6],start_node = 0,end_node = 2) == 0.7200000000000001
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [3, 4]],succProb = [0.7, 0.8, 0.9],start_node = 0,end_node = 4) == 0
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]],succProb = [0.5, 0.4, 0.3, 0.2],start_node = 0,end_node = 4) == 0.012
    assert candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.01, 0.99, 0.02, 0.98, 0.03, 0.97, 0.04, 0.96, 0.05, 0.95, 0.06, 0.94, 0.07, 0.93],start_node = 0,end_node = 14) == 3.7815442046807046e-11
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],start_node = 1,end_node = 7) == 0.08000000000000002
    assert candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 11) == 0.3
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],start_node = 0,end_node = 5) == 0.5
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],start_node = 0,end_node = 7) == 0.06400000000000002
    assert candidate(n = 15,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11], [6, 12], [7, 13], [8, 14], [9, 14]],succProb = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7],start_node = 0,end_node = 14) == 0.028000000000000004
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 5) == 0.03024
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.99],start_node = 0,end_node = 6) == 0.99
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6],start_node = 0,end_node = 9) == 0
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 9) == 0.1
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 0], [1, 4], [4, 5], [5, 6], [6, 7], [7, 4]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 6) == 0.036000000000000004
    assert candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],succProb = [0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5],start_node = 0,end_node = 7) == 0.015
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 5) == 0.6
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],start_node = 0,end_node = 19) == 1.907348632812502e-25
    assert candidate(n = 6,edges = [[0, 1], [0, 5], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],start_node = 0,end_node = 4) == 0.13999999999999999
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [0, 2], [2, 3], [3, 4], [2, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 9) == 0
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 5,end_node = 9) == 0.0625
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.92, 0.91],start_node = 0,end_node = 9) == 0.6281565095552946
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 0], [6, 1], [7, 2]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],start_node = 0,end_node = 6) == 0.5599999999999999
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],succProb = [0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5],start_node = 0,end_node = 9) == 0.5
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01],start_node = 0,end_node = 6) == 0.7
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 5) == 0.5
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 19) == 0.1
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 9) == 0.0003628800000000001
    assert candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [0, 5], [5, 10], [1, 6], [6, 11], [2, 7], [7, 0], [3, 8], [8, 1], [4, 9], [9, 2]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2],start_node = 0,end_node = 11) == 0.33599999999999997
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9],start_node = 0,end_node = 9) == 0.9
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 3], [3, 5], [5, 7], [7, 9]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2],start_node = 0,end_node = 9) == 0.1
    assert candidate(n = 15,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4],start_node = 0,end_node = 14) == 0.048
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],succProb = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01, 0.02, 0.03, 0.04, 0.05],start_node = 0,end_node = 9) == 0.1
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 9) == 0.1
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 19) == 1.000000000000001e-19
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 3], [2, 4], [0, 4], [1, 5], [2, 5]],succProb = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.9, 0.9, 0.9, 0.9, 0.9],start_node = 0,end_node = 5) == 0.7290000000000001
    assert candidate(n = 6,edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],start_node = 0,end_node = 5) == 0.108
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7], [1, 5], [2, 6], [3, 7]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3],start_node = 0,end_node = 7) == 0.8
    assert candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],start_node = 0,end_node = 14) == 2.6127360000000006e-06
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 9) == 0.001953125
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [2, 5]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],start_node = 0,end_node = 5) == 0.21600000000000003
    assert candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [0, 14]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 14) == 0.1
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 6], [1, 3], [2, 4], [3, 5]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1],start_node = 0,end_node = 6) == 0.7
    assert candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],succProb = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18],start_node = 0,end_node = 14) == 2.6676557107200007e-14
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9],start_node = 0,end_node = 19) == 0.9
    assert candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]],succProb = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],start_node = 0,end_node = 5) == 1.0000000000000004e-05
    assert candidate(n = 10,edges = [[0, 9], [0, 8], [8, 9], [1, 7], [1, 6], [6, 7], [2, 5], [2, 4], [4, 5], [3, 0], [3, 1], [3, 2]],succProb = [0.1, 0.2, 0.15, 0.3, 0.4, 0.35, 0.5, 0.6, 0.55, 0.7, 0.8, 0.85],start_node = 3,end_node = 9) == 0.06999999999999999
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],succProb = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],start_node = 0,end_node = 4) == 0.0625
    assert candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2],start_node = 0,end_node = 11) == 0.024
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5],start_node = 0,end_node = 19) == 6.584094720000003e-13
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],start_node = 0,end_node = 19) == 0.8
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]],succProb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],start_node = 0,end_node = 19) == 1.907348632812502e-25
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01],start_node = 0,end_node = 6) == 1.0000000000000002e-12
    assert candidate(n = 20,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [0, 10], [10, 15]],succProb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.3, 0.4],start_node = 0,end_node = 19) == 0.03024
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.15, 0.25, 0.35, 0.45],start_node = 0,end_node = 7) == 0.2
    assert candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],succProb = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.99],start_node = 0,end_node = 11) == 9.900000000000002e-21
    assert candidate(n = 25,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 0]],succProb = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3],start_node = 0,end_node = 24) == 0.3


