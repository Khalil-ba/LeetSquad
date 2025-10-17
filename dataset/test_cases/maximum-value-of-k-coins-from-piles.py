def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(piles = [[30, 10], [50, 20, 10]],k = 3) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[30, 10], [50, 20, 10]],k = 3) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2], [3, 4], [5, 6]],k = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2], [3, 4], [5, 6]],k = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20], [5, 5, 5, 5], [1, 1, 1, 1, 1]],k = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20], [5, 5, 5, 5], [1, 1, 1, 1, 1]],k = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3], [4, 5, 6]],k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3], [4, 5, 6]],k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[30, 10, 20], [10, 20, 30], [5, 5, 5]],k = 5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[30, 10, 20], [10, 20, 30], [5, 5, 5]],k = 5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [2], [3], [4], [5]],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [2], [3], [4], [5]],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10]],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10]],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30], [30, 20, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 10) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30], [30, 20, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 10) == 124: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],k = 5) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],k = 5) == 33: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 100, 3], [7, 8, 9]],k = 2) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 100, 3], [7, 8, 9]],k = 2) == 101: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]],k = 7) == 706
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]],k = 7) == 706: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[3, 1, 5], [1, 2, 3], [4, 6]],k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[3, 1, 5], [1, 2, 3], [4, 6]],k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],k = 25) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],k = 25) == 55: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [10, 20, 30, 40, 50, 60]],k = 12) == 237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [10, 20, 30, 40, 50, 60]],k = 12) == 237: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10000, 20000, 30000, 40000, 50000], [10000, 20000, 30000, 40000, 50000], [10000, 20000, 30000, 40000, 50000]],k = 10) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10000, 20000, 30000, 40000, 50000], [10000, 20000, 30000, 40000, 50000], [10000, 20000, 30000, 40000, 50000]],k = 10) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 90, 80], [70, 60, 50, 40], [30, 20, 10]],k = 7) == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 90, 80], [70, 60, 50, 40], [30, 20, 10]],k = 7) == 490: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 100, 3, 50], [7, 8, 9, 100], [1, 2, 3, 4, 5]],k = 7) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 100, 3, 50], [7, 8, 9, 100], [1, 2, 3, 4, 5]],k = 7) == 228: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]],k = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]],k = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[5, 1, 2, 3], [4, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],k = 8) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[5, 1, 2, 3], [4, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],k = 8) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]],k = 8) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]],k = 8) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],k = 50) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],k = 50) == 400: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 900, 800], [700, 600, 500], [400, 300, 200], [100, 90, 80], [70, 60, 50], [40, 30, 20], [10, 9, 8], [7, 6, 5]],k = 20) == 5959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 900, 800], [700, 600, 500], [400, 300, 200], [100, 90, 80], [70, 60, 50], [40, 30, 20], [10, 9, 8], [7, 6, 5]],k = 20) == 5959: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 2000, 3000], [1000, 1000, 1000, 1000], [500, 500, 500, 500, 500, 500], [200, 200, 200]],k = 10) == 11500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 2000, 3000], [1000, 1000, 1000, 1000], [500, 500, 500, 500, 500, 500], [200, 200, 200]],k = 10) == 11500: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]],k = 30) == 1105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]],k = 30) == 1105: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],k = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],k = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],k = 10) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],k = 10) == 35: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20], [30, 40, 50, 60], [70, 80, 90], [100]],k = 7) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20], [30, 40, 50, 60], [70, 80, 90], [100]],k = 7) == 460: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 15, 20], [25, 30, 35], [40, 45, 50], [5, 10, 15], [1, 2, 3]],k = 12) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 15, 20], [25, 30, 35], [40, 45, 50], [5, 10, 15], [1, 2, 3]],k = 12) == 300: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]],k = 15) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]],k = 15) == 195: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[99999, 99998, 99997, 99996, 99995], [99994, 99993, 99992, 99991, 99990], [99989, 99988, 99987, 99986, 99985], [99984, 99983, 99982, 99981, 99980]],k = 15) == 1499880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[99999, 99998, 99997, 99996, 99995], [99994, 99993, 99992, 99991, 99990], [99989, 99988, 99987, 99986, 99985], [99984, 99983, 99982, 99981, 99980]],k = 15) == 1499880: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]],k = 8) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]],k = 8) == 81: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30], [5, 15, 25], [1, 2, 3], [9, 18, 27]],k = 8) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30], [5, 15, 25], [1, 2, 3], [9, 18, 27]],k = 8) == 134: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 500, 250, 125, 62, 31, 15, 7, 3, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]],k = 20) == 3017
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 500, 250, 125, 62, 31, 15, 7, 3, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]],k = 20) == 3017: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 90, 80, 70, 60], [50, 40, 30, 20, 10], [1, 2, 3, 4, 5]],k = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 90, 80, 70, 60], [50, 40, 30, 20, 10], [1, 2, 3, 4, 5]],k = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30], [40, 50, 60, 70], [80, 90]],k = 8) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30], [40, 50, 60, 70], [80, 90]],k = 8) == 420: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100000], [100000], [100000], [100000], [100000], [100000], [100000]],k = 7) == 700000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100000], [100000], [100000], [100000], [100000], [100000], [100000]],k = 7) == 700000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50], [20, 30, 40, 50, 60], [30, 40, 50, 60, 70]],k = 6) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50], [20, 30, 40, 50, 60], [30, 40, 50, 60, 70]],k = 6) == 270: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2]],k = 15) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2]],k = 15) == 59: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10]],k = 15) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10]],k = 15) == 150: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000]],k = 5) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000]],k = 5) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500], [1000, 2000, 3000, 4000, 5000]],k = 10) == 16500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500], [1000, 2000, 3000, 4000, 5000]],k = 10) == 16500: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]],k = 15) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]],k = 15) == 105: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 10, 30, 50], [10, 20, 30, 40], [5, 15, 25, 35]],k = 10) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 10, 30, 50], [10, 20, 30, 40], [5, 15, 25, 35]],k = 10) == 211: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1000]],k = 10) == 1009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1000]],k = 10) == 1009: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30], [1, 2, 3, 4, 5], [100, 200], [50, 60, 70]],k = 7) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30], [1, 2, 3, 4, 5], [100, 200], [50, 60, 70]],k = 7) == 510: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6]],k = 15) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6]],k = 15) == 95: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 900, 800], [700, 600], [500, 400, 300, 200, 100]],k = 12) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 900, 800], [700, 600], [500, 400, 300, 200, 100]],k = 12) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 100, 100], [100, 100, 100], [100, 100, 100], [100, 100, 100]],k = 8) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 100, 100], [100, 100, 100], [100, 100, 100], [100, 100, 100]],k = 8) == 800: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]],k = 15) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]],k = 15) == 140: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]],k = 15) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]],k = 15) == 70: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 2000, 3000], [1500, 2500, 3500], [1200, 2200, 3200]],k = 5) == 10900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 2000, 3000], [1500, 2500, 3500], [1200, 2200, 3200]],k = 5) == 10900: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40], [5, 15, 25], [100], [50, 75]],k = 6) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40], [5, 15, 25], [100], [50, 75]],k = 6) == 285: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1000, 2000], [3000, 4000, 5000], [6000, 7000, 8000], [9000, 10000, 11000]],k = 6) == 51000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1000, 2000], [3000, 4000, 5000], [6000, 7000, 8000], [9000, 10000, 11000]],k = 6) == 51000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]],k = 25) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]],k = 25) == 135: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]],k = 20) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]],k = 20) == 40: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30], [15, 25, 35, 45], [5, 10, 15, 20, 25]],k = 10) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30], [15, 25, 35, 45], [5, 10, 15, 20, 25]],k = 10) == 210: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 100, 3], [7, 8, 9], [4, 5, 6], [10, 20, 30], [1000, 2000, 3000]],k = 12) == 6189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 100, 3], [7, 8, 9], [4, 5, 6], [10, 20, 30], [1000, 2000, 3000]],k = 12) == 6189: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 10) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 10) == 155: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 15) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 15) == 320: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],k = 20) == 605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],k = 20) == 605: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40], [50, 60, 70], [80, 90, 100, 110, 120], [130, 140]],k = 10) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40], [50, 60, 70], [80, 90, 100, 110, 120], [130, 140]],k = 10) == 950: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]],k = 5) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]],k = 5) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[50], [20], [10], [5]],k = 3) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[50], [20], [10], [5]],k = 3) == 80: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[9, 7, 5, 3, 1], [8, 6, 4, 2], [10, 20, 30], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 15) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[9, 7, 5, 3, 1], [8, 6, 4, 2], [10, 20, 30], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 15) == 108: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2]],k = 15) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2]],k = 15) == 78: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [2, 12, 22, 32, 42]],k = 10) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [2, 12, 22, 32, 42]],k = 10) == 275: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 2000], [100, 200, 300, 400, 500], [50]],k = 8) == 4550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 2000], [100, 200, 300, 400, 500], [50]],k = 8) == 4550: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[5, 10, 15], [20, 25, 30, 35, 40], [1, 1, 1, 1, 1, 1, 1], [99, 98, 97, 96]],k = 10) == 545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[5, 10, 15], [20, 25, 30, 35, 40], [1, 1, 1, 1, 1, 1, 1], [99, 98, 97, 96]],k = 10) == 545: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1000]],k = 20) == 1038
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1000]],k = 20) == 1038: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50], [5, 10, 15, 20, 25], [1, 2, 3, 4, 5], [100, 200, 300, 400, 500]],k = 10) == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50], [5, 10, 15, 20, 25], [1, 2, 3, 4, 5], [100, 200, 300, 400, 500]],k = 10) == 1650: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1000, 2000, 3000], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [500, 600, 700, 800, 900], [10, 20, 30, 40, 50]],k = 15) == 9653
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1000, 2000, 3000], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [500, 600, 700, 800, 900], [10, 20, 30, 40, 50]],k = 15) == 9653: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],k = 12) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],k = 12) == 147: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],k = 10) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],k = 10) == 300: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],k = 14) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],k = 14) == 105: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [15, 14, 13, 12, 11]],k = 15) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [15, 14, 13, 12, 11]],k = 15) == 120: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 200, 300], [400, 500, 600], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],k = 15) == 2145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 200, 300], [400, 500, 600], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],k = 15) == 2145: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 200, 300], [50, 60, 70, 80], [10, 20, 30, 40, 50]],k = 15) == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 200, 300], [50, 60, 70, 80], [10, 20, 30, 40, 50]],k = 15) == 1010: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],k = 18) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],k = 18) == 90: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[5, 1, 2], [3, 10, 1], [4, 4, 4], [2, 8, 6]],k = 6) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[5, 1, 2], [3, 10, 1], [4, 4, 4], [2, 8, 6]],k = 6) == 34: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 100, 3], [7, 8, 9], [5, 6, 7], [4, 5, 6]],k = 10) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 100, 3], [7, 8, 9], [5, 6, 7], [4, 5, 6]],k = 10) == 152: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 1, 1, 1, 1], [2, 2, 2], [3, 3], [4], [5, 5, 5, 5]],k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 1, 1, 1, 1], [2, 2, 2], [3, 3], [4], [5, 5, 5, 5]],k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13], [6, 8, 10, 12, 14], [7, 9, 11, 13, 15], [8, 10, 12, 14, 16], [9, 11, 13, 15, 17], [10, 12, 14, 16, 18]],k = 25) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13], [6, 8, 10, 12, 14], [7, 9, 11, 13, 15], [8, 10, 12, 14, 16], [9, 11, 13, 15, 17], [10, 12, 14, 16, 18]],k = 25) == 300: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 15) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 15) == 95: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],k = 15) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],k = 15) == 120: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[10, 20, 30], [5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 8) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[10, 20, 30], [5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 8) == 81: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],k = 8) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],k = 8) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[100, 200], [50, 150, 250], [200, 300, 400, 500], [300, 400, 500, 600, 700]],k = 15) == 4650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[100, 200], [50, 150, 250], [200, 300, 400, 500], [300, 400, 500, 600, 700]],k = 15) == 4650: {e}')
    
    total += 1
    try:
        result = candidate(piles = [[1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23]],k = 12) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [[1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23]],k = 12) == 201: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(piles = [[30, 10], [50, 20, 10]],k = 3) == 100
    assert candidate(piles = [[1, 2], [3, 4], [5, 6]],k = 5) == 19
    assert candidate(piles = [[10, 20], [5, 5, 5, 5], [1, 1, 1, 1, 1]],k = 5) == 45
    assert candidate(piles = [[1, 2, 3], [4, 5, 6]],k = 3) == 15
    assert candidate(piles = [[30, 10, 20], [10, 20, 30], [5, 5, 5]],k = 5) == 100
    assert candidate(piles = [[1], [2], [3], [4], [5]],k = 3) == 12
    assert candidate(piles = [[10]],k = 1) == 10
    assert candidate(piles = [[10, 20, 30], [30, 20, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 10) == 124
    assert candidate(piles = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],k = 5) == 33
    assert candidate(piles = [[1, 100, 3], [7, 8, 9]],k = 2) == 101
    assert candidate(piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]],k = 7) == 706
    assert candidate(piles = [[3, 1, 5], [1, 2, 3], [4, 6]],k = 3) == 13
    assert candidate(piles = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],k = 4) == 16
    assert candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],k = 10) == 55
    assert candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],k = 25) == 55
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 10) == 55
    assert candidate(piles = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [10, 20, 30, 40, 50, 60]],k = 12) == 237
    assert candidate(piles = [[10000, 20000, 30000, 40000, 50000], [10000, 20000, 30000, 40000, 50000], [10000, 20000, 30000, 40000, 50000]],k = 10) == 300000
    assert candidate(piles = [[100, 90, 80], [70, 60, 50, 40], [30, 20, 10]],k = 7) == 490
    assert candidate(piles = [[1, 100, 3, 50], [7, 8, 9, 100], [1, 2, 3, 4, 5]],k = 7) == 228
    assert candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]],k = 10) == 550
    assert candidate(piles = [[5, 1, 2, 3], [4, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],k = 8) == 100
    assert candidate(piles = [[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]],k = 8) == 10000
    assert candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]],k = 50) == 400
    assert candidate(piles = [[1000, 900, 800], [700, 600, 500], [400, 300, 200], [100, 90, 80], [70, 60, 50], [40, 30, 20], [10, 9, 8], [7, 6, 5]],k = 20) == 5959
    assert candidate(piles = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],k = 10) == 10
    assert candidate(piles = [[1000, 2000, 3000], [1000, 1000, 1000, 1000], [500, 500, 500, 500, 500, 500], [200, 200, 200]],k = 10) == 11500
    assert candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]],k = 30) == 1105
    assert candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],k = 15) == 40
    assert candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 20) == 210
    assert candidate(piles = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],k = 10) == 35
    assert candidate(piles = [[10, 20], [30, 40, 50, 60], [70, 80, 90], [100]],k = 7) == 460
    assert candidate(piles = [[10, 15, 20], [25, 30, 35], [40, 45, 50], [5, 10, 15], [1, 2, 3]],k = 12) == 300
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]],k = 15) == 195
    assert candidate(piles = [[99999, 99998, 99997, 99996, 99995], [99994, 99993, 99992, 99991, 99990], [99989, 99988, 99987, 99986, 99985], [99984, 99983, 99982, 99981, 99980]],k = 15) == 1499880
    assert candidate(piles = [[1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]],k = 8) == 81
    assert candidate(piles = [[10, 20, 30], [5, 15, 25], [1, 2, 3], [9, 18, 27]],k = 8) == 134
    assert candidate(piles = [[1000, 500, 250, 125, 62, 31, 15, 7, 3, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]],k = 20) == 3017
    assert candidate(piles = [[100, 90, 80, 70, 60], [50, 40, 30, 20, 10], [1, 2, 3, 4, 5]],k = 10) == 550
    assert candidate(piles = [[10, 20, 30], [40, 50, 60, 70], [80, 90]],k = 8) == 420
    assert candidate(piles = [[100000], [100000], [100000], [100000], [100000], [100000], [100000]],k = 7) == 700000
    assert candidate(piles = [[10, 20, 30, 40, 50], [20, 30, 40, 50, 60], [30, 40, 50, 60, 70]],k = 6) == 270
    assert candidate(piles = [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2]],k = 15) == 59
    assert candidate(piles = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10]],k = 15) == 150
    assert candidate(piles = [[100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000], [100000]],k = 5) == 500000
    assert candidate(piles = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 300, 400, 500], [1000, 2000, 3000, 4000, 5000]],k = 10) == 16500
    assert candidate(piles = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]],k = 15) == 105
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 10) == 55
    assert candidate(piles = [[1, 10, 30, 50], [10, 20, 30, 40], [5, 15, 25, 35]],k = 10) == 211
    assert candidate(piles = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1000]],k = 10) == 1009
    assert candidate(piles = [[10, 20, 30], [1, 2, 3, 4, 5], [100, 200], [50, 60, 70]],k = 7) == 510
    assert candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6]],k = 15) == 95
    assert candidate(piles = [[1000, 900, 800], [700, 600], [500, 400, 300, 200, 100]],k = 12) == 5500
    assert candidate(piles = [[1], [1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 20) == 20
    assert candidate(piles = [[100, 100, 100], [100, 100, 100], [100, 100, 100], [100, 100, 100]],k = 8) == 800
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]],k = 15) == 140
    assert candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1]],k = 15) == 70
    assert candidate(piles = [[1000, 2000, 3000], [1500, 2500, 3500], [1200, 2200, 3200]],k = 5) == 10900
    assert candidate(piles = [[10, 20, 30, 40], [5, 15, 25], [100], [50, 75]],k = 6) == 285
    assert candidate(piles = [[1, 1000, 2000], [3000, 4000, 5000], [6000, 7000, 8000], [9000, 10000, 11000]],k = 6) == 51000
    assert candidate(piles = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]],k = 25) == 135
    assert candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]],k = 20) == 40
    assert candidate(piles = [[10, 20, 30], [15, 25, 35, 45], [5, 10, 15, 20, 25]],k = 10) == 210
    assert candidate(piles = [[1, 100, 3], [7, 8, 9], [4, 5, 6], [10, 20, 30], [1000, 2000, 3000]],k = 12) == 6189
    assert candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 10) == 155
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 15) == 320
    assert candidate(piles = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],k = 20) == 605
    assert candidate(piles = [[10, 20, 30, 40], [50, 60, 70], [80, 90, 100, 110, 120], [130, 140]],k = 10) == 950
    assert candidate(piles = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]],k = 5) == 4000
    assert candidate(piles = [[50], [20], [10], [5]],k = 3) == 80
    assert candidate(piles = [[9, 7, 5, 3, 1], [8, 6, 4, 2], [10, 20, 30], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 15) == 108
    assert candidate(piles = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 4, 6, 8, 10], [10, 8, 6, 4, 2]],k = 15) == 78
    assert candidate(piles = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [2, 12, 22, 32, 42]],k = 10) == 275
    assert candidate(piles = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]],k = 20) == 210
    assert candidate(piles = [[1000, 2000], [100, 200, 300, 400, 500], [50]],k = 8) == 4550
    assert candidate(piles = [[5, 10, 15], [20, 25, 30, 35, 40], [1, 1, 1, 1, 1, 1, 1], [99, 98, 97, 96]],k = 10) == 545
    assert candidate(piles = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1000]],k = 20) == 1038
    assert candidate(piles = [[10, 20, 30, 40, 50], [5, 10, 15, 20, 25], [1, 2, 3, 4, 5], [100, 200, 300, 400, 500]],k = 10) == 1650
    assert candidate(piles = [[1000, 2000, 3000], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [500, 600, 700, 800, 900], [10, 20, 30, 40, 50]],k = 15) == 9653
    assert candidate(piles = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],k = 12) == 147
    assert candidate(piles = [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],k = 10) == 300
    assert candidate(piles = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],k = 14) == 105
    assert candidate(piles = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [15, 14, 13, 12, 11]],k = 15) == 120
    assert candidate(piles = [[100, 200, 300], [400, 500, 600], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],k = 15) == 2145
    assert candidate(piles = [[100, 200, 300], [50, 60, 70, 80], [10, 20, 30, 40, 50]],k = 15) == 1010
    assert candidate(piles = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],k = 18) == 90
    assert candidate(piles = [[5, 1, 2], [3, 10, 1], [4, 4, 4], [2, 8, 6]],k = 6) == 34
    assert candidate(piles = [[1, 100, 3], [7, 8, 9], [5, 6, 7], [4, 5, 6]],k = 10) == 152
    assert candidate(piles = [[1, 1, 1, 1, 1], [2, 2, 2], [3, 3], [4], [5, 5, 5, 5]],k = 10) == 36
    assert candidate(piles = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13], [6, 8, 10, 12, 14], [7, 9, 11, 13, 15], [8, 10, 12, 14, 16], [9, 11, 13, 15, 17], [10, 12, 14, 16, 18]],k = 25) == 300
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 15) == 95
    assert candidate(piles = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],k = 15) == 120
    assert candidate(piles = [[10, 20, 30], [5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 8) == 81
    assert candidate(piles = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],k = 8) == 100
    assert candidate(piles = [[100, 200], [50, 150, 250], [200, 300, 400, 500], [300, 400, 500, 600, 700]],k = 15) == 4650
    assert candidate(piles = [[1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23]],k = 12) == 201


