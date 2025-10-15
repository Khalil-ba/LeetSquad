def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 6,lights = [[1, 2], [3, 2], [5, 2]],requirement = [1, 2, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,lights = [[1, 2], [3, 2], [5, 2]],requirement = [1, 2, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,lights = [[0, 1]],requirement = [2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,lights = [[0, 1]],requirement = [2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],requirement = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],requirement = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,lights = [[1, 0], [1, 1], [1, 2]],requirement = [0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,lights = [[1, 0], [1, 1], [1, 2]],requirement = [0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[2, 3], [5, 2], [7, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[2, 3], [5, 2], [7, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,lights = [[0, 0], [1, 1], [2, 2]],requirement = [0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,lights = [[0, 0], [1, 1], [2, 2]],requirement = [0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,lights = [[0, 1], [2, 1], [3, 2]],requirement = [0, 2, 1, 4, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,lights = [[0, 1], [2, 1], [3, 2]],requirement = [0, 2, 1, 4, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 5], [5, 5], [9, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 5], [5, 5], [9, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,lights = [[1, 0], [1, 1], [1, 2]],requirement = [1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,lights = [[1, 0], [1, 1], [1, 2]],requirement = [1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,lights = [[1, 1], [2, 2], [3, 3]],requirement = [1, 2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,lights = [[1, 1], [2, 2], [3, 3]],requirement = [1, 2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 5], [5, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 5], [5, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 2], [5, 3], [8, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 2], [5, 3], [8, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,lights = [[1, 1]],requirement = [0, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,lights = [[1, 1]],requirement = [0, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,lights = [[0, 0], [1, 1], [2, 0]],requirement = [0, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,lights = [[0, 0], [1, 1], [2, 0]],requirement = [0, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,lights = [[2, 3], [5, 4], [8, 2], [12, 5], [15, 3]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,lights = [[2, 3], [5, 4], [8, 2], [12, 5], [15, 3]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,lights = [[2, 5], [5, 5], [10, 3], [15, 2], [18, 1]],requirement = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,lights = [[2, 5], [5, 5], [10, 3], [15, 2], [18, 1]],requirement = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,lights = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,lights = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,lights = [[5, 6], [8, 4], [12, 5], [18, 3], [22, 2]],requirement = [0, 0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,lights = [[5, 6], [8, 4], [12, 5], [18, 3], [22, 2]],requirement = [0, 0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,lights = [[10, 5], [20, 10], [30, 15], [40, 5], [50, 10], [60, 15]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,lights = [[10, 5], [20, 10], [30, 15], [40, 5], [50, 10], [60, 15]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,lights = [[0, 7], [3, 2], [7, 3], [10, 4], [12, 1]],requirement = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,lights = [[0, 7], [3, 2], [7, 3], [10, 4], [12, 1]],requirement = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],requirement = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],requirement = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,lights = [[10, 15], [20, 20], [30, 10], [40, 5], [50, 3], [60, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,lights = [[10, 15], [20, 20], [30, 10], [40, 5], [50, 3], [60, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],requirement = [0, 1, 2, 3, 4, 3, 2, 1, 0, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],requirement = [0, 1, 2, 3, 4, 3, 2, 1, 0, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,lights = [[0, 10], [5, 10], [10, 10], [15, 10], [20, 10]],requirement = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,lights = [[0, 10], [5, 10], [10, 10], [15, 10], [20, 10]],requirement = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,lights = [[0, 5], [15, 5], [10, 3]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,lights = [[0, 5], [15, 5], [10, 3]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],requirement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],requirement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,lights = [[0, 4], [3, 3], [7, 2], [10, 1], [12, 2]],requirement = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,lights = [[0, 4], [3, 3], [7, 2], [10, 1], [12, 2]],requirement = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],requirement = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],requirement = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,lights = [[5, 15], [15, 10], [25, 5], [35, 2], [40, 1]],requirement = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,lights = [[5, 15], [15, 10], [25, 5], [35, 2], [40, 1]],requirement = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]],requirement = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]],requirement = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,lights = [[1, 1], [5, 5], [10, 5], [15, 5]],requirement = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,lights = [[1, 1], [5, 5], [10, 5], [15, 5]],requirement = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,lights = [[5, 5], [10, 5], [15, 5], [20, 5]],requirement = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,lights = [[5, 5], [10, 5], [15, 5], [20, 5]],requirement = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,lights = [[0, 24], [25, 24], [12, 12], [37, 12]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,lights = [[0, 24], [25, 24], [12, 12], [37, 12]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,lights = [[0, 2], [4, 3], [8, 4], [12, 5], [16, 6], [20, 7]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,lights = [[0, 2], [4, 3], [8, 4], [12, 5], [16, 6], [20, 7]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,lights = [[2, 3], [5, 5], [10, 4], [15, 2]],requirement = [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,lights = [[2, 3], [5, 5], [10, 4], [15, 2]],requirement = [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,lights = [[2, 4], [5, 6], [11, 2], [7, 3]],requirement = [0, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 0]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,lights = [[2, 4], [5, 6], [11, 2], [7, 3]],requirement = [0, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 0]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,lights = [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,lights = [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],requirement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],requirement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,lights = [[0, 5], [5, 5], [10, 5]],requirement = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,lights = [[0, 5], [5, 5], [10, 5]],requirement = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,lights = [[0, 5], [5, 5], [10, 5], [15, 5], [20, 5], [25, 5], [30, 5], [35, 5], [40, 5], [45, 5]],requirement = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,lights = [[0, 5], [5, 5], [10, 5], [15, 5], [20, 5], [25, 5], [30, 5], [35, 5], [40, 5], [45, 5]],requirement = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]) == 47: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 6,lights = [[1, 2], [3, 2], [5, 2]],requirement = [1, 2, 3, 2, 1, 0]) == 5
    assert candidate(n = 1,lights = [[0, 1]],requirement = [2]) == 0
    assert candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],requirement = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 10
    assert candidate(n = 3,lights = [[1, 0], [1, 1], [1, 2]],requirement = [0, 0, 0]) == 3
    assert candidate(n = 10,lights = [[2, 3], [5, 2], [7, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(n = 3,lights = [[0, 0], [1, 1], [2, 2]],requirement = [0, 0, 0]) == 3
    assert candidate(n = 5,lights = [[0, 1], [2, 1], [3, 2]],requirement = [0, 2, 1, 4, 1]) == 4
    assert candidate(n = 10,lights = [[0, 5], [5, 5], [9, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(n = 3,lights = [[1, 0], [1, 1], [1, 2]],requirement = [1, 2, 1]) == 3
    assert candidate(n = 6,lights = [[1, 1], [2, 2], [3, 3]],requirement = [1, 2, 3, 4, 5, 6]) == 3
    assert candidate(n = 10,lights = [[0, 5], [5, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(n = 10,lights = [[0, 2], [5, 3], [8, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(n = 3,lights = [[1, 1]],requirement = [0, 1, 0]) == 3
    assert candidate(n = 3,lights = [[0, 0], [1, 1], [2, 0]],requirement = [0, 0, 0]) == 3
    assert candidate(n = 20,lights = [[2, 3], [5, 4], [8, 2], [12, 5], [15, 3]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(n = 20,lights = [[2, 5], [5, 5], [10, 3], [15, 2], [18, 1]],requirement = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(n = 100,lights = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(n = 25,lights = [[5, 6], [8, 4], [12, 5], [18, 3], [22, 2]],requirement = [0, 0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0, 0]) == 15
    assert candidate(n = 75,lights = [[10, 5], [20, 10], [30, 15], [40, 5], [50, 10], [60, 15]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 57
    assert candidate(n = 15,lights = [[0, 7], [3, 2], [7, 3], [10, 4], [12, 1]],requirement = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]) == 15
    assert candidate(n = 10,lights = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],requirement = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(n = 75,lights = [[10, 15], [20, 20], [30, 10], [40, 5], [50, 3], [60, 1]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 56
    assert candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],requirement = [0, 1, 2, 3, 4, 3, 2, 1, 0, 0]) == 10
    assert candidate(n = 30,lights = [[0, 10], [5, 10], [10, 10], [15, 10], [20, 10]],requirement = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 26
    assert candidate(n = 20,lights = [[0, 5], [15, 5], [10, 3]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(n = 10,lights = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],requirement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(n = 15,lights = [[0, 4], [3, 3], [7, 2], [10, 1], [12, 2]],requirement = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]) == 12
    assert candidate(n = 10,lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],requirement = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(n = 50,lights = [[5, 15], [15, 10], [25, 5], [35, 2], [40, 1]],requirement = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 44
    assert candidate(n = 20,lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]],requirement = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 20
    assert candidate(n = 20,lights = [[1, 1], [5, 5], [10, 5], [15, 5]],requirement = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0]) == 20
    assert candidate(n = 30,lights = [[5, 5], [10, 5], [15, 5], [20, 5]],requirement = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == 28
    assert candidate(n = 50,lights = [[0, 24], [25, 24], [12, 12], [37, 12]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(n = 25,lights = [[0, 2], [4, 3], [8, 4], [12, 5], [16, 6], [20, 7]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
    assert candidate(n = 20,lights = [[2, 3], [5, 5], [10, 4], [15, 2]],requirement = [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 13
    assert candidate(n = 15,lights = [[2, 4], [5, 6], [11, 2], [7, 3]],requirement = [0, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 0]) == 14
    assert candidate(n = 100,lights = [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5]],requirement = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 91
    assert candidate(n = 10,lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],requirement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
    assert candidate(n = 15,lights = [[0, 5], [5, 5], [10, 5]],requirement = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 11
    assert candidate(n = 50,lights = [[0, 5], [5, 5], [10, 5], [15, 5], [20, 5], [25, 5], [30, 5], [35, 5], [40, 5], [45, 5]],requirement = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]) == 47


