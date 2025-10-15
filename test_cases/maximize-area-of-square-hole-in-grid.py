def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1,m = 1,hBars = [2],vBars = [2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 1,hBars = [2],vBars = [2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 3,hBars = [2, 3],vBars = [2, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 3,hBars = [2, 3],vBars = [2, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 1,hBars = [2, 3],vBars = [2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 1,hBars = [2, 3],vBars = [2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [3, 5, 7],vBars = [4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [3, 5, 7],vBars = [4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 10,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],vBars = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 10,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],vBars = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 15,hBars = [3, 5, 7, 9, 11],vBars = [3, 5, 7, 9, 11]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 15,hBars = [3, 5, 7, 9, 11],vBars = [3, 5, 7, 9, 11]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,hBars = [5, 7, 9, 11, 13, 15, 17, 19],vBars = [6, 8, 10, 12, 14, 16, 18, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,hBars = [5, 7, 9, 11, 13, 15, 17, 19],vBars = [6, 8, 10, 12, 14, 16, 18, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 15,hBars = [3, 5, 7, 9, 11, 13, 15],vBars = [3, 5, 7, 9, 11, 13, 15]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 15,hBars = [3, 5, 7, 9, 11, 13, 15],vBars = [3, 5, 7, 9, 11, 13, 15]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 3, 5, 6],vBars = [3, 5, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 3, 5, 6],vBars = [3, 5, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 10,hBars = [2, 4, 6, 8, 10],vBars = [3, 6, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 10,hBars = [2, 4, 6, 8, 10],vBars = [3, 6, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 6,hBars = [2, 3, 5, 7, 8],vBars = [2, 4, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 6,hBars = [2, 3, 5, 7, 8],vBars = [2, 4, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 50,hBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],vBars = [10, 20, 30, 40, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 50,hBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],vBars = [10, 20, 30, 40, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 20,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 20,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 4,hBars = [2, 3, 4, 5, 6],vBars = [2, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 4,hBars = [2, 3, 4, 5, 6],vBars = [2, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 6,hBars = [2, 4, 5, 7],vBars = [2, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 6,hBars = [2, 4, 5, 7],vBars = [2, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 2,hBars = [2, 3],vBars = [2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 2,hBars = [2, 3],vBars = [2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,m = 30,hBars = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],vBars = [5, 7, 9, 11, 13, 15]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,m = 30,hBars = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],vBars = [5, 7, 9, 11, 13, 15]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 200,hBars = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],vBars = [40, 60, 80, 100, 120, 140, 160, 180, 200]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 200,hBars = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],vBars = [40, 60, 80, 100, 120, 140, 160, 180, 200]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 25,hBars = [5, 10, 15, 20, 25],vBars = [5, 10, 15, 20, 25]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 25,hBars = [5, 10, 15, 20, 25],vBars = [5, 10, 15, 20, 25]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 3, 5, 7, 9],vBars = [2, 3, 5, 7, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 3, 5, 7, 9],vBars = [2, 3, 5, 7, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 25,hBars = [2, 5, 7, 10, 13, 15, 18, 20, 23],vBars = [3, 6, 9, 12, 15, 18, 21, 24]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 25,hBars = [2, 5, 7, 10, 13, 15, 18, 20, 23],vBars = [3, 6, 9, 12, 15, 18, 21, 24]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,hBars = [2, 3, 5, 7, 8, 9],vBars = [2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,hBars = [2, 3, 5, 7, 8, 9],vBars = [2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,hBars = [3, 6, 9],vBars = [3, 6, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,hBars = [3, 6, 9],vBars = [3, 6, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,hBars = [10, 15, 20, 25, 30, 35, 40, 45, 50],vBars = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,hBars = [10, 15, 20, 25, 30, 35, 40, 45, 50],vBars = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,m = 150,hBars = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],vBars = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,m = 150,hBars = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],vBars = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,hBars = [2, 50, 51, 52, 100],vBars = [2, 50, 51, 52, 100]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,hBars = [2, 50, 51, 52, 100],vBars = [2, 50, 51, 52, 100]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [3, 5, 7],vBars = [3, 5, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [3, 5, 7],vBars = [3, 5, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 3,hBars = [2, 3],vBars = [2, 3, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 3,hBars = [2, 3],vBars = [2, 3, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 20,hBars = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],vBars = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 20,hBars = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],vBars = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 25,hBars = [6, 12, 18, 24],vBars = [5, 10, 15, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 25,hBars = [6, 12, 18, 24],vBars = [5, 10, 15, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 3, 5, 7, 9],vBars = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 3, 5, 7, 9],vBars = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 8,hBars = [2, 3, 5, 6, 7],vBars = [2, 3, 5, 6, 7]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 8,hBars = [2, 3, 5, 6, 7],vBars = [2, 3, 5, 6, 7]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,hBars = [2, 4, 5],vBars = [2, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,hBars = [2, 4, 5],vBars = [2, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,m = 100,hBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],vBars = [20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,m = 100,hBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],vBars = [20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 3,hBars = [2, 3, 4, 5],vBars = [2, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 3,hBars = [2, 3, 4, 5],vBars = [2, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,hBars = [2, 25, 26, 50],vBars = [2, 25, 26, 50]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,hBars = [2, 25, 26, 50],vBars = [2, 25, 26, 50]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,hBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],vBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,hBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],vBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,hBars = [2, 3, 4, 5],vBars = [2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,hBars = [2, 3, 4, 5],vBars = [2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 20,hBars = [2, 3, 4, 5, 6],vBars = [5, 10, 15, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 20,hBars = [2, 3, 4, 5, 6],vBars = [5, 10, 15, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 10,hBars = [3, 5, 7, 9, 11, 13, 15],vBars = [3, 5, 7, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 10,hBars = [3, 5, 7, 9, 11, 13, 15],vBars = [3, 5, 7, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7,hBars = [3, 4, 5],vBars = [3, 4, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7,hBars = [3, 4, 5],vBars = [3, 4, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 20,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10],vBars = [2, 4, 6, 8, 10, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 20,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10],vBars = [2, 4, 6, 8, 10, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 4,hBars = [2, 4, 5],vBars = [2, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 4,hBars = [2, 4, 5],vBars = [2, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,m = 50,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,m = 50,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7,hBars = [2, 3, 5, 6],vBars = [2, 4, 5, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7,hBars = [2, 3, 5, 6],vBars = [2, 4, 5, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7,hBars = [3, 4, 5, 6],vBars = [3, 4, 5, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7,hBars = [3, 4, 5, 6],vBars = [3, 4, 5, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 4, 6, 8, 10, 12],vBars = [2, 4, 6, 8, 10, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 4, 6, 8, 10, 12],vBars = [2, 4, 6, 8, 10, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 5,hBars = [3, 4, 5, 7, 8],vBars = [2, 4, 5, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 5,hBars = [3, 4, 5, 7, 8],vBars = [2, 4, 5, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,hBars = [2, 3, 5, 6, 8, 9],vBars = [2, 3, 5, 6, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,hBars = [2, 3, 5, 6, 8, 9],vBars = [2, 3, 5, 6, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 12,hBars = [2, 4, 6, 8, 10],vBars = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 12,hBars = [2, 4, 6, 8, 10],vBars = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 10,hBars = [2, 4, 6, 8, 10, 12, 14],vBars = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 10,hBars = [2, 4, 6, 8, 10, 12, 14],vBars = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 3, 4, 5],vBars = [2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 3, 4, 5],vBars = [2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7,hBars = [3, 5, 6],vBars = [3, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7,hBars = [3, 5, 6],vBars = [3, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,m = 20,hBars = [5, 10, 15, 20],vBars = [4, 8, 12, 16]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,m = 20,hBars = [5, 10, 15, 20],vBars = [4, 8, 12, 16]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,hBars = [10, 20, 30, 40, 50],vBars = [15, 25, 35, 45, 55]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,hBars = [10, 20, 30, 40, 50],vBars = [15, 25, 35, 45, 55]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 8,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 8,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 6,hBars = [2, 3, 4, 5],vBars = [2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 6,hBars = [2, 3, 4, 5],vBars = [2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 3,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 3,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 3,hBars = [2, 3, 4],vBars = [2, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 3,hBars = [2, 3, 4],vBars = [2, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10,hBars = [2, 4, 6, 8, 10],vBars = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10,hBars = [2, 4, 6, 8, 10],vBars = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 8,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 8,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,hBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],vBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,hBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],vBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 6,hBars = [2, 3, 4, 5, 6, 7, 8],vBars = [2, 3, 4, 5, 6, 7, 8]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 6,hBars = [2, 3, 4, 5, 6, 7, 8],vBars = [2, 3, 4, 5, 6, 7, 8]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 4,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 4,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 15,hBars = [3, 6, 9, 12, 15, 18, 21],vBars = [3, 6, 9, 12, 15, 18]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 15,hBars = [3, 6, 9, 12, 15, 18, 21],vBars = [3, 6, 9, 12, 15, 18]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 12,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 12,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 6,hBars = [2, 3, 4, 5, 6],vBars = [2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 6,hBars = [2, 3, 4, 5, 6],vBars = [2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,hBars = [2, 3, 5, 7, 9],vBars = [2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,hBars = [2, 3, 5, 7, 9],vBars = [2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 12,hBars = [2, 3, 5, 7, 9, 11, 13, 15],vBars = [2, 3, 5, 7, 9, 11, 13, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 12,hBars = [2, 3, 5, 7, 9, 11, 13, 15],vBars = [2, 3, 5, 7, 9, 11, 13, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 10,hBars = [5, 6, 7, 8, 9, 10, 12],vBars = [4, 6, 7, 9, 10, 12, 14]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 10,hBars = [5, 6, 7, 8, 9, 10, 12],vBars = [4, 6, 7, 9, 10, 12, 14]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 4,hBars = [2, 3],vBars = [2, 3, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 4,hBars = [2, 3],vBars = [2, 3, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,hBars = [50, 51, 52, 53, 54],vBars = [50, 51, 52, 53, 54]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,hBars = [50, 51, 52, 53, 54],vBars = [50, 51, 52, 53, 54]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 3,hBars = [2, 3, 4, 5],vBars = [2, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 3,hBars = [2, 3, 4, 5],vBars = [2, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7,hBars = [2, 3, 5, 6],vBars = [2, 3, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7,hBars = [2, 3, 5, 6],vBars = [2, 3, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 3,hBars = [2, 3],vBars = [2, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 3,hBars = [2, 3],vBars = [2, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 30,hBars = [10, 12, 13, 15],vBars = [15, 16, 18, 20]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 30,hBars = [10, 12, 13, 15],vBars = [15, 16, 18, 20]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 4,hBars = [2, 3, 5],vBars = [2, 3, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 4,hBars = [2, 3, 5],vBars = [2, 3, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 7,hBars = [3, 5, 6],vBars = [3, 5, 6, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 7,hBars = [3, 5, 6],vBars = [3, 5, 6, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 10,hBars = [2, 3, 5, 7, 9, 11, 13, 15],vBars = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 10,hBars = [2, 3, 5, 7, 9, 11, 13, 15],vBars = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 5,hBars = [2, 3, 5],vBars = [2, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 5,hBars = [2, 3, 5],vBars = [2, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 4,hBars = [2, 3, 4],vBars = [2, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 4,hBars = [2, 3, 4],vBars = [2, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 15,hBars = [2, 3, 4, 6, 8, 10, 12],vBars = [3, 5, 7, 9, 11, 13, 15]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 15,hBars = [2, 3, 4, 6, 8, 10, 12],vBars = [3, 5, 7, 9, 11, 13, 15]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 1,hBars = [],vBars = []) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 1,hBars = [],vBars = []) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 2,hBars = [2, 3, 4],vBars = [2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 2,hBars = [2, 3, 4],vBars = [2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,m = 40,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]) == 961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,m = 40,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]) == 961: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 100,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 100,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 50,hBars = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],vBars = [10, 15, 20, 25, 30, 35, 40]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 50,hBars = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],vBars = [10, 15, 20, 25, 30, 35, 40]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 5,hBars = [3, 4, 5, 6],vBars = [3, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 5,hBars = [3, 4, 5, 6],vBars = [3, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 5,hBars = [2, 3, 4, 5, 6],vBars = [2, 3, 4, 5, 6]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 5,hBars = [2, 3, 4, 5, 6],vBars = [2, 3, 4, 5, 6]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 6,hBars = [2, 4],vBars = [2, 3, 4, 5, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 6,hBars = [2, 4],vBars = [2, 3, 4, 5, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 12,hBars = [3, 6, 9, 12],vBars = [3, 6, 9, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 12,hBars = [3, 6, 9, 12],vBars = [3, 6, 9, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 6,hBars = [2, 3, 5, 6],vBars = [2, 4, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 6,hBars = [2, 3, 5, 6],vBars = [2, 4, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9,hBars = [2, 3, 4, 5, 6, 7, 8],vBars = [2, 3, 4, 5, 6, 7, 8]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9,hBars = [2, 3, 4, 5, 6, 7, 8],vBars = [2, 3, 4, 5, 6, 7, 8]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,m = 15,hBars = [3, 4, 5, 7, 8],vBars = [5, 6, 7, 9, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,m = 15,hBars = [3, 4, 5, 7, 8],vBars = [5, 6, 7, 9, 10]) == 16: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1,m = 1,hBars = [2],vBars = [2]) == 4
    assert candidate(n = 2,m = 3,hBars = [2, 3],vBars = [2, 4]) == 4
    assert candidate(n = 2,m = 1,hBars = [2, 3],vBars = [2]) == 4
    assert candidate(n = 5,m = 5,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
    assert candidate(n = 10,m = 10,hBars = [3, 5, 7],vBars = [4, 6, 8]) == 4
    assert candidate(n = 20,m = 10,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],vBars = [2, 4, 6, 8, 10]) == 4
    assert candidate(n = 15,m = 15,hBars = [3, 5, 7, 9, 11],vBars = [3, 5, 7, 9, 11]) == 4
    assert candidate(n = 20,m = 15,hBars = [5, 7, 9, 11, 13, 15, 17, 19],vBars = [6, 8, 10, 12, 14, 16, 18, 20]) == 4
    assert candidate(n = 15,m = 15,hBars = [3, 5, 7, 9, 11, 13, 15],vBars = [3, 5, 7, 9, 11, 13, 15]) == 4
    assert candidate(n = 10,m = 10,hBars = [2, 3, 5, 6],vBars = [3, 5, 7]) == 4
    assert candidate(n = 20,m = 10,hBars = [2, 4, 6, 8, 10],vBars = [3, 6, 9]) == 4
    assert candidate(n = 8,m = 6,hBars = [2, 3, 5, 7, 8],vBars = [2, 4, 6]) == 4
    assert candidate(n = 100,m = 50,hBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],vBars = [10, 20, 30, 40, 50]) == 4
    assert candidate(n = 20,m = 20,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4
    assert candidate(n = 20,m = 20,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 400
    assert candidate(n = 6,m = 4,hBars = [2, 3, 4, 5, 6],vBars = [2, 4]) == 4
    assert candidate(n = 7,m = 6,hBars = [2, 4, 5, 7],vBars = [2, 4, 5]) == 9
    assert candidate(n = 3,m = 2,hBars = [2, 3],vBars = [2]) == 4
    assert candidate(n = 40,m = 30,hBars = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],vBars = [5, 7, 9, 11, 13, 15]) == 4
    assert candidate(n = 300,m = 200,hBars = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],vBars = [40, 60, 80, 100, 120, 140, 160, 180, 200]) == 4
    assert candidate(n = 25,m = 25,hBars = [5, 10, 15, 20, 25],vBars = [5, 10, 15, 20, 25]) == 4
    assert candidate(n = 10,m = 10,hBars = [2, 3, 5, 7, 9],vBars = [2, 3, 5, 7, 9]) == 9
    assert candidate(n = 25,m = 25,hBars = [2, 5, 7, 10, 13, 15, 18, 20, 23],vBars = [3, 6, 9, 12, 15, 18, 21, 24]) == 4
    assert candidate(n = 9,m = 9,hBars = [2, 3, 5, 7, 8, 9],vBars = [2, 4, 6, 8]) == 4
    assert candidate(n = 9,m = 9,hBars = [3, 6, 9],vBars = [3, 6, 9]) == 4
    assert candidate(n = 50,m = 50,hBars = [10, 15, 20, 25, 30, 35, 40, 45, 50],vBars = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 4
    assert candidate(n = 200,m = 150,hBars = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],vBars = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 4
    assert candidate(n = 20,m = 15,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14]) == 4
    assert candidate(n = 100,m = 100,hBars = [2, 50, 51, 52, 100],vBars = [2, 50, 51, 52, 100]) == 16
    assert candidate(n = 10,m = 10,hBars = [3, 5, 7],vBars = [3, 5, 7]) == 4
    assert candidate(n = 3,m = 3,hBars = [2, 3],vBars = [2, 3, 4]) == 9
    assert candidate(n = 25,m = 20,hBars = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],vBars = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 9
    assert candidate(n = 30,m = 25,hBars = [6, 12, 18, 24],vBars = [5, 10, 15, 20]) == 4
    assert candidate(n = 10,m = 10,hBars = [2, 3, 5, 7, 9],vBars = [2, 4, 6, 8, 10]) == 4
    assert candidate(n = 8,m = 8,hBars = [2, 3, 5, 6, 7],vBars = [2, 3, 5, 6, 7]) == 16
    assert candidate(n = 5,m = 5,hBars = [2, 4, 5],vBars = [2, 4]) == 4
    assert candidate(n = 150,m = 100,hBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],vBars = [20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
    assert candidate(n = 6,m = 3,hBars = [2, 3, 4, 5],vBars = [2, 3]) == 9
    assert candidate(n = 50,m = 50,hBars = [2, 25, 26, 50],vBars = [2, 25, 26, 50]) == 9
    assert candidate(n = 50,m = 50,hBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],vBars = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 4
    assert candidate(n = 5,m = 5,hBars = [2, 3, 4, 5],vBars = [2, 3, 4]) == 16
    assert candidate(n = 10,m = 20,hBars = [2, 3, 4, 5, 6],vBars = [5, 10, 15, 20]) == 4
    assert candidate(n = 15,m = 10,hBars = [3, 5, 7, 9, 11, 13, 15],vBars = [3, 5, 7, 9]) == 4
    assert candidate(n = 9,m = 9,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(n = 7,m = 7,hBars = [3, 4, 5],vBars = [3, 4, 5]) == 16
    assert candidate(n = 30,m = 20,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10],vBars = [2, 4, 6, 8, 10, 12]) == 4
    assert candidate(n = 5,m = 4,hBars = [2, 4, 5],vBars = [2, 4]) == 4
    assert candidate(n = 50,m = 50,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 4
    assert candidate(n = 10,m = 10,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4
    assert candidate(n = 7,m = 7,hBars = [2, 3, 5, 6],vBars = [2, 4, 5, 7]) == 9
    assert candidate(n = 7,m = 7,hBars = [3, 4, 5, 6],vBars = [3, 4, 5, 6]) == 25
    assert candidate(n = 10,m = 10,hBars = [2, 4, 6, 8, 10, 12],vBars = [2, 4, 6, 8, 10, 12]) == 4
    assert candidate(n = 10,m = 5,hBars = [3, 4, 5, 7, 8],vBars = [2, 4, 5, 7]) == 9
    assert candidate(n = 9,m = 9,hBars = [2, 3, 5, 6, 8, 9],vBars = [2, 3, 5, 6, 8, 9]) == 9
    assert candidate(n = 12,m = 12,hBars = [2, 4, 6, 8, 10],vBars = [2, 4, 6, 8, 10]) == 4
    assert candidate(n = 15,m = 10,hBars = [2, 4, 6, 8, 10, 12, 14],vBars = [2, 4, 6, 8, 10]) == 4
    assert candidate(n = 10,m = 10,hBars = [2, 3, 4, 5],vBars = [2, 3, 4, 5]) == 25
    assert candidate(n = 7,m = 7,hBars = [3, 5, 6],vBars = [3, 5, 6]) == 9
    assert candidate(n = 25,m = 20,hBars = [5, 10, 15, 20],vBars = [4, 8, 12, 16]) == 4
    assert candidate(n = 100,m = 100,hBars = [10, 20, 30, 40, 50],vBars = [15, 25, 35, 45, 55]) == 4
    assert candidate(n = 8,m = 8,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4
    assert candidate(n = 6,m = 6,hBars = [2, 3, 4, 5],vBars = [2, 3, 4, 5]) == 25
    assert candidate(n = 3,m = 3,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
    assert candidate(n = 4,m = 3,hBars = [2, 3, 4],vBars = [2, 3]) == 9
    assert candidate(n = 10,m = 10,hBars = [2, 4, 6, 8, 10],vBars = [2, 4, 6, 8, 10]) == 4
    assert candidate(n = 10,m = 8,hBars = [2, 4, 6, 8],vBars = [2, 4, 6, 8]) == 4
    assert candidate(n = 100,m = 100,hBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],vBars = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
    assert candidate(n = 8,m = 6,hBars = [2, 3, 4, 5, 6, 7, 8],vBars = [2, 3, 4, 5, 6, 7, 8]) == 64
    assert candidate(n = 5,m = 4,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
    assert candidate(n = 20,m = 15,hBars = [3, 6, 9, 12, 15, 18, 21],vBars = [3, 6, 9, 12, 15, 18]) == 4
    assert candidate(n = 12,m = 12,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 121
    assert candidate(n = 7,m = 6,hBars = [2, 3, 4, 5, 6],vBars = [2, 3, 4, 5]) == 25
    assert candidate(n = 9,m = 9,hBars = [2, 3, 5, 7, 9],vBars = [2, 4, 6, 8]) == 4
    assert candidate(n = 15,m = 12,hBars = [2, 3, 5, 7, 9, 11, 13, 15],vBars = [2, 3, 5, 7, 9, 11, 13, 15]) == 9
    assert candidate(n = 15,m = 10,hBars = [5, 6, 7, 8, 9, 10, 12],vBars = [4, 6, 7, 9, 10, 12, 14]) == 9
    assert candidate(n = 3,m = 4,hBars = [2, 3],vBars = [2, 3, 4]) == 9
    assert candidate(n = 100,m = 100,hBars = [50, 51, 52, 53, 54],vBars = [50, 51, 52, 53, 54]) == 36
    assert candidate(n = 7,m = 3,hBars = [2, 3, 4, 5],vBars = [2, 3]) == 9
    assert candidate(n = 7,m = 7,hBars = [2, 3, 5, 6],vBars = [2, 3, 5, 6]) == 9
    assert candidate(n = 3,m = 3,hBars = [2, 3],vBars = [2, 3]) == 9
    assert candidate(n = 20,m = 30,hBars = [10, 12, 13, 15],vBars = [15, 16, 18, 20]) == 9
    assert candidate(n = 5,m = 5,hBars = [2, 3, 4],vBars = [2, 3, 4]) == 16
    assert candidate(n = 5,m = 4,hBars = [2, 3, 5],vBars = [2, 3, 4]) == 9
    assert candidate(n = 8,m = 7,hBars = [3, 5, 6],vBars = [3, 5, 6, 7]) == 9
    assert candidate(n = 15,m = 10,hBars = [2, 3, 5, 7, 9, 11, 13, 15],vBars = [2, 4, 6, 8, 10]) == 4
    assert candidate(n = 6,m = 5,hBars = [2, 3, 5],vBars = [2, 4, 5]) == 9
    assert candidate(n = 5,m = 4,hBars = [2, 3, 4],vBars = [2, 3]) == 9
    assert candidate(n = 12,m = 15,hBars = [2, 3, 4, 6, 8, 10, 12],vBars = [3, 5, 7, 9, 11, 13, 15]) == 4
    assert candidate(n = 1,m = 1,hBars = [],vBars = []) == 4
    assert candidate(n = 4,m = 2,hBars = [2, 3, 4],vBars = [2]) == 4
    assert candidate(n = 30,m = 40,hBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],vBars = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]) == 961
    assert candidate(n = 100,m = 100,hBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],vBars = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4
    assert candidate(n = 100,m = 50,hBars = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],vBars = [10, 15, 20, 25, 30, 35, 40]) == 4
    assert candidate(n = 10,m = 5,hBars = [3, 4, 5, 6],vBars = [3, 4]) == 9
    assert candidate(n = 5,m = 5,hBars = [2, 3, 4, 5, 6],vBars = [2, 3, 4, 5, 6]) == 36
    assert candidate(n = 4,m = 6,hBars = [2, 4],vBars = [2, 3, 4, 5, 6]) == 4
    assert candidate(n = 12,m = 12,hBars = [3, 6, 9, 12],vBars = [3, 6, 9, 12]) == 4
    assert candidate(n = 8,m = 6,hBars = [2, 3, 5, 6],vBars = [2, 4, 6]) == 4
    assert candidate(n = 9,m = 9,hBars = [2, 3, 4, 5, 6, 7, 8],vBars = [2, 3, 4, 5, 6, 7, 8]) == 64
    assert candidate(n = 15,m = 15,hBars = [3, 4, 5, 7, 8],vBars = [5, 6, 7, 9, 10]) == 16


