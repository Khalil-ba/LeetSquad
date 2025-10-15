def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [50, 150, 50], [100, 200, 50]]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [50, 150, 50], [100, 200, 50]]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [1, 2, 1], [1, 2, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [1, 2, 1], [1, 2, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [50, 150, 50], [150, 200, 50]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [50, 150, 50], [150, 200, 50]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [2, 9, 8], [3, 8, 6], [4, 7, 4], [5, 6, 2]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [2, 9, 8], [3, 8, 6], [4, 7, 4], [5, 6, 2]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[5, 10, 5], [15, 20, 5], [25, 30, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[5, 10, 5], [15, 20, 5], [25, 30, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [10, 20, 5], [20, 30, 5]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [10, 20, 5], [20, 30, 5]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 1], [2, 6, 2], [3, 7, 3], [4, 8, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 1], [2, 6, 2], [3, 7, 3], [4, 8, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[10, 20, 5], [20, 30, 5], [30, 40, 5], [40, 50, 5]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[10, 20, 5], [20, 30, 5], [30, 40, 5], [40, 50, 5]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[5, 10, 3], [10, 15, 3], [15, 20, 4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[5, 10, 3], [10, 15, 3], [15, 20, 4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 2], [2, 5, 3], [5, 6, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 2], [2, 5, 3], [5, 6, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 5], [6, 10, 5], [11, 15, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 5], [6, 10, 5], [11, 15, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [10, 20, 10], [20, 30, 10]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [10, 20, 10], [20, 30, 10]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 5], [2, 9, 4], [3, 8, 3], [4, 7, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 5], [2, 9, 4], [3, 8, 3], [4, 7, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[2, 3, 1], [4, 5, 1], [1, 5, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[2, 3, 1], [4, 5, 1], [1, 5, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 3], [2, 6, 4], [3, 7, 5], [4, 8, 6], [5, 9, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 3], [2, 6, 4], [3, 7, 5], [4, 8, 6], [5, 9, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 5], [10, 20, 5], [20, 30, 5]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 5], [10, 20, 5], [20, 30, 5]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 2], [2, 3, 2], [3, 4, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 2], [2, 3, 2], [3, 4, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [51, 150, 50], [101, 200, 50]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [51, 150, 50], [101, 200, 50]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 5], [10, 20, 10], [15, 25, 10]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 5], [10, 20, 10], [15, 25, 10]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 20, 10], [5, 15, 5], [10, 25, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 20, 10], [5, 15, 5], [10, 25, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 1], [2, 6, 1], [3, 7, 1], [4, 8, 1], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 1], [2, 6, 1], [3, 7, 1], [4, 8, 1], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1], [6, 8, 1], [7, 9, 1], [8, 10, 1], [9, 11, 1], [10, 12, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1], [6, 8, 1], [7, 9, 1], [8, 10, 1], [9, 11, 1], [10, 12, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 15, 10], [5, 20, 12], [10, 25, 15], [15, 30, 18]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 15, 10], [5, 20, 12], [10, 25, 15], [15, 30, 18]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 500, 250], [200, 600, 200], [300, 700, 150], [400, 800, 100]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 500, 250], [200, 600, 200], [300, 700, 150], [400, 800, 100]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 5, 5], [7, 4, 4], [8, 3, 3], [9, 2, 2], [10, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 5, 5], [7, 4, 4], [8, 3, 3], [9, 2, 2], [10, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 2], [2, 4, 2], [3, 4, 2], [4, 5, 2], [5, 6, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 2], [2, 4, 2], [3, 4, 2], [4, 5, 2], [5, 6, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 50, 25], [25, 75, 25], [50, 100, 25], [75, 125, 25], [100, 150, 25], [125, 175, 25], [150, 200, 25]]) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 50, 25], [25, 75, 25], [50, 100, 25], [75, 125, 25], [100, 150, 25], [125, 175, 25], [150, 200, 25]]) == 97: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 5], [5, 10, 5], [10, 15, 5], [15, 20, 5]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 5], [5, 10, 5], [10, 15, 5], [15, 20, 5]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[10, 20, 1], [11, 21, 1], [12, 22, 1], [13, 23, 1], [14, 24, 1], [15, 25, 1], [16, 26, 1], [17, 27, 1], [18, 28, 1], [19, 29, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[10, 20, 1], [11, 21, 1], [12, 22, 1], [13, 23, 1], [14, 24, 1], [15, 25, 1], [16, 26, 1], [17, 27, 1], [18, 28, 1], [19, 29, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 10], [20, 120, 20], [40, 140, 30], [60, 160, 40], [80, 180, 50], [100, 190, 60]]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 10], [20, 120, 20], [40, 140, 30], [60, 160, 40], [80, 180, 50], [100, 190, 60]]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [2, 15, 5], [3, 20, 3], [4, 25, 2], [5, 30, 1], [6, 35, 2], [7, 40, 3], [8, 45, 4], [9, 50, 5], [10, 55, 6]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [2, 15, 5], [3, 20, 3], [4, 25, 2], [5, 30, 1], [6, 35, 2], [7, 40, 3], [8, 45, 4], [9, 50, 5], [10, 55, 6]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 9], [2, 9, 8], [3, 8, 7], [4, 7, 6], [5, 6, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 9], [2, 9, 8], [3, 8, 7], [4, 7, 6], [5, 6, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[10, 20, 10], [15, 30, 5], [20, 40, 3], [25, 50, 2], [30, 60, 1], [35, 70, 2], [40, 80, 3], [45, 90, 4], [50, 100, 5]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[10, 20, 10], [15, 30, 5], [20, 40, 3], [25, 50, 2], [30, 60, 1], [35, 70, 2], [40, 80, 3], [45, 90, 4], [50, 100, 5]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1000], [500, 1500, 1000], [1000, 2000, 1000], [1, 1000, 500], [1001, 2000, 500]]) == 1499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1000], [500, 1500, 1000], [1000, 2000, 1000], [1, 1000, 500], [1001, 2000, 500]]) == 1499: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[10, 20, 5], [15, 25, 4], [20, 30, 3], [25, 35, 2], [30, 40, 1], [35, 45, 2], [40, 50, 3], [45, 55, 4], [50, 60, 5], [55, 65, 6]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[10, 20, 5], [15, 25, 4], [20, 30, 3], [25, 35, 2], [30, 40, 1], [35, 45, 2], [40, 50, 3], [45, 55, 4], [50, 60, 5], [55, 65, 6]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1000], [500, 1500, 500], [1000, 2000, 1000], [1500, 2000, 500], [1, 1000, 500], [500, 1000, 250]]) == 1499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1000], [500, 1500, 500], [1000, 2000, 1000], [1500, 2000, 500], [1, 1000, 500], [500, 1000, 250]]) == 1499: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [20, 30, 15], [40, 50, 10], [60, 70, 5], [80, 90, 3]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [20, 30, 15], [40, 50, 10], [60, 70, 5], [80, 90, 3]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 20, 15], [5, 15, 10], [10, 25, 12], [15, 30, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 20, 15], [5, 15, 10], [10, 25, 12], [15, 30, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 9], [2, 10, 8], [3, 10, 7], [4, 10, 6], [5, 10, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 9], [2, 10, 8], [3, 10, 7], [4, 10, 6], [5, 10, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 2000], [2, 1999, 1999], [3, 1998, 1998], [4, 1997, 1997], [5, 1996, 1996]]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 2000], [2, 1999, 1999], [3, 1998, 1998], [4, 1997, 1997], [5, 1996, 1996]]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 3, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1], [10, 10, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 3, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1], [10, 10, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 1000, 500], [1, 1000, 500], [1, 1000, 500], [1, 1000, 500], [1, 1000, 500]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 1000, 500], [1, 1000, 500], [1, 1000, 500], [1, 1000, 500], [1, 1000, 500]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[5, 15, 10], [10, 20, 5], [15, 25, 3], [20, 30, 2], [25, 35, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[5, 15, 10], [10, 20, 5], [15, 25, 3], [20, 30, 2], [25, 35, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 1], [2, 6, 1], [3, 7, 1], [4, 8, 1], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 1], [2, 6, 1], [3, 7, 1], [4, 8, 1], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 20, 5], [2, 19, 5], [3, 18, 5], [4, 17, 5], [5, 16, 5], [6, 15, 5], [7, 14, 5], [8, 13, 5], [9, 12, 5], [10, 11, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 20, 5], [2, 19, 5], [3, 18, 5], [4, 17, 5], [5, 16, 5], [6, 15, 5], [7, 14, 5], [8, 13, 5], [9, 12, 5], [10, 11, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 1000, 500], [200, 800, 300], [400, 600, 200], [500, 700, 150]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 1000, 500], [200, 800, 300], [400, 600, 200], [500, 700, 150]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1], [15, 16, 1], [17, 18, 1], [19, 20, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1], [15, 16, 1], [17, 18, 1], [19, 20, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 500, 250], [250, 750, 300], [500, 1000, 350], [750, 1250, 400], [1000, 1500, 450]]) == 1048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 500, 250], [250, 750, 300], [500, 1000, 350], [750, 1250, 400], [1000, 1500, 450]]) == 1048: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 3], [2, 9, 5], [3, 8, 4], [4, 7, 1], [5, 6, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 3], [2, 9, 5], [3, 8, 4], [4, 7, 1], [5, 6, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 5, 5], [7, 4, 4], [8, 3, 3], [9, 2, 2]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 5, 5], [7, 4, 4], [8, 3, 3], [9, 2, 2]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 3], [4, 6, 2], [7, 9, 1], [10, 12, 3], [13, 15, 2]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 3], [4, 6, 2], [7, 9, 1], [10, 12, 3], [13, 15, 2]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[5, 10, 5], [10, 15, 5], [15, 20, 5], [20, 25, 5], [25, 30, 5], [30, 35, 5], [35, 40, 5], [40, 45, 5]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[5, 10, 5], [10, 15, 5], [15, 20, 5], [20, 25, 5], [25, 30, 5], [30, 35, 5], [35, 40, 5], [40, 45, 5]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 50, 25], [25, 75, 30], [50, 100, 35], [75, 125, 40], [100, 150, 45]]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 50, 25], [25, 75, 30], [50, 100, 35], [75, 125, 40], [100, 150, 45]]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 3], [4, 6, 3], [7, 9, 3], [10, 12, 3], [13, 15, 3], [16, 18, 3], [19, 21, 3], [22, 24, 3], [25, 27, 3], [28, 30, 3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 3], [4, 6, 3], [7, 9, 3], [10, 12, 3], [13, 15, 3], [16, 18, 3], [19, 21, 3], [22, 24, 3], [25, 27, 3], [28, 30, 3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 3], [1, 20, 3], [1, 30, 3], [1, 40, 3], [1, 50, 3], [1, 60, 3], [1, 70, 3], [1, 80, 3], [1, 90, 3], [1, 100, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 3], [1, 20, 3], [1, 30, 3], [1, 40, 3], [1, 50, 3], [1, 60, 3], [1, 70, 3], [1, 80, 3], [1, 90, 3], [1, 100, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 1000, 999], [500, 1500, 1000], [1000, 2000, 1000]]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 1000, 999], [500, 1500, 1000], [1000, 2000, 1000]]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 5], [2, 9, 4], [3, 8, 3], [4, 7, 2], [5, 6, 1], [6, 5, 1], [7, 4, 1], [8, 3, 1], [9, 2, 1], [10, 1, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 5], [2, 9, 4], [3, 8, 3], [4, 7, 2], [5, 6, 1], [6, 5, 1], [7, 4, 1], [8, 3, 1], [9, 2, 1], [10, 1, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 99], [2, 150, 98], [3, 200, 97], [4, 250, 96], [5, 300, 95], [6, 350, 94], [7, 400, 93], [8, 450, 92], [9, 500, 91]]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 99], [2, 150, 98], [3, 200, 97], [4, 250, 96], [5, 300, 95], [6, 350, 94], [7, 400, 93], [8, 450, 92], [9, 500, 91]]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1], [15, 16, 1], [17, 18, 1], [19, 20, 1], [21, 22, 1], [23, 24, 1], [25, 26, 1], [27, 28, 1], [29, 30, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1], [15, 16, 1], [17, 18, 1], [19, 20, 1], [21, 22, 1], [23, 24, 1], [25, 26, 1], [27, 28, 1], [29, 30, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [2, 90, 40], [3, 80, 30], [4, 70, 20], [5, 60, 10], [6, 50, 5], [7, 40, 3], [8, 30, 2], [9, 20, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [2, 90, 40], [3, 80, 30], [4, 70, 20], [5, 60, 10], [6, 50, 5], [7, 40, 3], [8, 30, 2], [9, 20, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 10, 2], [3, 10, 3], [4, 10, 4], [5, 10, 5], [6, 10, 6], [7, 10, 7], [8, 10, 8], [9, 10, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 10, 2], [3, 10, 3], [4, 10, 4], [5, 10, 5], [6, 10, 6], [7, 10, 7], [8, 10, 8], [9, 10, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 2000], [10, 500, 400], [150, 800, 300], [300, 1800, 500], [1000, 1900, 600]]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 2000], [10, 500, 400], [150, 800, 300], [300, 1800, 500], [1000, 1900, 600]]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1000], [2, 1999, 999], [3, 1998, 998], [4, 1997, 997], [5, 1996, 996], [6, 1995, 995], [7, 1994, 994], [8, 1993, 993], [9, 1992, 992], [10, 1991, 991]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1000], [2, 1999, 999], [3, 1998, 998], [4, 1997, 997], [5, 1996, 996], [6, 1995, 995], [7, 1994, 994], [8, 1993, 993], [9, 1992, 992], [10, 1991, 991]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 5], [2, 6, 4], [3, 7, 3], [4, 8, 2], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 5], [2, 6, 4], [3, 7, 3], [4, 8, 2], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 50, 10], [10, 20, 5], [20, 30, 5], [30, 40, 5], [40, 50, 5], [50, 60, 5], [60, 70, 5], [70, 80, 5], [80, 90, 5]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 50, 10], [10, 20, 5], [20, 30, 5], [30, 40, 5], [40, 50, 5], [50, 60, 5], [60, 70, 5], [70, 80, 5], [80, 90, 5]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [50, 150, 60], [100, 200, 70], [150, 250, 80], [200, 300, 90]]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [50, 150, 60], [100, 200, 70], [150, 250, 80], [200, 300, 90]]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 7, 5], [7, 8, 4], [8, 9, 3], [9, 10, 2], [10, 10, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 7, 5], [7, 8, 4], [8, 9, 3], [9, 10, 2], [10, 10, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[50, 150, 100], [100, 200, 100], [150, 250, 100], [200, 300, 100], [250, 350, 100], [300, 400, 100], [350, 450, 100], [400, 500, 100]]) == 446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[50, 150, 100], [100, 200, 100], [150, 250, 100], [200, 300, 100], [250, 350, 100], [300, 400, 100], [350, 450, 100], [400, 500, 100]]) == 446: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 11, 2], [3, 12, 3], [4, 13, 4], [5, 14, 5], [6, 15, 6], [7, 16, 7], [8, 17, 8], [9, 18, 9], [10, 19, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 11, 2], [3, 12, 3], [4, 13, 4], [5, 14, 5], [6, 15, 6], [7, 16, 7], [8, 17, 8], [9, 18, 9], [10, 19, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 1], [6, 10, 1], [11, 15, 1], [16, 20, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 1], [6, 10, 1], [11, 15, 1], [16, 20, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 100], [50, 150, 50], [100, 200, 30], [150, 250, 20], [200, 300, 10]]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 100], [50, 150, 50], [100, 200, 30], [150, 250, 20], [200, 300, 10]]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 5], [2, 6, 5], [3, 7, 5], [4, 8, 5], [5, 9, 5], [6, 10, 5], [7, 11, 5], [8, 12, 5], [9, 13, 5], [10, 14, 5]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 5], [2, 6, 5], [3, 7, 5], [4, 8, 5], [5, 9, 5], [6, 10, 5], [7, 11, 5], [8, 12, 5], [9, 13, 5], [10, 14, 5]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 500], [2, 1999, 499], [3, 1998, 498], [4, 1997, 497], [5, 1996, 496], [6, 1995, 495], [7, 1994, 494], [8, 1993, 493], [9, 1992, 492], [10, 1991, 491]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 500], [2, 1999, 499], [3, 1998, 498], [4, 1997, 497], [5, 1996, 496], [6, 1995, 495], [7, 1994, 494], [8, 1993, 493], [9, 1992, 492], [10, 1991, 491]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [51, 150, 50], [101, 200, 50], [151, 250, 50], [201, 300, 50]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [51, 150, 50], [101, 200, 50], [151, 250, 50], [201, 300, 50]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 1], [2, 99, 1], [3, 98, 1], [4, 97, 1], [5, 96, 1], [6, 95, 1], [7, 94, 1], [8, 93, 1], [9, 92, 1], [10, 91, 1], [11, 90, 1], [12, 89, 1], [13, 88, 1], [14, 87, 1], [15, 86, 1], [16, 85, 1], [17, 84, 1], [18, 83, 1], [19, 82, 1], [20, 81, 1], [21, 80, 1], [22, 79, 1], [23, 78, 1], [24, 77, 1], [25, 76, 1], [26, 75, 1], [27, 74, 1], [28, 73, 1], [29, 72, 1], [30, 71, 1], [31, 70, 1], [32, 69, 1], [33, 68, 1], [34, 67, 1], [35, 66, 1], [36, 65, 1], [37, 64, 1], [38, 63, 1], [39, 62, 1], [40, 61, 1], [41, 60, 1], [42, 59, 1], [43, 58, 1], [44, 57, 1], [45, 56, 1], [46, 55, 1], [47, 54, 1], [48, 53, 1], [49, 52, 1], [50, 51, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 1], [2, 99, 1], [3, 98, 1], [4, 97, 1], [5, 96, 1], [6, 95, 1], [7, 94, 1], [8, 93, 1], [9, 92, 1], [10, 91, 1], [11, 90, 1], [12, 89, 1], [13, 88, 1], [14, 87, 1], [15, 86, 1], [16, 85, 1], [17, 84, 1], [18, 83, 1], [19, 82, 1], [20, 81, 1], [21, 80, 1], [22, 79, 1], [23, 78, 1], [24, 77, 1], [25, 76, 1], [26, 75, 1], [27, 74, 1], [28, 73, 1], [29, 72, 1], [30, 71, 1], [31, 70, 1], [32, 69, 1], [33, 68, 1], [34, 67, 1], [35, 66, 1], [36, 65, 1], [37, 64, 1], [38, 63, 1], [39, 62, 1], [40, 61, 1], [41, 60, 1], [42, 59, 1], [43, 58, 1], [44, 57, 1], [45, 56, 1], [46, 55, 1], [47, 54, 1], [48, 53, 1], [49, 52, 1], [50, 51, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 3], [2, 4, 2], [3, 5, 2], [4, 6, 2], [5, 7, 2], [6, 8, 2], [7, 9, 2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 3], [2, 4, 2], [3, 5, 2], [4, 6, 2], [5, 7, 2], [6, 8, 2], [7, 9, 2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 5], [2, 10, 5], [3, 15, 5], [4, 20, 5], [5, 25, 5], [6, 30, 5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 5], [2, 10, 5], [3, 15, 5], [4, 20, 5], [5, 25, 5], [6, 30, 5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 1], [2, 5, 2], [3, 7, 3], [4, 9, 4], [5, 11, 5], [6, 13, 6], [7, 15, 7]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 1], [2, 5, 2], [3, 7, 3], [4, 9, 4], [5, 11, 5], [6, 13, 6], [7, 15, 7]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 50, 40], [25, 75, 30], [50, 100, 20], [75, 125, 10]]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 50, 40], [25, 75, 30], [50, 100, 20], [75, 125, 10]]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 20, 5], [1, 15, 5], [1, 10, 5], [1, 5, 5], [6, 10, 5], [11, 15, 5], [16, 20, 5]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 20, 5], [1, 15, 5], [1, 10, 5], [1, 5, 5], [6, 10, 5], [11, 15, 5], [16, 20, 5]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1000], [500, 1500, 500], [1000, 2000, 500], [1, 500, 100], [1500, 2000, 100]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1000], [500, 1500, 500], [1000, 2000, 500], [1, 500, 100], [1500, 2000, 100]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1], [2, 2000, 2], [3, 2000, 3], [4, 2000, 4], [5, 2000, 5], [6, 2000, 6], [7, 2000, 7], [8, 2000, 8], [9, 2000, 9], [10, 2000, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1], [2, 2000, 2], [3, 2000, 3], [4, 2000, 4], [5, 2000, 5], [6, 2000, 6], [7, 2000, 7], [8, 2000, 8], [9, 2000, 9], [10, 2000, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[100, 200, 100], [150, 250, 100], [200, 300, 100], [250, 350, 100], [300, 400, 100]]) == 298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[100, 200, 100], [150, 250, 100], [200, 300, 100], [250, 350, 100], [300, 400, 100]]) == 298: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1000], [2, 1999, 999], [3, 1998, 998], [4, 1997, 997], [5, 1996, 996], [6, 1995, 995], [7, 1994, 994], [8, 1993, 993], [9, 1992, 992], [10, 1991, 991]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1000], [2, 1999, 999], [3, 1998, 998], [4, 1997, 997], [5, 1996, 996], [6, 1995, 995], [7, 1994, 994], [8, 1993, 993], [9, 1992, 992], [10, 1991, 991]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2000, 1000], [1000, 2000, 1000], [500, 1500, 500], [100, 1900, 900]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2000, 1000], [1000, 2000, 1000], [500, 1500, 500], [100, 1900, 900]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [1, 8, 1], [1, 9, 1], [1, 10, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [1, 8, 1], [1, 9, 1], [1, 10, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5], [6, 7, 4], [7, 8, 3], [8, 9, 2], [9, 10, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5], [6, 7, 4], [7, 8, 3], [8, 9, 2], [9, 10, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 3], [2, 10, 3], [3, 10, 3], [4, 10, 3], [5, 10, 3], [6, 10, 3], [7, 10, 3], [8, 10, 3], [9, 10, 3], [1, 10, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 3], [2, 10, 3], [3, 10, 3], [4, 10, 3], [5, 10, 3], [6, 10, 3], [7, 10, 3], [8, 10, 3], [9, 10, 3], [1, 10, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [50, 150, 50], [100, 200, 50], [150, 250, 50], [200, 300, 50]]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [50, 150, 50], [100, 200, 50], [150, 250, 50], [200, 300, 50]]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 50, 25], [10, 60, 25], [20, 70, 25], [30, 80, 25], [40, 90, 25], [50, 100, 25], [60, 110, 25], [70, 120, 25], [80, 130, 25], [90, 140, 25]]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 50, 25], [10, 60, 25], [20, 70, 25], [30, 80, 25], [40, 90, 25], [50, 100, 25], [60, 110, 25], [70, 120, 25], [80, 130, 25], [90, 140, 25]]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 10, 2], [3, 10, 3], [4, 10, 4], [5, 10, 5], [6, 10, 6], [7, 10, 7], [8, 10, 8], [9, 10, 9], [10, 10, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 10, 2], [3, 10, 3], [4, 10, 4], [5, 10, 5], [6, 10, 6], [7, 10, 7], [8, 10, 8], [9, 10, 9], [10, 10, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 10, 1], [2, 9, 1], [3, 8, 1], [4, 7, 1], [5, 6, 1], [6, 5, 1], [7, 4, 1], [8, 3, 1], [9, 2, 1], [10, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 10, 1], [2, 9, 1], [3, 8, 1], [4, 7, 1], [5, 6, 1], [6, 5, 1], [7, 4, 1], [8, 3, 1], [9, 2, 1], [10, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 2], [1, 5, 2], [1, 5, 2], [1, 5, 2], [1, 5, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 2], [1, 5, 2], [1, 5, 2], [1, 5, 2], [1, 5, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 100, 50], [20, 150, 60], [30, 180, 70], [40, 200, 80]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 100, 50], [20, 150, 60], [30, 180, 70], [40, 200, 80]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [[1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [[1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5]]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]]) == 2
    assert candidate(tasks = [[1, 100, 50], [50, 150, 50], [100, 200, 50]]) == 99
    assert candidate(tasks = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 5
    assert candidate(tasks = [[1, 2, 1], [1, 2, 1], [1, 2, 1]]) == 1
    assert candidate(tasks = [[1, 100, 50], [50, 150, 50], [150, 200, 50]]) == 100
    assert candidate(tasks = [[1, 10, 10], [2, 9, 8], [3, 8, 6], [4, 7, 4], [5, 6, 2]]) == 10
    assert candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6]]) == 10
    assert candidate(tasks = [[5, 10, 5], [15, 20, 5], [25, 30, 5]]) == 15
    assert candidate(tasks = [[1, 10, 10], [10, 20, 5], [20, 30, 5]]) == 18
    assert candidate(tasks = [[1, 5, 1], [2, 6, 2], [3, 7, 3], [4, 8, 4]]) == 4
    assert candidate(tasks = [[10, 20, 5], [20, 30, 5], [30, 40, 5], [40, 50, 5]]) == 17
    assert candidate(tasks = [[5, 10, 3], [10, 15, 3], [15, 20, 4]]) == 8
    assert candidate(tasks = [[1, 3, 2], [2, 5, 3], [5, 6, 2]]) == 4
    assert candidate(tasks = [[1, 5, 5], [6, 10, 5], [11, 15, 5]]) == 15
    assert candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1]]) == 2
    assert candidate(tasks = [[1, 10, 10], [10, 20, 10], [20, 30, 10]]) == 28
    assert candidate(tasks = [[1, 10, 10]]) == 10
    assert candidate(tasks = [[1, 10, 5], [2, 9, 4], [3, 8, 3], [4, 7, 2]]) == 5
    assert candidate(tasks = [[2, 3, 1], [4, 5, 1], [1, 5, 2]]) == 2
    assert candidate(tasks = [[1, 5, 3], [2, 6, 4], [3, 7, 5], [4, 8, 6], [5, 9, 7]]) == 7
    assert candidate(tasks = [[1, 10, 5], [10, 20, 5], [20, 30, 5]]) == 13
    assert candidate(tasks = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]]) == 4
    assert candidate(tasks = [[1, 2, 2], [2, 3, 2], [3, 4, 2]]) == 4
    assert candidate(tasks = [[1, 100, 50], [51, 150, 50], [101, 200, 50]]) == 100
    assert candidate(tasks = [[1, 10, 5], [10, 20, 10], [15, 25, 10]]) == 18
    assert candidate(tasks = [[1, 20, 10], [5, 15, 5], [10, 25, 10]]) == 10
    assert candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1]]) == 3
    assert candidate(tasks = [[1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3], [1, 5, 3], [2, 5, 3], [3, 5, 3], [4, 5, 3]]) == 3
    assert candidate(tasks = [[1, 5, 1], [2, 6, 1], [3, 7, 1], [4, 8, 1], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 2
    assert candidate(tasks = [[1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1], [6, 8, 1], [7, 9, 1], [8, 10, 1], [9, 11, 1], [10, 12, 1]]) == 4
    assert candidate(tasks = [[1, 15, 10], [5, 20, 12], [10, 25, 15], [15, 30, 18]]) == 25
    assert candidate(tasks = [[1, 500, 250], [200, 600, 200], [300, 700, 150], [400, 800, 100]]) == 250
    assert candidate(tasks = [[1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5]]) == 5
    assert candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 5, 5], [7, 4, 4], [8, 3, 3], [9, 2, 2], [10, 1, 1]]) == 10
    assert candidate(tasks = [[1, 5, 2], [2, 4, 2], [3, 4, 2], [4, 5, 2], [5, 6, 2]]) == 4
    assert candidate(tasks = [[1, 50, 25], [25, 75, 25], [50, 100, 25], [75, 125, 25], [100, 150, 25], [125, 175, 25], [150, 200, 25]]) == 97
    assert candidate(tasks = [[1, 5, 5], [5, 10, 5], [10, 15, 5], [15, 20, 5]]) == 17
    assert candidate(tasks = [[10, 20, 1], [11, 21, 1], [12, 22, 1], [13, 23, 1], [14, 24, 1], [15, 25, 1], [16, 26, 1], [17, 27, 1], [18, 28, 1], [19, 29, 1]]) == 1
    assert candidate(tasks = [[1, 100, 10], [20, 120, 20], [40, 140, 30], [60, 160, 40], [80, 180, 50], [100, 190, 60]]) == 69
    assert candidate(tasks = [[1, 10, 10], [2, 15, 5], [3, 20, 3], [4, 25, 2], [5, 30, 1], [6, 35, 2], [7, 40, 3], [8, 45, 4], [9, 50, 5], [10, 55, 6]]) == 15
    assert candidate(tasks = [[1, 10, 9], [2, 9, 8], [3, 8, 7], [4, 7, 6], [5, 6, 5]]) == 9
    assert candidate(tasks = [[10, 20, 10], [15, 30, 5], [20, 40, 3], [25, 50, 2], [30, 60, 1], [35, 70, 2], [40, 80, 3], [45, 90, 4], [50, 100, 5]]) == 17
    assert candidate(tasks = [[1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5], [1, 10, 5]]) == 5
    assert candidate(tasks = [[1, 2000, 1000], [500, 1500, 1000], [1000, 2000, 1000], [1, 1000, 500], [1001, 2000, 500]]) == 1499
    assert candidate(tasks = [[10, 20, 5], [15, 25, 4], [20, 30, 3], [25, 35, 2], [30, 40, 1], [35, 45, 2], [40, 50, 3], [45, 55, 4], [50, 60, 5], [55, 65, 6]]) == 17
    assert candidate(tasks = [[1, 2000, 1000], [500, 1500, 500], [1000, 2000, 1000], [1500, 2000, 500], [1, 1000, 500], [500, 1000, 250]]) == 1499
    assert candidate(tasks = [[1, 100, 50], [20, 30, 15], [40, 50, 10], [60, 70, 5], [80, 90, 3]]) == 50
    assert candidate(tasks = [[1, 20, 15], [5, 15, 10], [10, 25, 12], [15, 30, 10]]) == 19
    assert candidate(tasks = [[1, 10, 9], [2, 10, 8], [3, 10, 7], [4, 10, 6], [5, 10, 5]]) == 9
    assert candidate(tasks = [[1, 2000, 2000], [2, 1999, 1999], [3, 1998, 1998], [4, 1997, 1997], [5, 1996, 1996]]) == 2000
    assert candidate(tasks = [[1, 10, 1], [2, 3, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1], [10, 10, 1]]) == 5
    assert candidate(tasks = [[1, 1000, 500], [1, 1000, 500], [1, 1000, 500], [1, 1000, 500], [1, 1000, 500]]) == 500
    assert candidate(tasks = [[5, 15, 10], [10, 20, 5], [15, 25, 3], [20, 30, 2], [25, 35, 1]]) == 12
    assert candidate(tasks = [[1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5]]) == 5
    assert candidate(tasks = [[1, 5, 1], [2, 6, 1], [3, 7, 1], [4, 8, 1], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 2
    assert candidate(tasks = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5]]) == 4
    assert candidate(tasks = [[1, 20, 5], [2, 19, 5], [3, 18, 5], [4, 17, 5], [5, 16, 5], [6, 15, 5], [7, 14, 5], [8, 13, 5], [9, 12, 5], [10, 11, 5]]) == 5
    assert candidate(tasks = [[1, 1000, 500], [200, 800, 300], [400, 600, 200], [500, 700, 150]]) == 500
    assert candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1], [15, 16, 1], [17, 18, 1], [19, 20, 1]]) == 10
    assert candidate(tasks = [[1, 500, 250], [250, 750, 300], [500, 1000, 350], [750, 1250, 400], [1000, 1500, 450]]) == 1048
    assert candidate(tasks = [[1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3], [1, 10, 3]]) == 3
    assert candidate(tasks = [[1, 10, 3], [2, 9, 5], [3, 8, 4], [4, 7, 1], [5, 6, 2]]) == 5
    assert candidate(tasks = [[1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10], [1, 10, 10]]) == 10
    assert candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 5, 5], [7, 4, 4], [8, 3, 3], [9, 2, 2]]) == 10
    assert candidate(tasks = [[1, 3, 3], [4, 6, 2], [7, 9, 1], [10, 12, 3], [13, 15, 2]]) == 11
    assert candidate(tasks = [[5, 10, 5], [10, 15, 5], [15, 20, 5], [20, 25, 5], [25, 30, 5], [30, 35, 5], [35, 40, 5], [40, 45, 5]]) == 33
    assert candidate(tasks = [[1, 50, 25], [25, 75, 30], [50, 100, 35], [75, 125, 40], [100, 150, 45]]) == 103
    assert candidate(tasks = [[1, 3, 3], [4, 6, 3], [7, 9, 3], [10, 12, 3], [13, 15, 3], [16, 18, 3], [19, 21, 3], [22, 24, 3], [25, 27, 3], [28, 30, 3]]) == 30
    assert candidate(tasks = [[1, 10, 3], [1, 20, 3], [1, 30, 3], [1, 40, 3], [1, 50, 3], [1, 60, 3], [1, 70, 3], [1, 80, 3], [1, 90, 3], [1, 100, 3]]) == 3
    assert candidate(tasks = [[1, 1000, 999], [500, 1500, 1000], [1000, 2000, 1000]]) == 1998
    assert candidate(tasks = [[1, 10, 5], [2, 9, 4], [3, 8, 3], [4, 7, 2], [5, 6, 1], [6, 5, 1], [7, 4, 1], [8, 3, 1], [9, 2, 1], [10, 1, 1]]) == 5
    assert candidate(tasks = [[1, 100, 99], [2, 150, 98], [3, 200, 97], [4, 250, 96], [5, 300, 95], [6, 350, 94], [7, 400, 93], [8, 450, 92], [9, 500, 91]]) == 99
    assert candidate(tasks = [[1, 2, 1], [3, 4, 1], [5, 6, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1], [15, 16, 1], [17, 18, 1], [19, 20, 1], [21, 22, 1], [23, 24, 1], [25, 26, 1], [27, 28, 1], [29, 30, 1]]) == 15
    assert candidate(tasks = [[1, 100, 50], [2, 90, 40], [3, 80, 30], [4, 70, 20], [5, 60, 10], [6, 50, 5], [7, 40, 3], [8, 30, 2], [9, 20, 1]]) == 50
    assert candidate(tasks = [[1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1], [1, 10, 1]]) == 1
    assert candidate(tasks = [[1, 10, 1], [2, 10, 2], [3, 10, 3], [4, 10, 4], [5, 10, 5], [6, 10, 6], [7, 10, 7], [8, 10, 8], [9, 10, 9]]) == 5
    assert candidate(tasks = [[1, 2000, 2000], [10, 500, 400], [150, 800, 300], [300, 1800, 500], [1000, 1900, 600]]) == 2000
    assert candidate(tasks = [[1, 2000, 1000], [2, 1999, 999], [3, 1998, 998], [4, 1997, 997], [5, 1996, 996], [6, 1995, 995], [7, 1994, 994], [8, 1993, 993], [9, 1992, 992], [10, 1991, 991]]) == 1000
    assert candidate(tasks = [[1, 5, 5], [2, 6, 4], [3, 7, 3], [4, 8, 2], [5, 9, 1], [6, 10, 1], [7, 11, 1], [8, 12, 1], [9, 13, 1], [10, 14, 1]]) == 6
    assert candidate(tasks = [[1, 50, 10], [10, 20, 5], [20, 30, 5], [30, 40, 5], [40, 50, 5], [50, 60, 5], [60, 70, 5], [70, 80, 5], [80, 90, 5]]) == 33
    assert candidate(tasks = [[1, 100, 50], [50, 150, 60], [100, 200, 70], [150, 250, 80], [200, 300, 90]]) == 208
    assert candidate(tasks = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1]]) == 5
    assert candidate(tasks = [[1, 10, 10], [2, 9, 9], [3, 8, 8], [4, 7, 7], [5, 6, 6], [6, 7, 5], [7, 8, 4], [8, 9, 3], [9, 10, 2], [10, 10, 1]]) == 10
    assert candidate(tasks = [[50, 150, 100], [100, 200, 100], [150, 250, 100], [200, 300, 100], [250, 350, 100], [300, 400, 100], [350, 450, 100], [400, 500, 100]]) == 446
    assert candidate(tasks = [[1, 10, 1], [2, 11, 2], [3, 12, 3], [4, 13, 4], [5, 14, 5], [6, 15, 6], [7, 16, 7], [8, 17, 8], [9, 18, 9], [10, 19, 10]]) == 10
    assert candidate(tasks = [[1, 5, 1], [6, 10, 1], [11, 15, 1], [16, 20, 1]]) == 4
    assert candidate(tasks = [[1, 100, 100], [50, 150, 50], [100, 200, 30], [150, 250, 20], [200, 300, 10]]) == 138
    assert candidate(tasks = [[1, 5, 5], [2, 6, 5], [3, 7, 5], [4, 8, 5], [5, 9, 5], [6, 10, 5], [7, 11, 5], [8, 12, 5], [9, 13, 5], [10, 14, 5]]) == 14
    assert candidate(tasks = [[1, 2000, 500], [2, 1999, 499], [3, 1998, 498], [4, 1997, 497], [5, 1996, 496], [6, 1995, 495], [7, 1994, 494], [8, 1993, 493], [9, 1992, 492], [10, 1991, 491]]) == 500
    assert candidate(tasks = [[1, 100, 50], [51, 150, 50], [101, 200, 50], [151, 250, 50], [201, 300, 50]]) == 150
    assert candidate(tasks = [[1, 100, 1], [2, 99, 1], [3, 98, 1], [4, 97, 1], [5, 96, 1], [6, 95, 1], [7, 94, 1], [8, 93, 1], [9, 92, 1], [10, 91, 1], [11, 90, 1], [12, 89, 1], [13, 88, 1], [14, 87, 1], [15, 86, 1], [16, 85, 1], [17, 84, 1], [18, 83, 1], [19, 82, 1], [20, 81, 1], [21, 80, 1], [22, 79, 1], [23, 78, 1], [24, 77, 1], [25, 76, 1], [26, 75, 1], [27, 74, 1], [28, 73, 1], [29, 72, 1], [30, 71, 1], [31, 70, 1], [32, 69, 1], [33, 68, 1], [34, 67, 1], [35, 66, 1], [36, 65, 1], [37, 64, 1], [38, 63, 1], [39, 62, 1], [40, 61, 1], [41, 60, 1], [42, 59, 1], [43, 58, 1], [44, 57, 1], [45, 56, 1], [46, 55, 1], [47, 54, 1], [48, 53, 1], [49, 52, 1], [50, 51, 1]]) == 1
    assert candidate(tasks = [[1, 3, 3], [2, 4, 2], [3, 5, 2], [4, 6, 2], [5, 7, 2], [6, 8, 2], [7, 9, 2]]) == 7
    assert candidate(tasks = [[1, 5, 5], [2, 10, 5], [3, 15, 5], [4, 20, 5], [5, 25, 5], [6, 30, 5]]) == 10
    assert candidate(tasks = [[1, 3, 1], [2, 5, 2], [3, 7, 3], [4, 9, 4], [5, 11, 5], [6, 13, 6], [7, 15, 7]]) == 9
    assert candidate(tasks = [[1, 50, 40], [25, 75, 30], [50, 100, 20], [75, 125, 10]]) == 59
    assert candidate(tasks = [[1, 20, 5], [1, 15, 5], [1, 10, 5], [1, 5, 5], [6, 10, 5], [11, 15, 5], [16, 20, 5]]) == 20
    assert candidate(tasks = [[1, 2000, 1000], [500, 1500, 500], [1000, 2000, 500], [1, 500, 100], [1500, 2000, 100]]) == 1000
    assert candidate(tasks = [[1, 2000, 1], [2, 2000, 2], [3, 2000, 3], [4, 2000, 4], [5, 2000, 5], [6, 2000, 6], [7, 2000, 7], [8, 2000, 8], [9, 2000, 9], [10, 2000, 10]]) == 10
    assert candidate(tasks = [[100, 200, 100], [150, 250, 100], [200, 300, 100], [250, 350, 100], [300, 400, 100]]) == 298
    assert candidate(tasks = [[1, 2000, 1000], [2, 1999, 999], [3, 1998, 998], [4, 1997, 997], [5, 1996, 996], [6, 1995, 995], [7, 1994, 994], [8, 1993, 993], [9, 1992, 992], [10, 1991, 991]]) == 1000
    assert candidate(tasks = [[1, 2000, 1000], [1000, 2000, 1000], [500, 1500, 500], [100, 1900, 900]]) == 1000
    assert candidate(tasks = [[1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [1, 8, 1], [1, 9, 1], [1, 10, 1]]) == 1
    assert candidate(tasks = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5], [6, 7, 4], [7, 8, 3], [8, 9, 2], [9, 10, 1]]) == 6
    assert candidate(tasks = [[1, 10, 3], [2, 10, 3], [3, 10, 3], [4, 10, 3], [5, 10, 3], [6, 10, 3], [7, 10, 3], [8, 10, 3], [9, 10, 3], [1, 10, 3]]) == 3
    assert candidate(tasks = [[1, 100, 50], [50, 150, 50], [100, 200, 50], [150, 250, 50], [200, 300, 50]]) == 148
    assert candidate(tasks = [[1, 50, 25], [10, 60, 25], [20, 70, 25], [30, 80, 25], [40, 90, 25], [50, 100, 25], [60, 110, 25], [70, 120, 25], [80, 130, 25], [90, 140, 25]]) == 63
    assert candidate(tasks = [[1, 10, 1], [2, 10, 2], [3, 10, 3], [4, 10, 4], [5, 10, 5], [6, 10, 6], [7, 10, 7], [8, 10, 8], [9, 10, 9], [10, 10, 10]]) == 5
    assert candidate(tasks = [[1, 10, 1], [2, 9, 1], [3, 8, 1], [4, 7, 1], [5, 6, 1], [6, 5, 1], [7, 4, 1], [8, 3, 1], [9, 2, 1], [10, 1, 1]]) == 1
    assert candidate(tasks = [[1, 3, 1], [2, 4, 1], [3, 5, 1], [4, 6, 1], [5, 7, 1]]) == 2
    assert candidate(tasks = [[1, 5, 2], [1, 5, 2], [1, 5, 2], [1, 5, 2], [1, 5, 2]]) == 2
    assert candidate(tasks = [[1, 100, 50], [20, 150, 60], [30, 180, 70], [40, 200, 80]]) == 80
    assert candidate(tasks = [[1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5]]) == 6


