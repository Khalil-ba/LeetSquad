def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [50, 60], [60, 90]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [50, 60], [60, 90]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [10, 20], [20, 30]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [10, 20], [20, 30]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 9], [3, 7], [4, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 9], [3, 7], [4, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [11, 15], [16, 20], [21, 25], [1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [11, 15], [16, 20], [21, 25], [1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 15], [10, 20], [25, 30], [5, 10], [15, 25], [20, 25]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 15], [10, 20], [25, 30], [5, 10], [15, 25], [20, 25]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 5], [3, 8], [4, 9], [5, 10], [6, 11]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 5], [3, 8], [4, 9], [5, 10], [6, 11]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [10, 20], [20, 30], [5, 15], [15, 25]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [10, 20], [20, 30], [5, 15], [15, 25]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000], [3500, 4500]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000], [3500, 4500]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41], [11, 40], [12, 39], [13, 38], [14, 37], [15, 36], [16, 35], [17, 34], [18, 33], [19, 32], [20, 31], [21, 30], [22, 29], [23, 28], [24, 27], [25, 26]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41], [11, 40], [12, 39], [13, 38], [14, 37], [15, 36], [16, 35], [17, 34], [18, 33], [19, 32], [20, 31], [21, 30], [22, 29], [23, 28], [24, 27], [25, 26]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100], [1, 50], [51, 100]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100], [1, 50], [51, 100]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 500000], [500001, 1000000], [2, 499999], [500002, 999998], [3, 499998], [500003, 999997]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 500000], [500001, 1000000], [2, 499999], [500002, 999998], [3, 499998], [500003, 999997]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 500000], [500001, 1000000], [1, 500000], [500001, 1000000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 500000], [500001, 1000000], [1, 500000], [500001, 1000000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [15, 20], [25, 30], [10, 15], [20, 25], [30, 35], [15, 20], [25, 30], [35, 40], [20, 25]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [15, 20], [25, 30], [10, 15], [20, 25], [30, 35], [15, 20], [25, 30], [35, 40], [20, 25]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 6], [3, 9], [4, 12], [5, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 6], [3, 9], [4, 12], [5, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30], [1, 10], [6, 15], [11, 20], [16, 25]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30], [1, 10], [6, 15], [11, 20], [16, 25]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000000], [2, 999999], [3, 999998], [4, 999997]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000000], [2, 999999], [3, 999998], [4, 999997]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [15, 20], [25, 30], [5, 20], [10, 25], [15, 30], [5, 30]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [15, 20], [25, 30], [5, 20], [10, 25], [15, 30], [5, 30]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100000], [100000, 200000], [200000, 300000], [300000, 400000], [400000, 500000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100000], [100000, 200000], [200000, 300000], [300000, 400000], [400000, 500000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350], [300, 400]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350], [300, 400]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 5], [5, 9], [9, 13]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 5], [5, 9], [9, 13]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 5], [4, 7], [6, 9], [8, 11], [10, 13], [12, 15]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 5], [4, 7], [6, 9], [8, 11], [10, 13], [12, 15]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000000], [1000000, 2000000], [1, 1000000], [1000000, 2000000], [1, 1000000], [1000000, 2000000]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000000], [1000000, 2000000], [1, 1000000], [1000000, 2000000], [1, 1000000], [1000000, 2000000]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [1, 20], [1, 30], [1, 40], [1, 50], [1, 60], [1, 70], [1, 80], [1, 90], [1, 100]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [1, 20], [1, 30], [1, 40], [1, 50], [1, 60], [1, 70], [1, 80], [1, 90], [1, 100]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000000], [1, 1000000], [1, 1000000]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000000], [1, 1000000], [1, 1000000]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 3], [1, 3], [2, 4], [2, 4], [2, 4], [3, 5], [3, 5], [3, 5], [4, 6], [4, 6], [4, 6], [5, 7], [5, 7], [5, 7]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 3], [1, 3], [2, 4], [2, 4], [2, 4], [3, 5], [3, 5], [3, 5], [4, 6], [4, 6], [4, 6], [5, 7], [5, 7], [5, 7]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000000], [2, 999999], [3, 999998], [4, 999997], [5, 999996]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000000], [2, 999999], [3, 999998], [4, 999997], [5, 999996]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1000], [500, 1500], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1000], [500, 1500], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [3, 5], [6, 9], [12, 14]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [3, 5], [6, 9], [12, 14]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [1, 10], [11, 20], [21, 30], [31, 40], [1, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [1, 10], [11, 20], [21, 30], [31, 40], [1, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[10, 20], [20, 30], [30, 40], [10, 20], [20, 30], [30, 40], [10, 30], [20, 40], [30, 50]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[10, 20], [20, 30], [30, 40], [10, 20], [20, 30], [30, 40], [10, 30], [20, 40], [30, 50]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [1, 10], [1, 10], [10, 20], [10, 20], [10, 20]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [1, 10], [1, 10], [10, 20], [10, 20], [10, 20]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [50, 150], [100, 200], [200, 300]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [50, 150], [100, 200], [200, 300]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[5, 10], [15, 20], [25, 30], [35, 40], [10, 15], [20, 25], [30, 35]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[5, 10], [15, 20], [25, 30], [35, 40], [10, 15], [20, 25], [30, 35]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [1, 50]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [1, 50]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 20], [5, 15], [10, 25], [15, 30], [20, 35]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 20], [5, 15], [10, 25], [15, 30], [20, 35]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 3], [4, 7], [8, 10], [2, 5], [6, 9], [11, 13], [1, 4], [5, 8], [9, 12]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 3], [4, 7], [8, 10], [2, 5], [6, 9], [11, 13], [1, 4], [5, 8], [9, 12]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 10], [2, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 10], [2, 9]]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 1
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert candidate(intervals = [[1, 1000000]]) == 1
    assert candidate(intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
    assert candidate(intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]) == 1
    assert candidate(intervals = [[1, 100], [50, 60], [60, 90]]) == 3
    assert candidate(intervals = [[1, 10], [10, 20], [20, 30]]) == 2
    assert candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 1
    assert candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5]]) == 4
    assert candidate(intervals = [[1, 5], [2, 9], [3, 7], [4, 10]]) == 4
    assert candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97]]) == 4
    assert candidate(intervals = [[5, 10], [11, 15], [16, 20], [21, 25], [1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]) == 2
    assert candidate(intervals = [[5, 15], [10, 20], [25, 30], [5, 10], [15, 25], [20, 25]]) == 3
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 3
    assert candidate(intervals = [[1, 10], [2, 5], [3, 8], [4, 9], [5, 10], [6, 11]]) == 5
    assert candidate(intervals = [[1, 10], [10, 20], [20, 30], [5, 15], [15, 25]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 2
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 2
    assert candidate(intervals = [[1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000], [3500, 4500]]) == 3
    assert candidate(intervals = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41], [11, 40], [12, 39], [13, 38], [14, 37], [15, 36], [16, 35], [17, 34], [18, 33], [19, 32], [20, 31], [21, 30], [22, 29], [23, 28], [24, 27], [25, 26]]) == 25
    assert candidate(intervals = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]) == 5
    assert candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 5
    assert candidate(intervals = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]]) == 10
    assert candidate(intervals = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15]]) == 5
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50]]) == 3
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 5
    assert candidate(intervals = [[10, 20], [15, 25], [20, 30], [25, 35], [30, 40], [35, 45], [40, 50], [45, 55], [50, 60], [55, 65]]) == 3
    assert candidate(intervals = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100], [1, 50], [51, 100]]) == 11
    assert candidate(intervals = [[1, 500000], [500001, 1000000], [2, 499999], [500002, 999998], [3, 499998], [500003, 999997]]) == 3
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 5
    assert candidate(intervals = [[1, 500000], [500001, 1000000], [1, 500000], [500001, 1000000]]) == 2
    assert candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 1
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 3
    assert candidate(intervals = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]]) == 10
    assert candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50]]) == 2
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]]) == 5
    assert candidate(intervals = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]) == 10
    assert candidate(intervals = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == 10
    assert candidate(intervals = [[5, 10], [15, 20], [25, 30], [10, 15], [20, 25], [30, 35], [15, 20], [25, 30], [35, 40], [20, 25]]) == 4
    assert candidate(intervals = [[1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20]]) == 3
    assert candidate(intervals = [[1, 3], [2, 6], [3, 9], [4, 12], [5, 15]]) == 4
    assert candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 9
    assert candidate(intervals = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30], [1, 10], [6, 15], [11, 20], [16, 25]]) == 3
    assert candidate(intervals = [[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]]) == 10
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 2
    assert candidate(intervals = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19]]) == 2
    assert candidate(intervals = [[1, 1000000], [2, 999999], [3, 999998], [4, 999997]]) == 4
    assert candidate(intervals = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 5
    assert candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 2
    assert candidate(intervals = [[5, 10], [15, 20], [25, 30], [5, 20], [10, 25], [15, 30], [5, 30]]) == 5
    assert candidate(intervals = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]]) == 10
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 4
    assert candidate(intervals = [[1, 100000], [100000, 200000], [200000, 300000], [300000, 400000], [400000, 500000]]) == 2
    assert candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
    assert candidate(intervals = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 6
    assert candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350], [300, 400]]) == 3
    assert candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 5], [5, 9], [9, 13]]) == 3
    assert candidate(intervals = [[1, 3], [2, 5], [4, 7], [6, 9], [8, 11], [10, 13], [12, 15]]) == 2
    assert candidate(intervals = [[1, 1000000], [1000000, 2000000], [1, 1000000], [1000000, 2000000], [1, 1000000], [1000000, 2000000]]) == 6
    assert candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 3
    assert candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 9
    assert candidate(intervals = [[1, 10], [1, 20], [1, 30], [1, 40], [1, 50], [1, 60], [1, 70], [1, 80], [1, 90], [1, 100]]) == 10
    assert candidate(intervals = [[1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20], [1, 10], [11, 20]]) == 4
    assert candidate(intervals = [[1, 2], [2, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30]]) == 2
    assert candidate(intervals = [[1, 5], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 3
    assert candidate(intervals = [[1, 1000000], [1, 1000000], [1, 1000000]]) == 3
    assert candidate(intervals = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]]) == 6
    assert candidate(intervals = [[1, 3], [1, 3], [1, 3], [2, 4], [2, 4], [2, 4], [3, 5], [3, 5], [3, 5], [4, 6], [4, 6], [4, 6], [5, 7], [5, 7], [5, 7]]) == 9
    assert candidate(intervals = [[1, 1000000], [2, 999999], [3, 999998], [4, 999997], [5, 999996]]) == 5
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 2
    assert candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50]]) == 2
    assert candidate(intervals = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == 5
    assert candidate(intervals = [[1, 1000], [500, 1500], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500], [3000, 4000]]) == 3
    assert candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 6
    assert candidate(intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [3, 5], [6, 9], [12, 14]]) == 3
    assert candidate(intervals = [[1, 10], [11, 20], [21, 30], [31, 40], [1, 10], [11, 20], [21, 30], [31, 40], [1, 10]]) == 3
    assert candidate(intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 6
    assert candidate(intervals = [[10, 20], [20, 30], [30, 40], [10, 20], [20, 30], [30, 40], [10, 30], [20, 40], [30, 50]]) == 7
    assert candidate(intervals = [[1, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35]]) == 2
    assert candidate(intervals = [[1, 10], [1, 10], [1, 10], [10, 20], [10, 20], [10, 20]]) == 6
    assert candidate(intervals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 6
    assert candidate(intervals = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == 5
    assert candidate(intervals = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]) == 10
    assert candidate(intervals = [[1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15]]) == 6
    assert candidate(intervals = [[1, 100], [50, 150], [100, 200], [200, 300]]) == 3
    assert candidate(intervals = [[5, 10], [15, 20], [25, 30], [35, 40], [10, 15], [20, 25], [30, 35]]) == 2
    assert candidate(intervals = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [1, 50]]) == 3
    assert candidate(intervals = [[1, 100], [50, 150], [100, 200], [150, 250], [200, 300]]) == 3
    assert candidate(intervals = [[1, 20], [5, 15], [10, 25], [15, 30], [20, 35]]) == 4
    assert candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]]) == 1
    assert candidate(intervals = [[1, 3], [4, 7], [8, 10], [2, 5], [6, 9], [11, 13], [1, 4], [5, 8], [9, 12]]) == 3
    assert candidate(intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 2
    assert candidate(intervals = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 10], [2, 9]]) == 3


