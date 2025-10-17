def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1]],angle = 90,location = [0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1]],angle = 90,location = [0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [100, 99], [99, 100], [99, 99]],angle = 45,location = [100, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [100, 99], [99, 100], [99, 99]],angle = 45,location = [100, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [5, 5], [10, 10]],angle = 90,location = [0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [5, 5], [10, 10]],angle = 90,location = [0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 2], [3, 3], [4, 4], [1, 1]],angle = 45,location = [2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 2], [3, 3], [4, 4], [1, 1]],angle = 45,location = [2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]],angle = 0,location = [0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]],angle = 0,location = [0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 1]],angle = 13,location = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 1]],angle = 13,location = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]],angle = 45,location = [1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]],angle = 45,location = [1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],angle = 90,location = [3, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],angle = 90,location = [3, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]],angle = 0,location = [0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]],angle = 0,location = [0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [51, 50], [52, 50]],angle = 1,location = [50, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [51, 50], [52, 50]],angle = 1,location = [50, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [50, 50]],angle = 90,location = [25, 25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [50, 50]],angle = 90,location = [25, 25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 1], [2, 2], [3, 3]],angle = 90,location = [1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 1], [2, 2], [3, 3]],angle = 90,location = [1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100]],angle = 360,location = [100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100]],angle = 360,location = [100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [100, 100]],angle = 1,location = [50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [100, 100]],angle = 1,location = [50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1]],angle = 180,location = [1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1]],angle = 180,location = [1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],angle = 360,location = [1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],angle = 360,location = [1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 180,location = [3, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 180,location = [3, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [11, 10], [12, 10], [13, 10], [14, 10]],angle = 45,location = [10, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [11, 10], [12, 10], [13, 10], [14, 10]],angle = 45,location = [10, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [1, 2], [2, 1]],angle = 45,location = [1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [1, 2], [2, 1]],angle = 45,location = [1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 1], [2, 2], [3, 4], [1, 1]],angle = 90,location = [1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 1], [2, 2], [3, 4], [1, 1]],angle = 90,location = [1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]],angle = 90,location = [0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]],angle = 90,location = [0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 0], [0, 0]],angle = 180,location = [0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 0], [0, 0]],angle = 180,location = [0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1]],angle = 360,location = [1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1]],angle = 360,location = [1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 360,location = [1, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 360,location = [1, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [2, 0], [0, 2], [-2, 0], [0, -2]],angle = 45,location = [0, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [2, 0], [0, 2], [-2, 0], [0, -2]],angle = 45,location = [0, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15], [5, 5], [25, 25], [5, 25], [25, 5], [15, 5], [5, 15], [25, 15], [15, 25]],angle = 120,location = [15, 15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15], [5, 5], [25, 25], [5, 25], [25, 5], [15, 5], [5, 15], [25, 15], [15, 25]],angle = 120,location = [15, 15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [10, 5], [15, 5], [20, 5], [25, 5], [5, 10], [10, 10], [15, 10], [20, 10], [25, 10]],angle = 45,location = [15, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [10, 5], [15, 5], [20, 5], [25, 5], [5, 10], [10, 10], [15, 10], [20, 10], [25, 10]],angle = 45,location = [15, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0], [60, 0], [70, 0], [80, 0], [90, 0]],angle = 10,location = [50, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0], [60, 0], [70, 0], [80, 0], [90, 0]],angle = 10,location = [50, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 30,location = [5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 30,location = [5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],angle = 10,location = [1, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],angle = 10,location = [1, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4]],angle = 180,location = [1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4]],angle = 180,location = [1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4]],angle = 180,location = [2, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4]],angle = 180,location = [2, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],angle = 30,location = [5, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],angle = 30,location = [5, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]],angle = 30,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]],angle = 30,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 1], [1, 2], [3, 1], [1, 3], [2, 2]],angle = 90,location = [2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 1], [1, 2], [3, 1], [1, 3], [2, 2]],angle = 90,location = [2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 0], [20, 0], [30, 0], [40, 0], [50, 0]],angle = 180,location = [25, 25]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 0], [20, 0], [30, 0], [40, 0], [50, 0]],angle = 180,location = [25, 25]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],angle = 359,location = [1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],angle = 359,location = [1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 180,location = [5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 180,location = [5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [5, 1]],angle = 90,location = [3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [5, 1]],angle = 90,location = [3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [50, 50], [50, 100], [100, 50], [75, 75], [25, 25], [75, 25], [25, 75]],angle = 45,location = [50, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [50, 50], [50, 100], [100, 50], [75, 75], [25, 25], [75, 25], [25, 75]],angle = 45,location = [50, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 90,location = [4, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 90,location = [4, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 3], [3, 2], [4, 5], [5, 4], [6, 5], [5, 6]],angle = 45,location = [4, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 3], [3, 2], [4, 5], [5, 4], [6, 5], [5, 6]],angle = 45,location = [4, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 6], [6, 5], [5, 4], [4, 5]],angle = 90,location = [5, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 6], [6, 5], [5, 4], [4, 5]],angle = 90,location = [5, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 1], [3, 4], [5, 5], [4, 2], [1, 2], [3, 1]],angle = 45,location = [3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 1], [3, 4], [5, 5], [4, 2], [1, 2], [3, 1]],angle = 45,location = [3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 0], [2, 2], [1, 3], [3, 3], [0, 2]],angle = 60,location = [2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 0], [2, 2], [1, 3], [3, 3], [0, 2]],angle = 60,location = [2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 10,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 10,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]],angle = 90,location = [5, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]],angle = 90,location = [5, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 9], [9, 10], [9, 11], [11, 10], [11, 11], [8, 8], [8, 9], [9, 8], [11, 9]],angle = 45,location = [10, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 9], [9, 10], [9, 11], [11, 10], [11, 11], [8, 8], [8, 9], [9, 8], [11, 9]],angle = 45,location = [10, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],angle = 30,location = [5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],angle = 30,location = [5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 2], [4, 5], [5, 4], [3, 3]],angle = 45,location = [3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 2], [4, 5], [5, 4], [3, 3]],angle = 45,location = [3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [0, 1], [2, 1], [0, 2], [2, 2], [0, 3], [2, 3], [0, 4], [2, 4], [0, 5], [2, 5]],angle = 90,location = [1, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [0, 1], [2, 1], [0, 2], [2, 2], [0, 3], [2, 3], [0, 4], [2, 4], [0, 5], [2, 5]],angle = 90,location = [1, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 45,location = [25, 25]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 45,location = [25, 25]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 10], [5, 15], [5, 20], [5, 25]],angle = 90,location = [5, 15]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 10], [5, 15], [5, 20], [5, 25]],angle = 90,location = [5, 15]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 30,location = [3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 30,location = [3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],angle = 90,location = [5, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],angle = 90,location = [5, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],angle = 30,location = [5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],angle = 30,location = [5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15], [5, 5], [25, 25]],angle = 90,location = [15, 15]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15], [5, 5], [25, 25]],angle = 90,location = [15, 15]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]],angle = 90,location = [0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]],angle = 90,location = [0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 45,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 45,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [50, 40], [50, 30], [50, 20], [50, 10], [50, 0], [50, -10], [50, -20], [50, -30], [50, -40]],angle = 120,location = [50, 50]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [50, 40], [50, 30], [50, 20], [50, 10], [50, 0], [50, -10], [50, -20], [50, -30], [50, -40]],angle = 120,location = [50, 50]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],angle = 60,location = [2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],angle = 60,location = [2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4], [5, 5], [5, 5], [5, 5]],angle = 90,location = [3, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4], [5, 5], [5, 5], [5, 5]],angle = 90,location = [3, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]],angle = 45,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]],angle = 45,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 30,location = [0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 30,location = [0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],angle = 60,location = [5, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],angle = 60,location = [5, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70]],angle = 15,location = [10, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70]],angle = 15,location = [10, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 30,location = [25, 25]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 30,location = [25, 25]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 0], [0, 100], [100, 100], [50, 50], [25, 25], [75, 75]],angle = 60,location = [50, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 0], [0, 100], [100, 100], [50, 50], [25, 25], [75, 75]],angle = 60,location = [50, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],angle = 180,location = [10, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],angle = 180,location = [10, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]],angle = 90,location = [0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]],angle = 90,location = [0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]],angle = 90,location = [5, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]],angle = 90,location = [5, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]],angle = 15,location = [25, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]],angle = 15,location = [25, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2]],angle = 90,location = [3, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2]],angle = 90,location = [3, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 90,location = [30, 30]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 90,location = [30, 30]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 1], [1, 1], [0, 0], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 90,location = [1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 1], [1, 1], [0, 0], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 90,location = [1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 60,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 60,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 10,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 10,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 10,location = [5, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 10,location = [5, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [11, 11], [10, 11], [9, 10], [10, 9], [9, 9], [9, 11], [11, 9]],angle = 60,location = [10, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [11, 11], [10, 11], [9, 10], [10, 9], [9, 9], [9, 11], [11, 9]],angle = 60,location = [10, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 60,location = [3, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 60,location = [3, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [10, 10], [10, 11], [11, 10], [11, 11]],angle = 90,location = [8, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [10, 10], [10, 11], [11, 10], [11, 11]],angle = 90,location = [8, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15]],angle = 45,location = [15, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15]],angle = 45,location = [15, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [1, 4], [1, 4], [1, 5], [1, 5], [1, 5], [1, 1], [1, 1], [1, 1]],angle = 10,location = [1, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [1, 4], [1, 4], [1, 5], [1, 5], [1, 5], [1, 1], [1, 1], [1, 1]],angle = 10,location = [1, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 0], [0, 100], [0, 0], [100, 100], [50, 50]],angle = 90,location = [50, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 0], [0, 100], [0, 0], [100, 100], [50, 50]],angle = 90,location = [50, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 10,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 10,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [7, 8], [8, 7], [8, 8]],angle = 90,location = [6, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [7, 8], [8, 7], [8, 8]],angle = 90,location = [6, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [50, 49], [50, 51], [49, 50], [51, 50], [49, 49], [51, 51], [52, 52], [48, 48]],angle = 30,location = [50, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [50, 49], [50, 51], [49, 50], [51, 50], [49, 49], [51, 51], [52, 52], [48, 48]],angle = 30,location = [50, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 5,location = [1, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 5,location = [1, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 0], [0, 2], [2, 2], [1, 1], [0, 0], [1, 0]],angle = 45,location = [1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 0], [0, 2], [2, 2], [1, 1], [0, 0], [1, 0]],angle = 45,location = [1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 0], [0, 10], [10, 10], [5, 5], [2, 2], [8, 8]],angle = 30,location = [5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 0], [0, 10], [10, 10], [5, 5], [2, 2], [8, 8]],angle = 30,location = [5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3], [4, 4]],angle = 45,location = [3, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3], [4, 4]],angle = 45,location = [3, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 120,location = [1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 120,location = [1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 90,location = [0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 90,location = [0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [100, 99], [99, 100], [99, 98], [101, 100], [100, 101]],angle = 10,location = [100, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [100, 99], [99, 100], [99, 98], [101, 100], [100, 101]],angle = 10,location = [100, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 90,location = [1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 90,location = [1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 45,location = [5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 45,location = [5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 10], [15, 20], [10, 15], [15, 15]],angle = 30,location = [15, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 10], [15, 20], [10, 15], [15, 15]],angle = 30,location = [15, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 90,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 90,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 360,location = [5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 360,location = [5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],angle = 360,location = [3, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],angle = 360,location = [3, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 11], [11, 10], [11, 11], [10, 9], [9, 10], [9, 9], [9, 11], [11, 9]],angle = 60,location = [10, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 11], [11, 10], [11, 11], [10, 9], [9, 10], [9, 9], [9, 11], [11, 9]],angle = 60,location = [10, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]],angle = 10,location = [2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]],angle = 10,location = [2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 0], [0, 10], [10, 10], [0, 0], [5, 5]],angle = 60,location = [5, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 0], [0, 10], [10, 10], [0, 0], [5, 5]],angle = 60,location = [5, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [50, 40], [50, 60], [40, 50], [60, 50], [40, 40], [60, 60], [40, 60], [60, 40], [50, 30], [50, 70], [30, 50], [70, 50]],angle = 60,location = [50, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [50, 40], [50, 60], [40, 50], [60, 50], [40, 40], [60, 60], [40, 60], [60, 40], [50, 30], [50, 70], [30, 50], [70, 50]],angle = 60,location = [50, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [9, 10], [8, 10], [7, 10], [6, 10], [5, 10], [4, 10], [3, 10], [2, 10], [1, 10]],angle = 5,location = [5, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [9, 10], [8, 10], [7, 10], [6, 10], [5, 10], [4, 10], [3, 10], [2, 10], [1, 10]],angle = 5,location = [5, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 20,location = [1, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 20,location = [1, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[90, 90], [91, 90], [90, 91], [91, 91], [100, 100]],angle = 10,location = [90, 90]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[90, 90], [91, 90], [90, 91], [91, 91], [100, 100]],angle = 10,location = [90, 90]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],angle = 30,location = [5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],angle = 30,location = [5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [1, 10], [10, 9], [9, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 60,location = [5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [1, 10], [10, 9], [9, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 60,location = [5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 0], [5, 10], [10, 5], [0, 5]],angle = 180,location = [5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 0], [5, 10], [10, 5], [0, 5]],angle = 180,location = [5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [1, 4], [1, 4], [1, 5], [1, 5], [1, 5]],angle = 10,location = [1, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [1, 4], [1, 4], [1, 5], [1, 5], [1, 5]],angle = 10,location = [1, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70], [10, 80], [10, 90]],angle = 10,location = [10, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70], [10, 80], [10, 90]],angle = 10,location = [10, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],angle = 10,location = [5, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],angle = 10,location = [5, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 180,location = [1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 180,location = [1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 5,location = [5, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 5,location = [5, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],angle = 30,location = [5, 50]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],angle = 30,location = [5, 50]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 0], [0, 5], [5, 5], [0, 0], [2, 2], [3, 3], [1, 1], [4, 4]],angle = 90,location = [2, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 0], [0, 5], [5, 5], [0, 0], [2, 2], [3, 3], [1, 1], [4, 4]],angle = 90,location = [2, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 0], [6, 1], [7, 0], [8, 1], [9, 0], [10, 1]],angle = 15,location = [5, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 0], [6, 1], [7, 0], [8, 1], [9, 0], [10, 1]],angle = 15,location = [5, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7]],angle = 45,location = [5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7]],angle = 45,location = [5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [10, 30], [20, 10], [20, 20], [20, 30], [30, 10], [30, 20], [30, 30]],angle = 30,location = [20, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [10, 30], [20, 10], [20, 20], [20, 30], [30, 10], [30, 20], [30, 30]],angle = 30,location = [20, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 1], [1, 2], [0, 1], [0, 2], [1, 1], [2, 0], [2, 2], [0, 0]],angle = 45,location = [1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 1], [1, 2], [0, 1], [0, 2], [1, 1], [2, 0], [2, 2], [0, 0]],angle = 45,location = [1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],angle = 90,location = [2, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],angle = 90,location = [2, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [51, 50], [52, 50], [53, 50], [54, 50], [55, 50]],angle = 5,location = [52, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [51, 50], [52, 50], [53, 50], [54, 50], [55, 50]],angle = 5,location = [52, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 10], [10, 20], [20, 20], [10, 30], [20, 30], [10, 40], [20, 40]],angle = 180,location = [15, 15]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 10], [10, 20], [20, 20], [10, 30], [20, 30], [10, 40], [20, 40]],angle = 180,location = [15, 15]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 0], [0, 100], [50, 50], [25, 25], [75, 75]],angle = 45,location = [50, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 0], [0, 100], [50, 50], [25, 25], [75, 75]],angle = 45,location = [50, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 2], [4, 5], [5, 4], [3, 3], [2, 1]],angle = 45,location = [3, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 2], [4, 5], [5, 4], [3, 3], [2, 1]],angle = 45,location = [3, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],angle = 180,location = [5, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],angle = 180,location = [5, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 180,location = [5, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 180,location = [5, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 90,location = [1, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 90,location = [1, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],angle = 1,location = [5, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],angle = 1,location = [5, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],angle = 40,location = [50, 50]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],angle = 40,location = [50, 50]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 45,location = [1, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 45,location = [1, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]],angle = 90,location = [20, 20]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]],angle = 90,location = [20, 20]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],angle = 90,location = [3, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],angle = 90,location = [3, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 60,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 60,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]],angle = 45,location = [50, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]],angle = 45,location = [50, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9], [5, 4], [4, 5], [4, 4], [6, 4], [4, 6], [7, 6], [6, 7], [8, 6], [6, 8]],angle = 45,location = [5, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9], [5, 4], [4, 5], [4, 4], [6, 4], [4, 6], [7, 6], [6, 7], [8, 6], [6, 8]],angle = 45,location = [5, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 30,location = [1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 30,location = [1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 10,location = [5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 10,location = [5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [2, 1], [2, 1], [2, 1], [3, 1], [3, 1], [3, 1], [4, 1], [4, 1], [4, 1], [5, 1], [5, 1], [5, 1]],angle = 90,location = [3, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [2, 1], [2, 1], [2, 1], [3, 1], [3, 1], [3, 1], [4, 1], [4, 1], [4, 1], [5, 1], [5, 1], [5, 1]],angle = 90,location = [3, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [10, 10], [10, 10]],angle = 45,location = [15, 15]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [10, 10], [10, 10]],angle = 45,location = [15, 15]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 2], [3, 2], [4, 2], [2, 3], [3, 3], [4, 3], [2, 4], [3, 4], [4, 4]],angle = 45,location = [3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 2], [3, 2], [4, 2], [2, 3], [3, 3], [4, 3], [2, 4], [3, 4], [4, 4]],angle = 45,location = [3, 3]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1]],angle = 90,location = [0, 0]) == 2
    assert candidate(points = [[100, 100], [100, 99], [99, 100], [99, 99]],angle = 45,location = [100, 100]) == 3
    assert candidate(points = [[0, 0], [5, 5], [10, 10]],angle = 90,location = [0, 0]) == 3
    assert candidate(points = [[2, 2], [3, 3], [4, 4], [1, 1]],angle = 45,location = [2, 2]) == 3
    assert candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]],angle = 0,location = [0, 0]) == 2
    assert candidate(points = [[1, 0], [2, 1]],angle = 13,location = [1, 1]) == 1
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]],angle = 45,location = [1, 1]) == 4
    assert candidate(points = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],angle = 90,location = [3, 2]) == 3
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]],angle = 0,location = [0, 0]) == 4
    assert candidate(points = [[50, 50], [51, 50], [52, 50]],angle = 1,location = [50, 50]) == 3
    assert candidate(points = [[0, 0], [50, 50]],angle = 90,location = [25, 25]) == 1
    assert candidate(points = [[2, 1], [2, 2], [3, 3]],angle = 90,location = [1, 1]) == 3
    assert candidate(points = [[100, 100]],angle = 360,location = [100, 100]) == 1
    assert candidate(points = [[0, 0], [100, 100]],angle = 1,location = [50, 50]) == 1
    assert candidate(points = [[1, 1], [1, 1], [1, 1]],angle = 180,location = [1, 1]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],angle = 360,location = [1, 1]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 180,location = [3, 3]) == 5
    assert candidate(points = [[10, 10], [11, 10], [12, 10], [13, 10], [14, 10]],angle = 45,location = [10, 10]) == 5
    assert candidate(points = [[1, 1], [2, 2], [1, 2], [2, 1]],angle = 45,location = [1, 1]) == 3
    assert candidate(points = [[2, 1], [2, 2], [3, 4], [1, 1]],angle = 90,location = [1, 1]) == 4
    assert candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]],angle = 90,location = [0, 0]) == 4
    assert candidate(points = [[0, 0], [0, 0], [0, 0]],angle = 180,location = [0, 0]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1]],angle = 360,location = [1, 1]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 360,location = [1, 1]) == 17
    assert candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [2, 0], [0, 2], [-2, 0], [0, -2]],angle = 45,location = [0, 0]) == 2
    assert candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15], [5, 5], [25, 25], [5, 25], [25, 5], [15, 5], [5, 15], [25, 15], [15, 25]],angle = 120,location = [15, 15]) == 6
    assert candidate(points = [[5, 5], [10, 5], [15, 5], [20, 5], [25, 5], [5, 10], [10, 10], [15, 10], [20, 10], [25, 10]],angle = 45,location = [15, 15]) == 5
    assert candidate(points = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0], [60, 0], [70, 0], [80, 0], [90, 0]],angle = 10,location = [50, 0]) == 6
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 30,location = [5, 5]) == 5
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],angle = 10,location = [1, 5]) == 5
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4]],angle = 180,location = [1, 1]) == 10
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4]],angle = 180,location = [2, 2]) == 12
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],angle = 30,location = [5, 1]) == 10
    assert candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]],angle = 30,location = [5, 5]) == 6
    assert candidate(points = [[2, 1], [1, 2], [3, 1], [1, 3], [2, 2]],angle = 90,location = [2, 1]) == 4
    assert candidate(points = [[10, 0], [20, 0], [30, 0], [40, 0], [50, 0]],angle = 180,location = [25, 25]) == 5
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],angle = 359,location = [1, 1]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 180,location = [5, 5]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [5, 1]],angle = 90,location = [3, 3]) == 4
    assert candidate(points = [[100, 100], [50, 50], [50, 100], [100, 50], [75, 75], [25, 25], [75, 25], [25, 75]],angle = 45,location = [50, 50]) == 4
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 90,location = [4, 4]) == 5
    assert candidate(points = [[2, 3], [3, 2], [4, 5], [5, 4], [6, 5], [5, 6]],angle = 45,location = [4, 4]) == 2
    assert candidate(points = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 6], [6, 5], [5, 4], [4, 5]],angle = 90,location = [5, 5]) == 8
    assert candidate(points = [[2, 1], [3, 4], [5, 5], [4, 2], [1, 2], [3, 1]],angle = 45,location = [3, 3]) == 2
    assert candidate(points = [[2, 0], [2, 2], [1, 3], [3, 3], [0, 2]],angle = 60,location = [2, 1]) == 3
    assert candidate(points = [[5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 10,location = [5, 5]) == 6
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]],angle = 90,location = [5, 1]) == 11
    assert candidate(points = [[10, 10], [10, 9], [9, 10], [9, 11], [11, 10], [11, 11], [8, 8], [8, 9], [9, 8], [11, 9]],angle = 45,location = [10, 10]) == 4
    assert candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],angle = 30,location = [5, 5]) == 4
    assert candidate(points = [[1, 2], [2, 2], [4, 5], [5, 4], [3, 3]],angle = 45,location = [3, 3]) == 3
    assert candidate(points = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [0, 1], [2, 1], [0, 2], [2, 2], [0, 3], [2, 3], [0, 4], [2, 4], [0, 5], [2, 5]],angle = 90,location = [1, 1]) == 17
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 45,location = [25, 25]) == 3
    assert candidate(points = [[5, 5], [5, 10], [5, 15], [5, 20], [5, 25]],angle = 90,location = [5, 15]) == 3
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 30,location = [3, 3]) == 3
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],angle = 90,location = [5, 1]) == 6
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],angle = 30,location = [5, 5]) == 4
    assert candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15], [5, 5], [25, 25]],angle = 90,location = [15, 15]) == 4
    assert candidate(points = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]],angle = 90,location = [0, 0]) == 4
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 45,location = [5, 5]) == 6
    assert candidate(points = [[50, 50], [50, 40], [50, 30], [50, 20], [50, 10], [50, 0], [50, -10], [50, -20], [50, -30], [50, -40]],angle = 120,location = [50, 50]) == 10
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],angle = 60,location = [2, 2]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4], [5, 5], [5, 5], [5, 5]],angle = 90,location = [3, 3]) == 9
    assert candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]],angle = 45,location = [5, 5]) == 6
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 30,location = [0, 0]) == 10
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],angle = 60,location = [5, 1]) == 6
    assert candidate(points = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70]],angle = 15,location = [10, 10]) == 7
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 30,location = [25, 25]) == 3
    assert candidate(points = [[100, 0], [0, 100], [100, 100], [50, 50], [25, 25], [75, 75]],angle = 60,location = [50, 50]) == 3
    assert candidate(points = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],angle = 180,location = [10, 5]) == 10
    assert candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]],angle = 90,location = [0, 0]) == 3
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]],angle = 90,location = [5, 0]) == 7
    assert candidate(points = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]],angle = 15,location = [25, 10]) == 3
    assert candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2]],angle = 90,location = [3, 2]) == 6
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],angle = 90,location = [30, 30]) == 3
    assert candidate(points = [[1, 0], [0, 1], [1, 1], [0, 0], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 90,location = [1, 1]) == 5
    assert candidate(points = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 60,location = [5, 5]) == 6
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 10,location = [5, 5]) == 6
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 10,location = [5, 1]) == 5
    assert candidate(points = [[10, 10], [11, 11], [10, 11], [9, 10], [10, 9], [9, 9], [9, 11], [11, 9]],angle = 60,location = [10, 10]) == 3
    assert candidate(points = [[0, 1], [1, 0], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 60,location = [3, 3]) == 5
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [10, 10], [10, 11], [11, 10], [11, 11]],angle = 90,location = [8, 8]) == 4
    assert candidate(points = [[10, 10], [10, 20], [20, 10], [20, 20], [15, 15]],angle = 45,location = [15, 15]) == 2
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [1, 4], [1, 4], [1, 5], [1, 5], [1, 5], [1, 1], [1, 1], [1, 1]],angle = 10,location = [1, 3]) == 12
    assert candidate(points = [[100, 0], [0, 100], [0, 0], [100, 100], [50, 50]],angle = 90,location = [50, 50]) == 3
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 10,location = [5, 5]) == 6
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [7, 8], [8, 7], [8, 8]],angle = 90,location = [6, 6]) == 5
    assert candidate(points = [[50, 50], [50, 49], [50, 51], [49, 50], [51, 50], [49, 49], [51, 51], [52, 52], [48, 48]],angle = 30,location = [50, 50]) == 3
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 5,location = [1, 5]) == 6
    assert candidate(points = [[2, 0], [0, 2], [2, 2], [1, 1], [0, 0], [1, 0]],angle = 45,location = [1, 1]) == 3
    assert candidate(points = [[10, 0], [0, 10], [10, 10], [5, 5], [2, 2], [8, 8]],angle = 30,location = [5, 5]) == 3
    assert candidate(points = [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3], [4, 4]],angle = 45,location = [3, 3]) == 6
    assert candidate(points = [[1, 2], [2, 1], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 120,location = [1, 1]) == 10
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 90,location = [0, 0]) == 10
    assert candidate(points = [[100, 100], [100, 99], [99, 100], [99, 98], [101, 100], [100, 101]],angle = 10,location = [100, 100]) == 2
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],angle = 90,location = [1, 1]) == 15
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 45,location = [5, 5]) == 5
    assert candidate(points = [[10, 10], [20, 10], [15, 20], [10, 15], [15, 15]],angle = 30,location = [15, 15]) == 2
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 90,location = [5, 5]) == 6
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 360,location = [5, 5]) == 15
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],angle = 360,location = [3, 4]) == 11
    assert candidate(points = [[10, 10], [10, 11], [11, 10], [11, 11], [10, 9], [9, 10], [9, 9], [9, 11], [11, 9]],angle = 60,location = [10, 10]) == 3
    assert candidate(points = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3]],angle = 10,location = [2, 2]) == 1
    assert candidate(points = [[10, 0], [0, 10], [10, 10], [0, 0], [5, 5]],angle = 60,location = [5, 5]) == 2
    assert candidate(points = [[50, 50], [50, 40], [50, 60], [40, 50], [60, 50], [40, 40], [60, 60], [40, 60], [60, 40], [50, 30], [50, 70], [30, 50], [70, 50]],angle = 60,location = [50, 50]) == 4
    assert candidate(points = [[10, 10], [9, 10], [8, 10], [7, 10], [6, 10], [5, 10], [4, 10], [3, 10], [2, 10], [1, 10]],angle = 5,location = [5, 10]) == 6
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 20,location = [1, 5]) == 6
    assert candidate(points = [[90, 90], [91, 90], [90, 91], [91, 91], [100, 100]],angle = 10,location = [90, 90]) == 3
    assert candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],angle = 30,location = [5, 5]) == 4
    assert candidate(points = [[10, 1], [1, 10], [10, 9], [9, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],angle = 60,location = [5, 5]) == 5
    assert candidate(points = [[5, 0], [5, 10], [10, 5], [0, 5]],angle = 180,location = [5, 5]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [1, 4], [1, 4], [1, 5], [1, 5], [1, 5]],angle = 10,location = [1, 3]) == 9
    assert candidate(points = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70], [10, 80], [10, 90]],angle = 10,location = [10, 50]) == 5
    assert candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],angle = 10,location = [5, 0]) == 6
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],angle = 180,location = [1, 1]) == 10
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 5,location = [5, 1]) == 5
    assert candidate(points = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],angle = 30,location = [5, 50]) == 6
    assert candidate(points = [[5, 0], [0, 5], [5, 5], [0, 0], [2, 2], [3, 3], [1, 1], [4, 4]],angle = 90,location = [2, 2]) == 5
    assert candidate(points = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 0], [6, 1], [7, 0], [8, 1], [9, 0], [10, 1]],angle = 15,location = [5, 0]) == 4
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7]],angle = 45,location = [5, 5]) == 4
    assert candidate(points = [[10, 10], [10, 20], [10, 30], [20, 10], [20, 20], [20, 30], [30, 10], [30, 20], [30, 30]],angle = 30,location = [20, 20]) == 2
    assert candidate(points = [[1, 0], [2, 1], [1, 2], [0, 1], [0, 2], [1, 1], [2, 0], [2, 2], [0, 0]],angle = 45,location = [1, 1]) == 3
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],angle = 90,location = [2, 0]) == 4
    assert candidate(points = [[50, 50], [51, 50], [52, 50], [53, 50], [54, 50], [55, 50]],angle = 5,location = [52, 50]) == 4
    assert candidate(points = [[10, 10], [20, 10], [10, 20], [20, 20], [10, 30], [20, 30], [10, 40], [20, 40]],angle = 180,location = [15, 15]) == 7
    assert candidate(points = [[100, 0], [0, 100], [50, 50], [25, 25], [75, 75]],angle = 45,location = [50, 50]) == 2
    assert candidate(points = [[1, 2], [2, 2], [4, 5], [5, 4], [3, 3], [2, 1]],angle = 45,location = [3, 3]) == 4
    assert candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],angle = 180,location = [5, 0]) == 10
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],angle = 180,location = [5, 1]) == 9
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 90,location = [1, 5]) == 6
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],angle = 1,location = [5, 0]) == 6
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],angle = 40,location = [50, 50]) == 6
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],angle = 45,location = [1, 5]) == 6
    assert candidate(points = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]],angle = 90,location = [20, 20]) == 5
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],angle = 90,location = [3, 1]) == 6
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9]],angle = 60,location = [5, 5]) == 6
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]],angle = 45,location = [50, 50]) == 5
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [7, 7], [8, 8], [9, 9], [5, 4], [4, 5], [4, 4], [6, 4], [4, 6], [7, 6], [6, 7], [8, 6], [6, 8]],angle = 45,location = [5, 5]) == 8
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],angle = 30,location = [1, 1]) == 10
    assert candidate(points = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],angle = 10,location = [5, 5]) == 6
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [2, 1], [2, 1], [2, 1], [3, 1], [3, 1], [3, 1], [4, 1], [4, 1], [4, 1], [5, 1], [5, 1], [5, 1]],angle = 90,location = [3, 1]) == 9
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [10, 10], [10, 10]],angle = 45,location = [15, 15]) == 3
    assert candidate(points = [[2, 2], [3, 2], [4, 2], [2, 3], [3, 3], [4, 3], [2, 4], [3, 4], [4, 4]],angle = 45,location = [3, 3]) == 3


