def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 9],k = 3) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 9],k = 3) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],k = 1) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],k = 1) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 1) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 1) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 4) == 20.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 4) == 20.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 7, 5, 6, 2, 3],k = 4) == 18.166666666666664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 7, 5, 6, 2, 3],k = 4) == 18.166666666666664: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 5) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 5) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 1) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 1) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 3) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 3) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],k = 2) == 4.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],k = 2) == 4.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400],k = 2) == 600.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400],k = 2) == 600.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 7) == 28.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 7) == 28.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],k = 2) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],k = 2) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 9, 2],k = 3) == 16.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 9, 2],k = 3) == 16.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 37.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 37.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 8) == 125.17647058823529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 8) == 125.17647058823529: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 8) == 265.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 8) == 265.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 37.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 37.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 2) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 2) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 3) == 360.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 3) == 360.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 36.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 36.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 10) == 1000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 10) == 1000.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 15) == 660.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 15) == 660.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9],k = 3) == 21.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9],k = 3) == 21.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 375.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 375.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 4, 8, 9, 1, 2],k = 3) == 16.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 4, 8, 9, 1, 2],k = 3) == 16.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 1, 10, 100, 100, 1, 10, 100, 100, 1, 10, 100],k = 5) == 370.14285714285717
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 1, 10, 100, 100, 1, 10, 100, 100, 1, 10, 100],k = 5) == 370.14285714285717: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 6) == 950.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 6) == 950.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 3) == 1102222.2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 3) == 1102222.2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3],k = 4) == 23.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3],k = 4) == 23.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],k = 3) == 32.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],k = 3) == 32.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 102.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 102.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 60.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 60.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 5) == 18.333333333333332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 5) == 18.333333333333332: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 1, 0, 1, 10, 100, 1000, 10000],k = 4) == 12031.714285714286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 1, 0, 1, 10, 100, 1000, 10000],k = 4) == 12031.714285714286: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 8) == 1260.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 8) == 1260.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 4, 3, 8, 7, 5, 6, 2],k = 4) == 24.666666666666664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 4, 3, 8, 7, 5, 6, 2],k = 4) == 24.666666666666664: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 375.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 375.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 20) == 405.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 20) == 405.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 5) == 81.66666666666667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 5) == 81.66666666666667: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 9, 2, 6, 7],k = 3) == 18.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 9, 2, 6, 7],k = 3) == 18.25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10],k = 3) == 23.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10],k = 3) == 23.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 35.0625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 35.0625: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 33.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 33.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 5) == 50000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 5) == 50000.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 9, 5, 7, 8],k = 3) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 9, 5, 7, 8],k = 3) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],k = 5) == 49987.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],k = 5) == 49987.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 6, 2, 3, 4, 5, 1, 2],k = 4) == 15.333333333333334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 6, 2, 3, 4, 5, 1, 2],k = 4) == 15.333333333333334: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 2) == 750.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 2) == 750.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9],k = 3) == 21.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9],k = 3) == 21.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 5500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 5500.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 1, 8, 4, 9],k = 2) == 13.8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 1, 8, 4, 9],k = 2) == 13.8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 82.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 82.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 235.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 235.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 80.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 80.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 318.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 318.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 120.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 120.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1],k = 7) == 24.32857142857143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1],k = 7) == 24.32857142857143: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 2) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 2) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7],k = 3) == 18.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7],k = 3) == 18.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 23.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 23.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3],k = 6) == 34.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3],k = 6) == 34.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 3750.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 3750.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 100, 3, 100, 4, 100, 5, 100],k = 5) == 322.49999999999994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 100, 3, 100, 4, 100, 5, 100],k = 5) == 322.49999999999994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 3) == 30000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 3) == 30000.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 58.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 58.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 937.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 937.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 21.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 21.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 9, 8, 7, 6, 5, 4],k = 5) == 33.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 9, 8, 7, 6, 5, 4],k = 5) == 33.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 10) == 670.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 10) == 670.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 20) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 20) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 15.0
    assert candidate(nums = [9, 1, 2, 3, 9],k = 3) == 20.0
    assert candidate(nums = [1, 2, 3],k = 1) == 2.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 1) == 4.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 4) == 20.5
    assert candidate(nums = [4, 1, 7, 5, 6, 2, 3],k = 4) == 18.166666666666664
    assert candidate(nums = [10, 20, 30, 40, 50],k = 5) == 150.0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1) == 5.0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 50.0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 3) == 15.0
    assert candidate(nums = [1, 2, 3],k = 2) == 4.5
    assert candidate(nums = [100, 200, 300, 400],k = 2) == 600.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 7) == 28.0
    assert candidate(nums = [1, 2, 3, 4],k = 2) == 6.0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 27.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55.0
    assert candidate(nums = [5, 3, 8, 1, 9, 2],k = 3) == 16.0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 37.5
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 8) == 125.17647058823529
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 8) == 265.5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 37.5
    assert candidate(nums = [10, 20, 30, 40, 50],k = 2) == 75.0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 3) == 360.0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 36.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 10) == 1000.0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 15) == 660.0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50.0
    assert candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9],k = 3) == 21.0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 375.0
    assert candidate(nums = [5, 3, 6, 4, 8, 9, 1, 2],k = 3) == 16.5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 15.0
    assert candidate(nums = [100, 10, 1, 10, 100, 100, 1, 10, 100, 100, 1, 10, 100],k = 5) == 370.14285714285717
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1.0
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 6) == 950.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 5.5
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 3) == 1102222.2
    assert candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3],k = 4) == 23.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5.0
    assert candidate(nums = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],k = 3) == 32.5
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 102.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 60.0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 5) == 18.333333333333332
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3.0
    assert candidate(nums = [15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 55.0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 75.0
    assert candidate(nums = [1000, 100, 10, 1, 0, 1, 10, 100, 1000, 10000],k = 4) == 12031.714285714286
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3.0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 8) == 1260.0
    assert candidate(nums = [9, 1, 4, 3, 8, 7, 5, 6, 2],k = 4) == 24.666666666666664
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 375.0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 5.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 20) == 405.0
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 5) == 81.66666666666667
    assert candidate(nums = [5, 3, 8, 1, 9, 2, 6, 7],k = 3) == 18.25
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10],k = 3) == 23.5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 35.0625
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 33.0
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 5) == 50000.0
    assert candidate(nums = [9, 1, 2, 3, 9, 5, 7, 8],k = 3) == 21.5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 50.0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 25.0
    assert candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],k = 5) == 49987.5
    assert candidate(nums = [4, 3, 2, 6, 2, 3, 4, 5, 1, 2],k = 4) == 15.333333333333334
    assert candidate(nums = [100, 200, 300, 400, 500],k = 2) == 750.0
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9],k = 3) == 21.5
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 5500.0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 55.0
    assert candidate(nums = [5, 6, 1, 8, 4, 9],k = 2) == 13.8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 82.5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 235.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 80.0
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 318.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 120.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 15.0
    assert candidate(nums = [5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1, 5, 2, 3, 1],k = 7) == 24.32857142857143
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 2) == 15.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 22.5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2) == 150.0
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7],k = 3) == 18.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 23.5
    assert candidate(nums = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3],k = 6) == 34.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 150.0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 3750.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10.0
    assert candidate(nums = [1, 100, 2, 100, 3, 100, 4, 100, 5, 100],k = 5) == 322.49999999999994
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 3) == 30000.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 150.0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 58.0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1500.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 937.5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 21.0
    assert candidate(nums = [9, 1, 2, 3, 9, 8, 7, 6, 5, 4],k = 5) == 33.5
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 10) == 670.0
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 20) == 180.0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 45.0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50.0


