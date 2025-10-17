def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(slices = [9, 7, 7, 7, 6, 6]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 7, 7, 7, 6, 6]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1000, 1000, 1000, 1000, 1000, 1000]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1000, 1000, 1000, 1000, 1000, 1000]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 1, 1, 1, 1, 1, 1, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 1, 1, 1, 1, 1, 1, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(slices = [8, 9, 8, 6, 1, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [8, 9, 8, 6, 1, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 1, 1, 1, 1, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 1, 1, 1, 1, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(slices = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(slices = [7, 8, 9, 1, 2, 3, 4, 5, 6]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [7, 8, 9, 1, 2, 3, 4, 5, 6]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(slices = [7, 7, 7, 7, 7, 7, 7]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [7, 7, 7, 7, 7, 7, 7]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1000, 1, 1000, 1, 1000, 1]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1000, 1, 1000, 1, 1000, 1]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 7, 8, 6, 3, 4]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 7, 8, 6, 3, 4]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 3, 1, 5, 2, 5, 1, 5, 6]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 3, 1, 5, 2, 5, 1, 5, 6]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 798: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000, 6, 1000]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000, 6, 1000]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 3, 9, 7, 1, 4, 8, 6, 2, 10, 12, 11]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 3, 9, 7, 1, 4, 8, 6, 2, 10, 12, 11]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(slices = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5, 500, 6]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5, 500, 6]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 200, 300, 400, 500, 600, 100, 200, 300, 400, 500, 600]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 200, 300, 400, 500, 600, 100, 200, 300, 400, 500, 600]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(slices = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800]) == 3200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800]) == 3200: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6]) == 394
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6]) == 394: {e}')
    
    total += 1
    try:
        result = candidate(slices = [900, 100, 200, 300, 400, 500, 600, 700, 800, 100, 200, 300, 400, 500, 600, 700, 800, 900, 100, 200, 300, 400, 500, 600, 700]) == 5400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [900, 100, 200, 300, 400, 500, 600, 700, 800, 100, 200, 300, 400, 500, 600, 700, 800, 900, 100, 200, 300, 400, 500, 600, 700]) == 5400: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 1, 15, 2, 20, 3, 25, 4, 30, 5, 35, 6]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 1, 15, 2, 20, 3, 25, 4, 30, 5, 35, 6]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(slices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(slices = [300, 200, 100, 50, 25, 12, 6, 3, 1, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 3450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [300, 200, 100, 50, 25, 12, 6, 3, 1, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 3450: {e}')
    
    total += 1
    try:
        result = candidate(slices = [15, 1, 25, 3, 20, 4, 2, 30, 5, 6, 7, 8]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [15, 1, 25, 3, 20, 4, 2, 30, 5, 6, 7, 8]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995]) == 3994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995]) == 3994: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 2278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 2278: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]) == 3485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]) == 3485: {e}')
    
    total += 1
    try:
        result = candidate(slices = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(slices = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 12, 11]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 12, 11]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(slices = [300, 1, 100, 2, 200, 3, 150, 4, 250, 5, 350, 6]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [300, 1, 100, 2, 200, 3, 150, 4, 250, 5, 350, 6]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(slices = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(slices = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [12, 3, 11, 4, 2, 5, 6, 7, 8, 9, 10, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [12, 3, 11, 4, 2, 5, 6, 7, 8, 9, 10, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2244: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(slices = [999, 1, 999, 2, 999, 3, 999, 4, 999, 5, 999, 6, 999, 7, 999, 8, 999, 9, 999, 10, 999, 11, 999, 12, 999, 13, 999, 14, 999, 15]) == 9990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [999, 1, 999, 2, 999, 3, 999, 4, 999, 5, 999, 6, 999, 7, 999, 8, 999, 9, 999, 10, 999, 11, 999, 12, 999, 13, 999, 14, 999, 15]) == 9990: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 2, 8, 1, 5, 6, 7, 3, 4, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 2, 8, 1, 5, 6, 7, 3, 4, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(slices = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 3996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 3996: {e}')
    
    total += 1
    try:
        result = candidate(slices = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5, 500, 6]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5, 500, 6]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [200, 150, 100, 50, 100, 150, 200, 250, 300, 350, 400, 450]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [200, 150, 100, 50, 100, 150, 200, 250, 300, 350, 400, 450]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(slices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 7, 4, 6, 10, 3, 8, 2, 9, 1, 11, 6]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 7, 4, 6, 10, 3, 8, 2, 9, 1, 11, 6]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(slices = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 97: {e}')
    
    total += 1
    try:
        result = candidate(slices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]) == 5600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]) == 5600: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 133: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 5, 1, 2, 8, 3, 9, 4, 7, 6, 11, 12]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 5, 1, 2, 8, 3, 9, 4, 7, 6, 11, 12]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(slices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(slices = [500, 1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6]) == 3994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [500, 1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6]) == 3994: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10, 11]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10, 11]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(slices = [900, 100, 800, 200, 700, 300, 600, 400, 500, 500, 600, 400]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [900, 100, 800, 200, 700, 300, 600, 400, 500, 500, 600, 400]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(slices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(slices = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]) == 2210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]) == 2210: {e}')
    
    total += 1
    try:
        result = candidate(slices = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(slices = [12, 3, 14, 5, 16, 7, 18, 9, 11, 2, 13, 4]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [12, 3, 14, 5, 16, 7, 18, 9, 11, 2, 13, 4]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(slices = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10, 1100, 11, 1200, 12]) == 6800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10, 1100, 11, 1200, 12]) == 6800: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(slices = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(slices = [10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(slices = [500, 300, 200, 400, 100, 600, 700, 800, 900, 100, 100, 100]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [500, 300, 200, 400, 100, 600, 700, 800, 900, 100, 100, 100]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(slices = [2, 5, 3, 4, 8, 1, 9, 7, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(slices = [2, 5, 3, 4, 8, 1, 9, 7, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(slices = [9, 7, 7, 7, 6, 6]) == 16
    assert candidate(slices = [1000, 1000, 1000, 1000, 1000, 1000]) == 2000
    assert candidate(slices = [10, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 21
    assert candidate(slices = [1, 2, 3, 4, 1, 2]) == 6
    assert candidate(slices = [8, 9, 8, 6, 1, 1]) == 16
    assert candidate(slices = [10, 1, 1, 1, 1, 10]) == 11
    assert candidate(slices = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36
    assert candidate(slices = [7, 8, 9, 1, 2, 3, 4, 5, 6]) == 21
    assert candidate(slices = [7, 7, 7, 7, 7, 7, 7]) == 14
    assert candidate(slices = [1000, 1, 1000, 1, 1000, 1]) == 2000
    assert candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(slices = [5, 7, 8, 6, 3, 4]) == 13
    assert candidate(slices = [1, 3, 1, 5, 2, 5, 1, 5, 6]) == 16
    assert candidate(slices = [1, 2, 3, 4, 5, 6]) == 10
    assert candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 2100
    assert candidate(slices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 798
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 78
    assert candidate(slices = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000, 6, 1000]) == 4000
    assert candidate(slices = [5, 3, 9, 7, 1, 4, 8, 6, 2, 10, 12, 11]) == 38
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(slices = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5, 500, 6]) == 2000
    assert candidate(slices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8]) == 280
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55
    assert candidate(slices = [100, 200, 300, 400, 500, 600, 100, 200, 300, 400, 500, 600]) == 2000
    assert candidate(slices = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) == 400
    assert candidate(slices = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800]) == 3200
    assert candidate(slices = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6]) == 394
    assert candidate(slices = [900, 100, 200, 300, 400, 500, 600, 700, 800, 100, 200, 300, 400, 500, 600, 700, 800, 900, 100, 200, 300, 400, 500, 600, 700]) == 5400
    assert candidate(slices = [10, 1, 15, 2, 20, 3, 25, 4, 30, 5, 35, 6]) == 110
    assert candidate(slices = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55
    assert candidate(slices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600
    assert candidate(slices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 144
    assert candidate(slices = [300, 200, 100, 50, 25, 12, 6, 3, 1, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 3450
    assert candidate(slices = [15, 1, 25, 3, 20, 4, 2, 30, 5, 6, 7, 8]) == 90
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 560
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35
    assert candidate(slices = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995]) == 3994
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 36
    assert candidate(slices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
    assert candidate(slices = [1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3600
    assert candidate(slices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 2278
    assert candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 550
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 144
    assert candidate(slices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 3600
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]) == 3485
    assert candidate(slices = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 2000
    assert candidate(slices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 30
    assert candidate(slices = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
    assert candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 360
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 36
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 12, 11]) == 35
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 23
    assert candidate(slices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 21000
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 144
    assert candidate(slices = [300, 1, 100, 2, 200, 3, 150, 4, 250, 5, 350, 6]) == 1100
    assert candidate(slices = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 64
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
    assert candidate(slices = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 5000
    assert candidate(slices = [12, 3, 11, 4, 2, 5, 6, 7, 8, 9, 10, 1]) == 41
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2244
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]) == 5050
    assert candidate(slices = [5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8, 5, 6, 3, 7, 4, 8]) == 75
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11]) == 36
    assert candidate(slices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
    assert candidate(slices = [999, 1, 999, 2, 999, 3, 999, 4, 999, 5, 999, 6, 999, 7, 999, 8, 999, 9, 999, 10, 999, 11, 999, 12, 999, 13, 999, 14, 999, 15]) == 9990
    assert candidate(slices = [9, 2, 8, 1, 5, 6, 7, 3, 4, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 60
    assert candidate(slices = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 3996
    assert candidate(slices = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5, 500, 6]) == 2000
    assert candidate(slices = [200, 150, 100, 50, 100, 150, 200, 250, 300, 350, 400, 450]) == 1200
    assert candidate(slices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 68
    assert candidate(slices = [5, 7, 4, 6, 10, 3, 8, 2, 9, 1, 11, 6]) == 38
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 560
    assert candidate(slices = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 1000
    assert candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 76
    assert candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 2100
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10]) == 55
    assert candidate(slices = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15]) == 39
    assert candidate(slices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 97
    assert candidate(slices = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(slices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 180
    assert candidate(slices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]) == 5600
    assert candidate(slices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 133
    assert candidate(slices = [10, 5, 1, 2, 8, 3, 9, 4, 7, 6, 11, 12]) == 38
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 55
    assert candidate(slices = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 50
    assert candidate(slices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(slices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 114
    assert candidate(slices = [500, 1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6]) == 3994
    assert candidate(slices = [1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10, 11]) == 127
    assert candidate(slices = [900, 100, 800, 200, 700, 300, 600, 400, 500, 500, 600, 400]) == 3000
    assert candidate(slices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 28
    assert candidate(slices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(slices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 8
    assert candidate(slices = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]) == 2210
    assert candidate(slices = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 560
    assert candidate(slices = [12, 3, 14, 5, 16, 7, 18, 9, 11, 2, 13, 4]) == 61
    assert candidate(slices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 10000
    assert candidate(slices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600
    assert candidate(slices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 90
    assert candidate(slices = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10, 1100, 11, 1200, 12]) == 6800
    assert candidate(slices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210
    assert candidate(slices = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 3600
    assert candidate(slices = [10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1]) == 31
    assert candidate(slices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(slices = [500, 300, 200, 400, 100, 600, 700, 800, 900, 100, 100, 100]) == 2500
    assert candidate(slices = [2, 5, 3, 4, 8, 1, 9, 7, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 210


