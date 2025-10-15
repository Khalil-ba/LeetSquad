def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 3], [3, 1], [1, 2], [2, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 3], [3, 1], [1, 2], [2, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requests = [[0, 1], [1, 0], [0, 2], [2, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requests = [[0, 1], [1, 0], [0, 2], [2, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requests = [[0, 1], [1, 2], [2, 0], [0, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requests = [[0, 1], [1, 2], [2, 0], [0, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 3], [3, 4], [4, 2], [2, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 3], [3, 4], [4, 2], [2, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requests = [[0, 0], [1, 2], [2, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requests = [[0, 0], [1, 2], [2, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,requests = [[0, 0], [1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,requests = [[0, 0], [1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requests = [[0, 1], [1, 0], [1, 2], [2, 1], [0, 2], [2, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requests = [[0, 1], [1, 0], [1, 2], [2, 1], [0, 2], [2, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,requests = [[0, 1], [1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,requests = [[0, 1], [1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4], [5, 0], [0, 5], [0, 2], [2, 0], [1, 3], [3, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4], [5, 0], [0, 5], [0, 2], [2, 0], [1, 3], [3, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [2, 1], [1, 3], [3, 2], [0, 3], [3, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [2, 1], [1, 3], [3, 2], [0, 3], [3, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [0, 7], [1, 6], [2, 5], [3, 4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [0, 7], [1, 6], [2, 5], [3, 4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [1, 3], [3, 1], [2, 3], [3, 2], [0, 3], [3, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [1, 3], [3, 1], [2, 3], [3, 2], [0, 3], [3, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0], [1, 3], [3, 5], [5, 7], [7, 9], [9, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0], [1, 3], [3, 5], [5, 7], [7, 9], [9, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1], [0, 3], [1, 4], [2, 0], [3, 1], [4, 2]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1], [0, 3], [1, 4], [2, 0], [3, 1], [4, 2]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 6], [6, 1], [1, 4], [4, 7], [7, 2], [2, 5], [5, 0]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 6], [6, 1], [1, 4], [4, 7], [7, 2], [2, 5], [5, 0]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1], [0, 3], [1, 4], [2, 5], [3, 0], [4, 1], [5, 2], [0, 4], [1, 5], [2, 0], [3, 1], [4, 2], [5, 3]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1], [0, 3], [1, 4], [2, 5], [3, 0], [4, 1], [5, 2], [0, 4], [1, 5], [2, 0], [3, 1], [4, 2], [5, 3]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [3, 6], [6, 9], [9, 2], [2, 5], [5, 8], [8, 1], [1, 4], [4, 7], [7, 0]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [3, 6], [6, 9], [9, 2], [2, 5], [5, 8], [8, 1], [1, 4], [4, 7], [7, 0]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 5], [5, 10], [10, 3]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 5], [5, 10], [10, 3]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [2, 1], [1, 3], [3, 2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [2, 1], [1, 3], [3, 2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1], [0, 3], [1, 0], [2, 1], [3, 2]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1], [0, 3], [1, 0], [2, 1], [3, 2]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [7, 14], [14, 7], [7, 0], [0, 7]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [7, 14], [14, 7], [7, 0], [0, 7]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [3, 6], [6, 3], [3, 0], [0, 3], [3, 0], [0, 6], [6, 0], [0, 3], [3, 0]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [3, 6], [6, 3], [3, 0], [0, 3], [3, 0], [0, 6], [6, 0], [0, 3], [3, 0]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 6], [1, 4], [4, 7], [2, 5], [5, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 6], [1, 4], [4, 7], [2, 5], [5, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 1], [1, 2], [2, 3], [3, 0], [0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1], [0, 3], [1, 0], [2, 1], [3, 2]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 1], [1, 2], [2, 3], [3, 0], [0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1], [0, 3], [1, 0], [2, 1], [3, 2]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 3], [3, 6], [6, 4], [4, 7], [7, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 3], [3, 6], [6, 4], [4, 7], [7, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 2], [1, 4], [4, 0]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 2], [1, 4], [4, 0]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [2, 4], [4, 1], [1, 3], [3, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [2, 4], [4, 1], [1, 3], [3, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 6], [1, 5], [2, 4]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 6], [1, 5], [2, 4]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [6, 3], [3, 9], [9, 5], [5, 1], [1, 7], [7, 10], [10, 4], [4, 8], [8, 2], [2, 11], [11, 0]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [6, 3], [3, 9], [9, 5], [5, 1], [1, 7], [7, 10], [10, 4], [4, 8], [8, 2], [2, 11], [11, 0]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [0, 4], [4, 0], [1, 2], [2, 1], [1, 3], [3, 1], [1, 4], [4, 1], [2, 3], [3, 2], [2, 4], [4, 2], [3, 4], [4, 3]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [0, 4], [4, 0], [1, 2], [2, 1], [1, 3], [3, 1], [1, 4], [4, 1], [2, 3], [3, 2], [2, 4], [4, 2], [3, 4], [4, 3]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2], [0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2], [0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [0, 2], [1, 0], [2, 0], [1, 2], [2, 1], [3, 4], [4, 3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [0, 2], [1, 0], [2, 0], [1, 2], [2, 1], [3, 4], [4, 3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [0, 3], [3, 0], [1, 4], [4, 1], [2, 5], [5, 2]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [0, 3], [3, 0], [1, 4], [4, 1], [2, 5], [5, 2]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requests = [[0, 1], [1, 2], [2, 0], [0, 2], [1, 0], [2, 1], [0, 1], [1, 2], [2, 0]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requests = [[0, 1], [1, 2], [2, 0], [0, 2], [1, 0], [2, 1], [0, 1], [1, 2], [2, 0]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 7], [7, 0]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 7], [7, 0]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 4], [1, 3], [2, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 4], [1, 3], [2, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 3]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 3]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 1], [1, 3], [3, 5], [5, 7], [7, 9], [9, 1]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 1], [1, 3], [3, 5], [5, 7], [7, 9], [9, 1]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 7], [7, 1], [1, 6], [6, 2], [2, 5], [5, 3], [3, 4], [4, 0], [0, 2], [2, 4], [4, 6], [6, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 7], [7, 1], [1, 6], [6, 2], [2, 5], [5, 3], [3, 4], [4, 0], [0, 2], [2, 4], [4, 6], [6, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [7, 12], [12, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [7, 12], [12, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [0, 1], [1, 0], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1], [0, 3], [3, 0], [1, 3], [3, 1], [2, 3], [3, 2], [0, 4], [4, 0], [1, 4], [4, 1], [2, 4], [4, 2], [3, 4], [4, 3]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [0, 1], [1, 0], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1], [0, 3], [3, 0], [1, 3], [3, 1], [2, 3], [3, 2], [0, 4], [4, 0], [1, 4], [4, 1], [2, 4], [4, 2], [3, 4], [4, 3]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 0], [0, 9], [9, 15], [15, 3]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 0], [0, 9], [9, 15], [15, 3]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 1], [6, 2], [7, 3]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 1], [6, 2], [7, 3]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [3, 6], [6, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [3, 6], [6, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 1], [11, 2]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 1], [11, 2]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [2, 4], [4, 1], [1, 3], [3, 5], [5, 3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [2, 4], [4, 1], [1, 3], [3, 5], [5, 3]]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 6
    assert candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0]]) == 6
    assert candidate(n = 4,requests = [[0, 3], [3, 1], [1, 2], [2, 0]]) == 4
    assert candidate(n = 3,requests = [[0, 1], [1, 0], [0, 2], [2, 0]]) == 4
    assert candidate(n = 3,requests = [[0, 1], [1, 2], [2, 0], [0, 2]]) == 3
    assert candidate(n = 6,requests = [[0, 3], [3, 4], [4, 2], [2, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 7
    assert candidate(n = 3,requests = [[0, 0], [1, 2], [2, 1]]) == 3
    assert candidate(n = 2,requests = [[0, 0], [1, 1]]) == 2
    assert candidate(n = 3,requests = [[0, 1], [1, 0], [1, 2], [2, 1], [0, 2], [2, 0]]) == 6
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == 5
    assert candidate(n = 5,requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5
    assert candidate(n = 2,requests = [[0, 1], [1, 0]]) == 2
    assert candidate(n = 6,requests = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4], [5, 0], [0, 5], [0, 2], [2, 0], [1, 3], [3, 1]]) == 16
    assert candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [2, 1], [1, 3], [3, 2], [0, 3], [3, 1]]) == 8
    assert candidate(n = 8,requests = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [0, 7], [1, 6], [2, 5], [3, 4]]) == 8
    assert candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [1, 3], [3, 1], [2, 3], [3, 2], [0, 3], [3, 0]]) == 10
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]]) == 14
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0], [1, 3], [3, 5], [5, 7], [7, 9], [9, 1]]) == 20
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1], [0, 3], [1, 4], [2, 0], [3, 1], [4, 2]]) == 15
    assert candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 6], [6, 1], [1, 4], [4, 7], [7, 2], [2, 5], [5, 0]]) == 16
    assert candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 16
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1], [0, 3], [1, 4], [2, 5], [3, 0], [4, 1], [5, 2], [0, 4], [1, 5], [2, 0], [3, 1], [4, 2], [5, 3]]) == 24
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == 12
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [3, 6], [6, 9], [9, 2], [2, 5], [5, 8], [8, 1], [1, 4], [4, 7], [7, 0]]) == 20
    assert candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 5], [5, 10], [10, 3]]) == 12
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 18
    assert candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [2, 1], [1, 3], [3, 2]]) == 7
    assert candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1], [0, 3], [1, 0], [2, 1], [3, 2]]) == 12
    assert candidate(n = 20,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]]) == 20
    assert candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [7, 14], [14, 7], [7, 0], [0, 7]]) == 19
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [3, 6], [6, 3], [3, 0], [0, 3], [3, 0], [0, 6], [6, 0], [0, 3], [3, 0]]) == 17
    assert candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 6], [1, 4], [4, 7], [2, 5], [5, 0]]) == 10
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]]) == 15
    assert candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 1], [1, 2], [2, 3], [3, 0], [0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1], [0, 3], [1, 0], [2, 1], [3, 2]]) == 20
    assert candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 3], [3, 6], [6, 4], [4, 7], [7, 5]]) == 15
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 2], [1, 4], [4, 0]]) == 9
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [2, 4], [4, 1], [1, 3], [3, 0]]) == 10
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 6], [1, 5], [2, 4]]) == 7
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 0]]) == 14
    assert candidate(n = 9,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 18
    assert candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [6, 3], [3, 9], [9, 5], [5, 1], [1, 7], [7, 10], [10, 4], [4, 8], [8, 2], [2, 11], [11, 0]]) == 24
    assert candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]]) == 15
    assert candidate(n = 5,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [0, 4], [4, 0], [1, 2], [2, 1], [1, 3], [3, 1], [1, 4], [4, 1], [2, 3], [3, 2], [2, 4], [4, 2], [3, 4], [4, 3]]) == 20
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]) == 10
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2], [0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == 20
    assert candidate(n = 4,requests = [[0, 1], [1, 0], [0, 2], [2, 0], [0, 3], [3, 0], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]]) == 12
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == 10
    assert candidate(n = 5,requests = [[0, 1], [0, 2], [1, 0], [2, 0], [1, 2], [2, 1], [3, 4], [4, 3]]) == 8
    assert candidate(n = 6,requests = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [0, 3], [3, 0], [1, 4], [4, 1], [2, 5], [5, 2]]) == 12
    assert candidate(n = 4,requests = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3], [2, 0], [3, 1]]) == 8
    assert candidate(n = 3,requests = [[0, 1], [1, 2], [2, 0], [0, 2], [1, 0], [2, 1], [0, 1], [1, 2], [2, 0]]) == 9
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == 10
    assert candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 7], [7, 0]]) == 16
    assert candidate(n = 6,requests = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == 12
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 4], [1, 3], [2, 0]]) == 5
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1]]) == 14
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 3]]) == 11
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 1], [1, 3], [3, 5], [5, 7], [7, 9], [9, 1]]) == 19
    assert candidate(n = 8,requests = [[0, 7], [7, 1], [1, 6], [6, 2], [2, 5], [5, 3], [3, 4], [4, 0], [0, 2], [2, 4], [4, 6], [6, 0]]) == 12
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [1, 3], [2, 4], [3, 5]]) == 12
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3], [3, 1], [1, 4], [4, 2], [2, 5], [5, 0]]) == 12
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 10
    assert candidate(n = 15,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [7, 12], [12, 5]]) == 15
    assert candidate(n = 5,requests = [[0, 1], [0, 1], [1, 0], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1], [0, 3], [3, 0], [1, 3], [3, 1], [2, 3], [3, 2], [0, 4], [4, 0], [1, 4], [4, 1], [2, 4], [4, 2], [3, 4], [4, 3]]) == 22
    assert candidate(n = 18,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 0], [0, 9], [9, 15], [15, 3]]) == 18
    assert candidate(n = 8,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 1], [6, 2], [7, 3]]) == 15
    assert candidate(n = 10,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [3, 6], [6, 9]]) == 10
    assert candidate(n = 12,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 1], [11, 2]]) == 23
    assert candidate(n = 5,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == 10
    assert candidate(n = 7,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 13
    assert candidate(n = 6,requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 2], [2, 4], [4, 1], [1, 3], [3, 5], [5, 3]]) == 10


