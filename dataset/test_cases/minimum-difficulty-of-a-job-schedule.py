def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [300, 500, 1000],d = 3) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [300, 500, 1000],d = 3) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [6, 5, 4, 3, 2, 1],d = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [6, 5, 4, 3, 2, 1],d = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [15, 97, 88, 92, 49],d = 2) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [15, 97, 88, 92, 49],d = 2) == 112: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [7, 1, 7, 1, 7, 1],d = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [7, 1, 7, 1, 7, 1],d = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [0, 0, 0, 0],d = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [0, 0, 0, 0],d = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 3) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 3) == 80: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1000, 0, 1000, 0, 1000],d = 3) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1000, 0, 1000, 0, 1000],d = 3) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [30, 10, 40, 20, 10, 50],d = 3) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [30, 10, 40, 20, 10, 50],d = 3) == 90: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 200, 300],d = 1) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 200, 300],d = 1) == 300: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [3, 2, 1],d = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [3, 2, 1],d = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1],d = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1],d = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 4, 3, 2, 1],d = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 4, 3, 2, 1],d = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [9, 9, 9],d = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [9, 9, 9],d = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 4, 3, 2, 1],d = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 4, 3, 2, 1],d = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],d = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],d = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2],d = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2],d = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 2) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 2) == 60: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1],d = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1],d = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 5) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 5) == 150: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [500, 400, 300, 200, 100, 900, 800, 700, 600, 500],d = 4) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [500, 400, 300, 200, 100, 900, 800, 700, 600, 500],d = 4) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],d = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],d = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],d = 15) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],d = 15) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 4, 15, 8, 12, 9, 5, 6, 7, 11, 3],d = 4) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 4, 15, 8, 12, 9, 5, 6, 7, 11, 3],d = 4) == 32: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],d = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],d = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 300],d = 15) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 300],d = 15) == 405: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [8, 5, 7, 9, 4, 2, 6, 3, 10, 1, 12, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 20) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [8, 5, 7, 9, 4, 2, 6, 3, 10, 1, 12, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 20) == 220: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [9, 4, 5, 3, 2, 8, 7, 1, 6, 10],d = 5) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [9, 4, 5, 3, 2, 8, 7, 1, 6, 10],d = 5) == 29: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 29) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 29) == 29: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],d = 10) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],d = 10) == 180: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 10) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 10) == 65: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [300, 200, 100, 250, 400, 350, 500, 450, 550, 600],d = 5) == 1450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [300, 200, 100, 250, 400, 350, 500, 450, 550, 600],d = 5) == 1450: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 8, 6, 5, 3, 4, 2, 7, 1, 9],d = 4) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 8, 6, 5, 3, 4, 2, 7, 1, 9],d = 4) == 23: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],d = 25) == 660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],d = 25) == 660: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 15) == 1350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 15) == 1350: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 5) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 5) == 400: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],d = 10) == 6500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],d = 10) == 6500: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],d = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],d = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 7) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 7) == 35: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 100, 20, 50, 30, 70, 40, 60, 90, 80, 10, 200, 150, 300, 250],d = 5) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 100, 20, 50, 30, 70, 40, 60, 90, 80, 10, 200, 150, 300, 250],d = 5) == 480: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 15) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 15) == 75: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],d = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],d = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 300],d = 10) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 300],d = 10) == 345: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],d = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],d = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [9, 18, 1, 5, 19, 12, 4, 7, 8, 6],d = 5) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [9, 18, 1, 5, 19, 12, 4, 7, 8, 6],d = 5) == 44: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],d = 10) == 9855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],d = 10) == 9855: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 15) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 15) == 135: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [3, 6, 1, 9, 10, 5, 4, 8, 7, 2],d = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [3, 6, 1, 9, 10, 5, 4, 8, 7, 2],d = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288, 287, 286, 285, 284, 283, 282, 281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271],d = 5) == 1390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288, 287, 286, 285, 284, 283, 282, 281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271],d = 5) == 1390: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [7, 8, 4, 3, 2, 9, 10, 11, 1, 2],d = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [7, 8, 4, 3, 2, 9, 10, 11, 1, 2],d = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 3) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 3) == 130: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950],d = 10) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950],d = 10) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],d = 15) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],d = 15) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],d = 10) == 3250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],d = 10) == 3250: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],d = 5) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],d = 5) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],d = 10) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],d = 10) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 5) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 5) == 300: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 30) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 30) == 465: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],d = 25) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],d = 25) == 50: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],d = 10) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],d = 10) == 45: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [3, 6, 5, 10, 12, 8, 7, 4, 15, 11, 9, 1, 14, 13, 2, 16, 18, 17, 19, 20, 21, 22, 23, 24, 25],d = 10) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [3, 6, 5, 10, 12, 8, 7, 4, 15, 11, 9, 1, 14, 13, 2, 16, 18, 17, 19, 20, 21, 22, 23, 24, 25],d = 10) == 86: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 30) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 30) == 465: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [300, 200, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],d = 10) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [300, 200, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],d = 10) == 300: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],d = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],d = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16],d = 10) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16],d = 10) == 69: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 50, 100, 150, 200, 250, 300],d = 10) == 2300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 50, 100, 150, 200, 250, 300],d = 10) == 2300: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],d = 2) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],d = 2) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],d = 10) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],d = 10) == 140: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991],d = 5) == 2993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991],d = 5) == 2993: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],d = 15) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],d = 15) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 3) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 3) == 130: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [300, 250, 200, 150, 100, 50, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 10) == 353
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [300, 250, 200, 150, 100, 50, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 10) == 353: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],d = 10) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],d = 10) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],d = 5) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],d = 5) == 500: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [9, 18, 7, 16, 15, 14, 13, 2, 11, 10, 8, 6, 5, 4, 3, 1, 12, 17, 19, 20],d = 5) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [9, 18, 7, 16, 15, 14, 13, 2, 11, 10, 8, 6, 5, 4, 3, 1, 12, 17, 19, 20],d = 5) == 46: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [500, 300, 700, 100, 200, 400, 800, 600, 900],d = 4) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [500, 300, 700, 100, 200, 400, 800, 600, 900],d = 4) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],d = 15) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],d = 15) == 255: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 8, 3, 1, 9, 4, 6, 7, 2, 10, 15, 12, 14, 11, 13, 16, 18, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 8) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 8, 3, 1, 9, 4, 6, 7, 2, 10, 15, 12, 14, 11, 13, 16, 18, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 8) == 64: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],d = 29) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],d = 29) == 87: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 7) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 7) == 31: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [2, 3, 6, 5, 4, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15],d = 7) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [2, 3, 6, 5, 4, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15],d = 7) == 41: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],d = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],d = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [300, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],d = 7) == 1600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [300, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],d = 7) == 1600: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],d = 4) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],d = 4) == 25: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],d = 7) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],d = 7) == 240: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 10) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 10) == 75: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 7) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 7) == 41: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 7) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 7) == 36: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [200, 150, 100, 50, 0, 50, 100, 150, 200],d = 6) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [200, 150, 100, 50, 0, 50, 100, 150, 200],d = 6) == 600: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],d = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],d = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],d = 10) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],d = 10) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 5) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 5) == 400: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 10) == 55
    assert candidate(jobDifficulty = [300, 500, 1000],d = 3) == 1800
    assert candidate(jobDifficulty = [6, 5, 4, 3, 2, 1],d = 2) == 7
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 5) == 20
    assert candidate(jobDifficulty = [15, 97, 88, 92, 49],d = 2) == 112
    assert candidate(jobDifficulty = [7, 1, 7, 1, 7, 1],d = 3) == 15
    assert candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 5) == 25
    assert candidate(jobDifficulty = [0, 0, 0, 0],d = 4) == 0
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 3) == 80
    assert candidate(jobDifficulty = [1000, 0, 1000, 0, 1000],d = 3) == 2000
    assert candidate(jobDifficulty = [30, 10, 40, 20, 10, 50],d = 3) == 90
    assert candidate(jobDifficulty = [100, 200, 300],d = 1) == 300
    assert candidate(jobDifficulty = [3, 2, 1],d = 1) == 3
    assert candidate(jobDifficulty = [1],d = 1) == 1
    assert candidate(jobDifficulty = [5, 4, 3, 2, 1],d = 1) == 5
    assert candidate(jobDifficulty = [9, 9, 9],d = 4) == -1
    assert candidate(jobDifficulty = [5, 4, 3, 2, 1],d = 5) == 15
    assert candidate(jobDifficulty = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],d = 10) == 30
    assert candidate(jobDifficulty = [1, 2],d = 2) == 3
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 2) == 60
    assert candidate(jobDifficulty = [1, 1, 1],d = 3) == 3
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50],d = 5) == 150
    assert candidate(jobDifficulty = [500, 400, 300, 200, 100, 900, 800, 700, 600, 500],d = 4) == 1700
    assert candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
    assert candidate(jobDifficulty = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],d = 5) == 32
    assert candidate(jobDifficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 10) == 550
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],d = 15) == 1200
    assert candidate(jobDifficulty = [10, 4, 15, 8, 12, 9, 5, 6, 7, 11, 3],d = 4) == 32
    assert candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 10) == 55
    assert candidate(jobDifficulty = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],d = 10) == 15
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 300],d = 15) == 405
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 5) == 25
    assert candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 13
    assert candidate(jobDifficulty = [8, 5, 7, 9, 4, 2, 6, 3, 10, 1, 12, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 20) == 220
    assert candidate(jobDifficulty = [9, 4, 5, 3, 2, 8, 7, 1, 6, 10],d = 5) == 29
    assert candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 29) == 29
    assert candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],d = 10) == 180
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 10) == 65
    assert candidate(jobDifficulty = [300, 200, 100, 250, 400, 350, 500, 450, 550, 600],d = 5) == 1450
    assert candidate(jobDifficulty = [5, 8, 6, 5, 3, 4, 2, 7, 1, 9],d = 4) == 23
    assert candidate(jobDifficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],d = 25) == 660
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 15) == 1350
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 5) == 400
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 10) == 60
    assert candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],d = 10) == 6500
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 4) == 16
    assert candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 1) == 30
    assert candidate(jobDifficulty = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],d = 5) == 21
    assert candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 7) == 35
    assert candidate(jobDifficulty = [10, 100, 20, 50, 30, 70, 40, 60, 90, 80, 10, 200, 150, 300, 250],d = 5) == 480
    assert candidate(jobDifficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],d = 15) == 75
    assert candidate(jobDifficulty = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],d = 10) == 100
    assert candidate(jobDifficulty = [8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 11
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 300],d = 10) == 345
    assert candidate(jobDifficulty = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],d = 5) == 25
    assert candidate(jobDifficulty = [9, 18, 1, 5, 19, 12, 4, 7, 8, 6],d = 5) == 44
    assert candidate(jobDifficulty = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],d = 10) == 9855
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 15) == 135
    assert candidate(jobDifficulty = [3, 6, 1, 9, 10, 5, 4, 8, 7, 2],d = 10) == 55
    assert candidate(jobDifficulty = [300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288, 287, 286, 285, 284, 283, 282, 281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271],d = 5) == 1390
    assert candidate(jobDifficulty = [7, 8, 4, 3, 2, 9, 10, 11, 1, 2],d = 3) == 14
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 3) == 130
    assert candidate(jobDifficulty = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950],d = 10) == 6000
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],d = 15) == 1200
    assert candidate(jobDifficulty = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 3) == 13
    assert candidate(jobDifficulty = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],d = 10) == 3250
    assert candidate(jobDifficulty = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],d = 5) == 1400
    assert candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],d = 10) == 5500
    assert candidate(jobDifficulty = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 5) == 300
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 30) == 465
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 5) == 40
    assert candidate(jobDifficulty = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],d = 25) == 50
    assert candidate(jobDifficulty = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],d = 10) == 45
    assert candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
    assert candidate(jobDifficulty = [3, 6, 5, 10, 12, 8, 7, 4, 15, 11, 9, 1, 14, 13, 2, 16, 18, 17, 19, 20, 21, 22, 23, 24, 25],d = 10) == 86
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 30) == 465
    assert candidate(jobDifficulty = [300, 200, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],d = 10) == 300
    assert candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],d = 2) == 20
    assert candidate(jobDifficulty = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16],d = 10) == 69
    assert candidate(jobDifficulty = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 50, 100, 150, 200, 250, 300],d = 10) == 2300
    assert candidate(jobDifficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],d = 2) == 1100
    assert candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],d = 10) == 140
    assert candidate(jobDifficulty = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991],d = 5) == 2993
    assert candidate(jobDifficulty = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],d = 15) == 1500
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 3) == 130
    assert candidate(jobDifficulty = [300, 250, 200, 150, 100, 50, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 10) == 353
    assert candidate(jobDifficulty = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],d = 10) == 10000
    assert candidate(jobDifficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],d = 10) == 550
    assert candidate(jobDifficulty = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],d = 5) == 500
    assert candidate(jobDifficulty = [9, 18, 7, 16, 15, 14, 13, 2, 11, 10, 8, 6, 5, 4, 3, 1, 12, 17, 19, 20],d = 5) == 46
    assert candidate(jobDifficulty = [500, 300, 700, 100, 200, 400, 800, 600, 900],d = 4) == 1900
    assert candidate(jobDifficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],d = 15) == 255
    assert candidate(jobDifficulty = [5, 8, 3, 1, 9, 4, 6, 7, 2, 10, 15, 12, 14, 11, 13, 16, 18, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 8) == 64
    assert candidate(jobDifficulty = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],d = 29) == 87
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 7) == 31
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 5) == 25
    assert candidate(jobDifficulty = [2, 3, 6, 5, 4, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15],d = 7) == 41
    assert candidate(jobDifficulty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],d = 1) == 0
    assert candidate(jobDifficulty = [300, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],d = 7) == 1600
    assert candidate(jobDifficulty = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],d = 4) == 25
    assert candidate(jobDifficulty = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],d = 7) == 240
    assert candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],d = 10) == 75
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],d = 7) == 41
    assert candidate(jobDifficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d = 7) == 36
    assert candidate(jobDifficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],d = 10) == 10
    assert candidate(jobDifficulty = [200, 150, 100, 50, 0, 50, 100, 150, 200],d = 6) == 600
    assert candidate(jobDifficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],d = 20) == -1
    assert candidate(jobDifficulty = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],d = 10) == 10000
    assert candidate(jobDifficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],d = 5) == 400


