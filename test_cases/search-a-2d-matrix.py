def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20]],target = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20]],target = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3], [0, 3, 10], [15, 20, 25]],target = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3], [0, 3, 10], [15, 20, 25]],target = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1]],target = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1]],target = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -8, -6, -4], [-3, -1, 1, 3], [5, 7, 9, 11]],target = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -8, -6, -4], [-3, -1, 1, 3], [5, 7, 9, 11]],target = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -8, -6, -4], [-3, -1, 1, 3], [5, 7, 9, 11]],target = -5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -8, -6, -4], [-3, -1, 1, 3], [5, 7, 9, 11]],target = -5) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],target = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],target = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 13) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1]],target = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1]],target = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [8, 9, 10, 12]],target = -3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [8, 9, 10, 12]],target = -3) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7]],target = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7]],target = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3], [0, 3, 10], [15, 20, 25]],target = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3], [0, 3, 10], [15, 20, 25]],target = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5]],target = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5]],target = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -2], [-1, 0, 2, 3], [4, 5, 7, 8]],target = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -2], [-1, 0, 2, 3], [4, 5, 7, 8]],target = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3]],target = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3]],target = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = -10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = -10) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7]],target = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7]],target = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -2], [-1, 0, 2, 3], [4, 5, 7, 8]],target = -3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -2], [-1, 0, 2, 3], [4, 5, 7, 8]],target = -3) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [8, 9, 10, 12]],target = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [8, 9, 10, 12]],target = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 21) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 21) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = -11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = -11) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5]],target = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5]],target = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 60) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 60) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3]],target = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3]],target = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],target = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],target = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3]],target = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3]],target = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -950, -900, -850], [-800, -750, -700, -650], [-600, -550, -500, -450], [-400, -350, -300, -250], [-200, -150, -100, -50]],target = -325) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -950, -900, -850], [-800, -750, -700, -650], [-600, -550, -500, -450], [-400, -350, -300, -250], [-200, -150, -100, -50]],target = -325) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]],target = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]],target = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -5, 0, 5, 10], [-4, -2, 2, 4, 8], [6, 7, 12, 13, 14], [15, 16, 18, 19, 20], [21, 22, 23, 24, 25]],target = 12) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -5, 0, 5, 10], [-4, -2, 2, 4, 8], [6, 7, 12, 13, 14], [15, 16, 18, 19, 20], [21, 22, 23, 24, 25]],target = 12) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13], [14, 15, 16, 17, 18], [19, 20, 21, 22, 23]],target = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13], [14, 15, 16, 17, 18], [19, 20, 21, 22, 23]],target = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], [160, 170, 180, 190, 200]],target = 150) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], [160, 170, 180, 190, 200]],target = 150) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15], [17, 19, 21, 23, 25, 27, 29, 31], [33, 35, 37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59, 61, 63]],target = 62) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15], [17, 19, 21, 23, 25, 27, 29, 31], [33, 35, 37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59, 61, 63]],target = 62) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10000]],target = -10000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10000]],target = -10000) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],target = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],target = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]],target = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]],target = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 35) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 35) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = -88) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = -88) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],target = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],target = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 61) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 61) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-4, -3, -2, -1, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = -2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-4, -3, -2, -1, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = -2) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [16, 19, 22, 25, 28], [17, 20, 23, 26, 29]],target = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [16, 19, 22, 25, 28], [17, 20, 23, 26, 29]],target = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23], [25, 27, 29, 31], [33, 35, 37, 39], [41, 43, 45, 47], [49, 51, 53, 55], [57, 59, 61, 63]],target = 64) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23], [25, 27, 29, 31], [33, 35, 37, 39], [41, 43, 45, 47], [49, 51, 53, 55], [57, 59, 61, 63]],target = 64) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -55) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -55) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59], [61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89], [91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119]],target = 119) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59], [61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89], [91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119]],target = 119) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = -6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = -6) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = 61) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = 61) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -45) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -45) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = -83) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = -83) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -2, -1], [0, 3, 5], [8, 9, 10]],target = -3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -2, -1], [0, 3, 5], [8, 9, 10]],target = -3) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]],target = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]],target = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]],target = 14) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]],target = 14) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986], [-985, -984, -983, -982, -981], [-980, -979, -978, -977, -976]],target = -987) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986], [-985, -984, -983, -982, -981], [-980, -979, -978, -977, -976]],target = -987) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 38) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 38) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986]],target = -987) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986]],target = -987) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30], [31, 32, 33]],target = 17) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30], [31, 32, 33]],target = 17) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -99, -98, -97], [-96, -95, -94, -93], [-92, -91, -90, -89], [-88, -87, -86, -85]],target = -90) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -99, -98, -97], [-96, -95, -94, -93], [-92, -91, -90, -89], [-88, -87, -86, -85]],target = -90) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],target = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],target = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39]],target = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39]],target = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11], [13, 15, 17, 19, 21, 23], [25, 27, 29, 31, 33, 35], [37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59]],target = 30) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11], [13, 15, 17, 19, 21, 23], [25, 27, 29, 31, 33, 35], [37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59]],target = 30) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 25) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 11, 12, 13, 14, 15]],target = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 11, 12, 13, 14, 15]],target = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 27) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 27) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -90, -80, -70, -60], [-50, -40, -30, -20, -10], [0, 10, 20, 30, 40], [50, 60, 70, 80, 90], [100, 110, 120, 130, 140]],target = -35) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -90, -80, -70, -60], [-50, -40, -30, -20, -10], [0, 10, 20, 30, 40], [50, 60, 70, 80, 90], [100, 110, 120, 130, 140]],target = -35) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = 45) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = 45) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]],target = 22) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]],target = 22) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]],target = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]],target = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 35) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 35) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 68) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 68) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -98, -95, -93], [-88, -86, -82, -80], [-74, -70, -66, -62], [-58, -54, -50, -46]],target = -66) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -98, -95, -93], [-88, -86, -82, -80], [-74, -70, -66, -62], [-58, -54, -50, -46]],target = -66) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 26) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 26) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 5, 9, 13], [17, 21, 25, 29], [33, 37, 41, 45], [49, 53, 57, 61]],target = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 5, 9, 13], [17, 21, 25, 29], [33, 37, 41, 45], [49, 53, 57, 61]],target = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68], [69, 70, 71, 72]],target = 67) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68], [69, 70, 71, 72]],target = 67) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -2, -1], [0, 3, 5], [8, 9, 10]],target = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -2, -1], [0, 3, 5], [8, 9, 10]],target = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10000, -9999, -9998, -9997], [-9996, -9995, -9994, -9993], [-9992, -9991, -9990, -9989], [-9988, -9987, -9986, -9985]],target = -9990) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10000, -9999, -9998, -9997], [-9996, -9995, -9994, -9993], [-9992, -9991, -9990, -9989], [-9988, -9987, -9986, -9985]],target = -9990) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]],target = -5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]],target = -5) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -8, -6, -4, -2], [0, 2, 4, 6, 8], [10, 12, 14, 16, 18], [20, 22, 24, 26, 28], [30, 32, 34, 36, 38]],target = -5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -8, -6, -4, -2], [0, 2, 4, 6, 8], [10, 12, 14, 16, 18], [20, 22, 24, 26, 28], [30, 32, 34, 36, 38]],target = -5) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10], [11], [12], [13], [14], [15]],target = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10], [11], [12], [13], [14], [15]],target = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [21, 23, 25, 27, 29, 31, 33, 35, 37, 39], [41, 43, 45, 47, 49, 51, 53, 55, 57, 59], [61, 63, 65, 67, 69, 71, 73, 75, 77, 79]],target = 40) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [21, 23, 25, 27, 29, 31, 33, 35, 37, 39], [41, 43, 45, 47, 49, 51, 53, 55, 57, 59], [61, 63, 65, 67, 69, 71, 73, 75, 77, 79]],target = 40) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],target = 51) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],target = 51) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = -2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = -2) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1], [2], [3]],target = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1], [2], [3]],target = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -3, -1, 1, 3], [5, 7, 9, 11, 13], [15, 17, 19, 21, 23], [25, 27, 29, 31, 33], [35, 37, 39, 41, 43]],target = 42) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -3, -1, 1, 3], [5, 7, 9, 11, 13], [15, 17, 19, 21, 23], [25, 27, 29, 31, 33], [35, 37, 39, 41, 43]],target = 42) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]],target = 75) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]],target = 75) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 50) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 50) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 5, 9, 13, 17, 21], [25, 29, 33, 37, 41, 45], [49, 53, 57, 61, 65, 69], [73, 77, 81, 85, 89, 93], [97, 101, 105, 109, 113, 117]],target = 97) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 5, 9, 13, 17, 21], [25, 29, 33, 37, 41, 45], [49, 53, 57, 61, 65, 69], [73, 77, 81, 85, 89, 93], [97, 101, 105, 109, 113, 117]],target = 97) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-9999, -9997, -9995, -9993], [-9991, -9989, -9987, -9985], [-9983, -9981, -9979, -9977], [-9975, -9973, -9971, -9969]],target = -9996) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-9999, -9997, -9995, -9993], [-9991, -9989, -9987, -9985], [-9983, -9981, -9979, -9977], [-9975, -9973, -9971, -9969]],target = -9996) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],target = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],target = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = -300) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = -300) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10000]],target = 10000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10000]],target = 10000) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009], [1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019], [1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029], [1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039]],target = 1025) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009], [1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019], [1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029], [1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039]],target = 1025) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3]],target = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3]],target = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = -5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = -5) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10000, -9999, -9998], [-9997, -9996, -9995], [-9994, -9993, -9992], [-9991, -9990, -9989], [-9988, -9987, -9986]],target = -9992) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10000, -9999, -9998], [-9997, -9996, -9995], [-9994, -9993, -9992], [-9991, -9990, -9989], [-9988, -9987, -9986]],target = -9992) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = 2000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = 2000) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],target = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],target = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [70, 71, 72, 73]],target = 70) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [70, 71, 72, 73]],target = 70) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]],target = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]],target = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29]],target = 29) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29]],target = 29) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10000, -9000, -8000, -7000], [-6000, -5000, -4000, -3000], [-2000, -1000, 0, 1000], [2000, 3000, 4000, 5000]],target = -5000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10000, -9000, -8000, -7000], [-6000, -5000, -4000, -3000], [-2000, -1000, 0, 1000], [2000, 3000, 4000, 5000]],target = -5000) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 1, 3], [5, 7, 9], [11, 13, 15]],target = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 1, 3], [5, 7, 9], [11, 13, 15]],target = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -900, -800], [-700, -600, -500], [-400, -300, -200], [-100, -50, 0], [50, 100, 150]],target = -450) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -900, -800], [-700, -600, -500], [-400, -300, -200], [-100, -50, 0], [50, 100, 150]],target = -450) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]],target = 42) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]],target = 42) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]],target = 17) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]],target = 17) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-3, -2, -1, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24]],target = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-3, -2, -1, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24]],target = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986], [-985, -984, -983, -982, -981]],target = -993) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986], [-985, -984, -983, -982, -981]],target = -993) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13], [15, 17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39, 41]],target = 28) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13], [15, 17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39, 41]],target = 28) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10000, 10001, 10002], [10003, 10004, 10005], [10006, 10007, 10008]],target = 10004) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10000, 10001, 10002], [10003, 10004, 10005], [10006, 10007, 10008]],target = 10004) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-50, -49, -48, -47, -46], [-45, -44, -43, -42, -41], [-40, -39, -38, -37, -36], [-35, -34, -33, -32, -31], [-30, -29, -28, -27, -26]],target = -33) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-50, -49, -48, -47, -46], [-45, -44, -43, -42, -41], [-40, -39, -38, -37, -36], [-35, -34, -33, -32, -31], [-30, -29, -28, -27, -26]],target = -33) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -101) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -101) == False: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 26) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 26) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20]],target = 10) == True
    assert candidate(matrix = [[-10, -5, -3], [0, 3, 10], [15, 20, 25]],target = 3) == True
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 0) == True
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 5) == True
    assert candidate(matrix = [[1]],target = 1) == True
    assert candidate(matrix = [[-10, -8, -6, -4], [-3, -1, 1, 3], [5, 7, 9, 11]],target = 10) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],target = 0) == False
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 20) == True
    assert candidate(matrix = [[-10, -8, -6, -4], [-3, -1, 1, 3], [5, 7, 9, 11]],target = -5) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],target = 8) == True
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 13) == False
    assert candidate(matrix = [[1]],target = 2) == False
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [8, 9, 10, 12]],target = -3) == True
    assert candidate(matrix = [[1, 3, 5, 7]],target = 5) == True
    assert candidate(matrix = [[-10, -5, -3], [0, 3, 10], [15, 20, 25]],target = 1) == False
    assert candidate(matrix = [[1, 3, 5]],target = 5) == True
    assert candidate(matrix = [[-10, -5, -3, -2], [-1, 0, 2, 3], [4, 5, 7, 8]],target = 11) == False
    assert candidate(matrix = [[1]],target = 0) == False
    assert candidate(matrix = [[1, 3]],target = 3) == True
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = -10) == True
    assert candidate(matrix = [[1, 3, 5, 7]],target = 8) == False
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 10) == False
    assert candidate(matrix = [[-10, -5, -3, -2], [-1, 0, 2, 3], [4, 5, 7, 8]],target = -3) == True
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 0) == False
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [8, 9, 10, 12]],target = 15) == False
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 21) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 3) == True
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = 11) == True
    assert candidate(matrix = [[-10, -5, -3, -1], [0, 2, 3, 5], [7, 8, 11, 13], [15, 16, 18, 20]],target = -11) == False
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 6) == True
    assert candidate(matrix = [[1, 3, 5]],target = 6) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 60) == True
    assert candidate(matrix = [[1, 3]],target = 1) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],target = 10) == True
    assert candidate(matrix = [[1, 3]],target = 2) == False
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 7) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 1) == True
    assert candidate(matrix = [[-1000, -950, -900, -850], [-800, -750, -700, -650], [-600, -550, -500, -450], [-400, -350, -300, -250], [-200, -150, -100, -50]],target = -325) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 1) == True
    assert candidate(matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]],target = 18) == False
    assert candidate(matrix = [[-10, -5, 0, 5, 10], [-4, -2, 2, 4, 8], [6, 7, 12, 13, 14], [15, 16, 18, 19, 20], [21, 22, 23, 24, 25]],target = 12) == True
    assert candidate(matrix = [[-1, 0, 1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13], [14, 15, 16, 17, 18], [19, 20, 21, 22, 23]],target = 0) == True
    assert candidate(matrix = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], [160, 170, 180, 190, 200]],target = 150) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15], [17, 19, 21, 23, 25, 27, 29, 31], [33, 35, 37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59, 61, 63]],target = 62) == False
    assert candidate(matrix = [[-10000]],target = -10000) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],target = 25) == True
    assert candidate(matrix = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]],target = 20) == True
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 35) == False
    assert candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = 5) == False
    assert candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = 0) == False
    assert candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = -88) == True
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],target = 10) == True
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 61) == False
    assert candidate(matrix = [[-4, -3, -2, -1, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = -2) == True
    assert candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 5) == False
    assert candidate(matrix = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [16, 19, 22, 25, 28], [17, 20, 23, 26, 29]],target = 18) == False
    assert candidate(matrix = [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23], [25, 27, 29, 31], [33, 35, 37, 39], [41, 43, 45, 47], [49, 51, 53, 55], [57, 59, 61, 63]],target = 64) == False
    assert candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -55) == False
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59], [61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89], [91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119]],target = 119) == True
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = -6) == False
    assert candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = 61) == False
    assert candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 5) == False
    assert candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -45) == False
    assert candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = -83) == True
    assert candidate(matrix = [[-5, -2, -1], [0, 3, 5], [8, 9, 10]],target = -3) == False
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]],target = 1) == True
    assert candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 20) == False
    assert candidate(matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]],target = 14) == False
    assert candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986], [-985, -984, -983, -982, -981], [-980, -979, -978, -977, -976]],target = -987) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 38) == False
    assert candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 20) == False
    assert candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986]],target = -987) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 15) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 0) == False
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30], [31, 32, 33]],target = 17) == True
    assert candidate(matrix = [[-100, -99, -98, -97], [-96, -95, -94, -93], [-92, -91, -90, -89], [-88, -87, -86, -85]],target = -90) == True
    assert candidate(matrix = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],target = -1) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39]],target = 20) == False
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11], [13, 15, 17, 19, 21, 23], [25, 27, 29, 31, 33, 35], [37, 39, 41, 43, 45, 47], [49, 51, 53, 55, 57, 59]],target = 30) == False
    assert candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 25) == False
    assert candidate(matrix = [[10, 11, 12, 13, 14, 15]],target = 15) == True
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = 10) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 27) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 13) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 31) == False
    assert candidate(matrix = [[-100, -90, -80, -70, -60], [-50, -40, -30, -20, -10], [0, 10, 20, 30, 40], [50, 60, 70, 80, 90], [100, 110, 120, 130, 140]],target = -35) == False
    assert candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = 45) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]],target = 22) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]],target = 25) == True
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 35) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68]],target = 68) == True
    assert candidate(matrix = [[-100, -98, -95, -93], [-88, -86, -82, -80], [-74, -70, -66, -62], [-58, -54, -50, -46]],target = -66) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 26) == False
    assert candidate(matrix = [[1, 5, 9, 13], [17, 21, 25, 29], [33, 37, 41, 45], [49, 53, 57, 61]],target = 18) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [61, 62, 63, 64], [65, 66, 67, 68], [69, 70, 71, 72]],target = 67) == True
    assert candidate(matrix = [[-5, -2, -1], [0, 3, 5], [8, 9, 10]],target = 11) == False
    assert candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = 0) == True
    assert candidate(matrix = [[-10000, -9999, -9998, -9997], [-9996, -9995, -9994, -9993], [-9992, -9991, -9990, -9989], [-9988, -9987, -9986, -9985]],target = -9990) == True
    assert candidate(matrix = [[-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]],target = -5) == True
    assert candidate(matrix = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]],target = 0) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],target = 0) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 13) == True
    assert candidate(matrix = [[-10, -8, -6, -4, -2], [0, 2, 4, 6, 8], [10, 12, 14, 16, 18], [20, 22, 24, 26, 28], [30, 32, 34, 36, 38]],target = -5) == False
    assert candidate(matrix = [[10], [11], [12], [13], [14], [15]],target = 15) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [21, 23, 25, 27, 29, 31, 33, 35, 37, 39], [41, 43, 45, 47, 49, 51, 53, 55, 57, 59], [61, 63, 65, 67, 69, 71, 73, 75, 77, 79]],target = 40) == False
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 1) == True
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]],target = 51) == False
    assert candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = 0) == True
    assert candidate(matrix = [[-1, 0, 3, 5, 9, 12], [13, 18, 20, 23, 28, 31], [32, 34, 36, 39, 42, 45], [46, 48, 51, 54, 57, 60]],target = -2) == False
    assert candidate(matrix = [[1], [2], [3]],target = 2) == True
    assert candidate(matrix = [[-5, -3, -1, 1, 3], [5, 7, 9, 11, 13], [15, 17, 19, 21, 23], [25, 27, 29, 31, 33], [35, 37, 39, 41, 43]],target = 42) == False
    assert candidate(matrix = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]],target = 75) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49]],target = 50) == False
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = -1) == True
    assert candidate(matrix = [[1, 5, 9, 13, 17, 21], [25, 29, 33, 37, 41, 45], [49, 53, 57, 61, 65, 69], [73, 77, 81, 85, 89, 93], [97, 101, 105, 109, 113, 117]],target = 97) == True
    assert candidate(matrix = [[-9999, -9997, -9995, -9993], [-9991, -9989, -9987, -9985], [-9983, -9981, -9979, -9977], [-9975, -9973, -9971, -9969]],target = -9996) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],target = 5) == True
    assert candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = -300) == False
    assert candidate(matrix = [[10000]],target = 10000) == True
    assert candidate(matrix = [[1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009], [1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019], [1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029], [1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039]],target = 1025) == True
    assert candidate(matrix = [[1, 2, 3]],target = 2) == True
    assert candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = -5) == False
    assert candidate(matrix = [[-10000, -9999, -9998], [-9997, -9996, -9995], [-9994, -9993, -9992], [-9991, -9990, -9989], [-9988, -9987, -9986]],target = -9992) == True
    assert candidate(matrix = [[-1000, -500, -250, -100], [-50, -25, -10, 0], [5, 10, 25, 50], [100, 250, 500, 1000]],target = 2000) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],target = 11) == False
    assert candidate(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [70, 71, 72, 73]],target = 70) == True
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]],target = 18) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29]],target = 29) == True
    assert candidate(matrix = [[-10000, -9000, -8000, -7000], [-6000, -5000, -4000, -3000], [-2000, -1000, 0, 1000], [2000, 3000, 4000, 5000]],target = -5000) == True
    assert candidate(matrix = [[-1, 1, 3], [5, 7, 9], [11, 13, 15]],target = 0) == False
    assert candidate(matrix = [[-1000, -900, -800], [-700, -600, -500], [-400, -300, -200], [-100, -50, 0], [50, 100, 150]],target = -450) == False
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]],target = 42) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],target = 25) == True
    assert candidate(matrix = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]],target = 17) == True
    assert candidate(matrix = [[-3, -2, -1, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24]],target = 13) == True
    assert candidate(matrix = [[-1000, -999, -998, -997, -996], [-995, -994, -993, -992, -991], [-990, -989, -988, -987, -986], [-985, -984, -983, -982, -981]],target = -993) == True
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13], [15, 17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39, 41]],target = 28) == False
    assert candidate(matrix = [[10000, 10001, 10002], [10003, 10004, 10005], [10006, 10007, 10008]],target = 10004) == True
    assert candidate(matrix = [[-50, -49, -48, -47, -46], [-45, -44, -43, -42, -41], [-40, -39, -38, -37, -36], [-35, -34, -33, -32, -31], [-30, -29, -28, -27, -26]],target = -33) == True
    assert candidate(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],target = 31) == False
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],target = 9) == True
    assert candidate(matrix = [[-100, -90, -80, -70], [-60, -50, -40, -30], [-20, -10, 0, 10], [20, 30, 40, 50]],target = -101) == False
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 26) == False


