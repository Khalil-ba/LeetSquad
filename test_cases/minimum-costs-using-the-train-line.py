def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1],express = [1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1],express = [1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30],express = [5, 15, 25],expressCost = 2) == [7, 22, 47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30],express = [5, 15, 25],expressCost = 2) == [7, 22, 47]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8],express = [1, 3, 5, 7],expressCost = 10) == [2, 6, 12, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8],express = [1, 3, 5, 7],expressCost = 10) == [2, 6, 12, 20]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30],express = [5, 15, 25],expressCost = 10) == [10, 30, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30],express = [5, 15, 25],expressCost = 10) == [10, 30, 55]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5],express = [10, 10, 10],expressCost = 1) == [5, 10, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5],express = [10, 10, 10],expressCost = 1) == [5, 10, 15]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5],express = [10],expressCost = 7) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5],express = [10],expressCost = 7) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8],express = [1, 3, 5, 7],expressCost = 5) == [2, 6, 12, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8],express = [1, 3, 5, 7],expressCost = 5) == [2, 6, 12, 20]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 2, 3, 4, 5],express = [5, 4, 3, 2, 1],expressCost = 10) == [1, 3, 6, 10, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 2, 3, 4, 5],express = [5, 4, 3, 2, 1],expressCost = 10) == [1, 3, 6, 10, 15]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300],express = [150, 250, 350],expressCost = 10) == [100, 300, 600]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300],express = [150, 250, 350],expressCost = 10) == [100, 300, 600]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 6, 9, 5],express = [5, 2, 3, 10],expressCost = 8) == [1, 7, 14, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 6, 9, 5],express = [5, 2, 3, 10],expressCost = 8) == [1, 7, 14, 19]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15],express = [3, 6, 9],expressCost = 5) == [5, 14, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15],express = [3, 6, 9],expressCost = 5) == [5, 14, 23]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [3, 3, 3],express = [1, 1, 1],expressCost = 5) == [3, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [3, 3, 3],express = [1, 1, 1],expressCost = 5) == [3, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30],express = [15, 25, 35],expressCost = 10) == [10, 30, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30],express = [15, 25, 35],expressCost = 10) == [10, 30, 60]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [3, 3, 3],express = [4, 4, 4],expressCost = 5) == [3, 6, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [3, 3, 3],express = [4, 4, 4],expressCost = 5) == [3, 6, 9]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [11, 5, 13],express = [7, 10, 6],expressCost = 3) == [10, 15, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [11, 5, 13],express = [7, 10, 6],expressCost = 3) == [10, 15, 24]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],expressCost = 10) == [5, 10, 15, 20, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],expressCost = 10) == [5, 10, 15, 20, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 150) == [100, 153, 156, 160, 165, 171, 178, 186, 195, 205]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 150) == [100, 153, 156, 160, 165, 171, 178, 186, 195, 205]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100000, 100000, 100000],express = [100000, 100000, 100000],expressCost = 1) == [100000, 200000, 300000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100000, 100000, 100000],express = [100000, 100000, 100000],expressCost = 1) == [100000, 200000, 300000]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 10) == [5, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 10) == [5, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 5) == [10, 30, 60, 85, 95]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 5) == [10, 30, 60, 85, 95]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],express = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],expressCost = 15) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 112, 119, 124, 127, 128]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],express = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],expressCost = 15) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 112, 119, 124, 127, 128]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100000, 100000, 100000],express = [1, 1, 1],expressCost = 100000) == [100000, 100002, 100003]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100000, 100000, 100000],express = [1, 1, 1],expressCost = 100000) == [100000, 100002, 100003]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50],express = [5, 15, 25, 35, 45],expressCost = 20) == [10, 30, 60, 100, 145]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50],express = [5, 15, 25, 35, 45],expressCost = 20) == [10, 30, 60, 100, 145]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 15) == [1, 4, 9, 16, 25, 36, 46, 49, 51, 52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 15) == [1, 4, 9, 16, 25, 36, 46, 49, 51, 52]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 25) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 25) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],express = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],expressCost = 20) == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],express = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],expressCost = 20) == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 5) == [10, 30, 60, 85, 95]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 5) == [10, 30, 60, 85, 95]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],express = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],expressCost = 50) == [55, 70, 95, 130, 175, 225, 265, 295, 315, 325]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],express = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],expressCost = 50) == [55, 70, 95, 130, 175, 225, 265, 295, 315, 325]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 1) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 1) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 15) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 104, 110, 115, 119, 122, 124, 125]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 15) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 104, 110, 115, 119, 122, 124, 125]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],express = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3],expressCost = 25) == [3, 9, 18, 30, 45, 63, 84, 106, 112, 115]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],express = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3],expressCost = 25) == [3, 9, 18, 30, 45, 63, 84, 106, 112, 115]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 20) == [10, 30, 60, 100, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 20) == [10, 30, 60, 100, 110]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],expressCost = 500) == [100, 300, 600, 1000, 1500, 2100, 2800, 3200, 3400, 3500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],expressCost = 500) == [100, 300, 600, 1000, 1500, 2100, 2800, 3200, 3400, 3500]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 15) == [9, 18, 21, 25, 30, 36, 43, 51, 60, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 15) == [9, 18, 21, 25, 30, 36, 43, 51, 60, 70]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8, 10, 12, 14],express = [1, 3, 5, 7, 9, 11, 13],expressCost = 7) == [2, 6, 12, 20, 30, 42, 56]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8, 10, 12, 14],express = [1, 3, 5, 7, 9, 11, 13],expressCost = 7) == [2, 6, 12, 20, 30, 42, 56]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5],express = [2, 2, 2, 2, 2, 2],expressCost = 10) == [5, 10, 15, 18, 20, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5],express = [2, 2, 2, 2, 2, 2],expressCost = 10) == [5, 10, 15, 18, 20, 22]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500],express = [500, 400, 300, 200, 100],expressCost = 100) == [100, 300, 600, 900, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500],express = [500, 400, 300, 200, 100],expressCost = 100) == [100, 300, 600, 900, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 1) == [2, 4, 7, 11, 16, 21, 26, 31, 36, 41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 1) == [2, 4, 7, 11, 16, 21, 26, 31, 36, 41]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 15) == [10, 30, 60, 95, 105]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 15) == [10, 30, 60, 95, 105]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5],express = [5, 5, 5, 5, 5],expressCost = 2) == [5, 10, 15, 20, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5],express = [5, 5, 5, 5, 5],expressCost = 2) == [5, 10, 15, 20, 25]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],express = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2],expressCost = 10) == [2, 5, 10, 17, 28, 41, 56, 61, 64, 66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],express = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2],expressCost = 10) == [2, 5, 10, 17, 28, 41, 56, 61, 64, 66]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500],express = [1, 2, 3, 4, 5],expressCost = 500) == [100, 300, 506, 510, 515]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500],express = [1, 2, 3, 4, 5],expressCost = 500) == [100, 300, 506, 510, 515]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 2) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 2) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5],expressCost = 15) == [5, 15, 30, 40, 50, 55, 65, 70, 80, 85]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5],expressCost = 15) == [5, 15, 30, 40, 50, 55, 65, 70, 80, 85]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8, 10],express = [10, 8, 6, 4, 2],expressCost = 5) == [2, 6, 12, 20, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8, 10],express = [10, 8, 6, 4, 2],expressCost = 5) == [2, 6, 12, 20, 23]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],express = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 5) == [1, 3, 6, 10, 15, 21, 28, 32, 34, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],express = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 5) == [1, 3, 6, 10, 15, 21, 28, 32, 34, 35]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 320, 340, 350]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 320, 340, 350]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 10, 10, 10, 10],express = [9, 9, 9, 9, 9],expressCost = 1) == [10, 19, 28, 37, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 10, 10, 10, 10],express = [9, 9, 9, 9, 9],expressCost = 1) == [10, 19, 28, 37, 46]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25],express = [25, 20, 15, 10, 5],expressCost = 20) == [5, 15, 30, 50, 65]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25],express = [25, 20, 15, 10, 5],expressCost = 20) == [5, 15, 30, 50, 65]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [3, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [3, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500],express = [1000, 1000, 1000, 1000, 1000],expressCost = 999) == [100, 300, 600, 1000, 1500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500],express = [1000, 1000, 1000, 1000, 1000],expressCost = 999) == [100, 300, 600, 1000, 1500]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500],express = [1, 2, 3, 4, 5],expressCost = 1000) == [100, 300, 600, 1000, 1015]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500],express = [1, 2, 3, 4, 5],expressCost = 1000) == [100, 300, 600, 1000, 1015]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 50) == [51, 53, 56, 60, 65, 71, 78, 86, 95, 105]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 50) == [51, 53, 56, 60, 65, 71, 78, 86, 95, 105]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 545]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 545]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 5) == [6, 8, 11, 15, 20, 25, 29, 32, 34, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 5) == [6, 8, 11, 15, 20, 25, 29, 32, 34, 35]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],expressCost = 20) == [5, 15, 30, 50, 75, 105, 140, 180, 225, 275]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],expressCost = 20) == [5, 15, 30, 50, 75, 105, 140, 180, 225, 275]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 10, 100, 1000, 10000],express = [10000, 1000, 100, 10, 1],expressCost = 5000) == [1, 11, 111, 1111, 5122]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 10, 100, 1000, 10000],express = [10000, 1000, 100, 10, 1],expressCost = 5000) == [1, 11, 111, 1111, 5122]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 10) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 99, 105, 110, 114, 117, 119, 120]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 10) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 99, 105, 110, 114, 117, 119, 120]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25],express = [10, 20, 30, 40, 50],expressCost = 20) == [5, 15, 30, 50, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25],express = [10, 20, 30, 40, 50],expressCost = 20) == [5, 15, 30, 50, 75]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],express = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],expressCost = 1) == [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],express = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],expressCost = 1) == [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400],express = [1, 2, 3, 4],expressCost = 100) == [100, 103, 106, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400],express = [1, 2, 3, 4],expressCost = 100) == [100, 103, 106, 110]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [45, 40, 35, 30, 25, 20, 15, 10, 5, 1],expressCost = 25) == [5, 15, 30, 50, 75, 105, 135, 145, 150, 151]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [45, 40, 35, 30, 25, 20, 15, 10, 5, 1],expressCost = 25) == [5, 15, 30, 50, 75, 105, 135, 145, 150, 151]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25],express = [25, 20, 15, 10, 5],expressCost = 100) == [5, 15, 30, 50, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25],express = [25, 20, 15, 10, 5],expressCost = 100) == [5, 15, 30, 50, 75]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],expressCost = 5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],expressCost = 5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [7, 14, 21, 28, 35, 42],express = [42, 35, 28, 21, 14, 7],expressCost = 21) == [7, 21, 42, 70, 98, 105]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [7, 14, 21, 28, 35, 42],express = [42, 35, 28, 21, 14, 7],expressCost = 21) == [7, 21, 42, 70, 98, 105]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],expressCost = 200) == [100, 215, 230, 250, 275, 305, 340, 380, 425, 475]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],expressCost = 200) == [100, 215, 230, 250, 275, 305, 340, 380, 425, 475]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 20) == [5, 15, 30, 40, 50, 62, 76, 92, 110, 130]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 20) == [5, 15, 30, 40, 50, 62, 76, 92, 110, 130]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 100) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 100) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],express = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],expressCost = 15) == [2, 6, 12, 20, 30, 42, 56, 69, 73, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],express = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],expressCost = 15) == [2, 6, 12, 20, 30, 42, 56, 69, 73, 75]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 320, 340, 350]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 320, 340, 350]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],express = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],expressCost = 1) == [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],express = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],expressCost = 1) == [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100000, 100000, 100000, 100000, 100000],express = [1, 1, 1, 1, 1],expressCost = 50000) == [50001, 50002, 50003, 50004, 50005]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100000, 100000, 100000, 100000, 100000],express = [1, 1, 1, 1, 1],expressCost = 50000) == [50001, 50002, 50003, 50004, 50005]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 3, 5, 7, 11, 13],express = [13, 11, 7, 5, 3, 2],expressCost = 20) == [2, 5, 10, 17, 28, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 3, 5, 7, 11, 13],express = [13, 11, 7, 5, 3, 2],expressCost = 20) == [2, 5, 10, 17, 28, 40]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [100, 200, 300, 400, 500],express = [50, 100, 150, 200, 250],expressCost = 1000) == [100, 300, 600, 1000, 1500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [100, 200, 300, 400, 500],express = [50, 100, 150, 200, 250],expressCost = 1000) == [100, 300, 600, 1000, 1500]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [3, 6, 9, 12, 15, 18],express = [18, 15, 12, 9, 6, 3],expressCost = 15) == [3, 9, 18, 30, 45, 51]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [3, 6, 9, 12, 15, 18],express = [18, 15, 12, 9, 6, 3],expressCost = 15) == [3, 9, 18, 30, 45, 51]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 20) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 20) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50],express = [5, 15, 25, 35, 45],expressCost = 5) == [10, 25, 50, 85, 130]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50],express = [5, 15, 25, 35, 45],expressCost = 5) == [10, 25, 50, 85, 130]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [2, 4, 6, 8, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [2, 4, 6, 8, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 15) == [3, 9, 18, 25, 30, 36, 43, 51, 60, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 15) == [3, 9, 18, 25, 30, 36, 43, 51, 60, 70]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],express = [40, 36, 32, 28, 24, 20, 16, 12, 8, 4],expressCost = 150) == [4, 12, 24, 40, 60, 84, 112, 144, 180, 220]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],express = [40, 36, 32, 28, 24, 20, 16, 12, 8, 4],expressCost = 150) == [4, 12, 24, 40, 60, 84, 112, 144, 180, 220]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 25) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 25) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]: {e}')
    
    total += 1
    try:
        result = candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 50) == [10, 30, 56, 60, 65, 71, 78, 86, 95, 105]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 50) == [10, 30, 56, 60, 65, 71, 78, 86, 95, 105]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(regular = [1, 1, 1, 1],express = [1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4]
    assert candidate(regular = [10, 20, 30],express = [5, 15, 25],expressCost = 2) == [7, 22, 47]
    assert candidate(regular = [2, 4, 6, 8],express = [1, 3, 5, 7],expressCost = 10) == [2, 6, 12, 20]
    assert candidate(regular = [10, 20, 30],express = [5, 15, 25],expressCost = 10) == [10, 30, 55]
    assert candidate(regular = [5, 5, 5],express = [10, 10, 10],expressCost = 1) == [5, 10, 15]
    assert candidate(regular = [5],express = [10],expressCost = 7) == [5]
    assert candidate(regular = [2, 4, 6, 8],express = [1, 3, 5, 7],expressCost = 5) == [2, 6, 12, 20]
    assert candidate(regular = [1, 2, 3, 4, 5],express = [5, 4, 3, 2, 1],expressCost = 10) == [1, 3, 6, 10, 15]
    assert candidate(regular = [100, 200, 300],express = [150, 250, 350],expressCost = 10) == [100, 300, 600]
    assert candidate(regular = [1, 6, 9, 5],express = [5, 2, 3, 10],expressCost = 8) == [1, 7, 14, 19]
    assert candidate(regular = [5, 10, 15],express = [3, 6, 9],expressCost = 5) == [5, 14, 23]
    assert candidate(regular = [3, 3, 3],express = [1, 1, 1],expressCost = 5) == [3, 6, 8]
    assert candidate(regular = [10, 20, 30],express = [15, 25, 35],expressCost = 10) == [10, 30, 60]
    assert candidate(regular = [3, 3, 3],express = [4, 4, 4],expressCost = 5) == [3, 6, 9]
    assert candidate(regular = [11, 5, 13],express = [7, 10, 6],expressCost = 3) == [10, 15, 24]
    assert candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],expressCost = 10) == [5, 10, 15, 20, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55]
    assert candidate(regular = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 150) == [100, 153, 156, 160, 165, 171, 178, 186, 195, 205]
    assert candidate(regular = [100000, 100000, 100000],express = [100000, 100000, 100000],expressCost = 1) == [100000, 200000, 300000]
    assert candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 10) == [5, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    assert candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 5) == [10, 30, 60, 85, 95]
    assert candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],express = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],expressCost = 15) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 112, 119, 124, 127, 128]
    assert candidate(regular = [100000, 100000, 100000],express = [1, 1, 1],expressCost = 100000) == [100000, 100002, 100003]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(regular = [10, 20, 30, 40, 50],express = [5, 15, 25, 35, 45],expressCost = 20) == [10, 30, 60, 100, 145]
    assert candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 15) == [1, 4, 9, 16, 25, 36, 46, 49, 51, 52]
    assert candidate(regular = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 25) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
    assert candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],express = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],expressCost = 20) == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420]
    assert candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 5) == [10, 30, 60, 85, 95]
    assert candidate(regular = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],express = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],expressCost = 50) == [55, 70, 95, 130, 175, 225, 265, 295, 315, 325]
    assert candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 1) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 15) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 104, 110, 115, 119, 122, 124, 125]
    assert candidate(regular = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],express = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3],expressCost = 25) == [3, 9, 18, 30, 45, 63, 84, 106, 112, 115]
    assert candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 20) == [10, 30, 60, 100, 110]
    assert candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],expressCost = 500) == [100, 300, 600, 1000, 1500, 2100, 2800, 3200, 3400, 3500]
    assert candidate(regular = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 15) == [9, 18, 21, 25, 30, 36, 43, 51, 60, 70]
    assert candidate(regular = [2, 4, 6, 8, 10, 12, 14],express = [1, 3, 5, 7, 9, 11, 13],expressCost = 7) == [2, 6, 12, 20, 30, 42, 56]
    assert candidate(regular = [5, 5, 5, 5, 5, 5],express = [2, 2, 2, 2, 2, 2],expressCost = 10) == [5, 10, 15, 18, 20, 22]
    assert candidate(regular = [100, 200, 300, 400, 500],express = [500, 400, 300, 200, 100],expressCost = 100) == [100, 300, 600, 900, 1000]
    assert candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 1) == [2, 4, 7, 11, 16, 21, 26, 31, 36, 41]
    assert candidate(regular = [10, 20, 30, 40, 50],express = [50, 40, 30, 20, 10],expressCost = 15) == [10, 30, 60, 95, 105]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(regular = [5, 5, 5, 5, 5],express = [5, 5, 5, 5, 5],expressCost = 2) == [5, 10, 15, 20, 25]
    assert candidate(regular = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],express = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2],expressCost = 10) == [2, 5, 10, 17, 28, 41, 56, 61, 64, 66]
    assert candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert candidate(regular = [100, 200, 300, 400, 500],express = [1, 2, 3, 4, 5],expressCost = 500) == [100, 300, 506, 510, 515]
    assert candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 2) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5],expressCost = 15) == [5, 15, 30, 40, 50, 55, 65, 70, 80, 85]
    assert candidate(regular = [1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(regular = [2, 4, 6, 8, 10],express = [10, 8, 6, 4, 2],expressCost = 5) == [2, 6, 12, 20, 23]
    assert candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],express = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 5) == [1, 3, 6, 10, 15, 21, 28, 32, 34, 35]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 320, 340, 350]
    assert candidate(regular = [10, 10, 10, 10, 10],express = [9, 9, 9, 9, 9],expressCost = 1) == [10, 19, 28, 37, 46]
    assert candidate(regular = [5, 10, 15, 20, 25],express = [25, 20, 15, 10, 5],expressCost = 20) == [5, 15, 30, 50, 65]
    assert candidate(regular = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [3, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(regular = [100, 200, 300, 400, 500],express = [1000, 1000, 1000, 1000, 1000],expressCost = 999) == [100, 300, 600, 1000, 1500]
    assert candidate(regular = [100, 200, 300, 400, 500],express = [1, 2, 3, 4, 5],expressCost = 1000) == [100, 300, 600, 1000, 1015]
    assert candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 50) == [51, 53, 56, 60, 65, 71, 78, 86, 95, 105]
    assert candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 545]
    assert candidate(regular = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 5) == [6, 8, 11, 15, 20, 25, 29, 32, 34, 35]
    assert candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],expressCost = 20) == [5, 15, 30, 50, 75, 105, 140, 180, 225, 275]
    assert candidate(regular = [1, 10, 100, 1000, 10000],express = [10000, 1000, 100, 10, 1],expressCost = 5000) == [1, 11, 111, 1111, 5122]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 10) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 99, 105, 110, 114, 117, 119, 120]
    assert candidate(regular = [5, 10, 15, 20, 25],express = [10, 20, 30, 40, 50],expressCost = 20) == [5, 15, 30, 50, 75]
    assert candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],express = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],expressCost = 1) == [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]
    assert candidate(regular = [100, 200, 300, 400],express = [1, 2, 3, 4],expressCost = 100) == [100, 103, 106, 110]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [45, 40, 35, 30, 25, 20, 15, 10, 5, 1],expressCost = 25) == [5, 15, 30, 50, 75, 105, 135, 145, 150, 151]
    assert candidate(regular = [5, 10, 15, 20, 25],express = [25, 20, 15, 10, 5],expressCost = 100) == [5, 15, 30, 50, 75]
    assert candidate(regular = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],express = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],expressCost = 5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(regular = [7, 14, 21, 28, 35, 42],express = [42, 35, 28, 21, 14, 7],expressCost = 21) == [7, 21, 42, 70, 98, 105]
    assert candidate(regular = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],express = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],expressCost = 200) == [100, 215, 230, 250, 275, 305, 340, 380, 425, 475]
    assert candidate(regular = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 20) == [5, 15, 30, 40, 50, 62, 76, 92, 110, 130]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],expressCost = 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],express = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],expressCost = 100) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
    assert candidate(regular = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],express = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],expressCost = 15) == [2, 6, 12, 20, 30, 42, 56, 69, 73, 75]
    assert candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],expressCost = 50) == [10, 30, 60, 100, 150, 210, 280, 320, 340, 350]
    assert candidate(regular = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],express = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],expressCost = 1) == [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
    assert candidate(regular = [100000, 100000, 100000, 100000, 100000],express = [1, 1, 1, 1, 1],expressCost = 50000) == [50001, 50002, 50003, 50004, 50005]
    assert candidate(regular = [2, 3, 5, 7, 11, 13],express = [13, 11, 7, 5, 3, 2],expressCost = 20) == [2, 5, 10, 17, 28, 40]
    assert candidate(regular = [100, 200, 300, 400, 500],express = [50, 100, 150, 200, 250],expressCost = 1000) == [100, 300, 600, 1000, 1500]
    assert candidate(regular = [3, 6, 9, 12, 15, 18],express = [18, 15, 12, 9, 6, 3],expressCost = 15) == [3, 9, 18, 30, 45, 51]
    assert candidate(regular = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(regular = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 20) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert candidate(regular = [10, 20, 30, 40, 50],express = [5, 15, 25, 35, 45],expressCost = 5) == [10, 25, 50, 85, 130]
    assert candidate(regular = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],express = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],expressCost = 5) == [2, 4, 6, 8, 10, 11, 12, 13, 14, 15]
    assert candidate(regular = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 15) == [3, 9, 18, 25, 30, 36, 43, 51, 60, 70]
    assert candidate(regular = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],express = [40, 36, 32, 28, 24, 20, 16, 12, 8, 4],expressCost = 150) == [4, 12, 24, 40, 60, 84, 112, 144, 180, 220]
    assert candidate(regular = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],express = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],expressCost = 25) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert candidate(regular = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],express = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],expressCost = 50) == [10, 30, 56, 60, 65, 71, 78, 86, 95, 105]


