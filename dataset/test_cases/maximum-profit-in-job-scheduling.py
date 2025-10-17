def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(startTime = [1, 10, 4, 3, 8, 9],endTime = [2, 11, 5, 7, 9, 10],profit = [3, 1, 5, 6, 4, 3]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 10, 4, 3, 8, 9],endTime = [2, 11, 5, 7, 9, 10],profit = [3, 1, 5, 6, 4, 3]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 6, 7],endTime = [3, 5, 9, 8, 9],profit = [50, 20, 60, 40, 30]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 6, 7],endTime = [3, 5, 9, 8, 9],profit = [50, 20, 60, 40, 30]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 10, 100, 1000],endTime = [2, 20, 200, 2000],profit = [5, 50, 500, 5000]) == 5555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 10, 100, 1000],endTime = [2, 20, 200, 2000],profit = [5, 50, 500, 5000]) == 5555: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 8],endTime = [2, 5, 10, 12],profit = [50, 20, 100, 80]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 8],endTime = [2, 5, 10, 12],profit = [50, 20, 100, 80]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 1, 1, 2],endTime = [4, 2, 4, 3],profit = [50, 10, 40, 70]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 1, 1, 2],endTime = [4, 2, 4, 3],profit = [50, 10, 40, 70]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 5, 10],endTime = [15, 18, 19],profit = [20, 20, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 5, 10],endTime = [15, 18, 19],profit = [20, 20, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1],endTime = [2],profit = [5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1],endTime = [2],profit = [5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 8, 12, 14],endTime = [4, 5, 10, 11, 14, 15],profit = [5, 6, 8, 3, 10, 4]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 8, 12, 14],endTime = [4, 5, 10, 11, 14, 15],profit = [5, 6, 8, 3, 10, 4]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6],endTime = [2, 3, 4, 5, 6, 7],profit = [1, 2, 3, 4, 5, 6]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6],endTime = [2, 3, 4, 5, 6, 7],profit = [1, 2, 3, 4, 5, 6]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1],endTime = [2, 3, 4],profit = [5, 6, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1],endTime = [2, 3, 4],profit = [5, 6, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 3],endTime = [3, 4, 5, 6],profit = [50, 10, 40, 70]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 3],endTime = [3, 4, 5, 6],profit = [50, 10, 40, 70]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 6],endTime = [3, 5, 10, 6, 9],profit = [20, 20, 100, 70, 60]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 6],endTime = [3, 5, 10, 6, 9],profit = [20, 20, 100, 70, 60]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 8, 4, 1, 1],endTime = [6, 10, 7, 8, 2],profit = [100, 500, 100, 200, 300]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 8, 4, 1, 1],endTime = [6, 10, 7, 8, 2],profit = [100, 500, 100, 200, 300]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 8],endTime = [5, 7, 10, 12],profit = [50, 20, 100, 200]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 8],endTime = [5, 7, 10, 12],profit = [50, 20, 100, 200]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [2, 5, 8, 11],endTime = [5, 7, 10, 14],profit = [20, 30, 40, 50]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [2, 5, 8, 11],endTime = [5, 7, 10, 14],profit = [20, 30, 40, 50]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 10, 15, 20, 25],endTime = [10, 15, 20, 25, 30],profit = [100, 150, 200, 250, 300]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 10, 15, 20, 25],endTime = [10, 15, 20, 25, 30],profit = [100, 150, 200, 250, 300]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300],endTime = [200, 300, 400],profit = [1000, 2000, 3000]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300],endTime = [200, 300, 400],profit = [1000, 2000, 3000]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37],endTime = [5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30, 33, 34, 37, 38, 41, 42],profit = [100, 200, 150, 300, 100, 500, 400, 300, 600, 700, 800, 600, 400, 300, 200, 100, 900, 800, 700, 600]) == 3400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37],endTime = [5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30, 33, 34, 37, 38, 41, 42],profit = [100, 200, 150, 300, 100, 500, 400, 300, 600, 700, 800, 600, 400, 300, 200, 100, 900, 800, 700, 600]) == 3400: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [2, 3, 4, 5, 6, 7],profit = [100, 200, 300, 400, 500, 600]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [2, 3, 4, 5, 6, 7],profit = [100, 200, 300, 400, 500, 600]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 5, 6, 8, 10, 12, 14, 16],endTime = [5, 4, 6, 9, 8, 11, 13, 15, 17, 19],profit = [5, 3, 7, 9, 8, 6, 4, 2, 1, 10]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 5, 6, 8, 10, 12, 14, 16],endTime = [5, 4, 6, 9, 8, 11, 13, 15, 17, 19],profit = [5, 3, 7, 9, 8, 6, 4, 2, 1, 10]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7],endTime = [3, 4, 4, 5, 6, 7, 7, 8, 9, 10],profit = [50, 40, 30, 20, 60, 10, 20, 100, 5, 45]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7],endTime = [3, 4, 4, 5, 6, 7, 7, 8, 9, 10],profit = [50, 40, 30, 20, 60, 10, 20, 100, 5, 45]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],endTime = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],endTime = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 5, 8, 11, 13, 16, 19, 22, 25, 28],endTime = [4, 9, 12, 15, 17, 20, 23, 26, 29, 32],profit = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 5, 8, 11, 13, 16, 19, 22, 25, 28],endTime = [4, 9, 12, 15, 17, 20, 23, 26, 29, 32],profit = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 370: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 7, 10, 12, 13, 14, 15, 16, 18, 20],endTime = [5, 8, 13, 14, 15, 17, 20, 21, 22, 23],profit = [5, 8, 13, 14, 15, 17, 20, 21, 22, 23]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 7, 10, 12, 13, 14, 15, 16, 18, 20],endTime = [5, 8, 13, 14, 15, 17, 20, 21, 22, 23],profit = [5, 8, 13, 14, 15, 17, 20, 21, 22, 23]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],endTime = [5, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104, 114, 124, 134, 144],profit = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],endTime = [5, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104, 114, 124, 134, 144],profit = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],endTime = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250]) == 12350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],endTime = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250]) == 12350: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 5, 8, 11, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50],endTime = [4, 6, 9, 13, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 6900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 5, 8, 11, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50],endTime = [4, 6, 9, 13, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 6900: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 5, 10, 15, 20, 25, 30],endTime = [4, 9, 14, 19, 24, 29, 34],profit = [100, 200, 300, 400, 500, 600, 700]) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 5, 10, 15, 20, 25, 30],endTime = [4, 9, 14, 19, 24, 29, 34],profit = [100, 200, 300, 400, 500, 600, 700]) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 8, 12, 15, 18, 20, 25, 30],endTime = [5, 7, 10, 14, 16, 19, 22, 24, 30, 35],profit = [50, 20, 70, 10, 120, 30, 50, 25, 80, 60]) == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 8, 12, 15, 18, 20, 25, 30],endTime = [5, 7, 10, 14, 16, 19, 22, 24, 30, 35],profit = [50, 20, 70, 10, 120, 30, 50, 25, 80, 60]) == 430: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],endTime = [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8],profit = [10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],endTime = [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8],profit = [10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16],endTime = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 20, 19, 21, 22, 23, 24],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16],endTime = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 20, 19, 21, 22, 23, 24],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 5, 8, 10, 11, 12, 15, 18, 20, 22],endTime = [4, 9, 11, 13, 14, 17, 19, 23, 24, 25],profit = [20, 30, 5, 10, 50, 40, 70, 60, 10, 20]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 5, 8, 10, 11, 12, 15, 18, 20, 22],endTime = [4, 9, 11, 13, 14, 17, 19, 23, 24, 25],profit = [20, 30, 5, 10, 50, 40, 70, 60, 10, 20]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],endTime = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],profit = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],endTime = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],profit = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],profit = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],profit = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],endTime = [6, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48],profit = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]) == 730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],endTime = [6, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48],profit = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]) == 730: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 4600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 4600: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 8, 10, 13, 16, 18, 20, 23],endTime = [4, 7, 10, 12, 14, 17, 20, 22, 24, 27],profit = [500, 400, 300, 200, 100, 50, 75, 125, 175, 225]) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 8, 10, 13, 16, 18, 20, 23],endTime = [4, 7, 10, 12, 14, 17, 20, 22, 24, 27],profit = [500, 400, 300, 200, 100, 50, 75, 125, 175, 225]) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000],endTime = [1000000001, 900000001, 800000001, 700000001, 600000001, 500000001, 400000001, 300000001, 200000001, 100000001],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000],endTime = [1000000001, 900000001, 800000001, 700000001, 600000001, 500000001, 400000001, 300000001, 200000001, 100000001],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 120000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 120000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 260: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],profit = [20, 15, 10, 5, 40, 35, 30, 25, 20, 15, 10, 5, 40, 35, 30]) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],profit = [20, 15, 10, 5, 40, 35, 30, 25, 20, 15, 10, 5, 40, 35, 30]) == 335: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 1360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 1360: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 5, 6, 8, 12, 15, 18, 20, 25],endTime = [5, 5, 10, 10, 13, 17, 20, 22, 28, 30],profit = [50, 20, 70, 10, 30, 60, 5, 40, 90, 25]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 5, 6, 8, 12, 15, 18, 20, 25],endTime = [5, 5, 10, 10, 13, 17, 20, 22, 28, 30],profit = [50, 20, 70, 10, 30, 60, 5, 40, 90, 25]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [5, 4, 8, 10, 9, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22],profit = [100, 200, 150, 300, 250, 200, 400, 350, 300, 250, 200, 150, 100, 50, 100]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [5, 4, 8, 10, 9, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22],profit = [100, 200, 150, 300, 250, 200, 400, 350, 300, 250, 200, 150, 100, 50, 100]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],endTime = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800],profit = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],endTime = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800],profit = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 5, 8, 10, 13, 16, 18, 20, 22, 25, 27, 29],endTime = [4, 9, 11, 12, 15, 17, 19, 21, 24, 26, 28, 30],profit = [100, 150, 100, 50, 200, 100, 150, 50, 100, 200, 50, 150]) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 5, 8, 10, 13, 16, 18, 20, 22, 25, 27, 29],endTime = [4, 9, 11, 12, 15, 17, 19, 21, 24, 26, 28, 30],profit = [100, 150, 100, 50, 200, 100, 150, 50, 100, 200, 50, 150]) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 8, 6, 10, 12, 14, 18, 20, 22, 24],profit = [10, 30, 20, 40, 50, 70, 60, 80, 90, 100]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 8, 6, 10, 12, 14, 18, 20, 22, 24],profit = [10, 30, 20, 40, 50, 70, 60, 80, 90, 100]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 4, 5, 6, 8, 9],endTime = [2, 5, 7, 7, 9, 10, 11],profit = [10, 20, 40, 10, 30, 50, 20]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 4, 5, 6, 8, 9],endTime = [2, 5, 7, 7, 9, 10, 11],profit = [10, 20, 40, 10, 30, 50, 20]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 5, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81],endTime = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 3200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 5, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81],endTime = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 3200: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16],endTime = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],profit = [20, 25, 20, 30, 35, 40, 35, 45, 50, 55, 50, 60, 65, 70, 65, 75, 80, 85, 90, 95]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16],endTime = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],profit = [20, 25, 20, 30, 35, 40, 35, 45, 50, 55, 50, 60, 65, 70, 65, 75, 80, 85, 90, 95]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],profit = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],profit = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1000000000, 900000000, 800000000, 700000000, 600000000],endTime = [1000000001, 900000001, 800000001, 700000001, 600000001],profit = [100, 200, 300, 400, 500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1000000000, 900000000, 800000000, 700000000, 600000000],endTime = [1000000001, 900000001, 800000001, 700000001, 600000001],profit = [100, 200, 300, 400, 500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23],profit = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23],profit = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],endTime = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 210000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],endTime = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 210000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 3850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 3850: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 5, 7, 8, 9, 10, 12, 15, 16, 19],endTime = [5, 8, 9, 10, 12, 15, 16, 20, 21, 25],profit = [100, 80, 40, 60, 70, 50, 30, 90, 20, 150]) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 5, 7, 8, 9, 10, 12, 15, 16, 19],endTime = [5, 8, 9, 10, 12, 15, 16, 20, 21, 25],profit = [100, 80, 40, 60, 70, 50, 30, 90, 20, 150]) == 440: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],endTime = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],endTime = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 1010: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],profit = [20, 40, 30, 60, 50, 80, 70, 100, 90, 120, 110, 140, 130, 160, 150, 180, 170, 200, 190, 220, 210, 240, 230]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],profit = [20, 40, 30, 60, 50, 80, 70, 100, 90, 120, 110, 140, 130, 160, 150, 180, 170, 200, 190, 220, 210, 240, 230]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 2, 4, 6, 7, 9, 10],endTime = [3, 3, 5, 8, 7, 10, 12, 15],profit = [50, 20, 30, 40, 60, 70, 80, 90]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 2, 4, 6, 7, 9, 10],endTime = [3, 3, 5, 8, 7, 10, 12, 15],profit = [50, 20, 30, 40, 60, 70, 80, 90]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 12, 8, 4, 9, 15, 18, 20, 25, 30],endTime = [7, 16, 13, 5, 11, 20, 22, 23, 32, 31],profit = [100, 150, 90, 60, 120, 200, 80, 40, 180, 160]) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 12, 8, 4, 9, 15, 18, 20, 25, 30],endTime = [7, 16, 13, 5, 11, 20, 22, 23, 32, 31],profit = [100, 150, 90, 60, 120, 200, 80, 40, 180, 160]) == 640: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [500, 300, 700, 100, 400, 800, 200, 600, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [500, 300, 700, 100, 400, 800, 200, 600, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],profit = [10, 50, 20, 60, 30, 70, 40, 80, 50, 90, 60]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],profit = [10, 50, 20, 60, 30, 70, 40, 80, 50, 90, 60]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 5, 8, 13, 21],endTime = [5, 4, 6, 8, 10, 15, 25],profit = [20, 20, 10, 40, 20, 30, 50]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 5, 8, 13, 21],endTime = [5, 4, 6, 8, 10, 15, 25],profit = [20, 20, 10, 40, 20, 30, 50]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 6050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 6050: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],endTime = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],endTime = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],endTime = [2, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],endTime = [2, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [3, 15, 5, 10, 20, 25],endTime = [10, 20, 10, 15, 25, 30],profit = [50, 70, 30, 60, 100, 40]) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [3, 15, 5, 10, 20, 25],endTime = [10, 20, 10, 15, 25, 30],profit = [50, 70, 30, 60, 100, 40]) == 320: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],endTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],endTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1275: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 77000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 77000: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 5, 7, 9, 10, 12, 15, 18, 20],endTime = [5, 6, 8, 10, 12, 14, 17, 20, 22, 25, 27],profit = [100, 50, 70, 60, 80, 90, 120, 150, 200, 180, 220]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 5, 7, 9, 10, 12, 15, 18, 20],endTime = [5, 6, 8, 10, 12, 14, 17, 20, 22, 25, 27],profit = [100, 50, 70, 60, 80, 90, 120, 150, 200, 180, 220]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 2750: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],endTime = [9, 14, 19, 24, 29, 34, 39, 44, 49, 54],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 3250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],endTime = [9, 14, 19, 24, 29, 34, 39, 44, 49, 54],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 3250: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(startTime = [1, 10, 4, 3, 8, 9],endTime = [2, 11, 5, 7, 9, 10],profit = [3, 1, 5, 6, 4, 3]) == 17
    assert candidate(startTime = [1, 3, 5, 6, 7],endTime = [3, 5, 9, 8, 9],profit = [50, 20, 60, 40, 30]) == 130
    assert candidate(startTime = [1, 10, 100, 1000],endTime = [2, 20, 200, 2000],profit = [5, 50, 500, 5000]) == 5555
    assert candidate(startTime = [1, 3, 6, 8],endTime = [2, 5, 10, 12],profit = [50, 20, 100, 80]) == 170
    assert candidate(startTime = [3, 1, 1, 2],endTime = [4, 2, 4, 3],profit = [50, 10, 40, 70]) == 130
    assert candidate(startTime = [3, 5, 10],endTime = [15, 18, 19],profit = [20, 20, 100]) == 100
    assert candidate(startTime = [1],endTime = [2],profit = [5]) == 5
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(startTime = [1, 3, 6, 8, 12, 14],endTime = [4, 5, 10, 11, 14, 15],profit = [5, 6, 8, 3, 10, 4]) == 28
    assert candidate(startTime = [1, 2, 3, 4, 5, 6],endTime = [2, 3, 4, 5, 6, 7],profit = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(startTime = [1, 1, 1],endTime = [2, 3, 4],profit = [5, 6, 4]) == 6
    assert candidate(startTime = [1, 2, 3, 3],endTime = [3, 4, 5, 6],profit = [50, 10, 40, 70]) == 120
    assert candidate(startTime = [1, 2, 3, 4, 6],endTime = [3, 5, 10, 6, 9],profit = [20, 20, 100, 70, 60]) == 150
    assert candidate(startTime = [5, 8, 4, 1, 1],endTime = [6, 10, 7, 8, 2],profit = [100, 500, 100, 200, 300]) == 900
    assert candidate(startTime = [1, 3, 6, 8],endTime = [5, 7, 10, 12],profit = [50, 20, 100, 200]) == 250
    assert candidate(startTime = [2, 5, 8, 11],endTime = [5, 7, 10, 14],profit = [20, 30, 40, 50]) == 140
    assert candidate(startTime = [5, 10, 15, 20, 25],endTime = [10, 15, 20, 25, 30],profit = [100, 150, 200, 250, 300]) == 1000
    assert candidate(startTime = [100, 200, 300],endTime = [200, 300, 400],profit = [1000, 2000, 3000]) == 6000
    assert candidate(startTime = [1, 2, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37],endTime = [5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30, 33, 34, 37, 38, 41, 42],profit = [100, 200, 150, 300, 100, 500, 400, 300, 600, 700, 800, 600, 400, 300, 200, 100, 900, 800, 700, 600]) == 3400
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1000
    assert candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [2, 3, 4, 5, 6, 7],profit = [100, 200, 300, 400, 500, 600]) == 600
    assert candidate(startTime = [1, 2, 3, 5, 6, 8, 10, 12, 14, 16],endTime = [5, 4, 6, 9, 8, 11, 13, 15, 17, 19],profit = [5, 3, 7, 9, 8, 6, 4, 2, 1, 10]) == 33
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 325
    assert candidate(startTime = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7],endTime = [3, 4, 4, 5, 6, 7, 7, 8, 9, 10],profit = [50, 40, 30, 20, 60, 10, 20, 100, 5, 45]) == 155
    assert candidate(startTime = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],endTime = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2100
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(startTime = [1, 5, 8, 11, 13, 16, 19, 22, 25, 28],endTime = [4, 9, 12, 15, 17, 20, 23, 26, 29, 32],profit = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 370
    assert candidate(startTime = [3, 7, 10, 12, 13, 14, 15, 16, 18, 20],endTime = [5, 8, 13, 14, 15, 17, 20, 21, 22, 23],profit = [5, 8, 13, 14, 15, 17, 20, 21, 22, 23]) == 84
    assert candidate(startTime = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],endTime = [5, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104, 114, 124, 134, 144],profit = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 1800
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],endTime = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250]) == 12350
    assert candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 1000
    assert candidate(startTime = [1, 2, 3, 5, 8, 11, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50],endTime = [4, 6, 9, 13, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 6900
    assert candidate(startTime = [1, 5, 10, 15, 20, 25, 30],endTime = [4, 9, 14, 19, 24, 29, 34],profit = [100, 200, 300, 400, 500, 600, 700]) == 2800
    assert candidate(startTime = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 360
    assert candidate(startTime = [1, 3, 6, 8, 12, 15, 18, 20, 25, 30],endTime = [5, 7, 10, 14, 16, 19, 22, 24, 30, 35],profit = [50, 20, 70, 10, 120, 30, 50, 25, 80, 60]) == 430
    assert candidate(startTime = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],endTime = [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8],profit = [10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25]) == 70
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 3000
    assert candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16],endTime = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 20, 19, 21, 22, 23, 24],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 42
    assert candidate(startTime = [3, 5, 8, 10, 11, 12, 15, 18, 20, 22],endTime = [4, 9, 11, 13, 14, 17, 19, 23, 24, 25],profit = [20, 30, 5, 10, 50, 40, 70, 60, 10, 20]) == 190
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],endTime = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],profit = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 720
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],profit = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10]) == 600
    assert candidate(startTime = [1, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],endTime = [6, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48],profit = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]) == 730
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 4600
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
    assert candidate(startTime = [1, 3, 6, 8, 10, 13, 16, 18, 20, 23],endTime = [4, 7, 10, 12, 14, 17, 20, 22, 24, 27],profit = [500, 400, 300, 200, 100, 50, 75, 125, 175, 225]) == 1250
    assert candidate(startTime = [1000000000, 900000000, 800000000, 700000000, 600000000, 500000000, 400000000, 300000000, 200000000, 100000000],endTime = [1000000001, 900000001, 800000001, 700000001, 600000001, 500000001, 400000001, 300000001, 200000001, 100000001],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 120000
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 260
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],profit = [20, 15, 10, 5, 40, 35, 30, 25, 20, 15, 10, 5, 40, 35, 30]) == 335
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 1360
    assert candidate(startTime = [1, 2, 5, 6, 8, 12, 15, 18, 20, 25],endTime = [5, 5, 10, 10, 13, 17, 20, 22, 28, 30],profit = [50, 20, 70, 10, 30, 60, 5, 40, 90, 25]) == 270
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [5, 4, 8, 10, 9, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22],profit = [100, 200, 150, 300, 250, 200, 400, 350, 300, 250, 200, 150, 100, 50, 100]) == 750
    assert candidate(startTime = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],endTime = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800],profit = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 100
    assert candidate(startTime = [1, 5, 8, 10, 13, 16, 18, 20, 22, 25, 27, 29],endTime = [4, 9, 11, 12, 15, 17, 19, 21, 24, 26, 28, 30],profit = [100, 150, 100, 50, 200, 100, 150, 50, 100, 200, 50, 150]) == 1300
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 4500
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 8, 6, 10, 12, 14, 18, 20, 22, 24],profit = [10, 30, 20, 40, 50, 70, 60, 80, 90, 100]) == 250
    assert candidate(startTime = [1, 3, 4, 5, 6, 8, 9],endTime = [2, 5, 7, 7, 9, 10, 11],profit = [10, 20, 40, 10, 30, 50, 20]) == 100
    assert candidate(startTime = [3, 5, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81],endTime = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 3200
    assert candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16],endTime = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],profit = [20, 25, 20, 30, 35, 40, 35, 45, 50, 55, 50, 60, 65, 70, 65, 75, 80, 85, 90, 95]) == 275
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],profit = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 250
    assert candidate(startTime = [1000000000, 900000000, 800000000, 700000000, 600000000],endTime = [1000000001, 900000001, 800000001, 700000001, 600000001],profit = [100, 200, 300, 400, 500]) == 1500
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23],profit = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 110
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 50
    assert candidate(startTime = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],endTime = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 210000
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 3850
    assert candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(startTime = [1, 5, 7, 8, 9, 10, 12, 15, 16, 19],endTime = [5, 8, 9, 10, 12, 15, 16, 20, 21, 25],profit = [100, 80, 40, 60, 70, 50, 30, 90, 20, 150]) == 440
    assert candidate(startTime = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],endTime = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 1010
    assert candidate(startTime = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],profit = [20, 40, 30, 60, 50, 80, 70, 100, 90, 120, 110, 140, 130, 160, 150, 180, 170, 200, 190, 220, 210, 240, 230]) == 750
    assert candidate(startTime = [1, 2, 2, 4, 6, 7, 9, 10],endTime = [3, 3, 5, 8, 7, 10, 12, 15],profit = [50, 20, 30, 40, 60, 70, 80, 90]) == 270
    assert candidate(startTime = [3, 12, 8, 4, 9, 15, 18, 20, 25, 30],endTime = [7, 16, 13, 5, 11, 20, 22, 23, 32, 31],profit = [100, 150, 90, 60, 120, 200, 80, 40, 180, 160]) == 640
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 165
    assert candidate(startTime = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18],endTime = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [500, 300, 700, 100, 400, 800, 200, 600, 900, 1000]) == 5500
    assert candidate(startTime = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],profit = [10, 50, 20, 60, 30, 70, 40, 80, 50, 90, 60]) == 560
    assert candidate(startTime = [1, 2, 3, 5, 8, 13, 21],endTime = [5, 4, 6, 8, 10, 15, 25],profit = [20, 20, 10, 40, 20, 30, 50]) == 160
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1100
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 6050
    assert candidate(startTime = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],endTime = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(startTime = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],endTime = [2, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
    assert candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(startTime = [3, 15, 5, 10, 20, 25],endTime = [10, 20, 10, 15, 25, 30],profit = [50, 70, 30, 60, 100, 40]) == 320
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],endTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1275
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],endTime = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],profit = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 77000
    assert candidate(startTime = [1, 2, 3, 5, 7, 9, 10, 12, 15, 18, 20],endTime = [5, 6, 8, 10, 12, 14, 17, 20, 22, 25, 27],profit = [100, 50, 70, 60, 80, 90, 120, 150, 200, 180, 220]) == 550
    assert candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],profit = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 2750
    assert candidate(startTime = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],endTime = [9, 14, 19, 24, 29, 34, 39, 44, 49, 54],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 3250


