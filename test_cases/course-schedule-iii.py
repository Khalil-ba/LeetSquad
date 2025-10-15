def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [11, 15], [11, 16], [8, 13], [11, 17], [4, 11], [2, 12]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [11, 15], [11, 16], [8, 13], [11, 17], [4, 11], [2, 12]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [300, 3100]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [300, 3100]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 100], [10, 100], [10, 100], [10, 100], [10, 100]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 100], [10, 100], [10, 100], [10, 100], [10, 100]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [3, 6], [7, 8], [2, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [3, 6], [7, 8], [2, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [2, 5], [4, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [2, 5], [4, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 16], [8, 14]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 16], [8, 14]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 15], [20, 30], [10, 25]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 15], [20, 30], [10, 25]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 100], [200, 200], [300, 300]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 100], [200, 200], [300, 300]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[3, 7], [4, 9], [4, 10], [2, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[3, 7], [4, 9], [4, 10], [2, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[3, 2], [4, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[3, 2], [4, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 100], [20, 200], [30, 300], [40, 400]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 100], [20, 200], [30, 300], [40, 400]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 1000], [500, 1500]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 1000], [500, 1500]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[9, 14], [2, 11], [8, 12], [8, 13], [10, 14], [2, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[9, 14], [2, 11], [8, 12], [8, 13], [10, 14], [2, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 10], [4, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 10], [4, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [5, 6], [6, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [5, 6], [6, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 20], [10, 25], [15, 30]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 20], [10, 25], [15, 30]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[4, 7], [2, 10], [3, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[4, 7], [2, 10], [3, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [4, 6], [2, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [4, 6], [2, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 3], [2, 5], [3, 7], [4, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 3], [2, 5], [3, 7], [4, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[2, 5], [2, 7], [2, 10], [3, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[2, 5], [2, 7], [2, 10], [3, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 16], [8, 14], [10, 16], [4, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 16], [8, 14], [10, 16], [4, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 15], [10, 20], [15, 30]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 15], [10, 20], [15, 30]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 2], [2, 5], [4, 6], [7, 8]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 2], [2, 5], [4, 6], [7, 8]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 20], [2, 30], [3, 40], [4, 50]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 20], [2, 30], [3, 40], [4, 50]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 40], [30, 60]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 40], [30, 60]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 100], [2, 101], [3, 102], [4, 103], [5, 104]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 100], [2, 101], [3, 102], [4, 103], [5, 104]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 100], [10, 200], [10, 300], [10, 400], [10, 500], [10, 600], [10, 700], [10, 800], [10, 900], [10, 1000], [10, 1100], [10, 1200]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 100], [10, 200], [10, 300], [10, 400], [10, 500], [10, 600], [10, 700], [10, 800], [10, 900], [10, 1000], [10, 1100], [10, 1200]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [150, 300], [50, 250], [200, 500], [100, 400]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [150, 300], [50, 250], [200, 500], [100, 400]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000], [11, 1100], [12, 1200], [13, 1300], [14, 1400], [15, 1500]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000], [11, 1100], [12, 1200], [13, 1300], [14, 1400], [15, 1500]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20], [1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20], [1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[300, 500], [200, 400], [100, 300], [200, 500], [100, 400], [300, 600]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[300, 500], [200, 400], [100, 300], [200, 500], [100, 400], [300, 600]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 500], [50, 250], [200, 600], [300, 900], [100, 400], [250, 700]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 500], [50, 250], [200, 600], [300, 900], [100, 400], [250, 700]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21], [11, 23], [12, 25], [13, 27], [14, 29], [15, 31]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21], [11, 23], [12, 25], [13, 27], [14, 29], [15, 31]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 300], [200, 700], [100, 500], [200, 800], [100, 600], [200, 900], [100, 700], [200, 1000]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 300], [200, 700], [100, 500], [200, 800], [100, 600], [200, 900], [100, 700], [200, 1000]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10000, 10001], [10000, 10002], [10000, 10003], [10000, 10004], [10000, 10005]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10000, 10001], [10000, 10002], [10000, 10003], [10000, 10004], [10000, 10005]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 250], [100, 300], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [100, 600]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 250], [100, 300], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [100, 600]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 300], [200, 500], [100, 400], [200, 600], [300, 800], [100, 500], [200, 700]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 300], [200, 500], [100, 400], [200, 600], [300, 800], [100, 500], [200, 700]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 400], [300, 600], [400, 800], [500, 1000], [600, 1200], [700, 1400], [800, 1600], [900, 1800]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 400], [300, 600], [400, 800], [500, 1000], [600, 1200], [700, 1400], [800, 1600], [900, 1800]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [3, 6], [2, 10], [10, 12], [4, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [3, 6], [2, 10], [10, 12], [4, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [1000, 2000], [500, 1500], [1000, 2500], [500, 2000], [1000, 3000], [500, 2500], [1000, 3500], [500, 3000], [1000, 4000]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [1000, 2000], [500, 1500], [1000, 2500], [500, 2000], [1000, 3000], [500, 2500], [1000, 3500], [500, 3000], [1000, 4000]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [50, 150], [30, 100], [200, 300], [10, 50]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [50, 150], [30, 100], [200, 300], [10, 50]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 300], [200, 400], [300, 500], [400, 600], [500, 700], [600, 800], [700, 900], [800, 1000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 300], [200, 400], [300, 500], [400, 600], [500, 700], [600, 800], [700, 900], [800, 1000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 10], [3, 8], [4, 9], [2, 6], [7, 12], [1, 5], [6, 11], [8, 13], [9, 14], [10, 15]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 10], [3, 8], [4, 9], [2, 6], [7, 12], [1, 5], [6, 11], [8, 13], [9, 14], [10, 15]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [9, 19], [8, 18], [7, 17], [6, 16], [5, 15], [4, 14], [3, 13], [2, 12], [1, 11], [11, 21], [12, 22], [13, 23], [14, 24], [15, 25]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [9, 19], [8, 18], [7, 17], [6, 16], [5, 15], [4, 14], [3, 13], [2, 12], [1, 11], [11, 21], [12, 22], [13, 23], [14, 24], [15, 25]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 50], [200, 150], [300, 250], [400, 350], [500, 450], [600, 550]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 50], [200, 150], [300, 250], [400, 350], [500, 450], [600, 550]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 1000], [900, 900], [800, 800], [700, 700], [600, 600], [500, 500]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 1000], [900, 900], [800, 800], [700, 700], [600, 600], [500, 500]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[300, 600], [200, 500], [100, 400], [50, 300], [25, 250], [10, 200], [5, 150], [2, 100]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[300, 600], [200, 500], [100, 400], [50, 300], [25, 250], [10, 200], [5, 150], [2, 100]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 15], [20, 20], [30, 25], [40, 30], [50, 35], [60, 40], [70, 45], [80, 50], [90, 55], [100, 60]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 15], [20, 20], [30, 25], [40, 30], [50, 35], [60, 40], [70, 45], [80, 50], [90, 55], [100, 60]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160], [160, 170], [170, 180], [180, 190], [190, 200]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160], [160, 170], [170, 180], [180, 190], [190, 200]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [500, 1500], [250, 1000], [125, 500], [62, 250], [31, 125], [15, 62], [7, 31], [3, 15], [1, 7]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [500, 1500], [250, 1000], [125, 500], [62, 250], [31, 125], [15, 62], [7, 31], [3, 15], [1, 7]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [100, 1000], [500, 2000], [100, 3000], [500, 2500]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [100, 1000], [500, 2000], [100, 3000], [500, 2500]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70], [10, 80], [10, 90], [10, 100], [10, 110], [10, 120], [10, 130], [10, 140], [10, 150], [10, 160], [10, 170], [10, 180], [10, 190], [10, 200], [10, 210], [10, 220], [10, 230], [10, 240], [10, 250], [10, 260], [10, 270], [10, 280], [10, 290], [10, 300]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70], [10, 80], [10, 90], [10, 100], [10, 110], [10, 120], [10, 130], [10, 140], [10, 150], [10, 160], [10, 170], [10, 180], [10, 190], [10, 200], [10, 210], [10, 220], [10, 230], [10, 240], [10, 250], [10, 260], [10, 270], [10, 280], [10, 290], [10, 300]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 1], [2, 3], [3, 6], [4, 10], [5, 15], [6, 21]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 1], [2, 3], [3, 6], [4, 10], [5, 15], [6, 21]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 10], [4, 15], [6, 20], [3, 25], [7, 30], [2, 35], [8, 40], [1, 45]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 10], [4, 15], [6, 20], [3, 25], [7, 30], [2, 35], [8, 40], [1, 45]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 600], [500, 700], [500, 800], [500, 900], [500, 1000], [500, 1100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 600], [500, 700], [500, 800], [500, 900], [500, 1000], [500, 1100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [40, 50], [20, 100], [10, 11], [5, 6]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [40, 50], [20, 100], [10, 11], [5, 6]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[200, 500], [100, 400], [150, 300], [50, 200], [300, 700], [400, 800]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[200, 500], [100, 400], [150, 300], [50, 200], [300, 700], [400, 800]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [500, 1500], [300, 1000], [100, 400], [50, 300]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [500, 1500], [300, 1000], [100, 400], [50, 300]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [200, 500], [300, 800], [400, 1200], [100, 300]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [200, 500], [300, 800], [400, 1200], [100, 300]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [1500, 2500], [2000, 3000], [500, 1500], [1000, 2500], [1500, 3000], [2000, 3500], [500, 2000], [1000, 3000], [1500, 3500]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [1500, 2500], [2000, 3000], [500, 1500], [1000, 2500], [1500, 3000], [2000, 3500], [500, 2000], [1000, 3000], [1500, 3500]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [500, 2500], [800, 3000], [1500, 4000]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [500, 2500], [800, 3000], [1500, 4000]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 1200], [500, 700], [250, 400], [125, 200], [62, 100], [31, 50], [15, 25], [7, 12], [3, 6], [1, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 1200], [500, 700], [250, 400], [125, 200], [62, 100], [31, 50], [15, 25], [7, 12], [3, 6], [1, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[50, 100], [10, 20], [40, 150], [30, 120], [15, 80]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[50, 100], [10, 20], [40, 150], [30, 120], [15, 80]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 1500], [2000, 2500], [3000, 3500], [4000, 4500], [5000, 5500]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 1500], [2000, 2500], [3000, 3500], [4000, 4500], [5000, 5500]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [900, 1900], [800, 1800], [700, 1700], [600, 1600], [500, 1500], [400, 1400], [300, 1300], [200, 1200], [100, 1100]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [900, 1900], [800, 1800], [700, 1700], [600, 1600], [500, 1500], [400, 1400], [300, 1300], [200, 1200], [100, 1100]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [10, 16], [10, 17], [10, 18], [10, 19], [10, 20], [10, 21], [10, 22], [10, 23], [10, 24], [10, 25], [10, 26], [10, 27], [10, 28], [10, 29], [10, 30]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [10, 16], [10, 17], [10, 18], [10, 19], [10, 20], [10, 21], [10, 22], [10, 23], [10, 24], [10, 25], [10, 26], [10, 27], [10, 28], [10, 29], [10, 30]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[50, 100], [25, 100], [75, 150], [50, 150], [25, 150], [100, 200], [75, 200], [125, 250]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[50, 100], [25, 100], [75, 150], [50, 150], [25, 150], [100, 200], [75, 200], [125, 250]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 30], [20, 50], [30, 70], [40, 90], [50, 110], [60, 130], [70, 150]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 30], [20, 50], [30, 70], [40, 90], [50, 110], [60, 130], [70, 150]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[300, 400], [200, 300], [100, 200], [50, 150], [10, 100]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[300, 400], [200, 300], [100, 200], [50, 150], [10, 100]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[50, 100], [50, 150], [50, 200], [50, 250], [50, 300], [50, 350], [50, 400]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[50, 100], [50, 150], [50, 200], [50, 250], [50, 300], [50, 350], [50, 400]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[150, 300], [100, 450], [50, 300], [200, 600], [250, 750], [100, 500], [50, 350], [300, 800]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[150, 300], [100, 450], [50, 300], [200, 600], [250, 750], [100, 500], [50, 350], [300, 800]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100], [60, 120], [70, 140], [80, 160], [90, 180], [100, 200]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100], [60, 120], [70, 140], [80, 160], [90, 180], [100, 200]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 700], [600, 1200], [100, 600], [400, 900], [300, 800], [200, 500]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 700], [600, 1200], [100, 600], [400, 900], [300, 800], [200, 500]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000], [6000, 6000], [7000, 7000], [8000, 8000], [9000, 9000], [10000, 10000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000], [6000, 6000], [7000, 7000], [8000, 8000], [9000, 9000], [10000, 10000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[300, 600], [500, 900], [200, 500], [400, 800], [600, 1200], [100, 400], [700, 1100]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[300, 600], [500, 900], [200, 500], [400, 800], [600, 1200], [100, 400], [700, 1100]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 1000], [1, 999], [1, 998], [1, 997], [1, 996], [1, 995], [1, 994], [1, 993], [1, 992], [1, 991]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 1000], [1, 999], [1, 998], [1, 997], [1, 996], [1, 995], [1, 994], [1, 993], [1, 992], [1, 991]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[50, 200], [100, 250], [150, 300], [200, 350], [250, 400], [300, 450], [350, 500], [400, 550], [450, 600]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[50, 200], [100, 250], [150, 300], [200, 350], [250, 400], [300, 450], [350, 500], [400, 550], [450, 600]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 900], [200, 1000], [300, 1200], [400, 1500], [100, 600], [200, 800]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 900], [200, 1000], [300, 1200], [400, 1500], [100, 600], [200, 800]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50], [50, 55]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50], [50, 55]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [500, 2500]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [500, 2500]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 800], [200, 600], [400, 1000], [300, 750], [100, 500]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 800], [200, 600], [400, 1000], [300, 750], [100, 500]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [50, 250], [200, 400], [150, 350], [50, 200]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [50, 250], [200, 400], [150, 350], [50, 200]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[50, 150], [100, 250], [150, 350], [200, 450], [250, 550], [300, 650], [350, 750], [400, 850]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[50, 150], [100, 250], [150, 350], [200, 450], [250, 550], [300, 650], [350, 750], [400, 850]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 500], [100, 1000], [100, 1500], [100, 2000], [100, 2500], [100, 3000]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 500], [100, 1000], [100, 1500], [100, 2000], [100, 2500], [100, 3000]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 50], [20, 60], [30, 70], [40, 80], [50, 90], [60, 100], [70, 110], [80, 120], [90, 130], [100, 140]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 50], [20, 60], [30, 70], [40, 80], [50, 90], [60, 100], [70, 110], [80, 120], [90, 130], [100, 140]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [10, 110], [20, 120], [30, 130], [40, 140], [50, 150], [60, 160], [70, 170], [80, 180], [90, 190], [100, 200]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [10, 110], [20, 120], [30, 130], [40, 140], [50, 150], [60, 160], [70, 170], [80, 180], [90, 190], [100, 200]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [500, 1500], [200, 500], [100, 300], [50, 250]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [500, 1500], [200, 500], [100, 300], [50, 250]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[300, 500], [300, 400], [200, 300], [400, 600], [100, 200]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[300, 500], [300, 400], [200, 300], [400, 600], [100, 200]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40], [45, 45], [50, 50]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40], [45, 45], [50, 50]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 10], [1, 2], [3, 7], [1, 5], [2, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 10], [1, 2], [3, 7], [1, 5], [2, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[7, 10], [3, 9], [2, 5], [4, 11], [6, 12]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[7, 10], [3, 9], [2, 5], [4, 11], [6, 12]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 5], [6, 10], [7, 12], [2, 3], [3, 8], [1, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 5], [6, 10], [7, 12], [2, 3], [3, 8], [1, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [1000, 3000], [1000, 4000], [1000, 5000], [1000, 6000]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [1000, 3000], [1000, 4000], [1000, 5000], [1000, 6000]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [1000, 2000], [1500, 3000], [2000, 4000], [2500, 5000], [3000, 6000]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [1000, 2000], [1500, 3000], [2000, 4000], [2500, 5000], [3000, 6000]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [50, 100], [150, 400]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [50, 100], [150, 400]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 150], [100, 100], [100, 250], [100, 300], [100, 350]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 150], [100, 100], [100, 250], [100, 300], [100, 350]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50], [30, 60], [35, 70], [40, 80], [45, 90], [50, 100], [55, 110], [60, 120], [65, 130], [70, 140], [75, 150], [80, 160], [85, 170], [90, 180], [95, 190], [100, 200]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50], [30, 60], [35, 70], [40, 80], [45, 90], [50, 100], [55, 110], [60, 120], [65, 130], [70, 140], [75, 150], [80, 160], [85, 170], [90, 180], [95, 190], [100, 200]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [300, 600], [200, 1000], [100, 1200], [400, 800], [600, 1200]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [300, 600], [200, 1000], [100, 1200], [400, 800], [600, 1200]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 200], [100, 250], [100, 300], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [100, 600], [100, 650], [100, 700]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 200], [100, 250], [100, 300], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [100, 600], [100, 650], [100, 700]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1000, 2000], [500, 1000], [250, 750], [125, 500], [63, 350], [32, 250], [16, 175], [8, 125], [4, 80], [2, 50]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1000, 2000], [500, 1000], [250, 750], [125, 500], [63, 350], [32, 250], [16, 175], [8, 125], [4, 80], [2, 50]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[100, 250], [200, 500], [300, 750], [400, 1000], [500, 1250], [600, 1500], [700, 1750], [800, 2000]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[100, 250], [200, 500], [300, 750], [400, 1000], [500, 1250], [600, 1500], [700, 1750], [800, 2000]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[2000, 3000], [1000, 2500], [500, 1500], [250, 1000], [125, 500], [62, 250], [31, 125], [15, 62], [7, 31]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[2000, 3000], [1000, 2500], [500, 1500], [250, 1000], [125, 500], [62, 250], [31, 125], [15, 62], [7, 31]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[500, 1000], [300, 600], [200, 800], [400, 900], [100, 500], [700, 1200]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[500, 1000], [300, 600], [200, 800], [400, 900], [100, 500], [700, 1200]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(courses = [[300, 500], [200, 400], [100, 300], [50, 200], [25, 100], [12, 50], [6, 25], [3, 12], [1, 6]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(courses = [[300, 500], [200, 400], [100, 300], [50, 200], [25, 100], [12, 50], [6, 25], [3, 12], [1, 6]]) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [11, 15], [11, 16], [8, 13], [11, 17], [4, 11], [2, 12]]) == 4
    assert candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [300, 3100]]) == 4
    assert candidate(courses = [[10, 100], [10, 100], [10, 100], [10, 100], [10, 100]]) == 5
    assert candidate(courses = [[5, 5], [3, 6], [7, 8], [2, 4]]) == 2
    assert candidate(courses = [[5, 5], [2, 5], [4, 6]]) == 2
    assert candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 16], [8, 14]]) == 3
    assert candidate(courses = [[10, 15], [20, 30], [10, 25]]) == 2
    assert candidate(courses = [[1, 2]]) == 1
    assert candidate(courses = [[100, 100], [200, 200], [300, 300]]) == 1
    assert candidate(courses = [[3, 7], [4, 9], [4, 10], [2, 5]]) == 3
    assert candidate(courses = [[3, 2], [4, 3]]) == 0
    assert candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
    assert candidate(courses = [[10, 100], [20, 200], [30, 300], [40, 400]]) == 4
    assert candidate(courses = [[100, 200], [200, 1000], [500, 1500]]) == 3
    assert candidate(courses = [[9, 14], [2, 11], [8, 12], [8, 13], [10, 14], [2, 4]]) == 3
    assert candidate(courses = [[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 10], [4, 8]]) == 4
    assert candidate(courses = [[5, 5], [5, 6], [6, 10]]) == 1
    assert candidate(courses = [[5, 20], [10, 25], [15, 30]]) == 3
    assert candidate(courses = [[4, 7], [2, 10], [3, 10]]) == 3
    assert candidate(courses = [[5, 5], [4, 6], [2, 6]]) == 2
    assert candidate(courses = [[1, 3], [2, 5], [3, 7], [4, 9]]) == 3
    assert candidate(courses = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert candidate(courses = [[5, 15], [3, 19], [6, 7], [2, 10], [5, 16], [8, 14], [10, 11], [2, 19]]) == 5
    assert candidate(courses = [[2, 5], [2, 7], [2, 10], [3, 15]]) == 4
    assert candidate(courses = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 16], [8, 14], [10, 16], [4, 8]]) == 3
    assert candidate(courses = [[5, 15], [10, 20], [15, 30]]) == 3
    assert candidate(courses = [[1, 2], [2, 5], [4, 6], [7, 8]]) == 2
    assert candidate(courses = [[1, 20], [2, 30], [3, 40], [4, 50]]) == 4
    assert candidate(courses = [[10, 20], [20, 40], [30, 60]]) == 3
    assert candidate(courses = [[1, 100], [2, 101], [3, 102], [4, 103], [5, 104]]) == 5
    assert candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996]]) == 5
    assert candidate(courses = [[10, 100], [10, 200], [10, 300], [10, 400], [10, 500], [10, 600], [10, 700], [10, 800], [10, 900], [10, 1000], [10, 1100], [10, 1200]]) == 12
    assert candidate(courses = [[100, 200], [150, 300], [50, 250], [200, 500], [100, 400]]) == 4
    assert candidate(courses = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000], [11, 1100], [12, 1200], [13, 1300], [14, 1400], [15, 1500]]) == 15
    assert candidate(courses = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20], [1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == 5
    assert candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160]]) == 2
    assert candidate(courses = [[300, 500], [200, 400], [100, 300], [200, 500], [100, 400], [300, 600]]) == 3
    assert candidate(courses = [[100, 500], [50, 250], [200, 600], [300, 900], [100, 400], [250, 700]]) == 5
    assert candidate(courses = [[5, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
    assert candidate(courses = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21], [11, 23], [12, 25], [13, 27], [14, 29], [15, 31]]) == 5
    assert candidate(courses = [[100, 300], [200, 700], [100, 500], [200, 800], [100, 600], [200, 900], [100, 700], [200, 1000]]) == 7
    assert candidate(courses = [[10000, 10001], [10000, 10002], [10000, 10003], [10000, 10004], [10000, 10005]]) == 1
    assert candidate(courses = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 1
    assert candidate(courses = [[100, 250], [100, 300], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [100, 600]]) == 6
    assert candidate(courses = [[100, 300], [200, 500], [100, 400], [200, 600], [300, 800], [100, 500], [200, 700]]) == 5
    assert candidate(courses = [[100, 200], [200, 400], [300, 600], [400, 800], [500, 1000], [600, 1200], [700, 1400], [800, 1600], [900, 1800]]) == 4
    assert candidate(courses = [[5, 5], [3, 6], [2, 10], [10, 12], [4, 8]]) == 3
    assert candidate(courses = [[500, 1000], [1000, 2000], [500, 1500], [1000, 2500], [500, 2000], [1000, 3000], [500, 2500], [1000, 3500], [500, 3000], [1000, 4000]]) == 6
    assert candidate(courses = [[100, 200], [50, 150], [30, 100], [200, 300], [10, 50]]) == 4
    assert candidate(courses = [[100, 300], [200, 400], [300, 500], [400, 600], [500, 700], [600, 800], [700, 900], [800, 1000]]) == 2
    assert candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]]) == 10
    assert candidate(courses = [[5, 10], [3, 8], [4, 9], [2, 6], [7, 12], [1, 5], [6, 11], [8, 13], [9, 14], [10, 15]]) == 3
    assert candidate(courses = [[10, 20], [9, 19], [8, 18], [7, 17], [6, 16], [5, 15], [4, 14], [3, 13], [2, 12], [1, 11], [11, 21], [12, 22], [13, 23], [14, 24], [15, 25]]) == 5
    assert candidate(courses = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]]) == 10
    assert candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000]]) == 2
    assert candidate(courses = [[100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300], [100, 300]]) == 3
    assert candidate(courses = [[100, 50], [200, 150], [300, 250], [400, 350], [500, 450], [600, 550]]) == 0
    assert candidate(courses = [[1000, 1000], [900, 900], [800, 800], [700, 700], [600, 600], [500, 500]]) == 1
    assert candidate(courses = [[300, 600], [200, 500], [100, 400], [50, 300], [25, 250], [10, 200], [5, 150], [2, 100]]) == 7
    assert candidate(courses = [[10, 15], [20, 20], [30, 25], [40, 30], [50, 35], [60, 40], [70, 45], [80, 50], [90, 55], [100, 60]]) == 1
    assert candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110], [110, 120], [120, 130], [130, 140], [140, 150], [150, 160], [160, 170], [170, 180], [180, 190], [190, 200]]) == 2
    assert candidate(courses = [[1000, 2000], [500, 1500], [250, 1000], [125, 500], [62, 250], [31, 125], [15, 62], [7, 31], [3, 15], [1, 7]]) == 10
    assert candidate(courses = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]]) == 10
    assert candidate(courses = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100]]) == 2
    assert candidate(courses = [[500, 1000], [100, 1000], [500, 2000], [100, 3000], [500, 2500]]) == 5
    assert candidate(courses = [[10, 20], [10, 30], [10, 40], [10, 50], [10, 60], [10, 70], [10, 80], [10, 90], [10, 100], [10, 110], [10, 120], [10, 130], [10, 140], [10, 150], [10, 160], [10, 170], [10, 180], [10, 190], [10, 200], [10, 210], [10, 220], [10, 230], [10, 240], [10, 250], [10, 260], [10, 270], [10, 280], [10, 290], [10, 300]]) == 29
    assert candidate(courses = [[1, 1], [2, 3], [3, 6], [4, 10], [5, 15], [6, 21]]) == 6
    assert candidate(courses = [[5, 10], [4, 15], [6, 20], [3, 25], [7, 30], [2, 35], [8, 40], [1, 45]]) == 8
    assert candidate(courses = [[500, 600], [500, 700], [500, 800], [500, 900], [500, 1000], [500, 1100]]) == 2
    assert candidate(courses = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 1
    assert candidate(courses = [[10, 20], [40, 50], [20, 100], [10, 11], [5, 6]]) == 3
    assert candidate(courses = [[200, 500], [100, 400], [150, 300], [50, 200], [300, 700], [400, 800]]) == 4
    assert candidate(courses = [[1000, 2000], [500, 1500], [300, 1000], [100, 400], [50, 300]]) == 5
    assert candidate(courses = [[500, 1000], [200, 500], [300, 800], [400, 1200], [100, 300]]) == 4
    assert candidate(courses = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]]) == 3
    assert candidate(courses = [[1000, 2000], [1500, 2500], [2000, 3000], [500, 1500], [1000, 2500], [1500, 3000], [2000, 3500], [500, 2000], [1000, 3000], [1500, 3500]]) == 4
    assert candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [500, 2500], [800, 3000], [1500, 4000]]) == 5
    assert candidate(courses = [[1000, 1200], [500, 700], [250, 400], [125, 200], [62, 100], [31, 50], [15, 25], [7, 12], [3, 6], [1, 3]]) == 6
    assert candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100]]) == 2
    assert candidate(courses = [[50, 100], [10, 20], [40, 150], [30, 120], [15, 80]]) == 5
    assert candidate(courses = [[1000, 1500], [2000, 2500], [3000, 3500], [4000, 4500], [5000, 5500]]) == 1
    assert candidate(courses = [[1000, 2000], [900, 1900], [800, 1800], [700, 1700], [600, 1600], [500, 1500], [400, 1400], [300, 1300], [200, 1200], [100, 1100]]) == 5
    assert candidate(courses = [[10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [10, 16], [10, 17], [10, 18], [10, 19], [10, 20], [10, 21], [10, 22], [10, 23], [10, 24], [10, 25], [10, 26], [10, 27], [10, 28], [10, 29], [10, 30]]) == 3
    assert candidate(courses = [[50, 100], [25, 100], [75, 150], [50, 150], [25, 150], [100, 200], [75, 200], [125, 250]]) == 4
    assert candidate(courses = [[10, 30], [20, 50], [30, 70], [40, 90], [50, 110], [60, 130], [70, 150]]) == 4
    assert candidate(courses = [[300, 400], [200, 300], [100, 200], [50, 150], [10, 100]]) == 3
    assert candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
    assert candidate(courses = [[50, 100], [50, 150], [50, 200], [50, 250], [50, 300], [50, 350], [50, 400]]) == 7
    assert candidate(courses = [[150, 300], [100, 450], [50, 300], [200, 600], [250, 750], [100, 500], [50, 350], [300, 800]]) == 6
    assert candidate(courses = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800]]) == 2
    assert candidate(courses = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100], [60, 120], [70, 140], [80, 160], [90, 180], [100, 200]]) == 4
    assert candidate(courses = [[500, 700], [600, 1200], [100, 600], [400, 900], [300, 800], [200, 500]]) == 4
    assert candidate(courses = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000], [6000, 6000], [7000, 7000], [8000, 8000], [9000, 9000], [10000, 10000]]) == 1
    assert candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]]) == 2
    assert candidate(courses = [[300, 600], [500, 900], [200, 500], [400, 800], [600, 1200], [100, 400], [700, 1100]]) == 4
    assert candidate(courses = [[1, 1000], [1, 999], [1, 998], [1, 997], [1, 996], [1, 995], [1, 994], [1, 993], [1, 992], [1, 991]]) == 10
    assert candidate(courses = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 2
    assert candidate(courses = [[50, 200], [100, 250], [150, 300], [200, 350], [250, 400], [300, 450], [350, 500], [400, 550], [450, 600]]) == 3
    assert candidate(courses = [[500, 900], [200, 1000], [300, 1200], [400, 1500], [100, 600], [200, 800]]) == 5
    assert candidate(courses = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50], [50, 55]]) == 2
    assert candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [500, 2500]]) == 4
    assert candidate(courses = [[500, 800], [200, 600], [400, 1000], [300, 750], [100, 500]]) == 4
    assert candidate(courses = [[100, 200], [50, 250], [200, 400], [150, 350], [50, 200]]) == 4
    assert candidate(courses = [[50, 150], [100, 250], [150, 350], [200, 450], [250, 550], [300, 650], [350, 750], [400, 850]]) == 4
    assert candidate(courses = [[100, 500], [100, 1000], [100, 1500], [100, 2000], [100, 2500], [100, 3000]]) == 6
    assert candidate(courses = [[10, 50], [20, 60], [30, 70], [40, 80], [50, 90], [60, 100], [70, 110], [80, 120], [90, 130], [100, 140]]) == 3
    assert candidate(courses = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [10, 110], [20, 120], [30, 130], [40, 140], [50, 150], [60, 160], [70, 170], [80, 180], [90, 190], [100, 200]]) == 6
    assert candidate(courses = [[1000, 2000], [500, 1500], [200, 500], [100, 300], [50, 250]]) == 5
    assert candidate(courses = [[300, 500], [300, 400], [200, 300], [400, 600], [100, 200]]) == 2
    assert candidate(courses = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40], [45, 45], [50, 50]]) == 1
    assert candidate(courses = [[500, 1000], [1000, 2000], [1500, 2500], [2000, 3000], [2500, 3500]]) == 2
    assert candidate(courses = [[5, 10], [1, 2], [3, 7], [1, 5], [2, 4]]) == 4
    assert candidate(courses = [[7, 10], [3, 9], [2, 5], [4, 11], [6, 12]]) == 3
    assert candidate(courses = [[5, 5], [6, 10], [7, 12], [2, 3], [3, 8], [1, 4]]) == 3
    assert candidate(courses = [[1000, 2000], [1000, 3000], [1000, 4000], [1000, 5000], [1000, 6000]]) == 5
    assert candidate(courses = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000]]) == 1
    assert candidate(courses = [[500, 1000], [1000, 2000], [1500, 3000], [2000, 4000], [2500, 5000], [3000, 6000]]) == 4
    assert candidate(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200], [50, 100], [150, 400]]) == 5
    assert candidate(courses = [[100, 150], [100, 100], [100, 250], [100, 300], [100, 350]]) == 3
    assert candidate(courses = [[100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200], [100, 200]]) == 2
    assert candidate(courses = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50], [30, 60], [35, 70], [40, 80], [45, 90], [50, 100], [55, 110], [60, 120], [65, 130], [70, 140], [75, 150], [80, 160], [85, 170], [90, 180], [95, 190], [100, 200]]) == 5
    assert candidate(courses = [[500, 1000], [300, 600], [200, 1000], [100, 1200], [400, 800], [600, 1200]]) == 4
    assert candidate(courses = [[100, 200], [100, 250], [100, 300], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [100, 600], [100, 650], [100, 700]]) == 7
    assert candidate(courses = [[1000, 2000], [500, 1000], [250, 750], [125, 500], [63, 350], [32, 250], [16, 175], [8, 125], [4, 80], [2, 50]]) == 10
    assert candidate(courses = [[100, 250], [200, 500], [300, 750], [400, 1000], [500, 1250], [600, 1500], [700, 1750], [800, 2000]]) == 5
    assert candidate(courses = [[2000, 3000], [1000, 2500], [500, 1500], [250, 1000], [125, 500], [62, 250], [31, 125], [15, 62], [7, 31]]) == 8
    assert candidate(courses = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]]) == 10
    assert candidate(courses = [[500, 1000], [300, 600], [200, 800], [400, 900], [100, 500], [700, 1200]]) == 3
    assert candidate(courses = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]) == 2
    assert candidate(courses = [[300, 500], [200, 400], [100, 300], [50, 200], [25, 100], [12, 50], [6, 25], [3, 12], [1, 6]]) == 8


