def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == [[15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == [[15, 7], [9, 20], [3]]: {e}')
    
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
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == [[4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == [[4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == [[5, 1, 6, 8], [1, 3, -1], [2, 4], [0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == [[5, 1, 6, 8], [1, 3, -1], [2, 4], [0]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == [[5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == [[5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2])) == [[2], [1, 4], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2])) == [[2], [1, 4], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 4, 5, None, None, 6])) == [[4, 5, 6], [8, 15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 4, 5, None, None, 6])) == [[4, 5, 6], [8, 15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == [[10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == [[10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == [[7, 8], [4, 5, 6], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == [[7, 8], [4, 5, 6], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == [[6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == [[6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == [[4, 5], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == [[4, 5], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == [[12, 13, 14, 15], [8, 9, 10, 11], [4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == [[12, 13, 14, 15], [8, 9, 10, 11], [4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 15, 7, 2, 25, 8, 6, 1, 12, 9, 4, 18, 10])) == [[8, 6, 1, 12, 9, 4, 18, 10], [15, 7, 2, 25], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 15, 7, 2, 25, 8, 6, 1, 12, 9, 4, 18, 10])) == [[8, 6, 1, 12, 9, 4, 18, 10], [15, 7, 2, 25], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, None, 4, None])) == [[2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, None, 4, None])) == [[2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 17, 18, 20, None, None, None, None, None, None, 1])) == [[1], [12, 17, 18, 20], [15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 17, 18, 20, None, None, None, None, None, None, 1])) == [[1], [12, 17, 18, 20], [15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2, None, None])) == [[2], [1, 4], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2, None, None])) == [[2], [1, 4], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, None, 4, None, 3, None, 2, None, 1])) == [[1], [2], [3], [4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, None, 4, None, 3, None, 2, None, 1])) == [[1], [2], [3], [4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, 18, 25, 27])) == [[25, 27], [12, 18], [15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, 18, 25, 27])) == [[25, 27], [12, 18], [15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == [[16], [15], [14], [13], [12], [11], [10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == [[16], [15], [14], [13], [12], [11], [10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == [[6, 20], [5, 15], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == [[6, 20], [5, 15], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5])) == [[5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5])) == [[5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 10, None, 15, 7, 5, 11, 18])) == [[5, 11, 18], [10, 15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 10, None, 15, 7, 5, 11, 18])) == [[5, 11, 18], [10, 15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, None, None, 22])) == [[22], [25], [15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, None, None, 22])) == [[22], [25], [15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == [[3, 7, 18], [5, 15], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == [[3, 7, 18], [5, 15], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == [[4, 4, 4, 4], [3, 3], [2, 2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == [[4, 4, 4, 4], [3, 3], [2, 2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9])) == [[-7, -8, -9], [-3, -4, -5, -6], [-1, -2], [0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9])) == [[-7, -8, -9], [-3, -4, -5, -6], [-1, -2], [0]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, None, 17, 18, 19, 20, 21, 22, 23])) == [[16, 17, 18, 19, 20, 21, 22, 23], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, None, 17, 18, 19, 20, 21, 22, 23])) == [[16, 17, 18, 19, 20, 21, 22, 23], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == [[9], [8], [7], [6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == [[9], [8], [7], [6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 35, 65, 70, 85, 105, 115, 135, 145, 155, 175, 185])) == [[5, 15, 20, 35, 65, 70, 85, 105, 115, 135, 145, 155, 175, 185], [10, 30, 60, 80, 110, 140, 160, 180], [25, 75, 125, 175], [50, 150], [100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 35, 65, 70, 85, 105, 115, 135, 145, 155, 175, 185])) == [[5, 15, 20, 35, 65, 70, 85, 105, 115, 135, 145, 155, 175, 185], [10, 30, 60, 80, 110, 140, 160, 180], [25, 75, 125, 175], [50, 150], [100]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == [[3, 5], [0, 4, 7, 9], [2, 8], [6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == [[3, 5], [0, 4, 7, 9], [2, 8], [6]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == [[7, 2, 5, 1], [11, 13, 4], [4, 8], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == [[7, 2, 5, 1], [11, 13, 4], [4, 8], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == [[7, 2, 1], [11, 13, 4], [4, 8], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == [[7, 2, 1], [11, 13, 4], [4, 8], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 1, None, 2, None, 3, None, 4])) == [[4], [3], [2], [1], [0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 1, None, 2, None, 3, None, 4])) == [[4], [3], [2], [1], [0]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, 10, 11, None, 13, None, None, 14, 15])) == [[14, 15], [8, 9, 10, 11, 13], [4, 5, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, 10, 11, None, 13, None, None, 14, 15])) == [[14, 15], [8, 9, 10, 11, 13], [4, 5, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 8, 10, 15, 7, None, None, None, 13, None, None, None, 17])) == [[13, 17], [8, 10, 15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 8, 10, 15, 7, None, None, None, 13, None, None, None, 17])) == [[13, 17], [8, 10, 15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == [[-7, -8, -9, -10], [-3, -4, -5, -6], [-1, -2], [0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == [[-7, -8, -9, -10], [-3, -4, -5, -6], [-1, -2], [0]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == [[9], [8], [7], [6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == [[9], [8], [7], [6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 16, 17])) == [[16, 17], [15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 16, 17])) == [[16, 17], [15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == [[3, 6], [1, 4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == [[3, 6], [1, 4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, 15])) == [[14, 15], [8, 9, 10, 11, 12, 13], [4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, 15])) == [[14, 15], [8, 9, 10, 11, 12, 13], [4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == [[8], [7], [6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == [[8], [7], [6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, 9])) == [[9], [7, 8], [4, 5, 6], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, 9])) == [[9], [7, 8], [4, 5, 6], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -5, 15, None, -8, None, 20, -12, None, None, 18])) == [[-12, 18], [-8, 20], [-5, 15], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -5, 15, None, -8, None, 20, -12, None, None, 18])) == [[-12, 18], [-8, 20], [-5, 15], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == [[10, 30, 60, 80, 110, 140, 160, 180], [25, 75, 125, 175], [50, 150], [100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == [[10, 30, 60, 80, 110, 140, 160, 180], [25, 75, 125, 175], [50, 150], [100]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, None, 20, 30, 40, None, 50, None, None, 60, 70])) == [[60, 70], [50], [30, 40], [20], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, None, 20, 30, 40, None, 50, None, None, 60, 70])) == [[60, 70], [50], [30, 40], [20], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, 6, None, None, 3, None, None, None, 9])) == [[9], [6, 3], [7, 2, 5, 1], [11, 13, 4], [4, 8], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, 6, None, None, 3, None, None, None, 9])) == [[9], [6, 3], [7, 2, 5, 1], [11, 13, 4], [4, 8], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == [[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == [[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])) == [[7, 4], [6, 2, 0, 8], [5, 1], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])) == [[7, 4], [6, 2, 0, 8], [5, 1], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == [[16, 17, 18, 19, 20], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == [[16, 17, 18, 19, 20], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6, 2, None, None, None, None, 7])) == [[7], [2], [3, 6], [1, 4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6, 2, None, None, None, None, 7])) == [[7], [2], [3, 6], [1, 4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, 6, None, None, 11, 12])) == [[11, 12], [2, 6], [1, 4, 7, 9], [3, 8], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, 6, None, None, 11, 12])) == [[11, 12], [2, 6], [1, 4, 7, 9], [3, 8], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [[8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [[8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 3, None, None])) == [[3], [7, 2, 1], [11, 13, 4], [4, 8], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 3, None, None])) == [[3], [7, 2, 1], [11, 13, 4], [4, 8], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7])) == [[6, 7], [4, 5], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7])) == [[6, 7], [4, 5], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == [[3, 4, 4, 3], [2, 2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == [[3, 4, 4, 3], [2, 2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, 3, None, 6, 7])) == [[3, 6, 7], [1, 4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, 3, None, 6, 7])) == [[3, 6, 7], [1, 4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == [[2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == [[2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, 8])) == [[8], [7], [6], [4, 5], [2, 3], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, 8])) == [[8], [7], [6], [4, 5], [2, 3], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) == [[4, 4], [3, 3], [2, 2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) == [[4, 4], [3, 3], [2, 2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == [[7], [6], [5], [4], [3], [2], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == [[7], [6], [5], [4], [3], [2], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == [[-15], [-7, -8, -9, -10, -11, -12, -13, -14], [-3, -4, -5, -6], [-1, -2], [0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == [[-15], [-7, -8, -9, -10, -11, -12, -13, -14], [-3, -4, -5, -6], [-1, -2], [0]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 10, None, 15, 7, 11, None, 13, 14])) == [[11, 13, 14], [10, 15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 10, None, 15, 7, 11, None, 13, 14])) == [[11, 13, 14], [10, 15, 7], [9, 20], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 10, 11, 15, 7, None, None, 12, None, 16, 13, None, None, None, 14, 17, 18])) == [[14, 17, 18], [12, 16, 13], [10, 11, 15, 7], [9, 20], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 10, 11, 15, 7, None, None, 12, None, 16, 13, None, None, None, 14, 17, 18])) == [[14, 17, 18], [12, 16, 13], [10, 11, 15, 7], [9, 20], [3]]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == [[15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([1])) == [[1]]
    assert candidate(root = tree_node([])) == []
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == [[4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == [[5, 1, 6, 8], [1, 3, -1], [2, 4], [0]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == [[5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == [[2], [1, 4], [3]]
    assert candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 4, 5, None, None, 6])) == [[4, 5, 6], [8, 15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == [[10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == [[7, 8], [4, 5, 6], [2, 3], [1]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == [[6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == [[4, 5], [2, 3], [1]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == [[12, 13, 14, 15], [8, 9, 10, 11], [4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([3, 9, 20, 15, 7, 2, 25, 8, 6, 1, 12, 9, 4, 18, 10])) == [[8, 6, 1, 12, 9, 4, 18, 10], [15, 7, 2, 25], [9, 20], [3]]
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, None, 4, None])) == [[2], [1]]
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 17, 18, 20, None, None, None, None, None, None, 1])) == [[1], [12, 17, 18, 20], [15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([3, 1, 4, None, 2, None, None])) == [[2], [1, 4], [3]]
    assert candidate(root = tree_node([5, None, 4, None, 3, None, 2, None, 1])) == [[1], [2], [3], [4], [5]]
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, 18, 25, 27])) == [[25, 27], [12, 18], [15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == [[16], [15], [14], [13], [12], [11], [10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == [[6, 20], [5, 15], [10]]
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5])) == [[5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([3, 9, 20, 10, None, 15, 7, 5, 11, 18])) == [[5, 11, 18], [10, 15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, None, None, 22])) == [[22], [25], [15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == [[3, 7, 18], [5, 15], [10]]
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == [[4, 4, 4, 4], [3, 3], [2, 2], [1]]
    assert candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9])) == [[-7, -8, -9], [-3, -4, -5, -6], [-1, -2], [0]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, None, 17, 18, 19, 20, 21, 22, 23])) == [[16, 17, 18, 19, 20, 21, 22, 23], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == [[9], [8], [7], [6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 35, 65, 70, 85, 105, 115, 135, 145, 155, 175, 185])) == [[5, 15, 20, 35, 65, 70, 85, 105, 115, 135, 145, 155, 175, 185], [10, 30, 60, 80, 110, 140, 160, 180], [25, 75, 125, 175], [50, 150], [100]]
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == [[3, 5], [0, 4, 7, 9], [2, 8], [6]]
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == [[7, 2, 5, 1], [11, 13, 4], [4, 8], [5]]
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == [[7, 2, 1], [11, 13, 4], [4, 8], [5]]
    assert candidate(root = tree_node([0, None, 1, None, 2, None, 3, None, 4])) == [[4], [3], [2], [1], [0]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, 8, 9, 10, 11, None, 13, None, None, 14, 15])) == [[14, 15], [8, 9, 10, 11, 13], [4, 5, 7], [2, 3], [1]]
    assert candidate(root = tree_node([3, 9, 20, 8, 10, 15, 7, None, None, None, 13, None, None, None, 17])) == [[13, 17], [8, 10, 15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == [[-7, -8, -9, -10], [-3, -4, -5, -6], [-1, -2], [0]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == [[9], [8], [7], [6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 16, 17])) == [[16, 17], [15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == [[3, 6], [1, 4], [5]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, 15])) == [[14, 15], [8, 9, 10, 11, 12, 13], [4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == [[8], [7], [6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, 9])) == [[9], [7, 8], [4, 5, 6], [2, 3], [1]]
    assert candidate(root = tree_node([10, -5, 15, None, -8, None, 20, -12, None, None, 18])) == [[-12, 18], [-8, 20], [-5, 15], [10]]
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == [[10, 30, 60, 80, 110, 140, 160, 180], [25, 75, 125, 175], [50, 150], [100]]
    assert candidate(root = tree_node([10, None, 20, 30, 40, None, 50, None, None, 60, 70])) == [[60, 70], [50], [30, 40], [20], [10]]
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, 6, None, None, 3, None, None, None, 9])) == [[9], [6, 3], [7, 2, 5, 1], [11, 13, 4], [4, 8], [5]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == [[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])) == [[7, 4], [6, 2, 0, 8], [5, 1], [3]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == [[16, 17, 18, 19, 20], [8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6, 2, None, None, None, None, 7])) == [[7], [2], [3, 6], [1, 4], [5]]
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, 6, None, None, 11, 12])) == [[11, 12], [2, 6], [1, 4, 7, 9], [3, 8], [5]]
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == [[8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 3, None, None])) == [[3], [7, 2, 1], [11, 13, 4], [4, 8], [5]]
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7])) == [[6, 7], [4, 5], [2, 3], [1]]
    assert candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == [[3, 4, 4, 3], [2, 2], [1]]
    assert candidate(root = tree_node([5, 1, 4, 3, None, 6, 7])) == [[3, 6, 7], [1, 4], [5]]
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == [[2], [1]]
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, 8])) == [[8], [7], [6], [4, 5], [2, 3], [1]]
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) == [[4, 4], [3, 3], [2, 2], [1]]
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == [[7], [6], [5], [4], [3], [2], [1]]
    assert candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == [[-15], [-7, -8, -9, -10, -11, -12, -13, -14], [-3, -4, -5, -6], [-1, -2], [0]]
    assert candidate(root = tree_node([3, 9, 20, 10, None, 15, 7, 11, None, 13, 14])) == [[11, 13, 14], [10, 15, 7], [9, 20], [3]]
    assert candidate(root = tree_node([3, 9, 20, 10, 11, 15, 7, None, None, 12, None, 16, 13, None, None, None, 14, 17, 18])) == [[14, 17, 18], [12, 16, 13], [10, 11, 15, 7], [9, 20], [3]]


