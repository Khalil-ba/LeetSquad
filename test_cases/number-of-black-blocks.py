def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2]]) == [9, 3, 3, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2]]) == [9, 3, 3, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,coordinates = [[2, 2], [3, 3], [1, 1]]) == [6, 8, 2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,coordinates = [[2, 2], [3, 3], [1, 1]]) == [6, 8, 2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,coordinates = [[0, 0], [1, 1], [0, 2]]) == [0, 2, 2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,coordinates = [[0, 0], [1, 1], [0, 2]]) == [0, 2, 2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,coordinates = [[1, 1], [1, 2], [2, 1], [2, 2]]) == [7, 4, 4, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,coordinates = [[1, 1], [1, 2], [2, 1], [2, 2]]) == [7, 4, 4, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[5, 5], [4, 4], [6, 6]]) == [71, 8, 2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[5, 5], [4, 4], [6, 6]]) == [71, 8, 2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,coordinates = [[0, 0]]) == [3, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,coordinates = [[0, 0]]) == [3, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [2, 4, 3, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [2, 4, 3, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3]]) == [71, 5, 4, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3]]) == [71, 5, 4, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[3, 3], [4, 4], [5, 5]]) == [71, 8, 2, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[3, 3], [4, 4], [5, 5]]) == [71, 8, 2, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1]]) == [8, 1, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1]]) == [8, 1, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1]]) == [12, 1, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1]]) == [12, 1, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [4, 5, 3, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [4, 5, 3, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [9, 9], [4, 4]]) == [75, 6, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [9, 9], [4, 4]]) == [75, 6, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,coordinates = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [1, 4, 4, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,coordinates = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [1, 4, 4, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [6, 7, 3, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [6, 7, 3, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,coordinates = []) == [1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,coordinates = []) == [1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [68, 9, 4, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [68, 9, 4, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [25, 9, 7, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [25, 9, 7, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == [9743, 39, 19, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == [9743, 39, 19, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 7,coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 0], [7, 6]]) == [25, 10, 7, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 7,coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 0], [7, 6]]) == [25, 10, 7, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2], [6, 0], [6, 1], [6, 2]]) == [150, 1, 8, 0, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2], [6, 0], [6, 1], [6, 2]]) == [150, 1, 8, 0, 12]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 4], [2, 0], [2, 4], [3, 0], [3, 4], [4, 0], [4, 4], [5, 0], [5, 4], [6, 0], [6, 4], [7, 0], [7, 4], [8, 0], [8, 4], [9, 0], [9, 4]]) == [16, 0, 18, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 4], [2, 0], [2, 4], [3, 0], [3, 4], [4, 0], [4, 4], [5, 0], [5, 4], [6, 0], [6, 4], [7, 0], [7, 4], [8, 0], [8, 4], [9, 0], [9, 4]]) == [16, 0, 18, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50,coordinates = [[25, 25], [24, 24], [26, 26], [24, 25], [25, 24], [25, 26], [26, 25]]) == [2387, 6, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50,coordinates = [[25, 25], [24, 24], [26, 26], [24, 25], [25, 24], [25, 26], [26, 25]]) == [2387, 6, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,coordinates = [[0, 4], [1, 3], [1, 5], [2, 2], [2, 4], [2, 6], [3, 1], [3, 3], [3, 5], [3, 7], [4, 0], [4, 2], [4, 4], [4, 6], [4, 8], [5, 1], [5, 3], [5, 5], [5, 7], [6, 2], [6, 4], [6, 6], [7, 3], [7, 5], [8, 4]]) == [12, 12, 40, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,coordinates = [[0, 4], [1, 3], [1, 5], [2, 2], [2, 4], [2, 6], [3, 1], [3, 3], [3, 5], [3, 7], [4, 0], [4, 2], [4, 4], [4, 6], [4, 8], [5, 1], [5, 3], [5, 5], [5, 7], [6, 2], [6, 4], [6, 6], [7, 3], [7, 5], [8, 4]]) == [12, 12, 40, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,coordinates = [[0, 0], [0, 7], [7, 0], [7, 7], [1, 1], [1, 6], [6, 1], [6, 6], [2, 2], [2, 5], [5, 2], [5, 5], [3, 3], [3, 4], [4, 3], [4, 4]]) == [16, 16, 16, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,coordinates = [[0, 0], [0, 7], [7, 0], [7, 7], [1, 1], [1, 6], [6, 1], [6, 6], [2, 2], [2, 5], [5, 2], [5, 5], [3, 3], [3, 4], [4, 3], [4, 4]]) == [16, 16, 16, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,coordinates = [[0, 1], [1, 0], [2, 1], [3, 0], [4, 1], [5, 0], [6, 1]]) == [30, 6, 6, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,coordinates = [[0, 1], [1, 0], [2, 1], [3, 0], [4, 1], [5, 0], [6, 1]]) == [30, 6, 6, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [12, 6, 6, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [12, 6, 6, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [56, 14, 10, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [56, 14, 10, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == [100, 17, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == [100, 17, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5], [6, 6]]) == [12, 2, 14, 0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5], [6, 6]]) == [12, 2, 14, 0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]) == [65, 1, 6, 0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]) == [65, 1, 6, 0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [50, 50], [50, 51], [50, 52], [50, 53], [51, 50], [51, 51], [51, 52], [51, 53], [52, 50], [52, 51], [52, 52], [52, 53], [53, 50], [53, 51], [53, 52], [53, 53]]) == [9760, 5, 18, 0, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [50, 50], [50, 51], [50, 52], [50, 53], [51, 50], [51, 51], [51, 52], [51, 53], [52, 50], [52, 51], [52, 52], [52, 53], [53, 50], [53, 51], [53, 52], [53, 53]]) == [9760, 5, 18, 0, 18]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,coordinates = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 1], [2, 2], [3, 0], [3, 3], [4, 1], [4, 2], [5, 0], [5, 3], [6, 1], [6, 2], [7, 0], [7, 3]]) == [21, 7, 21, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,coordinates = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 1], [2, 2], [3, 0], [3, 3], [4, 1], [4, 2], [5, 0], [5, 3], [6, 1], [6, 2], [7, 0], [7, 3]]) == [21, 7, 21, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [42, 10, 8, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [42, 10, 8, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 20,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2]]) == [156, 1, 6, 0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 20,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2]]) == [156, 1, 6, 0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 6,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 0], [0, 5], [6, 5], [5, 0], [4, 1], [1, 4], [2, 3], [3, 2]]) == [7, 8, 14, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 6,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 0], [0, 5], [6, 5], [5, 0], [4, 1], [1, 4], [2, 3], [3, 2]]) == [7, 8, 14, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,coordinates = [[4, 4], [3, 3], [3, 5], [5, 3], [5, 5], [2, 2], [2, 6], [6, 2], [6, 6], [1, 1], [1, 7], [7, 1], [7, 7], [0, 0], [0, 8], [8, 0], [8, 8]]) == [24, 24, 16, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,coordinates = [[4, 4], [3, 3], [3, 5], [5, 3], [5, 5], [2, 2], [2, 6], [6, 2], [6, 6], [1, 1], [1, 7], [7, 1], [7, 7], [0, 0], [0, 8], [8, 0], [8, 8]]) == [24, 24, 16, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [56, 16, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [56, 16, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == [28, 0, 4, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == [28, 0, 4, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5]]) == [8, 2, 10, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5]]) == [8, 2, 10, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == [30, 12, 7, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == [30, 12, 7, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,coordinates = [[0, 0], [0, 8], [8, 0], [8, 8], [4, 4], [3, 3], [5, 5], [2, 2], [6, 6]]) == [44, 16, 4, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,coordinates = [[0, 0], [0, 8], [8, 0], [8, 8], [4, 4], [3, 3], [5, 5], [2, 2], [6, 6]]) == [44, 16, 4, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 7], [7, 8]]) == [36, 6, 15, 2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 7], [7, 8]]) == [36, 6, 15, 2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,coordinates = [[10, 10], [10, 11], [11, 10], [11, 11], [20, 20], [21, 20], [20, 21], [21, 21]]) == [9783, 8, 8, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,coordinates = [[10, 10], [10, 11], [11, 10], [11, 11], [20, 20], [21, 20], [20, 21], [21, 21]]) == [9783, 8, 8, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 7,coordinates = [[0, 3], [1, 2], [2, 1], [3, 0], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1]]) == [24, 16, 8, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 7,coordinates = [[0, 3], [1, 2], [2, 1], [3, 0], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1]]) == [24, 16, 8, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,coordinates = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]) == [8, 3, 9, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,coordinates = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]) == [8, 3, 9, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == [8, 3, 2, 3, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == [8, 3, 2, 3, 14]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 7], [6, 0], [6, 7], [3, 3], [3, 4], [4, 3], [4, 4], [2, 2], [2, 5], [5, 2], [5, 5]]) == [17, 16, 8, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 7], [6, 0], [6, 7], [3, 3], [3, 4], [4, 3], [4, 4], [2, 2], [2, 5], [5, 2], [5, 5]]) == [17, 16, 8, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 5], [6, 6]]) == [19, 7, 15, 1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 5], [6, 6]]) == [19, 7, 15, 1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 7,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6]]) == [21, 5, 11, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 7,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6]]) == [21, 5, 11, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]) == [72, 1, 4, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]) == [72, 1, 4, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 6,coordinates = [[0, 0], [0, 5], [1, 1], [1, 4], [2, 2], [2, 3], [3, 3], [3, 4], [4, 1], [4, 5]]) == [2, 9, 7, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 6,coordinates = [[0, 0], [0, 5], [1, 1], [1, 4], [2, 2], [2, 3], [3, 3], [3, 4], [4, 1], [4, 5]]) == [2, 9, 7, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 6,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [14, 7, 5, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 6,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [14, 7, 5, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [0, 7], [7, 0]]) == [28, 14, 7, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [0, 7], [7, 0]]) == [28, 14, 7, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3], [1, 1], [4, 4]]) == [10, 10, 5, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3], [1, 1], [4, 4]]) == [10, 10, 5, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 6,coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == [14, 4, 12, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 6,coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == [14, 4, 12, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [238, 19, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [238, 19, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == [27, 0, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == [27, 0, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 11,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == [81, 19, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 11,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == [81, 19, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == [69, 3, 7, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == [69, 3, 7, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,coordinates = [[0, 1], [1, 2], [2, 0], [3, 1], [3, 2], [4, 0], [4, 1]]) == [0, 7, 3, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,coordinates = [[0, 1], [1, 2], [2, 0], [3, 1], [3, 2], [4, 0], [4, 1]]) == [0, 7, 3, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,coordinates = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5]]) == [23, 16, 3, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,coordinates = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5]]) == [23, 16, 3, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 10,coordinates = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [5, 5], [6, 5], [7, 5], [5, 6], [6, 6], [7, 6]]) == [78, 5, 10, 0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 10,coordinates = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [5, 5], [6, 5], [7, 5], [5, 6], [6, 6], [7, 6]]) == [78, 5, 10, 0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1]]) == [5, 1, 4, 7, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1]]) == [5, 1, 4, 7, 3]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [3, 5], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [5, 7]]) == [18, 5, 9, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [3, 5], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [5, 7]]) == [18, 5, 9, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == [13, 3, 11, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == [13, 3, 11, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,coordinates = [[0, 1], [0, 3], [1, 2], [1, 4], [2, 1], [2, 3], [2, 5], [3, 2], [3, 4], [3, 6], [4, 1], [4, 3], [4, 5], [5, 2], [5, 4], [6, 3]]) == [7, 12, 23, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,coordinates = [[0, 1], [0, 3], [1, 2], [1, 4], [2, 1], [2, 3], [2, 5], [3, 2], [3, 4], [3, 6], [4, 1], [4, 3], [4, 5], [5, 2], [5, 4], [6, 3]]) == [7, 12, 23, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [52, 10, 14, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [52, 10, 14, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 6,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]) == [6, 1, 8, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 6,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]) == [6, 1, 8, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 6], [1, 1], [1, 5], [2, 2], [2, 4], [3, 3], [4, 2], [4, 4], [5, 1], [5, 5]]) == [6, 14, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 6], [1, 1], [1, 5], [2, 2], [2, 4], [3, 3], [4, 2], [4, 4], [5, 1], [5, 5]]) == [6, 14, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [4, 4]]) == [34, 5, 6, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [4, 4]]) == [34, 5, 6, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,coordinates = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 1], [2, 2], [3, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [37, 13, 12, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,coordinates = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 1], [2, 2], [3, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [37, 13, 12, 2, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 5,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2]]) == [9, 3, 3, 0, 1]
    assert candidate(m = 5,n = 5,coordinates = [[2, 2], [3, 3], [1, 1]]) == [6, 8, 2, 0, 0]
    assert candidate(m = 3,n = 3,coordinates = [[0, 0], [1, 1], [0, 2]]) == [0, 2, 2, 0, 0]
    assert candidate(m = 5,n = 5,coordinates = [[1, 1], [1, 2], [2, 1], [2, 2]]) == [7, 4, 4, 0, 1]
    assert candidate(m = 10,n = 10,coordinates = [[5, 5], [4, 4], [6, 6]]) == [71, 8, 2, 0, 0]
    assert candidate(m = 3,n = 3,coordinates = [[0, 0]]) == [3, 1, 0, 0, 0]
    assert candidate(m = 4,n = 4,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [2, 4, 3, 0, 0]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3]]) == [71, 5, 4, 0, 1]
    assert candidate(m = 10,n = 10,coordinates = [[3, 3], [4, 4], [5, 5]]) == [71, 8, 2, 0, 0]
    assert candidate(m = 4,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1]]) == [8, 1, 2, 0, 1]
    assert candidate(m = 5,n = 5,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1]]) == [12, 1, 2, 0, 1]
    assert candidate(m = 4,n = 5,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [4, 5, 3, 0, 0]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [9, 9], [4, 4]]) == [75, 6, 0, 0, 0]
    assert candidate(m = 4,n = 4,coordinates = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [1, 4, 4, 0, 0]
    assert candidate(m = 5,n = 5,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [6, 7, 3, 0, 0]
    assert candidate(m = 2,n = 2,coordinates = []) == [1, 0, 0, 0, 0]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == [68, 9, 4, 0, 0]
    assert candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [25, 9, 7, 0, 1]
    assert candidate(m = 100,n = 100,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == [9743, 39, 19, 0, 0]
    assert candidate(m = 8,n = 7,coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [0, 0], [7, 6]]) == [25, 10, 7, 0, 0]
    assert candidate(m = 20,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2], [6, 0], [6, 1], [6, 2]]) == [150, 1, 8, 0, 12]
    assert candidate(m = 10,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 4], [2, 0], [2, 4], [3, 0], [3, 4], [4, 0], [4, 4], [5, 0], [5, 4], [6, 0], [6, 4], [7, 0], [7, 4], [8, 0], [8, 4], [9, 0], [9, 4]]) == [16, 0, 18, 2, 0]
    assert candidate(m = 50,n = 50,coordinates = [[25, 25], [24, 24], [26, 26], [24, 25], [25, 24], [25, 26], [26, 25]]) == [2387, 6, 4, 2, 2]
    assert candidate(m = 9,n = 9,coordinates = [[0, 4], [1, 3], [1, 5], [2, 2], [2, 4], [2, 6], [3, 1], [3, 3], [3, 5], [3, 7], [4, 0], [4, 2], [4, 4], [4, 6], [4, 8], [5, 1], [5, 3], [5, 5], [5, 7], [6, 2], [6, 4], [6, 6], [7, 3], [7, 5], [8, 4]]) == [12, 12, 40, 0, 0]
    assert candidate(m = 8,n = 8,coordinates = [[0, 0], [0, 7], [7, 0], [7, 7], [1, 1], [1, 6], [6, 1], [6, 6], [2, 2], [2, 5], [5, 2], [5, 5], [3, 3], [3, 4], [4, 3], [4, 4]]) == [16, 16, 16, 0, 1]
    assert candidate(m = 7,n = 8,coordinates = [[0, 1], [1, 0], [2, 1], [3, 0], [4, 1], [5, 0], [6, 1]]) == [30, 6, 6, 0, 0]
    assert candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [12, 6, 6, 0, 1]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [56, 14, 10, 0, 1]
    assert candidate(m = 15,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == [100, 17, 9, 0, 0]
    assert candidate(m = 7,n = 7,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5], [6, 6]]) == [12, 2, 14, 0, 8]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]) == [65, 1, 6, 0, 9]
    assert candidate(m = 100,n = 100,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [50, 50], [50, 51], [50, 52], [50, 53], [51, 50], [51, 51], [51, 52], [51, 53], [52, 50], [52, 51], [52, 52], [52, 53], [53, 50], [53, 51], [53, 52], [53, 53]]) == [9760, 5, 18, 0, 18]
    assert candidate(m = 8,n = 8,coordinates = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 1], [2, 2], [3, 0], [3, 3], [4, 1], [4, 2], [5, 0], [5, 3], [6, 1], [6, 2], [7, 0], [7, 3]]) == [21, 7, 21, 0, 0]
    assert candidate(m = 9,n = 9,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [42, 10, 8, 0, 4]
    assert candidate(m = 10,n = 20,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2]]) == [156, 1, 6, 0, 8]
    assert candidate(m = 7,n = 6,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 0], [0, 5], [6, 5], [5, 0], [4, 1], [1, 4], [2, 3], [3, 2]]) == [7, 8, 14, 0, 1]
    assert candidate(m = 9,n = 9,coordinates = [[4, 4], [3, 3], [3, 5], [5, 3], [5, 5], [2, 2], [2, 6], [6, 2], [6, 6], [1, 1], [1, 7], [7, 1], [7, 7], [0, 0], [0, 8], [8, 0], [8, 8]]) == [24, 24, 16, 0, 0]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [56, 16, 9, 0, 0]
    assert candidate(m = 10,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == [28, 0, 4, 0, 4]
    assert candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5]]) == [8, 2, 10, 0, 5]
    assert candidate(m = 8,n = 8,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == [30, 12, 7, 0, 0]
    assert candidate(m = 9,n = 9,coordinates = [[0, 0], [0, 8], [8, 0], [8, 8], [4, 4], [3, 3], [5, 5], [2, 2], [6, 6]]) == [44, 16, 4, 0, 0]
    assert candidate(m = 9,n = 9,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 7], [7, 8]]) == [36, 6, 15, 2, 5]
    assert candidate(m = 100,n = 100,coordinates = [[10, 10], [10, 11], [11, 10], [11, 11], [20, 20], [21, 20], [20, 21], [21, 21]]) == [9783, 8, 8, 0, 2]
    assert candidate(m = 9,n = 7,coordinates = [[0, 3], [1, 2], [2, 1], [3, 0], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1]]) == [24, 16, 8, 0, 0]
    assert candidate(m = 6,n = 6,coordinates = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]) == [8, 3, 9, 1, 4]
    assert candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == [8, 3, 2, 3, 14]
    assert candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 7], [6, 0], [6, 7], [3, 3], [3, 4], [4, 3], [4, 4], [2, 2], [2, 5], [5, 2], [5, 5]]) == [17, 16, 8, 0, 1]
    assert candidate(m = 8,n = 8,coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6], [6, 5], [6, 6]]) == [19, 7, 15, 1, 7]
    assert candidate(m = 8,n = 7,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6]]) == [21, 5, 11, 0, 5]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]) == [72, 1, 4, 0, 4]
    assert candidate(m = 5,n = 6,coordinates = [[0, 0], [0, 5], [1, 1], [1, 4], [2, 2], [2, 3], [3, 3], [3, 4], [4, 1], [4, 5]]) == [2, 9, 7, 2, 0]
    assert candidate(m = 7,n = 6,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [14, 7, 5, 2, 2]
    assert candidate(m = 8,n = 8,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [0, 7], [7, 0]]) == [28, 14, 7, 0, 0]
    assert candidate(m = 6,n = 6,coordinates = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3], [1, 1], [4, 4]]) == [10, 10, 5, 0, 0]
    assert candidate(m = 8,n = 6,coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == [14, 4, 12, 0, 5]
    assert candidate(m = 15,n = 20,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [238, 19, 9, 0, 0]
    assert candidate(m = 5,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == [27, 0, 9, 0, 0]
    assert candidate(m = 12,n = 11,coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == [81, 19, 10, 0, 0]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == [69, 3, 7, 0, 2]
    assert candidate(m = 5,n = 4,coordinates = [[0, 1], [1, 2], [2, 0], [3, 1], [3, 2], [4, 0], [4, 1]]) == [0, 7, 3, 2, 0]
    assert candidate(m = 7,n = 8,coordinates = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5]]) == [23, 16, 3, 0, 0]
    assert candidate(m = 12,n = 10,coordinates = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [5, 5], [6, 5], [7, 5], [5, 6], [6, 6], [7, 6]]) == [78, 5, 10, 0, 6]
    assert candidate(m = 6,n = 5,coordinates = [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1]]) == [5, 1, 4, 7, 3]
    assert candidate(m = 7,n = 8,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [3, 5], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [5, 7]]) == [18, 5, 9, 4, 6]
    assert candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]) == [13, 3, 11, 0, 3]
    assert candidate(m = 7,n = 8,coordinates = [[0, 1], [0, 3], [1, 2], [1, 4], [2, 1], [2, 3], [2, 5], [3, 2], [3, 4], [3, 6], [4, 1], [4, 3], [4, 5], [5, 2], [5, 4], [6, 3]]) == [7, 12, 23, 0, 0]
    assert candidate(m = 10,n = 10,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [52, 10, 14, 0, 5]
    assert candidate(m = 5,n = 6,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4]]) == [6, 1, 8, 0, 5]
    assert candidate(m = 6,n = 7,coordinates = [[0, 0], [0, 6], [1, 1], [1, 5], [2, 2], [2, 4], [3, 3], [4, 2], [4, 4], [5, 1], [5, 5]]) == [6, 14, 10, 0, 0]
    assert candidate(m = 8,n = 8,coordinates = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 3], [4, 4]]) == [34, 5, 6, 0, 4]
    assert candidate(m = 9,n = 9,coordinates = [[0, 1], [0, 2], [1, 0], [1, 3], [2, 1], [2, 2], [3, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [37, 13, 12, 2, 0]


