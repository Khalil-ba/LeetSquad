def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 10],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 8],k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 8],k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 3, 4, 7],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 3, 4, 7],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 3, 2, 18, 9, 12, 3, 6, 5, 0],k = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 3, 2, 18, 9, 12, 3, 6, 5, 0],k = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 6],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 6],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 8, 10],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 8, 10],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 8, 10],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 8, 10],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 3, 4, 2],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 3, 4, 2],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 50) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 50) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 10, 20, 40, 50, 60],k = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 10, 20, 40, 50, 60],k = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 3, 7, 8, 12],k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 3, 7, 8, 12],k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 15) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 15) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 15, 20, 25, 30],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 15, 20, 25, 30],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 799: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40],k = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40],k = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 50) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 50) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 20) == 410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 20) == 410: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56],k = 7) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56],k = 7) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 15, 17, 20, 22, 30],k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 15, 17, 20, 22, 30],k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 5) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 5) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 150) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 150) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 1000, 1500, 2000, 2500, 3000],k = 300) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 1000, 1500, 2000, 2500, 3000],k = 300) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],k = 500) == 8999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],k = 500) == 8999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 23, 45, 12, 19, 32, 55, 60, 48, 37, 28, 17, 7, 5, 3, 1, 2, 4, 6, 9, 11, 13, 15, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 46, 47, 49, 50],k = 8) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 23, 45, 12, 19, 32, 55, 60, 48, 37, 28, 17, 7, 5, 3, 1, 2, 4, 6, 9, 11, 13, 15, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 46, 47, 49, 50],k = 8) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 300) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 300) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 10, 5, 0, 20, 25],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 10, 5, 0, 20, 25],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 100, 1000, 10, 100000],k = 500) == 98990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 100, 1000, 10, 100000],k = 500) == 98990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000, 2, 9999, 3, 9998, 4, 9997],k = 5000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000, 2, 9999, 3, 9998, 4, 9997],k = 5000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 10) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 10) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 200, 150, 250],k = 75) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 200, 150, 250],k = 75) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 15, 17, 20, 22, 25, 27, 30],k = 10) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 15, 17, 20, 22, 25, 27, 30],k = 10) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 11, 12, 9, 10],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 11, 12, 9, 10],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],k = 15) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],k = 15) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 22, 35, 14, 7, 30],k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 22, 35, 14, 7, 30],k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],k = 20) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],k = 20) == 149: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220],k = 10) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220],k = 10) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 50, 250, 300],k = 75) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 50, 250, 300],k = 75) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 12, 78, 45, 90, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90],k = 30) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 12, 78, 45, 90, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90],k = 30) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2000, 3000, 4000, 5000, 6000],k = 100) == 5799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2000, 3000, 4000, 5000, 6000],k = 100) == 5799: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 4) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 4) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 11, 14, 7],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 11, 14, 7],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 10) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 10) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 60) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 60) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 0) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 0) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75],k = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75],k = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 25) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 25) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 15, 18, 22, 25, 28, 32, 35, 38, 42, 45, 48, 52, 55, 58, 62],k = 10) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 15, 18, 22, 25, 28, 32, 35, 38, 42, 45, 48, 52, 55, 58, 62],k = 10) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77],k = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77],k = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 4000, 3000, 2000, 1000],k = 1000) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 4000, 3000, 2000, 1000],k = 1000) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 15, 20, 25, 30, 35],k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 15, 20, 25, 30, 35],k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500],k = 25) == 449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500],k = 25) == 449: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 5) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 5) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 1, 8, 9, 10, 11, 12, 15, 20],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 1, 8, 9, 10, 11, 12, 15, 20],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 1, 2, 11, 5, 7, 3, 13, 9],k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 1, 2, 11, 5, 7, 3, 13, 9],k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 18, 20, 25, 30, 40, 50],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 18, 20, 25, 30, 40, 50],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 17, 13, 2, 8],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 17, 13, 2, 8],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 50) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 50) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 20) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 20) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500],k = 50) == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500],k = 50) == 399: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000],k = 2000) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000],k = 2000) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 7) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 7) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 10, 5, 11, 6, 9, 4, 12, 3, 7],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 10, 5, 11, 6, 9, 4, 12, 3, 7],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500],k = 20) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500],k = 20) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 300, 200, 400, 600, 700, 800, 900, 100],k = 50) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 300, 200, 400, 600, 700, 800, 900, 100],k = 50) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50],k = 7) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50],k = 7) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 15, 18, 3, 5, 7, 10, 12, 14],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 15, 18, 3, 5, 7, 10, 12, 14],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 9980],k = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 9980],k = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 15, 16, 23, 42],k = 5) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 15, 16, 23, 42],k = 5) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 16, 20, 24, 28],k = 7) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 16, 20, 24, 28],k = 7) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 30, 20, 40, 60, 70, 80, 90, 10],k = 15) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 30, 20, 40, 60, 70, 80, 90, 10],k = 15) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 1, 15, 17, 5, 13, 19, 9, 7, 11],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 1, 15, 17, 5, 13, 19, 9, 7, 11],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 75: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 10],k = 2) == 6
    assert candidate(nums = [1, 5, 8],k = 2) == 3
    assert candidate(nums = [6, 3, 4, 7],k = 3) == 4
    assert candidate(nums = [6, 3, 2, 18, 9, 12, 3, 6, 5, 0],k = 6) == 9
    assert candidate(nums = [4, 9, 6],k = 2) == 2
    assert candidate(nums = [1, 3, 6],k = 3) == 3
    assert candidate(nums = [7, 8, 8, 10],k = 3) == 3
    assert candidate(nums = [1],k = 0) == 0
    assert candidate(nums = [4, 1, 8, 10],k = 2) == 5
    assert candidate(nums = [6, 3, 4, 2],k = 1) == 2
    assert candidate(nums = [100, 200, 300, 400, 500],k = 50) == 300
    assert candidate(nums = [30, 10, 20, 40, 50, 60],k = 15) == 20
    assert candidate(nums = [10, 15, 3, 7, 8, 12],k = 4) == 6
    assert candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 1000) == 9
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3) == 12
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 15) == 80
    assert candidate(nums = [5, 8, 12, 15, 20, 25, 30],k = 10) == 15
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 799
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 18
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40],k = 5) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 50) == 90
    assert candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 20) == 410
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 8
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56],k = 7) == 35
    assert candidate(nums = [8, 10, 15, 17, 20, 22, 30],k = 10) == 14
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 70
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 5) == 47
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 9
    assert candidate(nums = [100, 200, 300, 400, 500],k = 150) == 200
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000],k = 300) == 1900
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 7
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 100) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 7
    assert candidate(nums = [1, 10, 100, 1000, 10000],k = 500) == 8999
    assert candidate(nums = [8, 23, 45, 12, 19, 32, 55, 60, 48, 37, 28, 17, 7, 5, 3, 1, 2, 4, 6, 9, 11, 13, 15, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 46, 47, 49, 50],k = 8) == 43
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 300) == 500
    assert candidate(nums = [15, 10, 5, 0, 20, 25],k = 10) == 15
    assert candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 1000) == 9
    assert candidate(nums = [10000, 100, 1000, 10, 100000],k = 500) == 98990
    assert candidate(nums = [1, 10000, 2, 9999, 3, 9998, 4, 9997],k = 5000) == 7
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 10) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 12
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5) == 18
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 150
    assert candidate(nums = [100, 50, 200, 150, 250],k = 75) == 100
    assert candidate(nums = [5, 8, 12, 15, 17, 20, 22, 25, 27, 30],k = 10) == 17
    assert candidate(nums = [8, 11, 12, 9, 10],k = 3) == 4
    assert candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],k = 15) == 250
    assert candidate(nums = [15, 22, 35, 14, 7, 30],k = 10) == 13
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 2) == 14
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],k = 20) == 149
    assert candidate(nums = [10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220],k = 10) == 190
    assert candidate(nums = [100, 200, 150, 50, 250, 300],k = 75) == 100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(nums = [10, 10, 10, 10, 10],k = 10) == 0
    assert candidate(nums = [23, 45, 12, 78, 45, 90, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90],k = 30) == 44
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 600
    assert candidate(nums = [1, 1000, 2000, 3000, 4000, 5000, 6000],k = 100) == 5799
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],k = 4) == 28
    assert candidate(nums = [5, 2, 11, 14, 7],k = 4) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 10) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 60) == 120
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 0) == 900
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75],k = 20) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 25) == 90
    assert candidate(nums = [5, 8, 12, 15, 18, 22, 25, 28, 32, 35, 38, 42, 45, 48, 52, 55, 58, 62],k = 10) == 37
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77],k = 15) == 40
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 14
    assert candidate(nums = [5000, 4000, 3000, 2000, 1000],k = 1000) == 2000
    assert candidate(nums = [5, 8, 12, 15, 20, 25, 30, 35],k = 3) == 24
    assert candidate(nums = [1, 100, 200, 300, 400, 500],k = 25) == 449
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 5) == 34
    assert candidate(nums = [2, 5, 1, 8, 9, 10, 11, 12, 15, 20],k = 5) == 9
    assert candidate(nums = [10, 15, 1, 2, 11, 5, 7, 3, 13, 9],k = 4) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 9
    assert candidate(nums = [10, 15, 18, 20, 25, 30, 40, 50],k = 5) == 30
    assert candidate(nums = [5, 1, 9, 17, 13, 2, 8],k = 5) == 8
    assert candidate(nums = [100, 200, 300, 400, 500],k = 50) == 300
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 20) == 100
    assert candidate(nums = [1, 100, 200, 300, 400, 500],k = 50) == 399
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000],k = 2000) == 15000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 10
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 7) == 119
    assert candidate(nums = [8, 10, 5, 11, 6, 9, 4, 12, 3, 7],k = 3) == 5
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500],k = 20) == 360
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == 63
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 90
    assert candidate(nums = [1000, 500, 300, 200, 400, 600, 700, 800, 900, 100],k = 50) == 800
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 9
    assert candidate(nums = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50],k = 7) == 31
    assert candidate(nums = [2, 8, 15, 18, 3, 5, 7, 10, 12, 14],k = 4) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 60
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 40
    assert candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 9980],k = 100) == 19
    assert candidate(nums = [4, 8, 15, 16, 23, 42],k = 5) == 28
    assert candidate(nums = [5, 8, 12, 16, 20, 24, 28],k = 7) == 11
    assert candidate(nums = [100, 50, 30, 20, 40, 60, 70, 80, 90, 10],k = 15) == 60
    assert candidate(nums = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2],k = 1) == 7
    assert candidate(nums = [20, 1, 15, 17, 5, 13, 19, 9, 7, 11],k = 5) == 9
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10) == 75


