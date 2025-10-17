def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [3, 0, -3, 4, -5, 0, -7, 1],difference = -3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, -3, 4, -5, 0, -7, 1],difference = -3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4],difference = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4],difference = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7],difference = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7],difference = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1],difference = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1],difference = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1],difference = -1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1],difference = -1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9],difference = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9],difference = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8],difference = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8],difference = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5],difference = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5],difference = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 7, 8, 5, 3, 4, 2, 1],difference = -2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 7, 8, 5, 3, 4, 2, 1],difference = -2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],difference = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],difference = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 1, 5, 2, 3, 4, 1],difference = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 1, 5, 2, 3, 4, 1],difference = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10],difference = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10],difference = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44],difference = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44],difference = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30],difference = -2) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30],difference = -2) == 31: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 10, 30, 20, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 10, 30, 20, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 8, 6, 4, 2, -2, -4, -6, -8, -10],difference = -2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 8, 6, 4, 2, -2, -4, -6, -8, -10],difference = -2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],difference = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],difference = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],difference = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],difference = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16],difference = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16],difference = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, -999, -998, -997, -996, -995, -994, -993, -992, -991],difference = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, -999, -998, -997, -996, -995, -994, -993, -992, -991],difference = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],difference = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],difference = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],difference = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],difference = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50],difference = -2) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50],difference = -2) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100],difference = 3) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100],difference = 3) == 34: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8],difference = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8],difference = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],difference = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],difference = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40],difference = -2) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40],difference = -2) == 41: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],difference = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],difference = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],difference = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],difference = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],difference = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],difference = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55],difference = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55],difference = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],difference = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],difference = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],difference = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],difference = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, -3, -6, -9, -12, -15, -18, -21, -24, -27],difference = -3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, -3, -6, -9, -12, -15, -18, -21, -24, -27],difference = -3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],difference = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],difference = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 7, 4, 3, 2, 1],difference = -3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 7, 4, 3, 2, 1],difference = -3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13],difference = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13],difference = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 6, 8, 10, 14, 18, 22, 26],difference = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 6, 8, 10, 14, 18, 22, 26],difference = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],difference = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],difference = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],difference = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],difference = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55],difference = -5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55],difference = -5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],difference = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],difference = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],difference = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],difference = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 1, -1, -3, -5, -7, -9],difference = -2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 1, -1, -3, -5, -7, -9],difference = -2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46],difference = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46],difference = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],difference = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],difference = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 10, 11, 12, 15, 16, 17, 20, 21, 22],difference = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 10, 11, 12, 15, 16, 17, 20, 21, 22],difference = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],difference = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],difference = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],difference = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],difference = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5],difference = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5],difference = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63],difference = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63],difference = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],difference = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],difference = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20],difference = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20],difference = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],difference = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],difference = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70],difference = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70],difference = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],difference = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],difference = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],difference = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],difference = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],difference = -10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],difference = -10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32],difference = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32],difference = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],difference = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],difference = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],difference = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],difference = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 15, 20, 25, 30, 35, 40, 45, 50],difference = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 15, 20, 25, 30, 35, 40, 45, 50],difference = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25],difference = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25],difference = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],difference = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],difference = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],difference = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],difference = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],difference = -1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],difference = -1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13],difference = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13],difference = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],difference = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],difference = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],difference = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],difference = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],difference = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],difference = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91],difference = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91],difference = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],difference = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],difference = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],difference = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],difference = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 2, 5, 8, 4, 6, 1, 3, 7],difference = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 2, 5, 8, 4, 6, 1, 3, 7],difference = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],difference = 2) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],difference = 2) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],difference = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],difference = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],difference = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],difference = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],difference = 13) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],difference = 13) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25],difference = -2) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25],difference = -2) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10000, 9998, 9996, 9994, 9992, 9990, 9988, 9986, 9984, 9982],difference = -2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10000, 9998, 9996, 9994, 9992, 9990, 9988, 9986, 9984, 9982],difference = -2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],difference = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],difference = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 7, 8, 10, 11],difference = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 7, 8, 10, 11],difference = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 6, 11, 16, 21, 26, 31],difference = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 6, 11, 16, 21, 26, 31],difference = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],difference = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],difference = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40],difference = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40],difference = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 97, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64, 61, 58, 55, 52, 49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, -2, -5, -8, -11, -14, -17, -20, -23, -26, -29, -32, -35, -38, -41, -44, -47, -50],difference = -3) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 97, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64, 61, 58, 55, 52, 49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, -2, -5, -8, -11, -14, -17, -20, -23, -26, -29, -32, -35, -38, -41, -44, -47, -50],difference = -3) == 51: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],difference = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],difference = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],difference = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],difference = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],difference = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],difference = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 0, -3, -6, -9, -12, -15],difference = -3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, -3, -6, -9, -12, -15],difference = -3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],difference = 0) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],difference = 0) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],difference = 4) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],difference = 4) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 4, 7, 2, 5, 8, 11, 14],difference = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 4, 7, 2, 5, 8, 11, 14],difference = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 8, 7, 6, 5, 4],difference = -1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 8, 7, 6, 5, 4],difference = -1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50],difference = -5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50],difference = -5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14],difference = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14],difference = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 0, -3, -6, -9, -12, -15, -18],difference = -3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, -3, -6, -9, -12, -15, -18],difference = -3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 7, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6],difference = -3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 7, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6],difference = -3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],difference = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],difference = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 0, -3, -6, -9, -12, -15, -18, -21, -24],difference = -3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, -3, -6, -9, -12, -15, -18, -21, -24],difference = -3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],difference = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],difference = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41],difference = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41],difference = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],difference = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],difference = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22],difference = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22],difference = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],difference = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],difference = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18],difference = -2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18],difference = -2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10],difference = -10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10],difference = -10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],difference = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],difference = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],difference = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],difference = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986],difference = -1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986],difference = -1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10000, -9999, -9998, -9997, -9996, -9995, -9994, -9993, -9992, -9991],difference = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10000, -9999, -9998, -9997, -9996, -9995, -9994, -9993, -9992, -9991],difference = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18],difference = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18],difference = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],difference = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],difference = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, -99, 198, -297, 396, -495, 594, -693, 792, -891, 990, -1089, 1188, -1287, 1386],difference = -198) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, -99, 198, -297, 396, -495, 594, -693, 792, -891, 990, -1089, 1188, -1287, 1386],difference = -198) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],difference = -10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],difference = -10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50],difference = -5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50],difference = -5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],difference = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],difference = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],difference = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],difference = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],difference = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],difference = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],difference = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],difference = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],difference = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],difference = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],difference = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],difference = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],difference = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],difference = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6],difference = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6],difference = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],difference = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],difference = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7],difference = -3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7],difference = -3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],difference = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],difference = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 9, 17, 33, 65, 129, 257],difference = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 9, 17, 33, 65, 129, 257],difference = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 0, -5, -10, -15, -20, -25, -30],difference = -5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 0, -5, -10, -15, -20, -25, -30],difference = -5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],difference = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],difference = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [200, 195, 190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125, 120, 115, 110],difference = -5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [200, 195, 190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125, 120, 115, 110],difference = -5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37],difference = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37],difference = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],difference = -1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],difference = -1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],difference = -10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],difference = -10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],difference = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],difference = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],difference = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],difference = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],difference = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],difference = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],difference = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],difference = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 12, 10, 0, -2, 7, 15, 22, 29, 36, 43],difference = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 12, 10, 0, -2, 7, 15, 22, 29, 36, 43],difference = 7) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [3, 0, -3, 4, -5, 0, -7, 1],difference = -3) == 3
    assert candidate(arr = [1, 2, 3, 4],difference = 1) == 4
    assert candidate(arr = [1, 3, 5, 7],difference = 1) == 1
    assert candidate(arr = [1, 1, 1, 1, 1],difference = 0) == 5
    assert candidate(arr = [5, 4, 3, 2, 1],difference = -1) == 5
    assert candidate(arr = [1, 3, 5, 7, 9],difference = 2) == 5
    assert candidate(arr = [4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8],difference = 0) == 2
    assert candidate(arr = [1, 2, 3, 4, 5],difference = 2) == 3
    assert candidate(arr = [1, 5, 7, 8, 5, 3, 4, 2, 1],difference = -2) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],difference = 1) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 10
    assert candidate(arr = [4, 1, 1, 5, 2, 3, 4, 1],difference = 1) == 4
    assert candidate(arr = [1, 4, 7, 10],difference = 3) == 4
    assert candidate(arr = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44],difference = 3) == 15
    assert candidate(arr = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30],difference = -2) == 31
    assert candidate(arr = [20, 10, 30, 20, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 9
    assert candidate(arr = [10, 8, 6, 4, 2, -2, -4, -6, -8, -10],difference = -2) == 5
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 11
    assert candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],difference = 1) == 3
    assert candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],difference = 4) == 2
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16],difference = 2) == 8
    assert candidate(arr = [1000, -999, -998, -997, -996, -995, -994, -993, -992, -991],difference = 1) == 9
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 1) == 1
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],difference = 5) == 15
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],difference = 2) == 13
    assert candidate(arr = [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50],difference = -2) == 26
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100],difference = 3) == 34
    assert candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8],difference = 2) == 4
    assert candidate(arr = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],difference = 5) == 10
    assert candidate(arr = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40],difference = -2) == 41
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 30
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],difference = 2) == 20
    assert candidate(arr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],difference = 2) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],difference = 1) == 40
    assert candidate(arr = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55],difference = 6) == 10
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],difference = 2) == 10
    assert candidate(arr = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],difference = 2) == 21
    assert candidate(arr = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, -3, -6, -9, -12, -15, -18, -21, -24, -27],difference = -3) == 20
    assert candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],difference = 1) == 8
    assert candidate(arr = [10, 7, 4, 3, 2, 1],difference = -3) == 4
    assert candidate(arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13],difference = 1) == 4
    assert candidate(arr = [1, 2, 3, 4, 6, 8, 10, 14, 18, 22, 26],difference = 2) == 5
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],difference = 100) == 10
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],difference = 3) == 3
    assert candidate(arr = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55],difference = -5) == 10
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],difference = 4) == 10
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],difference = 1) == 4
    assert candidate(arr = [5, 3, 1, -1, -3, -5, -7, -9],difference = -2) == 8
    assert candidate(arr = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46],difference = 5) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],difference = 1) == 15
    assert candidate(arr = [5, 6, 7, 10, 11, 12, 15, 16, 17, 20, 21, 22],difference = 1) == 3
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],difference = 1) == 50
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],difference = 10) == 15
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5],difference = 1) == 5
    assert candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63],difference = 6) == 11
    assert candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],difference = 1) == 2
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 1) == 20
    assert candidate(arr = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20],difference = 2) == 10
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],difference = 0) == 10
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70],difference = 10) == 7
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],difference = 3) == 3
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 10
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],difference = 3) == 15
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],difference = -10) == 11
    assert candidate(arr = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32],difference = 3) == 10
    assert candidate(arr = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],difference = 3) == 10
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],difference = 2) == 2
    assert candidate(arr = [10, 15, 20, 25, 30, 35, 40, 45, 50],difference = 5) == 9
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25],difference = 4) == 7
    assert candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 9
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],difference = 5) == 11
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],difference = 2) == 21
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],difference = -1) == 21
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13],difference = 2) == 7
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],difference = 5) == 10
    assert candidate(arr = [2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],difference = 2) == 10
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],difference = 10) == 11
    assert candidate(arr = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91],difference = 9) == 11
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],difference = 2) == 20
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],difference = 2) == 8
    assert candidate(arr = [10, 2, 5, 8, 4, 6, 1, 3, 7],difference = 3) == 3
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],difference = 2) == 25
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 10
    assert candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],difference = 4) == 2
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],difference = 2) == 15
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],difference = 13) == 3
    assert candidate(arr = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25],difference = -2) == 26
    assert candidate(arr = [10000, 9998, 9996, 9994, 9992, 9990, 9988, 9986, 9984, 9982],difference = -2) == 10
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],difference = 2) == 11
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],difference = 2) == 2
    assert candidate(arr = [1, 2, 3, 6, 7, 8, 10, 11],difference = 1) == 3
    assert candidate(arr = [1, 6, 11, 16, 21, 26, 31],difference = 5) == 7
    assert candidate(arr = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],difference = 11) == 10
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40],difference = 3) == 14
    assert candidate(arr = [100, 97, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64, 61, 58, 55, 52, 49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, -2, -5, -8, -11, -14, -17, -20, -23, -26, -29, -32, -35, -38, -41, -44, -47, -50],difference = -3) == 51
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],difference = 3) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],difference = 1) == 15
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],difference = 3) == 11
    assert candidate(arr = [3, 0, -3, -6, -9, -12, -15],difference = -3) == 7
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],difference = 0) == 20
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],difference = 4) == 13
    assert candidate(arr = [10, 4, 7, 2, 5, 8, 11, 14],difference = 3) == 5
    assert candidate(arr = [1, 2, 3, 8, 7, 6, 5, 4],difference = -1) == 5
    assert candidate(arr = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50],difference = -5) == 21
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 1) == 20
    assert candidate(arr = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14],difference = 1) == 14
    assert candidate(arr = [3, 0, -3, -6, -9, -12, -15, -18],difference = -3) == 8
    assert candidate(arr = [10, 7, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6],difference = -3) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],difference = 2) == 10
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],difference = 5) == 20
    assert candidate(arr = [3, 0, -3, -6, -9, -12, -15, -18, -21, -24],difference = -3) == 10
    assert candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],difference = 4) == 10
    assert candidate(arr = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41],difference = 3) == 13
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],difference = 0) == 10
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22],difference = 3) == 8
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],difference = 2) == 13
    assert candidate(arr = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12, -14, -16, -18],difference = -2) == 20
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10],difference = -10) == 12
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],difference = 2) == 6
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],difference = -1) == 20
    assert candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],difference = 1) == 10
    assert candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986],difference = -1) == 15
    assert candidate(arr = [-10000, -9999, -9998, -9997, -9996, -9995, -9994, -9993, -9992, -9991],difference = 1) == 10
    assert candidate(arr = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18],difference = 3) == 2
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],difference = 4) == 11
    assert candidate(arr = [100, -99, 198, -297, 396, -495, 594, -693, 792, -891, 990, -1089, 1188, -1287, 1386],difference = -198) == 7
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],difference = -10) == 10
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],difference = 10) == 10
    assert candidate(arr = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50],difference = -5) == 11
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],difference = 3) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 30
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],difference = 1) == 10
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],difference = 5) == 13
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],difference = 1) == 25
    assert candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],difference = 1) == 3
    assert candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],difference = 1) == 2
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],difference = 1) == 2
    assert candidate(arr = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6],difference = 1) == 7
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536],difference = 2) == 2
    assert candidate(arr = [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7],difference = -3) == 20
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],difference = 4) == 20
    assert candidate(arr = [1, 2, 3, 5, 9, 17, 33, 65, 129, 257],difference = 1) == 3
    assert candidate(arr = [10, 5, 0, -5, -10, -15, -20, -25, -30],difference = -5) == 9
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],difference = 1) == 26
    assert candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],difference = 2) == 2
    assert candidate(arr = [200, 195, 190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125, 120, 115, 110],difference = -5) == 19
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37],difference = 3) == 13
    assert candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],difference = -1) == 11
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],difference = -10) == 21
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],difference = 3) == 1
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],difference = 1) == 3
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],difference = 10) == 15
    assert candidate(arr = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],difference = 0) == 10
    assert candidate(arr = [4, 12, 10, 0, -2, 7, 15, 22, 29, 36, 43],difference = 7) == 5


