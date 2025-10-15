def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 5, 5, 5, 5, 5],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 5, 5, 5, 5, 5],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 3],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 3],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [4, 1, 2, 2, 7, 1, 3, 2],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [4, 1, 2, 2, 7, 1, 3, 2],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 3, 5, 1],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 3, 5, 1],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(weights = [4, 1, 5, 1, 2],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [4, 1, 5, 1, 2],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 5, 5, 5, 5, 5],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 5, 5, 5, 5, 5],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(weights = [4, 1, 5, 1, 2],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [4, 1, 5, 1, 2],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50],k = 4) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50],k = 4) == 60: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50],k = 2) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50],k = 2) == 60: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50],k = 2) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50],k = 2) == 60: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125],k = 5) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125],k = 5) == 560: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000000000, 500000000, 1000000000, 500000000, 1000000000],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000000000, 500000000, 1000000000, 500000000, 1000000000],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 96: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 15) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 15) == 280: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 100, 200, 100, 200, 100],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 100, 200, 100, 200, 100],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 180: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 3) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 3) == 280: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 4) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 4) == 300: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 4) == 122087790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 4) == 122087790: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],k = 4) == 12208779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],k = 4) == 12208779: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 6) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 6) == 700: {e}')
    
    total += 1
    try:
        result = candidate(weights = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 3) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 3) == 280: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 25) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 25) == 720: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 20) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 20) == 380: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10) == 18000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10) == 18000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [2, 3, 4, 1, 6, 7, 8],k = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [2, 3, 4, 1, 6, 7, 8],k = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 90: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 7) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 7) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 9) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 9) == 72: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 5) == 2777777775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 5) == 2777777775: {e}')
    
    total += 1
    try:
        result = candidate(weights = [2, 1, 3, 4, 5, 6, 7],k = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [2, 1, 3, 4, 5, 6, 7],k = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(weights = [500000000, 1, 500000000, 1, 500000000, 1, 500000000],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [500000000, 1, 500000000, 1, 500000000, 1, 500000000],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 6) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 6) == 50: {e}')
    
    total += 1
    try:
        result = candidate(weights = [20, 15, 10, 5, 1, 2, 3, 4, 5, 10, 15, 20],k = 4) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [20, 15, 10, 5, 1, 2, 3, 4, 5, 10, 15, 20],k = 4) == 81: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 1, 3, 8, 2, 9, 4, 7, 6, 10],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 1, 3, 8, 2, 9, 4, 7, 6, 10],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 1, 3, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 1, 3, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 144: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 80: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 800: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 400: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 6) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 6) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 3) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 3) == 28: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 320: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 960: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 6) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 6) == 39: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 1, 8, 2, 7, 3, 6, 4, 5],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 1, 8, 2, 7, 3, 6, 4, 5],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 2) == 1099999989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 2) == 1099999989: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 13) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 13) == 96: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 6) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 6) == 1400: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
    assert candidate(weights = [1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(weights = [5, 5, 5, 5, 5, 5],k = 4) == 0
    assert candidate(weights = [1, 3],k = 2) == 0
    assert candidate(weights = [4, 1, 2, 2, 7, 1, 3, 2],k = 3) == 10
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
    assert candidate(weights = [1, 3, 5, 1],k = 2) == 4
    assert candidate(weights = [4, 1, 5, 1, 2],k = 3) == 4
    assert candidate(weights = [5, 5, 5, 5, 5, 5],k = 2) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 4) == 30
    assert candidate(weights = [4, 1, 5, 1, 2],k = 3) == 4
    assert candidate(weights = [10, 20, 30, 40, 50],k = 4) == 60
    assert candidate(weights = [10, 20, 30, 40, 50],k = 2) == 60
    assert candidate(weights = [10, 20, 30, 40, 50],k = 2) == 60
    assert candidate(weights = [1, 2, 3, 4, 5],k = 3) == 8
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
    assert candidate(weights = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
    assert candidate(weights = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125],k = 5) == 560
    assert candidate(weights = [1000000000, 500000000, 1000000000, 500000000, 1000000000],k = 3) == 0
    assert candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 30
    assert candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 0
    assert candidate(weights = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 15) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 96
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 15) == 280
    assert candidate(weights = [100, 200, 100, 200, 100, 200, 100],k = 4) == 0
    assert candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 10) == 0
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 13) == 0
    assert candidate(weights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 8) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 180
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 4000
    assert candidate(weights = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 3) == 280
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 4) == 300
    assert candidate(weights = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 4) == 122087790
    assert candidate(weights = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],k = 4) == 12208779
    assert candidate(weights = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2],k = 7) == 0
    assert candidate(weights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 3) == 0
    assert candidate(weights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 6) == 700
    assert candidate(weights = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 3) == 280
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 1200
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 25) == 720
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 20) == 380
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10) == 18000
    assert candidate(weights = [2, 3, 4, 1, 6, 7, 8],k = 4) == 18
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 0
    assert candidate(weights = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],k = 4) == 0
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(weights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 20) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 90
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 7) == 6000
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 120
    assert candidate(weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 9) == 72
    assert candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 32
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(weights = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555, 666666666, 777777777, 888888888],k = 5) == 2777777775
    assert candidate(weights = [2, 1, 3, 4, 5, 6, 7],k = 4) == 19
    assert candidate(weights = [500000000, 1, 500000000, 1, 500000000, 1, 500000000],k = 3) == 0
    assert candidate(weights = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 6) == 50
    assert candidate(weights = [20, 15, 10, 5, 1, 2, 3, 4, 5, 10, 15, 20],k = 4) == 81
    assert candidate(weights = [5, 1, 3, 8, 2, 9, 4, 7, 6, 10],k = 3) == 19
    assert candidate(weights = [1, 2, 3, 4, 5],k = 1) == 0
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 0
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(weights = [5, 1, 3, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 144
    assert candidate(weights = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 6) == 0
    assert candidate(weights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 5) == 0
    assert candidate(weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 80
    assert candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 24
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 800
    assert candidate(weights = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],k = 3) == 0
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 400
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 6) == 4000
    assert candidate(weights = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 3) == 28
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 320
    assert candidate(weights = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5],k = 10) == 0
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 960
    assert candidate(weights = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 6) == 39
    assert candidate(weights = [9, 1, 8, 2, 7, 3, 6, 4, 5],k = 3) == 2
    assert candidate(weights = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 2) == 1099999989
    assert candidate(weights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995],k = 3) == 12
    assert candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 13) == 96
    assert candidate(weights = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 4) == 35
    assert candidate(weights = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 4) == 0
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 6) == 1400


