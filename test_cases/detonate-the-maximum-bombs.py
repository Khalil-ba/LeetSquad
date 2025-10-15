def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 100], [1, 1, 50], [1, 1, 25]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 100], [1, 1, 50], [1, 1, 25]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [10, 10, 10], [5, 5, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [10, 10, 10], [5, 5, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [10, 10, 1], [5, 5, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [10, 10, 1], [5, 5, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [10, 10, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [10, 10, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 100], [50, 50, 100], [100, 100, 100]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 100], [50, 50, 100], [100, 100, 100]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 1], [101, 101, 1], [102, 102, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 1], [101, 101, 1], [102, 102, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[2, 1, 3], [6, 1, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[2, 1, 3], [6, 1, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 3], [2, 2, 3], [3, 3, 3], [4, 4, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 3], [2, 2, 3], [3, 3, 3], [4, 4, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 3], [6, 6, 1], [7, 7, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 3], [6, 6, 1], [7, 7, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 10], [20, 20, 10], [30, 30, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 10], [20, 20, 10], [30, 30, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1], [60, 10, 1], [70, 10, 1], [80, 10, 1], [90, 10, 1], [100, 10, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1], [60, 10, 1], [70, 10, 1], [80, 10, 1], [90, 10, 1], [100, 10, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 10], [100, 110, 10], [100, 120, 10], [110, 100, 10], [110, 110, 10], [110, 120, 10], [120, 100, 10], [120, 110, 10], [120, 120, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 10], [100, 110, 10], [100, 120, 10], [110, 100, 10], [110, 110, 10], [110, 120, 10], [120, 100, 10], [120, 110, 10], [120, 120, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[50, 50, 10], [60, 60, 20], [70, 70, 30], [80, 80, 40], [90, 90, 50]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[50, 50, 10], [60, 60, 20], [70, 70, 30], [80, 80, 40], [90, 90, 50]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 3], [10, 13, 3], [13, 10, 3], [13, 13, 3], [16, 16, 3], [16, 19, 3], [19, 16, 3], [19, 19, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 3], [10, 13, 3], [13, 10, 3], [13, 13, 3], [16, 16, 3], [16, 19, 3], [19, 16, 3], [19, 19, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [1, 10, 10], [10, 1, 10], [10, 10, 10], [15, 15, 15], [15, 5, 15], [5, 15, 15], [20, 20, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [1, 10, 10], [10, 1, 10], [10, 10, 10], [15, 15, 15], [15, 5, 15], [5, 15, 15], [20, 20, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1], [7, 0, 1], [8, 0, 1], [9, 0, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1], [7, 0, 1], [8, 0, 1], [9, 0, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[50, 50, 5], [55, 50, 5], [60, 50, 5], [65, 50, 5], [70, 50, 5], [75, 50, 5], [80, 50, 5], [85, 50, 5], [90, 50, 5], [95, 50, 5], [100, 50, 5], [105, 50, 5], [110, 50, 5], [115, 50, 5], [120, 50, 5], [125, 50, 5], [130, 50, 5], [135, 50, 5], [140, 50, 5], [145, 50, 5]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[50, 50, 5], [55, 50, 5], [60, 50, 5], [65, 50, 5], [70, 50, 5], [75, 50, 5], [80, 50, 5], [85, 50, 5], [90, 50, 5], [95, 50, 5], [100, 50, 5], [105, 50, 5], [110, 50, 5], [115, 50, 5], [120, 50, 5], [125, 50, 5], [130, 50, 5], [135, 50, 5], [140, 50, 5], [145, 50, 5]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 10], [110, 100, 10], [120, 100, 10], [130, 100, 10], [140, 100, 10], [150, 100, 10], [160, 100, 10], [170, 100, 10], [180, 100, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 10], [110, 100, 10], [120, 100, 10], [130, 100, 10], [140, 100, 10], [150, 100, 10], [160, 100, 10], [170, 100, 10], [180, 100, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[50, 50, 5], [60, 50, 5], [70, 50, 5], [80, 50, 5], [50, 60, 5], [50, 70, 5], [50, 80, 5], [50, 90, 5], [50, 100, 5], [60, 60, 15]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[50, 50, 5], [60, 50, 5], [70, 50, 5], [80, 50, 5], [50, 60, 5], [50, 70, 5], [50, 80, 5], [50, 90, 5], [50, 100, 5], [60, 60, 15]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 50], [200, 100, 50], [100, 200, 50], [200, 200, 50], [150, 150, 100]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 50], [200, 100, 50], [100, 200, 50], [200, 200, 50], [150, 150, 100]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 1], [20, 20, 1], [30, 30, 1], [40, 40, 1], [50, 50, 1], [60, 60, 1], [70, 70, 1], [80, 80, 1], [90, 90, 1], [100, 100, 100]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 1], [20, 20, 1], [30, 30, 1], [40, 40, 1], [50, 50, 1], [60, 60, 1], [70, 70, 1], [80, 80, 1], [90, 90, 1], [100, 100, 100]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 5], [5, 15, 5], [15, 5, 5], [15, 15, 5], [10, 10, 20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 5], [5, 15, 5], [15, 5, 5], [15, 15, 5], [10, 10, 20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [2, 2, 10], [3, 3, 2], [4, 4, 8], [5, 5, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [2, 2, 10], [3, 3, 2], [4, 4, 8], [5, 5, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 100], [1, 1, 100], [1, 1, 100], [1, 1, 100], [1, 1, 100]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 100], [1, 1, 100], [1, 1, 100], [1, 1, 100], [1, 1, 100]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 20], [5, 0, 15], [10, 0, 10], [15, 0, 5], [20, 0, 1], [25, 0, 20], [30, 0, 15], [35, 0, 10], [40, 0, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 20], [5, 0, 15], [10, 0, 10], [15, 0, 5], [20, 0, 1], [25, 0, 20], [30, 0, 15], [35, 0, 10], [40, 0, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 1], [2, 0, 1], [0, 2, 1], [2, 2, 1], [1, 1, 1.5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 1], [2, 0, 1], [0, 2, 1], [2, 2, 1], [1, 1, 1.5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[50, 50, 15], [60, 50, 20], [70, 50, 10], [50, 60, 25], [50, 70, 12], [50, 80, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[50, 50, 15], [60, 50, 20], [70, 50, 10], [50, 60, 25], [50, 70, 12], [50, 80, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [10, 0, 20], [20, 0, 30], [30, 0, 40], [40, 0, 50], [50, 0, 60], [60, 0, 70], [70, 0, 80], [80, 0, 90]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [10, 0, 20], [20, 0, 30], [30, 0, 40], [40, 0, 50], [50, 0, 60], [60, 0, 70], [70, 0, 80], [80, 0, 90]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [10, 1, 10], [1, 10, 10], [10, 10, 10], [5, 5, 5], [15, 15, 15]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [10, 1, 10], [1, 10, 10], [10, 10, 10], [5, 5, 5], [15, 15, 15]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [20, 20, 10], [30, 30, 10], [40, 40, 10], [50, 50, 10], [60, 60, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [20, 20, 10], [30, 30, 10], [40, 40, 10], [50, 50, 10], [60, 60, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 50], [200, 200, 50], [300, 300, 50], [100, 200, 60], [200, 300, 70]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 50], [200, 200, 50], [300, 300, 50], [100, 200, 60], [200, 300, 70]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 1], [15, 15, 2], [20, 20, 3], [25, 25, 4], [30, 30, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 1], [15, 15, 2], [20, 20, 3], [25, 25, 4], [30, 30, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 1], [5, 6, 1], [5, 7, 1], [5, 8, 1], [5, 9, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 1], [5, 6, 1], [5, 7, 1], [5, 8, 1], [5, 9, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [2, 2, 20], [3, 3, 30], [4, 4, 40], [5, 5, 50], [6, 6, 60]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [2, 2, 20], [3, 3, 30], [4, 4, 40], [5, 5, 50], [6, 6, 60]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 20], [10, 5, 20], [15, 5, 20], [20, 5, 20], [25, 5, 20], [30, 5, 20], [35, 5, 20], [40, 5, 20], [45, 5, 20], [50, 5, 20]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 20], [10, 5, 20], [15, 5, 20], [20, 5, 20], [25, 5, 20], [30, 5, 20], [35, 5, 20], [40, 5, 20], [45, 5, 20], [50, 5, 20]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 100], [200, 200, 100], [400, 400, 100], [600, 600, 100], [800, 800, 100], [1000, 1000, 100], [1200, 1200, 100], [1400, 1400, 100], [1600, 1600, 100], [1800, 1800, 100]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 100], [200, 200, 100], [400, 400, 100], [600, 600, 100], [800, 800, 100], [1000, 1000, 100], [1200, 1200, 100], [1400, 1400, 100], [1600, 1600, 100], [1800, 1800, 100]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [20, 20, 10], [10, 10, 15], [30, 30, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [20, 20, 10], [10, 10, 15], [30, 30, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 15], [20, 20, 15], [30, 30, 15], [40, 40, 15], [50, 50, 15], [60, 60, 15], [70, 70, 15], [80, 80, 15], [90, 90, 15]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 15], [20, 20, 15], [30, 30, 15], [40, 40, 15], [50, 50, 15], [60, 60, 15], [70, 70, 15], [80, 80, 15], [90, 90, 15]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 15], [20, 20, 15], [30, 30, 15], [40, 40, 15], [50, 50, 15], [60, 60, 15], [70, 70, 15]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 15], [20, 20, 15], [30, 30, 15], [40, 40, 15], [50, 50, 15], [60, 60, 15], [70, 70, 15]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 100], [200, 100, 100], [300, 100, 100], [400, 100, 100], [500, 100, 100], [600, 100, 100], [700, 100, 100], [800, 100, 100], [900, 100, 100]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 100], [200, 100, 100], [300, 100, 100], [400, 100, 100], [500, 100, 100], [600, 100, 100], [700, 100, 100], [800, 100, 100], [900, 100, 100]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1], [7, 0, 1], [8, 0, 1], [9, 0, 1], [10, 0, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1], [7, 0, 1], [8, 0, 1], [9, 0, 1], [10, 0, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 10, 5], [20, 10, 5], [25, 10, 5], [30, 10, 5], [35, 10, 5], [40, 10, 5], [45, 10, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 10, 5], [20, 10, 5], [25, 10, 5], [30, 10, 5], [35, 10, 5], [40, 10, 5], [45, 10, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 100], [1, 101, 100], [101, 101, 100], [101, 1, 100], [51, 51, 100], [51, 1, 100], [1, 51, 100], [101, 51, 100], [51, 101, 100]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 100], [1, 101, 100], [101, 101, 100], [101, 1, 100], [51, 51, 100], [51, 1, 100], [1, 51, 100], [101, 51, 100], [51, 101, 100]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 2], [6, 6, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 2], [6, 6, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 20], [30, 30, 20], [50, 50, 20], [70, 70, 20], [90, 90, 20], [110, 110, 20], [130, 130, 20], [150, 150, 20], [170, 170, 20], [190, 190, 20], [210, 210, 20], [230, 230, 20], [250, 250, 20], [270, 270, 20], [290, 290, 20]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 20], [30, 30, 20], [50, 50, 20], [70, 70, 20], [90, 90, 20], [110, 110, 20], [130, 130, 20], [150, 150, 20], [170, 170, 20], [190, 190, 20], [210, 210, 20], [230, 230, 20], [250, 250, 20], [270, 270, 20], [290, 290, 20]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 2], [10, 5, 2], [15, 5, 2], [20, 5, 2], [25, 5, 2], [30, 5, 2], [35, 5, 2], [40, 5, 2], [45, 5, 2], [50, 5, 2], [55, 5, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 2], [10, 5, 2], [15, 5, 2], [20, 5, 2], [25, 5, 2], [30, 5, 2], [35, 5, 2], [40, 5, 2], [45, 5, 2], [50, 5, 2], [55, 5, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 15], [20, 20, 25], [30, 30, 35], [40, 40, 45], [50, 50, 55]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 15], [20, 20, 25], [30, 30, 35], [40, 40, 45], [50, 50, 55]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 100], [200, 200, 50], [300, 300, 25], [400, 400, 12.5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 100], [200, 200, 50], [300, 300, 25], [400, 400, 12.5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 10], [15, 5, 10], [5, 15, 10], [15, 15, 10], [10, 10, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 10], [15, 5, 10], [5, 15, 10], [15, 15, 10], [10, 10, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 2], [6, 6, 2], [7, 7, 2], [8, 8, 2], [9, 9, 2]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 2], [6, 6, 2], [7, 7, 2], [8, 8, 2], [9, 9, 2]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 25], [15, 10, 15], [10, 15, 20], [5, 10, 10], [10, 5, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 25], [15, 10, 15], [10, 15, 20], [5, 10, 10], [10, 5, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 3], [4, 4, 3], [7, 1, 3], [4, 7, 3], [10, 10, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 3], [4, 4, 3], [7, 1, 3], [4, 7, 3], [10, 10, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [1, 6, 5], [6, 1, 5], [6, 6, 5], [3, 3, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [1, 6, 5], [6, 1, 5], [6, 6, 5], [3, 3, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1000], [2, 2, 1000], [3, 3, 1000], [4, 4, 1000], [5, 5, 1000], [6, 6, 1000], [7, 7, 1000], [8, 8, 1000]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1000], [2, 2, 1000], [3, 3, 1000], [4, 4, 1000], [5, 5, 1000], [6, 6, 1000], [7, 7, 1000], [8, 8, 1000]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 50], [150, 100, 50], [200, 100, 50], [250, 100, 50], [300, 100, 50], [350, 100, 50], [400, 100, 50], [450, 100, 50]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 50], [150, 100, 50], [200, 100, 50], [250, 100, 50], [300, 100, 50], [350, 100, 50], [400, 100, 50], [450, 100, 50]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 5], [10, 0, 5], [5, 5, 5], [15, 5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 5], [10, 0, 5], [5, 5, 5], [15, 5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 10, 5], [10, 15, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 10, 5], [10, 15, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [15, 0, 10], [30, 0, 10], [22, 0, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [15, 0, 10], [30, 0, 10], [22, 0, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [20, 0, 10], [40, 0, 10], [60, 0, 10], [80, 0, 10], [100, 0, 10], [120, 0, 10], [140, 0, 10], [160, 0, 10], [180, 0, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [20, 0, 10], [40, 0, 10], [60, 0, 10], [80, 0, 10], [100, 0, 10], [120, 0, 10], [140, 0, 10], [160, 0, 10], [180, 0, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 5], [10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 5], [10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[50, 50, 50], [60, 60, 50], [70, 70, 50], [80, 80, 50], [90, 90, 50], [100, 100, 50]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[50, 50, 50], [60, 60, 50], [70, 70, 50], [80, 80, 50], [90, 90, 50], [100, 100, 50]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[50, 50, 50], [100, 100, 50], [150, 150, 50], [200, 200, 50], [250, 250, 50], [300, 300, 50], [350, 350, 50], [400, 400, 50], [450, 450, 50]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[50, 50, 50], [100, 100, 50], [150, 150, 50], [200, 200, 50], [250, 250, 50], [300, 300, 50], [350, 350, 50], [400, 400, 50], [450, 450, 50]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [30, 0, 10], [40, 0, 10], [50, 0, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [30, 0, 10], [40, 0, 10], [50, 0, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 15, 3], [20, 20, 4], [25, 25, 2], [30, 30, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 15, 3], [20, 20, 4], [25, 25, 2], [30, 30, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 15], [15, 15, 15], [20, 20, 15], [25, 25, 15], [30, 30, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 15], [15, 15, 15], [20, 20, 15], [25, 25, 15], [30, 30, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 100], [101, 101, 100], [201, 201, 100], [301, 301, 100], [401, 401, 100]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 100], [101, 101, 100], [201, 201, 100], [301, 301, 100], [401, 401, 100]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 3], [7, 5, 3], [9, 5, 3], [11, 5, 3], [13, 5, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 3], [7, 5, 3], [9, 5, 3], [11, 5, 3], [13, 5, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5], [5, 5, 5], [6, 6, 5], [7, 7, 5], [8, 8, 5], [9, 9, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5], [5, 5, 5], [6, 6, 5], [7, 7, 5], [8, 8, 5], [9, 9, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10000, 10000, 5000], [15000, 10000, 10000], [20000, 10000, 3000], [10000, 20000, 6000], [25000, 25000, 8000]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10000, 10000, 5000], [15000, 10000, 10000], [20000, 10000, 3000], [10000, 20000, 6000], [25000, 25000, 8000]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1000, 1000, 1000], [2000, 2000, 500], [3000, 3000, 250], [4000, 4000, 125]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1000, 1000, 1000], [2000, 2000, 500], [3000, 3000, 250], [4000, 4000, 125]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [30, 0, 10], [40, 0, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [30, 0, 10], [40, 0, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 50], [20, 20, 40], [30, 30, 30], [40, 40, 20], [50, 50, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 50], [20, 20, 40], [30, 30, 30], [40, 40, 20], [50, 50, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 10], [10, 10, 10], [15, 15, 10], [20, 20, 10], [25, 25, 10], [30, 30, 10], [35, 35, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 10], [10, 10, 10], [15, 15, 10], [20, 20, 10], [25, 25, 10], [30, 30, 10], [35, 35, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 10], [20, 20, 10], [30, 30, 10], [40, 40, 10], [50, 50, 10], [60, 60, 10], [70, 70, 10], [80, 80, 10], [90, 90, 10], [100, 100, 10], [110, 110, 10], [120, 120, 10], [130, 130, 10], [140, 140, 10], [150, 150, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 10], [20, 20, 10], [30, 30, 10], [40, 40, 10], [50, 50, 10], [60, 60, 10], [70, 70, 10], [80, 80, 10], [90, 90, 10], [100, 100, 10], [110, 110, 10], [120, 120, 10], [130, 130, 10], [140, 140, 10], [150, 150, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [10, 1, 5], [10, 10, 15], [20, 20, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [10, 1, 5], [10, 10, 15], [20, 20, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [10, 1, 5], [1, 10, 5], [5, 5, 2], [7, 7, 7]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [10, 1, 5], [1, 10, 5], [5, 5, 2], [7, 7, 7]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10000], [2, 2, 10000], [3, 3, 10000], [4, 4, 10000], [5, 5, 10000], [6, 6, 10000], [7, 7, 10000], [8, 8, 10000], [9, 9, 10000], [10, 10, 10000]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10000], [2, 2, 10000], [3, 3, 10000], [4, 4, 10000], [5, 5, 10000], [6, 6, 10000], [7, 7, 10000], [8, 8, 10000], [9, 9, 10000], [10, 10, 10000]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 1], [11, 11, 2], [12, 12, 3], [13, 13, 4], [14, 14, 5], [15, 15, 6], [16, 16, 7], [17, 17, 8], [18, 18, 9], [19, 19, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 1], [11, 11, 2], [12, 12, 3], [13, 13, 4], [14, 14, 5], [15, 15, 6], [16, 16, 7], [17, 17, 8], [18, 18, 9], [19, 19, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [15, 5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [15, 5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [11, 1, 10], [21, 1, 10], [1, 11, 10], [11, 11, 10], [21, 11, 10], [1, 21, 10], [11, 21, 10], [21, 21, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [11, 1, 10], [21, 1, 10], [1, 11, 10], [11, 11, 10], [21, 11, 10], [1, 21, 10], [11, 21, 10], [21, 21, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 10], [2, 1, 10], [3, 1, 10], [4, 1, 10], [5, 1, 10], [6, 1, 10], [7, 1, 10], [8, 1, 10], [9, 1, 10], [10, 1, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 10], [2, 1, 10], [3, 1, 10], [4, 1, 10], [5, 1, 10], [6, 1, 10], [7, 1, 10], [8, 1, 10], [9, 1, 10], [10, 1, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5], [5, 5, 5], [6, 6, 5], [7, 7, 5], [8, 8, 5], [9, 9, 5], [10, 10, 5], [11, 11, 5], [12, 12, 5], [13, 13, 5], [14, 14, 5], [15, 15, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5], [5, 5, 5], [6, 6, 5], [7, 7, 5], [8, 8, 5], [9, 9, 5], [10, 10, 5], [11, 11, 5], [12, 12, 5], [13, 13, 5], [14, 14, 5], [15, 15, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 1], [1, 2, 2], [2, 4, 3], [3, 6, 4], [4, 8, 5], [5, 10, 6], [6, 12, 7], [7, 14, 8], [8, 16, 9]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 1], [1, 2, 2], [2, 4, 3], [3, 6, 4], [4, 8, 5], [5, 10, 6], [6, 12, 7], [7, 14, 8], [8, 16, 9]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[5, 5, 5], [10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5], [45, 45, 5], [50, 50, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[5, 5, 5], [10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5], [45, 45, 5], [50, 50, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[0, 0, 50], [50, 0, 50], [100, 0, 50], [150, 0, 50], [200, 0, 50], [250, 0, 50], [300, 0, 50], [350, 0, 50], [400, 0, 50]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[0, 0, 50], [50, 0, 50], [100, 0, 50], [150, 0, 50], [200, 0, 50], [250, 0, 50], [300, 0, 50], [350, 0, 50], [400, 0, 50]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [20, 20, 5], [30, 30, 5], [40, 40, 5], [50, 50, 5], [60, 60, 5], [70, 70, 5], [80, 80, 5], [90, 90, 5], [100, 100, 5], [110, 110, 5], [120, 120, 5], [130, 130, 5], [140, 140, 5], [150, 150, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [20, 20, 5], [30, 30, 5], [40, 40, 5], [50, 50, 5], [60, 60, 5], [70, 70, 5], [80, 80, 5], [90, 90, 5], [100, 100, 5], [110, 110, 5], [120, 120, 5], [130, 130, 5], [140, 140, 5], [150, 150, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 3], [12, 12, 2], [15, 15, 1], [18, 18, 4], [20, 20, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 3], [12, 12, 2], [15, 15, 1], [18, 18, 4], [20, 20, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[10, 10, 5], [15, 10, 10], [20, 10, 3], [10, 20, 6], [25, 25, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[10, 10, 5], [15, 10, 10], [20, 10, 3], [10, 20, 6], [25, 25, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[100, 100, 50], [200, 200, 50], [300, 300, 50], [250, 250, 100]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[100, 100, 50], [200, 200, 50], [300, 300, 50], [250, 250, 100]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bombs = [[1, 1, 5], [5, 1, 5], [9, 1, 5], [13, 1, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bombs = [[1, 1, 5], [5, 1, 5], [9, 1, 5], [13, 1, 5]]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5]]) == 1
    assert candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5]]) == 4
    assert candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1]]) == 1
    assert candidate(bombs = [[1, 1, 100], [1, 1, 50], [1, 1, 25]]) == 3
    assert candidate(bombs = [[1, 1, 10], [10, 10, 10], [5, 5, 5]]) == 2
    assert candidate(bombs = [[1, 1, 10], [10, 10, 1], [5, 5, 5]]) == 2
    assert candidate(bombs = [[1, 1, 5], [10, 10, 5]]) == 1
    assert candidate(bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
    assert candidate(bombs = [[5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1]]) == 1
    assert candidate(bombs = [[0, 0, 100], [50, 50, 100], [100, 100, 100]]) == 3
    assert candidate(bombs = [[100, 100, 1], [101, 101, 1], [102, 102, 1]]) == 1
    assert candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2]]) == 4
    assert candidate(bombs = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3
    assert candidate(bombs = [[2, 1, 3], [6, 1, 4]]) == 2
    assert candidate(bombs = [[1, 1, 3], [2, 2, 3], [3, 3, 3], [4, 4, 3]]) == 4
    assert candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 1
    assert candidate(bombs = [[5, 5, 3], [6, 6, 1], [7, 7, 4]]) == 3
    assert candidate(bombs = [[5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8]]) == 4
    assert candidate(bombs = [[10, 10, 10], [20, 20, 10], [30, 30, 10]]) == 1
    assert candidate(bombs = [[10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1], [60, 10, 1], [70, 10, 1], [80, 10, 1], [90, 10, 1], [100, 10, 1]]) == 1
    assert candidate(bombs = [[100, 100, 10], [100, 110, 10], [100, 120, 10], [110, 100, 10], [110, 110, 10], [110, 120, 10], [120, 100, 10], [120, 110, 10], [120, 120, 10]]) == 9
    assert candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1]]) == 7
    assert candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5]]) == 1
    assert candidate(bombs = [[50, 50, 10], [60, 60, 20], [70, 70, 30], [80, 80, 40], [90, 90, 50]]) == 5
    assert candidate(bombs = [[10, 10, 3], [10, 13, 3], [13, 10, 3], [13, 13, 3], [16, 16, 3], [16, 19, 3], [19, 16, 3], [19, 19, 3]]) == 4
    assert candidate(bombs = [[1, 1, 10], [1, 10, 10], [10, 1, 10], [10, 10, 10], [15, 15, 15], [15, 5, 15], [5, 15, 15], [20, 20, 5]]) == 8
    assert candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1], [7, 0, 1], [8, 0, 1], [9, 0, 1]]) == 10
    assert candidate(bombs = [[50, 50, 5], [55, 50, 5], [60, 50, 5], [65, 50, 5], [70, 50, 5], [75, 50, 5], [80, 50, 5], [85, 50, 5], [90, 50, 5], [95, 50, 5], [100, 50, 5], [105, 50, 5], [110, 50, 5], [115, 50, 5], [120, 50, 5], [125, 50, 5], [130, 50, 5], [135, 50, 5], [140, 50, 5], [145, 50, 5]]) == 20
    assert candidate(bombs = [[100, 100, 10], [110, 100, 10], [120, 100, 10], [130, 100, 10], [140, 100, 10], [150, 100, 10], [160, 100, 10], [170, 100, 10], [180, 100, 10]]) == 9
    assert candidate(bombs = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1]]) == 1
    assert candidate(bombs = [[50, 50, 5], [60, 50, 5], [70, 50, 5], [80, 50, 5], [50, 60, 5], [50, 70, 5], [50, 80, 5], [50, 90, 5], [50, 100, 5], [60, 60, 15]]) == 6
    assert candidate(bombs = [[100, 100, 50], [200, 100, 50], [100, 200, 50], [200, 200, 50], [150, 150, 100]]) == 5
    assert candidate(bombs = [[10, 10, 1], [20, 20, 1], [30, 30, 1], [40, 40, 1], [50, 50, 1], [60, 60, 1], [70, 70, 1], [80, 80, 1], [90, 90, 1], [100, 100, 100]]) == 8
    assert candidate(bombs = [[5, 5, 5], [5, 15, 5], [15, 5, 5], [15, 15, 5], [10, 10, 20]]) == 5
    assert candidate(bombs = [[1, 1, 5], [2, 2, 10], [3, 3, 2], [4, 4, 8], [5, 5, 1]]) == 5
    assert candidate(bombs = [[1, 1, 100], [1, 1, 100], [1, 1, 100], [1, 1, 100], [1, 1, 100]]) == 5
    assert candidate(bombs = [[0, 0, 20], [5, 0, 15], [10, 0, 10], [15, 0, 5], [20, 0, 1], [25, 0, 20], [30, 0, 15], [35, 0, 10], [40, 0, 5]]) == 9
    assert candidate(bombs = [[0, 0, 1], [2, 0, 1], [0, 2, 1], [2, 2, 1], [1, 1, 1.5]]) == 5
    assert candidate(bombs = [[50, 50, 15], [60, 50, 20], [70, 50, 10], [50, 60, 25], [50, 70, 12], [50, 80, 5]]) == 6
    assert candidate(bombs = [[0, 0, 10], [10, 0, 20], [20, 0, 30], [30, 0, 40], [40, 0, 50], [50, 0, 60], [60, 0, 70], [70, 0, 80], [80, 0, 90]]) == 9
    assert candidate(bombs = [[1, 1, 10], [10, 1, 10], [1, 10, 10], [10, 10, 10], [5, 5, 5], [15, 15, 15]]) == 6
    assert candidate(bombs = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]]) == 10
    assert candidate(bombs = [[1, 1, 10], [20, 20, 10], [30, 30, 10], [40, 40, 10], [50, 50, 10], [60, 60, 10]]) == 1
    assert candidate(bombs = [[100, 100, 50], [200, 200, 50], [300, 300, 50], [100, 200, 60], [200, 300, 70]]) == 1
    assert candidate(bombs = [[10, 10, 1], [15, 15, 2], [20, 20, 3], [25, 25, 4], [30, 30, 5]]) == 1
    assert candidate(bombs = [[5, 5, 1], [5, 6, 1], [5, 7, 1], [5, 8, 1], [5, 9, 1]]) == 5
    assert candidate(bombs = [[1, 1, 10], [2, 2, 20], [3, 3, 30], [4, 4, 40], [5, 5, 50], [6, 6, 60]]) == 6
    assert candidate(bombs = [[5, 5, 20], [10, 5, 20], [15, 5, 20], [20, 5, 20], [25, 5, 20], [30, 5, 20], [35, 5, 20], [40, 5, 20], [45, 5, 20], [50, 5, 20]]) == 10
    assert candidate(bombs = [[1, 1, 100], [200, 200, 100], [400, 400, 100], [600, 600, 100], [800, 800, 100], [1000, 1000, 100], [1200, 1200, 100], [1400, 1400, 100], [1600, 1600, 100], [1800, 1800, 100]]) == 1
    assert candidate(bombs = [[0, 0, 10], [20, 20, 10], [10, 10, 15], [30, 30, 20]]) == 3
    assert candidate(bombs = [[10, 10, 15], [20, 20, 15], [30, 30, 15], [40, 40, 15], [50, 50, 15], [60, 60, 15], [70, 70, 15], [80, 80, 15], [90, 90, 15]]) == 9
    assert candidate(bombs = [[10, 10, 15], [20, 20, 15], [30, 30, 15], [40, 40, 15], [50, 50, 15], [60, 60, 15], [70, 70, 15]]) == 7
    assert candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 10
    assert candidate(bombs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]) == 8
    assert candidate(bombs = [[100, 100, 100], [200, 100, 100], [300, 100, 100], [400, 100, 100], [500, 100, 100], [600, 100, 100], [700, 100, 100], [800, 100, 100], [900, 100, 100]]) == 9
    assert candidate(bombs = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1], [7, 0, 1], [8, 0, 1], [9, 0, 1], [10, 0, 1]]) == 11
    assert candidate(bombs = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1]]) == 1
    assert candidate(bombs = [[10, 10, 5], [15, 10, 5], [20, 10, 5], [25, 10, 5], [30, 10, 5], [35, 10, 5], [40, 10, 5], [45, 10, 5]]) == 8
    assert candidate(bombs = [[1, 1, 100], [1, 101, 100], [101, 101, 100], [101, 1, 100], [51, 51, 100], [51, 1, 100], [1, 51, 100], [101, 51, 100], [51, 101, 100]]) == 9
    assert candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 2], [6, 6, 2]]) == 6
    assert candidate(bombs = [[10, 10, 20], [30, 30, 20], [50, 50, 20], [70, 70, 20], [90, 90, 20], [110, 110, 20], [130, 130, 20], [150, 150, 20], [170, 170, 20], [190, 190, 20], [210, 210, 20], [230, 230, 20], [250, 250, 20], [270, 270, 20], [290, 290, 20]]) == 1
    assert candidate(bombs = [[5, 5, 2], [10, 5, 2], [15, 5, 2], [20, 5, 2], [25, 5, 2], [30, 5, 2], [35, 5, 2], [40, 5, 2], [45, 5, 2], [50, 5, 2], [55, 5, 2]]) == 1
    assert candidate(bombs = [[10, 10, 15], [20, 20, 25], [30, 30, 35], [40, 40, 45], [50, 50, 55]]) == 5
    assert candidate(bombs = [[100, 100, 100], [200, 200, 50], [300, 300, 25], [400, 400, 12.5]]) == 1
    assert candidate(bombs = [[5, 5, 10], [15, 5, 10], [5, 15, 10], [15, 15, 10], [10, 10, 5]]) == 5
    assert candidate(bombs = [[1, 1, 2], [2, 2, 2], [3, 3, 2], [4, 4, 2], [5, 5, 2], [6, 6, 2], [7, 7, 2], [8, 8, 2], [9, 9, 2]]) == 9
    assert candidate(bombs = [[10, 10, 25], [15, 10, 15], [10, 15, 20], [5, 10, 10], [10, 5, 15]]) == 5
    assert candidate(bombs = [[1, 1, 3], [4, 4, 3], [7, 1, 3], [4, 7, 3], [10, 10, 3]]) == 2
    assert candidate(bombs = [[1, 1, 5], [1, 6, 5], [6, 1, 5], [6, 6, 5], [3, 3, 1]]) == 5
    assert candidate(bombs = [[1, 1, 1000], [2, 2, 1000], [3, 3, 1000], [4, 4, 1000], [5, 5, 1000], [6, 6, 1000], [7, 7, 1000], [8, 8, 1000]]) == 8
    assert candidate(bombs = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == 1
    assert candidate(bombs = [[100, 100, 50], [150, 100, 50], [200, 100, 50], [250, 100, 50], [300, 100, 50], [350, 100, 50], [400, 100, 50], [450, 100, 50]]) == 8
    assert candidate(bombs = [[0, 0, 5], [10, 0, 5], [5, 5, 5], [15, 5, 5]]) == 1
    assert candidate(bombs = [[10, 10, 5], [15, 10, 5], [10, 15, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5]]) == 4
    assert candidate(bombs = [[0, 0, 10], [15, 0, 10], [30, 0, 10], [22, 0, 5]]) == 2
    assert candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]) == 15
    assert candidate(bombs = [[0, 0, 10], [20, 0, 10], [40, 0, 10], [60, 0, 10], [80, 0, 10], [100, 0, 10], [120, 0, 10], [140, 0, 10], [160, 0, 10], [180, 0, 10]]) == 1
    assert candidate(bombs = [[5, 5, 5], [10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5]]) == 1
    assert candidate(bombs = [[50, 50, 50], [60, 60, 50], [70, 70, 50], [80, 80, 50], [90, 90, 50], [100, 100, 50]]) == 6
    assert candidate(bombs = [[50, 50, 50], [100, 100, 50], [150, 150, 50], [200, 200, 50], [250, 250, 50], [300, 300, 50], [350, 350, 50], [400, 400, 50], [450, 450, 50]]) == 1
    assert candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [30, 0, 10], [40, 0, 10], [50, 0, 10]]) == 6
    assert candidate(bombs = [[10, 10, 5], [15, 15, 3], [20, 20, 4], [25, 25, 2], [30, 30, 6]]) == 1
    assert candidate(bombs = [[10, 10, 15], [15, 15, 15], [20, 20, 15], [25, 25, 15], [30, 30, 15]]) == 5
    assert candidate(bombs = [[10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5]]) == 1
    assert candidate(bombs = [[1, 1, 100], [101, 101, 100], [201, 201, 100], [301, 301, 100], [401, 401, 100]]) == 1
    assert candidate(bombs = [[5, 5, 3], [7, 5, 3], [9, 5, 3], [11, 5, 3], [13, 5, 3]]) == 5
    assert candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5], [5, 5, 5], [6, 6, 5], [7, 7, 5], [8, 8, 5], [9, 9, 5]]) == 9
    assert candidate(bombs = [[10000, 10000, 5000], [15000, 10000, 10000], [20000, 10000, 3000], [10000, 20000, 6000], [25000, 25000, 8000]]) == 3
    assert candidate(bombs = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9]]) == 9
    assert candidate(bombs = [[1000, 1000, 1000], [2000, 2000, 500], [3000, 3000, 250], [4000, 4000, 125]]) == 1
    assert candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [30, 0, 10], [40, 0, 10]]) == 5
    assert candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]) == 5
    assert candidate(bombs = [[10, 10, 50], [20, 20, 40], [30, 30, 30], [40, 40, 20], [50, 50, 10]]) == 5
    assert candidate(bombs = [[5, 5, 10], [10, 10, 10], [15, 15, 10], [20, 20, 10], [25, 25, 10], [30, 30, 10], [35, 35, 10]]) == 7
    assert candidate(bombs = [[10, 10, 10], [20, 20, 10], [30, 30, 10], [40, 40, 10], [50, 50, 10], [60, 60, 10], [70, 70, 10], [80, 80, 10], [90, 90, 10], [100, 100, 10], [110, 110, 10], [120, 120, 10], [130, 130, 10], [140, 140, 10], [150, 150, 10]]) == 1
    assert candidate(bombs = [[1, 1, 10], [10, 1, 5], [10, 10, 15], [20, 20, 10]]) == 4
    assert candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7]]) == 7
    assert candidate(bombs = [[1, 1, 10], [10, 1, 5], [1, 10, 5], [5, 5, 2], [7, 7, 7]]) == 5
    assert candidate(bombs = [[1, 1, 10000], [2, 2, 10000], [3, 3, 10000], [4, 4, 10000], [5, 5, 10000], [6, 6, 10000], [7, 7, 10000], [8, 8, 10000], [9, 9, 10000], [10, 10, 10000]]) == 10
    assert candidate(bombs = [[10, 10, 1], [11, 11, 2], [12, 12, 3], [13, 13, 4], [14, 14, 5], [15, 15, 6], [16, 16, 7], [17, 17, 8], [18, 18, 9], [19, 19, 10]]) == 10
    assert candidate(bombs = [[0, 0, 10], [10, 0, 10], [20, 0, 10], [15, 5, 5]]) == 4
    assert candidate(bombs = [[1, 1, 10], [11, 1, 10], [21, 1, 10], [1, 11, 10], [11, 11, 10], [21, 11, 10], [1, 21, 10], [11, 21, 10], [21, 21, 10]]) == 9
    assert candidate(bombs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == 5
    assert candidate(bombs = [[1, 1, 10], [2, 1, 10], [3, 1, 10], [4, 1, 10], [5, 1, 10], [6, 1, 10], [7, 1, 10], [8, 1, 10], [9, 1, 10], [10, 1, 10]]) == 10
    assert candidate(bombs = [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5], [5, 5, 5], [6, 6, 5], [7, 7, 5], [8, 8, 5], [9, 9, 5], [10, 10, 5], [11, 11, 5], [12, 12, 5], [13, 13, 5], [14, 14, 5], [15, 15, 5]]) == 15
    assert candidate(bombs = [[0, 0, 1], [1, 2, 2], [2, 4, 3], [3, 6, 4], [4, 8, 5], [5, 10, 6], [6, 12, 7], [7, 14, 8], [8, 16, 9]]) == 8
    assert candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]]) == 9
    assert candidate(bombs = [[5, 5, 5], [10, 10, 5], [15, 15, 5], [20, 20, 5], [25, 25, 5], [30, 30, 5], [35, 35, 5], [40, 40, 5], [45, 45, 5], [50, 50, 5]]) == 1
    assert candidate(bombs = [[0, 0, 50], [50, 0, 50], [100, 0, 50], [150, 0, 50], [200, 0, 50], [250, 0, 50], [300, 0, 50], [350, 0, 50], [400, 0, 50]]) == 9
    assert candidate(bombs = [[10, 10, 5], [20, 20, 5], [30, 30, 5], [40, 40, 5], [50, 50, 5], [60, 60, 5], [70, 70, 5], [80, 80, 5], [90, 90, 5], [100, 100, 5], [110, 110, 5], [120, 120, 5], [130, 130, 5], [140, 140, 5], [150, 150, 5]]) == 1
    assert candidate(bombs = [[10, 10, 3], [12, 12, 2], [15, 15, 1], [18, 18, 4], [20, 20, 5]]) == 2
    assert candidate(bombs = [[10, 10, 5], [15, 10, 10], [20, 10, 3], [10, 20, 6], [25, 25, 8]]) == 3
    assert candidate(bombs = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13]]) == 13
    assert candidate(bombs = [[100, 100, 50], [200, 200, 50], [300, 300, 50], [250, 250, 100]]) == 3
    assert candidate(bombs = [[1, 1, 5], [5, 1, 5], [9, 1, 5], [13, 1, 5]]) == 4


