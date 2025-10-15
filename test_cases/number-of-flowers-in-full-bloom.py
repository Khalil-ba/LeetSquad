def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [3, 3]],people = [3, 3, 2]) == [2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [3, 3]],people = [3, 3, 2]) == [2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 100]],people = [50, 100, 150]) == [1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 100]],people = [50, 100, 150]) == [1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4]],people = [1, 2, 3, 4]) == [1, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4]],people = [1, 2, 3, 4]) == [1, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 10], [15, 20], [1, 5]],people = [6, 12, 4]) == [1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 10], [15, 20], [1, 5]],people = [6, 12, 4]) == [1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000]],people = [1, 500000000, 1000000000]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000]],people = [1, 500000000, 1000000000]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 10], [15, 20], [25, 30]],people = [10, 20, 30, 40]) == [1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 10], [15, 20], [25, 30]],people = [10, 20, 30, 40]) == [1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13]],people = [2, 3, 7, 11]) == [1, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13]],people = [2, 3, 7, 11]) == [1, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000]],people = [1, 1000000000]) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000]],people = [1, 1000000000]) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 11], [8, 8], [8, 9], [10, 10], [9, 11], [5, 7]],people = [6, 10, 7]) == [2, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 11], [8, 8], [8, 9], [10, 10], [9, 11], [5, 7]],people = [6, 10, 7]) == [2, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1], [2, 2], [3, 3]],people = [1, 2, 3]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1], [2, 2], [3, 3]],people = [1, 2, 3]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [3, 6, 8, 10, 15]) == [3, 5, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [3, 6, 8, 10, 15]) == [3, 5, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10]],people = [1, 5, 10]) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10]],people = [1, 5, 10]) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],people = [1, 5, 10, 15]) == [1, 2, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],people = [1, 5, 10, 15]) == [1, 2, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [5, 7], [9, 11], [13, 15], [17, 19], [21, 23]],people = [2, 6, 10, 14, 18, 22, 24]) == [1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [5, 7], [9, 11], [13, 15], [17, 19], [21, 23]],people = [2, 6, 10, 14, 18, 22, 24]) == [1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [1, 1, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [1, 1, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997]],people = [1, 2, 3, 4, 999999999, 1000000000]) == [1, 2, 3, 4, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997]],people = [1, 2, 3, 4, 999999999, 1000000000]) == [1, 2, 3, 4, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[100000000, 200000000], [300000000, 400000000], [500000000, 600000000]],people = [150000000, 350000000, 550000000]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[100000000, 200000000], [300000000, 400000000], [500000000, 600000000]],people = [150000000, 350000000, 550000000]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[2, 5], [8, 10], [12, 14], [18, 22], [26, 28], [30, 34]],people = [2, 5, 8, 10, 12, 14, 18, 22, 26, 28, 30, 34]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[2, 5], [8, 10], [12, 14], [18, 22], [26, 28], [30, 34]],people = [2, 5, 8, 10, 12, 14, 18, 22, 26, 28, 30, 34]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [5, 6, 7, 8, 9, 10]) == [5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [5, 6, 7, 8, 9, 10]) == [5, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13], [14, 17], [18, 21], [22, 25]],people = [2, 3, 7, 11, 15, 19, 23]) == [1, 2, 2, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13], [14, 17], [18, 21], [22, 25]],people = [2, 3, 7, 11, 15, 19, 23]) == [1, 2, 2, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300]],people = [1, 50, 100, 150, 200, 250, 300]) == [1, 2, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300]],people = [1, 50, 100, 150, 200, 250, 300]) == [1, 2, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35]],people = [10, 15, 20, 25, 30, 35]) == [2, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35]],people = [10, 15, 20, 25, 30, 35]) == [2, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 20], [20, 30], [10, 25], [15, 35], [25, 40]],people = [10, 15, 20, 25, 30, 35, 40]) == [2, 3, 4, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 20], [20, 30], [10, 25], [15, 35], [25, 40]],people = [10, 15, 20, 25, 30, 35, 40]) == [2, 3, 4, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50]],people = [5, 15, 25, 35, 45, 55]) == [1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50]],people = [5, 15, 25, 35, 45, 55]) == [1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21], [22, 24], [25, 27], [28, 30]],people = [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21], [22, 24], [25, 27], [28, 30]],people = [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]],people = [2, 6, 10, 14, 18, 22]) == [1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]],people = [2, 6, 10, 14, 18, 22]) == [1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]],people = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]],people = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]],people = [3, 8, 13, 18, 23]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]],people = [3, 8, 13, 18, 23]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 3, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 3, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13], [10, 15], [16, 20], [21, 25], [26, 30]],people = [2, 5, 6, 7, 10, 15, 20, 25, 30]) == [1, 3, 3, 2, 3, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13], [10, 15], [16, 20], [21, 25], [26, 30]],people = [2, 5, 6, 7, 10, 15, 20, 25, 30]) == [1, 3, 3, 2, 3, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 15], [15, 20], [20, 25], [25, 30]],people = [12, 17, 22, 27]) == [1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 15], [15, 20], [20, 25], [25, 30]],people = [12, 17, 22, 27]) == [1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]],people = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]],people = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000], [500, 1500], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000], [3500, 4500], [4000, 5000], [4500, 5500]],people = [1, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000], [500, 1500], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000], [3500, 4500], [4000, 5000], [4500, 5500]],people = [1, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [2, 3], [4, 6], [7, 8], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [2, 3], [4, 6], [7, 8], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 300000000], [500000000, 1000000000], [700000000, 900000000], [800000000, 1000000000], [900000000, 1100000000]],people = [100000000, 300000000, 500000000, 700000000, 900000000, 1100000000]) == [1, 1, 1, 2, 4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 300000000], [500000000, 1000000000], [700000000, 900000000], [800000000, 1000000000], [900000000, 1100000000]],people = [100000000, 300000000, 500000000, 700000000, 900000000, 1100000000]) == [1, 1, 1, 2, 4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50]],people = [5, 15, 25, 35, 45]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50]],people = [5, 15, 25, 35, 45]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [100000001, 2000000000], [2000000001, 3000000000], [3000000001, 4000000000], [4000000001, 5000000000]],people = [500000000, 1500000000, 2500000000, 3500000000, 4500000000, 5500000000]) == [2, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [100000001, 2000000000], [2000000001, 3000000000], [3000000001, 4000000000], [4000000001, 5000000000]],people = [500000000, 1500000000, 2500000000, 3500000000, 4500000000, 5500000000]) == [2, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [2, 9], [6, 8], [4, 7], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 3, 3, 3, 3, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [2, 9], [6, 8], [4, 7], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 3, 3, 3, 3, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[2, 11], [4, 12], [8, 15], [9, 16], [10, 17]],people = [5, 10, 15, 20]) == [2, 5, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[2, 11], [4, 12], [8, 15], [9, 16], [10, 17]],people = [5, 10, 15, 20]) == [2, 5, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 500000000], [500000000, 1000000000]],people = [1, 250000000, 500000000, 750000000, 1000000000]) == [1, 2, 3, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 500000000], [500000000, 1000000000]],people = [1, 250000000, 500000000, 750000000, 1000000000]) == [1, 2, 3, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],people = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],people = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 6]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],people = [1, 5, 10]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],people = [1, 5, 10]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995]],people = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 999999995, 999999997, 1000000000]) == [1, 3, 5, 6, 6, 6, 6, 6, 6, 6, 6, 4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995]],people = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 999999995, 999999997, 1000000000]) == [1, 3, 5, 6, 6, 6, 6, 6, 6, 6, 6, 4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [5, 15], [10, 20], [15, 25], [20, 30]],people = [1, 6, 11, 16, 21]) == [1, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [5, 15], [10, 20], [15, 25], [20, 30]],people = [1, 6, 11, 16, 21]) == [1, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 12], [12, 14], [14, 16], [16, 18], [18, 20], [20, 22], [22, 24], [24, 26], [26, 28]],people = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]) == [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 12], [12, 14], [14, 16], [16, 18], [18, 20], [20, 22], [22, 24], [24, 26], [26, 28]],people = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]) == [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [2, 8], [3, 9], [10, 15], [12, 18], [16, 20]],people = [1, 3, 5, 7, 10, 12, 15, 18, 20]) == [1, 3, 3, 2, 1, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [2, 8], [3, 9], [10, 15], [12, 18], [16, 20]],people = [1, 3, 5, 7, 10, 12, 15, 18, 20]) == [1, 3, 3, 2, 1, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 500000000], [500000001, 1000000000]],people = [250000000, 750000000, 1000000000]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 500000000], [500000001, 1000000000]],people = [250000000, 750000000, 1000000000]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000]],people = [1, 1000000000, 2000000000]) == [10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000]],people = [1, 1000000000, 2000000000]) == [10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000]],people = [1, 500, 1000]) == [10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000]],people = [1, 500, 1000]) == [10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20]],people = [5, 15, 25]) == [0, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20]],people = [5, 15, 25]) == [0, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 6], [6, 11], [11, 16], [16, 21]],people = [1, 5, 6, 10, 11, 15, 16, 20, 21]) == [1, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 6], [6, 11], [11, 16], [16, 21]],people = [1, 5, 6, 10, 11, 15, 16, 20, 21]) == [1, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160], [160, 170], [170, 180], [180, 190]],people = [105, 115, 125, 135, 145, 155, 165, 175, 185]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160], [160, 170], [170, 180], [180, 190]],people = [105, 115, 125, 135, 145, 155, 165, 175, 185]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21]],people = [2, 5, 8, 11, 14, 17, 20]) == [1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21]],people = [2, 5, 8, 11, 14, 17, 20]) == [1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 2, 3, 4, 5, 1000000000, 999999999, 999999998, 999999997, 999999996]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 2, 3, 4, 5, 1000000000, 999999999, 999999998, 999999997, 999999996]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10000], [10001, 20000], [20001, 30000], [30001, 40000], [40001, 50000]],people = [5000, 15000, 25000, 35000, 45000]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10000], [10001, 20000], [20001, 30000], [30001, 40000], [40001, 50000]],people = [5000, 15000, 25000, 35000, 45000]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 500000000, 1000000000]) == [1, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 500000000, 1000000000]) == [1, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 100], [10, 90], [20, 80], [30, 70], [40, 60], [50, 50]],people = [1, 50, 100, 150]) == [1, 6, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 100], [10, 90], [20, 80], [30, 70], [40, 60], [50, 50]],people = [1, 50, 100, 150]) == [1, 6, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350]],people = [50, 100, 150, 200, 250, 300, 350]) == [2, 3, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350]],people = [50, 100, 150, 200, 250, 300, 350]) == [2, 3, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[100, 200], [150, 250], [200, 300], [250, 350], [300, 400]],people = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == [0, 1, 2, 3, 3, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[100, 200], [150, 250], [200, 300], [250, 350], [300, 400]],people = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == [0, 1, 2, 3, 3, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5]) == [10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5]) == [10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]],people = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]],people = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995], [7, 999999994], [8, 999999993], [9, 999999992], [10, 999999991]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995], [7, 999999994], [8, 999999993], [9, 999999992], [10, 999999991]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]],people = [3, 8, 13, 18, 23, 28]) == [1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]],people = [3, 8, 13, 18, 23, 28]) == [1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [10, 15], [20, 25], [30, 35], [40, 45]],people = [3, 8, 13, 18, 23, 28, 33, 38, 43]) == [1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [10, 15], [20, 25], [30, 35], [40, 45]],people = [3, 8, 13, 18, 23, 28, 33, 38, 43]) == [1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995], [7, 999999994], [8, 999999993], [9, 999999992], [10, 999999991]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999999991, 999999992, 999999993, 999999994, 999999995, 999999996, 999999997, 999999998, 999999999, 1000000000]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995], [7, 999999994], [8, 999999993], [9, 999999992], [10, 999999991]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999999991, 999999992, 999999993, 999999994, 999999995, 999999996, 999999997, 999999998, 999999999, 1000000000]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]],people = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]],people = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35]],people = [5, 8, 10, 12, 15, 18, 20, 23, 25, 28, 30]) == [1, 1, 2, 2, 3, 2, 3, 2, 3, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35]],people = [5, 8, 10, 12, 15, 18, 20, 23, 25, 28, 30]) == [1, 1, 2, 2, 3, 2, 3, 2, 3, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 5, 9]) == [1, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 5, 9]) == [1, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 5], [10, 20], [25, 35], [40, 50], [55, 60]],people = [5, 15, 25, 35, 45, 55, 60]) == [1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 5], [10, 20], [25, 35], [40, 50], [55, 60]],people = [5, 15, 25, 35, 45, 55, 60]) == [1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]],people = [8, 13, 18, 23, 28, 33]) == [1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]],people = [8, 13, 18, 23, 28, 33]) == [1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000]) == [10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000]) == [10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 500000000, 1000000000]) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 500000000, 1000000000]) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],people = [1, 2, 3, 4, 5]) == [5, 5, 5, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],people = [1, 2, 3, 4, 5]) == [5, 5, 5, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],people = [1, 5, 9, 13, 17, 20]) == [1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],people = [1, 5, 9, 13, 17, 20]) == [1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 3, 5, 7, 9]) == [1, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 3, 5, 7, 9]) == [1, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50]],people = [5, 15, 25, 35, 45, 55, 1, 11, 21, 31, 41]) == [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50]],people = [5, 15, 25, 35, 45, 55, 1, 11, 21, 31, 41]) == [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(flowers = [[1, 10], [3, 3]],people = [3, 3, 2]) == [2, 2, 1]
    assert candidate(flowers = [[1, 100]],people = [50, 100, 150]) == [1, 1, 0]
    assert candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4]],people = [1, 2, 3, 4]) == [1, 2, 2, 1]
    assert candidate(flowers = [[5, 10], [15, 20], [1, 5]],people = [6, 12, 4]) == [1, 0, 1]
    assert candidate(flowers = [[1, 1000000000]],people = [1, 500000000, 1000000000]) == [1, 1, 1]
    assert candidate(flowers = [[5, 10], [15, 20], [25, 30]],people = [10, 20, 30, 40]) == [1, 1, 1, 0]
    assert candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13]],people = [2, 3, 7, 11]) == [1, 2, 2, 2]
    assert candidate(flowers = [[1, 1000000000]],people = [1, 1000000000]) == [1, 1]
    assert candidate(flowers = [[5, 11], [8, 8], [8, 9], [10, 10], [9, 11], [5, 7]],people = [6, 10, 7]) == [2, 3, 2]
    assert candidate(flowers = [[1, 1], [2, 2], [3, 3]],people = [1, 2, 3]) == [1, 1, 1]
    assert candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [3, 6, 8, 10, 15]) == [3, 5, 3, 1, 0]
    assert candidate(flowers = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10]],people = [1, 5, 10]) == [5, 5, 5]
    assert candidate(flowers = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(flowers = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],people = [1, 5, 10, 15]) == [1, 2, 2, 0]
    assert candidate(flowers = [[1, 3], [5, 7], [9, 11], [13, 15], [17, 19], [21, 23]],people = [2, 6, 10, 14, 18, 22, 24]) == [1, 1, 1, 1, 1, 1, 0]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [1, 1, 5, 5, 5]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997]],people = [1, 2, 3, 4, 999999999, 1000000000]) == [1, 2, 3, 4, 2, 1]
    assert candidate(flowers = [[100000000, 200000000], [300000000, 400000000], [500000000, 600000000]],people = [150000000, 350000000, 550000000]) == [1, 1, 1]
    assert candidate(flowers = [[2, 5], [8, 10], [12, 14], [18, 22], [26, 28], [30, 34]],people = [2, 5, 8, 10, 12, 14, 18, 22, 26, 28, 30, 34]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [5, 6, 7, 8, 9, 10]) == [5, 5, 4, 3, 2, 1]
    assert candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13], [14, 17], [18, 21], [22, 25]],people = [2, 3, 7, 11, 15, 19, 23]) == [1, 2, 2, 2, 1, 1, 1]
    assert candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300]],people = [1, 50, 100, 150, 200, 250, 300]) == [1, 2, 3, 3, 3, 2, 1]
    assert candidate(flowers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35]],people = [10, 15, 20, 25, 30, 35]) == [2, 3, 3, 3, 2, 1]
    assert candidate(flowers = [[5, 20], [20, 30], [10, 25], [15, 35], [25, 40]],people = [10, 15, 20, 25, 30, 35, 40]) == [2, 3, 4, 4, 3, 2, 1]
    assert candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50]],people = [5, 15, 25, 35, 45, 55]) == [1, 1, 1, 1, 1, 0]
    assert candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21], [22, 24], [25, 27], [28, 30]],people = [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]],people = [2, 6, 10, 14, 18, 22]) == [1, 1, 1, 1, 1, 0]
    assert candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]],people = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]],people = [3, 8, 13, 18, 23]) == [1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 3, 3, 3, 3, 2, 1]
    assert candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]
    assert candidate(flowers = [[1, 6], [3, 7], [9, 12], [4, 13], [10, 15], [16, 20], [21, 25], [26, 30]],people = [2, 5, 6, 7, 10, 15, 20, 25, 30]) == [1, 3, 3, 2, 3, 1, 1, 1, 1]
    assert candidate(flowers = [[10, 15], [15, 20], [20, 25], [25, 30]],people = [12, 17, 22, 27]) == [1, 1, 1, 1]
    assert candidate(flowers = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]],people = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 1000], [500, 1500], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000], [3500, 4500], [4000, 5000], [4500, 5500]],people = [1, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2]
    assert candidate(flowers = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(flowers = [[1, 5], [2, 3], [4, 6], [7, 8], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 300000000], [500000000, 1000000000], [700000000, 900000000], [800000000, 1000000000], [900000000, 1100000000]],people = [100000000, 300000000, 500000000, 700000000, 900000000, 1100000000]) == [1, 1, 1, 2, 4, 1]
    assert candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50]],people = [5, 15, 25, 35, 45]) == [1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 1000000000], [100000001, 2000000000], [2000000001, 3000000000], [3000000001, 4000000000], [4000000001, 5000000000]],people = [500000000, 1500000000, 2500000000, 3500000000, 4500000000, 5500000000]) == [2, 1, 1, 1, 1, 0]
    assert candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5]
    assert candidate(flowers = [[1, 5], [2, 9], [6, 8], [4, 7], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 3, 3, 3, 3, 2, 2, 1]
    assert candidate(flowers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    assert candidate(flowers = [[2, 11], [4, 12], [8, 15], [9, 16], [10, 17]],people = [5, 10, 15, 20]) == [2, 5, 3, 0]
    assert candidate(flowers = [[1, 1000000000], [2, 500000000], [500000000, 1000000000]],people = [1, 250000000, 500000000, 750000000, 1000000000]) == [1, 2, 3, 2, 2]
    assert candidate(flowers = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],people = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 6]
    assert candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],people = [1, 5, 10]) == [1, 1, 1]
    assert candidate(flowers = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995]],people = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 999999995, 999999997, 1000000000]) == [1, 3, 5, 6, 6, 6, 6, 6, 6, 6, 6, 4, 1]
    assert candidate(flowers = [[1, 10], [5, 15], [10, 20], [15, 25], [20, 30]],people = [1, 6, 11, 16, 21]) == [1, 2, 2, 2, 2]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(flowers = [[10, 12], [12, 14], [14, 16], [16, 18], [18, 20], [20, 22], [22, 24], [24, 26], [26, 28]],people = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]) == [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert candidate(flowers = [[1, 5], [2, 8], [3, 9], [10, 15], [12, 18], [16, 20]],people = [1, 3, 5, 7, 10, 12, 15, 18, 20]) == [1, 3, 3, 2, 1, 2, 2, 2, 1]
    assert candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 500000000], [500000001, 1000000000]],people = [250000000, 750000000, 1000000000]) == [1, 1, 1]
    assert candidate(flowers = [[1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000], [1, 2000000000]],people = [1, 1000000000, 2000000000]) == [10, 10, 10]
    assert candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000]],people = [1, 500, 1000]) == [10, 10, 10]
    assert candidate(flowers = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(flowers = [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20]],people = [5, 15, 25]) == [0, 10, 0]
    assert candidate(flowers = [[1, 6], [6, 11], [11, 16], [16, 21]],people = [1, 5, 6, 10, 11, 15, 16, 20, 21]) == [1, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(flowers = [[100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160], [160, 170], [170, 180], [180, 190]],people = [105, 115, 125, 135, 145, 155, 165, 175, 185]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18], [19, 21]],people = [2, 5, 8, 11, 14, 17, 20]) == [1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 2, 3, 4, 5, 1000000000, 999999999, 999999998, 999999997, 999999996]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert candidate(flowers = [[1, 10000], [10001, 20000], [20001, 30000], [30001, 40000], [40001, 50000]],people = [5000, 15000, 25000, 35000, 45000]) == [1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996]],people = [1, 500000000, 1000000000]) == [1, 5, 1]
    assert candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [10, 10, 10, 10, 10]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(flowers = [[1, 100], [10, 90], [20, 80], [30, 70], [40, 60], [50, 50]],people = [1, 50, 100, 150]) == [1, 6, 1, 0]
    assert candidate(flowers = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350]],people = [50, 100, 150, 200, 250, 300, 350]) == [2, 3, 3, 3, 3, 2, 1]
    assert candidate(flowers = [[100, 200], [150, 250], [200, 300], [250, 350], [300, 400]],people = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == [0, 1, 2, 3, 3, 3, 2, 1, 0]
    assert candidate(flowers = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],people = [1, 2, 3, 4, 5]) == [10, 10, 10, 10, 10]
    assert candidate(flowers = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
    assert candidate(flowers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]],people = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995], [7, 999999994], [8, 999999993], [9, 999999992], [10, 999999991]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(flowers = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]],people = [3, 8, 13, 18, 23, 28]) == [1, 1, 1, 1, 1, 0]
    assert candidate(flowers = [[1, 5], [10, 15], [20, 25], [30, 35], [40, 45]],people = [3, 8, 13, 18, 23, 28, 33, 38, 43]) == [1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(flowers = [[1, 1000000000], [2, 999999999], [3, 999999998], [4, 999999997], [5, 999999996], [6, 999999995], [7, 999999994], [8, 999999993], [9, 999999992], [10, 999999991]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999999991, 999999992, 999999993, 999999994, 999999995, 999999996, 999999997, 999999998, 999999999, 1000000000]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(flowers = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]],people = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
    assert candidate(flowers = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35]],people = [5, 8, 10, 12, 15, 18, 20, 23, 25, 28, 30]) == [1, 1, 2, 2, 3, 2, 3, 2, 3, 2, 2]
    assert candidate(flowers = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 5, 9]) == [1, 2, 2]
    assert candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]],people = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 5], [10, 20], [25, 35], [40, 50], [55, 60]],people = [5, 15, 25, 35, 45, 55, 60]) == [1, 1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]],people = [8, 13, 18, 23, 28, 33]) == [1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000]) == [10, 10]
    assert candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 500000000, 1000000000]) == [5, 5, 5]
    assert candidate(flowers = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]],people = [1, 2, 3, 4, 5]) == [5, 5, 5, 0, 0]
    assert candidate(flowers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],people = [1, 5, 9, 13, 17, 20]) == [1, 1, 1, 1, 1, 1]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 3, 5, 7, 9]) == [1, 2, 2, 2, 2]
    assert candidate(flowers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(flowers = [[1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000], [1, 1000000000]],people = [1, 1000000000, 500000000, 250000000, 750000000]) == [5, 5, 5, 5, 5]
    assert candidate(flowers = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50]],people = [5, 15, 25, 35, 45, 55, 1, 11, 21, 31, 41]) == [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]


