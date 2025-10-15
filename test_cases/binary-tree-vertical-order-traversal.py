def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == [[1], [2], [3], [4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == [[1], [2], [3], [4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == [[5], [3], [1, 3], [2], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == [[5], [3], [1, 3], [2], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6], [3, 11, 13, 14], [7], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6], [3, 11, 13, 14], [7], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9])) == [[4, 10, 11], [3, 7, 6], [2, 5, 8, 9], [0], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9])) == [[4, 10, 11], [3, 7, 6], [2, 5, 8, 9], [0], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7])) == [[4], [9], [3, 0, 1], [8], [7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7])) == [[4], [9], [3, 0, 1], [8], [7]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 10, 9, 11, None, 5, None, None, None, None, None, None, None, 6])) == [[4], [2, 5], [1, 10, 9, 6], [3], [11]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 10, 9, 11, None, 5, None, None, None, None, None, None, None, 6])) == [[4], [2, 5], [1, 10, 9, 6], [3], [11]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0])) == [[0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0])) == [[0]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == [[9], [3, 15], [20], [7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == [[9], [3, 15], [20], [7]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == [[1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == [[1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([])) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([])) == []: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, 0, 2, 4, 6, 8, 12, 18, 22, None, None, None, None, None, None, None, 3, 11, 13, None, 14, None, None, None, None, 10, None, None, None, None, None, None, None, None, None, 16, 17, None, None, None, None, 19, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, 24, None, None, None, None, None, 25, None, None, None, None, None, None, None, None, None, None, None, None, 26])) == [[0], [1, 11], [3, 2, 4, 8], [7, 5, 9, 13], [15, 6, 12, 18, 10], [20, 3, 14], [22]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, 0, 2, 4, 6, 8, 12, 18, 22, None, None, None, None, None, None, None, 3, 11, 13, None, 14, None, None, None, None, 10, None, None, None, None, None, None, None, None, None, 16, 17, None, None, None, None, 19, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, 24, None, None, None, None, None, 25, None, None, None, None, None, None, None, None, None, None, None, None, 26])) == [[0], [1, 11], [3, 2, 4, 8], [7, 5, 9, 13], [15, 6, 12, 18, 10], [20, 3, 14], [22]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -5, -3, 9, 1, None, -2, 7, 3, None, -4, None, None, None, None, None, None])) == [[7], [9], [-5, 3], [10, 1], [-3, -4], [-2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -5, -3, 9, 1, None, -2, 7, 3, None, -4, None, None, None, None, None, None])) == [[7], [9], [-5, 3], [10, 1], [-3, -4], [-2]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 8, 21, 7, 11, 18, 24, 6, 9, 12, 17, 20, 23, 5, 8, 10, 13, 16, 19, 22, 25, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2])) == [[10], [6], [7, 13, 16, 22], [8, 9, 12, 20], [15, 11, 18, 19, 25], [21, 17, 23, 5], [24, 4], [8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 8, 21, 7, 11, 18, 24, 6, 9, 12, 17, 20, 23, 5, 8, 10, 13, 16, 19, 22, 25, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2])) == [[10], [6], [7, 13, 16, 22], [8, 9, 12, 20], [15, 11, 18, 19, 25], [21, 17, 23, 5], [24, 4], [8]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 38, None, 4, 6, 8, 11, 13, 17, 19, 22, 24, 26, 28, 30, 31, 33, 36, 39, None, 1, 3, 9, 14, 16, 21, 29, 34, 37, None, None, 3, 14, 18, 20, 25, 27, 31, 35, 38, None, None, 5, 10, 12, 13, 17, 19, 23, 26, 28, 32, 34, 36, 39, None, None, 6, 7, 8, 9, 11, 15, 16, 21, 22, 24, 29, 30, 33, 37, None, None, None, None, 21, 22, None, None, None, None, None, None, None, None, None, None, None, 34, 37, None, None, None, None])) == [[23, 28, 7, 37], [2, 39, 1, 16, 14], [5, 4, 6, 11, 22, 26, 32, 34, 39, 8, 9, 15, 24], [10, 7, 12, 23, 3, 9, 21, 29, 37, 18, 20, 27], [20, 15, 25, 8, 13, 17, 24, 26, 30, 36, 11, 16, 21, 29, 21, 22], [30, 18, 27, 32, 14, 34, 25, 31, 35, 5, 12], [35, 19, 28, 31, 33, 6, 22, 30, 34], [38, 3, 38, 10, 13, 17], [36, 33, 37], [19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 38, None, 4, 6, 8, 11, 13, 17, 19, 22, 24, 26, 28, 30, 31, 33, 36, 39, None, 1, 3, 9, 14, 16, 21, 29, 34, 37, None, None, 3, 14, 18, 20, 25, 27, 31, 35, 38, None, None, 5, 10, 12, 13, 17, 19, 23, 26, 28, 32, 34, 36, 39, None, None, 6, 7, 8, 9, 11, 15, 16, 21, 22, 24, 29, 30, 33, 37, None, None, None, None, 21, 22, None, None, None, None, None, None, None, None, None, None, None, 34, 37, None, None, None, None])) == [[23, 28, 7, 37], [2, 39, 1, 16, 14], [5, 4, 6, 11, 22, 26, 32, 34, 39, 8, 9, 15, 24], [10, 7, 12, 23, 3, 9, 21, 29, 37, 18, 20, 27], [20, 15, 25, 8, 13, 17, 24, 26, 30, 36, 11, 16, 21, 29, 21, 22], [30, 18, 27, 32, 14, 34, 25, 31, 35, 5, 12], [35, 19, 28, 31, 33, 6, 22, 30, 34], [38, 3, 38, 10, 13, 17], [36, 33, 37], [19]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 9, 3, 6, 10, 15, 1, 4, 7, 11, 13, 16, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 12, 14, 17, 18])) == [[1], [3], [5, 4, 7, 13], [8, 6, 10], [9, 11, 16], [15], [2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 9, 3, 6, 10, 15, 1, 4, 7, 11, 13, 16, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 12, 14, 17, 18])) == [[1], [3], [5, 4, 7, 13], [8, 6, 10], [9, 11, 16], [15], [2]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 2, 5, None, 16, 1, 4, 6, 8, None, None, None, None, None, 17])) == [[1], [2], [3, 4, 6], [7, 5, 17], [15, 8], [16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 2, 5, None, 16, 1, 4, 6, 8, None, None, None, None, None, 17])) == [[1], [2], [3, 4, 6], [7, 5, 17], [15, 8], [16]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == [[32], [16], [8, 33, 34, 36, 40], [4, 17, 18, 20, 24], [2, 9, 10, 12, 35, 37, 38], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14, 39], [7, 23, 27, 29, 30], [15], [31]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == [[32], [16], [8, 33, 34, 36, 40], [4, 17, 18, 20, 24], [2, 9, 10, 12, 35, 37, 38], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14, 39], [7, 23, 27, 29, 30], [15], [31]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, 8, None, 9, None, None, 10, None, 11, None, None, None, None, None, None, None, None, None, 12])) == [[9], [1, 11], [2], [3], [5, 4], [6, 8], [7, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, 8, None, 9, None, None, 10, None, 11, None, None, None, None, None, None, None, None, None, 12])) == [[9], [1, 11], [2], [3], [5, 4], [6, 8], [7, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 35, 45, 55, 65, 85, 95, 105, 115, 135, 145, 155, 165, 185, 195, 3, 7, 13, 23, 37, 43, 47, 53, 57, 63, 67, 73, 77, 83, 87, 93, 97, 103, 107, 113, 117, 123, 127, 133, 137, 143, 147, 153, 157, 163, 167, 173, 177, 183, 187, 193, 197])) == [[177], [3], [5, 183, 187, 197], [10, 7, 13, 37, 57, 97], [25, 15, 35, 55, 105, 193], [50, 40, 60, 110, 23, 43, 47, 63, 67, 77, 103, 107, 117, 137], [100, 75, 125, 45, 65, 85, 115, 135, 155], [150, 90, 140, 160, 53, 73, 83, 87, 113, 123, 127, 143, 147, 157], [175, 95, 145, 165, 185], [190, 93, 133, 153, 163, 167], [195], [173]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 35, 45, 55, 65, 85, 95, 105, 115, 135, 145, 155, 165, 185, 195, 3, 7, 13, 23, 37, 43, 47, 53, 57, 63, 67, 73, 77, 83, 87, 93, 97, 103, 107, 113, 117, 123, 127, 133, 137, 143, 147, 153, 157, 163, 167, 173, 177, 183, 187, 193, 197])) == [[177], [3], [5, 183, 187, 197], [10, 7, 13, 37, 57, 97], [25, 15, 35, 55, 105, 193], [50, 40, 60, 110, 23, 43, 47, 63, 67, 77, 103, 107, 117, 137], [100, 75, 125, 45, 65, 85, 115, 135, 155], [150, 90, 140, 160, 53, 73, 83, 87, 113, 123, 127, 143, 147, 157], [175, 95, 145, 165, 185], [190, 93, 133, 153, 163, 167], [195], [173]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 7, 20, 3, 11, 17, 23, 2, 5, 9, 13, 16, 18, 22, 24, 1, 4, 6, 8, 10, 12, 14, 19, 21, 25, 27, 3, 28, 29, 30])) == [[1], [2], [3, 4, 6, 10, 21], [7, 5, 9, 16], [15, 11, 17, 8, 12, 14, 25, 27, 28], [20, 13, 18, 22], [23, 19, 3, 29, 30], [24]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 7, 20, 3, 11, 17, 23, 2, 5, 9, 13, 16, 18, 22, 24, 1, 4, 6, 8, 10, 12, 14, 19, 21, 25, 27, 3, 28, 29, 30])) == [[1], [2], [3, 4, 6, 10, 21], [7, 5, 9, 16], [15, 11, 17, 8, 12, 14, 25, 27, 28], [20, 13, 18, 22], [23, 19, 3, 29, 30], [24]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 12])) == [[12], [1], [3], [5, 6, 11], [10, 7, 13], [15, 14], [18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 12])) == [[12], [1], [3], [5, 6, 11], [10, 7, 13], [15, 14], [18]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, None, None, 25, 35, 55, 65, 75, 5, 15, None, None, None, 22, 28, None, None, 32, 38, 52, 58, None, None, None, 62, 68, 72, 78, None, None, 85, None, 90, None, None, None, None, None, None, None, None, 95])) == [[58], [5], [10], [20, 15], [30, 35, 62, 72], [50, 40, 60, 22, 28, 95], [70, 25, 55, 65, 68, 78, 85], [80, 32, 38], [75, 90], [52]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, None, None, 25, 35, 55, 65, 75, 5, 15, None, None, None, 22, 28, None, None, 32, 38, 52, 58, None, None, None, 62, 68, 72, 78, None, None, 85, None, 90, None, None, None, None, None, None, None, None, 95])) == [[58], [5], [10], [20, 15], [30, 35, 62, 72], [50, 40, 60, 22, 28, 95], [70, 25, 55, 65, 68, 78, 85], [80, 32, 38], [75, 90], [52]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == [[0], [2, 3], [6, 4, 7], [8, 5], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == [[0], [2, 3], [6, 4, 7], [8, 5], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, 12, 13, 14, 15, 16, 17])) == [[3], [4], [5, 7, 12, 14], [8, 6, 10], [9, 13, 15, 16], [11], [17]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, 12, 13, 14, 15, 16, 17])) == [[3], [4], [5, 7, 12, 14], [8, 6, 10], [9, 13, 15, 16], [11], [17]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, None, 12, None, 22, 27, 40, None, 3, 6, 8, 9, 11, 13, 14, 18, 19, 21, 23, 26, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49])) == [[1, 26, 29], [5, 3, 6], [10, 7, 28, 31, 32, 34, 39, 44], [20, 15, 25, 8, 9, 13, 18], [30, 12, 22, 27, 33, 36, 37, 41, 42, 45, 46, 48], [35, 11, 14, 19, 21], [40, 38, 43, 47, 49], [23]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, None, 12, None, 22, 27, 40, None, 3, 6, 8, 9, 11, 13, 14, 18, 19, 21, 23, 26, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49])) == [[1, 26, 29], [5, 3, 6], [10, 7, 28, 31, 32, 34, 39, 44], [20, 15, 25, 8, 9, 13, 18], [30, 12, 22, 27, 33, 36, 37, 41, 42, 45, 46, 48], [35, 11, 14, 19, 21], [40, 38, 43, 47, 49], [23]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == [[1], [2], [4, 3, 5, 9], [8, 6, 10], [12, 7, 11, 13], [14], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == [[1], [2], [4, 3, 5, 9], [8, 6, 10], [12, 7, 11, 13], [14], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45])) == [[5], [10], [15, 12, 18, 28], [25, 20, 30], [35, 22, 32, 38], [40], [45]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45])) == [[5], [10], [15, 12, 18, 28], [25, 20, 30], [35, 22, 32, 38], [40], [45]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10, 11, 12, None, 13, 14, 15])) == [[4], [2], [1, 5, 6, 11], [3, 8, 9], [7, 12, 13, 14], [10], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10, 11, 12, None, 13, 14, 15])) == [[4], [2], [1, 5, 6, 11], [3, 8, 9], [7, 12, 13, 14], [10], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 7, 20, 3, 9, 15, 23, 1, 5, 8, 11, 13, 18, 21, 24, None, 2, 4, 6, None, 10, None, None, None, None, None, 14, 16, None, 17, 19, 22, None, None, 25, None, None, None, None, None, 26])) == [[1, 22], [3, 2, 4], [7, 5, 8, 13, 25], [12, 9, 15, 6, 10, 16], [20, 11, 18, 21], [23, 14, 17], [24, 26], [19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 7, 20, 3, 9, 15, 23, 1, 5, 8, 11, 13, 18, 21, 24, None, 2, 4, 6, None, 10, None, None, None, None, None, 14, 16, None, 17, 19, 22, None, None, 25, None, None, None, None, None, 26])) == [[1, 22], [3, 2, 4], [7, 5, 8, 13, 25], [12, 9, 15, 6, 10, 16], [20, 11, 18, 21], [23, 14, 17], [24, 26], [19]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, 3, 5, None, None, None, None, None, None, None])) == [[0], [2, 3, 5], [6, 4, 7], [8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, 3, 5, None, None, None, None, None, None, None])) == [[0], [2, 3, 5], [6, 4, 7], [8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 38, 1, 3, 6, 8, 11, 13, 17, 19, 22, 26, 28, 31, 33, 37, 39, 40])) == [[1], [2], [5, 3, 6, 11, 22], [10, 7, 12, 23], [20, 15, 25, 8, 13, 17, 26, 28, 33], [30, 18, 27, 32], [35, 19, 31, 37, 39], [38], [40]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 38, 1, 3, 6, 8, 11, 13, 17, 19, 22, 26, 28, 31, 33, 37, 39, 40])) == [[1], [2], [5, 3, 6, 11, 22], [10, 7, 12, 23], [20, 15, 25, 8, 13, 17, 26, 28, 33], [30, 18, 27, 32], [35, 19, 31, 37, 39], [38], [40]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14], [7, 23, 27, 29, 30], [15], [31]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14], [7, 23, 27, 29, 30], [15], [31]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, None, 18, 27, 32, None, 11, 14, 17, 19, 23, 26, 29, 31, 33, 34, 36, 37, 38, 39])) == [[39], [14], [5], [10, 17, 19, 31], [15, 12, 27], [25, 20, 30, 23, 26, 33, 34], [35, 18, 32], [40, 29, 36, 37], [11], [38]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, None, 18, 27, 32, None, 11, 14, 17, 19, 23, 26, 29, 31, 33, 34, 36, 37, 38, 39])) == [[39], [14], [5], [10, 17, 19, 31], [15, 12, 27], [25, 20, 30, 23, 26, 33, 34], [35, 18, 32], [40, 29, 36, 37], [11], [38]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, None, 5, 3])) == [[3], [7], [11], [4, 1], [5, 17], [8], [4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, None, 5, 3])) == [[3], [7], [11], [4, 1], [5, 17], [8], [4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == [[31], [15], [7, 32, 33, 35, 39, 47], [3, 16, 17, 19, 23], [1, 8, 9, 11, 34, 36, 37, 40, 41, 43, 48, 49], [0, 4, 5, 18, 20, 21, 24, 25, 27], [2, 10, 12, 13, 38, 42, 44, 45, 50], [6, 22, 26, 28, 29], [14, 46], [30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == [[31], [15], [7, 32, 33, 35, 39, 47], [3, 16, 17, 19, 23], [1, 8, 9, 11, 34, 36, 37, 40, 41, 43, 48, 49], [0, 4, 5, 18, 20, 21, 24, 25, 27], [2, 10, 12, 13, 38, 42, 44, 45, 50], [6, 22, 26, 28, 29], [14, 46], [30]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, None, 4, 6, 8, 12, 17, 22])) == [[1], [3, 4, 8], [7, 5, 9], [15, 6, 12, 17], [20], [22]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, None, 4, 6, 8, 12, 17, 22])) == [[1], [3, 4, 8], [7, 5, 9], [15, 6, 12, 17], [20], [22]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, None, 3, None, 1, 5, 4, None, 7, 2, None, None, 9, 6, 10])) == [[2], [2, 5], [3, 3], [3, 4], [1, 9, 6], [7], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, None, 3, None, 1, 5, 4, None, 7, 2, None, None, 9, 6, 10])) == [[2], [2, 5], [3, 3], [3, 4], [1, 9, 6], [7], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, 8, 9])) == [[1], [2], [3], [5, 4], [6, 8], [7], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, 8, 9])) == [[1], [2], [3], [5, 4], [6, 8], [7], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5, None, None, 6, None, None, None, None, None, None, None, None, 10, 11])) == [[4], [9, 5], [3, 0, 1], [8, 2], [7], [6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5, None, None, 6, None, None, None, None, None, None, None, None, 10, 11])) == [[4], [9, 5], [3, 0, 1], [8, 2], [7], [6]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 7, 11, 13, 17, 19, 23])) == [[1], [3], [6, 5, 7, 13], [12, 9, 15], [18, 11, 17, 19], [21], [23]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 7, 11, 13, 17, 19, 23])) == [[1], [3], [6, 5, 7, 13], [12, 9, 15], [18, 11, 17, 19], [21], [23]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 17, 20, 16, None, None, None, None, None, None, None, None, None, None, None, None, 19])) == [[16], [1], [3], [5, 6], [10, 7], [15, 8, 17], [18], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 17, 20, 16, None, None, None, None, None, None, None, None, None, None, None, None, 19])) == [[16], [1], [3], [5, 6], [10, 7], [15, 8, 17], [18], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, None, None, None, None, 12, None, None, None, None, 13, None, 14, None, None, None, None, 15, None, None, None, None, None, None, None, None, 16])) == [[3], [4], [5, 7], [8, 6, 10, 13], [9, 12], [11, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, None, None, None, None, 12, None, None, None, None, 13, None, 14, None, None, None, None, 15, None, None, None, None, None, None, None, None, 16])) == [[3], [4], [5, 7], [8, 6, 10, 13], [9, 12], [11, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14], [7, 23, 27, 29, 30], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14], [7, 23, 27, 29, 30], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 7, 23, 3, 11, 19, 29, 1, 5, 9, 13, 17, 21, 25, 27, 31, 33, 35, 37])) == [[31], [1], [3, 33, 35], [7, 5, 9, 17], [15, 11, 19, 37], [23, 13, 21, 25], [29], [27]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 7, 23, 3, 11, 19, 29, 1, 5, 9, 13, 17, 21, 25, 27, 31, 33, 35, 37])) == [[31], [1], [3, 33, 35], [7, 5, 9, 17], [15, 11, 19, 37], [23, 13, 21, 25], [29], [27]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, 20, None, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, 22])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6, 16, 17], [3, 11, 13, 14, 19], [7, 18], [15, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, 20, None, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, 22])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6, 16, 17], [3, 11, 13, 14, 19], [7, 18], [15, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -5, 15, -8, -3, 12, 20, -10, 1, None, -4, 11, 16, None, None, 13, 14])) == [[13], [-10], [-8, 14], [-5, 1, 11], [10, -3, 12], [15, -4, 16], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -5, 15, -8, -3, 12, 20, -10, 1, None, -4, 11, 16, None, None, 13, 14])) == [[13], [-10], [-8, 14], [-5, 1, 11], [10, -3, 12], [15, -4, 16], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, -2, 2, 3.5, None, None, None, None, None, None, None])) == [[-2], [1], [3, 2, 3.5], [5, 4, 7], [8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, -2, 2, 3.5, None, None, None, None, None, None, None])) == [[-2], [1], [3, 2, 3.5], [5, 4, 7], [8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37])) == [[2], [5], [10, 7, 12, 22], [20, 15, 25], [30, 18, 27, 32], [35], [37]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37])) == [[2], [5], [10, 7, 12, 22], [20, 15, 25], [30, 18, 27, 32], [35], [37]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25], [3, 11, 13, 14], [7, 23], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25], [3, 11, 13, 14], [7, 23], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == [[32], [16], [8, 33, 34, 36, 40, 48], [4, 17, 18, 20, 24], [2, 9, 10, 12, 35, 37, 38, 41, 42, 44, 49, 50], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14, 39, 43, 45, 46], [7, 23, 27, 29, 30], [15, 47], [31]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == [[32], [16], [8, 33, 34, 36, 40, 48], [4, 17, 18, 20, 24], [2, 9, 10, 12, 35, 37, 38, 41, 42, 44, 49, 50], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14, 39, 43, 45, 46], [7, 23, 27, 29, 30], [15, 47], [31]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, None, None, 17, None, None, None, 18, None, None, None, 19, None, None, None, None, None, None, 20, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, None, None, 25])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6, 16, 17], [3, 11, 13, 14, 19], [7, 18], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, None, None, 17, None, None, None, 18, None, None, None, 19, None, None, None, None, None, None, 20, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, None, None, 25])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6, 16, 17], [3, 11, 13, 14, 19], [7, 18], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 12, 4, 7, 10, 14, 2, None, 6, None, 9, 11, 13, None, 15, None, None, None, None, None, None, None, 16])) == [[15], [2], [4], [5, 6, 9], [8, 7, 10, 16], [12, 11, 13], [14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 12, 4, 7, 10, 14, 2, None, 6, None, 9, 11, 13, None, 15, None, None, None, None, None, None, None, 16])) == [[15], [2], [4], [5, 6, 9], [8, 7, 10, 16], [12, 11, 13], [14]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 6, 1, 3, None, 8, 0, 4, 9, None, None, None, 12])) == [[12], [0], [1], [2, 4, 9], [5, 3], [6], [8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 6, 1, 3, None, 8, 0, 4, 9, None, None, None, 12])) == [[12], [0], [1], [2, 4, 9], [5, 3], [6], [8]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, None, 8, 9])) == [[8], [1], [2, 9], [3], [5, 4], [6], [7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, None, 8, 9])) == [[8], [1], [2, 9], [3], [5, 4], [6], [7]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, 7, 12, 20, None, 6, 8, None, None, 18, None, None, None, None, 16, 17, None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 21, None, None, None, None, 22])) == [[5, 8], [10, 7, 12], [15, 6], [20, 16], [18], [17]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, 7, 12, 20, None, 6, 8, None, None, 18, None, None, None, None, 16, 17, None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 21, None, None, None, None, 22])) == [[5, 8], [10, 7, 12], [15, 6], [20, 16], [18], [17]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20])) == [[1], [3], [5, 4, 6, 11], [10, 7, 12], [15, 8, 13, 17], [18], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20])) == [[1], [3], [5, 4, 6, 11], [10, 7, 12], [15, 8, 13, 17], [18], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, None, 12])) == [[1], [3, 12], [5, 6], [10, 7], [15, 9], [18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, None, 12])) == [[1], [3, 12], [5, 6], [10, 7], [15, 9], [18]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19])) == [[13], [3, 8], [7, 9, 14, 16, 18], [15, 10, 11], [20, 17, 19], [12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19])) == [[13], [3, 8], [7, 9, 14, 16, 18], [15, 10, 11], [20, 17, 19], [12]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, 9, 10, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 14, 16, 17, 19, 21, 22, 23, 24])) == [[1], [3], [5, 4, 6, 11, 10], [10, 7, 12, 2], [15, 8, 13, 18], [20], [25], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, 9, 10, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 14, 16, 17, 19, 21, 22, 23, 24])) == [[1], [3], [5, 4, 6, 11, 10], [10, 7, 12, 2], [15, 8, 13, 18], [20], [25], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 13, 18, 25])) == [[1], [3], [5, 6, 11], [10, 7, 12], [15, 8, 13, 18], [20], [25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 13, 18, 25])) == [[1], [3], [5, 6, 11], [10, 7, 12], [15, 8, 13, 18], [20], [25]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7, -6, 5, 2, None, None, None, None, 8, 10, None, None, None, None, None, None])) == [[10], [-6], [4], [9, 5, 2], [3, 0, 1], [8], [7], [8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7, -6, 5, 2, None, None, None, None, 8, 10, None, None, None, None, None, None])) == [[10], [-6], [4], [9, 5, 2], [3, 0, 1], [8], [7], [8]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45, 3, 7, 11, 14, 16, 19, 21, 23, 27, 29, 31, 33, 37, 39, 43, 47, None, 4, 6, 8, 9, 13, 15, 17, 20, 24, 26, 30, 34, 36, 40, 42, 46, 50, 2, 1, 5, 10, 18, 25, 35, 45, None, None, None, None, None, None, None, None, 50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1])) == [[3, 50, 46, 37, 21], [5, 4, 6, 9, 20, 46], [10, 7, 11, 16, 27, 49, 48, 44, 43, 41, 36, 35, 33, 29, 20, 19, 17, 13, 4], [15, 12, 18, 28, 8, 13, 15, 24, 26, 34, 50, 2, 5, 35], [25, 20, 30, 14, 19, 21, 29, 31, 37, 47, 42, 40, 39, 34, 32, 31, 28, 27, 25, 18, 16, 15, 12, 11, 9, 3, 2], [35, 22, 32, 38, 17, 30, 36, 40, 1, 10, 18, 45], [40, 23, 33, 39, 43, 38, 30, 26, 24, 23, 14, 10, 8, 7, 1], [45, 42, 25], [47, 22, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45, 3, 7, 11, 14, 16, 19, 21, 23, 27, 29, 31, 33, 37, 39, 43, 47, None, 4, 6, 8, 9, 13, 15, 17, 20, 24, 26, 30, 34, 36, 40, 42, 46, 50, 2, 1, 5, 10, 18, 25, 35, 45, None, None, None, None, None, None, None, None, 50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1])) == [[3, 50, 46, 37, 21], [5, 4, 6, 9, 20, 46], [10, 7, 11, 16, 27, 49, 48, 44, 43, 41, 36, 35, 33, 29, 20, 19, 17, 13, 4], [15, 12, 18, 28, 8, 13, 15, 24, 26, 34, 50, 2, 5, 35], [25, 20, 30, 14, 19, 21, 29, 31, 37, 47, 42, 40, 39, 34, 32, 31, 28, 27, 25, 18, 16, 15, 12, 11, 9, 3, 2], [35, 22, 32, 38, 17, 30, 36, 40, 1, 10, 18, 45], [40, 23, 33, 39, 43, 38, 30, 26, 24, 23, 14, 10, 8, 7, 1], [45, 42, 25], [47, 22, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, None, 16, None, None, None, 13, None, None, None, 14])) == [[16], [9, 12], [3, 15], [20], [7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, None, 16, None, None, None, 13, None, None, None, 14])) == [[16], [9, 12], [3, 15], [20], [7]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 13, None, 3, 7, 14, 1, 4, 6, 8, 10, 15, None, None, 9, 11, None, 12, 16, 17])) == [[2, 1, 6], [5, 3, 7, 9, 12, 16], [13, 4, 8, 10], [14, 11, 17], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 13, None, 3, 7, 14, 1, 4, 6, 8, 10, 15, None, None, 9, 11, None, 12, 16, 17])) == [[2, 1, 6], [5, 3, 7, 9, 12, 16], [13, 4, 8, 10], [14, 11, 17], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 6, None, 3, None, None, 2, 4])) == [[1, 2], [5, 3], [6, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 6, None, 3, None, None, 2, 4])) == [[1, 2], [5, 3], [6, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, 16, 18, 21, 23, None, 24, 26, 35, None, None, None, None, None, None, None, None, 32])) == [[26], [5], [10, 35], [15, 12, 16, 21], [20, 17, 22, 32], [25, 18, 23], [30], [24]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, 16, 18, 21, 23, None, 24, 26, 35, None, None, None, None, None, None, None, None, 32])) == [[26], [5], [10, 35], [15, 12, 16, 21], [20, 17, 22, 32], [25, 18, 23], [30], [24]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])) == [[1], [2], [3], [5, 4], [6, 7], [8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])) == [[1], [2], [3], [5, 4], [6, 7], [8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 13, 17, None, None, 12, 14, 16, None, None, None, None, None, 19])) == [[1, 19], [3, 12], [5, 6], [10, 7, 14, 16], [15, 8, 13], [18], [17]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 13, 17, None, None, 12, 14, 16, None, None, None, None, None, 19])) == [[1, 19], [3, 12], [5, 6], [10, 7, 14, 16], [15, 8, 13], [18], [17]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 185, 5, 15, 28, 45, 55, 65, 70, 80, 90, 105, 115, 130, 135, 145, 155, 165, 170, 180, 190, 195, 200])) == [[170], [5], [10, 180, 190, 200], [25, 15, 28, 55, 90], [50, 35, 60, 110, 195], [100, 75, 125, 45, 65, 70, 105, 115, 135], [150, 85, 140, 160], [175, 80, 130, 145, 155], [185], [165]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 185, 5, 15, 28, 45, 55, 65, 70, 80, 90, 105, 115, 130, 135, 145, 155, 165, 170, 180, 190, 195, 200])) == [[170], [5], [10, 180, 190, 200], [25, 15, 28, 55, 90], [50, 35, 60, 110, 195], [100, 75, 125, 45, 65, 70, 105, 115, 135], [150, 85, 140, 160], [175, 80, 130, 145, 155], [185], [165]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 30, 10, 25, 27, 35, 5, 15, None, None, 26, 33, 37, 40, None, 6, 9, 12, 18, None, None, None, None, None, None, 29, None, 31, None, 36, None, None, None, None, None, None, None, None])) == [[5], [10, 6, 9, 18], [20, 15, 26, 31, 36], [50, 25, 27, 12], [30, 33, 37], [35], [40], [29]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 30, 10, 25, 27, 35, 5, 15, None, None, 26, 33, 37, 40, None, 6, 9, 12, 18, None, None, None, None, None, None, 29, None, 31, None, 36, None, None, None, None, None, None, None, None])) == [[5], [10, 6, 9, 18], [20, 15, 26, 31, 36], [50, 25, 27, 12], [30, 33, 37], [35], [40], [29]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, 2, None, 4, 8, 13, 18, None, 10, 11, 12, 14, 16, 17, 19])) == [[1, 10, 16], [3, 2, 8], [7, 5, 9, 11, 12, 17, 19], [15, 4, 13, 18], [20, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, 2, None, 4, 8, 13, 18, None, 10, 11, 12, 14, 16, 17, 19])) == [[1, 10, 16], [3, 2, 8], [7, 5, 9, 11, 12, 17, 19], [15, 4, 13, 18], [20, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 3, 9, 15, 21, 28, 34, 40, 46, 53, 60, 65, 72, 79, 84, 89, 96])) == [[3], [6], [12, 9, 15, 28, 53], [25, 18, 31, 56], [50, 37, 62, 21, 34, 40, 60, 65, 79], [75, 43, 68, 81], [87, 46, 72, 84, 89], [93], [96]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 3, 9, 15, 21, 28, 34, 40, 46, 53, 60, 65, 72, 79, 84, 89, 96])) == [[3], [6], [12, 9, 15, 28, 53], [25, 18, 31, 56], [50, 37, 62, 21, 34, 40, 60, 65, 79], [75, 43, 68, 81], [87, 46, 72, 84, 89], [93], [96]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -10, 10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80, -90, 90, -100, 100])) == [[-80], [-40], [-20, 80, -90, -100], [-10, 40, -50, -60], [1, 20, -30, 90, 100], [10, 50, 60, -70], [30], [70]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -10, 10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80, -90, 90, -100, 100])) == [[-80], [-40], [-20, 80, -90, -100], [-10, 40, -50, -60], [1, 20, -30, 90, 100], [10, 50, 60, -70], [30], [70]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 12, 4, 7, 10, 15, 3, 6, 9, 11, 13, 16, 18, 20])) == [[3], [4], [5, 6, 9, 13], [8, 7, 10], [12, 11, 16, 18], [15], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 12, 4, 7, 10, 15, 3, 6, 9, 11, 13, 16, 18, 20])) == [[3], [4], [5, 6, 9, 13], [8, 7, 10], [12, 11, 16, 18], [15], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 19, 21, 24, None, 7, None, None, None, None, None, None, 11, None, None, 23, None, None, None, None, None, 6, None, None, 8, None, None, 13, None, 14, None, 16, None, 17, None, None, None, None, None, None, None, 9])) == [[5], [10, 11], [15, 12, 21], [20, 18, 22], [25, 19, 24], [30, 23], [7, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 19, 21, 24, None, 7, None, None, None, None, None, None, 11, None, None, 23, None, None, None, None, None, 6, None, None, 8, None, None, 13, None, 14, None, 16, None, 17, None, None, None, None, None, None, None, 9])) == [[5], [10, 11], [15, 12, 21], [20, 18, 22], [25, 19, 24], [30, 23], [7, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 9, 1, 5, 8, 10, 0, 2, 4, 6, None, 9])) == [[0], [1], [3, 2, 4], [7, 5, 8], [9, 6, 9], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 9, 1, 5, 8, 10, 0, 2, 4, 6, None, 9])) == [[0], [1], [3, 2, 4], [7, 5, 8], [9, 6, 9], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 16, 20, None, None, None, None, None, 19])) == [[1], [3], [5, 6], [10, 7], [15, 8, 16], [18, 19], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 16, 20, None, None, None, None, None, 19])) == [[1], [3], [5, 6], [10, 7], [15, 8, 16], [18, 19], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 9, 4, 7, 8, 10, 3, None, 6, None, None, 9, None, None, 11, None, 12])) == [[11], [3], [4, 12], [5, 6], [8, 7, 8], [9, 9], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 9, 4, 7, 8, 10, 3, None, 6, None, None, 9, None, None, 11, None, 12])) == [[11], [3], [4, 12], [5, 6], [8, 7, 8], [9, 9], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37, 0, 4, 8, 14, 16, 24, 26, 31, 34, 36, 39, 41, 43])) == [[0], [2], [5, 4, 8, 16, 34], [10, 7, 12, 22], [20, 15, 25, 14, 24, 26, 36, 39, 43], [30, 18, 27, 32], [35, 31, 41], [37]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37, 0, 4, 8, 14, 16, 24, 26, 31, 34, 36, 39, 41, 43])) == [[0], [2], [5, 4, 8, 16, 34], [10, 7, 12, 22], [20, 15, 25, 14, 24, 26, 36, 39, 43], [30, 18, 27, 32], [35, 31, 41], [37]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100])) == [[-80], [-40], [-20, -90, -100], [-10, -50, -60], [-30], [-70]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100])) == [[-80], [-40], [-20, -90, -100], [-10, -50, -60], [-30], [-70]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37, 1, 3, 6, 8, 11, 13, 17, 19, 21, 23, 26, 28, 31, 33, 36, 38, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9])) == [[1], [2, 4], [5, 3, 6, 11, 21], [10, 7, 12, 22], [20, 15, 25, 8, 13, 17, 23, 26, 31], [30, 18, 27, 32], [35, 19, 28, 33, 36], [37], [38]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37, 1, 3, 6, 8, 11, 13, 17, 19, 21, 23, 26, 28, 31, 33, 36, 38, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9])) == [[1], [2, 4], [5, 3, 6, 11, 21], [10, 7, 12, 22], [20, 15, 25, 8, 13, 17, 23, 26, 31], [30, 18, 27, 32], [35, 19, 28, 33, 36], [37], [38]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 6, 8, 5, 7, 7, 9, 4, None, None, None, None, 6, 8, 10, None, None, None, None, None, None, None, None, None, None, 5, 9, 11])) == [[4], [5], [6], [7, 7, 7], [8, 6, 8], [9], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 6, 8, 5, 7, 7, 9, 4, None, None, None, None, 6, 8, 10, None, None, None, None, None, None, None, None, None, None, 5, 9, 11])) == [[4], [5], [6], [7, 7, 7], [8, 6, 8], [9], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90, 1, 7, 12, 18, 28, 38, 48, 52, 58, 62, 68, 78, 82, 88, 92, 98, None, 6, 11, 13, 17, 21, 27, 32, 37, 42, 47, 51, 54, 57, 61, 64, 67, 72, 77, 81, 84, 87, 91, 95, 99, None, None, None, None, None, None, None, None, None, None, None, None, 14, 16, 19, 22, 26, 31, 36, 41, 46, 50, 53, 56, 60, 63, 66, 71, 76, 80, 83, 86, 90, 94, 98, None, 9, 11, 18, 25, 34, 43, 52, 61, 70, 79, 88, 97, None, 8, 20, 29, 39, 49, 59, 69, 78, 87, 96, None, None, None, None, None, None, 3, 24, 38, 48, 58, 68, 77, 86, 95, None, None, None, None, None, None, 2, 23, 37, 47, 57, 67, 76, 85, 94, None, None, None, None, None, None, None, 21, 36, 46, 56, 66, 75, 84, 93, None, None, None, None, None, None, None, None, 22, 35, 45, 55, 65, 74, 83, 92, None, None, None, None, None, None, None, None, None, 26, 34, 44, 54, 64, 73, 82, 91, None, None, None, None, None, None, None, None, None, None, 27, 33, 43, 53, 63, 72, 81, 90, None, None, None, None, None, None, None, None, None, None, None, 28, 32, 42, 52, 62, 71, 80, 89, None, None, None, None, None, None, None, None, None, None, None, None, 30, 31, 41, 51, 61, 70, 79, 88, None, None, None, None, None, None, None, None, None, None, None, None, None, 39, 40, 49, 59, 69, 78, 87, 96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 50, 60, 70, 80, 90])) == [[87, 95, 93], [1, 16, 50, 11, 69], [5, 6, 11, 17, 37, 67, 96, 3, 23, 92, 64, 50, 90], [10, 7, 12, 28, 58, 19, 22, 31, 53, 56, 63, 80, 18, 25, 43, 79, 49, 27, 43, 81, 28, 32, 52, 89, 78], [25, 15, 30, 55, 13, 21, 27, 42, 47, 54, 72, 77, 84, 99, 69, 24, 38, 58, 37, 47, 67, 36, 22, 35, 55, 73, 82, 60, 70], [50, 35, 60, 18, 38, 48, 62, 68, 82, 14, 26, 36, 41, 60, 66, 71, 83, 86, 94, 34, 52, 61, 88, 97, 8, 59, 33, 53, 63, 90, 42, 62, 71, 31, 39, 87], [75, 40, 65, 80, 32, 51, 57, 61, 81, 87, 91, 78, 48, 68, 77, 2, 57, 76, 85, 46, 56, 45, 65, 74, 26, 91, 80], [85, 52, 78, 88, 92, 46, 76, 90, 98, 70, 20, 29, 72, 80, 30, 41, 51, 70, 40, 49, 96], [90, 64, 95, 86, 94, 21, 66, 75, 83, 34, 44], [98, 9, 39, 61, 79, 88, 59], [84, 54]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90, 1, 7, 12, 18, 28, 38, 48, 52, 58, 62, 68, 78, 82, 88, 92, 98, None, 6, 11, 13, 17, 21, 27, 32, 37, 42, 47, 51, 54, 57, 61, 64, 67, 72, 77, 81, 84, 87, 91, 95, 99, None, None, None, None, None, None, None, None, None, None, None, None, 14, 16, 19, 22, 26, 31, 36, 41, 46, 50, 53, 56, 60, 63, 66, 71, 76, 80, 83, 86, 90, 94, 98, None, 9, 11, 18, 25, 34, 43, 52, 61, 70, 79, 88, 97, None, 8, 20, 29, 39, 49, 59, 69, 78, 87, 96, None, None, None, None, None, None, 3, 24, 38, 48, 58, 68, 77, 86, 95, None, None, None, None, None, None, 2, 23, 37, 47, 57, 67, 76, 85, 94, None, None, None, None, None, None, None, 21, 36, 46, 56, 66, 75, 84, 93, None, None, None, None, None, None, None, None, 22, 35, 45, 55, 65, 74, 83, 92, None, None, None, None, None, None, None, None, None, 26, 34, 44, 54, 64, 73, 82, 91, None, None, None, None, None, None, None, None, None, None, 27, 33, 43, 53, 63, 72, 81, 90, None, None, None, None, None, None, None, None, None, None, None, 28, 32, 42, 52, 62, 71, 80, 89, None, None, None, None, None, None, None, None, None, None, None, None, 30, 31, 41, 51, 61, 70, 79, 88, None, None, None, None, None, None, None, None, None, None, None, None, None, 39, 40, 49, 59, 69, 78, 87, 96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 50, 60, 70, 80, 90])) == [[87, 95, 93], [1, 16, 50, 11, 69], [5, 6, 11, 17, 37, 67, 96, 3, 23, 92, 64, 50, 90], [10, 7, 12, 28, 58, 19, 22, 31, 53, 56, 63, 80, 18, 25, 43, 79, 49, 27, 43, 81, 28, 32, 52, 89, 78], [25, 15, 30, 55, 13, 21, 27, 42, 47, 54, 72, 77, 84, 99, 69, 24, 38, 58, 37, 47, 67, 36, 22, 35, 55, 73, 82, 60, 70], [50, 35, 60, 18, 38, 48, 62, 68, 82, 14, 26, 36, 41, 60, 66, 71, 83, 86, 94, 34, 52, 61, 88, 97, 8, 59, 33, 53, 63, 90, 42, 62, 71, 31, 39, 87], [75, 40, 65, 80, 32, 51, 57, 61, 81, 87, 91, 78, 48, 68, 77, 2, 57, 76, 85, 46, 56, 45, 65, 74, 26, 91, 80], [85, 52, 78, 88, 92, 46, 76, 90, 98, 70, 20, 29, 72, 80, 30, 41, 51, 70, 40, 49, 96], [90, 64, 95, 86, 94, 21, 66, 75, 83, 34, 44], [98, 9, 39, 61, 79, 88, 59], [84, 54]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -3, 9, -10, None, 5, 10, None, -1, None, 3, 8, 15, -4, -2, 7, 12, None, None, None, None, None, None, None, None, -6])) == [[-10, -4], [-3, -1, -6], [0, 5, -2, 7], [9, 3, 8], [10, 12], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -3, 9, -10, None, 5, 10, None, -1, None, 3, 8, 15, -4, -2, 7, 12, None, None, None, None, None, None, None, None, -6])) == [[-10, -4], [-3, -1, -6], [0, 5, -2, 7], [9, 3, 8], [10, 12], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8])) == [[1], [2], [3], [5, 4], [6], [7], [8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8])) == [[1], [2], [3], [5, 4], [6], [7], [8]]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == [[1], [2], [3], [4], [5]]
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == [[5], [3], [1, 3], [2], [9]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6], [3, 11, 13, 14], [7], [15]]
    assert candidate(root = tree_node([0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9])) == [[4, 10, 11], [3, 7, 6], [2, 5, 8, 9], [0], [1]]
    assert candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7])) == [[4], [9], [3, 0, 1], [8], [7]]
    assert candidate(root = tree_node([1, 2, 3, 4, 10, 9, 11, None, 5, None, None, None, None, None, None, None, 6])) == [[4], [2, 5], [1, 10, 9, 6], [3], [11]]
    assert candidate(root = tree_node([0])) == [[0]]
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == [[9], [3, 15], [20], [7]]
    assert candidate(root = tree_node([1])) == [[1]]
    assert candidate(root = tree_node([])) == []
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, 0, 2, 4, 6, 8, 12, 18, 22, None, None, None, None, None, None, None, 3, 11, 13, None, 14, None, None, None, None, 10, None, None, None, None, None, None, None, None, None, 16, 17, None, None, None, None, 19, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, 24, None, None, None, None, None, 25, None, None, None, None, None, None, None, None, None, None, None, None, 26])) == [[0], [1, 11], [3, 2, 4, 8], [7, 5, 9, 13], [15, 6, 12, 18, 10], [20, 3, 14], [22]]
    assert candidate(root = tree_node([10, -5, -3, 9, 1, None, -2, 7, 3, None, -4, None, None, None, None, None, None])) == [[7], [9], [-5, 3], [10, 1], [-3, -4], [-2]]
    assert candidate(root = tree_node([15, 8, 21, 7, 11, 18, 24, 6, 9, 12, 17, 20, 23, 5, 8, 10, 13, 16, 19, 22, 25, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2])) == [[10], [6], [7, 13, 16, 22], [8, 9, 12, 20], [15, 11, 18, 19, 25], [21, 17, 23, 5], [24, 4], [8]]
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 38, None, 4, 6, 8, 11, 13, 17, 19, 22, 24, 26, 28, 30, 31, 33, 36, 39, None, 1, 3, 9, 14, 16, 21, 29, 34, 37, None, None, 3, 14, 18, 20, 25, 27, 31, 35, 38, None, None, 5, 10, 12, 13, 17, 19, 23, 26, 28, 32, 34, 36, 39, None, None, 6, 7, 8, 9, 11, 15, 16, 21, 22, 24, 29, 30, 33, 37, None, None, None, None, 21, 22, None, None, None, None, None, None, None, None, None, None, None, 34, 37, None, None, None, None])) == [[23, 28, 7, 37], [2, 39, 1, 16, 14], [5, 4, 6, 11, 22, 26, 32, 34, 39, 8, 9, 15, 24], [10, 7, 12, 23, 3, 9, 21, 29, 37, 18, 20, 27], [20, 15, 25, 8, 13, 17, 24, 26, 30, 36, 11, 16, 21, 29, 21, 22], [30, 18, 27, 32, 14, 34, 25, 31, 35, 5, 12], [35, 19, 28, 31, 33, 6, 22, 30, 34], [38, 3, 38, 10, 13, 17], [36, 33, 37], [19]]
    assert candidate(root = tree_node([8, 5, 9, 3, 6, 10, 15, 1, 4, 7, 11, 13, 16, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 12, 14, 17, 18])) == [[1], [3], [5, 4, 7, 13], [8, 6, 10], [9, 11, 16], [15], [2]]
    assert candidate(root = tree_node([7, 3, 15, 2, 5, None, 16, 1, 4, 6, 8, None, None, None, None, None, 17])) == [[1], [2], [3, 4, 6], [7, 5, 17], [15, 8], [16]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == [[32], [16], [8, 33, 34, 36, 40], [4, 17, 18, 20, 24], [2, 9, 10, 12, 35, 37, 38], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14, 39], [7, 23, 27, 29, 30], [15], [31]]
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, 8, None, 9, None, None, 10, None, 11, None, None, None, None, None, None, None, None, None, 12])) == [[9], [1, 11], [2], [3], [5, 4], [6, 8], [7, 10]]
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 35, 45, 55, 65, 85, 95, 105, 115, 135, 145, 155, 165, 185, 195, 3, 7, 13, 23, 37, 43, 47, 53, 57, 63, 67, 73, 77, 83, 87, 93, 97, 103, 107, 113, 117, 123, 127, 133, 137, 143, 147, 153, 157, 163, 167, 173, 177, 183, 187, 193, 197])) == [[177], [3], [5, 183, 187, 197], [10, 7, 13, 37, 57, 97], [25, 15, 35, 55, 105, 193], [50, 40, 60, 110, 23, 43, 47, 63, 67, 77, 103, 107, 117, 137], [100, 75, 125, 45, 65, 85, 115, 135, 155], [150, 90, 140, 160, 53, 73, 83, 87, 113, 123, 127, 143, 147, 157], [175, 95, 145, 165, 185], [190, 93, 133, 153, 163, 167], [195], [173]]
    assert candidate(root = tree_node([15, 7, 20, 3, 11, 17, 23, 2, 5, 9, 13, 16, 18, 22, 24, 1, 4, 6, 8, 10, 12, 14, 19, 21, 25, 27, 3, 28, 29, 30])) == [[1], [2], [3, 4, 6, 10, 21], [7, 5, 9, 16], [15, 11, 17, 8, 12, 14, 25, 27, 28], [20, 13, 18, 22], [23, 19, 3, 29, 30], [24]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, None, None, 12])) == [[12], [1], [3], [5, 6, 11], [10, 7, 13], [15, 14], [18]]
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, None, None, 25, 35, 55, 65, 75, 5, 15, None, None, None, 22, 28, None, None, 32, 38, 52, 58, None, None, None, 62, 68, 72, 78, None, None, 85, None, 90, None, None, None, None, None, None, None, None, 95])) == [[58], [5], [10], [20, 15], [30, 35, 62, 72], [50, 40, 60, 22, 28, 95], [70, 25, 55, 65, 68, 78, 85], [80, 32, 38], [75, 90], [52]]
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == [[0], [2, 3], [6, 4, 7], [8, 5], [9]]
    assert candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, 12, 13, 14, 15, 16, 17])) == [[3], [4], [5, 7, 12, 14], [8, 6, 10], [9, 13, 15, 16], [11], [17]]
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, None, 12, None, 22, 27, 40, None, 3, 6, 8, 9, 11, 13, 14, 18, 19, 21, 23, 26, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49])) == [[1, 26, 29], [5, 3, 6], [10, 7, 28, 31, 32, 34, 39, 44], [20, 15, 25, 8, 9, 13, 18], [30, 12, 22, 27, 33, 36, 37, 41, 42, 45, 46, 48], [35, 11, 14, 19, 21], [40, 38, 43, 47, 49], [23]]
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == [[1], [2], [4, 3, 5, 9], [8, 6, 10], [12, 7, 11, 13], [14], [15]]
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45])) == [[5], [10], [15, 12, 18, 28], [25, 20, 30], [35, 22, 32, 38], [40], [45]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10, 11, 12, None, 13, 14, 15])) == [[4], [2], [1, 5, 6, 11], [3, 8, 9], [7, 12, 13, 14], [10], [15]]
    assert candidate(root = tree_node([12, 7, 20, 3, 9, 15, 23, 1, 5, 8, 11, 13, 18, 21, 24, None, 2, 4, 6, None, 10, None, None, None, None, None, 14, 16, None, 17, 19, 22, None, None, 25, None, None, None, None, None, 26])) == [[1, 22], [3, 2, 4], [7, 5, 8, 13, 25], [12, 9, 15, 6, 10, 16], [20, 11, 18, 21], [23, 14, 17], [24, 26], [19]]
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, 3, 5, None, None, None, None, None, None, None])) == [[0], [2, 3, 5], [6, 4, 7], [8], [9]]
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 38, 1, 3, 6, 8, 11, 13, 17, 19, 22, 26, 28, 31, 33, 37, 39, 40])) == [[1], [2], [5, 3, 6, 11, 22], [10, 7, 12, 23], [20, 15, 25, 8, 13, 17, 26, 28, 33], [30, 18, 27, 32], [35, 19, 31, 37, 39], [38], [40]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14], [7, 23, 27, 29, 30], [15], [31]]
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, None, 18, 27, 32, None, 11, 14, 17, 19, 23, 26, 29, 31, 33, 34, 36, 37, 38, 39])) == [[39], [14], [5], [10, 17, 19, 31], [15, 12, 27], [25, 20, 30, 23, 26, 33, 34], [35, 18, 32], [40, 29, 36, 37], [11], [38]]
    assert candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, None, 5, 3])) == [[3], [7], [11], [4, 1], [5, 17], [8], [4], [5]]
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == [[31], [15], [7, 32, 33, 35, 39, 47], [3, 16, 17, 19, 23], [1, 8, 9, 11, 34, 36, 37, 40, 41, 43, 48, 49], [0, 4, 5, 18, 20, 21, 24, 25, 27], [2, 10, 12, 13, 38, 42, 44, 45, 50], [6, 22, 26, 28, 29], [14, 46], [30]]
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, None, 4, 6, 8, 12, 17, 22])) == [[1], [3, 4, 8], [7, 5, 9], [15, 6, 12, 17], [20], [22]]
    assert candidate(root = tree_node([3, 2, 3, None, 3, None, 1, 5, 4, None, 7, 2, None, None, 9, 6, 10])) == [[2], [2, 5], [3, 3], [3, 4], [1, 9, 6], [7], [10]]
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, 8, 9])) == [[1], [2], [3], [5, 4], [6, 8], [7], [9]]
    assert candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5, None, None, 6, None, None, None, None, None, None, None, None, 10, 11])) == [[4], [9, 5], [3, 0, 1], [8, 2], [7], [6]]
    assert candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, 7, 11, 13, 17, 19, 23])) == [[1], [3], [6, 5, 7, 13], [12, 9, 15], [18, 11, 17, 19], [21], [23]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 17, 20, 16, None, None, None, None, None, None, None, None, None, None, None, None, 19])) == [[16], [1], [3], [5, 6], [10, 7], [15, 8, 17], [18], [20]]
    assert candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, None, None, None, None, 12, None, None, None, None, 13, None, 14, None, None, None, None, 15, None, None, None, None, None, None, None, None, 16])) == [[3], [4], [5, 7], [8, 6, 10, 13], [9, 12], [11, 14]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14], [7, 23, 27, 29, 30], [15]]
    assert candidate(root = tree_node([15, 7, 23, 3, 11, 19, 29, 1, 5, 9, 13, 17, 21, 25, 27, 31, 33, 35, 37])) == [[31], [1], [3, 33, 35], [7, 5, 9, 17], [15, 11, 19, 37], [23, 13, 21, 25], [29], [27]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, 20, None, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, 22])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6, 16, 17], [3, 11, 13, 14, 19], [7, 18], [15, 20]]
    assert candidate(root = tree_node([10, -5, 15, -8, -3, 12, 20, -10, 1, None, -4, 11, 16, None, None, 13, 14])) == [[13], [-10], [-8, 14], [-5, 1, 11], [10, -3, 12], [15, -4, 16], [20]]
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, -2, 2, 3.5, None, None, None, None, None, None, None])) == [[-2], [1], [3, 2, 3.5], [5, 4, 7], [8], [9]]
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37])) == [[2], [5], [10, 7, 12, 22], [20, 15, 25], [30, 18, 27, 32], [35], [37]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == [[16], [8], [4, 17, 18, 20, 24], [2, 9, 10, 12], [1, 5, 6, 19, 21, 22, 25], [3, 11, 13, 14], [7, 23], [15]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == [[32], [16], [8, 33, 34, 36, 40, 48], [4, 17, 18, 20, 24], [2, 9, 10, 12, 35, 37, 38, 41, 42, 44, 49, 50], [1, 5, 6, 19, 21, 22, 25, 26, 28], [3, 11, 13, 14, 39, 43, 45, 46], [7, 23, 27, 29, 30], [15, 47], [31]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, None, None, 17, None, None, None, 18, None, None, None, 19, None, None, None, None, None, None, 20, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, 23, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, None, None, 25])) == [[8], [4], [2, 9, 10, 12], [1, 5, 6, 16, 17], [3, 11, 13, 14, 19], [7, 18], [15]]
    assert candidate(root = tree_node([8, 5, 12, 4, 7, 10, 14, 2, None, 6, None, 9, 11, 13, None, 15, None, None, None, None, None, None, None, 16])) == [[15], [2], [4], [5, 6, 9], [8, 7, 10, 16], [12, 11, 13], [14]]
    assert candidate(root = tree_node([5, 2, 6, 1, 3, None, 8, 0, 4, 9, None, None, None, 12])) == [[12], [0], [1], [2, 4, 9], [5, 3], [6], [8]]
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, None, 8, 9])) == [[8], [1], [2, 9], [3], [5, 4], [6], [7]]
    assert candidate(root = tree_node([10, 5, 15, None, 7, 12, 20, None, 6, 8, None, None, 18, None, None, None, None, 16, 17, None, None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 21, None, None, None, None, 22])) == [[5, 8], [10, 7, 12], [15, 6], [20, 16], [18], [17]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 20])) == [[1], [3], [5, 4, 6, 11], [10, 7, 12], [15, 8, 13, 17], [18], [20]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, None, 12])) == [[1], [3, 12], [5, 6], [10, 7], [15, 9], [18]]
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19])) == [[13], [3, 8], [7, 9, 14, 16, 18], [15, 10, 11], [20, 17, 19], [12]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, 9, 10, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 14, 16, 17, 19, 21, 22, 23, 24])) == [[1], [3], [5, 4, 6, 11, 10], [10, 7, 12, 2], [15, 8, 13, 18], [20], [25], [9]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, 8, 11, 13, 18, 25])) == [[1], [3], [5, 6, 11], [10, 7, 12], [15, 8, 13, 18], [20], [25]]
    assert candidate(root = tree_node([3, 9, 8, 4, 0, 1, 7, -6, 5, 2, None, None, None, None, 8, 10, None, None, None, None, None, None])) == [[10], [-6], [4], [9, 5, 2], [3, 0, 1], [8], [7], [8]]
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45, 3, 7, 11, 14, 16, 19, 21, 23, 27, 29, 31, 33, 37, 39, 43, 47, None, 4, 6, 8, 9, 13, 15, 17, 20, 24, 26, 30, 34, 36, 40, 42, 46, 50, 2, 1, 5, 10, 18, 25, 35, 45, None, None, None, None, None, None, None, None, 50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1])) == [[3, 50, 46, 37, 21], [5, 4, 6, 9, 20, 46], [10, 7, 11, 16, 27, 49, 48, 44, 43, 41, 36, 35, 33, 29, 20, 19, 17, 13, 4], [15, 12, 18, 28, 8, 13, 15, 24, 26, 34, 50, 2, 5, 35], [25, 20, 30, 14, 19, 21, 29, 31, 37, 47, 42, 40, 39, 34, 32, 31, 28, 27, 25, 18, 16, 15, 12, 11, 9, 3, 2], [35, 22, 32, 38, 17, 30, 36, 40, 1, 10, 18, 45], [40, 23, 33, 39, 43, 38, 30, 26, 24, 23, 14, 10, 8, 7, 1], [45, 42, 25], [47, 22, 6]]
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, None, 16, None, None, None, 13, None, None, None, 14])) == [[16], [9, 12], [3, 15], [20], [7]]
    assert candidate(root = tree_node([5, 2, 13, None, 3, 7, 14, 1, 4, 6, 8, 10, 15, None, None, 9, 11, None, 12, 16, 17])) == [[2, 1, 6], [5, 3, 7, 9, 12, 16], [13, 4, 8, 10], [14, 11, 17], [15]]
    assert candidate(root = tree_node([5, 1, 6, None, 3, None, None, 2, 4])) == [[1, 2], [5, 3], [6, 4]]
    assert candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, 16, 18, 21, 23, None, 24, 26, 35, None, None, None, None, None, None, None, None, 32])) == [[26], [5], [10, 35], [15, 12, 16, 21], [20, 17, 22, 32], [25, 18, 23], [30], [24]]
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])) == [[1], [2], [3], [5, 4], [6, 7], [8], [9]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 13, 17, None, None, 12, 14, 16, None, None, None, None, None, 19])) == [[1, 19], [3, 12], [5, 6], [10, 7, 14, 16], [15, 8, 13], [18], [17]]
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 185, 5, 15, 28, 45, 55, 65, 70, 80, 90, 105, 115, 130, 135, 145, 155, 165, 170, 180, 190, 195, 200])) == [[170], [5], [10, 180, 190, 200], [25, 15, 28, 55, 90], [50, 35, 60, 110, 195], [100, 75, 125, 45, 65, 70, 105, 115, 135], [150, 85, 140, 160], [175, 80, 130, 145, 155], [185], [165]]
    assert candidate(root = tree_node([50, 20, 30, 10, 25, 27, 35, 5, 15, None, None, 26, 33, 37, 40, None, 6, 9, 12, 18, None, None, None, None, None, None, 29, None, 31, None, 36, None, None, None, None, None, None, None, None])) == [[5], [10, 6, 9, 18], [20, 15, 26, 31, 36], [50, 25, 27, 12], [30, 33, 37], [35], [40], [29]]
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, 2, None, 4, 8, 13, 18, None, 10, 11, 12, 14, 16, 17, 19])) == [[1, 10, 16], [3, 2, 8], [7, 5, 9, 11, 12, 17, 19], [15, 4, 13, 18], [20, 14]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 3, 9, 15, 21, 28, 34, 40, 46, 53, 60, 65, 72, 79, 84, 89, 96])) == [[3], [6], [12, 9, 15, 28, 53], [25, 18, 31, 56], [50, 37, 62, 21, 34, 40, 60, 65, 79], [75, 43, 68, 81], [87, 46, 72, 84, 89], [93], [96]]
    assert candidate(root = tree_node([1, -10, 10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80, -90, 90, -100, 100])) == [[-80], [-40], [-20, 80, -90, -100], [-10, 40, -50, -60], [1, 20, -30, 90, 100], [10, 50, 60, -70], [30], [70]]
    assert candidate(root = tree_node([8, 5, 12, 4, 7, 10, 15, 3, 6, 9, 11, 13, 16, 18, 20])) == [[3], [4], [5, 6, 9, 13], [8, 7, 10], [12, 11, 16, 18], [15], [20]]
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 19, 21, 24, None, 7, None, None, None, None, None, None, 11, None, None, 23, None, None, None, None, None, 6, None, None, 8, None, None, 13, None, 14, None, 16, None, 17, None, None, None, None, None, None, None, 9])) == [[5], [10, 11], [15, 12, 21], [20, 18, 22], [25, 19, 24], [30, 23], [7, 6]]
    assert candidate(root = tree_node([7, 3, 9, 1, 5, 8, 10, 0, 2, 4, 6, None, 9])) == [[0], [1], [3, 2, 4], [7, 5, 8], [9, 6, 9], [10]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 16, 20, None, None, None, None, None, 19])) == [[1], [3], [5, 6], [10, 7], [15, 8, 16], [18, 19], [20]]
    assert candidate(root = tree_node([8, 5, 9, 4, 7, 8, 10, 3, None, 6, None, None, 9, None, None, 11, None, 12])) == [[11], [3], [4, 12], [5, 6], [8, 7, 8], [9, 9], [10]]
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37, 0, 4, 8, 14, 16, 24, 26, 31, 34, 36, 39, 41, 43])) == [[0], [2], [5, 4, 8, 16, 34], [10, 7, 12, 22], [20, 15, 25, 14, 24, 26, 36, 39, 43], [30, 18, 27, 32], [35, 31, 41], [37]]
    assert candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100])) == [[-80], [-40], [-20, -90, -100], [-10, -50, -60], [-30], [-70]]
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 27, 32, 37, 1, 3, 6, 8, 11, 13, 17, 19, 21, 23, 26, 28, 31, 33, 36, 38, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9])) == [[1], [2, 4], [5, 3, 6, 11, 21], [10, 7, 12, 22], [20, 15, 25, 8, 13, 17, 23, 26, 31], [30, 18, 27, 32], [35, 19, 28, 33, 36], [37], [38]]
    assert candidate(root = tree_node([7, 6, 8, 5, 7, 7, 9, 4, None, None, None, None, 6, 8, 10, None, None, None, None, None, None, None, None, None, None, 5, 9, 11])) == [[4], [5], [6], [7, 7, 7], [8, 6, 8], [9], [10]]
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 85, 5, 15, 30, 40, 55, 65, 80, 90, 1, 7, 12, 18, 28, 38, 48, 52, 58, 62, 68, 78, 82, 88, 92, 98, None, 6, 11, 13, 17, 21, 27, 32, 37, 42, 47, 51, 54, 57, 61, 64, 67, 72, 77, 81, 84, 87, 91, 95, 99, None, None, None, None, None, None, None, None, None, None, None, None, 14, 16, 19, 22, 26, 31, 36, 41, 46, 50, 53, 56, 60, 63, 66, 71, 76, 80, 83, 86, 90, 94, 98, None, 9, 11, 18, 25, 34, 43, 52, 61, 70, 79, 88, 97, None, 8, 20, 29, 39, 49, 59, 69, 78, 87, 96, None, None, None, None, None, None, 3, 24, 38, 48, 58, 68, 77, 86, 95, None, None, None, None, None, None, 2, 23, 37, 47, 57, 67, 76, 85, 94, None, None, None, None, None, None, None, 21, 36, 46, 56, 66, 75, 84, 93, None, None, None, None, None, None, None, None, 22, 35, 45, 55, 65, 74, 83, 92, None, None, None, None, None, None, None, None, None, 26, 34, 44, 54, 64, 73, 82, 91, None, None, None, None, None, None, None, None, None, None, 27, 33, 43, 53, 63, 72, 81, 90, None, None, None, None, None, None, None, None, None, None, None, 28, 32, 42, 52, 62, 71, 80, 89, None, None, None, None, None, None, None, None, None, None, None, None, 30, 31, 41, 51, 61, 70, 79, 88, None, None, None, None, None, None, None, None, None, None, None, None, None, 39, 40, 49, 59, 69, 78, 87, 96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 50, 60, 70, 80, 90])) == [[87, 95, 93], [1, 16, 50, 11, 69], [5, 6, 11, 17, 37, 67, 96, 3, 23, 92, 64, 50, 90], [10, 7, 12, 28, 58, 19, 22, 31, 53, 56, 63, 80, 18, 25, 43, 79, 49, 27, 43, 81, 28, 32, 52, 89, 78], [25, 15, 30, 55, 13, 21, 27, 42, 47, 54, 72, 77, 84, 99, 69, 24, 38, 58, 37, 47, 67, 36, 22, 35, 55, 73, 82, 60, 70], [50, 35, 60, 18, 38, 48, 62, 68, 82, 14, 26, 36, 41, 60, 66, 71, 83, 86, 94, 34, 52, 61, 88, 97, 8, 59, 33, 53, 63, 90, 42, 62, 71, 31, 39, 87], [75, 40, 65, 80, 32, 51, 57, 61, 81, 87, 91, 78, 48, 68, 77, 2, 57, 76, 85, 46, 56, 45, 65, 74, 26, 91, 80], [85, 52, 78, 88, 92, 46, 76, 90, 98, 70, 20, 29, 72, 80, 30, 41, 51, 70, 40, 49, 96], [90, 64, 95, 86, 94, 21, 66, 75, 83, 34, 44], [98, 9, 39, 61, 79, 88, 59], [84, 54]]
    assert candidate(root = tree_node([0, -3, 9, -10, None, 5, 10, None, -1, None, 3, 8, 15, -4, -2, 7, 12, None, None, None, None, None, None, None, None, -6])) == [[-10, -4], [-3, -1, -6], [0, 5, -2, 7], [9, 3, 8], [10, 12], [15]]
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8])) == [[1], [2], [3], [5, 4], [6], [7], [8]]


