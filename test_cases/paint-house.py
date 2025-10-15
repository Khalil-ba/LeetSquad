def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(costs = [[11, 11, 13], [8, 12, 18], [9, 10, 3]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[11, 11, 13], [8, 12, 18], [9, 10, 3]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[7, 6, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[7, 6, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[11, 14, 5], [11, 14, 5], [13, 14, 7]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[11, 14, 5], [11, 14, 5], [13, 14, 7]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 19, 19], [18, 17, 16], [18, 17, 16], [16, 16, 5], [49, 50, 51]]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 19, 19], [18, 17, 16], [18, 17, 16], [16, 16, 5], [49, 50, 51]]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[12, 19, 8], [13, 14, 15], [10, 12, 14], [9, 10, 11], [12, 13, 11]]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[12, 19, 8], [13, 14, 15], [10, 12, 14], [9, 10, 11], [12, 13, 11]]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[11, 17, 12], [15, 16, 10], [14, 18, 13], [12, 19, 14], [10, 20, 15], [9, 21, 16]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[11, 17, 12], [15, 16, 10], [14, 18, 13], [12, 19, 14], [10, 20, 15], [9, 21, 16]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 20, 10], [10, 15, 10], [20, 10, 15], [10, 10, 15]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 20, 10], [10, 15, 10], [20, 10, 15], [10, 10, 15]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[16, 18, 19], [14, 15, 17], [13, 12, 11], [19, 20, 18], [17, 16, 15], [12, 14, 13], [11, 10, 12]]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[16, 18, 19], [14, 15, 17], [13, 12, 11], [19, 20, 18], [17, 16, 15], [12, 14, 13], [11, 10, 12]]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[3, 3, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[3, 3, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 10, 15], [15, 10, 5], [10, 5, 15], [5, 15, 10], [15, 10, 5]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 10, 15], [15, 10, 5], [10, 5, 15], [5, 15, 10], [15, 10, 5]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 20, 1], [2, 1, 20], [3, 2, 1], [20, 1, 2], [1, 20, 1], [2, 1, 20], [3, 2, 1], [20, 1, 2], [1, 20, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 20, 1], [2, 1, 20], [3, 2, 1], [20, 1, 2], [1, 20, 1], [2, 1, 20], [3, 2, 1], [20, 1, 2], [1, 20, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 20, 10], [10, 15, 20], [12, 13, 14], [17, 16, 15], [18, 19, 20]]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 20, 10], [10, 15, 20], [12, 13, 14], [17, 16, 15], [18, 19, 20]]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 1, 10], [1, 10, 20], [10, 20, 1], [20, 1, 10], [1, 10, 20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 1, 10], [1, 10, 20], [10, 20, 1], [20, 1, 10], [1, 10, 20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 19, 20], [2, 1, 20], [3, 2, 1], [20, 19, 1], [20, 20, 20]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 19, 20], [2, 1, 20], [3, 2, 1], [20, 19, 1], [20, 20, 20]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 14, 12], [11, 13, 10], [9, 16, 11], [15, 12, 13], [7, 15, 10], [8, 11, 9], [12, 14, 16]]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 14, 12], [11, 13, 10], [9, 16, 11], [15, 12, 13], [7, 15, 10], [8, 11, 9], [12, 14, 16]]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 18, 5], [15, 3, 13], [4, 19, 3], [2, 7, 12]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 18, 5], [15, 3, 13], [4, 19, 3], [2, 7, 12]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 1, 10], [10, 20, 1], [1, 10, 20], [20, 1, 10], [10, 20, 1], [1, 10, 20]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 1, 10], [10, 20, 1], [1, 10, 20], [20, 1, 10], [10, 20, 1], [1, 10, 20]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[12, 19, 11], [11, 12, 19], [19, 11, 12], [12, 19, 11], [11, 12, 19], [19, 11, 12], [12, 19, 11]]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[12, 19, 11], [11, 12, 19], [19, 11, 12], [12, 19, 11], [11, 12, 19], [19, 11, 12], [12, 19, 11]]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 100, 50], [100, 1, 50], [50, 50, 1], [1, 100, 100], [50, 50, 50]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 100, 50], [100, 1, 50], [50, 50, 1], [1, 100, 100], [50, 50, 50]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 19, 17], [18, 16, 14], [13, 15, 12], [10, 11, 9], [8, 7, 5]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 19, 17], [18, 16, 14], [13, 15, 12], [10, 11, 9], [8, 7, 5]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[8, 6, 10], [6, 10, 8], [10, 8, 6], [8, 6, 10], [6, 10, 8], [10, 8, 6], [8, 6, 10], [6, 10, 8], [10, 8, 6]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[8, 6, 10], [6, 10, 8], [10, 8, 6], [8, 6, 10], [6, 10, 8], [10, 8, 6], [8, 6, 10], [6, 10, 8], [10, 8, 6]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[4, 8, 7], [5, 1, 9], [2, 4, 6], [9, 3, 5], [1, 6, 4], [3, 2, 8], [7, 5, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[4, 8, 7], [5, 1, 9], [2, 4, 6], [9, 3, 5], [1, 6, 4], [3, 2, 8], [7, 5, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 1, 20], [20, 10, 1], [1, 20, 10], [10, 20, 1], [20, 1, 10], [1, 10, 20]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 1, 20], [20, 10, 1], [1, 20, 10], [10, 20, 1], [20, 1, 10], [1, 10, 20]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 18, 19], [2, 1, 4], [5, 3, 6], [8, 7, 9], [11, 10, 12], [14, 13, 15]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 18, 19], [2, 1, 4], [5, 3, 6], [8, 7, 9], [11, 10, 12], [14, 13, 15]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[2, 1, 1], [2, 3, 2], [3, 2, 2], [2, 4, 1], [1, 3, 2], [1, 1, 1], [1, 2, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[2, 1, 1], [2, 3, 2], [3, 2, 2], [2, 4, 1], [1, 3, 2], [1, 1, 1], [1, 2, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[11, 5, 3], [7, 9, 4], [12, 8, 6], [6, 5, 7], [14, 12, 11], [10, 13, 9]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[11, 5, 3], [7, 9, 4], [12, 8, 6], [6, 5, 7], [14, 12, 11], [10, 13, 9]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 5, 3], [1, 4, 2], [1, 3, 4], [1, 2, 3], [1, 3, 2], [1, 2, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 5, 3], [1, 4, 2], [1, 3, 4], [1, 2, 3], [1, 3, 2], [1, 2, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 1, 19], [18, 20, 2], [17, 18, 19], [16, 17, 18], [15, 16, 17]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 1, 19], [18, 20, 2], [17, 18, 19], [16, 17, 18], [15, 16, 17]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[17, 14, 10], [16, 9, 13], [15, 11, 14], [14, 8, 12], [13, 7, 11], [12, 6, 10], [11, 5, 9], [10, 4, 8], [9, 3, 7], [8, 2, 6]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[17, 14, 10], [16, 9, 13], [15, 11, 14], [14, 8, 12], [13, 7, 11], [12, 6, 10], [11, 5, 9], [10, 4, 8], [9, 3, 7], [8, 2, 6]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30], [30, 10, 20], [20, 30, 10]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30], [30, 10, 20], [20, 30, 10]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[7, 6, 2], [3, 8, 5], [4, 6, 3], [2, 5, 7], [1, 3, 2], [8, 4, 6], [9, 7, 5], [6, 1, 8]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[7, 6, 2], [3, 8, 5], [4, 6, 3], [2, 5, 7], [1, 3, 2], [8, 4, 6], [9, 7, 5], [6, 1, 8]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 5, 5], [10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35]]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 5, 5], [10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35]]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 4, 3], [2, 5, 1], [7, 1, 2], [4, 2, 6], [9, 8, 5], [3, 7, 9]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 4, 3], [2, 5, 1], [7, 1, 2], [4, 2, 6], [9, 8, 5], [3, 7, 9]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 3, 6], [1, 9, 8], [2, 7, 4], [8, 2, 9], [3, 5, 2], [6, 8, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 3, 6], [1, 9, 8], [2, 7, 4], [8, 2, 9], [3, 5, 2], [6, 8, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[8, 1, 3], [5, 7, 4], [10, 5, 2], [11, 8, 6], [4, 9, 1]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[8, 1, 3], [5, 7, 4], [10, 5, 2], [11, 8, 6], [4, 9, 1]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 1, 100], [1, 100, 10], [1, 1, 100]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 1, 100], [1, 100, 10], [1, 1, 100]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[8, 15, 20], [25, 10, 5], [30, 20, 10], [15, 25, 30], [10, 5, 15]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[8, 15, 20], [25, 10, 5], [30, 20, 10], [15, 25, 30], [10, 5, 15]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 20, 19], [20, 1, 2], [19, 2, 1], [2, 1, 20], [1, 2, 19]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 20, 19], [20, 1, 2], [19, 2, 1], [2, 1, 20], [1, 2, 19]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 8, 6], [3, 7, 4], [2, 6, 3], [8, 10, 7], [6, 9, 5]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 8, 6], [3, 7, 4], [2, 6, 3], [8, 10, 7], [6, 9, 5]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1], [1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1], [1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 1, 1], [19, 2, 2], [18, 3, 3], [17, 4, 4], [16, 5, 5], [15, 6, 6], [14, 7, 7], [13, 8, 8], [12, 9, 9]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 1, 1], [19, 2, 2], [18, 3, 3], [17, 4, 4], [16, 5, 5], [15, 6, 6], [14, 7, 7], [13, 8, 8], [12, 9, 9]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 18, 19], [17, 15, 16], [14, 12, 13], [11, 9, 10], [8, 6, 7], [5, 3, 4], [2, 1, 2]]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 18, 19], [17, 15, 16], [14, 12, 13], [11, 9, 10], [8, 6, 7], [5, 3, 4], [2, 1, 2]]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[3, 2, 20], [10, 3, 1], [5, 10, 2], [8, 5, 3], [11, 8, 5], [14, 11, 8], [17, 14, 11]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[3, 2, 20], [10, 3, 1], [5, 10, 2], [8, 5, 3], [11, 8, 5], [14, 11, 8], [17, 14, 11]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[12, 10, 14], [13, 15, 11], [16, 12, 9], [18, 16, 13]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[12, 10, 14], [13, 15, 11], [16, 12, 9], [18, 16, 13]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 3, 2], [3, 2, 1], [2, 1, 3], [3, 2, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 3, 2], [3, 2, 1], [2, 1, 3], [3, 2, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 15, 10], [10, 3, 18], [12, 18, 9], [8, 12, 15], [7, 10, 12]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 15, 10], [10, 3, 18], [12, 18, 9], [8, 12, 15], [7, 10, 12]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19]]) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19]]) == 380: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 10, 15], [10, 5, 15], [15, 10, 5], [5, 10, 15], [10, 5, 15], [15, 10, 5], [5, 10, 15], [10, 5, 15], [15, 10, 5]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 10, 15], [10, 5, 15], [15, 10, 5], [5, 10, 15], [10, 5, 15], [15, 10, 5], [5, 10, 15], [10, 5, 15], [15, 10, 5]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[2, 5, 7], [6, 3, 8], [1, 4, 9], [9, 7, 3], [5, 1, 6], [8, 2, 4]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[2, 5, 7], [6, 3, 8], [1, 4, 9], [9, 7, 3], [5, 1, 6], [8, 2, 4]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 10, 10], [1, 1, 1], [5, 5, 5], [2, 2, 2], [3, 3, 3]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 10, 10], [1, 1, 1], [5, 5, 5], [2, 2, 2], [3, 3, 3]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 18, 16], [14, 12, 10], [8, 6, 4], [2, 0, 1], [9, 7, 5]]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 18, 16], [14, 12, 10], [8, 6, 4], [2, 0, 1], [9, 7, 5]]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[12, 15, 10], [3, 18, 6], [4, 7, 8], [9, 10, 11], [5, 14, 2]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[12, 15, 10], [3, 18, 6], [4, 7, 8], [9, 10, 11], [5, 14, 2]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[19, 20, 18], [17, 16, 15], [14, 13, 12], [11, 10, 9], [8, 7, 6], [5, 4, 3], [2, 1, 0]]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[19, 20, 18], [17, 16, 15], [14, 13, 12], [11, 10, 9], [8, 7, 6], [5, 4, 3], [2, 1, 0]]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[17, 20, 16], [14, 13, 16], [15, 16, 14], [16, 14, 15], [15, 14, 16]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[17, 20, 16], [14, 13, 16], [15, 16, 14], [16, 14, 15], [15, 14, 16]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[7, 3, 8], [6, 4, 9], [2, 5, 7], [8, 1, 6], [4, 8, 2], [5, 6, 3], [9, 7, 1], [3, 9, 5], [6, 2, 8], [1, 7, 4]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[7, 3, 8], [6, 4, 9], [2, 5, 7], [8, 1, 6], [4, 8, 2], [5, 6, 3], [9, 7, 1], [3, 9, 5], [6, 2, 8], [1, 7, 4]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[19, 7, 13], [15, 20, 18], [8, 12, 15], [6, 11, 9], [17, 14, 16], [2, 10, 14], [5, 8, 12]]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[19, 7, 13], [15, 20, 18], [8, 12, 15], [6, 11, 9], [17, 14, 16], [2, 10, 14], [5, 8, 12]]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 25, 35], [20, 10, 30], [25, 20, 5], [30, 15, 10]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 25, 35], [20, 10, 30], [25, 20, 5], [30, 15, 10]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 10, 20], [10, 1, 20], [20, 10, 1], [1, 20, 10], [20, 1, 10], [10, 20, 1], [1, 10, 20], [10, 1, 20], [20, 10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 10, 20], [10, 1, 20], [20, 10, 1], [1, 20, 10], [20, 1, 10], [10, 20, 1], [1, 10, 20], [10, 1, 20], [20, 10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 15, 10], [17, 13, 12], [19, 18, 11], [12, 20, 15], [8, 14, 10]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 15, 10], [17, 13, 12], [19, 18, 11], [12, 20, 15], [8, 14, 10]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]) == 370: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[10, 5, 10], [5, 10, 5], [10, 5, 10], [5, 10, 5], [10, 5, 10]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[10, 5, 10], [5, 10, 5], [10, 5, 10], [5, 10, 5], [10, 5, 10]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1], [1, 1, 100], [1, 100, 1], [100, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1], [1, 1, 100], [1, 100, 1], [100, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 5, 3], [2, 4, 6], [3, 7, 9], [4, 8, 10], [5, 9, 11], [6, 10, 12]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 5, 3], [2, 4, 6], [3, 7, 9], [4, 8, 10], [5, 9, 11], [6, 10, 12]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[12, 5, 8], [10, 15, 9], [11, 13, 7], [6, 18, 14]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[12, 5, 8], [10, 15, 9], [11, 13, 7], [6, 18, 14]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[19, 18, 17], [16, 15, 14], [13, 12, 11], [10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 20, 19], [18, 17, 16], [15, 14, 13], [12, 11, 10]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[19, 18, 17], [16, 15, 14], [13, 12, 11], [10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 20, 19], [18, 17, 16], [15, 14, 13], [12, 11, 10]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[5, 3, 6], [4, 7, 8], [3, 2, 4], [7, 6, 5], [8, 9, 10], [11, 12, 13]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[5, 3, 6], [4, 7, 8], [3, 2, 4], [7, 6, 5], [8, 9, 10], [11, 12, 13]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 18, 20], [20, 16, 15], [13, 17, 14], [19, 12, 18]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 18, 20], [20, 16, 15], [13, 17, 14], [19, 12, 18]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[20, 1, 10], [10, 1, 10], [10, 10, 1], [1, 1, 20], [2, 1, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[20, 1, 10], [10, 1, 10], [10, 10, 1], [1, 1, 20], [2, 1, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 3, 2], [2, 1, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 3, 2], [2, 1, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[6, 15, 12], [10, 13, 7], [4, 11, 14], [3, 9, 10], [18, 16, 17], [1, 19, 15]]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[6, 15, 12], [10, 13, 7], [4, 11, 14], [3, 9, 10], [18, 16, 17], [1, 19, 15]]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 20, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 1]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 20, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 1]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[18, 9, 3], [16, 2, 4], [10, 12, 1], [3, 1, 11], [6, 9, 12], [15, 13, 5], [2, 14, 7], [8, 15, 6], [17, 11, 8], [14, 7, 9]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[18, 9, 3], [16, 2, 4], [10, 12, 1], [3, 1, 11], [6, 9, 12], [15, 13, 5], [2, 14, 7], [8, 15, 6], [17, 11, 8], [14, 7, 9]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[15, 18, 20], [5, 8, 12], [3, 6, 9], [7, 14, 16]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[15, 18, 20], [5, 8, 12], [3, 6, 9], [7, 14, 16]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[11, 12, 13], [13, 11, 12], [12, 13, 11], [11, 13, 12], [13, 12, 11], [12, 11, 13], [13, 11, 12]]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[11, 12, 13], [13, 11, 12], [12, 13, 11], [11, 13, 12], [13, 12, 11], [12, 11, 13], [13, 11, 12]]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[18, 20, 17], [19, 18, 20], [17, 19, 18], [18, 17, 19], [19, 18, 20], [17, 19, 18], [18, 17, 19]]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[18, 20, 17], [19, 18, 20], [17, 19, 18], [18, 17, 19], [19, 18, 20], [17, 19, 18], [18, 17, 19]]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[8, 12, 11], [9, 7, 8], [13, 14, 6], [10, 9, 10], [15, 16, 14]]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[8, 12, 11], [9, 7, 8], [13, 14, 6], [10, 9, 10], [15, 16, 14]]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(costs = [[11, 11, 13], [8, 12, 18], [9, 10, 3]]) == 22
    assert candidate(costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
    assert candidate(costs = [[7, 6, 2]]) == 2
    assert candidate(costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12]]) == 23
    assert candidate(costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
    assert candidate(costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]]) == 43
    assert candidate(costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]) == 26
    assert candidate(costs = [[11, 14, 5], [11, 14, 5], [13, 14, 7]]) == 23
    assert candidate(costs = [[20, 19, 19], [18, 17, 16], [18, 17, 16], [16, 16, 5], [49, 50, 51]]) == 106
    assert candidate(costs = [[12, 19, 8], [13, 14, 15], [10, 12, 14], [9, 10, 11], [12, 13, 11]]) == 53
    assert candidate(costs = [[11, 17, 12], [15, 16, 10], [14, 18, 13], [12, 19, 14], [10, 20, 15], [9, 21, 16]]) == 75
    assert candidate(costs = [[15, 20, 10], [10, 15, 10], [20, 10, 15], [10, 10, 15]]) == 40
    assert candidate(costs = [[16, 18, 19], [14, 15, 17], [13, 12, 11], [19, 20, 18], [17, 16, 15], [12, 14, 13], [11, 10, 12]]) == 98
    assert candidate(costs = [[3, 3, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 27
    assert candidate(costs = [[5, 10, 15], [15, 10, 5], [10, 5, 15], [5, 15, 10], [15, 10, 5]]) == 25
    assert candidate(costs = [[1, 20, 1], [2, 1, 20], [3, 2, 1], [20, 1, 2], [1, 20, 1], [2, 1, 20], [3, 2, 1], [20, 1, 2], [1, 20, 1]]) == 9
    assert candidate(costs = [[15, 20, 10], [10, 15, 20], [12, 13, 14], [17, 16, 15], [18, 19, 20]]) == 66
    assert candidate(costs = [[20, 1, 10], [1, 10, 20], [10, 20, 1], [20, 1, 10], [1, 10, 20]]) == 5
    assert candidate(costs = [[1, 19, 20], [2, 1, 20], [3, 2, 1], [20, 19, 1], [20, 20, 20]]) == 26
    assert candidate(costs = [[10, 14, 12], [11, 13, 10], [9, 16, 11], [15, 12, 13], [7, 15, 10], [8, 11, 9], [12, 14, 16]]) == 69
    assert candidate(costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]]) == 45
    assert candidate(costs = [[15, 18, 5], [15, 3, 13], [4, 19, 3], [2, 7, 12]]) == 13
    assert candidate(costs = [[20, 1, 10], [10, 20, 1], [1, 10, 20], [20, 1, 10], [10, 20, 1], [1, 10, 20]]) == 6
    assert candidate(costs = [[12, 19, 11], [11, 12, 19], [19, 11, 12], [12, 19, 11], [11, 12, 19], [19, 11, 12], [12, 19, 11]]) == 77
    assert candidate(costs = [[15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15], [15, 15, 15]]) == 150
    assert candidate(costs = [[1, 100, 50], [100, 1, 50], [50, 50, 1], [1, 100, 100], [50, 50, 50]]) == 54
    assert candidate(costs = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 45
    assert candidate(costs = [[20, 19, 17], [18, 16, 14], [13, 15, 12], [10, 11, 9], [8, 7, 5]]) == 60
    assert candidate(costs = [[8, 6, 10], [6, 10, 8], [10, 8, 6], [8, 6, 10], [6, 10, 8], [10, 8, 6], [8, 6, 10], [6, 10, 8], [10, 8, 6]]) == 54
    assert candidate(costs = [[4, 8, 7], [5, 1, 9], [2, 4, 6], [9, 3, 5], [1, 6, 4], [3, 2, 8], [7, 5, 1]]) == 14
    assert candidate(costs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 55
    assert candidate(costs = [[10, 1, 20], [20, 10, 1], [1, 20, 10], [10, 20, 1], [20, 1, 10], [1, 10, 20]]) == 6
    assert candidate(costs = [[20, 18, 19], [2, 1, 4], [5, 3, 6], [8, 7, 9], [11, 10, 12], [14, 13, 15]]) == 55
    assert candidate(costs = [[2, 1, 1], [2, 3, 2], [3, 2, 2], [2, 4, 1], [1, 3, 2], [1, 1, 1], [1, 2, 1]]) == 9
    assert candidate(costs = [[11, 5, 3], [7, 9, 4], [12, 8, 6], [6, 5, 7], [14, 12, 11], [10, 13, 9]]) == 42
    assert candidate(costs = [[1, 5, 3], [1, 4, 2], [1, 3, 4], [1, 2, 3], [1, 3, 2], [1, 2, 1]]) == 8
    assert candidate(costs = [[20, 1, 19], [18, 20, 2], [17, 18, 19], [16, 17, 18], [15, 16, 17]]) == 52
    assert candidate(costs = [[20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20]]) == 300
    assert candidate(costs = [[17, 14, 10], [16, 9, 13], [15, 11, 14], [14, 8, 12], [13, 7, 11], [12, 6, 10], [11, 5, 9], [10, 4, 8], [9, 3, 7], [8, 2, 6]]) == 80
    assert candidate(costs = [[10, 20, 30], [30, 10, 20], [20, 30, 10], [10, 20, 30], [30, 10, 20], [20, 30, 10]]) == 60
    assert candidate(costs = [[7, 6, 2], [3, 8, 5], [4, 6, 3], [2, 5, 7], [1, 3, 2], [8, 4, 6], [9, 7, 5], [6, 1, 8]]) == 22
    assert candidate(costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 5
    assert candidate(costs = [[20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19], [19, 20, 1], [1, 19, 20], [20, 1, 19]]) == 10
    assert candidate(costs = [[5, 5, 5], [10, 10, 10], [15, 15, 15], [20, 20, 20], [25, 25, 25], [30, 30, 30], [35, 35, 35]]) == 140
    assert candidate(costs = [[5, 4, 3], [2, 5, 1], [7, 1, 2], [4, 2, 6], [9, 8, 5], [3, 7, 9]]) == 17
    assert candidate(costs = [[5, 3, 6], [1, 9, 8], [2, 7, 4], [8, 2, 9], [3, 5, 2], [6, 8, 1]]) == 14
    assert candidate(costs = [[8, 1, 3], [5, 7, 4], [10, 5, 2], [11, 8, 6], [4, 9, 1]]) == 17
    assert candidate(costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]]) == 150
    assert candidate(costs = [[10, 1, 100], [1, 100, 10], [1, 1, 100]]) == 3
    assert candidate(costs = [[8, 15, 20], [25, 10, 5], [30, 20, 10], [15, 25, 30], [10, 5, 15]]) == 48
    assert candidate(costs = [[1, 20, 19], [20, 1, 2], [19, 2, 1], [2, 1, 20], [1, 2, 19]]) == 5
    assert candidate(costs = [[5, 8, 6], [3, 7, 4], [2, 6, 3], [8, 10, 7], [6, 9, 5]]) == 24
    assert candidate(costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1], [1, 1, 1]]) == 4
    assert candidate(costs = [[20, 1, 1], [19, 2, 2], [18, 3, 3], [17, 4, 4], [16, 5, 5], [15, 6, 6], [14, 7, 7], [13, 8, 8], [12, 9, 9]]) == 45
    assert candidate(costs = [[20, 18, 19], [17, 15, 16], [14, 12, 13], [11, 9, 10], [8, 6, 7], [5, 3, 4], [2, 1, 2]]) == 67
    assert candidate(costs = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) == 12
    assert candidate(costs = [[3, 2, 20], [10, 3, 1], [5, 10, 2], [8, 5, 3], [11, 8, 5], [14, 11, 8], [17, 14, 11]]) == 40
    assert candidate(costs = [[12, 10, 14], [13, 15, 11], [16, 12, 9], [18, 16, 13]]) == 46
    assert candidate(costs = [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 3, 2], [3, 2, 1], [2, 1, 3], [3, 2, 1]]) == 7
    assert candidate(costs = [[10, 15, 10], [10, 3, 18], [12, 18, 9], [8, 12, 15], [7, 10, 12]]) == 40
    assert candidate(costs = [[19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19]]) == 380
    assert candidate(costs = [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 45
    assert candidate(costs = [[9, 9, 9], [8, 8, 8], [7, 7, 7], [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1]]) == 45
    assert candidate(costs = [[5, 10, 15], [10, 5, 15], [15, 10, 5], [5, 10, 15], [10, 5, 15], [15, 10, 5], [5, 10, 15], [10, 5, 15], [15, 10, 5]]) == 45
    assert candidate(costs = [[2, 5, 7], [6, 3, 8], [1, 4, 9], [9, 7, 3], [5, 1, 6], [8, 2, 4]]) == 14
    assert candidate(costs = [[10, 10, 10], [1, 1, 1], [5, 5, 5], [2, 2, 2], [3, 3, 3]]) == 21
    assert candidate(costs = [[20, 18, 16], [14, 12, 10], [8, 6, 4], [2, 0, 1], [9, 7, 5]]) == 37
    assert candidate(costs = [[12, 15, 10], [3, 18, 6], [4, 7, 8], [9, 10, 11], [5, 14, 2]]) == 31
    assert candidate(costs = [[19, 20, 18], [17, 16, 15], [14, 13, 12], [11, 10, 9], [8, 7, 6], [5, 4, 3], [2, 1, 0]]) == 66
    assert candidate(costs = [[17, 20, 16], [14, 13, 16], [15, 16, 14], [16, 14, 15], [15, 14, 16]]) == 72
    assert candidate(costs = [[7, 3, 8], [6, 4, 9], [2, 5, 7], [8, 1, 6], [4, 8, 2], [5, 6, 3], [9, 7, 1], [3, 9, 5], [6, 2, 8], [1, 7, 4]]) == 28
    assert candidate(costs = [[19, 7, 13], [15, 20, 18], [8, 12, 15], [6, 11, 9], [17, 14, 16], [2, 10, 14], [5, 8, 12]]) == 64
    assert candidate(costs = [[15, 25, 35], [20, 10, 30], [25, 20, 5], [30, 15, 10]]) == 45
    assert candidate(costs = [[1, 10, 20], [10, 1, 20], [20, 10, 1], [1, 20, 10], [20, 1, 10], [10, 20, 1], [1, 10, 20], [10, 1, 20], [20, 10, 1]]) == 9
    assert candidate(costs = [[10, 15, 10], [17, 13, 12], [19, 18, 11], [12, 20, 15], [8, 14, 10]]) == 56
    assert candidate(costs = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]) == 370
    assert candidate(costs = [[10, 5, 10], [5, 10, 5], [10, 5, 10], [5, 10, 5], [10, 5, 10]]) == 25
    assert candidate(costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1], [1, 1, 100], [1, 100, 1], [100, 1, 1]]) == 6
    assert candidate(costs = [[1, 5, 3], [2, 4, 6], [3, 7, 9], [4, 8, 10], [5, 9, 11], [6, 10, 12]]) == 31
    assert candidate(costs = [[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]]) == 8
    assert candidate(costs = [[12, 5, 8], [10, 15, 9], [11, 13, 7], [6, 18, 14]]) == 28
    assert candidate(costs = [[19, 18, 17], [16, 15, 14], [13, 12, 11], [10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 20, 19], [18, 17, 16], [15, 14, 13], [12, 11, 10]]) == 101
    assert candidate(costs = [[5, 3, 6], [4, 7, 8], [3, 2, 4], [7, 6, 5], [8, 9, 10], [11, 12, 13]]) == 34
    assert candidate(costs = [[15, 18, 20], [20, 16, 15], [13, 17, 14], [19, 12, 18]]) == 55
    assert candidate(costs = [[20, 1, 10], [10, 1, 10], [10, 10, 1], [1, 1, 20], [2, 1, 1]]) == 14
    assert candidate(costs = [[1, 3, 2], [2, 1, 3], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2]]) == 8
    assert candidate(costs = [[6, 15, 12], [10, 13, 7], [4, 11, 14], [3, 9, 10], [18, 16, 17], [1, 19, 15]]) == 44
    assert candidate(costs = [[1, 20, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 1]]) == 55
    assert candidate(costs = [[18, 9, 3], [16, 2, 4], [10, 12, 1], [3, 1, 11], [6, 9, 12], [15, 13, 5], [2, 14, 7], [8, 15, 6], [17, 11, 8], [14, 7, 9]]) == 46
    assert candidate(costs = [[2, 1, 3], [1, 3, 2], [3, 2, 1], [2, 1, 3], [1, 3, 2], [3, 2, 1]]) == 6
    assert candidate(costs = [[15, 18, 20], [5, 8, 12], [3, 6, 9], [7, 14, 16]]) == 36
    assert candidate(costs = [[11, 12, 13], [13, 11, 12], [12, 13, 11], [11, 13, 12], [13, 12, 11], [12, 11, 13], [13, 11, 12]]) == 78
    assert candidate(costs = [[18, 20, 17], [19, 18, 20], [17, 19, 18], [18, 17, 19], [19, 18, 20], [17, 19, 18], [18, 17, 19]]) == 123
    assert candidate(costs = [[8, 12, 11], [9, 7, 8], [13, 14, 6], [10, 9, 10], [15, 16, 14]]) == 44
    assert candidate(costs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]) == 31
    assert candidate(costs = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 10


