def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mat = [[1], [2], [3]],target = 100) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1], [2], [3]],target = 100) == 94: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5], [5, 5, 5], [5, 5, 5]],target = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5], [5, 5, 5], [5, 5, 5]],target = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6]],target = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6]],target = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [5, 15, 25], [1, 10, 20]],target = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [5, 15, 25], [1, 10, 20]],target = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 36) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 36) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 150) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 150) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]],target = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]],target = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 100) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 100) == 110: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 150) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 9, 8, 7]],target = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 9, 8, 7]],target = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],target = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],target = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]],target = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]],target = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 60, 50, 40, 30], [20, 10, 0, -10, -20], [-30, -40, -50, -60, -70], [80, 90, 100, 110, 120]],target = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 60, 50, 40, 30], [20, 10, 0, -10, -20], [-30, -40, -50, -60, -70], [80, 90, 100, 110, 120]],target = 200) == 20: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 70, 70, 70, 70], [70, 70, 70, 70, 70], [70, 70, 70, 70, 70]],target = 800) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 70, 70, 70, 70], [70, 70, 70, 70, 70], [70, 70, 70, 70, 70]],target = 800) == 590: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [5, 10, 15, 20, 25], [7, 14, 21, 28, 35]],target = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [5, 10, 15, 20, 25], [7, 14, 21, 28, 35]],target = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 1, 1, 1, 1]],target = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 1, 1, 1, 1]],target = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [7, 17, 27, 37, 47]],target = 150) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [7, 17, 27, 37, 47]],target = 150) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 15, 25], [5, 15, 25], [5, 15, 25], [5, 15, 25], [5, 15, 25]],target = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 15, 25], [5, 15, 25], [5, 15, 25], [5, 15, 25], [5, 15, 25]],target = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 1], [70, 1], [70, 1], [70, 1], [70, 1], [70, 1], [70, 1]],target = 200) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 1], [70, 1], [70, 1], [70, 1], [70, 1], [70, 1], [70, 1]],target = 200) == 14: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],target = 75) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],target = 75) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[50, 60, 70], [10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[50, 60, 70], [10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 105) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 105) == 21: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]],target = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]],target = 50) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100]],target = 700) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100]],target = 700) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28]],target = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28]],target = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5]],target = 85) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5]],target = 85) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[60, 59, 58, 57, 56, 55, 54], [53, 52, 51, 50, 49, 48, 47], [46, 45, 44, 43, 42, 41, 40], [39, 38, 37, 36, 35, 34, 33], [32, 31, 30, 29, 28, 27, 26], [25, 24, 23, 22, 21, 20, 19]],target = 420) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[60, 59, 58, 57, 56, 55, 54], [53, 52, 51, 50, 49, 48, 47], [46, 45, 44, 43, 42, 41, 40], [39, 38, 37, 36, 35, 34, 33], [32, 31, 30, 29, 28, 27, 26], [25, 24, 23, 22, 21, 20, 19]],target = 420) == 165: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50, 60, 70], [70, 60, 50, 40, 30, 20, 10], [1, 2, 3, 4, 5, 6, 7]],target = 200) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50, 60, 70], [70, 60, 50, 40, 30, 20, 10], [1, 2, 3, 4, 5, 6, 7]],target = 200) == 53: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5]],target = 50) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5]],target = 50) == 35: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [20, 22, 24, 26, 28]],target = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [20, 22, 24, 26, 28]],target = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],target = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],target = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60]],target = 120) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60]],target = 120) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 10]],target = 50) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 10]],target = 50) == 16: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50]],target = 400) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50]],target = 400) == 50: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 70], [2, 69], [3, 68], [4, 67], [5, 66], [6, 65], [7, 64], [8, 63], [9, 62], [10, 61]],target = 400) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 70], [2, 69], [3, 68], [4, 67], [5, 66], [6, 65], [7, 64], [8, 63], [9, 62], [10, 61]],target = 400) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 6, 11, 16, 21, 26, 31, 36, 41, 46], [2, 7, 12, 17, 22, 27, 32, 37, 42, 47], [3, 8, 13, 18, 23, 28, 33, 38, 43, 48]],target = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 6, 11, 16, 21, 26, 31, 36, 41, 46], [2, 7, 12, 17, 22, 27, 32, 37, 42, 47], [3, 8, 13, 18, 23, 28, 33, 38, 43, 48]],target = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7]],target = 28) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7]],target = 28) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 50, 100], [2, 51, 101], [3, 52, 102], [4, 53, 103], [5, 54, 104]],target = 260) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 50, 100], [2, 51, 101], [3, 52, 102], [4, 53, 103], [5, 54, 104]],target = 260) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 69, 68, 67, 66, 65, 64], [63, 62, 61, 60, 59, 58, 57], [56, 55, 54, 53, 52, 51, 50], [49, 48, 47, 46, 45, 44, 43]],target = 260) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 69, 68, 67, 66, 65, 64], [63, 62, 61, 60, 59, 58, 57], [56, 55, 54, 53, 52, 51, 50], [49, 48, 47, 46, 45, 44, 43]],target = 260) == 22: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50, 60, 70], [11, 21, 31, 41, 51, 61, 71], [12, 22, 32, 42, 52, 62, 72], [13, 23, 33, 43, 53, 63, 73], [14, 24, 34, 44, 54, 64, 74], [15, 25, 35, 45, 55, 65, 75]],target = 300) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50, 60, 70], [11, 21, 31, 41, 51, 61, 71], [12, 22, 32, 42, 52, 62, 72], [13, 23, 33, 43, 53, 63, 73], [14, 24, 34, 44, 54, 64, 74], [15, 25, 35, 45, 55, 65, 75]],target = 300) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 10, 100], [10, 100, 1000], [100, 1000, 10000]],target = 1234) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 10, 100], [10, 100, 1000], [100, 1000, 10000]],target = 1234) == 34: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150], [160, 170, 180], [190, 200, 210]],target = 700) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150], [160, 170, 180], [190, 200, 210]],target = 700) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 69, 68], [67, 66, 65], [64, 63, 62], [61, 60, 59], [58, 57, 56]],target = 250) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 69, 68], [67, 66, 65], [64, 63, 62], [61, 60, 59], [58, 57, 56]],target = 250) == 60: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28]],target = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28]],target = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[50, 49, 48, 47, 46, 45, 44], [43, 42, 41, 40, 39, 38, 37], [36, 35, 34, 33, 32, 31, 30]],target = 130) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[50, 49, 48, 47, 46, 45, 44], [43, 42, 41, 40, 39, 38, 37], [36, 35, 34, 33, 32, 31, 30]],target = 130) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],target = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],target = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[3, 10, 7], [8, 6, 4], [15, 12, 9], [18, 16, 13]],target = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[3, 10, 7], [8, 6, 4], [15, 12, 9], [18, 16, 13]],target = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[60, 70, 80, 90, 100], [1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [100, 90, 80, 70, 60]],target = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[60, 70, 80, 90, 100], [1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [100, 90, 80, 70, 60]],target = 300) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12]],target = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12]],target = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 21, 42, 58], [9, 23, 46, 62], [11, 25, 49, 65], [13, 27, 51, 67], [15, 29, 53, 69]],target = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 21, 42, 58], [9, 23, 46, 62], [11, 25, 49, 65], [13, 27, 51, 67], [15, 29, 53, 69]],target = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 60, 50, 40], [30, 20, 10, 0], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],target = 150) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 60, 50, 40], [30, 20, 10, 0], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],target = 150) == 26: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 60, 50, 40, 30], [20, 30, 40, 50, 60], [10, 20, 30, 40, 50]],target = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 60, 50, 40, 30], [20, 30, 40, 50, 60], [10, 20, 30, 40, 50]],target = 200) == 20: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 17, 27, 37, 47], [8, 18, 28, 38, 48], [9, 19, 29, 39, 49], [10, 20, 30, 40, 50], [11, 21, 31, 41, 51]],target = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 17, 27, 37, 47], [8, 18, 28, 38, 48], [9, 19, 29, 39, 49], [10, 20, 30, 40, 50], [11, 21, 31, 41, 51]],target = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 69, 68, 67], [66, 65, 64, 63], [62, 61, 60, 59], [58, 57, 56, 55]],target = 260) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 69, 68, 67], [66, 65, 64, 63], [62, 61, 60, 59], [58, 57, 56, 55]],target = 260) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 80) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 80) == 30: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [1, 2, 3]],target = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [1, 2, 3]],target = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 60, 50, 40, 30], [10, 20, 30, 40, 50], [60, 50, 40, 30, 20], [1, 2, 3, 4, 5]],target = 180) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 60, 50, 40, 30], [10, 20, 30, 40, 50], [60, 50, 40, 30, 20], [1, 2, 3, 4, 5]],target = 180) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 60) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 60) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14], [15, 17, 19, 21, 23, 25, 27]],target = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14], [15, 17, 19, 21, 23, 25, 27]],target = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34]],target = 120) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34]],target = 120) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5]],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5]],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 11, 13, 15], [17, 19, 21, 23]],target = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 11, 13, 15], [17, 19, 21, 23]],target = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 70], [1, 70], [1, 70], [1, 70], [1, 70], [1, 70], [1, 70]],target = 300) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 70], [1, 70], [1, 70], [1, 70], [1, 70], [1, 70], [1, 70]],target = 300) == 17: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],target = 120) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],target = 120) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150], [160, 170, 180]],target = 600) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150], [160, 170, 180]],target = 600) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]],target = 100) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]],target = 100) == 66: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4]],target = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4]],target = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35]],target = 150) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35]],target = 150) == 45: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],target = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],target = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 10, 15], [10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 10, 15], [10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41]],target = 120) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41]],target = 120) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 800) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 800) == 310: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 15, 25], [10, 20, 30], [15, 25, 35], [20, 30, 40]],target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 15, 25], [10, 20, 30], [15, 25, 35], [20, 30, 40]],target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],target = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],target = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5]],target = 100) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5]],target = 100) == 85: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 100, 200], [2, 150, 250], [3, 200, 300], [4, 250, 350]],target = 800) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 100, 200], [2, 150, 250], [3, 200, 300], [4, 250, 350]],target = 800) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 50) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 50) == 12: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 15, 25, 35], [10, 20, 30, 40], [15, 25, 35, 45], [20, 30, 40, 50], [25, 35, 45, 55]],target = 200) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 15, 25, 35], [10, 20, 30, 40], [15, 25, 35, 45], [20, 30, 40, 50], [25, 35, 45, 55]],target = 200) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 10, 15, 20, 25], [30, 35, 40, 45, 50], [55, 60, 65, 70, 75]],target = 120) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 10, 15, 20, 25], [30, 35, 40, 45, 50], [55, 60, 65, 70, 75]],target = 120) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],target = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],target = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 50, 100, 150, 200], [2, 51, 101, 151, 201], [3, 52, 102, 152, 202], [4, 53, 103, 153, 203], [5, 54, 104, 154, 204]],target = 500) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 50, 100, 150, 200], [2, 51, 101, 151, 201], [3, 52, 102, 152, 202], [4, 53, 103, 153, 203], [5, 54, 104, 154, 204]],target = 500) == 10: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[70, 60, 50, 40, 30, 20, 10], [65, 55, 45, 35, 25, 15, 5], [1, 2, 3, 4, 5, 6, 7]],target = 200) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[70, 60, 50, 40, 30, 20, 10], [65, 55, 45, 35, 25, 15, 5], [1, 2, 3, 4, 5, 6, 7]],target = 200) == 58: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]],target = 40) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]],target = 40) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 30) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 30) == 4: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 5, 9, 14], [3, 7, 10, 17], [4, 8, 12, 19], [6, 11, 15, 20]],target = 45) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 5, 9, 14], [3, 7, 10, 17], [4, 8, 12, 19], [6, 11, 15, 20]],target = 45) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 14, 21, 28], [35, 42, 49, 56], [63, 70, 77, 84]],target = 210) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 14, 21, 28], [35, 42, 49, 56], [63, 70, 77, 84]],target = 210) == 42: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]],target = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]],target = 50) == 8: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],target = 55) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],target = 55) == 22: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 100, 200], [1, 100, 200], [1, 100, 200], [1, 100, 200], [1, 100, 200]],target = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 100, 200], [1, 100, 200], [1, 100, 200], [1, 100, 200], [1, 100, 200]],target = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],target = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],target = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 14, 21, 28, 35], [42, 49, 56, 63, 70], [77, 84, 91, 98, 105]],target = 250) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 14, 21, 28, 35], [42, 49, 56, 63, 70], [77, 84, 91, 98, 105]],target = 250) == 40: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]],target = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]],target = 150) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]],target = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]],target = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42]],target = 200) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42]],target = 200) == 53: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],target = 49) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],target = 49) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 80) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 80) == 0: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],target = 25) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],target = 25) == 15: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 100) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 100) == 16: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],target = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],target = 7) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mat = [[1], [2], [3]],target = 100) == 94
    assert candidate(mat = [[5, 5, 5], [5, 5, 5], [5, 5, 5]],target = 15) == 0
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 13) == 0
    assert candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6]],target = 20) == 2
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 25) == 1
    assert candidate(mat = [[10, 20, 30], [5, 15, 25], [1, 10, 20]],target = 50) == 4
    assert candidate(mat = [[7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 36) == 0
    assert candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 150) == 60
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]],target = 20) == 0
    assert candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 100) == 110
    assert candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 150) == 0
    assert candidate(mat = [[1, 2, 9, 8, 7]],target = 6) == 1
    assert candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],target = 5) == 2
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]],target = 21) == 0
    assert candidate(mat = [[70, 60, 50, 40, 30], [20, 10, 0, -10, -20], [-30, -40, -50, -60, -70], [80, 90, 100, 110, 120]],target = 200) == 20
    assert candidate(mat = [[70, 70, 70, 70, 70], [70, 70, 70, 70, 70], [70, 70, 70, 70, 70]],target = 800) == 590
    assert candidate(mat = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [5, 10, 15, 20, 25], [7, 14, 21, 28, 35]],target = 100) == 15
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 1, 1, 1, 1]],target = 25) == 5
    assert candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41], [7, 17, 27, 37, 47]],target = 150) == 3
    assert candidate(mat = [[5, 15, 25], [5, 15, 25], [5, 15, 25], [5, 15, 25], [5, 15, 25]],target = 50) == 5
    assert candidate(mat = [[70, 1], [70, 1], [70, 1], [70, 1], [70, 1], [70, 1], [70, 1]],target = 200) == 14
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],target = 75) == 12
    assert candidate(mat = [[50, 60, 70], [10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 200) == 0
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 105) == 21
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]],target = 50) == 8
    assert candidate(mat = [[1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100], [1, 10, 100]],target = 700) == 0
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28]],target = 100) == 30
    assert candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5]],target = 85) == 1
    assert candidate(mat = [[60, 59, 58, 57, 56, 55, 54], [53, 52, 51, 50, 49, 48, 47], [46, 45, 44, 43, 42, 41, 40], [39, 38, 37, 36, 35, 34, 33], [32, 31, 30, 29, 28, 27, 26], [25, 24, 23, 22, 21, 20, 19]],target = 420) == 165
    assert candidate(mat = [[10, 20, 30, 40, 50, 60, 70], [70, 60, 50, 40, 30, 20, 10], [1, 2, 3, 4, 5, 6, 7]],target = 200) == 53
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5]],target = 50) == 35
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [20, 22, 24, 26, 28]],target = 50) == 0
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],target = 50) == 1
    assert candidate(mat = [[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60]],target = 120) == 0
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 10]],target = 50) == 16
    assert candidate(mat = [[50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50], [50, 50, 50, 50, 50, 50, 50]],target = 400) == 50
    assert candidate(mat = [[1, 70], [2, 69], [3, 68], [4, 67], [5, 66], [6, 65], [7, 64], [8, 63], [9, 62], [10, 61]],target = 400) == 1
    assert candidate(mat = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 6, 11, 16, 21, 26, 31, 36, 41, 46], [2, 7, 12, 17, 22, 27, 32, 37, 42, 47], [3, 8, 13, 18, 23, 28, 33, 38, 43, 48]],target = 150) == 1
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7]],target = 28) == 0
    assert candidate(mat = [[1, 50, 100], [2, 51, 101], [3, 52, 102], [4, 53, 103], [5, 54, 104]],target = 260) == 0
    assert candidate(mat = [[70, 69, 68, 67, 66, 65, 64], [63, 62, 61, 60, 59, 58, 57], [56, 55, 54, 53, 52, 51, 50], [49, 48, 47, 46, 45, 44, 43]],target = 260) == 22
    assert candidate(mat = [[10, 20, 30, 40, 50, 60, 70], [11, 21, 31, 41, 51, 61, 71], [12, 22, 32, 42, 52, 62, 72], [13, 23, 33, 43, 53, 63, 73], [14, 24, 34, 44, 54, 64, 74], [15, 25, 35, 45, 55, 65, 75]],target = 300) == 5
    assert candidate(mat = [[1, 10, 100], [10, 100, 1000], [100, 1000, 10000]],target = 1234) == 34
    assert candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150], [160, 170, 180], [190, 200, 210]],target = 700) == 0
    assert candidate(mat = [[70, 69, 68], [67, 66, 65], [64, 63, 62], [61, 60, 59], [58, 57, 56]],target = 250) == 60
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28]],target = 100) == 30
    assert candidate(mat = [[50, 49, 48, 47, 46, 45, 44], [43, 42, 41, 40, 39, 38, 37], [36, 35, 34, 33, 32, 31, 30]],target = 130) == 1
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],target = 10) == 6
    assert candidate(mat = [[3, 10, 7], [8, 6, 4], [15, 12, 9], [18, 16, 13]],target = 50) == 1
    assert candidate(mat = [[60, 70, 80, 90, 100], [1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [100, 90, 80, 70, 60]],target = 300) == 0
    assert candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12]],target = 25) == 0
    assert candidate(mat = [[7, 21, 42, 58], [9, 23, 46, 62], [11, 25, 49, 65], [13, 27, 51, 67], [15, 29, 53, 69]],target = 200) == 0
    assert candidate(mat = [[70, 60, 50, 40], [30, 20, 10, 0], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],target = 150) == 26
    assert candidate(mat = [[70, 60, 50, 40, 30], [20, 30, 40, 50, 60], [10, 20, 30, 40, 50]],target = 200) == 20
    assert candidate(mat = [[7, 17, 27, 37, 47], [8, 18, 28, 38, 48], [9, 19, 29, 39, 49], [10, 20, 30, 40, 50], [11, 21, 31, 41, 51]],target = 150) == 5
    assert candidate(mat = [[70, 69, 68, 67], [66, 65, 64, 63], [62, 61, 60, 59], [58, 57, 56, 55]],target = 260) == 4
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 80) == 30
    assert candidate(mat = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [1, 2, 3]],target = 30) == 0
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 50) == 5
    assert candidate(mat = [[70, 60, 50, 40, 30], [10, 20, 30, 40, 50], [60, 50, 40, 30, 20], [1, 2, 3, 4, 5]],target = 180) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 60) == 0
    assert candidate(mat = [[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14], [15, 17, 19, 21, 23, 25, 27]],target = 50) == 0
    assert candidate(mat = [[10, 20, 30], [11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34]],target = 120) == 0
    assert candidate(mat = [[5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5]],target = 10) == 10
    assert candidate(mat = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 11, 13, 15], [17, 19, 21, 23]],target = 30) == 1
    assert candidate(mat = [[1, 70], [1, 70], [1, 70], [1, 70], [1, 70], [1, 70], [1, 70]],target = 300) == 17
    assert candidate(mat = [[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],target = 120) == 0
    assert candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150], [160, 170, 180]],target = 600) == 0
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]],target = 100) == 66
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4]],target = 20) == 10
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35]],target = 150) == 45
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],target = 1) == 5
    assert candidate(mat = [[5, 10, 15], [10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],target = 100) == 0
    assert candidate(mat = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 11, 21, 31, 41]],target = 120) == 4
    assert candidate(mat = [[70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70], [70, 70, 70]],target = 800) == 310
    assert candidate(mat = [[5, 15, 25], [10, 20, 30], [15, 25, 35], [20, 30, 40]],target = 100) == 0
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],target = 50) == 0
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5]],target = 100) == 85
    assert candidate(mat = [[1, 100, 200], [2, 150, 250], [3, 200, 300], [4, 250, 350]],target = 800) == 0
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 50) == 12
    assert candidate(mat = [[5, 15, 25, 35], [10, 20, 30, 40], [15, 25, 35, 45], [20, 30, 40, 50], [25, 35, 45, 55]],target = 200) == 5
    assert candidate(mat = [[5, 10, 15, 20, 25], [30, 35, 40, 45, 50], [55, 60, 65, 70, 75]],target = 120) == 0
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]],target = 30) == 0
    assert candidate(mat = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],target = 10) == 3
    assert candidate(mat = [[1, 50, 100, 150, 200], [2, 51, 101, 151, 201], [3, 52, 102, 152, 202], [4, 53, 103, 153, 203], [5, 54, 104, 154, 204]],target = 500) == 10
    assert candidate(mat = [[70, 60, 50, 40, 30, 20, 10], [65, 55, 45, 35, 25, 15, 5], [1, 2, 3, 4, 5, 6, 7]],target = 200) == 58
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]],target = 40) == 0
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 30) == 4
    assert candidate(mat = [[1, 5, 9, 14], [3, 7, 10, 17], [4, 8, 12, 19], [6, 11, 15, 20]],target = 45) == 0
    assert candidate(mat = [[7, 14, 21, 28], [35, 42, 49, 56], [63, 70, 77, 84]],target = 210) == 42
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]],target = 50) == 8
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],target = 55) == 22
    assert candidate(mat = [[1, 100, 200], [1, 100, 200], [1, 100, 200], [1, 100, 200], [1, 100, 200]],target = 500) == 0
    assert candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],target = 15) == 0
    assert candidate(mat = [[7, 14, 21, 28, 35], [42, 49, 56, 63, 70], [77, 84, 91, 98, 105]],target = 250) == 40
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]],target = 150) == 0
    assert candidate(mat = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]],target = 30) == 1
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42]],target = 200) == 53
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],target = 49) == 0
    assert candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 50) == 5
    assert candidate(mat = [[7, 8, 9], [1, 2, 3], [4, 5, 6], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 80) == 0
    assert candidate(mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],target = 25) == 15
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],target = 100) == 16
    assert candidate(mat = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],target = 7) == 0


