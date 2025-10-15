def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],threshold = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],threshold = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]],threshold = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]],threshold = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],threshold = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],threshold = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],threshold = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],threshold = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],threshold = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],threshold = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 200, 300], [200, 300, 400], [300, 400, 500]],threshold = 600) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 200, 300], [200, 300, 400], [300, 400, 500]],threshold = 600) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],threshold = 2500) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],threshold = 2500) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]],threshold = 2500) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]],threshold = 2500) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [20, 18, 16, 14, 12, 10, 8, 6, 4, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [20, 18, 16, 14, 12, 10, 8, 6, 4, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9]],threshold = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9]],threshold = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5]],threshold = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5]],threshold = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8], [8, 6, 4, 2, 0, 1, 3, 5, 7], [2, 4, 6, 8, 0, 9, 7, 5, 3]],threshold = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8], [8, 6, 4, 2, 0, 1, 3, 5, 7], [2, 4, 6, 8, 0, 9, 7, 5, 3]],threshold = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]],threshold = 250) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]],threshold = 250) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],threshold = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],threshold = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]],threshold = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]],threshold = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100]],threshold = 500) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100]],threshold = 500) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]],threshold = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]],threshold = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]],threshold = 40) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]],threshold = 40) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[2, 3, 5], [3, 8, 13], [5, 13, 21]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[2, 3, 5], [3, 8, 13], [5, 13, 21]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 100, 100], [100, 100, 100], [100, 100, 100], [100, 100, 100]],threshold = 250) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 100, 100], [100, 100, 100], [100, 100, 100], [100, 100, 100]],threshold = 250) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 4, 3, 3, 2, 1], [1, 2, 3, 4, 5, 4, 3, 2, 2, 1], [1, 2, 3, 4, 5, 4, 3, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 4, 3, 3, 2, 1], [1, 2, 3, 4, 5, 4, 3, 2, 2, 1], [1, 2, 3, 4, 5, 4, 3, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],threshold = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],threshold = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]],threshold = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]],threshold = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],threshold = 18) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],threshold = 18) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 11, 12], [13, 14, 15], [16, 17, 18]],threshold = 39) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 11, 12], [13, 14, 15], [16, 17, 18]],threshold = 39) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],threshold = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],threshold = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],threshold = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],threshold = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],threshold = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],threshold = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]],threshold = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]],threshold = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],threshold = 40) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],threshold = 40) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],threshold = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],threshold = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9]],threshold = 81) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9]],threshold = 81) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],threshold = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],threshold = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]],threshold = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]],threshold = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],threshold = 14) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],threshold = 14) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 1, 5, 6, 2], [2, 4, 6, 8, 7, 3], [5, 7, 8, 9, 10, 1], [6, 8, 9, 10, 11, 2], [7, 9, 10, 11, 12, 3]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 1, 5, 6, 2], [2, 4, 6, 8, 7, 3], [5, 7, 8, 9, 10, 1], [6, 8, 9, 10, 11, 2], [7, 9, 10, 11, 12, 3]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],threshold = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],threshold = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],threshold = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],threshold = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],threshold = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],threshold = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 2, 2, 2, 2, 2, 2, 1, 0], [0, 1, 2, 3, 3, 3, 3, 2, 1, 0], [0, 1, 2, 3, 4, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 4, 3, 2, 0], [0, 1, 2, 3, 4, 4, 3, 2, 1, 0], [0, 1, 2, 3, 3, 3, 3, 2, 1, 0], [0, 1, 2, 2, 2, 2, 2, 2, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 2, 2, 2, 2, 2, 2, 1, 0], [0, 1, 2, 3, 3, 3, 3, 2, 1, 0], [0, 1, 2, 3, 4, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 4, 3, 2, 0], [0, 1, 2, 3, 4, 4, 3, 2, 1, 0], [0, 1, 2, 3, 3, 3, 3, 2, 1, 0], [0, 1, 2, 2, 2, 2, 2, 2, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 9, 6, 8, 7], [4, 6, 4, 4, 3], [8, 5, 3, 3, 1], [7, 8, 4, 6, 2], [1, 1, 2, 7, 3]],threshold = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 9, 6, 8, 7], [4, 6, 4, 4, 3], [8, 5, 3, 3, 1], [7, 8, 4, 6, 2], [1, 1, 2, 7, 3]],threshold = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]],threshold = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]],threshold = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],threshold = 16) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],threshold = 16) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 5, 6, 7, 8], [8, 7, 6, 5, 9], [7, 6, 5, 4, 8], [6, 5, 4, 3, 7], [5, 4, 3, 2, 6]],threshold = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 5, 6, 7, 8], [8, 7, 6, 5, 9], [7, 6, 5, 4, 8], [6, 5, 4, 3, 7], [5, 4, 3, 2, 6]],threshold = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]],threshold = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]],threshold = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],threshold = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],threshold = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [6, 16, 26, 36, 46], [12, 22, 32, 42, 52]],threshold = 150) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [6, 16, 26, 36, 46], [12, 22, 32, 42, 52]],threshold = 150) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1]],threshold = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1]],threshold = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7, 8, 9, 10, 11], [4, 5, 6, 7, 8, 9, 10, 11, 12], [5, 6, 7, 8, 9, 10, 11, 12, 13], [6, 7, 8, 9, 10, 11, 12, 13, 14]],threshold = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7, 8, 9, 10, 11], [4, 5, 6, 7, 8, 9, 10, 11, 12], [5, 6, 7, 8, 9, 10, 11, 12, 13], [6, 7, 8, 9, 10, 11, 12, 13, 14]],threshold = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17], [17, 15, 13, 11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17], [17, 15, 13, 11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],threshold = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17], [17, 15, 13, 11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17], [17, 15, 13, 11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],threshold = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 1, 2], [1, 9, 1], [2, 1, 9]],threshold = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 1, 2], [1, 9, 1], [2, 1, 9]],threshold = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 150) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 150) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 8, 7, 6], [8, 7, 6, 5], [7, 6, 5, 4], [6, 5, 4, 3]],threshold = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 8, 7, 6], [8, 7, 6, 5], [7, 6, 5, 4], [6, 5, 4, 3]],threshold = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],threshold = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],threshold = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],threshold = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],threshold = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],threshold = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],threshold = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]],threshold = 81) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]],threshold = 81) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],threshold = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],threshold = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]],threshold = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]],threshold = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]],threshold = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]],threshold = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], [160, 170, 180, 190, 200], [210, 220, 230, 240, 250]],threshold = 500) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], [160, 170, 180, 190, 200], [210, 220, 230, 240, 250]],threshold = 500) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],threshold = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],threshold = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],threshold = 10) == 3
    assert candidate(mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]],threshold = 4) == 2
    assert candidate(mat = [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],threshold = 1) == 0
    assert candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],threshold = 100) == 1
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],threshold = 15) == 2
    assert candidate(mat = [[100, 200, 300], [200, 300, 400], [300, 400, 500]],threshold = 600) == 1
    assert candidate(mat = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],threshold = 2500) == 2
    assert candidate(mat = [[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]],threshold = 2500) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [20, 18, 16, 14, 12, 10, 8, 6, 4, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 50) == 3
    assert candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]],threshold = 20) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 30) == 3
    assert candidate(mat = [[5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 2, 4, 1, 3, 6, 8, 7, 9]],threshold = 30) == 3
    assert candidate(mat = [[5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 30], [30, 25, 20, 15, 10, 5]],threshold = 100) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8], [8, 6, 4, 2, 0, 1, 3, 5, 7], [2, 4, 6, 8, 0, 9, 7, 5, 3]],threshold = 30) == 3
    assert candidate(mat = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]],threshold = 250) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],threshold = 20) == 2
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 20) == 2
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],threshold = 30) == 2
    assert candidate(mat = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]],threshold = 10) == 1
    assert candidate(mat = [[100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100]],threshold = 500) == 2
    assert candidate(mat = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]],threshold = 2) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]],threshold = 40) == 3
    assert candidate(mat = [[2, 3, 5], [3, 8, 13], [5, 13, 21]],threshold = 20) == 2
    assert candidate(mat = [[100, 100, 100], [100, 100, 100], [100, 100, 100], [100, 100, 100]],threshold = 250) == 1
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 4, 4, 3, 2, 1], [1, 2, 3, 4, 5, 4, 3, 3, 2, 1], [1, 2, 3, 4, 5, 4, 3, 2, 2, 1], [1, 2, 3, 4, 5, 4, 3, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],threshold = 30) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 25) == 5
    assert candidate(mat = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]],threshold = 50) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],threshold = 18) == 2
    assert candidate(mat = [[10, 11, 12], [13, 14, 15], [16, 17, 18]],threshold = 39) == 1
    assert candidate(mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],threshold = 1) == 5
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],threshold = 100) == 3
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],threshold = 100) == 2
    assert candidate(mat = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1]],threshold = 1) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 20) == 2
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 20) == 4
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],threshold = 40) == 2
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 20) == 2
    assert candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],threshold = 10) == 3
    assert candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 5
    assert candidate(mat = [[9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9]],threshold = 81) == 3
    assert candidate(mat = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],threshold = 1000) == 1
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2
    assert candidate(mat = [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]],threshold = 50) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],threshold = 14) == 3
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],threshold = 100) == 4
    assert candidate(mat = [[1, 3, 1, 5, 6, 2], [2, 4, 6, 8, 7, 3], [5, 7, 8, 9, 10, 1], [6, 8, 9, 10, 11, 2], [7, 9, 10, 11, 12, 3]],threshold = 20) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],threshold = 10) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 20) == 4
    assert candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 15) == 2
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],threshold = 20) == 2
    assert candidate(mat = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],threshold = 1) == 5
    assert candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 2, 2, 2, 2, 2, 2, 1, 0], [0, 1, 2, 3, 3, 3, 3, 2, 1, 0], [0, 1, 2, 3, 4, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 4, 3, 2, 0], [0, 1, 2, 3, 4, 4, 3, 2, 1, 0], [0, 1, 2, 3, 3, 3, 3, 2, 1, 0], [0, 1, 2, 2, 2, 2, 2, 2, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 20) == 4
    assert candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 10) == 2
    assert candidate(mat = [[5, 9, 6, 8, 7], [4, 6, 4, 4, 3], [8, 5, 3, 3, 1], [7, 8, 4, 6, 2], [1, 1, 2, 7, 3]],threshold = 15) == 2
    assert candidate(mat = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]],threshold = 5) == 1
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]],threshold = 16) == 4
    assert candidate(mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]],threshold = 25) == 2
    assert candidate(mat = [[9, 5, 6, 7, 8], [8, 7, 6, 5, 9], [7, 6, 5, 4, 8], [6, 5, 4, 3, 7], [5, 4, 3, 2, 6]],threshold = 30) == 2
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]],threshold = 3) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],threshold = 50) == 3
    assert candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [6, 16, 26, 36, 46], [12, 22, 32, 42, 52]],threshold = 150) == 3
    assert candidate(mat = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1]],threshold = 2) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7, 8, 9, 10, 11], [4, 5, 6, 7, 8, 9, 10, 11, 12], [5, 6, 7, 8, 9, 10, 11, 12, 13], [6, 7, 8, 9, 10, 11, 12, 13, 14]],threshold = 100) == 4
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17], [17, 15, 13, 11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17], [17, 15, 13, 11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],threshold = 50) == 3
    assert candidate(mat = [[9, 1, 2], [1, 9, 1], [2, 1, 9]],threshold = 15) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 150) == 12
    assert candidate(mat = [[9, 8, 7, 6], [8, 7, 6, 5], [7, 6, 5, 4], [6, 5, 4, 3]],threshold = 30) == 2
    assert candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],threshold = 5) == 2
    assert candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],threshold = 5) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],threshold = 100) == 4
    assert candidate(mat = [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]],threshold = 81) == 3
    assert candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 10
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],threshold = 15) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]],threshold = 25) == 3
    assert candidate(mat = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]],threshold = 25) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 50) == 7
    assert candidate(mat = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], [160, 170, 180, 190, 200], [210, 220, 230, 240, 250]],threshold = 500) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],threshold = 3) == 1
    assert candidate(mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],threshold = 1) == 5
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5]],threshold = 25) == 2
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],threshold = 15) == 3


