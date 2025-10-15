def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3,relations = [[1, 3], [2, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,relations = [[1, 3], [2, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,relations = [[2, 1], [3, 1], [4, 1], [1, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,relations = [[2, 1], [3, 1], [4, 1], [1, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 6], [5, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 6], [5, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,relations = [[1, 2], [2, 3], [3, 1], [1, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,relations = [[1, 2], [2, 3], [3, 1], [1, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,relations = [[1, 2], [3, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,relations = [[1, 2], [3, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,relations = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,relations = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,relations = [[1, 5], [2, 5], [3, 5], [4, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,relations = [[1, 5], [2, 5], [3, 5], [4, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,relations = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,relations = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,relations = [[1, 2], [2, 3], [3, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,relations = [[1, 2], [2, 3], [3, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,relations = [[2, 1], [3, 1], [1, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,relations = [[2, 1], [3, 1], [1, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,relations = [[1, 2], [2, 3], [3, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,relations = [[1, 2], [2, 3], [3, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,relations = [[1, 2], [2, 4], [1, 3], [3, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,relations = [[1, 2], [2, 4], [1, 3], [3, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,relations = [[1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,relations = [[1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,relations = [[1, 2], [1, 3], [2, 4], [3, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,relations = [[1, 2], [1, 3], [2, 4], [3, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,relations = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,relations = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,relations = [[2, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,relations = [[2, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [1, 7], [7, 10], [10, 13]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [1, 7], [7, 10], [10, 13]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [2, 6], [3, 5], [1, 4], [4, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [2, 6], [3, 5], [1, 4], [4, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 10], [10, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 10], [10, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [2, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [2, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [2, 5], [3, 5], [4, 6], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [2, 5], [3, 5], [4, 6], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 2], [9, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 2], [9, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [3, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [3, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 6], [5, 6], [6, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 6], [5, 6], [6, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 5], [5, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 5], [5, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [3, 5], [5, 7], [7, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [3, 5], [5, 7], [7, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [4, 5], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [4, 5], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [6, 7], [6, 8], [7, 9], [8, 9], [9, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [6, 7], [6, 8], [7, 9], [8, 9], [9, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 3], [2, 4], [5, 7], [6, 8], [7, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 3], [2, 4], [5, 7], [6, 8], [7, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 3], [2, 3], [3, 5], [3, 4], [4, 6], [5, 6], [6, 7], [6, 8], [7, 10], [8, 10], [9, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 3], [2, 3], [3, 5], [3, 4], [4, 6], [5, 6], [6, 7], [6, 8], [7, 10], [8, 10], [9, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 5], [1, 6], [1, 7], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 8], [4, 9], [4, 10], [5, 9], [5, 10], [6, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 5], [1, 6], [1, 7], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 8], [4, 9], [4, 10], [5, 9], [5, 10], [6, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 2], [10, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 2], [10, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7], [7, 8], [7, 9], [8, 10], [9, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7], [7, 8], [7, 9], [8, 10], [9, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 8], [8, 9], [8, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 8], [8, 9], [8, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 3], [1, 4], [2, 4], [2, 5], [3, 6], [4, 6], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 3], [1, 4], [2, 4], [2, 5], [3, 6], [4, 6], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [2, 3], [3, 1], [1, 4], [4, 5], [5, 6], [6, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [2, 3], [3, 1], [1, 4], [4, 5], [5, 6], [6, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,relations = [[1, 2], [2, 3], [4, 5], [5, 6], [3, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,relations = [[1, 2], [2, 3], [4, 5], [5, 6], [3, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [7, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [7, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,relations = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 10], [6, 10], [7, 10], [8, 10], [10, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,relations = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 10], [6, 10], [7, 10], [8, 10], [10, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6], [7, 8], [8, 9], [7, 9], [10, 11], [11, 12], [10, 12], [13, 14], [14, 15], [13, 15]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6], [7, 8], [8, 9], [7, 9], [10, 11], [11, 12], [10, 12], [13, 14], [14, 15], [13, 15]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,relations = [[1, 2], [1, 5], [2, 3], [2, 6], [3, 4], [3, 7], [4, 8], [5, 6], [5, 9], [6, 7], [6, 10], [7, 8], [7, 11], [8, 12], [9, 10], [9, 13], [10, 11], [10, 14], [11, 12], [11, 15], [12, 16], [13, 14], [13, 17], [14, 15], [14, 18], [15, 16], [15, 19], [16, 20], [17, 18], [17, 21], [18, 19], [18, 22], [19, 20], [19, 23], [20, 24], [21, 22], [21, 25], [22, 23], [23, 24], [24, 25]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,relations = [[1, 2], [1, 5], [2, 3], [2, 6], [3, 4], [3, 7], [4, 8], [5, 6], [5, 9], [6, 7], [6, 10], [7, 8], [7, 11], [8, 12], [9, 10], [9, 13], [10, 11], [10, 14], [11, 12], [11, 15], [12, 16], [13, 14], [13, 17], [14, 15], [14, 18], [15, 16], [15, 19], [16, 20], [17, 18], [17, 21], [18, 19], [18, 22], [19, 20], [19, 23], [20, 24], [21, 22], [21, 25], [22, 23], [23, 24], [24, 25]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [6, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [6, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [12, 14], [13, 15], [14, 15]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [12, 14], [13, 15], [14, 15]]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3,relations = [[1, 3], [2, 3]]) == 2
    assert candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == -1
    assert candidate(n = 5,relations = [[2, 1], [3, 1], [4, 1], [1, 5]]) == 3
    assert candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 6], [5, 6]]) == 4
    assert candidate(n = 3,relations = [[1, 2], [2, 3], [3, 1], [1, 3]]) == -1
    assert candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]]) == 4
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
    assert candidate(n = 4,relations = [[1, 2], [3, 4]]) == 2
    assert candidate(n = 3,relations = []) == 1
    assert candidate(n = 5,relations = [[1, 5], [2, 5], [3, 5], [4, 5]]) == 2
    assert candidate(n = 5,relations = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 5
    assert candidate(n = 3,relations = [[1, 2], [2, 3], [3, 1]]) == -1
    assert candidate(n = 4,relations = [[2, 1], [3, 1], [1, 4]]) == 3
    assert candidate(n = 4,relations = [[1, 2], [2, 3], [3, 4]]) == 4
    assert candidate(n = 4,relations = [[1, 2], [2, 4], [1, 3], [3, 4]]) == 3
    assert candidate(n = 2,relations = [[1, 2]]) == 2
    assert candidate(n = 4,relations = [[1, 2], [1, 3], [2, 4], [3, 4]]) == 3
    assert candidate(n = 1,relations = []) == 1
    assert candidate(n = 6,relations = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6]]) == 3
    assert candidate(n = 6,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6]]) == 4
    assert candidate(n = 5,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 5]]) == 4
    assert candidate(n = 7,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7
    assert candidate(n = 2,relations = [[2, 1]]) == 2
    assert candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 6
    assert candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7]]) == 5
    assert candidate(n = 12,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 1]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1
    assert candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [1, 7], [7, 10], [10, 13]]) == 15
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 2]]) == -1
    assert candidate(n = 6,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [2, 6], [3, 5], [1, 4], [4, 2]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 10]]) == -1
    assert candidate(n = 10,relations = [[1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 6]]) == -1
    assert candidate(n = 12,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12]]) == 7
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 10], [10, 7]]) == -1
    assert candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]) == 5
    assert candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [2, 1]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [2, 5], [3, 5], [4, 6], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 8
    assert candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 15
    assert candidate(n = 25,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 25
    assert candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 10
    assert candidate(n = 9,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 4]]) == -1
    assert candidate(n = 9,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 2], [9, 4]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1
    assert candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 1]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 6
    assert candidate(n = 5,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [3, 5]]) == -1
    assert candidate(n = 25,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 20
    assert candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 6], [5, 6], [6, 7]]) == 5
    assert candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10]]) == 5
    assert candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 5], [5, 3]]) == -1
    assert candidate(n = 20,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 20
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 9
    assert candidate(n = 15,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1]]) == -1
    assert candidate(n = 8,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [3, 5], [5, 7], [7, 1]]) == -1
    assert candidate(n = 15,relations = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15]]) == 5
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [4, 5], [10, 1]]) == -1
    assert candidate(n = 6,relations = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [6, 7], [6, 8], [7, 9], [8, 9], [9, 10]]) == 7
    assert candidate(n = 10,relations = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 3], [2, 4], [5, 7], [6, 8], [7, 9]]) == 4
    assert candidate(n = 7,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]) == -1
    assert candidate(n = 10,relations = [[1, 3], [2, 3], [3, 5], [3, 4], [4, 6], [5, 6], [6, 7], [6, 8], [7, 10], [8, 10], [9, 10]]) == 6
    assert candidate(n = 10,relations = [[1, 5], [1, 6], [1, 7], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 8], [4, 9], [4, 10], [5, 9], [5, 10], [6, 10]]) == 3
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 2], [10, 3]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7], [7, 8], [7, 9], [8, 10], [9, 10]]) == 7
    assert candidate(n = 10,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 8], [8, 9], [8, 10]]) == 6
    assert candidate(n = 10,relations = [[1, 3], [1, 4], [2, 4], [2, 5], [3, 6], [4, 6], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 7
    assert candidate(n = 7,relations = [[1, 2], [2, 3], [3, 1], [1, 4], [4, 5], [5, 6], [6, 7]]) == -1
    assert candidate(n = 10,relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 10]]) == -1
    assert candidate(n = 6,relations = [[1, 2], [2, 3], [4, 5], [5, 6], [3, 6]]) == 4
    assert candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [7, 15]]) == 4
    assert candidate(n = 10,relations = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 10], [6, 10], [7, 10], [8, 10], [10, 9]]) == 4
    assert candidate(n = 15,relations = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6], [7, 8], [8, 9], [7, 9], [10, 11], [11, 12], [10, 12], [13, 14], [14, 15], [13, 15]]) == 3
    assert candidate(n = 25,relations = [[1, 2], [1, 5], [2, 3], [2, 6], [3, 4], [3, 7], [4, 8], [5, 6], [5, 9], [6, 7], [6, 10], [7, 8], [7, 11], [8, 12], [9, 10], [9, 13], [10, 11], [10, 14], [11, 12], [11, 15], [12, 16], [13, 14], [13, 17], [14, 15], [14, 18], [15, 16], [15, 19], [16, 20], [17, 18], [17, 21], [18, 19], [18, 22], [19, 20], [19, 23], [20, 24], [21, 22], [21, 25], [22, 23], [23, 24], [24, 25]]) == 10
    assert candidate(n = 7,relations = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [6, 7]]) == 5
    assert candidate(n = 15,relations = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 9], [7, 9], [8, 10], [9, 10], [10, 11], [11, 12], [12, 13], [12, 14], [13, 15], [14, 15]]) == 9


