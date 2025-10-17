def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(points = [[3, 1], [1, 3], [1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[3, 1], [1, 3], [1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 1], [1, 3], [2, 1], [1, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 1], [1, 3], [2, 1], [1, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [1, 2], [2, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [1, 2], [2, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 5], [0, 0], [2, 4], [4, -2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 5], [0, 0], [2, 4], [4, -2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2], [3, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2], [3, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [1, -1], [-2, 2], [2, -2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [1, -1], [-2, 2], [2, -2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [1, -1], [0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [1, -1], [0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[6, 2], [4, 4], [2, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[6, 2], [4, 4], [2, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [3, 2], [4, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [3, 2], [4, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 10], [10, 0], [5, 5], [15, 15]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 10], [10, 0], [5, 5], [15, 15]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 3], [3, 2], [4, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 3], [3, 2], [4, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [1, 1], [-2, -2], [2, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [1, 1], [-2, -2], [2, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [5, 5], [0, 0], [-5, -5], [-10, -10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [5, 5], [0, 0], [-5, -5], [-10, -10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [15, 15], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [15, 15], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1000000000, 1000000000], [1000000000, -1000000000], [0, 0], [1, 1], [2, 2], [3, 3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1000000000, 1000000000], [1000000000, -1000000000], [0, 0], [1, 1], [2, 2], [3, 3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-2, 3], [1, 1], [0, 0], [-1, -1], [2, 2], [3, -3], [4, 4], [-4, -4], [5, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-2, 3], [1, 1], [0, 0], [-1, -1], [2, 2], [3, -3], [4, 4], [-4, -4], [5, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -3], [-2, -1], [-3, -2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -3], [-2, -1], [-3, -2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [8, 5], [8, 6], [8, 7]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [8, 5], [8, 6], [8, 7]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [9, 10], [9, 9], [9, 8], [9, 7], [9, 6], [8, 10], [8, 9], [8, 8], [8, 7], [8, 6], [7, 10], [7, 9], [7, 8], [7, 7], [7, 6], [6, 10], [6, 9], [6, 8], [6, 7], [6, 6]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [9, 10], [9, 9], [9, 8], [9, 7], [9, 6], [8, 10], [8, 9], [8, 8], [8, 7], [8, 6], [7, 10], [7, 9], [7, 8], [7, 7], [7, 6], [6, 10], [6, 9], [6, 8], [6, 7], [6, 6]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [100, 100], [50, 50], [75, 25], [25, 75], [125, 125], [25, 25], [75, 75], [100, 50], [50, 100]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [100, 100], [50, 50], [75, 25], [25, 75], [125, 125], [25, 25], [75, 75], [100, 50], [50, 100]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [0, 0], [1, -1], [1, 1], [-1, -1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [0, 0], [1, -1], [1, 1], [-1, -1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 1], [1, 5], [3, 3], [4, 2], [2, 4], [6, 0], [0, 6], [7, 1], [1, 7]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 1], [1, 5], [3, 3], [4, 2], [2, 4], [6, 0], [0, 6], [7, 1], [1, 7]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [3, 1], [3, 3], [3, 5], [3, 7], [3, 9]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [3, 1], [3, 3], [3, 5], [3, 7], [3, 9]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1000000000, 1000000000], [500000000, 500000000], [0, 0], [-500000000, -500000000], [-1000000000, -1000000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1000000000, 1000000000], [500000000, 500000000], [0, 0], [-500000000, -500000000], [-1000000000, -1000000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [5, 4], [4, 5], [4, 4], [7, 7], [7, 6], [6, 7]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [5, 4], [4, 5], [4, 4], [7, 7], [7, 6], [6, 7]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [1, 1], [2, 2], [-2, -2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [1, 1], [2, 2], [-2, -2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -2], [-2, -3], [-1, -3], [-3, -1], [-3, -2], [0, 0], [0, -1], [0, -2], [0, -3]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -2], [-2, -3], [-1, -3], [-3, -1], [-3, -2], [0, 0], [0, -1], [0, -2], [0, -3]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1000000000, 1000000000], [1, 1], [500000000, 500000000], [2, 2], [999999999, 999999999]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1000000000, 1000000000], [1, 1], [500000000, 500000000], [2, 2], [999999999, 999999999]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 9], [10, 8], [9, 9], [8, 8], [9, 8], [8, 9]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 9], [10, 8], [9, 9], [8, 8], [9, 8], [8, 9]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 3], [3, 2], [4, 1], [5, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 3], [3, 2], [4, 1], [5, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [-1, -1], [1, -1], [1, 1], [0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [2, 2], [-2, -2], [2, -2], [-2, 2], [3, 3], [-3, -3], [3, -3], [-3, 3]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [-1, -1], [1, -1], [1, 1], [0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [2, 2], [-2, -2], [2, -2], [-2, 2], [3, 3], [-3, -3], [3, -3], [-3, 3]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2], [3, 10], [4, 9], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3], [4, 10], [5, 9], [6, 8], [7, 7], [8, 6], [9, 5], [10, 4], [5, 10], [6, 9], [7, 8], [8, 7], [9, 6], [10, 5], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6], [7, 10], [8, 9], [9, 8], [10, 7], [8, 10], [9, 9], [10, 8], [9, 10], [10, 9], [10, 10]]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2], [3, 10], [4, 9], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3], [4, 10], [5, 9], [6, 8], [7, 7], [8, 6], [9, 5], [10, 4], [5, 10], [6, 9], [7, 8], [8, 7], [9, 6], [10, 5], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6], [7, 10], [8, 9], [9, 8], [10, 7], [8, 10], [9, 9], [10, 8], [9, 10], [10, 9], [10, 10]]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [3, 0], [3, 1], [3, 2]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [3, 0], [3, 1], [3, 2]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100, 100], [0, 0], [100, -100], [50, 50], [-50, -50], [75, 25], [25, 75], [25, 25], [75, 75], [-25, -25], [-75, -75]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100, 100], [0, 0], [100, -100], [50, 50], [-50, -50], [75, 25], [25, 75], [25, 25], [75, 75], [-25, -25], [-75, -75]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 1], [3, 2], [2, 3], [1, 4]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 1], [3, 2], [2, 3], [1, 4]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [4, 5], [3, 5], [2, 5], [1, 5], [5, 0]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [4, 5], [3, 5], [2, 5], [1, 5], [5, 0]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [5, 5], [0, 0], [3, 3], [2, 2], [1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [5, 5], [0, 0], [3, 3], [2, 2], [1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1000000000, -1000000000], [-1000000000, 1000000000], [0, 0], [500000000, 500000000], [-500000000, -500000000]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1000000000, -1000000000], [-1000000000, 1000000000], [0, 0], [500000000, 500000000], [-500000000, -500000000]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -2], [-2, -1], [-1, -3], [-3, -1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -2], [-2, -1], [-1, -3], [-3, -1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 5], [3, 5], [1, 4], [2, 4], [3, 4], [1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 5], [3, 5], [1, 4], [2, 4], [3, 4], [1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [10, 1], [3, 3], [5, 5], [2, 8], [8, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [10, 1], [3, 3], [5, 5], [2, 8], [8, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [10, 19], [10, 18], [9, 20], [9, 19], [9, 18], [8, 20], [8, 19], [8, 18], [7, 20], [7, 19], [7, 18]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [10, 19], [10, 18], [9, 20], [9, 19], [9, 18], [8, 20], [8, 19], [8, 18], [7, 20], [7, 19], [7, 18]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-1, 9], [-2, 8], [-3, 7], [-4, 6], [-5, 5], [-6, 4], [-7, 3], [-8, 2], [-9, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-1, 9], [-2, 8], [-3, 7], [-4, 6], [-5, 5], [-6, 4], [-7, 3], [-8, 2], [-9, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [2, 1], [3, 3], [3, 2], [3, 1], [4, 4], [4, 3], [4, 2], [4, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [2, 1], [3, 3], [3, 2], [3, 1], [4, 4], [4, 3], [4, 2], [4, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1000000000, 1000000000], [999999999, 999999999], [999999998, 999999998], [999999997, 999999997], [999999996, 999999996], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1000000000, 1000000000], [999999999, 999999999], [999999998, 999999998], [999999997, 999999997], [999999996, 999999996], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 4], [2, 4], [3, 4]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 4], [2, 4], [3, 4]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [5, 1], [3, 3], [2, 4], [4, 2], [1, 3], [3, 1], [2, 3], [3, 2], [4, 1], [5, 2], [2, 5]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [5, 1], [3, 3], [2, 4], [4, 2], [1, 3], [3, 1], [2, 3], [3, 2], [4, 1], [5, 2], [2, 5]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [5, 1], [3, 3], [2, 4], [4, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [5, 1], [3, 3], [2, 4], [4, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [3, 7], [5, 9], [2, 3], [4, 6], [6, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [3, 7], [5, 9], [2, 3], [4, 6], [6, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5], [7, 3], [3, 7]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5], [7, 3], [3, 7]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [10, 2], [10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [10, 2], [10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [1, 4], [4, 1], [2, 4], [4, 2], [3, 3]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [1, 4], [4, 1], [2, 4], [4, 2], [3, 3]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [3, 9], [5, 8], [7, 7], [9, 6], [11, 5], [13, 4], [15, 3], [17, 2], [19, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [3, 9], [5, 8], [7, 7], [9, 6], [11, 5], [13, 4], [15, 3], [17, 2], [19, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5], [3, 3], [-3, -3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5], [3, 3], [-3, -3]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 10], [10, 5], [10, 10], [7, 7], [8, 8], [3, 3], [3, 8], [8, 3]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 10], [10, 5], [10, 10], [7, 7], [8, 8], [3, 3], [3, 8], [8, 3]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, 5], [0, 0], [5, -5], [10, -10], [5, 0], [0, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, 5], [0, 0], [5, -5], [10, -10], [5, 0], [0, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1000000000, 1000000000], [-1000000000, -1000000000], [0, 0], [500000000, 500000000], [-500000000, -500000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1000000000, 1000000000], [-1000000000, -1000000000], [0, 0], [500000000, 500000000], [-500000000, -500000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, -10], [10, 10], [0, 0], [5, 5], [-5, -5], [5, -5], [-5, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, -10], [10, 10], [0, 0], [5, 5], [-5, -5], [5, -5], [-5, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 10], [10, 5], [15, 0], [20, 5], [25, 10], [30, 5], [35, 0], [40, 5], [45, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 10], [10, 5], [15, 0], [20, 5], [25, 10], [30, 5], [35, 0], [40, 5], [45, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100, -100], [-200, -200], [-300, -300], [-400, -400], [-500, -500], [-600, -600], [-700, -700], [-800, -800], [-900, -900]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100, -100], [-200, -200], [-300, -300], [-400, -400], [-500, -500], [-600, -600], [-700, -700], [-800, -800], [-900, -900]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [11, 11], [12, 12], [9, 12], [8, 13], [7, 14], [6, 15], [5, 16], [4, 17], [3, 18], [2, 19], [1, 20]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [11, 11], [12, 12], [9, 12], [8, 13], [7, 14], [6, 15], [5, 16], [4, 17], [3, 18], [2, 19], [1, 20]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]) == 40: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(points = [[3, 1], [1, 3], [1, 1]]) == 2
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [1, 3], [2, 1], [1, 2]]) == 6
    assert candidate(points = [[1, 1], [2, 2], [1, 2], [2, 1]]) == 4
    assert candidate(points = [[-1, 5], [0, 0], [2, 4], [4, -2]]) == 4
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 4
    assert candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2], [3, 1]]) == 5
    assert candidate(points = [[-1, 1], [1, -1], [-2, 2], [2, -2]]) == 3
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]]) == 0
    assert candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7]]) == 3
    assert candidate(points = [[1, 1], [2, 2], [3, 3]]) == 0
    assert candidate(points = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1]]) == 4
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 0
    assert candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5]]) == 6
    assert candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2]]) == 4
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3]]) == 0
    assert candidate(points = [[-1, 1], [1, -1], [0, 0]]) == 2
    assert candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2]]) == 0
    assert candidate(points = [[6, 2], [4, 4], [2, 6]]) == 2
    assert candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4]]) == 3
    assert candidate(points = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]) == 4
    assert candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2]]) == 3
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]]) == 0
    assert candidate(points = [[1, 1], [2, 3], [3, 2], [4, 4]]) == 1
    assert candidate(points = [[0, 10], [10, 0], [5, 5], [15, 15]]) == 2
    assert candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5]]) == 4
    assert candidate(points = [[1, 5], [2, 3], [3, 2], [4, 1]]) == 3
    assert candidate(points = [[-1, -1], [1, 1], [-2, -2], [2, 2]]) == 0
    assert candidate(points = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 4
    assert candidate(points = [[10, 10], [5, 5], [0, 0], [-5, -5], [-10, -10]]) == 0
    assert candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]) == 4
    assert candidate(points = [[10, 10], [20, 20], [15, 15], [5, 5]]) == 0
    assert candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5]]) == 3
    assert candidate(points = [[-1000000000, 1000000000], [1000000000, -1000000000], [0, 0], [1, 1], [2, 2], [3, 3]]) == 8
    assert candidate(points = [[-2, 3], [1, 1], [0, 0], [-1, -1], [2, 2], [3, -3], [4, 4], [-4, -4], [5, 5]]) == 8
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -3], [-2, -1], [-3, -2]]) == 7
    assert candidate(points = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [8, 5], [8, 6], [8, 7]]) == 17
    assert candidate(points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0
    assert candidate(points = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [9, 10], [9, 9], [9, 8], [9, 7], [9, 6], [8, 10], [8, 9], [8, 8], [8, 7], [8, 6], [7, 10], [7, 9], [7, 8], [7, 7], [7, 6], [6, 10], [6, 9], [6, 8], [6, 7], [6, 6]]) == 40
    assert candidate(points = [[0, 0], [100, 100], [50, 50], [75, 25], [25, 75], [125, 125], [25, 25], [75, 75], [100, 50], [50, 100]]) == 12
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 13
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 9
    assert candidate(points = [[-1, 1], [0, 0], [1, -1], [1, 1], [-1, -1]]) == 6
    assert candidate(points = [[5, 1], [1, 5], [3, 3], [4, 2], [2, 4], [6, 0], [0, 6], [7, 1], [1, 7]]) == 8
    assert candidate(points = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [3, 1], [3, 3], [3, 5], [3, 7], [3, 9]]) == 13
    assert candidate(points = [[1000000000, 1000000000], [500000000, 500000000], [0, 0], [-500000000, -500000000], [-1000000000, -1000000000]]) == 0
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]) == 31
    assert candidate(points = [[5, 5], [5, 6], [6, 5], [6, 6], [5, 4], [4, 5], [4, 4], [7, 7], [7, 6], [6, 7]]) == 12
    assert candidate(points = [[-1, -1], [1, 1], [2, 2], [-2, -2], [0, 0]]) == 0
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 13
    assert candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4]]) == 12
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -2], [-2, -3], [-1, -3], [-3, -1], [-3, -2], [0, 0], [0, -1], [0, -2], [0, -3]]) == 16
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
    assert candidate(points = [[1000000000, 1000000000], [1, 1], [500000000, 500000000], [2, 2], [999999999, 999999999]]) == 0
    assert candidate(points = [[10, 10], [10, 9], [10, 8], [9, 9], [8, 8], [9, 8], [8, 9]]) == 8
    assert candidate(points = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]]) == 0
    assert candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9
    assert candidate(points = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1]]) == 9
    assert candidate(points = [[1, 5], [2, 3], [3, 2], [4, 1], [5, 4]]) == 4
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]) == 12
    assert candidate(points = [[-1, 1], [-1, -1], [1, -1], [1, 1], [0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [2, 2], [-2, -2], [2, -2], [-2, 2], [3, 3], [-3, -3], [3, -3], [-3, 3]]) == 24
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 31
    assert candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2], [3, 10], [4, 9], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3], [4, 10], [5, 9], [6, 8], [7, 7], [8, 6], [9, 5], [10, 4], [5, 10], [6, 9], [7, 8], [8, 7], [9, 6], [10, 5], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6], [7, 10], [8, 9], [9, 8], [10, 7], [8, 10], [9, 9], [10, 8], [9, 10], [10, 9], [10, 10]]) == 108
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [3, 0], [3, 1], [3, 2]]) == 17
    assert candidate(points = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8]]) == 22
    assert candidate(points = [[-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 0
    assert candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 26
    assert candidate(points = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]]) == 9
    assert candidate(points = [[-100, 100], [0, 0], [100, -100], [50, 50], [-50, -50], [75, 25], [25, 75], [25, 25], [75, 75], [-25, -25], [-75, -75]]) == 16
    assert candidate(points = [[5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 1], [3, 2], [2, 3], [1, 4]]) == 22
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5]]) == 31
    assert candidate(points = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]) == 5
    assert candidate(points = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [4, 5], [3, 5], [2, 5], [1, 5], [5, 0]]) == 9
    assert candidate(points = [[-5, -5], [5, 5], [0, 0], [3, 3], [2, 2], [1, 1]]) == 0
    assert candidate(points = [[1000000000, -1000000000], [-1000000000, 1000000000], [0, 0], [500000000, 500000000], [-500000000, -500000000]]) == 6
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]) == 0
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-1, -2], [-2, -1], [-1, -3], [-3, -1]]) == 8
    assert candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == 8
    assert candidate(points = [[1, 5], [2, 5], [3, 5], [1, 4], [2, 4], [3, 4], [1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]) == 22
    assert candidate(points = [[1, 10], [10, 1], [3, 3], [5, 5], [2, 8], [8, 2]]) == 6
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]) == 24
    assert candidate(points = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 8
    assert candidate(points = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900]]) == 0
    assert candidate(points = [[10, 20], [10, 19], [10, 18], [9, 20], [9, 19], [9, 18], [8, 20], [8, 19], [8, 18], [7, 20], [7, 19], [7, 18]]) == 17
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 0
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 25
    assert candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-1, 9], [-2, 8], [-3, 7], [-4, 6], [-5, 5], [-6, 4], [-7, 3], [-8, 2], [-9, 1]]) == 25
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 0
    assert candidate(points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 9
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 13
    assert candidate(points = [[1, 1], [2, 2], [2, 1], [3, 3], [3, 2], [3, 1], [4, 4], [4, 3], [4, 2], [4, 1]]) == 12
    assert candidate(points = [[1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1]]) == 13
    assert candidate(points = [[1000000000, 1000000000], [999999999, 999999999], [999999998, 999999998], [999999997, 999999997], [999999996, 999999996], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 0
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]]) == 0
    assert candidate(points = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 4], [2, 4], [3, 4]]) == 17
    assert candidate(points = [[1, 5], [5, 1], [3, 3], [2, 4], [4, 2], [1, 3], [3, 1], [2, 3], [3, 2], [4, 1], [5, 2], [2, 5]]) == 14
    assert candidate(points = [[1, 5], [5, 1], [3, 3], [2, 4], [4, 2]]) == 4
    assert candidate(points = [[1, 5], [3, 7], [5, 9], [2, 3], [4, 6], [6, 8]]) == 3
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
    assert candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5], [7, 3], [3, 7]]) == 8
    assert candidate(points = [[10, 10], [10, 9], [10, 8], [10, 7], [10, 6], [10, 5], [10, 4], [10, 3], [10, 2], [10, 1]]) == 9
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9
    assert candidate(points = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [1, 4], [4, 1], [2, 4], [4, 2], [3, 3]]) == 15
    assert candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]]) == 5
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9
    assert candidate(points = [[1, 10], [3, 9], [5, 8], [7, 7], [9, 6], [11, 5], [13, 4], [15, 3], [17, 2], [19, 1]]) == 9
    assert candidate(points = [[-10, 10], [10, -10], [0, 0], [5, 5], [-5, -5], [3, 3], [-3, -3]]) == 10
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 0
    assert candidate(points = [[5, 5], [5, 10], [10, 5], [10, 10], [7, 7], [8, 8], [3, 3], [3, 8], [8, 3]]) == 16
    assert candidate(points = [[-5, 5], [0, 0], [5, -5], [10, -10], [5, 0], [0, 5]]) == 5
    assert candidate(points = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]) == 9
    assert candidate(points = [[1000000000, 1000000000], [-1000000000, -1000000000], [0, 0], [500000000, 500000000], [-500000000, -500000000]]) == 0
    assert candidate(points = [[-10, -10], [10, 10], [0, 0], [5, 5], [-5, -5], [5, -5], [-5, 5]]) == 6
    assert candidate(points = [[5, 10], [10, 5], [15, 0], [20, 5], [25, 10], [30, 5], [35, 0], [40, 5], [45, 10]]) == 10
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]) == 40
    assert candidate(points = [[-100, -100], [-200, -200], [-300, -300], [-400, -400], [-500, -500], [-600, -600], [-700, -700], [-800, -800], [-900, -900]]) == 0
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 27
    assert candidate(points = [[10, 10], [11, 11], [12, 12], [9, 12], [8, 13], [7, 14], [6, 15], [5, 16], [4, 17], [3, 18], [2, 19], [1, 20]]) == 11
    assert candidate(points = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]) == 40


