def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1],k = 1,p = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1],k = 1,p = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 23, 29, 31, 37],k = 3,p = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 23, 29, 31, 37],k = 3,p = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2],k = 1,p = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2],k = 1,p = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65],k = 2,p = 13) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65],k = 2,p = 13) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 2,p = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 2,p = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20],k = 2,p = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20],k = 2,p = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],k = 3,p = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],k = 3,p = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 17],k = 1,p = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 17],k = 1,p = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 2,p = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 2,p = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 3, 2, 8, 7, 1],k = 3,p = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 3, 2, 8, 7, 1],k = 3,p = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 1,p = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 1,p = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 12, 15, 18],k = 2,p = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 12, 15, 18],k = 2,p = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 0,p = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 0,p = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],k = 3,p = 11) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],k = 3,p = 11) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 19, 19, 19, 19],k = 3,p = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 19, 19, 19, 19],k = 3,p = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],k = 2,p = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],k = 2,p = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],k = 1,p = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],k = 1,p = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],k = 1,p = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],k = 1,p = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7],k = 0,p = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7],k = 0,p = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],k = 3,p = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],k = 3,p = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],k = 1,p = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],k = 1,p = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],k = 2,p = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],k = 2,p = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 100, 50, 25, 12],k = 1,p = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 100, 50, 25, 12],k = 1,p = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 2,p = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 2,p = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 2,p = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 2,p = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1,p = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1,p = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 25],k = 3,p = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 25],k = 3,p = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 3, 9, 12, 15],k = 2,p = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 3, 9, 12, 15],k = 2,p = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 2, 2],k = 2,p = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 2, 2],k = 2,p = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 13, 17, 19, 23],k = 5,p = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 13, 17, 19, 23],k = 5,p = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],k = 0,p = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],k = 0,p = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30],k = 3,p = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30],k = 3,p = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],k = 5,p = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],k = 5,p = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40],k = 2,p = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40],k = 2,p = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],k = 4,p = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],k = 4,p = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 3, 2, 7, 4],k = 3,p = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 3, 2, 7, 4],k = 3,p = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 15,p = 3) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 15,p = 3) == 195: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 7,p = 13) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 7,p = 13) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 8,p = 1) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 8,p = 1) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 5,p = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 5,p = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 10,p = 11) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 10,p = 11) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],k = 1,p = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],k = 1,p = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,p = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,p = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 2,p = 11) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 2,p = 11) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 15,p = 7) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 15,p = 7) == 231: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 25,p = 2) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 25,p = 2) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 4,p = 4) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 4,p = 4) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200,p = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200,p = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 15,p = 200) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 15,p = 200) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,p = 3) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,p = 3) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 2,p = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 2,p = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5,p = 2) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5,p = 2) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209],k = 10,p = 11) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209],k = 10,p = 11) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 200],k = 5,p = 5) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 200],k = 5,p = 5) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 6,p = 11) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 6,p = 11) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 15,p = 19) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 15,p = 19) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10,p = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10,p = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,p = 3) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,p = 3) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 2,p = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 2,p = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,p = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,p = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 7,p = 7) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 7,p = 7) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],k = 4,p = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],k = 4,p = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],k = 10,p = 20) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],k = 10,p = 20) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 3,p = 15) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 3,p = 15) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 10,p = 5) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 10,p = 5) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],k = 7,p = 5) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],k = 7,p = 5) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126],k = 12,p = 6) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126],k = 12,p = 6) == 174: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5,p = 2) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5,p = 2) == 147: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3,p = 4) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3,p = 4) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 2,p = 13) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 2,p = 13) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 4) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 4) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3,p = 2) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3,p = 2) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 3) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 3) == 201: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15,p = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15,p = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 10,p = 7) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 10,p = 7) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 5,p = 3) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 5,p = 3) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10,p = 100) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10,p = 100) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 15,p = 2) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 15,p = 2) == 345: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10,p = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10,p = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 4,p = 7) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 4,p = 7) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,p = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,p = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 3,p = 11) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 3,p = 11) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2,p = 2) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2,p = 2) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 10,p = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 10,p = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 2) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 2) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300],k = 10,p = 15) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300],k = 10,p = 15) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,p = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,p = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 10,p = 5) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 10,p = 5) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 10,p = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 10,p = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 5,p = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 5,p = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],k = 5,p = 3) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],k = 5,p = 3) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 4,p = 7) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 4,p = 7) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 5,p = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 5,p = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50,p = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50,p = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 10,p = 3) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 10,p = 3) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 1) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 1) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 5,p = 3) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 5,p = 3) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4,p = 3) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4,p = 3) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 7,p = 3) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 7,p = 3) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2,p = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2,p = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 5,p = 13) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 5,p = 13) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,p = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,p = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6,p = 2) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6,p = 2) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91],k = 7,p = 7) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91],k = 7,p = 7) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4,p = 10) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4,p = 10) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10,p = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10,p = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],k = 15,p = 5) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],k = 15,p = 5) == 270: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10,p = 5) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10,p = 5) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0,p = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0,p = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6,p = 2) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6,p = 2) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 20,p = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 20,p = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,p = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,p = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10,p = 2) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10,p = 2) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 3,p = 7) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 3,p = 7) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414],k = 4,p = 101) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414],k = 4,p = 101) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285, 304, 323, 342, 361, 380, 399, 418, 437, 456, 475, 494, 513, 532, 551, 570],k = 20,p = 19) == 410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285, 304, 323, 342, 361, 380, 399, 418, 437, 456, 475, 494, 513, 532, 551, 570],k = 20,p = 19) == 410: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91],k = 6,p = 7) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91],k = 6,p = 7) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 20,p = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 20,p = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 2) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 2) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],k = 7,p = 5) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],k = 7,p = 5) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],k = 3,p = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],k = 3,p = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 15,p = 2) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 15,p = 2) == 465: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10],k = 3,p = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10],k = 3,p = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425],k = 10,p = 17) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425],k = 10,p = 17) == 205: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,p = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,p = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 2) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 2) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200],k = 4,p = 25) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200],k = 4,p = 25) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 20,p = 3) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 20,p = 3) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],k = 6,p = 101) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],k = 6,p = 101) == 66: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209],k = 8,p = 11) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209],k = 8,p = 11) == 124: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 5,p = 3) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 5,p = 3) == 65: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 1, 2, 1],k = 1,p = 2) == 5
    assert candidate(nums = [19, 23, 29, 31, 37],k = 3,p = 5) == 15
    assert candidate(nums = [1, 2, 1, 2],k = 1,p = 2) == 5
    assert candidate(nums = [13, 26, 39, 52, 65],k = 2,p = 13) == 9
    assert candidate(nums = [5, 5, 5, 5],k = 2,p = 5) == 2
    assert candidate(nums = [5, 10, 15, 20],k = 2,p = 5) == 7
    assert candidate(nums = [5, 10, 15, 20, 25],k = 3,p = 5) == 12
    assert candidate(nums = [7, 11, 13, 17],k = 1,p = 2) == 10
    assert candidate(nums = [100, 200, 300, 400, 500],k = 2,p = 100) == 9
    assert candidate(nums = [6, 3, 2, 8, 7, 1],k = 3,p = 3) == 21
    assert candidate(nums = [5, 5, 5, 5],k = 1,p = 5) == 1
    assert candidate(nums = [3, 9, 12, 15, 18],k = 2,p = 3) == 9
    assert candidate(nums = [10, 20, 30, 40, 50],k = 0,p = 10) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],k = 3,p = 11) == 12
    assert candidate(nums = [19, 19, 19, 19, 19],k = 3,p = 19) == 3
    assert candidate(nums = [7, 14, 21, 28, 35],k = 2,p = 7) == 9
    assert candidate(nums = [2, 4, 6, 8, 10],k = 1,p = 2) == 5
    assert candidate(nums = [3, 6, 9, 12, 15],k = 1,p = 3) == 5
    assert candidate(nums = [7, 7, 7, 7, 7],k = 0,p = 7) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30],k = 3,p = 5) == 15
    assert candidate(nums = [7, 14, 21, 28, 35],k = 1,p = 7) == 5
    assert candidate(nums = [3, 6, 9, 12, 15],k = 2,p = 3) == 9
    assert candidate(nums = [200, 100, 50, 25, 12],k = 1,p = 25) == 6
    assert candidate(nums = [1, 1, 1, 1, 1],k = 2,p = 1) == 2
    assert candidate(nums = [10, 20, 30, 40, 50],k = 2,p = 10) == 9
    assert candidate(nums = [1, 1, 1, 1],k = 1,p = 1) == 1
    assert candidate(nums = [10, 5, 15, 20, 25],k = 3,p = 5) == 12
    assert candidate(nums = [6, 3, 9, 12, 15],k = 2,p = 3) == 9
    assert candidate(nums = [2, 3, 3, 2, 2],k = 2,p = 2) == 11
    assert candidate(nums = [11, 13, 17, 19, 23],k = 5,p = 2) == 15
    assert candidate(nums = [2, 4, 6, 8, 10],k = 0,p = 2) == 0
    assert candidate(nums = [6, 12, 18, 24, 30],k = 3,p = 3) == 12
    assert candidate(nums = [11, 22, 33, 44, 55],k = 5,p = 10) == 15
    assert candidate(nums = [8, 16, 24, 32, 40],k = 2,p = 8) == 9
    assert candidate(nums = [1, 2, 3, 4],k = 4,p = 1) == 10
    assert candidate(nums = [1, 6, 3, 2, 7, 4],k = 3,p = 3) == 21
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 15,p = 3) == 195
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 7,p = 13) == 119
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 8,p = 1) == 132
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 5,p = 5) == 50
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 10,p = 11) == 155
    assert candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],k = 1,p = 20) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,p = 1) == 55
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 2,p = 11) == 19
    assert candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 15,p = 7) == 231
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 25,p = 2) == 325
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 1) == 5
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 4,p = 4) == 34
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200,p = 2) == 20
    assert candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 15,p = 200) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,p = 3) == 120
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 2,p = 2) == 9
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5,p = 2) == 65
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209],k = 10,p = 11) == 145
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 200],k = 5,p = 5) == 210
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 6,p = 11) == 75
    assert candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 15,p = 19) == 210
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10,p = 10) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,p = 3) == 210
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 2,p = 2) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,p = 10) == 40
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 7,p = 7) == 77
    assert candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],k = 4,p = 100) == 8
    assert candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],k = 10,p = 20) == 155
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 3,p = 15) == 27
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 10,p = 5) == 209
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],k = 7,p = 5) == 91
    assert candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126],k = 12,p = 6) == 174
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5,p = 2) == 147
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3,p = 4) == 47
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 2,p = 13) == 19
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 4) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3,p = 2) == 41
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 3) == 201
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15,p = 2) == 210
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],k = 10,p = 7) == 155
    assert candidate(nums = [15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 5,p = 3) == 40
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10,p = 100) == 155
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 15,p = 2) == 345
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10,p = 5) == 10
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 4,p = 7) == 34
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,p = 1) == 3
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 3,p = 11) == 27
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2,p = 2) == 55
    assert candidate(nums = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181],k = 10,p = 2) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 2) == 160
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300],k = 10,p = 15) == 155
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,p = 5) == 5
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 10,p = 5) == 155
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 10,p = 3) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 2) == 20
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 5,p = 2) == 19
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],k = 5,p = 3) == 45
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 4,p = 7) == 34
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 5,p = 4) == 40
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50,p = 1) == 50
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 10,p = 3) == 155
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,p = 1) == 90
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 5,p = 3) == 60
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 2) == 10
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 4,p = 3) == 34
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 7,p = 3) == 119
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2,p = 10) == 19
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 5,p = 13) == 90
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,p = 1) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6,p = 2) == 75
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91],k = 7,p = 7) == 70
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4,p = 10) == 34
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10,p = 2) == 210
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],k = 15,p = 5) == 270
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10,p = 5) == 155
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0,p = 5) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6,p = 2) == 75
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,p = 1) == 5
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 20,p = 2) == 210
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,p = 1) == 3
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10,p = 2) == 105
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 3,p = 7) == 27
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414],k = 4,p = 101) == 50
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285, 304, 323, 342, 361, 380, 399, 418, 437, 456, 475, 494, 513, 532, 551, 570],k = 20,p = 19) == 410
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91],k = 6,p = 7) == 63
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 20,p = 2) == 20
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 2) == 40
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],k = 7,p = 5) == 84
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],k = 3,p = 10) == 30
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],k = 15,p = 2) == 465
    assert candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10],k = 3,p = 5) == 6
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425],k = 10,p = 17) == 205
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,p = 10) == 40
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5,p = 2) == 40
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200],k = 4,p = 25) == 26
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 20,p = 3) == 210
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],k = 6,p = 101) == 66
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209],k = 8,p = 11) == 124
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 5,p = 3) == 65


