def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 10], [0, 9], [0, 8], [0, 7]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 10], [0, 9], [0, 8], [0, 7]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3]]) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3]]) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3], [2, 2]]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3], [2, 2]]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0]],bikes = [[0, 0]]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0]],bikes = [[0, 0]]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 0]],bikes = [[1, 0], [2, 2], [2, 1]]) == [0, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 0]],bikes = [[1, 0], [2, 2], [2, 1]]) == [0, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]) == [4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]) == [4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 0], [0, 0]],bikes = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 0], [0, 0]],bikes = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 4], [0, 5], [0, 6], [0, 7]]) == [3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 4], [0, 5], [0, 6], [0, 7]]) == [3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1000, 1000], [0, 1000], [1000, 0]],bikes = [[500, 500], [250, 250], [750, 750], [0, 0]]) == [3, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1000, 1000], [0, 1000], [1000, 0]],bikes = [[500, 500], [250, 250], [750, 750], [0, 0]]) == [3, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [2, 2], [4, 4]],bikes = [[1, 1], [3, 3], [5, 5], [7, 7]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [2, 2], [4, 4]],bikes = [[1, 1], [3, 3], [5, 5], [7, 7]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [200, 200], [150, 150], [100, 100]],bikes = [[100, 50], [200, 100], [50, 200], [150, 150]]) == [0, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [200, 200], [150, 150], [100, 100]],bikes = [[100, 50], [200, 100], [50, 200], [150, 150]]) == [0, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [0, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [0, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [0, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [0, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 0], [20, 0], [30, 0]],bikes = [[5, 0], [15, 0], [25, 0], [35, 0]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 0], [20, 0], [30, 0]],bikes = [[5, 0], [15, 0], [25, 0], [35, 0]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[2, 2], [1, 1], [3, 3], [4, 4], [5, 5]]) == [1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[2, 2], [1, 1], [3, 3], [4, 4], [5, 5]]) == [1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [1, 3], [2, 2]],bikes = [[2, 1], [3, 3], [4, 4], [5, 5]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [1, 3], [2, 2]],bikes = [[2, 1], [3, 3], [4, 4], [5, 5]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[6, 5], [4, 3], [2, 1], [7, 8]]) == [2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[6, 5], [4, 3], [2, 1], [7, 8]]) == [2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [2, 2], [4, 4]],bikes = [[1, 1], [3, 3], [5, 5], [6, 6], [7, 7]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [2, 2], [4, 4]],bikes = [[1, 1], [3, 3], [5, 5], [6, 6], [7, 7]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996]],bikes = [[1000, 1000], [999, 999], [998, 998], [997, 997], [996, 996], [995, 995]]) == [1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996]],bikes = [[1000, 1000], [999, 999], [998, 998], [997, 997], [996, 996], [995, 995]]) == [1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 999], [0, 0], [500, 500]],bikes = [[500, 499], [501, 500], [499, 500], [0, 1], [1, 0], [998, 998]]) == [5, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 999], [0, 0], [500, 500]],bikes = [[500, 499], [501, 500], [499, 500], [0, 1], [1, 0], [998, 998]]) == [5, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0]],bikes = [[0, 1], [1, 1], [2, 1], [3, 1]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0]],bikes = [[0, 1], [1, 1], [2, 1], [3, 1]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[6, 5], [4, 3], [2, 1], [0, 0], [8, 8]]) == [2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[6, 5], [4, 3], [2, 1], [0, 0], [8, 8]]) == [2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == [3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == [3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [1, 3], [3, 1], [3, 3]],bikes = [[0, 0], [0, 2], [2, 0], [2, 2], [4, 4]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [1, 3], [3, 1], [3, 3]],bikes = [[0, 0], [0, 2], [2, 0], [2, 2], [4, 4]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[200, 100], [100, 200], [300, 200]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[200, 100], [100, 200], [300, 200]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 0], [0, 0], [0, 0]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 0], [0, 0], [0, 0]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4]]) == [0, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4]]) == [0, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1]]) == [3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1]]) == [3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3]]) == [3, 0, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3]]) == [3, 0, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [100, 100], [200, 200], [300, 300]]) == [4, 5, 6, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [100, 100], [200, 200], [300, 300]]) == [4, 5, 6, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [100, 0], [200, 0], [300, 0]],bikes = [[0, 0], [0, 100], [0, 200], [0, 300], [0, 400], [0, 500]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [100, 0], [200, 0], [300, 0]],bikes = [[0, 0], [0, 100], [0, 200], [0, 300], [0, 400], [0, 500]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1000, 1000]],bikes = [[500, 500], [250, 250], [750, 750]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1000, 1000]],bikes = [[500, 500], [250, 250], [750, 750]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 2], [0, 4], [0, 6]],bikes = [[1, 1], [1, 3], [1, 5], [1, 7]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 2], [0, 4], [0, 6]],bikes = [[1, 1], [1, 3], [1, 5], [1, 7]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1000, 1000], [500, 500]],bikes = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1000, 1000], [500, 500]],bikes = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1000], [1000, 0], [1000, 1000]],bikes = [[500, 500], [0, 500], [500, 0], [500, 1000], [1000, 500]]) == [1, 3, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1000], [1000, 0], [1000, 1000]],bikes = [[500, 500], [0, 500], [500, 0], [500, 1000], [1000, 500]]) == [1, 3, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [6, 6], [9, 9], [11, 11], [12, 12]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [6, 6], [9, 9], [11, 11], [12, 12]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [1, 2, 3, 4, 5, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [1, 2, 3, 4, 5, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == [5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == [5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [1, 2, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [1, 2, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 0], [0, 10], [10, 10], [0, 0]],bikes = [[10, 10], [10, 0], [0, 10], [0, 0], [5, 5], [1, 1], [9, 9], [8, 8]]) == [1, 2, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 0], [0, 10], [10, 10], [0, 0]],bikes = [[10, 10], [10, 0], [0, 10], [0, 0], [5, 5], [1, 1], [9, 9], [8, 8]]) == [1, 2, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 999], [998, 998], [997, 997]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == [8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 999], [998, 998], [997, 997]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == [8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[500, 500], [400, 400], [300, 300]],bikes = [[200, 200], [100, 100], [0, 0], [900, 900], [800, 800], [700, 700]]) == [5, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[500, 500], [400, 400], [300, 300]],bikes = [[200, 200], [100, 100], [0, 0], [900, 900], [800, 800], [700, 700]]) == [5, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[1, 2], [2, 1], [2, 2], [1, 1], [0, 2], [0, 0]]) == [5, 4, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[1, 2], [2, 1], [2, 2], [1, 1], [0, 2], [0, 0]]) == [5, 4, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[3, 3], [2, 2], [1, 1], [0, 0]]) == [3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[3, 3], [2, 2], [1, 1], [0, 0]]) == [3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 4], [5, 0], [2, 3]],bikes = [[2, 5], [1, 1], [3, 0], [3, 4], [6, 2]]) == [1, 0, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 4], [5, 0], [2, 3]],bikes = [[2, 5], [1, 1], [3, 0], [3, 4], [6, 2]]) == [1, 0, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [1, 2], [2, 1], [2, 2]],bikes = [[1, 3], [3, 1], [3, 3], [2, 2], [1, 1], [2, 1], [1, 2]]) == [4, 6, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [1, 2], [2, 1], [2, 2]],bikes = [[1, 3], [3, 1], [3, 3], [2, 2], [1, 1], [2, 1], [1, 2]]) == [4, 6, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [100, 100], [150, 150]],bikes = [[100, 100], [50, 50], [150, 150], [200, 200], [250, 250]]) == [1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [100, 100], [150, 150]],bikes = [[100, 100], [50, 50], [150, 150], [200, 200], [250, 250]]) == [1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[500, 500], [501, 501], [499, 499], [502, 502]],bikes = [[500, 500], [501, 501], [499, 499], [502, 502], [503, 503]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[500, 500], [501, 501], [499, 499], [502, 502]],bikes = [[500, 500], [501, 501], [499, 499], [502, 502], [503, 503]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [1, 3], [3, 4], [3, 0], [2, 5]],bikes = [[0, 0], [0, 3], [0, 4], [1, 1], [1, 2], [2, 2], [3, 3], [4, 2]]) == [3, 1, 6, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [1, 3], [3, 4], [3, 0], [2, 5]],bikes = [[0, 0], [0, 3], [0, 4], [1, 1], [1, 2], [2, 2], [3, 3], [4, 2]]) == [3, 1, 6, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 1], [1, 0], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 1], [3, 2]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 1], [1, 0], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 1], [3, 2]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],bikes = [[2, 1], [4, 3], [6, 5], [8, 7], [10, 9], [0, 0]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],bikes = [[2, 1], [4, 3], [6, 5], [8, 7], [10, 9], [0, 0]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501], [601, 601]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501], [601, 601]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 5], [6, 6], [7, 7]],bikes = [[5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 5], [6, 6], [7, 7]],bikes = [[5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 0], [2, 1], [3, 2]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 0], [2, 1], [3, 2]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750]],bikes = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750], [375, 375], [625, 625], [500, 250]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750]],bikes = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750], [375, 375], [625, 625], [500, 250]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[105, 105], [205, 205], [305, 305], [405, 405], [505, 505], [605, 605]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[105, 105], [205, 205], [305, 305], [405, 405], [505, 505], [605, 605]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[200, 200], [200, 250], [200, 300], [200, 350], [200, 400]],bikes = [[250, 250], [250, 300], [250, 350], [250, 400], [250, 450]]) == [4, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[200, 200], [200, 250], [200, 300], [200, 350], [200, 400]],bikes = [[250, 250], [250, 300], [250, 350], [250, 400], [250, 450]]) == [4, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[0, 0], [5, 5], [10, 10], [15, 15], [20, 20]]) == [1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[0, 0], [5, 5], [10, 10], [15, 15], [20, 20]]) == [1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[2, 1], [4, 3], [6, 5], [7, 8], [8, 7], [9, 6]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[2, 1], [4, 3], [6, 5], [7, 8], [8, 7], [9, 6]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 1], [1, 0], [2, 1], [3, 2], [4, 3]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 1], [1, 0], [2, 1], [3, 2], [4, 3]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [2, 1], [3, 3]],bikes = [[2, 2], [3, 1], [1, 3], [2, 3]]) == [0, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [2, 1], [3, 3]],bikes = [[2, 2], [3, 1], [1, 3], [2, 3]]) == [0, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 10], [20, 20], [30, 30], [40, 40]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 10], [20, 20], [30, 30], [40, 40]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 5], [10, 10], [15, 15], [20, 20]],bikes = [[10, 5], [15, 10], [20, 15], [25, 20], [30, 25]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 5], [10, 10], [15, 15], [20, 20]],bikes = [[10, 5], [15, 10], [20, 15], [25, 20], [30, 25]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [6, 6], [11, 11]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [6, 6], [11, 11]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [1, 2, 3, 4, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [1, 2, 3, 4, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 100], [1, 200], [1, 300]],bikes = [[2, 200], [2, 300], [2, 400], [2, 500], [2, 600]]) == [2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 100], [1, 200], [1, 300]],bikes = [[2, 200], [2, 300], [2, 400], [2, 500], [2, 600]]) == [2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [11, 11], [12, 12], [13, 13]],bikes = [[10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [11, 11], [12, 12], [13, 13]],bikes = [[10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 0], [0, 0]],bikes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 0], [0, 0]],bikes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [51, 51], [52, 52], [53, 53], [54, 54]],bikes = [[50, 51], [51, 52], [52, 53], [53, 54], [54, 55], [55, 56], [56, 57]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [51, 51], [52, 52], [53, 53], [54, 54]],bikes = [[50, 51], [51, 52], [52, 53], [53, 54], [54, 55], [55, 56], [56, 57]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 5], [6, 6], [7, 7], [8, 8]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 5], [6, 6], [7, 7], [8, 8]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [5, 6, 7, 8]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 10], [0, 9], [0, 8], [0, 7]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3]]) == [1, 0]
    assert candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3], [2, 2]]) == [0, 2]
    assert candidate(workers = [[0, 0]],bikes = [[0, 0]]) == [0]
    assert candidate(workers = [[0, 0], [1, 1], [2, 0]],bikes = [[1, 0], [2, 2], [2, 1]]) == [0, 2, 1]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]) == [4, 3, 2, 1]
    assert candidate(workers = [[0, 0], [0, 0], [0, 0]],bikes = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 4], [0, 5], [0, 6], [0, 7]]) == [3, 2, 1, 0]
    assert candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [1000, 1000], [0, 1000], [1000, 0]],bikes = [[500, 500], [250, 250], [750, 750], [0, 0]]) == [3, 2, 0, 1]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [2, 2], [4, 4]],bikes = [[1, 1], [3, 3], [5, 5], [7, 7]]) == [0, 1, 2]
    assert candidate(workers = [[50, 50], [200, 200], [150, 150], [100, 100]],bikes = [[100, 50], [200, 100], [50, 200], [150, 150]]) == [0, 1, 3, 2]
    assert candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [0, 4, 8]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [0, 2, 4]
    assert candidate(workers = [[10, 0], [20, 0], [30, 0]],bikes = [[5, 0], [15, 0], [25, 0], [35, 0]]) == [0, 1, 2]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[2, 2], [1, 1], [3, 3], [4, 4], [5, 5]]) == [1, 0, 2]
    assert candidate(workers = [[1, 1], [1, 3], [2, 2]],bikes = [[2, 1], [3, 3], [4, 4], [5, 5]]) == [0, 1, 2]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[6, 5], [4, 3], [2, 1], [7, 8]]) == [2, 1, 0]
    assert candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [4, 3, 2]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == [4, 3, 2, 1, 0]
    assert candidate(workers = [[0, 0], [2, 2], [4, 4]],bikes = [[1, 1], [3, 3], [5, 5], [6, 6], [7, 7]]) == [0, 1, 2]
    assert candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996]],bikes = [[1000, 1000], [999, 999], [998, 998], [997, 997], [996, 996], [995, 995]]) == [1, 2, 3, 4]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [0, 1, 2, 3]
    assert candidate(workers = [[999, 999], [0, 0], [500, 500]],bikes = [[500, 499], [501, 500], [499, 500], [0, 1], [1, 0], [998, 998]]) == [5, 3, 0]
    assert candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0]],bikes = [[0, 1], [1, 1], [2, 1], [3, 1]]) == [0, 1, 2, 3]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45]]) == [0, 1, 2]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[6, 5], [4, 3], [2, 1], [0, 0], [8, 8]]) == [2, 1, 0]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == [3, 2, 1, 0]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[1, 1], [1, 3], [3, 1], [3, 3]],bikes = [[0, 0], [0, 2], [2, 0], [2, 2], [4, 4]]) == [0, 1, 2, 3]
    assert candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[200, 100], [100, 200], [300, 200]]) == [0, 1, 2]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[0, 0], [0, 0], [0, 0], [0, 0]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 1], [2, 2], [3, 3], [4, 4]]) == [0, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1]]) == [3, 2, 1, 0]
    assert candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2], [2, 3]]) == [3, 0, 2, 1]
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [100, 100], [200, 200], [300, 300]]) == [4, 5, 6, 2]
    assert candidate(workers = [[0, 0], [100, 0], [200, 0], [300, 0]],bikes = [[0, 0], [0, 100], [0, 200], [0, 300], [0, 400], [0, 500]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [1000, 1000]],bikes = [[500, 500], [250, 250], [750, 750]]) == [1, 2]
    assert candidate(workers = [[0, 0], [0, 2], [0, 4], [0, 6]],bikes = [[1, 1], [1, 3], [1, 5], [1, 7]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [1000, 1000], [500, 500]],bikes = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [0, 1000], [1000, 0], [1000, 1000]],bikes = [[500, 500], [0, 500], [500, 0], [500, 1000], [1000, 500]]) == [1, 3, 2, 4]
    assert candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [6, 6], [9, 9], [11, 11], [12, 12]]) == [0, 1, 2]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [1, 2, 3, 4, 5, 6, 0]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == [5, 7, 9, 11]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3]]) == [1, 2, 3, 0]
    assert candidate(workers = [[10, 0], [0, 10], [10, 10], [0, 0]],bikes = [[10, 10], [10, 0], [0, 10], [0, 0], [5, 5], [1, 1], [9, 9], [8, 8]]) == [1, 2, 0, 3]
    assert candidate(workers = [[999, 999], [998, 998], [997, 997]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == [8, 9, 10]
    assert candidate(workers = [[500, 500], [400, 400], [300, 300]],bikes = [[200, 200], [100, 100], [0, 0], [900, 900], [800, 800], [700, 700]]) == [5, 1, 0]
    assert candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[1, 2], [2, 1], [2, 2], [1, 1], [0, 2], [0, 0]]) == [5, 4, 0, 3]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[3, 3], [2, 2], [1, 1], [0, 0]]) == [3, 2, 1, 0]
    assert candidate(workers = [[0, 0], [1, 4], [5, 0], [2, 3]],bikes = [[2, 5], [1, 1], [3, 0], [3, 4], [6, 2]]) == [1, 0, 2, 3]
    assert candidate(workers = [[1, 1], [1, 2], [2, 1], [2, 2]],bikes = [[1, 3], [3, 1], [3, 3], [2, 2], [1, 1], [2, 1], [1, 2]]) == [4, 6, 5, 3]
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == [0, 1, 2, 3]
    assert candidate(workers = [[50, 50], [100, 100], [150, 150]],bikes = [[100, 100], [50, 50], [150, 150], [200, 200], [250, 250]]) == [1, 0, 2]
    assert candidate(workers = [[500, 500], [501, 501], [499, 499], [502, 502]],bikes = [[500, 500], [501, 501], [499, 499], [502, 502], [503, 503]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 1], [1, 3], [3, 4], [3, 0], [2, 5]],bikes = [[0, 0], [0, 3], [0, 4], [1, 1], [1, 2], [2, 2], [3, 3], [4, 2]]) == [3, 1, 6, 0, 2]
    assert candidate(workers = [[0, 1], [1, 0], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 1], [3, 2]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],bikes = [[2, 1], [4, 3], [6, 5], [8, 7], [10, 9], [0, 0]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501], [601, 601]]) == [0, 1, 2]
    assert candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401]]) == [0, 1, 2]
    assert candidate(workers = [[5, 5], [6, 6], [7, 7]],bikes = [[5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 0], [2, 1], [3, 2]]) == [0, 1, 2, 3]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750]],bikes = [[0, 0], [1000, 1000], [500, 500], [250, 250], [750, 750], [375, 375], [625, 625], [500, 250]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == [4, 3, 2, 1, 0]
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[105, 105], [205, 205], [305, 305], [405, 405], [505, 505], [605, 605]]) == [0, 1, 2, 3]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == [0, 1, 2]
    assert candidate(workers = [[200, 200], [200, 250], [200, 300], [200, 350], [200, 400]],bikes = [[250, 250], [250, 300], [250, 350], [250, 400], [250, 450]]) == [4, 0, 1, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]]) == [0, 1, 2]
    assert candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[0, 0], [5, 5], [10, 10], [15, 15], [20, 20]]) == [1, 2, 3]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 2], [3, 4], [5, 6]],bikes = [[2, 1], [4, 3], [6, 5], [7, 8], [8, 7], [9, 6]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 1], [1, 0], [2, 1], [3, 2], [4, 3]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[1, 2], [2, 1], [3, 3]],bikes = [[2, 2], [3, 1], [1, 3], [2, 3]]) == [0, 1, 3]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 10], [20, 20], [30, 30], [40, 40]]) == [0, 1, 2]
    assert candidate(workers = [[5, 5], [10, 10], [15, 15], [20, 20]],bikes = [[10, 5], [15, 10], [20, 15], [25, 20], [30, 25]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[0, 0], [1, 0], [2, 0], [3, 0]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [0, 1, 2, 3]
    assert candidate(workers = [[0, 0], [5, 5], [10, 10]],bikes = [[1, 1], [6, 6], [11, 11]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [1, 2, 3, 4, 5, 0]
    assert candidate(workers = [[0, 0], [10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]) == [4, 3, 2, 1, 0]
    assert candidate(workers = [[1, 100], [1, 200], [1, 300]],bikes = [[2, 200], [2, 300], [2, 400], [2, 500], [2, 600]]) == [2, 0, 1]
    assert candidate(workers = [[10, 10], [11, 11], [12, 12], [13, 13]],bikes = [[10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == [0, 1, 2, 3]
    assert candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[1, 2], [2, 3], [3, 4], [4, 5]]) == [0, 1, 2]
    assert candidate(workers = [[0, 0], [0, 0], [0, 0]],bikes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == [0, 1, 2]
    assert candidate(workers = [[50, 50], [51, 51], [52, 52], [53, 53], [54, 54]],bikes = [[50, 51], [51, 52], [52, 53], [53, 54], [54, 55], [55, 56], [56, 57]]) == [0, 1, 2, 3, 4]
    assert candidate(workers = [[5, 5], [6, 6], [7, 7], [8, 8]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == [5, 6, 7, 8]


