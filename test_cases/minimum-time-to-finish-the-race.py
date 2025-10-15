def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4]],changeTime = 5,numLaps = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4]],changeTime = 5,numLaps = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2], [3, 3]],changeTime = 4,numLaps = 3) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2], [3, 3]],changeTime = 4,numLaps = 3) == 17: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 5], [3, 3]],changeTime = 10,numLaps = 6) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 5], [3, 3]],changeTime = 10,numLaps = 6) == 56: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100000, 2]],changeTime = 100000,numLaps = 1000) == 199900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100000, 2]],changeTime = 100000,numLaps = 1000) == 199900000: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2]],changeTime = 3,numLaps = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2]],changeTime = 3,numLaps = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 10], [5, 5], [2, 2]],changeTime = 5,numLaps = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 10], [5, 5], [2, 2]],changeTime = 5,numLaps = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 5], [20, 2]],changeTime = 7,numLaps = 8) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 5], [20, 2]],changeTime = 7,numLaps = 8) == 129: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2]],changeTime = 3,numLaps = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2]],changeTime = 3,numLaps = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 5], [10, 2]],changeTime = 7,numLaps = 3) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 5], [10, 2]],changeTime = 7,numLaps = 3) == 29: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 5], [2, 2]],changeTime = 1,numLaps = 10) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 5], [2, 2]],changeTime = 1,numLaps = 10) == 29: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2]],changeTime = 3,numLaps = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2]],changeTime = 3,numLaps = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10], [2, 2], [3, 4]],changeTime = 6,numLaps = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10], [2, 2], [3, 4]],changeTime = 6,numLaps = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2]],changeTime = 3,numLaps = 10) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2]],changeTime = 3,numLaps = 10) == 27: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],changeTime = 5,numLaps = 750) == 4495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],changeTime = 5,numLaps = 750) == 4495: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4], [5, 6], [7, 8]],changeTime = 5,numLaps = 15) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4], [5, 6], [7, 8]],changeTime = 5,numLaps = 15) == 93: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 100000], [2, 90000], [3, 80000], [4, 70000], [5, 60000], [6, 50000], [7, 40000], [8, 30000], [9, 20000], [10, 10000]],changeTime = 100000,numLaps = 1000) == 99900500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 100000], [2, 90000], [3, 80000], [4, 70000], [5, 60000], [6, 50000], [7, 40000], [8, 30000], [9, 20000], [10, 10000]],changeTime = 100000,numLaps = 1000) == 99900500: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 5], [2, 2], [3, 3]],changeTime = 6,numLaps = 20) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 5], [2, 2], [3, 3]],changeTime = 6,numLaps = 20) == 114: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],changeTime = 1,numLaps = 900) == 1799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],changeTime = 1,numLaps = 900) == 1799: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 5], [2, 3], [3, 2]],changeTime = 7,numLaps = 15) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 5], [2, 3], [3, 2]],changeTime = 7,numLaps = 15) == 92: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 1,numLaps = 50) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 1,numLaps = 50) == 99: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 3], [2, 8], [7, 2]],changeTime = 5,numLaps = 200) == 1395
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 3], [2, 8], [7, 2]],changeTime = 5,numLaps = 200) == 1395: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100, 100], [200, 200], [300, 300]],changeTime = 50,numLaps = 1000) == 149950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100, 100], [200, 200], [300, 300]],changeTime = 50,numLaps = 1000) == 149950: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],changeTime = 5,numLaps = 500) == 3495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],changeTime = 5,numLaps = 500) == 3495: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25]],changeTime = 20,numLaps = 500) == 12480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25]],changeTime = 20,numLaps = 500) == 12480: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],changeTime = 5,numLaps = 50) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],changeTime = 5,numLaps = 50) == 195: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],changeTime = 50,numLaps = 750) == 12100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],changeTime = 50,numLaps = 750) == 12100: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],changeTime = 10,numLaps = 999) == 8984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],changeTime = 10,numLaps = 999) == 8984: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [3, 4], [5, 6]],changeTime = 10,numLaps = 15) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [3, 4], [5, 6]],changeTime = 10,numLaps = 15) == 75: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4], [1, 5]],changeTime = 5,numLaps = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4], [1, 5]],changeTime = 5,numLaps = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 10,numLaps = 25) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 10,numLaps = 25) == 190: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]],changeTime = 7,numLaps = 50) == 318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]],changeTime = 7,numLaps = 50) == 318: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100, 2], [200, 3], [300, 4], [400, 5]],changeTime = 150,numLaps = 600) == 134850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100, 2], [200, 3], [300, 4], [400, 5]],changeTime = 150,numLaps = 600) == 134850: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 10,numLaps = 1000) == 7990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 10,numLaps = 1000) == 7990: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 1,numLaps = 1000) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 1,numLaps = 1000) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1000, 2], [500, 3], [250, 4]],changeTime = 500,numLaps = 100) == 74500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1000, 2], [500, 3], [250, 4]],changeTime = 500,numLaps = 100) == 74500: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 3], [7, 4], [2, 2]],changeTime = 10,numLaps = 20) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 3], [7, 4], [2, 2]],changeTime = 10,numLaps = 20) == 150: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6]],changeTime = 5,numLaps = 500) == 5495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6]],changeTime = 5,numLaps = 500) == 5495: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 1,numLaps = 100) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 1,numLaps = 100) == 199: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 100000,numLaps = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 100000,numLaps = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10000], [2, 5000], [3, 1000], [4, 500], [5, 250], [6, 125], [7, 62], [8, 31], [9, 15], [10, 7]],changeTime = 1000,numLaps = 1000) == 522400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10000], [2, 5000], [3, 1000], [4, 500], [5, 250], [6, 125], [7, 62], [8, 31], [9, 15], [10, 7]],changeTime = 1000,numLaps = 1000) == 522400: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10], [2, 5], [3, 3]],changeTime = 15,numLaps = 500) == 6485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10], [2, 5], [3, 3]],changeTime = 15,numLaps = 500) == 6485: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10], [2, 2], [3, 4], [4, 5]],changeTime = 5,numLaps = 30) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10], [2, 2], [3, 4], [4, 5]],changeTime = 5,numLaps = 30) == 160: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100, 100], [200, 50], [300, 25]],changeTime = 100,numLaps = 300) == 59900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100, 100], [200, 50], [300, 25]],changeTime = 100,numLaps = 300) == 59900: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 50,numLaps = 750) == 44950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 50,numLaps = 750) == 44950: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 2], [1, 2]],changeTime = 0,numLaps = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 2], [1, 2]],changeTime = 0,numLaps = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2]],changeTime = 10,numLaps = 500) == 3990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2]],changeTime = 10,numLaps = 500) == 3990: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 15,numLaps = 50) == 470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 15,numLaps = 50) == 470: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 5,numLaps = 15) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 5,numLaps = 15) == 55: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[3, 5], [2, 3], [4, 4]],changeTime = 10,numLaps = 15) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[3, 5], [2, 3], [4, 4]],changeTime = 10,numLaps = 15) == 128: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 10], [3, 3], [2, 2]],changeTime = 10,numLaps = 20) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 10], [3, 3], [2, 2]],changeTime = 10,numLaps = 20) == 150: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100000, 100000], [50000, 50000], [25000, 25000], [12500, 12500], [6250, 6250]],changeTime = 100000,numLaps = 1000) == 106150000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100000, 100000], [50000, 50000], [25000, 25000], [12500, 12500], [6250, 6250]],changeTime = 100000,numLaps = 1000) == 106150000: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100, 10], [50, 5], [25, 2]],changeTime = 20,numLaps = 1000) == 44980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100, 10], [50, 5], [25, 2]],changeTime = 20,numLaps = 1000) == 44980: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],changeTime = 3,numLaps = 40) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],changeTime = 3,numLaps = 40) == 197: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 100,numLaps = 50) == 5150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 100,numLaps = 50) == 5150: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 1,numLaps = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 1,numLaps = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10000, 2], [5000, 3], [1000, 4], [500, 5], [250, 6], [125, 7], [62, 8], [31, 9], [15, 10], [7, 11]],changeTime = 10000,numLaps = 1000) == 3639260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10000, 2], [5000, 3], [1000, 4], [500, 5], [250, 6], [125, 7], [62, 8], [31, 9], [15, 10], [7, 11]],changeTime = 10000,numLaps = 1000) == 3639260: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[3, 2], [4, 3], [5, 4], [6, 5], [7, 6]],changeTime = 15,numLaps = 30) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[3, 2], [4, 3], [5, 4], [6, 5], [7, 6]],changeTime = 15,numLaps = 30) == 345: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]],changeTime = 5,numLaps = 200) == 795
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]],changeTime = 5,numLaps = 200) == 795: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],changeTime = 10,numLaps = 1000) == 14990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],changeTime = 10,numLaps = 1000) == 14990: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4]],changeTime = 0,numLaps = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4]],changeTime = 0,numLaps = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 5,numLaps = 15) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 5,numLaps = 15) == 55: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2], [8, 3], [1, 2]],changeTime = 20,numLaps = 20) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2], [8, 3], [1, 2]],changeTime = 20,numLaps = 20) == 155: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2], [10, 2], [15, 2]],changeTime = 20,numLaps = 1000) == 17480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2], [10, 2], [15, 2]],changeTime = 20,numLaps = 1000) == 17480: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 5]],changeTime = 10,numLaps = 800) == 11990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 5]],changeTime = 10,numLaps = 800) == 11990: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [5, 7], [8, 9]],changeTime = 5,numLaps = 20) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [5, 7], [8, 9]],changeTime = 5,numLaps = 20) == 125: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 3], [10, 2], [2, 6]],changeTime = 7,numLaps = 15) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 3], [10, 2], [2, 6]],changeTime = 7,numLaps = 15) == 128: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2], [3, 3], [4, 4]],changeTime = 10,numLaps = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2], [3, 3], [4, 4]],changeTime = 10,numLaps = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],changeTime = 7,numLaps = 60) == 443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],changeTime = 7,numLaps = 60) == 443: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 5,numLaps = 30) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 5,numLaps = 30) == 115: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]],changeTime = 1,numLaps = 1000) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]],changeTime = 1,numLaps = 1000) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[50, 50], [25, 25], [10, 10], [5, 5], [2, 2]],changeTime = 25,numLaps = 750) == 9725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[50, 50], [25, 25], [10, 10], [5, 5], [2, 2]],changeTime = 25,numLaps = 750) == 9725: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100000, 2], [50000, 3]],changeTime = 50000,numLaps = 500) == 49950000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100000, 2], [50000, 3]],changeTime = 50000,numLaps = 500) == 49950000: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],changeTime = 5,numLaps = 50) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],changeTime = 5,numLaps = 50) == 195: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[3, 5], [5, 3], [7, 2]],changeTime = 15,numLaps = 200) == 3285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[3, 5], [5, 3], [7, 2]],changeTime = 15,numLaps = 200) == 3285: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],changeTime = 10,numLaps = 200) == 1125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],changeTime = 10,numLaps = 200) == 1125: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],changeTime = 20,numLaps = 800) == 11180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],changeTime = 20,numLaps = 800) == 11180: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],changeTime = 5,numLaps = 50) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],changeTime = 5,numLaps = 50) == 195: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 10], [5, 5], [1, 2]],changeTime = 5,numLaps = 30) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 10], [5, 5], [1, 2]],changeTime = 5,numLaps = 30) == 115: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 100000], [2, 50000], [3, 25000], [4, 10000], [5, 5000]],changeTime = 100000,numLaps = 1000) == 62402500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 100000], [2, 50000], [3, 25000], [4, 10000], [5, 5000]],changeTime = 100000,numLaps = 1000) == 62402500: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 15,numLaps = 100) == 2485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 15,numLaps = 100) == 2485: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10], [2, 20], [3, 30], [4, 40]],changeTime = 100,numLaps = 500) == 27650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10], [2, 20], [3, 30], [4, 40]],changeTime = 100,numLaps = 500) == 27650: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],changeTime = 100,numLaps = 900) == 23480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],changeTime = 100,numLaps = 900) == 23480: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1000, 1000], [1000, 1000], [1000, 1000]],changeTime = 100000,numLaps = 1000) == 100900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1000, 1000], [1000, 1000], [1000, 1000]],changeTime = 100000,numLaps = 1000) == 100900000: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 3], [5, 7], [3, 4]],changeTime = 8,numLaps = 100) == 792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 3], [5, 7], [3, 4]],changeTime = 8,numLaps = 100) == 792: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 5], [3, 4], [4, 3]],changeTime = 10,numLaps = 100) == 1090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 5], [3, 4], [4, 3]],changeTime = 10,numLaps = 100) == 1090: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 10], [2, 5], [3, 2]],changeTime = 10,numLaps = 999) == 9482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 10], [2, 5], [3, 2]],changeTime = 10,numLaps = 999) == 9482: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],changeTime = 25,numLaps = 1000) == 27475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],changeTime = 25,numLaps = 1000) == 27475: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 100], [2, 50], [3, 25], [4, 10]],changeTime = 5,numLaps = 50) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 100], [2, 50], [3, 25], [4, 10]],changeTime = 5,numLaps = 50) == 295: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 3], [1, 4]],changeTime = 5,numLaps = 50) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 3], [1, 4]],changeTime = 5,numLaps = 50) == 195: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8]],changeTime = 8,numLaps = 100) == 842
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8]],changeTime = 8,numLaps = 100) == 842: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[5, 2], [4, 3], [3, 4], [2, 5]],changeTime = 1,numLaps = 999) == 2996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[5, 2], [4, 3], [3, 4], [2, 5]],changeTime = 1,numLaps = 999) == 2996: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1000, 100], [500, 50], [250, 25], [100, 10], [50, 5]],changeTime = 500,numLaps = 500) == 199500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1000, 100], [500, 50], [250, 25], [100, 10], [50, 5]],changeTime = 500,numLaps = 500) == 199500: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 2], [3, 3], [4, 4]],changeTime = 10,numLaps = 25) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 2], [3, 3], [4, 4]],changeTime = 10,numLaps = 25) == 190: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100, 100], [50, 50], [25, 25], [10, 10]],changeTime = 20,numLaps = 50) == 1480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100, 100], [50, 50], [25, 25], [10, 10]],changeTime = 20,numLaps = 50) == 1480: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 1,numLaps = 1000) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 1,numLaps = 1000) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[2, 5], [1, 3], [3, 2], [2, 4]],changeTime = 7,numLaps = 30) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[2, 5], [1, 3], [3, 2], [2, 4]],changeTime = 7,numLaps = 30) == 158: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 2,numLaps = 100) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 2,numLaps = 100) == 248: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 10,numLaps = 50) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 10,numLaps = 50) == 275: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[100000, 100000]],changeTime = 100000,numLaps = 1000) == 199900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[100000, 100000]],changeTime = 100000,numLaps = 1000) == 199900000: {e}')
    
    total += 1
    try:
        result = candidate(tires = [[1, 1000], [2, 500], [3, 250]],changeTime = 50,numLaps = 20) == 970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tires = [[1, 1000], [2, 500], [3, 250]],changeTime = 50,numLaps = 20) == 970: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tires = [[2, 3], [3, 4]],changeTime = 5,numLaps = 4) == 21
    assert candidate(tires = [[5, 2], [3, 3]],changeTime = 4,numLaps = 3) == 17
    assert candidate(tires = [[5, 5], [3, 3]],changeTime = 10,numLaps = 6) == 56
    assert candidate(tires = [[100000, 2]],changeTime = 100000,numLaps = 1000) == 199900000
    assert candidate(tires = [[5, 2]],changeTime = 3,numLaps = 3) == 21
    assert candidate(tires = [[10, 10], [5, 5], [2, 2]],changeTime = 5,numLaps = 3) == 13
    assert candidate(tires = [[10, 5], [20, 2]],changeTime = 7,numLaps = 8) == 129
    assert candidate(tires = [[1, 2]],changeTime = 3,numLaps = 1) == 1
    assert candidate(tires = [[5, 5], [10, 2]],changeTime = 7,numLaps = 3) == 29
    assert candidate(tires = [[10, 5], [2, 2]],changeTime = 1,numLaps = 10) == 29
    assert candidate(tires = [[5, 2]],changeTime = 3,numLaps = 2) == 13
    assert candidate(tires = [[1, 10], [2, 2], [3, 4]],changeTime = 6,numLaps = 5) == 25
    assert candidate(tires = [[1, 2]],changeTime = 3,numLaps = 10) == 27
    assert candidate(tires = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],changeTime = 5,numLaps = 750) == 4495
    assert candidate(tires = [[2, 3], [3, 4], [5, 6], [7, 8]],changeTime = 5,numLaps = 15) == 93
    assert candidate(tires = [[1, 100000], [2, 90000], [3, 80000], [4, 70000], [5, 60000], [6, 50000], [7, 40000], [8, 30000], [9, 20000], [10, 10000]],changeTime = 100000,numLaps = 1000) == 99900500
    assert candidate(tires = [[10, 5], [2, 2], [3, 3]],changeTime = 6,numLaps = 20) == 114
    assert candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],changeTime = 1,numLaps = 900) == 1799
    assert candidate(tires = [[1, 5], [2, 3], [3, 2]],changeTime = 7,numLaps = 15) == 92
    assert candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 1,numLaps = 50) == 99
    assert candidate(tires = [[5, 3], [2, 8], [7, 2]],changeTime = 5,numLaps = 200) == 1395
    assert candidate(tires = [[100, 100], [200, 200], [300, 300]],changeTime = 50,numLaps = 1000) == 149950
    assert candidate(tires = [[2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],changeTime = 5,numLaps = 500) == 3495
    assert candidate(tires = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25]],changeTime = 20,numLaps = 500) == 12480
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],changeTime = 5,numLaps = 50) == 195
    assert candidate(tires = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],changeTime = 50,numLaps = 750) == 12100
    assert candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],changeTime = 10,numLaps = 999) == 8984
    assert candidate(tires = [[1, 2], [3, 4], [5, 6]],changeTime = 10,numLaps = 15) == 75
    assert candidate(tires = [[2, 3], [3, 4], [1, 5]],changeTime = 5,numLaps = 10) == 50
    assert candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 10,numLaps = 25) == 190
    assert candidate(tires = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]],changeTime = 7,numLaps = 50) == 318
    assert candidate(tires = [[100, 2], [200, 3], [300, 4], [400, 5]],changeTime = 150,numLaps = 600) == 134850
    assert candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 10,numLaps = 1000) == 7990
    assert candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 1,numLaps = 1000) == 1999
    assert candidate(tires = [[1000, 2], [500, 3], [250, 4]],changeTime = 500,numLaps = 100) == 74500
    assert candidate(tires = [[5, 3], [7, 4], [2, 2]],changeTime = 10,numLaps = 20) == 150
    assert candidate(tires = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6]],changeTime = 5,numLaps = 500) == 5495
    assert candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 1,numLaps = 100) == 199
    assert candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 100000,numLaps = 1) == 1
    assert candidate(tires = [[1, 10000], [2, 5000], [3, 1000], [4, 500], [5, 250], [6, 125], [7, 62], [8, 31], [9, 15], [10, 7]],changeTime = 1000,numLaps = 1000) == 522400
    assert candidate(tires = [[1, 10], [2, 5], [3, 3]],changeTime = 15,numLaps = 500) == 6485
    assert candidate(tires = [[1, 10], [2, 2], [3, 4], [4, 5]],changeTime = 5,numLaps = 30) == 160
    assert candidate(tires = [[100, 100], [200, 50], [300, 25]],changeTime = 100,numLaps = 300) == 59900
    assert candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 50,numLaps = 750) == 44950
    assert candidate(tires = [[1, 2], [1, 2], [1, 2]],changeTime = 0,numLaps = 100) == 100
    assert candidate(tires = [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2]],changeTime = 10,numLaps = 500) == 3990
    assert candidate(tires = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],changeTime = 15,numLaps = 50) == 470
    assert candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 5,numLaps = 15) == 55
    assert candidate(tires = [[3, 5], [2, 3], [4, 4]],changeTime = 10,numLaps = 15) == 128
    assert candidate(tires = [[5, 10], [3, 3], [2, 2]],changeTime = 10,numLaps = 20) == 150
    assert candidate(tires = [[100000, 100000], [50000, 50000], [25000, 25000], [12500, 12500], [6250, 6250]],changeTime = 100000,numLaps = 1000) == 106150000
    assert candidate(tires = [[100, 10], [50, 5], [25, 2]],changeTime = 20,numLaps = 1000) == 44980
    assert candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],changeTime = 3,numLaps = 40) == 197
    assert candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 100,numLaps = 50) == 5150
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 1,numLaps = 1) == 1
    assert candidate(tires = [[10000, 2], [5000, 3], [1000, 4], [500, 5], [250, 6], [125, 7], [62, 8], [31, 9], [15, 10], [7, 11]],changeTime = 10000,numLaps = 1000) == 3639260
    assert candidate(tires = [[3, 2], [4, 3], [5, 4], [6, 5], [7, 6]],changeTime = 15,numLaps = 30) == 345
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]],changeTime = 5,numLaps = 200) == 795
    assert candidate(tires = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],changeTime = 10,numLaps = 1000) == 14990
    assert candidate(tires = [[1, 2], [2, 3], [3, 4]],changeTime = 0,numLaps = 100) == 100
    assert candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5]],changeTime = 5,numLaps = 15) == 55
    assert candidate(tires = [[5, 2], [8, 3], [1, 2]],changeTime = 20,numLaps = 20) == 155
    assert candidate(tires = [[5, 2], [10, 2], [15, 2]],changeTime = 20,numLaps = 1000) == 17480
    assert candidate(tires = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 5]],changeTime = 10,numLaps = 800) == 11990
    assert candidate(tires = [[2, 3], [5, 7], [8, 9]],changeTime = 5,numLaps = 20) == 125
    assert candidate(tires = [[5, 3], [10, 2], [2, 6]],changeTime = 7,numLaps = 15) == 128
    assert candidate(tires = [[5, 2], [3, 3], [4, 4]],changeTime = 10,numLaps = 20) == 210
    assert candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],changeTime = 7,numLaps = 60) == 443
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 5,numLaps = 30) == 115
    assert candidate(tires = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]],changeTime = 1,numLaps = 1000) == 1999
    assert candidate(tires = [[50, 50], [25, 25], [10, 10], [5, 5], [2, 2]],changeTime = 25,numLaps = 750) == 9725
    assert candidate(tires = [[100000, 2], [50000, 3]],changeTime = 50000,numLaps = 500) == 49950000
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],changeTime = 5,numLaps = 50) == 195
    assert candidate(tires = [[3, 5], [5, 3], [7, 2]],changeTime = 15,numLaps = 200) == 3285
    assert candidate(tires = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],changeTime = 10,numLaps = 200) == 1125
    assert candidate(tires = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],changeTime = 20,numLaps = 800) == 11180
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],changeTime = 5,numLaps = 50) == 195
    assert candidate(tires = [[10, 10], [5, 5], [1, 2]],changeTime = 5,numLaps = 30) == 115
    assert candidate(tires = [[1, 100000], [2, 50000], [3, 25000], [4, 10000], [5, 5000]],changeTime = 100000,numLaps = 1000) == 62402500
    assert candidate(tires = [[10, 10], [20, 20], [30, 30]],changeTime = 15,numLaps = 100) == 2485
    assert candidate(tires = [[1, 10], [2, 20], [3, 30], [4, 40]],changeTime = 100,numLaps = 500) == 27650
    assert candidate(tires = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]],changeTime = 100,numLaps = 900) == 23480
    assert candidate(tires = [[1000, 1000], [1000, 1000], [1000, 1000]],changeTime = 100000,numLaps = 1000) == 100900000
    assert candidate(tires = [[2, 3], [5, 7], [3, 4]],changeTime = 8,numLaps = 100) == 792
    assert candidate(tires = [[2, 5], [3, 4], [4, 3]],changeTime = 10,numLaps = 100) == 1090
    assert candidate(tires = [[1, 10], [2, 5], [3, 2]],changeTime = 10,numLaps = 999) == 9482
    assert candidate(tires = [[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],changeTime = 25,numLaps = 1000) == 27475
    assert candidate(tires = [[1, 100], [2, 50], [3, 25], [4, 10]],changeTime = 5,numLaps = 50) == 295
    assert candidate(tires = [[1, 2], [1, 3], [1, 4]],changeTime = 5,numLaps = 50) == 195
    assert candidate(tires = [[7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8]],changeTime = 8,numLaps = 100) == 842
    assert candidate(tires = [[5, 2], [4, 3], [3, 4], [2, 5]],changeTime = 1,numLaps = 999) == 2996
    assert candidate(tires = [[1000, 100], [500, 50], [250, 25], [100, 10], [50, 5]],changeTime = 500,numLaps = 500) == 199500
    assert candidate(tires = [[2, 2], [3, 3], [4, 4]],changeTime = 10,numLaps = 25) == 190
    assert candidate(tires = [[100, 100], [50, 50], [25, 25], [10, 10]],changeTime = 20,numLaps = 50) == 1480
    assert candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 1,numLaps = 1000) == 1999
    assert candidate(tires = [[2, 5], [1, 3], [3, 2], [2, 4]],changeTime = 7,numLaps = 30) == 158
    assert candidate(tires = [[1, 2], [2, 3], [3, 4], [4, 5]],changeTime = 2,numLaps = 100) == 248
    assert candidate(tires = [[1, 2], [1, 2], [1, 2], [1, 2]],changeTime = 10,numLaps = 50) == 275
    assert candidate(tires = [[100000, 100000]],changeTime = 100000,numLaps = 1000) == 199900000
    assert candidate(tires = [[1, 1000], [2, 500], [3, 250]],changeTime = 50,numLaps = 20) == 970


