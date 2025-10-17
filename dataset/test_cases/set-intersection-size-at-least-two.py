def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [5, 10], [7, 15]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [5, 10], [7, 15]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 7], [8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 7], [8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [3, 4], [5, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [3, 4], [5, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 4], [3, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 4], [3, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [50, 75], [25, 50], [75, 100]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [50, 75], [25, 50], [75, 100]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 5], [3, 7], [4, 8], [5, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 5], [3, 7], [4, 8], [5, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 13]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 13]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 6], [6, 9], [9, 12], [12, 15]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 6], [6, 9], [9, 12], [12, 15]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 6], [4, 7], [6, 8], [8, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 6], [4, 7], [6, 8], [8, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000], [500, 750], [250, 500], [750, 1000], [100, 300], [300, 500], [500, 700], [700, 900], [900, 1100]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000], [500, 750], [250, 500], [750, 1000], [100, 300], [300, 500], [500, 700], [700, 900], [900, 1100]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100000000], [50000000, 100000000], [1, 50000000], [50000000, 100000000], [25000000, 75000000], [75000000, 125000000]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100000000], [50000000, 100000000], [1, 50000000], [50000000, 100000000], [25000000, 75000000], [75000000, 125000000]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 4], [2, 4], [3, 4], [4, 4], [1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 4], [2, 4], [3, 4], [4, 4], [1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 7], [8, 9], [10, 12], [11, 13]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 7], [8, 9], [10, 12], [11, 13]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 20], [5, 15], [10, 25], [15, 30], [20, 40]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 20], [5, 15], [10, 25], [15, 30], [20, 40]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [1, 3], [2, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [1, 3], [2, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 50], [10, 30], [20, 40], [30, 50], [40, 60], [50, 70], [60, 80], [70, 90], [80, 100]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 50], [10, 30], [20, 40], [30, 50], [40, 60], [50, 70], [60, 80], [70, 90], [80, 100]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 5], [2, 4], [2, 6], [3, 5], [3, 7], [4, 6], [4, 8], [5, 7], [5, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 5], [2, 4], [2, 6], [3, 5], [3, 7], [4, 6], [4, 8], [5, 7], [5, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 30], [10, 20], [15, 25], [20, 30], [25, 30]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 30], [10, 20], [15, 25], [20, 30], [25, 30]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 20], [2, 19], [3, 18], [4, 17], [5, 16], [6, 15], [7, 14], [8, 13], [9, 12], [10, 11]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 20], [2, 19], [3, 18], [4, 17], [5, 16], [6, 15], [7, 14], [8, 13], [9, 12], [10, 11]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [6, 8], [7, 9], [8, 11], [9, 12]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [6, 8], [7, 9], [8, 11], [9, 12]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 16], [15, 17]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 16], [15, 17]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 7], [7, 11], [11, 15], [15, 19], [19, 23], [23, 27], [27, 31]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 7], [7, 11], [11, 15], [15, 19], [19, 23], [23, 27], [27, 31]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10], [5, 15], [10, 20], [15, 25]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10], [5, 15], [10, 20], [15, 25]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5], [6, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5], [6, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 4], [2, 5], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 4], [2, 5], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [11, 20], [12, 19], [13, 18], [14, 17], [15, 16]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [11, 20], [12, 19], [13, 18], [14, 17], [15, 16]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [5, 15], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [5, 15], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 5], [3, 6], [7, 12], [8, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 5], [3, 6], [7, 12], [8, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100000000], [50000000, 100000000], [1, 50000000], [50000000, 100000000]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100000000], [50000000, 100000000], [1, 50000000], [50000000, 100000000]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 8], [3, 6], [7, 10], [4, 5], [5, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 8], [3, 6], [7, 10], [4, 5], [5, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [11, 20], [21, 30], [1, 20], [11, 30], [1, 30]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [11, 20], [21, 30], [1, 20], [11, 30], [1, 30]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 50], [5, 55], [10, 60], [15, 65], [20, 70], [25, 75], [30, 80], [35, 85], [40, 90], [45, 95]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 50], [5, 55], [10, 60], [15, 65], [20, 70], [25, 75], [30, 80], [35, 85], [40, 90], [45, 95]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [1, 50], [50, 100], [25, 75], [75, 125], [100, 150]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [1, 50], [50, 100], [25, 75], [75, 125], [100, 150]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100], [1, 100]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100], [1, 100]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100000000], [50000000, 75000000], [25000000, 50000000], [75000000, 100000000]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100000000], [50000000, 75000000], [25000000, 50000000], [75000000, 100000000]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41], [11, 40], [12, 39], [13, 38], [14, 37], [15, 36], [16, 35], [17, 34], [18, 33], [19, 32], [20, 31], [21, 30], [22, 29], [23, 28], [24, 27], [25, 26]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41], [11, 40], [12, 39], [13, 38], [14, 37], [15, 36], [16, 35], [17, 34], [18, 33], [19, 32], [20, 31], [21, 30], [22, 29], [23, 28], [24, 27], [25, 26]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [25, 50], [50, 75], [75, 100], [100, 125], [125, 150]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [25, 50], [50, 75], [75, 100], [100, 125], [125, 150]]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(intervals = [[1, 10], [5, 10], [7, 15]]) == 2
    assert candidate(intervals = [[1, 2], [2, 3]]) == 3
    assert candidate(intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]) == 3
    assert candidate(intervals = [[1, 3], [3, 7], [8, 9]]) == 5
    assert candidate(intervals = [[1, 2], [3, 4], [5, 6]]) == 6
    assert candidate(intervals = [[1, 5], [2, 4], [3, 6]]) == 2
    assert candidate(intervals = [[1, 100], [50, 75], [25, 50], [75, 100]]) == 4
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 2
    assert candidate(intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]) == 5
    assert candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]]) == 11
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7
    assert candidate(intervals = [[1, 10], [2, 5], [3, 7], [4, 8], [5, 9]]) == 3
    assert candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 2
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 8
    assert candidate(intervals = [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 13]]) == 6
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 5
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20]]) == 20
    assert candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 2
    assert candidate(intervals = [[1, 3], [3, 6], [6, 9], [9, 12], [12, 15]]) == 6
    assert candidate(intervals = [[1, 3], [2, 6], [4, 7], [6, 8], [8, 10]]) == 6
    assert candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 2
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 6
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13]]) == 4
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]]) == 8
    assert candidate(intervals = [[1, 1000], [500, 750], [250, 500], [750, 1000], [100, 300], [300, 500], [500, 700], [700, 900], [900, 1100]]) == 6
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 5
    assert candidate(intervals = [[1, 100000000], [50000000, 100000000], [1, 50000000], [50000000, 100000000], [25000000, 75000000], [75000000, 125000000]]) == 4
    assert candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 2
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 6
    assert candidate(intervals = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [1, 4], [2, 4], [3, 4], [4, 4], [1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [1, 1]]) == 10
    assert candidate(intervals = [[1, 3], [3, 7], [8, 9], [10, 12], [11, 13]]) == 7
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 14
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 4
    assert candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13]]) == 4
    assert candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 2
    assert candidate(intervals = [[1, 20], [5, 15], [10, 25], [15, 30], [20, 40]]) == 4
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]) == 16
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12]]) == 4
    assert candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11]]) == 6
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [1, 3], [2, 4]]) == 4
    assert candidate(intervals = [[1, 50], [10, 30], [20, 40], [30, 50], [40, 60], [50, 70], [60, 80], [70, 90], [80, 100]]) == 6
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45]]) == 5
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 15
    assert candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]]) == 2
    assert candidate(intervals = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]) == 2
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
    assert candidate(intervals = [[1, 3], [1, 5], [2, 4], [2, 6], [3, 5], [3, 7], [4, 6], [4, 8], [5, 7], [5, 9]]) == 4
    assert candidate(intervals = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15], [16, 18]]) == 12
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45]]) == 5
    assert candidate(intervals = [[1, 30], [10, 20], [15, 25], [20, 30], [25, 30]]) == 4
    assert candidate(intervals = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]]) == 3
    assert candidate(intervals = [[1, 20], [2, 19], [3, 18], [4, 17], [5, 16], [6, 15], [7, 14], [8, 13], [9, 12], [10, 11]]) == 2
    assert candidate(intervals = [[5, 10], [6, 8], [7, 9], [8, 11], [9, 12]]) == 4
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 16], [15, 17]]) == 11
    assert candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 11
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]]) == 12
    assert candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 2
    assert candidate(intervals = [[1, 3], [3, 7], [7, 11], [11, 15], [15, 19], [19, 23], [23, 27], [27, 31]]) == 9
    assert candidate(intervals = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5]]) == 2
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10], [5, 15], [10, 20], [15, 25]]) == 12
    assert candidate(intervals = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994]]) == 2
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 11
    assert candidate(intervals = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
    assert candidate(intervals = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5], [6, 6]]) == 4
    assert candidate(intervals = [[1, 3], [1, 4], [2, 5], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]) == 8
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [11, 20], [12, 19], [13, 18], [14, 17], [15, 16]]) == 4
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 13
    assert candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]]) == 20
    assert candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 2
    assert candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30]]) == 30
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 11
    assert candidate(intervals = [[1, 10], [5, 15], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60]]) == 8
    assert candidate(intervals = [[1, 10], [2, 5], [3, 6], [7, 12], [8, 9]]) == 4
    assert candidate(intervals = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10]]) == 2
    assert candidate(intervals = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 6
    assert candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 7
    assert candidate(intervals = [[1, 100000000], [50000000, 100000000], [1, 50000000], [50000000, 100000000]]) == 3
    assert candidate(intervals = [[1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 2
    assert candidate(intervals = [[1, 10], [2, 8], [3, 6], [7, 10], [4, 5], [5, 9]]) == 4
    assert candidate(intervals = [[1, 10], [11, 20], [21, 30], [1, 20], [11, 30], [1, 30]]) == 6
    assert candidate(intervals = [[5, 15], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 6
    assert candidate(intervals = [[1, 50], [5, 55], [10, 60], [15, 65], [20, 70], [25, 75], [30, 80], [35, 85], [40, 90], [45, 95]]) == 2
    assert candidate(intervals = [[1, 100], [1, 50], [50, 100], [25, 75], [75, 125], [100, 150]]) == 4
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40]]) == 4
    assert candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100], [1, 100]]) == 20
    assert candidate(intervals = [[1, 100000000], [50000000, 75000000], [25000000, 50000000], [75000000, 100000000]]) == 4
    assert candidate(intervals = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41], [11, 40], [12, 39], [13, 38], [14, 37], [15, 36], [16, 35], [17, 34], [18, 33], [19, 32], [20, 31], [21, 30], [22, 29], [23, 28], [24, 27], [25, 26]]) == 2
    assert candidate(intervals = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == 6
    assert candidate(intervals = [[1, 100], [25, 50], [50, 75], [75, 100], [100, 125], [125, 150]]) == 6


