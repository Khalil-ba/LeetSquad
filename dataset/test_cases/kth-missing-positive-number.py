def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30],k = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30],k = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 7, 11],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 7, 11],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 8, 9, 10],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 8, 9, 10],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 8, 10, 11],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 8, 10, 11],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40],k = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40],k = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 60) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 60) == 80: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 9, 11, 15, 18, 22, 25],k = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 9, 11, 15, 18, 22, 25],k = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 500) == 509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 500) == 509: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 8, 9, 11, 14, 17, 18, 21],k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 8, 9, 11, 14, 17, 18, 21],k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25],k = 15) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25],k = 15) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 25) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 25) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 7, 15, 31, 63, 127],k = 200) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 7, 15, 31, 63, 127],k = 200) == 207: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 120) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 120) == 145: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59],k = 30) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59],k = 30) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 10, 17, 26, 37, 49, 62, 76, 91, 107, 124, 142, 161, 181],k = 25) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 10, 17, 26, 37, 49, 62, 76, 91, 107, 124, 142, 161, 181],k = 25) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 6, 8, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 32],k = 20) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 6, 8, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 32],k = 20) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 30) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 30) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1000],k = 1000) == 1011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1000],k = 1000) == 1011: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 8, 13, 18, 23, 28, 33, 38],k = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 8, 13, 18, 23, 28, 33, 38],k = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 6, 9, 11, 15, 17, 20, 23],k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 6, 9, 11, 15, 17, 20, 23],k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 200) == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 200) == 221: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25],k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25],k = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 100) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 100) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 15) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 15) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 75) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 75) == 94: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 150) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 150) == 164: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 5, 8, 10, 13, 16, 19, 22, 25],k = 18) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 5, 8, 10, 13, 16, 19, 22, 25],k = 18) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 6, 10, 14, 18, 22, 26],k = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 6, 10, 14, 18, 22, 26],k = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 75) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 75) == 84: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 30) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 30) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 30) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 30) == 34: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120],k = 150) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120],k = 150) == 165: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],k = 25) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],k = 25) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71],k = 50) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71],k = 50) == 63: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100],k = 100) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100],k = 100) == 134: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 25) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 25) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 50) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 50) == 54: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],k = 30) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],k = 30) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 100) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 100) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [25, 50, 75, 100, 125, 150, 175, 200],k = 50) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [25, 50, 75, 100, 125, 150, 175, 200],k = 50) == 52: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 75) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 75) == 90: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35],k = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35],k = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 8, 12, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79],k = 50) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 8, 12, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79],k = 50) == 66: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 30) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 30) == 34: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 50) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 50) == 57: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 9, 12, 15, 18, 21, 24, 27, 30],k = 20) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 9, 12, 15, 18, 21, 24, 27, 30],k = 20) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 50) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 50) == 58: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],k = 40) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],k = 40) == 48: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21],k = 30) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21],k = 30) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597],k = 100) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597],k = 100) == 109: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20],k = 15) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20],k = 15) == 31: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 30) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 30) == 38: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 454
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 454: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 500) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 500) == 550: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30],k = 12) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30],k = 12) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 7, 11, 14, 17, 20, 23, 26, 29],k = 40) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 7, 11, 14, 17, 20, 23, 26, 29],k = 40) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 150) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 150) == 171: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20],k = 50) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20],k = 50) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49],k = 25) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49],k = 25) == 31: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55],k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55],k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 100) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 100) == 150: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 505: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 50) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 50) == 58: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25],k = 25) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25],k = 25) == 34: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 75) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 75) == 82: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 15) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 15) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 8, 11, 15],k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 8, 11, 15],k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255],k = 60) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255],k = 60) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 30) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 30) == 51: {e}')
    
    total += 1
    try:
        result = candidate(arr = [300, 600, 900],k = 1000) == 1003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [300, 600, 900],k = 1000) == 1003: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 1000) == 1015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 1000) == 1015: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 100) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 100) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 9, 11, 12, 15],k = 15) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 9, 11, 12, 15],k = 15) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 40) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 40) == 43: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 100) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 100) == 102: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 150) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 150) == 175: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 50) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 50) == 58: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 8, 12, 17, 23, 30, 38, 47],k = 35) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 8, 12, 17, 23, 30, 38, 47],k = 35) == 44: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 8, 10, 13, 14],k = 7) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 8, 10, 13, 14],k = 7) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 20) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 20) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 505: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 12, 14, 20, 25],k = 8) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 12, 14, 20, 25],k = 8) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 20) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 20) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 7, 11, 15, 19, 24, 29, 35],k = 20) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 7, 11, 15, 19, 24, 29, 35],k = 20) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],k = 27) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],k = 27) == 36: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26],k = 50) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26],k = 50) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 302],k = 150) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 302],k = 150) == 167: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 13) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 13) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 20
    assert candidate(arr = [10, 20, 30],k = 15) == 16
    assert candidate(arr = [2, 3, 4, 7, 11],k = 5) == 9
    assert candidate(arr = [5, 6, 7, 8, 9],k = 1) == 1
    assert candidate(arr = [5, 6, 8, 9, 10],k = 3) == 3
    assert candidate(arr = [1, 3, 5, 7],k = 3) == 6
    assert candidate(arr = [1, 3, 5, 7, 9],k = 4) == 8
    assert candidate(arr = [10, 20, 30],k = 5) == 5
    assert candidate(arr = [1, 2, 3, 4, 8, 10, 11],k = 5) == 12
    assert candidate(arr = [1, 2, 3, 4],k = 2) == 6
    assert candidate(arr = [10, 20, 30, 40],k = 15) == 16
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 60) == 80
    assert candidate(arr = [2, 5, 9, 11, 15, 18, 22, 25],k = 15) == 21
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 120
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 500) == 509
    assert candidate(arr = [5, 6, 8, 9, 11, 14, 17, 18, 21],k = 10) == 16
    assert candidate(arr = [5, 10, 15, 20, 25],k = 15) == 18
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 24
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 25) == 29
    assert candidate(arr = [1, 3, 7, 15, 31, 63, 127],k = 200) == 207
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 120) == 145
    assert candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59],k = 30) == 40
    assert candidate(arr = [2, 5, 10, 17, 26, 37, 49, 62, 76, 91, 107, 124, 142, 161, 181],k = 25) == 30
    assert candidate(arr = [1, 4, 6, 8, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 32],k = 20) == 35
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 30) == 55
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1000],k = 1000) == 1011
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 25
    assert candidate(arr = [1, 4, 8, 13, 18, 23, 28, 33, 38],k = 20) == 26
    assert candidate(arr = [1, 4, 6, 9, 11, 15, 17, 20, 23],k = 10) == 16
    assert candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 200) == 221
    assert candidate(arr = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 35
    assert candidate(arr = [5, 10, 15, 20, 25],k = 10) == 12
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 100) == 110
    assert candidate(arr = [2, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 15) == 19
    assert candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 75) == 94
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 150) == 164
    assert candidate(arr = [1, 2, 5, 8, 10, 13, 16, 19, 22, 25],k = 18) == 28
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 60
    assert candidate(arr = [2, 6, 10, 14, 18, 22, 26],k = 15) == 20
    assert candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 75) == 84
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 30) == 40
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 30) == 34
    assert candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120],k = 150) == 165
    assert candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 28
    assert candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],k = 25) == 35
    assert candidate(arr = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71],k = 50) == 63
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100],k = 100) == 134
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 25) == 45
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 50) == 54
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],k = 30) == 40
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 100) == 110
    assert candidate(arr = [25, 50, 75, 100, 125, 150, 175, 200],k = 50) == 52
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 75) == 90
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 19
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 7) == 10
    assert candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35],k = 20) == 26
    assert candidate(arr = [3, 8, 12, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79],k = 50) == 66
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 30) == 34
    assert candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],k = 50) == 57
    assert candidate(arr = [2, 5, 9, 12, 15, 18, 21, 24, 27, 30],k = 20) == 29
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 50) == 58
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 30
    assert candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],k = 40) == 48
    assert candidate(arr = [1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21],k = 30) == 45
    assert candidate(arr = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597],k = 100) == 109
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10) == 19
    assert candidate(arr = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 26
    assert candidate(arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20],k = 15) == 31
    assert candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],k = 30) == 38
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 7) == 10
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 454
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 500) == 550
    assert candidate(arr = [5, 10, 15, 20, 25, 30],k = 12) == 14
    assert candidate(arr = [2, 5, 7, 11, 14, 17, 20, 23, 26, 29],k = 40) == 50
    assert candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 150) == 171
    assert candidate(arr = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20],k = 50) == 64
    assert candidate(arr = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49],k = 25) == 31
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55],k = 10) == 16
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 100) == 150
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 505
    assert candidate(arr = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 50) == 58
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25],k = 25) == 34
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 75) == 82
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 15) == 18
    assert candidate(arr = [2, 5, 8, 11, 15],k = 10) == 14
    assert candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255],k = 60) == 64
    assert candidate(arr = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 30) == 51
    assert candidate(arr = [300, 600, 900],k = 1000) == 1003
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 1000) == 1015
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 100) == 110
    assert candidate(arr = [1, 2, 3, 5, 6, 9, 11, 12, 15],k = 15) == 24
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 40) == 43
    assert candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 100) == 102
    assert candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 150) == 175
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 50) == 58
    assert candidate(arr = [2, 3, 5, 8, 12, 17, 23, 30, 38, 47],k = 35) == 44
    assert candidate(arr = [5, 6, 8, 10, 13, 14],k = 7) == 11
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 25) == 35
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 20) == 29
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 505
    assert candidate(arr = [5, 8, 12, 14, 20, 25],k = 8) == 10
    assert candidate(arr = [5, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 17
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 20) == 35
    assert candidate(arr = [1, 2, 4, 7, 11, 15, 19, 24, 29, 35],k = 20) == 28
    assert candidate(arr = [11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],k = 27) == 36
    assert candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 25) == 32
    assert candidate(arr = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26],k = 50) == 64
    assert candidate(arr = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 302],k = 150) == 167
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 13) == 15


