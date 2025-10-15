def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 2], [5, 6]],slots2 = [[1, 2], [5, 6]],duration = 1) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 2], [5, 6]],slots2 = [[1, 2], [5, 6]],duration = 1) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 5], [10, 15]],slots2 = [[2, 3]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 5], [10, 15]],slots2 = [[2, 3]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 1000000000]],slots2 = [[1, 1000000000]],duration = 1000000000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 1000000000]],slots2 = [[1, 1000000000]],duration = 1000000000) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [5, 6]],slots2 = [[2, 4]],duration = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [5, 6]],slots2 = [[2, 4]],duration = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70]],duration = 12) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70]],duration = 12) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [50, 60]],slots2 = [[10, 15], [55, 60]],duration = 5) == [55, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [50, 60]],slots2 = [[10, 15], [55, 60]],duration = 5) == [55, 60]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70]],duration = 8) == [60, 68]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70]],duration = 8) == [60, 68]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 5]],slots2 = [[6, 10]],duration = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 5]],slots2 = [[6, 10]],duration = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [4, 6]],slots2 = [[2, 4], [5, 7]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [4, 6]],slots2 = [[2, 4], [5, 7]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [6, 9]],slots2 = [[2, 4], [7, 10]],duration = 2) == [7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [6, 9]],slots2 = [[2, 4], [7, 10]],duration = 2) == [7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10]],slots2 = [[10, 20]],duration = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10]],slots2 = [[10, 20]],duration = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50]],slots2 = [[50, 100]],duration = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50]],slots2 = [[50, 100]],duration = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [5, 10]],slots2 = [[2, 4]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [5, 10]],slots2 = [[2, 4]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[8, 12]],slots2 = [[14, 16]],duration = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[8, 12]],slots2 = [[14, 16]],duration = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20]],slots2 = [[5, 10], [15, 20]],duration = 5) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20]],slots2 = [[5, 10], [15, 20]],duration = 5) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120]],slots2 = [[55, 60]],duration = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120]],slots2 = [[55, 60]],duration = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 100]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 10) == [10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 100]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 10) == [10, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10]],slots2 = [[2, 9]],duration = 5) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10]],slots2 = [[2, 9]],duration = 5) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30]],slots2 = [[5, 15], [25, 35]],duration = 5) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30]],slots2 = [[5, 15], [25, 35]],duration = 5) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10]],slots2 = [[2, 6], [7, 9]],duration = 2) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10]],slots2 = [[2, 6], [7, 9]],duration = 2) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3]],slots2 = [[2, 4]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3]],slots2 = [[2, 4]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 100]],slots2 = [[50, 60]],duration = 10) == [50, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 100]],slots2 = [[50, 60]],duration = 10) == [50, 60]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[8, 12], [15, 20]],slots2 = [[9, 13], [18, 24]],duration = 3) == [9, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[8, 12], [15, 20]],slots2 = [[9, 13], [18, 24]],duration = 3) == [9, 12]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20], [25, 30], [35, 40]],slots2 = [[3, 8], [12, 17], [22, 27], [32, 37]],duration = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20], [25, 30], [35, 40]],slots2 = [[3, 8], [12, 17], [22, 27], [32, 37]],duration = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 5) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 5) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 75], [145, 205]],duration = 15) == [10, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 75], [145, 205]],duration = 15) == [10, 25]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70], [80, 90]],slots2 = [[2, 9], [19, 29], [39, 49], [59, 69], [79, 89]],duration = 8) == [20, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70], [80, 90]],slots2 = [[2, 9], [19, 29], [39, 49], [59, 69], [79, 89]],duration = 8) == [20, 28]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 1000000000]],slots2 = [[500000000, 1500000000]],duration = 100000000) == [500000000, 600000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 1000000000]],slots2 = [[500000000, 1500000000]],duration = 100000000) == [500000000, 600000000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 25], [30, 40]],slots2 = [[10, 20], [25, 35], [40, 50]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 25], [30, 40]],slots2 = [[10, 20], [25, 35], [40, 50]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[0, 1000000000]],slots2 = [[500000000, 1000000000]],duration = 100000000) == [500000000, 600000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[0, 1000000000]],slots2 = [[500000000, 1000000000]],duration = 100000000) == [500000000, 600000000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70]],slots2 = [[5, 15], [25, 35], [45, 55], [65, 75]],duration = 5) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70]],slots2 = [[5, 15], [25, 35], [45, 55], [65, 75]],duration = 5) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 5], [10, 15], [20, 25]],slots2 = [[2, 6], [11, 16], [21, 26]],duration = 2) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 5], [10, 15], [20, 25]],slots2 = [[2, 6], [11, 16], [21, 26]],duration = 2) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 1000000], [2000000, 3000000]],slots2 = [[500000, 1500000], [2500000, 3500000]],duration = 100000) == [500000, 600000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 1000000], [2000000, 3000000]],slots2 = [[500000, 1500000], [2500000, 3500000]],duration = 100000) == [500000, 600000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 15], [30, 45], [60, 75]],slots2 = [[10, 20], [40, 50], [70, 80]],duration = 5) == [10, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 15], [30, 45], [60, 75]],slots2 = [[10, 20], [40, 50], [70, 80]],duration = 5) == [10, 15]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 110], [200, 210], [300, 310]],slots2 = [[105, 115], [205, 215], [305, 315]],duration = 5) == [105, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 110], [200, 210], [300, 310]],slots2 = [[105, 115], [205, 215], [305, 315]],duration = 5) == [105, 110]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20]],slots2 = [[10, 20], [20, 30]],duration = 10) == [10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20]],slots2 = [[10, 20], [20, 30]],duration = 10) == [10, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70], [80, 90]],slots2 = [[2, 9], [11, 19], [21, 29], [31, 39], [41, 49]],duration = 2) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70], [80, 90]],slots2 = [[2, 9], [11, 19], [21, 29], [31, 39], [41, 49]],duration = 2) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[8, 12], [18, 22], [28, 32]],slots2 = [[10, 14], [20, 24], [26, 30]],duration = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[8, 12], [18, 22], [28, 32]],slots2 = [[10, 14], [20, 24], [26, 30]],duration = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 1000000000]],slots2 = [[1, 1000000000]],duration = 500000000) == [1, 500000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 1000000000]],slots2 = [[1, 1000000000]],duration = 500000000) == [1, 500000001]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70], [130, 150]],duration = 10) == [60, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70], [130, 150]],duration = 10) == [60, 70]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 30], [60, 120], [140, 210]],slots2 = [[15, 40], [70, 100]],duration = 15) == [15, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 30], [60, 120], [140, 210]],slots2 = [[15, 40], [70, 100]],duration = 15) == [15, 30]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 80], [110, 130]],duration = 10) == [10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 80], [110, 130]],duration = 10) == [10, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[3, 8], [12, 17], [22, 27]],duration = 3) == [5, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[3, 8], [12, 17], [22, 27]],duration = 3) == [5, 8]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 500000000], [600000000, 1000000000]],slots2 = [[200000000, 400000000], [700000000, 900000000]],duration = 100000000) == [200000000, 300000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 500000000], [600000000, 1000000000]],slots2 = [[200000000, 400000000], [700000000, 900000000]],duration = 100000000) == [200000000, 300000000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 110], [120, 130], [140, 150]],slots2 = [[105, 115], [125, 135], [145, 155]],duration = 5) == [105, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 110], [120, 130], [140, 150]],slots2 = [[105, 115], [125, 135], [145, 155]],duration = 5) == [105, 110]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 11) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 11) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[0, 1000000000]],slots2 = [[0, 1000000000]],duration = 1000000000) == [0, 1000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[0, 1000000000]],slots2 = [[0, 1000000000]],duration = 1000000000) == [0, 1000000000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 15], [25, 40], [55, 70]],slots2 = [[10, 30], [40, 60], [70, 90]],duration = 15) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 15], [25, 40], [55, 70]],slots2 = [[10, 30], [40, 60], [70, 90]],duration = 15) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 105], [200, 205], [300, 305]],slots2 = [[102, 107], [202, 207], [302, 307]],duration = 3) == [102, 105]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 105], [200, 205], [300, 305]],slots2 = [[102, 107], [202, 207], [302, 307]],duration = 3) == [102, 105]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 15) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 15) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 5], [10, 20], [30, 40], [50, 60]],slots2 = [[2, 4], [15, 25], [45, 55]],duration = 5) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 5], [10, 20], [30, 40], [50, 60]],slots2 = [[2, 4], [15, 25], [45, 55]],duration = 5) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 2], [3, 4], [5, 6]],slots2 = [[1, 2], [3, 4], [5, 6]],duration = 1) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 2], [3, 4], [5, 6]],slots2 = [[1, 2], [3, 4], [5, 6]],duration = 1) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 150], [200, 300], [350, 450]],slots2 = [[120, 220], [250, 350], [400, 500]],duration = 30) == [120, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 150], [200, 300], [350, 450]],slots2 = [[120, 220], [250, 350], [400, 500]],duration = 30) == [120, 150]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[6, 11], [16, 21], [26, 31]],duration = 2) == [6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[6, 11], [16, 21], [26, 31]],duration = 2) == [6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20], [25, 30], [35, 40]],slots2 = [[7, 8], [17, 18], [27, 28], [37, 38]],duration = 1) == [7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20], [25, 30], [35, 40]],slots2 = [[7, 8], [17, 18], [27, 28], [37, 38]],duration = 1) == [7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 30], [40, 60], [70, 90]],slots2 = [[15, 35], [55, 75], [85, 105]],duration = 10) == [15, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 30], [40, 60], [70, 90]],slots2 = [[15, 35], [55, 75], [85, 105]],duration = 10) == [15, 25]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],duration = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],duration = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [5, 7], [9, 11]],slots2 = [[2, 4], [6, 8], [10, 12]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [5, 7], [9, 11]],slots2 = [[2, 4], [6, 8], [10, 12]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [5, 7], [9, 11]],slots2 = [[2, 4], [6, 8], [10, 12]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [5, 7], [9, 11]],slots2 = [[2, 4], [6, 8], [10, 12]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[25, 35], [45, 55], [50, 60]],duration = 5) == [30, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[25, 35], [45, 55], [50, 60]],duration = 5) == [30, 35]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30], [40, 50]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 5) == [20, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30], [40, 50]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 5) == [20, 25]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[8, 12], [20, 25], [30, 35]],slots2 = [[10, 14], [22, 27], [33, 38]],duration = 3) == [22, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[8, 12], [20, 25], [30, 35]],slots2 = [[10, 14], [22, 27], [33, 38]],duration = 3) == [22, 25]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 5], [10, 15], [20, 25]],slots2 = [[2, 3], [11, 14], [21, 24]],duration = 1) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 5], [10, 15], [20, 25]],slots2 = [[2, 3], [11, 14], [21, 24]],duration = 1) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [100, 150], [200, 250]],slots2 = [[10, 50], [100, 150], [200, 250]],duration = 30) == [10, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [100, 150], [200, 250]],slots2 = [[10, 50], [100, 150], [200, 250]],duration = 30) == [10, 40]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [25, 30], [35, 40]],slots2 = [[15, 20], [26, 31], [36, 41]],duration = 5) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [25, 30], [35, 40]],slots2 = [[15, 20], [26, 31], [36, 41]],duration = 5) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[10, 50], [60, 120], [140, 210]],duration = 30) == [10, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[10, 50], [60, 120], [140, 210]],duration = 30) == [10, 40]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 10) == [10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 10) == [10, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [11, 20], [21, 30]],slots2 = [[2, 9], [12, 19], [22, 29]],duration = 2) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [11, 20], [21, 30]],slots2 = [[2, 9], [12, 19], [22, 29]],duration = 2) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 150], [200, 250]],slots2 = [[120, 170], [220, 270]],duration = 30) == [120, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 150], [200, 250]],slots2 = [[120, 170], [220, 270]],duration = 30) == [120, 150]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [6, 9], [12, 15]],slots2 = [[2, 4], [5, 7], [8, 10]],duration = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [6, 9], [12, 15]],slots2 = [[2, 4], [5, 7], [8, 10]],duration = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [65, 75], [200, 210]],duration = 10) == [65, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [65, 75], [200, 210]],duration = 10) == [65, 75]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 15], [25, 30]],slots2 = [[12, 17], [27, 32]],duration = 3) == [12, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 15], [25, 30]],slots2 = [[12, 17], [27, 32]],duration = 3) == [12, 15]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 110], [120, 130], [140, 150]],slots2 = [[105, 115], [125, 135], [145, 155]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 110], [120, 130], [140, 150]],slots2 = [[105, 115], [125, 135], [145, 155]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 5], [10, 15], [20, 25], [30, 35]],slots2 = [[2, 3], [11, 14], [16, 21], [32, 36]],duration = 2) == [11, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 5], [10, 15], [20, 25], [30, 35]],slots2 = [[2, 3], [11, 14], [16, 21], [32, 36]],duration = 2) == [11, 13]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 80], [190, 215]],duration = 15) == [10, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 80], [190, 215]],duration = 15) == [10, 25]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[8, 12], [15, 20], [25, 30]],slots2 = [[9, 11], [16, 19], [27, 29]],duration = 2) == [9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[8, 12], [15, 20], [25, 30]],slots2 = [[9, 11], [16, 19], [27, 29]],duration = 2) == [9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[2, 5], [8, 13], [18, 23], [28, 33]],slots2 = [[1, 4], [7, 12], [17, 22], [27, 32]],duration = 3) == [8, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[2, 5], [8, 13], [18, 23], [28, 33]],slots2 = [[1, 4], [7, 12], [17, 22], [27, 32]],duration = 3) == [8, 11]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70], [110, 130]],duration = 10) == [60, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70], [110, 130]],duration = 10) == [60, 70]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 50], [60, 80]],slots2 = [[15, 25], [40, 60], [70, 90]],duration = 5) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 50], [60, 80]],slots2 = [[15, 25], [40, 60], [70, 90]],duration = 5) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 5) == [10, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 5) == [10, 15]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[2, 3], [4, 5], [6, 7], [8, 9]],duration = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[2, 3], [4, 5], [6, 7], [8, 9]],duration = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40]],slots2 = [[15, 25], [35, 45]],duration = 11) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40]],slots2 = [[15, 25], [35, 45]],duration = 11) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [65, 75], [200, 210]],duration = 5) == [10, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [65, 75], [200, 210]],duration = 5) == [10, 15]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 50], [60, 70]],slots2 = [[15, 25], [45, 55], [65, 75]],duration = 5) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 50], [60, 70]],slots2 = [[15, 25], [45, 55], [65, 75]],duration = 5) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 100]],slots2 = [[1, 100]],duration = 100) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 100]],slots2 = [[1, 100]],duration = 100) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [40, 50]],duration = 5) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [40, 50]],duration = 5) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],duration = 1) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],duration = 1) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60], [70, 80]],slots2 = [[15, 25], [35, 45], [55, 65], [75, 85]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60], [70, 80]],slots2 = [[15, 25], [35, 45], [55, 65], [75, 85]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 1000000000], [2000000000, 3000000000]],slots2 = [[500000000, 1500000000], [2500000000, 3500000000]],duration = 100000000) == [500000000, 600000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 1000000000], [2000000000, 3000000000]],slots2 = [[500000000, 1500000000], [2500000000, 3500000000]],duration = 100000000) == [500000000, 600000000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30], [40, 50]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 5) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30], [40, 50]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 5) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 15], [25, 35], [45, 55]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 10) == [5, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 15], [25, 35], [45, 55]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 10) == [5, 15]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 30], [50, 80], [100, 130]],slots2 = [[20, 50], [70, 100], [120, 150]],duration = 20) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 30], [50, 80], [100, 130]],slots2 = [[20, 50], [70, 100], [120, 150]],duration = 20) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 200], [300, 400], [500, 600]],slots2 = [[150, 250], [350, 450], [550, 650]],duration = 100) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 200], [300, 400], [500, 600]],slots2 = [[150, 250], [350, 450], [550, 650]],duration = 100) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[9, 12], [13, 18], [20, 25]],slots2 = [[10, 15], [16, 21], [22, 27]],duration = 3) == [22, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[9, 12], [13, 18], [20, 25]],slots2 = [[10, 15], [16, 21], [22, 27]],duration = 3) == [22, 25]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 15], [20, 25], [30, 35]],slots2 = [[12, 17], [22, 27], [32, 37]],duration = 3) == [12, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 15], [20, 25], [30, 35]],slots2 = [[12, 17], [22, 27], [32, 37]],duration = 3) == [12, 15]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[20, 30], [80, 100], [150, 170]],duration = 10) == [20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[20, 30], [80, 100], [150, 170]],duration = 10) == [20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1000000000, 2000000000]],slots2 = [[1500000000, 2500000000]],duration = 500000000) == [1500000000, 2000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1000000000, 2000000000]],slots2 = [[1500000000, 2500000000]],duration = 500000000) == [1500000000, 2000000000]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 3], [4, 6], [7, 9]],slots2 = [[2, 4], [5, 7], [8, 10]],duration = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 3], [4, 6], [7, 9]],slots2 = [[2, 4], [5, 7], [8, 10]],duration = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[8, 12], [16, 20], [24, 28]],slots2 = [[9, 11], [17, 19], [25, 27]],duration = 2) == [9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[8, 12], [16, 20], [24, 28]],slots2 = [[9, 11], [17, 19], [25, 27]],duration = 2) == [9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[6, 11], [16, 21], [26, 31]],duration = 4) == [6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[6, 11], [16, 21], [26, 31]],duration = 4) == [6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 100], [200, 300], [400, 500]],slots2 = [[50, 150], [250, 350], [450, 550]],duration = 50) == [50, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 100], [200, 300], [400, 500]],slots2 = [[50, 150], [250, 350], [450, 550]],duration = 50) == [50, 100]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [11, 20], [21, 30]],slots2 = [[5, 15], [16, 26], [21, 31]],duration = 5) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [11, 20], [21, 30]],slots2 = [[5, 15], [16, 26], [21, 31]],duration = 5) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [15, 20], [25, 30]],slots2 = [[5, 15], [20, 30], [35, 40]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [15, 20], [25, 30]],slots2 = [[5, 15], [20, 30], [35, 40]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[55, 65], [130, 145]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[55, 65], [130, 145]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1000000000, 1000000010], [1000000020, 1000000030]],slots2 = [[1000000005, 1000000015], [1000000025, 1000000035]],duration = 5) == [1000000005, 1000000010]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1000000000, 1000000010], [1000000020, 1000000030]],slots2 = [[1000000005, 1000000015], [1000000025, 1000000035]],duration = 5) == [1000000005, 1000000010]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[100, 200], [300, 400], [500, 600]],slots2 = [[150, 250], [350, 450], [550, 650]],duration = 50) == [150, 200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[100, 200], [300, 400], [500, 600]],slots2 = [[150, 250], [350, 450], [550, 650]],duration = 50) == [150, 200]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60], [70, 80]],slots2 = [[5, 25], [35, 55], [65, 85]],duration = 15) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60], [70, 80]],slots2 = [[5, 25], [35, 55], [65, 85]],duration = 15) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[5, 25], [35, 55], [65, 85]],duration = 20) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[5, 25], [35, 55], [65, 85]],duration = 20) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[3, 8], [13, 18], [23, 28]],duration = 2) == [5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[3, 8], [13, 18], [23, 28]],duration = 2) == [5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[0, 20], [40, 60], [80, 100]],slots2 = [[10, 30], [50, 70], [90, 110]],duration = 20) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[0, 20], [40, 60], [80, 100]],slots2 = [[10, 30], [50, 70], [90, 110]],duration = 20) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70]],slots2 = [[5, 15], [25, 35], [45, 55], [65, 75]],duration = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70]],slots2 = [[5, 15], [25, 35], [45, 55], [65, 75]],duration = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[1, 2], [3, 4], [5, 6]],slots2 = [[1, 2], [3, 4], [5, 6]],duration = 1) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[1, 2], [3, 4], [5, 6]],slots2 = [[1, 2], [3, 4], [5, 6]],duration = 1) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [55, 65], [145, 205]],duration = 8) == [145, 153]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [55, 65], [145, 205]],duration = 8) == [145, 153]: {e}')
    
    total += 1
    try:
        result = candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 55], [55, 65], [65, 75]],duration = 10) == [10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 55], [55, 65], [65, 75]],duration = 10) == [10, 20]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(slots1 = [[1, 2], [5, 6]],slots2 = [[1, 2], [5, 6]],duration = 1) == [1, 2]
    assert candidate(slots1 = [[1, 5], [10, 15]],slots2 = [[2, 3]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[1, 1000000000]],slots2 = [[1, 1000000000]],duration = 1000000000) == []
    assert candidate(slots1 = [[1, 3], [5, 6]],slots2 = [[2, 4]],duration = 2) == []
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70]],duration = 12) == []
    assert candidate(slots1 = [[1, 10], [50, 60]],slots2 = [[10, 15], [55, 60]],duration = 5) == [55, 60]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70]],duration = 8) == [60, 68]
    assert candidate(slots1 = [[1, 5]],slots2 = [[6, 10]],duration = 1) == []
    assert candidate(slots1 = [[1, 3], [4, 6]],slots2 = [[2, 4], [5, 7]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[1, 3], [6, 9]],slots2 = [[2, 4], [7, 10]],duration = 2) == [7, 9]
    assert candidate(slots1 = [[1, 10]],slots2 = [[10, 20]],duration = 1) == []
    assert candidate(slots1 = [[10, 50]],slots2 = [[50, 100]],duration = 5) == []
    assert candidate(slots1 = [[1, 3], [5, 10]],slots2 = [[2, 4]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[8, 12]],slots2 = [[14, 16]],duration = 1) == []
    assert candidate(slots1 = [[5, 10], [15, 20]],slots2 = [[5, 10], [15, 20]],duration = 5) == [5, 10]
    assert candidate(slots1 = [[10, 50], [60, 120]],slots2 = [[55, 60]],duration = 5) == []
    assert candidate(slots1 = [[1, 100]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 10) == [10, 20]
    assert candidate(slots1 = [[1, 10]],slots2 = [[2, 9]],duration = 5) == [2, 7]
    assert candidate(slots1 = [[1, 10], [20, 30]],slots2 = [[5, 15], [25, 35]],duration = 5) == [5, 10]
    assert candidate(slots1 = [[1, 10]],slots2 = [[2, 6], [7, 9]],duration = 2) == [2, 4]
    assert candidate(slots1 = [[1, 3]],slots2 = [[2, 4]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[10, 100]],slots2 = [[50, 60]],duration = 10) == [50, 60]
    assert candidate(slots1 = [[8, 12], [15, 20]],slots2 = [[9, 13], [18, 24]],duration = 3) == [9, 12]
    assert candidate(slots1 = [[5, 10], [15, 20], [25, 30], [35, 40]],slots2 = [[3, 8], [12, 17], [22, 27], [32, 37]],duration = 5) == []
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 5) == [15, 20]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 75], [145, 205]],duration = 15) == [10, 25]
    assert candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70], [80, 90]],slots2 = [[2, 9], [19, 29], [39, 49], [59, 69], [79, 89]],duration = 8) == [20, 28]
    assert candidate(slots1 = [[1, 1000000000]],slots2 = [[500000000, 1500000000]],duration = 100000000) == [500000000, 600000000]
    assert candidate(slots1 = [[5, 10], [15, 25], [30, 40]],slots2 = [[10, 20], [25, 35], [40, 50]],duration = 10) == []
    assert candidate(slots1 = [[0, 1000000000]],slots2 = [[500000000, 1000000000]],duration = 100000000) == [500000000, 600000000]
    assert candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70]],slots2 = [[5, 15], [25, 35], [45, 55], [65, 75]],duration = 5) == [5, 10]
    assert candidate(slots1 = [[1, 5], [10, 15], [20, 25]],slots2 = [[2, 6], [11, 16], [21, 26]],duration = 2) == [2, 4]
    assert candidate(slots1 = [[1, 1000000], [2000000, 3000000]],slots2 = [[500000, 1500000], [2500000, 3500000]],duration = 100000) == [500000, 600000]
    assert candidate(slots1 = [[5, 15], [30, 45], [60, 75]],slots2 = [[10, 20], [40, 50], [70, 80]],duration = 5) == [10, 15]
    assert candidate(slots1 = [[100, 110], [200, 210], [300, 310]],slots2 = [[105, 115], [205, 215], [305, 315]],duration = 5) == [105, 110]
    assert candidate(slots1 = [[10, 20]],slots2 = [[10, 20], [20, 30]],duration = 10) == [10, 20]
    assert candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70], [80, 90]],slots2 = [[2, 9], [11, 19], [21, 29], [31, 39], [41, 49]],duration = 2) == [2, 4]
    assert candidate(slots1 = [[8, 12], [18, 22], [28, 32]],slots2 = [[10, 14], [20, 24], [26, 30]],duration = 3) == []
    assert candidate(slots1 = [[1, 1000000000]],slots2 = [[1, 1000000000]],duration = 500000000) == [1, 500000001]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70], [130, 150]],duration = 10) == [60, 70]
    assert candidate(slots1 = [[10, 30], [60, 120], [140, 210]],slots2 = [[15, 40], [70, 100]],duration = 15) == [15, 30]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 10) == []
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 80], [110, 130]],duration = 10) == [10, 20]
    assert candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[3, 8], [12, 17], [22, 27]],duration = 3) == [5, 8]
    assert candidate(slots1 = [[1, 500000000], [600000000, 1000000000]],slots2 = [[200000000, 400000000], [700000000, 900000000]],duration = 100000000) == [200000000, 300000000]
    assert candidate(slots1 = [[100, 110], [120, 130], [140, 150]],slots2 = [[105, 115], [125, 135], [145, 155]],duration = 5) == [105, 110]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 11) == []
    assert candidate(slots1 = [[0, 1000000000]],slots2 = [[0, 1000000000]],duration = 1000000000) == [0, 1000000000]
    assert candidate(slots1 = [[5, 15], [25, 40], [55, 70]],slots2 = [[10, 30], [40, 60], [70, 90]],duration = 15) == []
    assert candidate(slots1 = [[100, 105], [200, 205], [300, 305]],slots2 = [[102, 107], [202, 207], [302, 307]],duration = 3) == [102, 105]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 15) == []
    assert candidate(slots1 = [[1, 5], [10, 20], [30, 40], [50, 60]],slots2 = [[2, 4], [15, 25], [45, 55]],duration = 5) == [15, 20]
    assert candidate(slots1 = [[1, 2], [3, 4], [5, 6]],slots2 = [[1, 2], [3, 4], [5, 6]],duration = 1) == [1, 2]
    assert candidate(slots1 = [[100, 150], [200, 300], [350, 450]],slots2 = [[120, 220], [250, 350], [400, 500]],duration = 30) == [120, 150]
    assert candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[6, 11], [16, 21], [26, 31]],duration = 2) == [6, 8]
    assert candidate(slots1 = [[5, 10], [15, 20], [25, 30], [35, 40]],slots2 = [[7, 8], [17, 18], [27, 28], [37, 38]],duration = 1) == [7, 8]
    assert candidate(slots1 = [[10, 30], [40, 60], [70, 90]],slots2 = [[15, 35], [55, 75], [85, 105]],duration = 10) == [15, 25]
    assert candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],duration = 1) == []
    assert candidate(slots1 = [[1, 3], [5, 7], [9, 11]],slots2 = [[2, 4], [6, 8], [10, 12]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[1, 3], [5, 7], [9, 11]],slots2 = [[2, 4], [6, 8], [10, 12]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[25, 35], [45, 55], [50, 60]],duration = 5) == [30, 35]
    assert candidate(slots1 = [[1, 10], [20, 30], [40, 50]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 5) == [20, 25]
    assert candidate(slots1 = [[8, 12], [20, 25], [30, 35]],slots2 = [[10, 14], [22, 27], [33, 38]],duration = 3) == [22, 25]
    assert candidate(slots1 = [[1, 5], [10, 15], [20, 25]],slots2 = [[2, 3], [11, 14], [21, 24]],duration = 1) == [2, 3]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [55, 65]],duration = 10) == []
    assert candidate(slots1 = [[10, 50], [100, 150], [200, 250]],slots2 = [[10, 50], [100, 150], [200, 250]],duration = 30) == [10, 40]
    assert candidate(slots1 = [[10, 20], [25, 30], [35, 40]],slots2 = [[15, 20], [26, 31], [36, 41]],duration = 5) == [15, 20]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[10, 50], [60, 120], [140, 210]],duration = 30) == [10, 40]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 10) == [10, 20]
    assert candidate(slots1 = [[1, 10], [11, 20], [21, 30]],slots2 = [[2, 9], [12, 19], [22, 29]],duration = 2) == [2, 4]
    assert candidate(slots1 = [[100, 150], [200, 250]],slots2 = [[120, 170], [220, 270]],duration = 30) == [120, 150]
    assert candidate(slots1 = [[1, 3], [6, 9], [12, 15]],slots2 = [[2, 4], [5, 7], [8, 10]],duration = 2) == []
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [65, 75], [200, 210]],duration = 10) == [65, 75]
    assert candidate(slots1 = [[10, 15], [25, 30]],slots2 = [[12, 17], [27, 32]],duration = 3) == [12, 15]
    assert candidate(slots1 = [[100, 110], [120, 130], [140, 150]],slots2 = [[105, 115], [125, 135], [145, 155]],duration = 10) == []
    assert candidate(slots1 = [[1, 5], [10, 15], [20, 25], [30, 35]],slots2 = [[2, 3], [11, 14], [16, 21], [32, 36]],duration = 2) == [11, 13]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 25], [55, 80], [190, 215]],duration = 15) == [10, 25]
    assert candidate(slots1 = [[8, 12], [15, 20], [25, 30]],slots2 = [[9, 11], [16, 19], [27, 29]],duration = 2) == [9, 11]
    assert candidate(slots1 = [[2, 5], [8, 13], [18, 23], [28, 33]],slots2 = [[1, 4], [7, 12], [17, 22], [27, 32]],duration = 3) == [8, 11]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[0, 15], [60, 70], [110, 130]],duration = 10) == [60, 70]
    assert candidate(slots1 = [[10, 20], [30, 50], [60, 80]],slots2 = [[15, 25], [40, 60], [70, 90]],duration = 5) == [15, 20]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[10, 20], [30, 40], [50, 60]],duration = 5) == [10, 15]
    assert candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[2, 3], [4, 5], [6, 7], [8, 9]],duration = 1) == []
    assert candidate(slots1 = [[10, 20], [30, 40]],slots2 = [[15, 25], [35, 45]],duration = 11) == []
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [65, 75], [200, 210]],duration = 5) == [10, 15]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 10) == []
    assert candidate(slots1 = [[10, 20], [30, 50], [60, 70]],slots2 = [[15, 25], [45, 55], [65, 75]],duration = 5) == [15, 20]
    assert candidate(slots1 = [[1, 100]],slots2 = [[1, 100]],duration = 100) == []
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[15, 25], [35, 45], [40, 50]],duration = 5) == [15, 20]
    assert candidate(slots1 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],slots2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],duration = 1) == [1, 2]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60], [70, 80]],slots2 = [[15, 25], [35, 45], [55, 65], [75, 85]],duration = 10) == []
    assert candidate(slots1 = [[1, 1000000000], [2000000000, 3000000000]],slots2 = [[500000000, 1500000000], [2500000000, 3500000000]],duration = 100000000) == [500000000, 600000000]
    assert candidate(slots1 = [[1, 10], [20, 30], [40, 50]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 5) == [5, 10]
    assert candidate(slots1 = [[5, 15], [25, 35], [45, 55]],slots2 = [[5, 15], [25, 35], [45, 55]],duration = 10) == [5, 15]
    assert candidate(slots1 = [[1, 30], [50, 80], [100, 130]],slots2 = [[20, 50], [70, 100], [120, 150]],duration = 20) == []
    assert candidate(slots1 = [[100, 200], [300, 400], [500, 600]],slots2 = [[150, 250], [350, 450], [550, 650]],duration = 100) == []
    assert candidate(slots1 = [[9, 12], [13, 18], [20, 25]],slots2 = [[10, 15], [16, 21], [22, 27]],duration = 3) == [22, 25]
    assert candidate(slots1 = [[10, 15], [20, 25], [30, 35]],slots2 = [[12, 17], [22, 27], [32, 37]],duration = 3) == [12, 15]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[20, 30], [80, 100], [150, 170]],duration = 10) == [20, 30]
    assert candidate(slots1 = [[1000000000, 2000000000]],slots2 = [[1500000000, 2500000000]],duration = 500000000) == [1500000000, 2000000000]
    assert candidate(slots1 = [[1, 3], [4, 6], [7, 9]],slots2 = [[2, 4], [5, 7], [8, 10]],duration = 2) == []
    assert candidate(slots1 = [[8, 12], [16, 20], [24, 28]],slots2 = [[9, 11], [17, 19], [25, 27]],duration = 2) == [9, 11]
    assert candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[6, 11], [16, 21], [26, 31]],duration = 4) == [6, 10]
    assert candidate(slots1 = [[1, 100], [200, 300], [400, 500]],slots2 = [[50, 150], [250, 350], [450, 550]],duration = 50) == [50, 100]
    assert candidate(slots1 = [[1, 10], [11, 20], [21, 30]],slots2 = [[5, 15], [16, 26], [21, 31]],duration = 5) == [5, 10]
    assert candidate(slots1 = [[1, 10], [15, 20], [25, 30]],slots2 = [[5, 15], [20, 30], [35, 40]],duration = 10) == []
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[55, 65], [130, 145]],duration = 10) == []
    assert candidate(slots1 = [[1000000000, 1000000010], [1000000020, 1000000030]],slots2 = [[1000000005, 1000000015], [1000000025, 1000000035]],duration = 5) == [1000000005, 1000000010]
    assert candidate(slots1 = [[100, 200], [300, 400], [500, 600]],slots2 = [[150, 250], [350, 450], [550, 650]],duration = 50) == [150, 200]
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60], [70, 80]],slots2 = [[5, 25], [35, 55], [65, 85]],duration = 15) == []
    assert candidate(slots1 = [[10, 20], [30, 40], [50, 60]],slots2 = [[5, 25], [35, 55], [65, 85]],duration = 20) == []
    assert candidate(slots1 = [[5, 10], [15, 20], [25, 30]],slots2 = [[3, 8], [13, 18], [23, 28]],duration = 2) == [5, 7]
    assert candidate(slots1 = [[0, 20], [40, 60], [80, 100]],slots2 = [[10, 30], [50, 70], [90, 110]],duration = 20) == []
    assert candidate(slots1 = [[1, 10], [20, 30], [40, 50], [60, 70]],slots2 = [[5, 15], [25, 35], [45, 55], [65, 75]],duration = 10) == []
    assert candidate(slots1 = [[1, 2], [3, 4], [5, 6]],slots2 = [[1, 2], [3, 4], [5, 6]],duration = 1) == [1, 2]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 15], [55, 65], [145, 205]],duration = 8) == [145, 153]
    assert candidate(slots1 = [[10, 50], [60, 120], [140, 210]],slots2 = [[5, 55], [55, 65], [65, 75]],duration = 10) == [10, 20]


