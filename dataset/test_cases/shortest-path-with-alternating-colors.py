def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,redEdges = [[0, 1], [1, 2]],blueEdges = [[1, 3]]) == [0, 1, -1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,redEdges = [[0, 1], [1, 2]],blueEdges = [[1, 3]]) == [0, 1, -1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,redEdges = [[0, 1], [0, 2], [0, 3]],blueEdges = [[1, 2], [1, 3], [2, 3]]) == [0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,redEdges = [[0, 1], [0, 2], [0, 3]],blueEdges = [[1, 2], [1, 3], [2, 3]]) == [0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,redEdges = [[0, 0], [0, 0]],blueEdges = [[0, 0], [0, 0]]) == [0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,redEdges = [[0, 0], [0, 0]],blueEdges = [[0, 0], [0, 0]]) == [0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,redEdges = [[0, 1]],blueEdges = [[2, 1]]) == [0, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,redEdges = [[0, 1]],blueEdges = [[2, 1]]) == [0, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,redEdges = [[0, 1], [0, 2], [1, 3]],blueEdges = [[2, 3]]) == [0, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,redEdges = [[0, 1], [0, 2], [1, 3]],blueEdges = [[2, 3]]) == [0, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,redEdges = [[0, 1]],blueEdges = [[1, 0]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,redEdges = [[0, 1]],blueEdges = [[1, 0]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = []) == [0, 1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = []) == [0, 1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,redEdges = [],blueEdges = [[0, 1], [1, 2]]) == [0, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,redEdges = [],blueEdges = [[0, 1], [1, 2]]) == [0, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4], [2, 4]],blueEdges = [[1, 2], [2, 3]]) == [0, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4], [2, 4]],blueEdges = [[1, 2], [2, 3]]) == [0, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,redEdges = [[0, 1], [1, 0]],blueEdges = [[2, 1]]) == [0, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,redEdges = [[0, 1], [1, 0]],blueEdges = [[2, 1]]) == [0, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,redEdges = [[0, 1], [1, 2]],blueEdges = [[1, 2]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,redEdges = [[0, 1], [1, 2]],blueEdges = [[1, 2]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,redEdges = [[0, 1], [0, 2], [1, 2]],blueEdges = [[0, 3], [2, 3]]) == [0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,redEdges = [[0, 1], [0, 2], [1, 2]],blueEdges = [[0, 3], [2, 3]]) == [0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,redEdges = [[0, 1], [1, 2], [2, 3]],blueEdges = [[0, 2]]) == [0, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,redEdges = [[0, 1], [1, 2], [2, 3]],blueEdges = [[0, 2]]) == [0, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,redEdges = [[0, 1], [1, 2], [2, 0]],blueEdges = [[0, 2]]) == [0, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,redEdges = [[0, 1], [1, 2], [2, 0]],blueEdges = [[0, 2]]) == [0, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,redEdges = [[0, 0]],blueEdges = [[0, 0]]) == [0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,redEdges = [[0, 0]],blueEdges = [[0, 0]]) == [0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,redEdges = [[0, 0]],blueEdges = [[1, 1]]) == [0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,redEdges = [[0, 0]],blueEdges = [[1, 1]]) == [0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,redEdges = [[0, 1], [1, 2]],blueEdges = []) == [0, 1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,redEdges = [[0, 1], [1, 2]],blueEdges = []) == [0, 1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,redEdges = [[0, 1], [2, 3]],blueEdges = [[1, 2], [3, 0]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,redEdges = [[0, 1], [2, 3]],blueEdges = [[1, 2], [3, 0]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 4]]) == [0, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 4]]) == [0, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5]]) == [0, 1, 1, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5]]) == [0, 1, 1, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 3], [3, 1], [2, 4]]) == [0, 1, -1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 3], [3, 1], [2, 4]]) == [0, 1, -1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]) == [0, 1, -1, 1, 2, 3, -1, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]) == [0, 1, -1, 1, 2, 3, -1, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 3], [1, 4], [2, 5]]) == [0, 1, -1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 3], [1, 4], [2, 5]]) == [0, 1, -1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 1, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 1, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[1, 3], [2, 4], [5, 7], [6, 8]]) == [0, 1, -1, 2, 3, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[1, 3], [2, 4], [5, 7], [6, 8]]) == [0, 1, -1, 2, 3, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]]) == [0, 1, 1, 1, 2, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]]) == [0, 1, 1, 1, 2, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4]],blueEdges = [[0, 3], [1, 2], [1, 4], [2, 3]]) == [0, 1, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4]],blueEdges = [[0, 3], [1, 2], [1, 4], [2, 3]]) == [0, 1, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 0]]) == [0, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 0]]) == [0, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],blueEdges = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 1, -1, -1, -1, -1, -1, -1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],blueEdges = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 1, -1, -1, -1, -1, -1, -1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[9, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[9, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 4], [2, 6]],blueEdges = [[0, 2], [1, 3], [3, 5], [5, 7], [7, 1], [4, 6]]) == [0, 1, 1, 2, 1, 3, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 4], [2, 6]],blueEdges = [[0, 2], [1, 3], [3, 5], [5, 7], [7, 1], [4, 6]]) == [0, 1, 1, 2, 1, 3, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 1]]) == [0, 1, 1, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 1]]) == [0, 1, 1, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 5], [5, 7], [7, 1], [0, 2], [2, 4], [4, 6], [6, 0]]) == [0, 1, 1, 2, -1, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 5], [5, 7], [7, 1], [0, 2], [2, 4], [4, 6], [6, 0]]) == [0, 1, 1, 2, -1, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [0, 4], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 0], [3, 1], [4, 2]]) == [0, 1, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [0, 4], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 0], [3, 1], [4, 2]]) == [0, 1, 1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[1, 3], [3, 5], [5, 1], [2, 4], [4, 6], [6, 2]]) == [0, 1, -1, 2, 3, -1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[1, 3], [3, 5], [5, 1], [2, 4], [4, 6], [6, 2]]) == [0, 1, -1, 2, 3, -1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == [0, 1, 1, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == [0, 1, 1, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],blueEdges = [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14], [8, 0], [9, 1], [10, 2], [11, 3], [12, 4], [13, 5], [14, 6]]) == [0, 1, 5, 9, 13, 17, 21, 1, 2, 3, 7, 11, 15, 19, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],blueEdges = [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14], [8, 0], [9, 1], [10, 2], [11, 3], [12, 4], [13, 5], [14, 6]]) == [0, 1, 5, 9, 13, 17, 21, 1, 2, 3, 7, 11, 15, 19, 23]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]],blueEdges = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [0, 1, 4, 5, 8, 9, 1, 2, 3, 6, 7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]],blueEdges = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [0, 1, 4, 5, 8, 9, 1, 2, 3, 6, 7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[5, 0], [0, 5], [1, 4], [4, 1], [2, 5], [5, 2]]) == [0, 1, 4, 5, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[5, 0], [0, 5], [1, 4], [4, 1], [2, 5], [5, 2]]) == [0, 1, 4, 5, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == [0, 1, -1, -1, 1, 2, 3, -1, -1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == [0, 1, -1, -1, 1, 2, 3, -1, -1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]) == [0, 1, -1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]) == [0, 1, -1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 1], [5, 2], [6, 4]]) == [0, 1, 4, 1, 2, 3, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 1], [5, 2], [6, 4]]) == [0, 1, 4, 1, 2, 3, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6]]) == [0, 1, -1, 1, 2, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6]]) == [0, 1, -1, 1, 2, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 5], [4, 6]],blueEdges = [[5, 7], [5, 8], [6, 7], [6, 8], [7, 0], [7, 1], [8, 0], [8, 2], [0, 3], [0, 4]]) == [0, 1, 1, 1, 1, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 5], [4, 6]],blueEdges = [[5, 7], [5, 8], [6, 7], [6, 8], [7, 0], [7, 1], [8, 0], [8, 2], [0, 3], [0, 4]]) == [0, 1, 1, 1, 1, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[9, 0], [0, 9], [1, 8], [8, 1], [2, 7], [7, 2], [3, 6], [6, 3], [4, 5], [5, 4]]) == [0, 1, -1, -1, -1, -1, -1, -1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[9, 0], [0, 9], [1, 8], [8, 1], [2, 7], [7, 2], [3, 6], [6, 3], [4, 5], [5, 4]]) == [0, 1, -1, -1, -1, -1, -1, -1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 4], [4, 5], [5, 1]]) == [0, 1, -1, 2, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 4], [4, 5], [5, 1]]) == [0, 1, -1, 2, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5]],blueEdges = [[0, 2], [2, 3], [3, 0], [4, 1], [5, 0]]) == [0, 1, 1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5]],blueEdges = [[0, 2], [2, 3], [3, 0], [4, 1], [5, 0]]) == [0, 1, 1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [2, 3], [4, 5], [5, 6]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, 1, 2, -1, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [2, 3], [4, 5], [5, 6]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, 1, 2, -1, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 7], [1, 6], [2, 5], [3, 4], [5, 3], [6, 2], [7, 1]]) == [0, 1, 5, 9, 10, 6, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 7], [1, 6], [2, 5], [3, 4], [5, 3], [6, 2], [7, 1]]) == [0, 1, 5, 9, 10, 6, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[7, 0], [0, 7], [1, 6], [6, 1], [2, 5], [5, 2], [3, 4], [4, 3]]) == [0, 1, -1, -1, -1, -1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[7, 0], [0, 7], [1, 6], [6, 1], [2, 5], [5, 2], [3, 4], [4, 3]]) == [0, 1, -1, -1, -1, -1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [2, 5]]) == [0, 1, -1, 1, 2, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [2, 5]]) == [0, 1, -1, 1, 2, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3]],blueEdges = [[0, 2], [2, 4], [4, 1], [1, 5]]) == [0, 1, 1, 1, -1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3]],blueEdges = [[0, 2], [2, 4], [4, 1], [1, 5]]) == [0, 1, 1, 1, -1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [2, 4]]) == [0, 1, 1, 2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [2, 4]]) == [0, 1, 1, 2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 3], [3, 5]]) == [0, 1, -1, 2, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 3], [3, 5]]) == [0, 1, -1, 2, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5]]) == [0, 1, 1, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5]]) == [0, 1, 1, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],blueEdges = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, -1, -1, -1, 1, 2, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],blueEdges = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, -1, -1, -1, 1, 2, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[1, 3], [2, 4], [5, 7]]) == [0, 1, -1, 2, 3, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[1, 3], [2, 4], [5, 7]]) == [0, 1, -1, 2, 3, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 2], [2, 0], [0, 1]]) == [0, 1, 2, 2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 2], [2, 0], [0, 1]]) == [0, 1, 2, 2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [0, 1, 1, 1, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [0, 1, 1, 1, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[1, 3], [2, 4]]) == [0, 1, -1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[1, 3], [2, 4]]) == [0, 1, -1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [2, 7], [3, 8], [4, 9]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 0], [8, 1], [9, 2]]) == [0, 1, 4, 1, 2, 1, 6, 3, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [2, 7], [3, 8], [4, 9]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 0], [8, 1], [9, 2]]) == [0, 1, 4, 1, 2, 1, 6, 3, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, -1, -1, -1, 1, 2, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, -1, -1, -1, 1, 2, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[0, 2], [2, 4], [4, 1], [1, 3], [3, 0]]) == [0, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[0, 2], [2, 4], [4, 1], [1, 3], [3, 0]]) == [0, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[6, 0], [0, 6], [1, 5], [5, 1], [2, 4], [4, 2], [3, 6], [6, 3]]) == [0, 1, 6, 4, 5, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[6, 0], [0, 6], [1, 5], [5, 1], [2, 4], [4, 2], [3, 6], [6, 3]]) == [0, 1, 6, 4, 5, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[1, 2], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [0, 3]]) == [0, 1, 1, 1, 2, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[1, 2], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [0, 3]]) == [0, 1, 1, 1, 2, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 1], [4, 3]]) == [0, 1, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 1], [4, 3]]) == [0, 1, 1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 0], [3, 4]],blueEdges = [[0, 2], [2, 3], [3, 0], [4, 1]]) == [0, 1, 1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 0], [3, 4]],blueEdges = [[0, 2], [2, 3], [3, 0], [4, 1]]) == [0, 1, 1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 5], [2, 6], [3, 7]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 1], [7, 2], [8, 4]]) == [0, 1, 3, 1, 2, 3, 4, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 5], [2, 6], [3, 7]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 1], [7, 2], [8, 4]]) == [0, 1, 3, 1, 2, 3, 4, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[8, 4], [4, 0], [0, 2], [2, 4], [5, 1], [1, 3], [3, 5], [7, 6]]) == [0, 1, 1, 2, -1, 3, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[8, 4], [4, 0], [0, 2], [2, 4], [5, 1], [1, 3], [3, 5], [7, 6]]) == [0, 1, 1, 2, -1, 3, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 3], [3, 1], [2, 4], [4, 2]]) == [0, 1, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 3], [3, 1], [2, 4], [4, 2]]) == [0, 1, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 0], [3, 1], [4, 0]]) == [0, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 0], [3, 1], [4, 0]]) == [0, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,redEdges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8]]) == [0, 1, -1, 1, 1, 2, 3, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,redEdges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8]]) == [0, 1, -1, 1, 1, 2, 3, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0]]) == [0, 1, 1, 2, 3, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0]]) == [0, 1, 1, 2, 3, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],blueEdges = [[0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],blueEdges = [[0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, 1, 1, 3, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, 1, 1, 3, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,redEdges = [[0, 2], [2, 4], [4, 6], [6, 8]],blueEdges = [[1, 3], [3, 5], [5, 7], [7, 9]]) == [0, -1, 1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,redEdges = [[0, 2], [2, 4], [4, 6], [6, 8]],blueEdges = [[1, 3], [3, 5], [5, 7], [7, 9]]) == [0, -1, 1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 4]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [0, 1, 5, 1, 2, 3, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 4]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [0, 1, 5, 1, 2, 3, 7]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7]],blueEdges = [[0, 3], [0, 4], [1, 5], [1, 6], [2, 7]]) == [0, 1, 1, 1, 1, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7]],blueEdges = [[0, 3], [0, 4], [1, 5], [1, 6], [2, 7]]) == [0, 1, 1, 1, 1, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 3], [2, 4], [3, 5], [4, 0], [5, 1], [5, 2]]) == [0, 1, -1, 2, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 3], [2, 4], [3, 5], [4, 0], [5, 1], [5, 2]]) == [0, 1, -1, 2, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]) == [0, 1, 1, 2, 3, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]) == [0, 1, 1, 2, 3, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [1, 4], [2, 5]]) == [0, 1, -1, 1, 2, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [1, 4], [2, 5]]) == [0, 1, -1, 1, 2, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, -1, 2, 3, -1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, -1, 2, 3, -1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 0], [0, 1]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 0], [0, 1]]) == [0, 1, 2, 3, 4]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,redEdges = [[0, 1], [1, 2]],blueEdges = [[1, 3]]) == [0, 1, -1, 2]
    assert candidate(n = 4,redEdges = [[0, 1], [0, 2], [0, 3]],blueEdges = [[1, 2], [1, 3], [2, 3]]) == [0, 1, 1, 1]
    assert candidate(n = 2,redEdges = [[0, 0], [0, 0]],blueEdges = [[0, 0], [0, 0]]) == [0, -1]
    assert candidate(n = 3,redEdges = [[0, 1]],blueEdges = [[2, 1]]) == [0, 1, -1]
    assert candidate(n = 4,redEdges = [[0, 1], [0, 2], [1, 3]],blueEdges = [[2, 3]]) == [0, 1, 1, 2]
    assert candidate(n = 2,redEdges = [[0, 1]],blueEdges = [[1, 0]]) == [0, 1]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = []) == [0, 1, -1, -1, -1]
    assert candidate(n = 3,redEdges = [],blueEdges = [[0, 1], [1, 2]]) == [0, 1, -1]
    assert candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4], [2, 4]],blueEdges = [[1, 2], [2, 3]]) == [0, 1, 1, 2, 3]
    assert candidate(n = 3,redEdges = [[0, 1], [1, 0]],blueEdges = [[2, 1]]) == [0, 1, -1]
    assert candidate(n = 3,redEdges = [[0, 1], [1, 2]],blueEdges = [[1, 2]]) == [0, 1, 2]
    assert candidate(n = 4,redEdges = [[0, 1], [0, 2], [1, 2]],blueEdges = [[0, 3], [2, 3]]) == [0, 1, 1, 1]
    assert candidate(n = 4,redEdges = [[0, 1], [1, 2], [2, 3]],blueEdges = [[0, 2]]) == [0, 1, 1, 2]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3, 4]
    assert candidate(n = 3,redEdges = [[0, 1], [1, 2], [2, 0]],blueEdges = [[0, 2]]) == [0, 1, 1]
    assert candidate(n = 2,redEdges = [[0, 0]],blueEdges = [[0, 0]]) == [0, -1]
    assert candidate(n = 2,redEdges = [[0, 0]],blueEdges = [[1, 1]]) == [0, -1]
    assert candidate(n = 5,redEdges = [],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, -1, -1, -1]
    assert candidate(n = 3,redEdges = [[0, 1], [1, 2]],blueEdges = []) == [0, 1, -1]
    assert candidate(n = 4,redEdges = [[0, 1], [2, 3]],blueEdges = [[1, 2], [3, 0]]) == [0, 1, 2, 3]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 4]]) == [0, 1, 1, 2, 3]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5]]) == [0, 1, 1, 2, 3, 3]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 3], [3, 1], [2, 4]]) == [0, 1, -1, 2, 3]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]
    assert candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]]) == [0, 1, -1, 1, 2, 3, -1, 3, 4]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 3], [1, 4], [2, 5]]) == [0, 1, -1, 1, 2, 3]
    assert candidate(n = 6,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 1, 2, 3, 3]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, 1]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[1, 3], [2, 4], [5, 7], [6, 8]]) == [0, 1, -1, 2, 3, -1, -1, -1, -1, -1]
    assert candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]]) == [0, 1, 1, 1, 2, 2, 3, 3]
    assert candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4]],blueEdges = [[0, 3], [1, 2], [1, 4], [2, 3]]) == [0, 1, 1, 1, 2]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 0]]) == [0, 1, 1, 2, 3]
    assert candidate(n = 10,redEdges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],blueEdges = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [0, 1, -1, -1, -1, -1, -1, -1, 2, 1]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[9, 8], [8, 7], [7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [0, 1, 2, 3, 4, 5, 6]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 4], [2, 6]],blueEdges = [[0, 2], [1, 3], [3, 5], [5, 7], [7, 1], [4, 6]]) == [0, 1, 1, 2, 1, 3, 2, 3]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 1]]) == [0, 1, 1, 2, 3, 3]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[7, 6], [6, 5], [5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1, -1, -1]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 5], [5, 7], [7, 1], [0, 2], [2, 4], [4, 6], [6, 0]]) == [0, 1, 1, 2, -1, 3, -1, -1]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(n = 5,redEdges = [[0, 1], [0, 4], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 0], [3, 1], [4, 2]]) == [0, 1, 1, 2, 1]
    assert candidate(n = 15,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[1, 3], [3, 5], [5, 1], [2, 4], [4, 6], [6, 2]]) == [0, 1, -1, 2, 3, -1, 4]
    assert candidate(n = 6,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == [0, 1, 1, 2, 3, 3]
    assert candidate(n = 15,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],blueEdges = [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14], [8, 0], [9, 1], [10, 2], [11, 3], [12, 4], [13, 5], [14, 6]]) == [0, 1, 5, 9, 13, 17, 21, 1, 2, 3, 7, 11, 15, 19, 23]
    assert candidate(n = 5,redEdges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4]],blueEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 1, 2, 3]
    assert candidate(n = 12,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]],blueEdges = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [0, 1, 4, 5, 8, 9, 1, 2, 3, 6, 7, 10]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[5, 0], [0, 5], [1, 4], [4, 1], [2, 5], [5, 2]]) == [0, 1, 4, 5, 2, 1]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == [0, 1, -1, -1, 1, 2, 3, -1, -1, 3]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]) == [0, 1, -1, 2, 1]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 1], [5, 2], [6, 4]]) == [0, 1, 4, 1, 2, 3, 6]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6]]) == [0, 1, -1, 1, 2, 3, -1]
    assert candidate(n = 9,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 5], [4, 6]],blueEdges = [[5, 7], [5, 8], [6, 7], [6, 8], [7, 0], [7, 1], [8, 0], [8, 2], [0, 3], [0, 4]]) == [0, 1, 1, 1, 1, 2, 2, 2, 2]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[9, 0], [0, 9], [1, 8], [8, 1], [2, 7], [7, 2], [3, 6], [6, 3], [4, 5], [5, 4]]) == [0, 1, -1, -1, -1, -1, -1, -1, 2, 1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 4], [4, 5], [5, 1]]) == [0, 1, -1, 2, -1, -1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5]],blueEdges = [[0, 2], [2, 3], [3, 0], [4, 1], [5, 0]]) == [0, 1, 1, -1, -1, -1]
    assert candidate(n = 7,redEdges = [[0, 1], [2, 3], [4, 5], [5, 6]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, 1, 2, -1, 3, 4]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 7], [1, 6], [2, 5], [3, 4], [5, 3], [6, 2], [7, 1]]) == [0, 1, 5, 9, 10, 6, 2, 1]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[7, 0], [0, 7], [1, 6], [6, 1], [2, 5], [5, 2], [3, 4], [4, 3]]) == [0, 1, -1, -1, -1, -1, 2, 1]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [2, 5]]) == [0, 1, -1, 1, 2, -1, -1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]) == [0, 1, -1, -1, -1, -1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3]],blueEdges = [[0, 2], [2, 4], [4, 1], [1, 5]]) == [0, 1, 1, 1, -1, 2]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [2, 4]]) == [0, 1, 1, 2, -1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 3], [3, 5]]) == [0, 1, -1, 2, 3, -1]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5]]) == [0, 1, 1, 2, 3, 3]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],blueEdges = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, -1, -1, -1, 1, 2, 3, -1, -1]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[1, 3], [2, 4], [5, 7]]) == [0, 1, -1, 2, 3, -1, -1, -1]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0]],blueEdges = [[1, 3], [3, 2], [2, 0], [0, 1]]) == [0, 1, 2, 2, -1]
    assert candidate(n = 7,redEdges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [0, 1, 1, 1, 2, 2, 3]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]],blueEdges = [[1, 3], [2, 4]]) == [0, 1, -1, 2, 3]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 5], [2, 7], [3, 8], [4, 9]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 0], [8, 1], [9, 2]]) == [0, 1, 4, 1, 2, 1, 6, 3, 2, 3]
    assert candidate(n = 10,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],blueEdges = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, -1, -1, -1, 1, 2, 3, -1, -1]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[0, 2], [2, 4], [4, 1], [1, 3], [3, 0]]) == [0, 1, 1, 2, 3]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[6, 0], [0, 6], [1, 5], [5, 1], [2, 4], [4, 2], [3, 6], [6, 3]]) == [0, 1, 6, 4, 5, 2, 1]
    assert candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[1, 2], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [0, 3]]) == [0, 1, 1, 1, 2, 3, 3, 4]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 1], [4, 3]]) == [0, 1, 1, 2, 1]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 0], [3, 4]],blueEdges = [[0, 2], [2, 3], [3, 0], [4, 1]]) == [0, 1, 1, -1, -1]
    assert candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == [0, 1, 1, 2, 3, 3, 4, 5, 5]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 5], [2, 6], [3, 7]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 1], [7, 2], [8, 4]]) == [0, 1, 3, 1, 2, 3, 4, 2, 4]
    assert candidate(n = 9,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[8, 4], [4, 0], [0, 2], [2, 4], [5, 1], [1, 3], [3, 5], [7, 6]]) == [0, 1, 1, 2, -1, 3, 4, -1, -1]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 3], [3, 1], [2, 4], [4, 2]]) == [0, 1, 4, 2, 3]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 0], [1, 2], [2, 3], [3, 4]],blueEdges = [[0, 2], [1, 3], [2, 0], [3, 1], [4, 0]]) == [0, 1, 1, 2, 3]
    assert candidate(n = 9,redEdges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],blueEdges = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8]]) == [0, 1, -1, 1, 1, 2, 3, 2, 3]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0]]) == [0, 1, 1, 2, 3, 3, 4, 5]
    assert candidate(n = 10,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],blueEdges = [[0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [4, 9]]) == [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    assert candidate(n = 7,redEdges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, 1, 1, 3, 2, 3]
    assert candidate(n = 10,redEdges = [[0, 2], [2, 4], [4, 6], [6, 8]],blueEdges = [[1, 3], [3, 5], [5, 7], [7, 9]]) == [0, -1, 1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 4]],blueEdges = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [0, 1, 5, 1, 2, 3, 7]
    assert candidate(n = 8,redEdges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7]],blueEdges = [[0, 3], [0, 4], [1, 5], [1, 6], [2, 7]]) == [0, 1, 1, 1, 1, 2, 2, 2]
    assert candidate(n = 6,redEdges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5]],blueEdges = [[1, 3], [2, 4], [3, 5], [4, 0], [5, 1], [5, 2]]) == [0, 1, -1, 2, 3, -1]
    assert candidate(n = 8,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],blueEdges = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]) == [0, 1, 1, 2, 3, 3, 4, 5]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[0, 3], [1, 4], [2, 5]]) == [0, 1, -1, 1, 2, 3, -1]
    assert candidate(n = 7,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],blueEdges = [[1, 3], [2, 4], [3, 5], [4, 6]]) == [0, 1, -1, 2, 3, -1, 4]
    assert candidate(n = 5,redEdges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],blueEdges = [[1, 2], [2, 3], [3, 4], [4, 0], [0, 1]]) == [0, 1, 2, 3, 4]


