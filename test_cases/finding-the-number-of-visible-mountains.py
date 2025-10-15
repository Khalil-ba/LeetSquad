def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [5, 5], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [5, 5], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[100, 100], [200, 50], [300, 100]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[100, 100], [200, 50], [300, 100]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [15, 5], [20, 15]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [15, 5], [20, 15]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [15, 5], [20, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [15, 5], [20, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [5, 6], [5, 7]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [5, 6], [5, 7]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[2, 2], [6, 3], [5, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[2, 2], [6, 3], [5, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 3], [1, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 3], [1, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [4, 4], [7, 7]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [4, 4], [7, 7]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [6, 3], [7, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [6, 3], [7, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [5, 5], [15, 15]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [5, 5], [15, 15]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[3, 3], [3, 3], [3, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[3, 3], [3, 3], [3, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [15, 5], [5, 5], [20, 15]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [15, 5], [5, 5], [20, 15]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [11, 10], [21, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [11, 10], [21, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[3, 5], [6, 5], [9, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[3, 5], [6, 5], [9, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[3, 5], [2, 2], [4, 4], [6, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[3, 5], [2, 2], [4, 4], [6, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [2, 3], [3, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [2, 3], [3, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10], [50, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10], [50, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [3, 4], [5, 6], [7, 8], [9, 5], [11, 7]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [3, 4], [5, 6], [7, 8], [9, 5], [11, 7]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[100000, 1], [100000, 2], [100000, 3], [100000, 4], [100000, 5], [100000, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[100000, 1], [100000, 2], [100000, 3], [100000, 4], [100000, 5], [100000, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [15, 10], [25, 10], [35, 10], [45, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [15, 10], [25, 10], [35, 10], [45, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [11, 11], [12, 10], [13, 11], [14, 10], [15, 11], [16, 10], [17, 11], [18, 10], [19, 11]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [11, 11], [12, 10], [13, 11], [14, 10], [15, 11], [16, 10], [17, 11], [18, 10], [19, 11]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [20, 15], [30, 25], [40, 35], [50, 45], [60, 55], [70, 65], [80, 75], [90, 85], [100, 95]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [20, 15], [30, 25], [40, 35], [50, 45], [60, 55], [70, 65], [80, 75], [90, 85], [100, 95]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [100000, 1], [50000, 50000], [25000, 25000], [75000, 25000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [100000, 1], [50000, 50000], [25000, 25000], [75000, 25000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 10], [15, 20], [15, 15], [25, 15], [30, 20], [5, 5], [35, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 10], [15, 20], [15, 15], [25, 15], [30, 20], [5, 5], [35, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [10, 15], [15, 10], [20, 15], [25, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [10, 15], [15, 10], [20, 15], [25, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [15, 15], [20, 5], [25, 15], [30, 5], [35, 15], [40, 5], [45, 15], [50, 5], [55, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [15, 15], [20, 5], [25, 15], [30, 5], [35, 15], [40, 5], [45, 15], [50, 5], [55, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [10, 10], [100, 100], [1000, 1000], [10000, 10000], [100000, 100000], [100000, 100000], [10000, 10000], [1000, 1000], [100, 100], [10, 10], [1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [10, 10], [100, 100], [1000, 1000], [10000, 10000], [100000, 100000], [100000, 100000], [10000, 10000], [1000, 1000], [100, 100], [10, 10], [1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [15, 15], [20, 5], [25, 15], [30, 5], [35, 15]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [15, 15], [20, 5], [25, 15], [30, 5], [35, 15]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 20], [30, 10], [40, 20], [50, 10], [60, 20], [70, 10], [80, 20], [90, 10], [100, 20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 20], [30, 10], [40, 20], [50, 10], [60, 20], [70, 10], [80, 20], [90, 10], [100, 20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3], [7, 1], [8, 3], [9, 1], [10, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3], [7, 1], [8, 3], [9, 1], [10, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [5, 5], [9, 1], [13, 5], [17, 10], [21, 5], [25, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [5, 5], [9, 1], [13, 5], [17, 10], [21, 5], [25, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[100, 100], [150, 150], [200, 200], [250, 250], [300, 300]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[100, 100], [150, 150], [200, 200], [250, 250], [300, 300]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [3, 5], [5, 5], [7, 5], [9, 5], [11, 5], [13, 5], [15, 5], [17, 5], [19, 5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [3, 5], [5, 5], [7, 5], [9, 5], [11, 5], [13, 5], [15, 5], [17, 5], [19, 5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91], [11, 90], [12, 89], [13, 88], [14, 87], [15, 86], [16, 85], [17, 84], [18, 83], [19, 82], [20, 81]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91], [11, 90], [12, 89], [13, 88], [14, 87], [15, 86], [16, 85], [17, 84], [18, 83], [19, 82], [20, 81]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 3], [3, 1], [5, 3], [7, 1], [9, 3], [11, 1], [13, 3], [15, 1], [17, 3], [19, 1], [21, 3], [23, 1], [25, 3], [27, 1], [29, 3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 3], [3, 1], [5, 3], [7, 1], [9, 3], [11, 1], [13, 3], [15, 1], [17, 3], [19, 1], [21, 3], [23, 1], [25, 3], [27, 1], [29, 3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19], [11, 20], [12, 21], [13, 22], [14, 23], [15, 24]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19], [11, 20], [12, 21], [13, 22], [14, 23], [15, 24]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [15, 5], [25, 5], [35, 5], [45, 5], [55, 5], [65, 5], [75, 5], [85, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [15, 5], [25, 5], [35, 5], [45, 5], [55, 5], [65, 5], [75, 5], [85, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [5, 5], [9, 9], [13, 13], [17, 17], [21, 21], [25, 25], [29, 29]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [5, 5], [9, 9], [13, 13], [17, 17], [21, 21], [25, 25], [29, 29]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3], [7, 1], [8, 3], [9, 1], [10, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3], [7, 1], [8, 3], [9, 1], [10, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[50000, 50000], [60000, 50000], [70000, 50000], [80000, 50000]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[50000, 50000], [60000, 50000], [70000, 50000], [80000, 50000]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [10, 10], [2, 2], [9, 9], [3, 3], [8, 8], [4, 4], [7, 7], [5, 5], [6, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [10, 10], [2, 2], [9, 9], [3, 3], [8, 8], [4, 4], [7, 7], [5, 5], [6, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 1], [15, 1], [25, 1], [35, 1], [45, 1], [55, 1], [65, 1], [75, 1], [85, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 1], [15, 1], [25, 1], [35, 1], [45, 1], [55, 1], [65, 1], [75, 1], [85, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 20], [15, 15], [20, 10], [25, 5], [30, 10], [35, 15], [40, 20], [45, 15], [50, 10], [55, 5], [60, 10], [65, 15], [70, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 20], [15, 15], [20, 10], [25, 5], [30, 10], [35, 15], [40, 20], [45, 15], [50, 10], [55, 5], [60, 10], [65, 15], [70, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 2], [12, 3], [13, 4], [14, 5], [15, 6], [16, 7], [17, 8], [18, 9], [19, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 2], [12, 3], [13, 4], [14, 5], [15, 6], [16, 7], [17, 8], [18, 9], [19, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [15, 5], [10, 10], [20, 5], [12, 8]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [15, 5], [10, 10], [20, 5], [12, 8]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 100], [20, 50], [30, 100], [40, 50], [50, 100], [60, 50], [70, 100]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 100], [20, 50], [30, 100], [40, 50], [50, 100], [60, 50], [70, 100]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [3, 10], [5, 1], [7, 5], [9, 1], [11, 6], [13, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [3, 10], [5, 1], [7, 5], [9, 1], [11, 6], [13, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100], [100, 100], [100, 1], [1, 1], [50, 50], [75, 25], [25, 75]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100], [100, 100], [100, 1], [1, 1], [50, 50], [75, 25], [25, 75]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 10], [12, 9], [13, 8], [14, 7], [15, 6], [16, 5], [17, 4], [18, 3], [19, 2], [20, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 10], [12, 9], [13, 8], [14, 7], [15, 6], [16, 5], [17, 4], [18, 3], [19, 2], [20, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [10, 1], [2, 8], [9, 2], [5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [10, 1], [2, 8], [9, 2], [5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 50], [20, 20], [30, 50], [40, 20], [50, 50], [60, 20], [70, 50], [80, 20], [90, 50]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 50], [20, 20], [30, 50], [40, 20], [50, 50], [60, 20], [70, 50], [80, 20], [90, 50]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 15], [20, 25], [30, 15], [40, 25], [50, 15], [60, 25], [70, 15], [80, 25], [90, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 15], [20, 25], [30, 15], [40, 25], [50, 15], [60, 25], [70, 15], [80, 25], [90, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 30], [30, 50], [40, 30], [50, 10], [60, 30], [70, 50]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 30], [30, 50], [40, 30], [50, 10], [60, 30], [70, 50]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 20], [15, 10], [25, 20], [35, 10], [45, 20], [55, 10], [65, 20], [75, 10], [85, 20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 20], [15, 10], [25, 20], [35, 10], [45, 20], [55, 10], [65, 20], [75, 10], [85, 20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 5], [15, 10], [20, 15], [25, 20], [30, 25], [35, 30]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 5], [15, 10], [20, 15], [25, 20], [30, 25], [35, 30]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 100], [20, 100], [30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 100], [20, 100], [30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 1], [10, 2], [15, 3], [20, 4], [25, 5], [30, 6], [35, 7], [40, 8], [45, 9], [50, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 1], [10, 2], [15, 3], [20, 4], [25, 5], [30, 6], [35, 7], [40, 8], [45, 9], [50, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10], [60, 10], [70, 10], [80, 10], [90, 10], [100, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10], [60, 10], [70, 10], [80, 10], [90, 10], [100, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [11, 9], [12, 8], [13, 7], [14, 6], [15, 5], [16, 4], [17, 3], [18, 2], [19, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [11, 9], [12, 8], [13, 7], [14, 6], [15, 5], [16, 4], [17, 3], [18, 2], [19, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 25], [10, 20], [15, 25], [20, 20], [25, 25], [30, 20], [35, 25], [40, 20], [45, 25], [50, 20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 25], [10, 20], [15, 25], [20, 20], [25, 25], [30, 20], [35, 25], [40, 20], [45, 25], [50, 20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [10, 10], [1, 2], [10, 9], [1, 3], [10, 8], [1, 4], [10, 7], [1, 5], [10, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [10, 10], [1, 2], [10, 9], [1, 3], [10, 8], [1, 4], [10, 7], [1, 5], [10, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [15, 10], [20, 10], [12, 15], [17, 15], [22, 15], [14, 20], [19, 20], [24, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [15, 10], [20, 10], [12, 15], [17, 15], [22, 15], [14, 20], [19, 20], [24, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 10], [15, 10], [25, 10], [35, 10], [45, 10], [55, 10], [65, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 10], [15, 10], [25, 10], [35, 10], [45, 10], [55, 10], [65, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 10], [10, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 10], [10, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [20, 15], [25, 5], [30, 20], [40, 10], [50, 25]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [20, 15], [25, 5], [30, 20], [40, 10], [50, 25]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [5, 5], [9, 9], [13, 13], [17, 17], [21, 21], [25, 25], [29, 29]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [5, 5], [9, 9], [13, 13], [17, 17], [21, 21], [25, 25], [29, 29]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100000], [100000, 1], [1, 1], [100000, 100000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100000], [100000, 1], [1, 1], [100000, 100000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5], [6, 6], [6, 6], [7, 7], [7, 7], [8, 8], [8, 8], [9, 9], [9, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5], [6, 6], [6, 6], [7, 7], [7, 7], [8, 8], [8, 8], [9, 9], [9, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100], [5, 50], [10, 100], [15, 50], [20, 100], [25, 50], [30, 100]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100], [5, 50], [10, 100], [15, 50], [20, 100], [25, 50], [30, 100]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [2, 6], [3, 5], [4, 6], [5, 5], [6, 6], [7, 5], [8, 6], [9, 5], [10, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [2, 6], [3, 5], [4, 6], [5, 5], [6, 6], [7, 5], [8, 6], [9, 5], [10, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 3], [10, 6], [15, 9], [20, 12], [25, 15], [30, 18], [35, 21], [40, 24], [45, 27], [50, 30]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 3], [10, 6], [15, 9], [20, 12], [25, 15], [30, 18], [35, 21], [40, 24], [45, 27], [50, 30]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [6, 6], [7, 5], [8, 6], [9, 5], [10, 6], [11, 5], [12, 6], [13, 5], [14, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [6, 6], [7, 5], [8, 6], [9, 5], [10, 6], [11, 5], [12, 6], [13, 5], [14, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 8], [7, 6], [8, 4], [9, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 8], [7, 6], [8, 4], [9, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 5], [4, 5], [7, 5], [10, 5], [13, 5], [16, 5], [19, 5]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 5], [4, 5], [7, 5], [10, 5], [13, 5], [16, 5], [19, 5]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[100, 100], [200, 200], [150, 150], [250, 250], [175, 175], [225, 225], [275, 275], [325, 325]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[100, 100], [200, 200], [150, 150], [250, 250], [175, 175], [225, 225], [275, 275], [325, 325]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[10, 10], [10, 10], [20, 20], [20, 20], [30, 30], [30, 30]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[10, 10], [10, 10], [20, 20], [20, 20], [30, 30], [30, 30]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(peaks = [[1, 50], [10, 50], [20, 50], [30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(peaks = [[1, 50], [10, 50], [20, 50], [30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50]]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(peaks = [[5, 5], [5, 5], [5, 5]]) == 0
    assert candidate(peaks = [[100, 100], [200, 50], [300, 100]]) == 3
    assert candidate(peaks = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 1
    assert candidate(peaks = [[10, 10], [15, 5], [20, 15]]) == 2
    assert candidate(peaks = [[10, 10], [15, 5], [20, 10]]) == 2
    assert candidate(peaks = [[5, 5], [5, 6], [5, 7]]) == 1
    assert candidate(peaks = [[2, 2], [6, 3], [5, 4]]) == 2
    assert candidate(peaks = [[1, 3], [1, 3]]) == 0
    assert candidate(peaks = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 1
    assert candidate(peaks = [[1, 1], [4, 4], [7, 7]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3]]) == 1
    assert candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 1
    assert candidate(peaks = [[5, 5], [6, 3], [7, 4]]) == 2
    assert candidate(peaks = [[10, 10], [5, 5], [15, 15]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 1
    assert candidate(peaks = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 1
    assert candidate(peaks = [[3, 3], [3, 3], [3, 3]]) == 0
    assert candidate(peaks = [[10, 10], [15, 5], [5, 5], [20, 15]]) == 2
    assert candidate(peaks = [[1, 10], [11, 10], [21, 10]]) == 3
    assert candidate(peaks = [[3, 5], [6, 5], [9, 5]]) == 3
    assert candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 1
    assert candidate(peaks = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 1
    assert candidate(peaks = [[3, 5], [2, 2], [4, 4], [6, 6]]) == 2
    assert candidate(peaks = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]) == 1
    assert candidate(peaks = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 1
    assert candidate(peaks = [[1, 5], [2, 3], [3, 5]]) == 2
    assert candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10], [50, 5]]) == 5
    assert candidate(peaks = [[1, 10], [3, 4], [5, 6], [7, 8], [9, 5], [11, 7]]) == 3
    assert candidate(peaks = [[100000, 1], [100000, 2], [100000, 3], [100000, 4], [100000, 5], [100000, 6]]) == 1
    assert candidate(peaks = [[5, 10], [15, 10], [25, 10], [35, 10], [45, 10]]) == 5
    assert candidate(peaks = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
    assert candidate(peaks = [[10, 10], [11, 11], [12, 10], [13, 11], [14, 10], [15, 11], [16, 10], [17, 11], [18, 10], [19, 11]]) == 5
    assert candidate(peaks = [[10, 5], [20, 15], [30, 25], [40, 35], [50, 45], [60, 55], [70, 65], [80, 75], [90, 85], [100, 95]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 1
    assert candidate(peaks = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45]]) == 9
    assert candidate(peaks = [[10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10]]) == 3
    assert candidate(peaks = [[1, 1], [100000, 1], [50000, 50000], [25000, 25000], [75000, 25000]]) == 2
    assert candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == 1
    assert candidate(peaks = [[10, 10], [20, 10], [15, 20], [15, 15], [25, 15], [30, 20], [5, 5], [35, 5]]) == 2
    assert candidate(peaks = [[5, 10], [10, 15], [15, 10], [20, 15], [25, 10]]) == 2
    assert candidate(peaks = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 1
    assert candidate(peaks = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]) == 1
    assert candidate(peaks = [[10, 5], [15, 15], [20, 5], [25, 15], [30, 5], [35, 15], [40, 5], [45, 15], [50, 5], [55, 15]]) == 5
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9]]) == 1
    assert candidate(peaks = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 1
    assert candidate(peaks = [[1, 1], [10, 10], [100, 100], [1000, 1000], [10000, 10000], [100000, 100000], [100000, 100000], [10000, 10000], [1000, 1000], [100, 100], [10, 10], [1, 1]]) == 0
    assert candidate(peaks = [[10, 5], [15, 15], [20, 5], [25, 15], [30, 5], [35, 15]]) == 3
    assert candidate(peaks = [[10, 10], [20, 20], [30, 10], [40, 20], [50, 10], [60, 20], [70, 10], [80, 20], [90, 10], [100, 20]]) == 5
    assert candidate(peaks = [[1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3], [7, 1], [8, 3], [9, 1], [10, 3]]) == 5
    assert candidate(peaks = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23]]) == 1
    assert candidate(peaks = [[1, 10], [5, 5], [9, 1], [13, 5], [17, 10], [21, 5], [25, 1]]) == 2
    assert candidate(peaks = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10]]) == 10
    assert candidate(peaks = [[100, 100], [150, 150], [200, 200], [250, 250], [300, 300]]) == 1
    assert candidate(peaks = [[1, 5], [3, 5], [5, 5], [7, 5], [9, 5], [11, 5], [13, 5], [15, 5], [17, 5], [19, 5]]) == 10
    assert candidate(peaks = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]]) == 5
    assert candidate(peaks = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 0
    assert candidate(peaks = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91], [11, 90], [12, 89], [13, 88], [14, 87], [15, 86], [16, 85], [17, 84], [18, 83], [19, 82], [20, 81]]) == 1
    assert candidate(peaks = [[1, 3], [3, 1], [5, 3], [7, 1], [9, 3], [11, 1], [13, 3], [15, 1], [17, 3], [19, 1], [21, 3], [23, 1], [25, 3], [27, 1], [29, 3]]) == 8
    assert candidate(peaks = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19], [11, 20], [12, 21], [13, 22], [14, 23], [15, 24]]) == 1
    assert candidate(peaks = [[5, 5], [15, 5], [25, 5], [35, 5], [45, 5], [55, 5], [65, 5], [75, 5], [85, 5]]) == 9
    assert candidate(peaks = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 10
    assert candidate(peaks = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]]) == 0
    assert candidate(peaks = [[1, 10], [5, 5], [9, 9], [13, 13], [17, 17], [21, 21], [25, 25], [29, 29]]) == 2
    assert candidate(peaks = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]]) == 1
    assert candidate(peaks = [[1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3], [7, 1], [8, 3], [9, 1], [10, 3]]) == 5
    assert candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 10]]) == 1
    assert candidate(peaks = [[50000, 50000], [60000, 50000], [70000, 50000], [80000, 50000]]) == 4
    assert candidate(peaks = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 1
    assert candidate(peaks = [[1, 1], [10, 10], [2, 2], [9, 9], [3, 3], [8, 8], [4, 4], [7, 7], [5, 5], [6, 6]]) == 1
    assert candidate(peaks = [[5, 1], [15, 1], [25, 1], [35, 1], [45, 1], [55, 1], [65, 1], [75, 1], [85, 1]]) == 9
    assert candidate(peaks = [[10, 20], [15, 15], [20, 10], [25, 5], [30, 10], [35, 15], [40, 20], [45, 15], [50, 10], [55, 5], [60, 10], [65, 15], [70, 20]]) == 3
    assert candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 2], [12, 3], [13, 4], [14, 5], [15, 6], [16, 7], [17, 8], [18, 9], [19, 10]]) == 2
    assert candidate(peaks = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5]]) == 0
    assert candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 10
    assert candidate(peaks = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6]]) == 1
    assert candidate(peaks = [[5, 5], [15, 5], [10, 10], [20, 5], [12, 8]]) == 2
    assert candidate(peaks = [[10, 100], [20, 50], [30, 100], [40, 50], [50, 100], [60, 50], [70, 100]]) == 4
    assert candidate(peaks = [[1, 1], [3, 10], [5, 1], [7, 5], [9, 1], [11, 6], [13, 1]]) == 2
    assert candidate(peaks = [[5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10]]) == 0
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
    assert candidate(peaks = [[1, 100], [100, 100], [100, 1], [1, 1], [50, 50], [75, 25], [25, 75]]) == 2
    assert candidate(peaks = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 10], [12, 9], [13, 8], [14, 7], [15, 6], [16, 5], [17, 4], [18, 3], [19, 2], [20, 1]]) == 2
    assert candidate(peaks = [[10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5]]) == 3
    assert candidate(peaks = [[1, 10], [10, 1], [2, 8], [9, 2], [5, 5]]) == 1
    assert candidate(peaks = [[10, 50], [20, 20], [30, 50], [40, 20], [50, 50], [60, 20], [70, 50], [80, 20], [90, 50]]) == 5
    assert candidate(peaks = [[10, 15], [20, 25], [30, 15], [40, 25], [50, 15], [60, 25], [70, 15], [80, 25], [90, 15]]) == 4
    assert candidate(peaks = [[10, 10], [20, 30], [30, 50], [40, 30], [50, 10], [60, 30], [70, 50]]) == 2
    assert candidate(peaks = [[5, 20], [15, 10], [25, 20], [35, 10], [45, 20], [55, 10], [65, 20], [75, 10], [85, 20]]) == 5
    assert candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5]]) == 3
    assert candidate(peaks = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 1
    assert candidate(peaks = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17]]) == 1
    assert candidate(peaks = [[10, 5], [15, 10], [20, 15], [25, 20], [30, 25], [35, 30]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 1
    assert candidate(peaks = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7]]) == 7
    assert candidate(peaks = [[10, 100], [20, 100], [30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100]]) == 9
    assert candidate(peaks = [[5, 1], [10, 2], [15, 3], [20, 4], [25, 5], [30, 6], [35, 7], [40, 8], [45, 9], [50, 10]]) == 10
    assert candidate(peaks = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10], [60, 10], [70, 10], [80, 10], [90, 10], [100, 10]]) == 10
    assert candidate(peaks = [[10, 10], [11, 9], [12, 8], [13, 7], [14, 6], [15, 5], [16, 4], [17, 3], [18, 2], [19, 1]]) == 1
    assert candidate(peaks = [[5, 25], [10, 20], [15, 25], [20, 20], [25, 25], [30, 20], [35, 25], [40, 20], [45, 25], [50, 20]]) == 5
    assert candidate(peaks = [[1, 1], [10, 10], [1, 2], [10, 9], [1, 3], [10, 8], [1, 4], [10, 7], [1, 5], [10, 6]]) == 2
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 9
    assert candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992]]) == 1
    assert candidate(peaks = [[10, 10], [15, 10], [20, 10], [12, 15], [17, 15], [22, 15], [14, 20], [19, 20], [24, 20]]) == 3
    assert candidate(peaks = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 1
    assert candidate(peaks = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 10
    assert candidate(peaks = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10]]) == 5
    assert candidate(peaks = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 9
    assert candidate(peaks = [[5, 10], [15, 10], [25, 10], [35, 10], [45, 10], [55, 10], [65, 10]]) == 7
    assert candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 10], [10, 1]]) == 2
    assert candidate(peaks = [[10, 10], [20, 15], [25, 5], [30, 20], [40, 10], [50, 25]]) == 4
    assert candidate(peaks = [[1, 1], [5, 5], [9, 9], [13, 13], [17, 17], [21, 21], [25, 25], [29, 29]]) == 1
    assert candidate(peaks = [[1, 100000], [100000, 1], [1, 1], [100000, 100000]]) == 2
    assert candidate(peaks = [[1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5], [6, 6], [6, 6], [7, 7], [7, 7], [8, 8], [8, 8], [9, 9], [9, 9]]) == 0
    assert candidate(peaks = [[1, 100], [5, 50], [10, 100], [15, 50], [20, 100], [25, 50], [30, 100]]) == 4
    assert candidate(peaks = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6]]) == 6
    assert candidate(peaks = [[1, 5], [2, 6], [3, 5], [4, 6], [5, 5], [6, 6], [7, 5], [8, 6], [9, 5], [10, 6]]) == 5
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(peaks = [[5, 3], [10, 6], [15, 9], [20, 12], [25, 15], [30, 18], [35, 21], [40, 24], [45, 27], [50, 30]]) == 10
    assert candidate(peaks = [[5, 5], [6, 6], [7, 5], [8, 6], [9, 5], [10, 6], [11, 5], [12, 6], [13, 5], [14, 6]]) == 5
    assert candidate(peaks = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 8], [7, 6], [8, 4], [9, 2]]) == 1
    assert candidate(peaks = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
    assert candidate(peaks = [[1, 5], [4, 5], [7, 5], [10, 5], [13, 5], [16, 5], [19, 5]]) == 7
    assert candidate(peaks = [[100, 100], [200, 200], [150, 150], [250, 250], [175, 175], [225, 225], [275, 275], [325, 325]]) == 1
    assert candidate(peaks = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
    assert candidate(peaks = [[10, 10], [10, 10], [20, 20], [20, 20], [30, 30], [30, 30]]) == 0
    assert candidate(peaks = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]) == 0
    assert candidate(peaks = [[1, 50], [10, 50], [20, 50], [30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50]]) == 10


