def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1000000], [1000000000, 1000000000, 1000000]]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1000000], [1000000000, 1000000000, 1000000]]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 1], [2, 3, 2], [4, 5, 3], [6, 7, 4], [8, 9, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 1], [2, 3, 2], [4, 5, 3], [6, 7, 4], [8, 9, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(events = [[10, 20, 15], [20, 30, 10], [1, 10, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[10, 20, 15], [20, 30, 10], [1, 10, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 4], [1, 10, 5], [5, 10, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 4], [1, 10, 5], [5, 10, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 5], [2, 5, 6], [4, 6, 7], [5, 7, 8]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 5], [2, 5, 6], [4, 6, 7], [5, 7, 8]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 10], [6, 10, 10], [11, 15, 10], [16, 20, 10]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 10], [6, 10, 10], [11, 15, 10], [16, 20, 10]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(events = [[2, 2, 1], [3, 3, 2], [4, 4, 3], [5, 5, 4], [6, 6, 5]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[2, 2, 1], [3, 3, 2], [4, 4, 3], [5, 5, 4], [6, 6, 5]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 10], [2, 3, 5], [4, 5, 7], [6, 7, 9]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 10], [2, 3, 5], [4, 5, 7], [6, 7, 9]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 100], [3, 4, 200], [5, 6, 300], [7, 8, 400], [9, 10, 500], [11, 12, 600]]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 100], [3, 4, 200], [5, 6, 300], [7, 8, 400], [9, 10, 500], [11, 12, 600]]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 1], [1, 4, 2], [2, 5, 3], [2, 4, 4], [3, 6, 5], [3, 5, 6], [4, 7, 7], [4, 6, 8], [5, 8, 9], [5, 7, 10]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 1], [1, 4, 2], [2, 5, 3], [2, 4, 4], [3, 6, 5], [3, 5, 6], [4, 7, 7], [4, 6, 8], [5, 8, 9], [5, 7, 10]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 5], [1, 10, 6], [1, 10, 7], [1, 10, 8], [1, 10, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 5], [1, 10, 6], [1, 10, 7], [1, 10, 8], [1, 10, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 1], [2, 3, 2], [3, 3, 3], [4, 5, 4], [5, 5, 5], [6, 7, 6], [7, 7, 7]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 1], [2, 3, 2], [3, 3, 3], [4, 5, 4], [5, 5, 5], [6, 7, 6], [7, 7, 7]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5], [11, 20, 6], [12, 19, 7], [13, 18, 8], [14, 17, 9], [15, 16, 10]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5], [11, 20, 6], [12, 19, 7], [13, 18, 8], [14, 17, 9], [15, 16, 10]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000, 1], [1000001, 2000000, 2], [2000001, 3000000, 3], [3000001, 4000000, 4], [4000001, 5000000, 5], [5000001, 6000000, 6], [6000001, 7000000, 7], [7000001, 8000000, 8], [8000001, 9000000, 9], [9000001, 10000000, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000, 1], [1000001, 2000000, 2], [2000001, 3000000, 3], [3000001, 4000000, 4], [4000001, 5000000, 5], [5000001, 6000000, 6], [6000001, 7000000, 7], [7000001, 8000000, 8], [8000001, 9000000, 9], [9000001, 10000000, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 5], [6, 10, 10], [11, 15, 15], [16, 20, 20], [21, 25, 25]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 5], [6, 10, 10], [11, 15, 15], [16, 20, 20], [21, 25, 25]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1000000], [2, 1000000000, 2000000], [3, 1000000000, 3000000], [4, 1000000000, 4000000], [5, 1000000000, 5000000]]) == 5000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1000000], [2, 1000000000, 2000000], [3, 1000000000, 3000000], [4, 1000000000, 4000000], [5, 1000000000, 5000000]]) == 5000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 100], [3, 4, 200], [5, 6, 300], [7, 8, 400], [9, 10, 500]]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 100], [3, 4, 200], [5, 6, 300], [7, 8, 400], [9, 10, 500]]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 1], [6, 10, 2], [11, 15, 3], [16, 20, 4], [21, 25, 5], [26, 30, 6]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 1], [6, 10, 2], [11, 15, 3], [16, 20, 4], [21, 25, 5], [26, 30, 6]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1000000], [2, 3, 900000], [3, 4, 800000], [4, 5, 700000], [5, 6, 600000], [6, 7, 500000], [7, 8, 400000], [8, 9, 300000], [9, 10, 200000], [10, 11, 100000]]) == 1800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1000000], [2, 3, 900000], [3, 4, 800000], [4, 5, 700000], [5, 6, 600000], [6, 7, 500000], [7, 8, 400000], [8, 9, 300000], [9, 10, 200000], [10, 11, 100000]]) == 1800000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3], [4, 1000000000, 4], [5, 1000000000, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3], [4, 1000000000, 4], [5, 1000000000, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1], [1000000000, 1000000000, 1000000]]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1], [1000000000, 1000000000, 1000000]]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 100, 1], [101, 200, 2], [201, 300, 3], [301, 400, 4], [401, 500, 5], [501, 600, 6], [601, 700, 7], [701, 800, 8], [801, 900, 9], [901, 1000, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 100, 1], [101, 200, 2], [201, 300, 3], [301, 400, 4], [401, 500, 5], [501, 600, 6], [601, 700, 7], [701, 800, 8], [801, 900, 9], [901, 1000, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 100], [2, 3, 200], [3, 4, 300], [4, 5, 400], [5, 6, 500]]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 100], [2, 3, 200], [3, 4, 300], [4, 5, 400], [5, 6, 500]]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 10], [2, 2, 20], [3, 3, 30], [4, 4, 40], [5, 5, 50], [6, 6, 60], [7, 7, 70], [8, 8, 80], [9, 9, 90], [10, 10, 100], [11, 11, 110], [12, 12, 120], [13, 13, 130], [14, 14, 140], [15, 15, 150]]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 10], [2, 2, 20], [3, 3, 30], [4, 4, 40], [5, 5, 50], [6, 6, 60], [7, 7, 70], [8, 8, 80], [9, 9, 90], [10, 10, 100], [11, 11, 110], [12, 12, 120], [13, 13, 130], [14, 14, 140], [15, 15, 150]]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1000000], [3, 4, 2000000], [5, 6, 3000000], [7, 8, 4000000], [9, 10, 5000000]]) == 9000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1000000], [3, 4, 2000000], [5, 6, 3000000], [7, 8, 4000000], [9, 10, 5000000]]) == 9000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 10], [2, 2, 9], [3, 3, 8], [4, 4, 7], [5, 5, 6], [6, 6, 5], [7, 7, 4], [8, 8, 3], [9, 9, 2], [10, 10, 1], [11, 11, 100], [12, 12, 99], [13, 13, 98], [14, 14, 97], [15, 15, 96]]) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 10], [2, 2, 9], [3, 3, 8], [4, 4, 7], [5, 5, 6], [6, 6, 5], [7, 7, 4], [8, 8, 3], [9, 9, 2], [10, 10, 1], [11, 11, 100], [12, 12, 99], [13, 13, 98], [14, 14, 97], [15, 15, 96]]) == 199: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1000000], [2, 2, 999999], [3, 3, 999998], [4, 4, 999997], [5, 5, 999996]]) == 1999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1000000], [2, 2, 999999], [3, 3, 999998], [4, 4, 999997], [5, 5, 999996]]) == 1999999: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1], [2, 999999999, 1000000], [3, 999999998, 2000000], [4, 999999997, 3000000]]) == 3000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1], [2, 999999999, 1000000], [3, 999999998, 2000000], [4, 999999997, 3000000]]) == 3000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 100], [5, 10, 200], [10, 15, 300], [15, 20, 400], [20, 25, 500], [25, 30, 600], [30, 35, 700], [35, 40, 800], [40, 45, 900], [45, 50, 1000]]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 100], [5, 10, 200], [10, 15, 300], [15, 20, 400], [20, 25, 500], [25, 30, 600], [30, 35, 700], [35, 40, 800], [40, 45, 900], [45, 50, 1000]]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 6, 50], [6, 7, 60], [7, 8, 70], [8, 9, 80], [9, 10, 90], [10, 11, 100], [11, 12, 110], [12, 13, 120], [13, 14, 130], [14, 15, 140], [15, 16, 150]]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 6, 50], [6, 7, 60], [7, 8, 70], [8, 9, 80], [9, 10, 90], [10, 11, 100], [11, 12, 110], [12, 13, 120], [13, 14, 130], [14, 15, 140], [15, 16, 150]]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7], [15, 16, 8], [17, 18, 9], [19, 20, 10], [21, 22, 11], [23, 24, 12], [25, 26, 13], [27, 28, 14], [29, 30, 15]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7], [15, 16, 8], [17, 18, 9], [19, 20, 10], [21, 22, 11], [23, 24, 12], [25, 26, 13], [27, 28, 14], [29, 30, 15]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 10], [3, 4, 20], [5, 6, 30], [7, 8, 40], [9, 10, 50], [11, 12, 60], [13, 14, 70], [15, 16, 80], [17, 18, 90], [19, 20, 100], [21, 22, 110], [23, 24, 120], [25, 26, 130], [27, 28, 140], [29, 30, 150]]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 10], [3, 4, 20], [5, 6, 30], [7, 8, 40], [9, 10, 50], [11, 12, 60], [13, 14, 70], [15, 16, 80], [17, 18, 90], [19, 20, 100], [21, 22, 110], [23, 24, 120], [25, 26, 130], [27, 28, 140], [29, 30, 150]]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1000000], [3, 4, 999999], [5, 6, 999998], [7, 8, 999997], [9, 10, 999996], [11, 12, 999995], [13, 14, 999994], [15, 16, 999993], [17, 18, 999992], [19, 20, 999991]]) == 1999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1000000], [3, 4, 999999], [5, 6, 999998], [7, 8, 999997], [9, 10, 999996], [11, 12, 999995], [13, 14, 999994], [15, 16, 999993], [17, 18, 999992], [19, 20, 999991]]) == 1999999: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 1000000], [1, 5, 900000], [1, 5, 800000], [1, 5, 700000], [1, 5, 600000], [1, 5, 500000], [1, 5, 400000], [1, 5, 300000], [1, 5, 200000], [1, 5, 100000]]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 1000000], [1, 5, 900000], [1, 5, 800000], [1, 5, 700000], [1, 5, 600000], [1, 5, 500000], [1, 5, 400000], [1, 5, 300000], [1, 5, 200000], [1, 5, 100000]]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[10, 20, 100], [20, 30, 200], [30, 40, 300], [40, 50, 400], [50, 60, 500], [60, 70, 600]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[10, 20, 100], [20, 30, 200], [30, 40, 300], [40, 50, 400], [50, 60, 500], [60, 70, 600]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 100], [2, 2, 200], [3, 3, 300], [4, 4, 400], [5, 5, 500], [6, 6, 600], [7, 7, 700], [8, 8, 800], [9, 9, 900], [10, 10, 1000]]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 100], [2, 2, 200], [3, 3, 300], [4, 4, 400], [5, 5, 500], [6, 6, 600], [7, 7, 700], [8, 8, 800], [9, 9, 900], [10, 10, 1000]]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 1], [2, 11, 2], [3, 12, 3], [4, 13, 4], [5, 14, 5], [6, 15, 6], [7, 16, 7], [8, 17, 8], [9, 18, 9], [10, 19, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 1], [2, 11, 2], [3, 12, 3], [4, 13, 4], [5, 14, 5], [6, 15, 6], [7, 16, 7], [8, 17, 8], [9, 18, 9], [10, 19, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 100], [2, 5, 200], [3, 7, 300], [4, 10, 400], [5, 12, 500], [6, 15, 600], [7, 17, 700], [8, 18, 800], [9, 19, 900]]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 100], [2, 5, 200], [3, 7, 300], [4, 10, 400], [5, 12, 500], [6, 15, 600], [7, 17, 700], [8, 18, 800], [9, 19, 900]]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 10], [1, 3, 20], [1, 4, 30], [1, 5, 40], [1, 6, 50], [1, 7, 60], [1, 8, 70], [1, 9, 80], [1, 10, 90]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 10], [1, 3, 20], [1, 4, 30], [1, 5, 40], [1, 6, 50], [1, 7, 60], [1, 8, 70], [1, 9, 80], [1, 10, 90]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 3], [1, 5, 1], [6, 6, 5], [7, 8, 4]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 3], [1, 5, 1], [6, 6, 5], [7, 8, 4]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1], [2, 10, 2], [3, 9, 3], [4, 8, 4], [5, 7, 5], [6, 6, 6], [7, 5, 7], [8, 4, 8], [9, 3, 9], [10, 2, 10], [11, 1, 11]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1], [2, 10, 2], [3, 9, 3], [4, 8, 4], [5, 7, 5], [6, 6, 6], [7, 5, 7], [8, 4, 8], [9, 3, 9], [10, 2, 10], [11, 1, 11]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 1], [2, 6, 2], [3, 7, 3], [4, 8, 4], [5, 9, 5], [6, 10, 6], [7, 11, 7], [8, 12, 8], [9, 13, 9], [10, 14, 10]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 1], [2, 6, 2], [3, 7, 3], [4, 8, 4], [5, 9, 5], [6, 10, 6], [7, 11, 7], [8, 12, 8], [9, 13, 9], [10, 14, 10]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 1], [2, 20, 2], [3, 30, 3], [4, 40, 4], [5, 50, 5], [6, 60, 6], [7, 70, 7], [8, 80, 8], [9, 90, 9], [10, 100, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 1], [2, 20, 2], [3, 30, 3], [4, 40, 4], [5, 50, 5], [6, 60, 6], [7, 70, 7], [8, 80, 8], [9, 90, 9], [10, 100, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1000000], [2, 999999999, 2000000], [3, 999999998, 3000000], [4, 999999997, 4000000]]) == 4000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1000000], [2, 999999999, 2000000], [3, 999999998, 3000000], [4, 999999997, 4000000]]) == 4000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 100], [11, 20, 200], [21, 30, 300], [31, 40, 400], [41, 50, 500], [51, 60, 600], [61, 70, 700], [71, 80, 800], [81, 90, 900], [91, 100, 1000], [1, 50, 500000], [51, 100, 500000]]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 100], [11, 20, 200], [21, 30, 300], [31, 40, 400], [41, 50, 500], [51, 60, 600], [61, 70, 700], [71, 80, 800], [81, 90, 900], [91, 100, 1000], [1, 50, 500000], [51, 100, 500000]]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 5], [3, 5, 5], [5, 7, 5], [7, 9, 5], [9, 11, 5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 5], [3, 5, 5], [5, 7, 5], [7, 9, 5], [9, 11, 5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 100, 1], [2, 99, 2], [3, 98, 3], [4, 97, 4], [5, 96, 5], [6, 95, 6], [7, 94, 7], [8, 93, 8], [9, 92, 9], [10, 91, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 100, 1], [2, 99, 2], [3, 98, 3], [4, 97, 4], [5, 96, 5], [6, 95, 6], [7, 94, 7], [8, 93, 8], [9, 92, 9], [10, 91, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50], [6, 10, 60], [7, 11, 70], [8, 12, 80], [9, 13, 90], [10, 14, 100]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50], [6, 10, 60], [7, 11, 70], [8, 12, 80], [9, 13, 90], [10, 14, 100]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 6, 50]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 6, 50]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 10], [2, 5, 20], [3, 5, 30], [4, 5, 40], [5, 5, 50], [6, 10, 60], [7, 10, 70], [8, 10, 80], [9, 10, 90], [10, 10, 100]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 10], [2, 5, 20], [3, 5, 30], [4, 5, 40], [5, 5, 50], [6, 10, 60], [7, 10, 70], [8, 10, 80], [9, 10, 90], [10, 10, 100]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1000000], [1000000000, 1000000000, 1], [500000000, 500000000, 2], [600000000, 600000000, 3], [700000000, 700000000, 4], [800000000, 800000000, 5]]) == 1000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1000000], [1000000000, 1000000000, 1], [500000000, 500000000, 2], [600000000, 600000000, 3], [700000000, 700000000, 4], [800000000, 800000000, 5]]) == 1000005: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 5], [10, 20, 10], [20, 30, 15], [30, 40, 20], [40, 50, 25], [50, 60, 30], [60, 70, 35], [70, 80, 40], [80, 90, 45], [90, 100, 50]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 5], [10, 20, 10], [20, 30, 15], [30, 40, 20], [40, 50, 25], [50, 60, 30], [60, 70, 35], [70, 80, 40], [80, 90, 45], [90, 100, 50]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1000000], [2, 2, 999999], [3, 3, 999998], [4, 4, 999997], [5, 5, 999996], [6, 6, 999995], [7, 7, 999994], [8, 8, 999993], [9, 9, 999992], [10, 10, 999991]]) == 1999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1000000], [2, 2, 999999], [3, 3, 999998], [4, 4, 999997], [5, 5, 999996], [6, 6, 999995], [7, 7, 999994], [8, 8, 999993], [9, 9, 999992], [10, 10, 999991]]) == 1999999: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12], [13, 14, 13], [14, 15, 14], [15, 16, 15]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12], [13, 14, 13], [14, 15, 14], [15, 16, 15]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 3], [2, 4, 5], [6, 8, 7], [9, 11, 10], [12, 15, 12], [16, 20, 15]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 3], [2, 4, 5], [6, 8, 7], [9, 11, 10], [12, 15, 12], [16, 20, 15]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 10], [2, 3, 20], [4, 5, 30], [6, 7, 40], [8, 9, 50], [11, 12, 60]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 10], [2, 3, 20], [4, 5, 30], [6, 7, 40], [8, 9, 50], [11, 12, 60]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 10], [11, 20, 20], [21, 30, 30], [31, 40, 40], [41, 50, 50], [51, 60, 60], [61, 70, 70], [71, 80, 80], [81, 90, 90], [91, 100, 100]]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 10], [11, 20, 20], [21, 30, 30], [31, 40, 40], [41, 50, 50], [51, 60, 60], [61, 70, 70], [71, 80, 80], [81, 90, 90], [91, 100, 100]]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 1], [4, 6, 2], [7, 9, 3], [10, 12, 4], [13, 15, 5], [16, 18, 6], [19, 21, 7], [22, 24, 8], [25, 27, 9], [28, 30, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 1], [4, 6, 2], [7, 9, 3], [10, 12, 4], [13, 15, 5], [16, 18, 6], [19, 21, 7], [22, 24, 8], [25, 27, 9], [28, 30, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12], [13, 14, 13], [14, 15, 14]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12], [13, 14, 13], [14, 15, 14]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 3], [3, 5, 2], [5, 7, 1], [7, 9, 4], [9, 11, 5], [11, 13, 6]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 3], [3, 5, 2], [5, 7, 1], [7, 9, 4], [9, 11, 5], [11, 13, 6]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 5], [3, 4, 10], [5, 6, 15], [7, 8, 20], [9, 10, 25], [11, 12, 30], [13, 14, 35], [15, 16, 40]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 5], [3, 4, 10], [5, 6, 15], [7, 8, 20], [9, 10, 25], [11, 12, 30], [13, 14, 35], [15, 16, 40]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7], [15, 16, 8], [17, 18, 9], [19, 20, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7], [15, 16, 8], [17, 18, 9], [19, 20, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 10], [2, 999999999, 20], [3, 999999998, 30], [4, 999999997, 40], [5, 999999996, 50], [6, 999999995, 60], [7, 999999994, 70], [8, 999999993, 80], [9, 999999992, 90], [10, 999999991, 100]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 10], [2, 999999999, 20], [3, 999999998, 30], [4, 999999997, 40], [5, 999999996, 50], [6, 999999995, 60], [7, 999999994, 70], [8, 999999993, 80], [9, 999999992, 90], [10, 999999991, 100]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1000000], [2, 2, 1000000], [3, 3, 1000000], [4, 4, 1000000], [5, 5, 1000000], [6, 6, 1000000], [7, 7, 1000000], [8, 8, 1000000], [9, 9, 1000000], [10, 10, 1000000]]) == 2000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1000000], [2, 2, 1000000], [3, 3, 1000000], [4, 4, 1000000], [5, 5, 1000000], [6, 6, 1000000], [7, 7, 1000000], [8, 8, 1000000], [9, 9, 1000000], [10, 10, 1000000]]) == 2000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 1], [10, 20, 2], [20, 30, 3], [30, 40, 4], [40, 50, 5], [50, 60, 6], [60, 70, 7], [70, 80, 8], [80, 90, 9], [90, 100, 10], [1, 100, 11], [2, 99, 12], [3, 98, 13], [4, 97, 14], [5, 96, 15]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 1], [10, 20, 2], [20, 30, 3], [30, 40, 4], [40, 50, 5], [50, 60, 6], [60, 70, 7], [70, 80, 8], [80, 90, 9], [90, 100, 10], [1, 100, 11], [2, 99, 12], [3, 98, 13], [4, 97, 14], [5, 96, 15]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 2], [2, 4, 3], [3, 5, 4], [4, 6, 5], [5, 7, 6], [6, 8, 7], [7, 9, 8], [8, 10, 9], [9, 11, 10]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 2], [2, 4, 3], [3, 5, 4], [4, 6, 5], [5, 7, 6], [6, 8, 7], [7, 9, 8], [8, 10, 9], [9, 11, 10]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3], [4, 1000000000, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3], [4, 1000000000, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 10], [2, 5, 8], [4, 6, 6], [7, 8, 5], [8, 10, 7], [9, 12, 4]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 10], [2, 5, 8], [4, 6, 6], [7, 8, 5], [8, 10, 7], [9, 12, 4]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1000000], [1000000001, 2000000000, 2000000], [2000000001, 3000000000, 3000000], [3000000001, 4000000000, 4000000], [4000000001, 5000000000, 5000000]]) == 9000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1000000], [1000000001, 2000000000, 2000000], [2000000001, 3000000000, 3000000], [3000000001, 4000000000, 4000000], [4000000001, 5000000000, 5000000]]) == 9000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1], [1000000001, 2000000000, 2], [2000000001, 3000000000, 3], [3000000001, 4000000000, 4], [4000000001, 5000000000, 5], [5000000001, 6000000000, 6], [6000000001, 7000000000, 7], [7000000001, 8000000000, 8], [8000000001, 9000000000, 9], [9000000001, 10000000000, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1], [1000000001, 2000000000, 2], [2000000001, 3000000000, 3], [3000000001, 4000000000, 4], [4000000001, 5000000000, 5], [5000000001, 6000000000, 6], [6000000001, 7000000000, 7], [7000000001, 8000000000, 8], [8000000001, 9000000000, 9], [9000000001, 10000000000, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 50], [3, 4, 60], [5, 6, 70], [7, 8, 80], [9, 10, 90], [11, 12, 100], [13, 14, 110], [15, 16, 120], [17, 18, 130], [19, 20, 140], [21, 22, 150], [23, 24, 160], [25, 26, 170], [27, 28, 180], [29, 30, 190]]) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 50], [3, 4, 60], [5, 6, 70], [7, 8, 80], [9, 10, 90], [11, 12, 100], [13, 14, 110], [15, 16, 120], [17, 18, 130], [19, 20, 140], [21, 22, 150], [23, 24, 160], [25, 26, 170], [27, 28, 180], [29, 30, 190]]) == 370: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 10], [2, 4, 20], [3, 5, 30], [4, 6, 40], [5, 7, 50], [6, 8, 60], [7, 9, 70], [8, 10, 80]]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 10], [2, 4, 20], [3, 5, 30], [4, 6, 40], [5, 7, 50], [6, 8, 60], [7, 9, 70], [8, 10, 80]]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 100], [3, 5, 200], [6, 8, 300], [9, 10, 400], [11, 12, 500]]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 100], [3, 5, 200], [6, 8, 300], [9, 10, 400], [11, 12, 500]]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 5], [2, 6, 10], [3, 7, 15], [4, 8, 20], [5, 9, 25], [6, 10, 30], [7, 11, 35], [8, 12, 40], [9, 13, 45], [10, 14, 50]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 5], [2, 6, 10], [3, 7, 15], [4, 8, 20], [5, 9, 25], [6, 10, 30], [7, 11, 35], [8, 12, 40], [9, 13, 45], [10, 14, 50]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 3, 5], [1, 3, 6], [1, 3, 7], [1, 3, 8], [1, 3, 9], [1, 3, 10], [1, 3, 11], [1, 3, 12], [1, 3, 13], [1, 3, 14], [1, 3, 15], [1, 3, 16]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 3, 5], [1, 3, 6], [1, 3, 7], [1, 3, 8], [1, 3, 9], [1, 3, 10], [1, 3, 11], [1, 3, 12], [1, 3, 13], [1, 3, 14], [1, 3, 15], [1, 3, 16]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1000000], [2, 999999999, 999999], [3, 999999998, 999998]]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1000000], [2, 999999999, 999999], [3, 999999998, 999998]]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50], [6, 10, 60], [7, 11, 70], [8, 12, 80], [9, 13, 90], [10, 14, 100], [11, 15, 110], [12, 16, 120], [13, 17, 130], [14, 18, 140], [15, 19, 150]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50], [6, 10, 60], [7, 11, 70], [8, 12, 80], [9, 13, 90], [10, 14, 100], [11, 15, 110], [12, 16, 120], [13, 17, 130], [14, 18, 140], [15, 19, 150]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 10, 100], [11, 20, 200], [21, 30, 300], [31, 40, 400], [41, 50, 500], [51, 60, 600], [61, 70, 700], [71, 80, 800], [81, 90, 900], [91, 100, 1000]]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 10, 100], [11, 20, 200], [21, 30, 300], [31, 40, 400], [41, 50, 500], [51, 60, 600], [61, 70, 700], [71, 80, 800], [81, 90, 900], [91, 100, 1000]]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 1000000000, 1000000], [2, 3, 500000], [4, 5, 600000], [6, 7, 400000], [8, 9, 700000], [10, 1000000000, 800000]]) == 1500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 1000000000, 1000000], [2, 3, 500000], [4, 5, 600000], [6, 7, 400000], [8, 9, 700000], [10, 1000000000, 800000]]) == 1500000: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9]]) == 16: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(events = [[1, 1000000000, 1000000], [1000000000, 1000000000, 1000000]]) == 1000000
    assert candidate(events = [[1, 10, 1], [2, 3, 2], [4, 5, 3], [6, 7, 4], [8, 9, 5]]) == 9
    assert candidate(events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]) == 19
    assert candidate(events = [[10, 20, 15], [20, 30, 10], [1, 10, 5]]) == 15
    assert candidate(events = [[1, 10, 4], [1, 10, 5], [5, 10, 3]]) == 5
    assert candidate(events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4
    assert candidate(events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]) == 5
    assert candidate(events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]) == 7
    assert candidate(events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]) == 8
    assert candidate(events = [[1, 3, 5], [2, 5, 6], [4, 6, 7], [5, 7, 8]]) == 13
    assert candidate(events = [[1, 5, 10], [6, 10, 10], [11, 15, 10], [16, 20, 10]]) == 20
    assert candidate(events = [[2, 2, 1], [3, 3, 2], [4, 4, 3], [5, 5, 4], [6, 6, 5]]) == 9
    assert candidate(events = [[1, 10, 10], [2, 3, 5], [4, 5, 7], [6, 7, 9]]) == 16
    assert candidate(events = [[1, 2, 100], [3, 4, 200], [5, 6, 300], [7, 8, 400], [9, 10, 500], [11, 12, 600]]) == 1100
    assert candidate(events = [[1, 5, 1], [1, 4, 2], [2, 5, 3], [2, 4, 4], [3, 6, 5], [3, 5, 6], [4, 7, 7], [4, 6, 8], [5, 8, 9], [5, 7, 10]]) == 14
    assert candidate(events = [[1, 10, 5], [1, 10, 6], [1, 10, 7], [1, 10, 8], [1, 10, 9]]) == 9
    assert candidate(events = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15]]) == 15
    assert candidate(events = [[1, 3, 1], [2, 3, 2], [3, 3, 3], [4, 5, 4], [5, 5, 5], [6, 7, 6], [7, 7, 7]]) == 12
    assert candidate(events = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5], [11, 20, 6], [12, 19, 7], [13, 18, 8], [14, 17, 9], [15, 16, 10]]) == 15
    assert candidate(events = [[1, 1000000, 1], [1000001, 2000000, 2], [2000001, 3000000, 3], [3000001, 4000000, 4], [4000001, 5000000, 5], [5000001, 6000000, 6], [6000001, 7000000, 7], [7000001, 8000000, 8], [8000001, 9000000, 9], [9000001, 10000000, 10]]) == 19
    assert candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7]]) == 13
    assert candidate(events = [[1, 5, 5], [6, 10, 10], [11, 15, 15], [16, 20, 20], [21, 25, 25]]) == 45
    assert candidate(events = [[1, 1000000000, 1000000], [2, 1000000000, 2000000], [3, 1000000000, 3000000], [4, 1000000000, 4000000], [5, 1000000000, 5000000]]) == 5000000
    assert candidate(events = [[1, 2, 100], [3, 4, 200], [5, 6, 300], [7, 8, 400], [9, 10, 500]]) == 900
    assert candidate(events = [[1, 5, 1], [6, 10, 2], [11, 15, 3], [16, 20, 4], [21, 25, 5], [26, 30, 6]]) == 11
    assert candidate(events = [[1, 2, 1000000], [2, 3, 900000], [3, 4, 800000], [4, 5, 700000], [5, 6, 600000], [6, 7, 500000], [7, 8, 400000], [8, 9, 300000], [9, 10, 200000], [10, 11, 100000]]) == 1800000
    assert candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3], [4, 1000000000, 4], [5, 1000000000, 5]]) == 5
    assert candidate(events = [[1, 1000000000, 1], [1000000000, 1000000000, 1000000]]) == 1000000
    assert candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50]]) == 50
    assert candidate(events = [[1, 100, 1], [101, 200, 2], [201, 300, 3], [301, 400, 4], [401, 500, 5], [501, 600, 6], [601, 700, 7], [701, 800, 8], [801, 900, 9], [901, 1000, 10]]) == 19
    assert candidate(events = [[1, 2, 100], [2, 3, 200], [3, 4, 300], [4, 5, 400], [5, 6, 500]]) == 800
    assert candidate(events = [[1, 1, 10], [2, 2, 20], [3, 3, 30], [4, 4, 40], [5, 5, 50], [6, 6, 60], [7, 7, 70], [8, 8, 80], [9, 9, 90], [10, 10, 100], [11, 11, 110], [12, 12, 120], [13, 13, 130], [14, 14, 140], [15, 15, 150]]) == 290
    assert candidate(events = [[1, 2, 1000000], [3, 4, 2000000], [5, 6, 3000000], [7, 8, 4000000], [9, 10, 5000000]]) == 9000000
    assert candidate(events = [[1, 1, 10], [2, 2, 9], [3, 3, 8], [4, 4, 7], [5, 5, 6], [6, 6, 5], [7, 7, 4], [8, 8, 3], [9, 9, 2], [10, 10, 1], [11, 11, 100], [12, 12, 99], [13, 13, 98], [14, 14, 97], [15, 15, 96]]) == 199
    assert candidate(events = [[1, 1, 1000000], [2, 2, 999999], [3, 3, 999998], [4, 4, 999997], [5, 5, 999996]]) == 1999999
    assert candidate(events = [[1, 1000000000, 1], [2, 999999999, 1000000], [3, 999999998, 2000000], [4, 999999997, 3000000]]) == 3000000
    assert candidate(events = [[1, 5, 100], [5, 10, 200], [10, 15, 300], [15, 20, 400], [20, 25, 500], [25, 30, 600], [30, 35, 700], [35, 40, 800], [40, 45, 900], [45, 50, 1000]]) == 1800
    assert candidate(events = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 6, 50], [6, 7, 60], [7, 8, 70], [8, 9, 80], [9, 10, 90], [10, 11, 100], [11, 12, 110], [12, 13, 120], [13, 14, 130], [14, 15, 140], [15, 16, 150]]) == 280
    assert candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7], [15, 16, 8], [17, 18, 9], [19, 20, 10], [21, 22, 11], [23, 24, 12], [25, 26, 13], [27, 28, 14], [29, 30, 15]]) == 29
    assert candidate(events = [[1, 2, 10], [3, 4, 20], [5, 6, 30], [7, 8, 40], [9, 10, 50], [11, 12, 60], [13, 14, 70], [15, 16, 80], [17, 18, 90], [19, 20, 100], [21, 22, 110], [23, 24, 120], [25, 26, 130], [27, 28, 140], [29, 30, 150]]) == 290
    assert candidate(events = [[1, 2, 1000000], [3, 4, 999999], [5, 6, 999998], [7, 8, 999997], [9, 10, 999996], [11, 12, 999995], [13, 14, 999994], [15, 16, 999993], [17, 18, 999992], [19, 20, 999991]]) == 1999999
    assert candidate(events = [[1, 5, 1000000], [1, 5, 900000], [1, 5, 800000], [1, 5, 700000], [1, 5, 600000], [1, 5, 500000], [1, 5, 400000], [1, 5, 300000], [1, 5, 200000], [1, 5, 100000]]) == 1000000
    assert candidate(events = [[1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15]]) == 15
    assert candidate(events = [[1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]]) == 10
    assert candidate(events = [[10, 20, 100], [20, 30, 200], [30, 40, 300], [40, 50, 400], [50, 60, 500], [60, 70, 600]]) == 1000
    assert candidate(events = [[1, 1, 100], [2, 2, 200], [3, 3, 300], [4, 4, 400], [5, 5, 500], [6, 6, 600], [7, 7, 700], [8, 8, 800], [9, 9, 900], [10, 10, 1000]]) == 1900
    assert candidate(events = [[1, 10, 1], [2, 11, 2], [3, 12, 3], [4, 13, 4], [5, 14, 5], [6, 15, 6], [7, 16, 7], [8, 17, 8], [9, 18, 9], [10, 19, 10]]) == 10
    assert candidate(events = [[1, 3, 100], [2, 5, 200], [3, 7, 300], [4, 10, 400], [5, 12, 500], [6, 15, 600], [7, 17, 700], [8, 18, 800], [9, 19, 900]]) == 1200
    assert candidate(events = [[1, 2, 10], [1, 3, 20], [1, 4, 30], [1, 5, 40], [1, 6, 50], [1, 7, 60], [1, 8, 70], [1, 9, 80], [1, 10, 90]]) == 90
    assert candidate(events = [[1, 5, 3], [1, 5, 1], [6, 6, 5], [7, 8, 4]]) == 9
    assert candidate(events = [[1, 1, 1], [2, 10, 2], [3, 9, 3], [4, 8, 4], [5, 7, 5], [6, 6, 6], [7, 5, 7], [8, 4, 8], [9, 3, 9], [10, 2, 10], [11, 1, 11]]) == 22
    assert candidate(events = [[1, 5, 1], [2, 6, 2], [3, 7, 3], [4, 8, 4], [5, 9, 5], [6, 10, 6], [7, 11, 7], [8, 12, 8], [9, 13, 9], [10, 14, 10]]) == 15
    assert candidate(events = [[1, 10, 1], [2, 20, 2], [3, 30, 3], [4, 40, 4], [5, 50, 5], [6, 60, 6], [7, 70, 7], [8, 80, 8], [9, 90, 9], [10, 100, 10]]) == 10
    assert candidate(events = [[1, 1000000000, 1000000], [2, 999999999, 2000000], [3, 999999998, 3000000], [4, 999999997, 4000000]]) == 4000000
    assert candidate(events = [[1, 10, 100], [11, 20, 200], [21, 30, 300], [31, 40, 400], [41, 50, 500], [51, 60, 600], [61, 70, 700], [71, 80, 800], [81, 90, 900], [91, 100, 1000], [1, 50, 500000], [51, 100, 500000]]) == 1000000
    assert candidate(events = [[1, 3, 5], [3, 5, 5], [5, 7, 5], [7, 9, 5], [9, 11, 5]]) == 10
    assert candidate(events = [[1, 100, 1], [2, 99, 2], [3, 98, 3], [4, 97, 4], [5, 96, 5], [6, 95, 6], [7, 94, 7], [8, 93, 8], [9, 92, 9], [10, 91, 10]]) == 10
    assert candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50], [6, 10, 60], [7, 11, 70], [8, 12, 80], [9, 13, 90], [10, 14, 100]]) == 150
    assert candidate(events = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1], [9, 10, 1], [10, 11, 1]]) == 2
    assert candidate(events = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 6, 50]]) == 80
    assert candidate(events = [[1, 5, 10], [2, 5, 20], [3, 5, 30], [4, 5, 40], [5, 5, 50], [6, 10, 60], [7, 10, 70], [8, 10, 80], [9, 10, 90], [10, 10, 100]]) == 150
    assert candidate(events = [[1, 1, 1000000], [1000000000, 1000000000, 1], [500000000, 500000000, 2], [600000000, 600000000, 3], [700000000, 700000000, 4], [800000000, 800000000, 5]]) == 1000005
    assert candidate(events = [[1, 10, 5], [10, 20, 10], [20, 30, 15], [30, 40, 20], [40, 50, 25], [50, 60, 30], [60, 70, 35], [70, 80, 40], [80, 90, 45], [90, 100, 50]]) == 90
    assert candidate(events = [[1, 1, 1000000], [2, 2, 999999], [3, 3, 999998], [4, 4, 999997], [5, 5, 999996], [6, 6, 999995], [7, 7, 999994], [8, 8, 999993], [9, 9, 999992], [10, 10, 999991]]) == 1999999
    assert candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12], [13, 14, 13], [14, 15, 14], [15, 16, 15]]) == 28
    assert candidate(events = [[1, 5, 3], [2, 4, 5], [6, 8, 7], [9, 11, 10], [12, 15, 12], [16, 20, 15]]) == 27
    assert candidate(events = [[1, 10, 10], [2, 3, 20], [4, 5, 30], [6, 7, 40], [8, 9, 50], [11, 12, 60]]) == 110
    assert candidate(events = [[1, 10, 10], [11, 20, 20], [21, 30, 30], [31, 40, 40], [41, 50, 50], [51, 60, 60], [61, 70, 70], [71, 80, 80], [81, 90, 90], [91, 100, 100]]) == 190
    assert candidate(events = [[1, 3, 1], [4, 6, 2], [7, 9, 3], [10, 12, 4], [13, 15, 5], [16, 18, 6], [19, 21, 7], [22, 24, 8], [25, 27, 9], [28, 30, 10]]) == 19
    assert candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12], [13, 14, 13], [14, 15, 14]]) == 26
    assert candidate(events = [[1, 3, 3], [3, 5, 2], [5, 7, 1], [7, 9, 4], [9, 11, 5], [11, 13, 6]]) == 10
    assert candidate(events = [[1, 2, 5], [3, 4, 10], [5, 6, 15], [7, 8, 20], [9, 10, 25], [11, 12, 30], [13, 14, 35], [15, 16, 40]]) == 75
    assert candidate(events = [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4], [9, 10, 5], [11, 12, 6], [13, 14, 7], [15, 16, 8], [17, 18, 9], [19, 20, 10]]) == 19
    assert candidate(events = [[1, 1000000000, 10], [2, 999999999, 20], [3, 999999998, 30], [4, 999999997, 40], [5, 999999996, 50], [6, 999999995, 60], [7, 999999994, 70], [8, 999999993, 80], [9, 999999992, 90], [10, 999999991, 100]]) == 100
    assert candidate(events = [[1, 1, 1000000], [2, 2, 1000000], [3, 3, 1000000], [4, 4, 1000000], [5, 5, 1000000], [6, 6, 1000000], [7, 7, 1000000], [8, 8, 1000000], [9, 9, 1000000], [10, 10, 1000000]]) == 2000000
    assert candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3]]) == 3
    assert candidate(events = [[1, 10, 1], [10, 20, 2], [20, 30, 3], [30, 40, 4], [40, 50, 5], [50, 60, 6], [60, 70, 7], [70, 80, 8], [80, 90, 9], [90, 100, 10], [1, 100, 11], [2, 99, 12], [3, 98, 13], [4, 97, 14], [5, 96, 15]]) == 18
    assert candidate(events = [[1, 3, 2], [2, 4, 3], [3, 5, 4], [4, 6, 5], [5, 7, 6], [6, 8, 7], [7, 9, 8], [8, 10, 9], [9, 11, 10]]) == 17
    assert candidate(events = [[1, 1000000000, 1], [2, 1000000000, 2], [3, 1000000000, 3], [4, 1000000000, 4]]) == 4
    assert candidate(events = [[1, 3, 10], [2, 5, 8], [4, 6, 6], [7, 8, 5], [8, 10, 7], [9, 12, 4]]) == 17
    assert candidate(events = [[1, 1000000000, 1000000], [1000000001, 2000000000, 2000000], [2000000001, 3000000000, 3000000], [3000000001, 4000000000, 4000000], [4000000001, 5000000000, 5000000]]) == 9000000
    assert candidate(events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15]]) == 29
    assert candidate(events = [[1, 1000000000, 1], [1000000001, 2000000000, 2], [2000000001, 3000000000, 3], [3000000001, 4000000000, 4], [4000000001, 5000000000, 5], [5000000001, 6000000000, 6], [6000000001, 7000000000, 7], [7000000001, 8000000000, 8], [8000000001, 9000000000, 9], [9000000001, 10000000000, 10]]) == 19
    assert candidate(events = [[1, 2, 50], [3, 4, 60], [5, 6, 70], [7, 8, 80], [9, 10, 90], [11, 12, 100], [13, 14, 110], [15, 16, 120], [17, 18, 130], [19, 20, 140], [21, 22, 150], [23, 24, 160], [25, 26, 170], [27, 28, 180], [29, 30, 190]]) == 370
    assert candidate(events = [[1, 3, 10], [2, 4, 20], [3, 5, 30], [4, 6, 40], [5, 7, 50], [6, 8, 60], [7, 9, 70], [8, 10, 80]]) == 130
    assert candidate(events = [[1, 2, 100], [3, 5, 200], [6, 8, 300], [9, 10, 400], [11, 12, 500]]) == 900
    assert candidate(events = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10]]) == 10
    assert candidate(events = [[1, 5, 5], [2, 6, 10], [3, 7, 15], [4, 8, 20], [5, 9, 25], [6, 10, 30], [7, 11, 35], [8, 12, 40], [9, 13, 45], [10, 14, 50]]) == 75
    assert candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8]]) == 14
    assert candidate(events = [[1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 3, 5], [1, 3, 6], [1, 3, 7], [1, 3, 8], [1, 3, 9], [1, 3, 10], [1, 3, 11], [1, 3, 12], [1, 3, 13], [1, 3, 14], [1, 3, 15], [1, 3, 16]]) == 16
    assert candidate(events = [[1, 1000000000, 1000000], [2, 999999999, 999999], [3, 999999998, 999998]]) == 1000000
    assert candidate(events = [[1, 5, 10], [2, 6, 20], [3, 7, 30], [4, 8, 40], [5, 9, 50], [6, 10, 60], [7, 11, 70], [8, 12, 80], [9, 13, 90], [10, 14, 100], [11, 15, 110], [12, 16, 120], [13, 17, 130], [14, 18, 140], [15, 19, 150]]) == 250
    assert candidate(events = [[1, 10, 100], [11, 20, 200], [21, 30, 300], [31, 40, 400], [41, 50, 500], [51, 60, 600], [61, 70, 700], [71, 80, 800], [81, 90, 900], [91, 100, 1000]]) == 1900
    assert candidate(events = [[1, 1000000000, 1000000], [2, 3, 500000], [4, 5, 600000], [6, 7, 400000], [8, 9, 700000], [10, 1000000000, 800000]]) == 1500000
    assert candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10], [11, 12, 11], [12, 13, 12]]) == 22
    assert candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9], [10, 11, 10]]) == 18
    assert candidate(events = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6], [7, 8, 7], [8, 9, 8], [9, 10, 9]]) == 16


