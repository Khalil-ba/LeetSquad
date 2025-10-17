def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8],k = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8],k = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0],k = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0],k = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6],k = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6],k = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -3, 3],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -3, 3],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -3, 3],k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -3, 3],k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6],k = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6],k = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9],k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9],k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0],k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0],k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],k = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],k = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230],k = 123) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230],k = 123) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],k = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],k = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],k = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],k = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 13) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16],k = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16],k = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],k = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],k = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 6, 6],k = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 6, 6],k = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],k = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],k = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 13) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100000) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 2000000000, -3000000000, 4000000000, 500000000, -600000000, 70000000, -80000000],k = 500000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 2000000000, -3000000000, 4000000000, 500000000, -600000000, 70000000, -80000000],k = 500000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 31) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 31) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115],k = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115],k = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 25) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 13) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16],k = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16],k = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 6, 8, 5, 7, 9, 11],k = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 6, 8, 5, 7, 9, 11],k = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 3, 2, 6, 8, 10, 9, 5, 1, 4],k = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 3, 2, 6, 8, 10, 9, 5, 1, 4],k = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],k = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],k = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12],k = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12],k = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],k = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],k = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],k = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],k = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, 1, 2, 3, 4],k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, 1, 2, 3, 4],k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, 10, 20, -20, 30, -30, 40, -40],k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, 10, 20, -20, 30, -30, 40, -40],k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 101) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 101) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],k = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],k = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 39) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 39) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8],k = 4) == True
    assert candidate(arr = [0, 0, 0, 0],k = 1) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6],k = 10) == False
    assert candidate(arr = [-1, 1, -2, 2, -3, 3],k = 2) == True
    assert candidate(arr = [-1, 1, -2, 2, -3, 3],k = 3) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6],k = 7) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 11) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9],k = 5) == True
    assert candidate(arr = [0, 0, 0, 0],k = 3) == True
    assert candidate(arr = [0, 0, 0, 0],k = 2) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 6) == False
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 8) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 10) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 7) == False
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == False
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],k = 20) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == True
    assert candidate(arr = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230],k = 123) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 25) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == True
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],k = 6) == False
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 10) == False
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],k = 3) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 17) == False
    assert candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],k = 3) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 13) == False
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 10) == False
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 7) == True
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16],k = 6) == False
    assert candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],k = 50) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == True
    assert candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 6, 6],k = 5) == False
    assert candidate(arr = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 15) == False
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == False
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],k = 15) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 13) == False
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100000) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == False
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 7) == False
    assert candidate(arr = [1000000000, 2000000000, -3000000000, 4000000000, 500000000, -600000000, 70000000, -80000000],k = 500000000) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 31) == True
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 20) == True
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 7) == True
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 4) == False
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 2) == True
    assert candidate(arr = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115],k = 6) == False
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 2) == True
    assert candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 10) == True
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 25) == False
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 11) == True
    assert candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 13) == False
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16],k = 5) == False
    assert candidate(arr = [1, 3, 2, 4, 6, 8, 5, 7, 9, 11],k = 3) == False
    assert candidate(arr = [7, 3, 2, 6, 8, 10, 9, 5, 1, 4],k = 7) == False
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],k = 5) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 5) == False
    assert candidate(arr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 10) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12],k = 5) == False
    assert candidate(arr = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == False
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],k = 20) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 5) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 8) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 13) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],k = 5) == False
    assert candidate(arr = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == True
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == True
    assert candidate(arr = [-1, -2, -3, -4, 1, 2, 3, 4],k = 3) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 15) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 20) == False
    assert candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 3) == True
    assert candidate(arr = [-10, 10, 20, -20, 30, -30, 40, -40],k = 10) == True
    assert candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == True
    assert candidate(arr = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 101) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],k = 19) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 39) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == True


