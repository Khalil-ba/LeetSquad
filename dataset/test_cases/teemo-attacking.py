def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4, 5],duration = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4, 5],duration = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 5, 9],duration = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 5, 9],duration = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1],duration = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1],duration = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 14, 15],duration = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 14, 15],duration = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4],duration = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4],duration = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5],duration = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5],duration = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 5, 10, 15],duration = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 5, 10, 15],duration = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],duration = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],duration = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 14, 15],duration = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 14, 15],duration = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 1, 1, 1],duration = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 1, 1, 1],duration = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2],duration = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2],duration = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4],duration = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4],duration = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 20, 30, 40, 50],duration = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 20, 30, 40, 50],duration = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 15, 20, 25],duration = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 15, 20, 25],duration = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 7, 8, 10],duration = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 7, 8, 10],duration = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 100, 200, 300, 400, 500],duration = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 100, 200, 300, 400, 500],duration = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 8) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 8) == 53: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],duration = 100) == 427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],duration = 100) == 427: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 6, 10, 12, 15],duration = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 6, 10, 12, 15],duration = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 6, 10],duration = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 6, 10],duration = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 5, 8, 13, 21, 34, 55],duration = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 5, 8, 13, 21, 34, 55],duration = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 4, 6, 8, 10],duration = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 4, 6, 8, 10],duration = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],duration = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],duration = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25],duration = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25],duration = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 8) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 8) == 80: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],duration = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],duration = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],duration = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],duration = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],duration = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],duration = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],duration = 50) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],duration = 50) == 249: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],duration = 7) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],duration = 7) == 47: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],duration = 2) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],duration = 2) == 30: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 7) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 7) == 52: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45],duration = 8) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45],duration = 8) == 52: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 7) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 7) == 32: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40],duration = 5) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40],duration = 5) == 44: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [2, 3, 5, 6, 8, 9, 11],duration = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [2, 3, 5, 6, 8, 9, 11],duration = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],duration = 2) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],duration = 2) == 30: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 5) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 5) == 23: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 5, 10, 15, 20, 25],duration = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 5, 10, 15, 20, 25],duration = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 5, 10, 15, 20, 25, 30, 35, 40],duration = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 5, 10, 15, 20, 25, 30, 35, 40],duration = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 7, 10, 13, 16],duration = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 7, 10, 13, 16],duration = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 5, 9, 12, 15, 18, 21, 24, 27],duration = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 5, 9, 12, 15, 18, 21, 24, 27],duration = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 200, 300, 400, 500],duration = 150) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 200, 300, 400, 500],duration = 150) == 550: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 7) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 7) == 32: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],duration = 3) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],duration = 3) == 33: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],duration = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],duration = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 109: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 12, 15, 17, 18, 20, 25, 30],duration = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 12, 15, 17, 18, 20, 25, 30],duration = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9],duration = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9],duration = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],duration = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],duration = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],duration = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],duration = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 101, 102, 103, 104, 105],duration = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 101, 102, 103, 104, 105],duration = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],duration = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],duration = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [2, 5, 10, 15, 20],duration = 6) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [2, 5, 10, 15, 20],duration = 6) == 24: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 15) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 15) == 60: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],duration = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],duration = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 10) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 10) == 99: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9],duration = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9],duration = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],duration = 10) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],duration = 10) == 39: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],duration = 2) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],duration = 2) == 40: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 5, 7, 9, 12, 15, 20, 25],duration = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 5, 7, 9, 12, 15, 20, 25],duration = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],duration = 15) == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],duration = 15) == 305: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 15) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 15) == 104: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 5, 10, 15, 20, 25, 30],duration = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 5, 10, 15, 20, 25, 30],duration = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 26],duration = 4) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 26],duration = 4) == 29: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],duration = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],duration = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],duration = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],duration = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],duration = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],duration = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15],duration = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15],duration = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 102, 105, 110, 115, 121, 128, 136, 145, 155],duration = 15) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 102, 105, 110, 115, 121, 128, 136, 145, 155],duration = 15) == 70: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25],duration = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25],duration = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 0, 0, 0, 0],duration = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 0, 0, 0, 0],duration = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14],duration = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14],duration = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1000, 1005, 1010, 1015, 1020, 1025],duration = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1000, 1005, 1010, 1015, 1020, 1025],duration = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],duration = 50) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],duration = 50) == 500: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [2, 2, 2, 2, 2],duration = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [2, 2, 2, 2, 2],duration = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [2, 4, 8, 12, 16, 20, 24, 28],duration = 6) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [2, 4, 8, 12, 16, 20, 24, 28],duration = 6) == 32: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],duration = 50) == 263
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],duration = 50) == 263: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 6, 10, 15],duration = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 6, 10, 15],duration = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 5, 6, 8, 10, 12, 15],duration = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 5, 6, 8, 10, 12, 15],duration = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],duration = 3) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],duration = 3) == 33: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 3, 6, 10, 15, 21, 28, 36, 45],duration = 7) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 3, 6, 10, 15, 21, 28, 36, 45],duration = 7) == 48: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 15, 25, 35, 45, 55],duration = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 15, 25, 35, 45, 55],duration = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 110: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],duration = 10) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],duration = 10) == 149: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],duration = 100) == 1099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],duration = 100) == 1099: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 5) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 5) == 53: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 3) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 3) == 23: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],duration = 8) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],duration = 8) == 78: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],duration = 3) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],duration = 3) == 45: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82],duration = 9) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82],duration = 9) == 90: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40],duration = 10) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40],duration = 10) == 45: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 4, 8, 12, 16],duration = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 4, 8, 12, 16],duration = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 200, 300, 400, 500],duration = 150) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 200, 300, 400, 500],duration = 150) == 550: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],duration = 50) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],duration = 50) == 500: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],duration = 50) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],duration = 50) == 249: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 15) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 15) == 105: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],duration = 7) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],duration = 7) == 77: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],duration = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],duration = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 2, 3, 10, 15, 20],duration = 5) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 2, 3, 10, 15, 20],duration = 5) == 22: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 9) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 9) == 90: {e}')
    
    total += 1
    try:
        result = candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],duration = 2) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],duration = 2) == 27: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(timeSeries = [0, 1, 2, 3, 4, 5],duration = 1) == 6
    assert candidate(timeSeries = [1, 5, 9],duration = 4) == 12
    assert candidate(timeSeries = [1],duration = 5) == 5
    assert candidate(timeSeries = [10, 14, 15],duration = 5) == 10
    assert candidate(timeSeries = [0, 1, 2, 3, 4],duration = 1) == 5
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 1) == 10
    assert candidate(timeSeries = [1, 2, 3, 4, 5],duration = 1) == 5
    assert candidate(timeSeries = [0, 5, 10, 15],duration = 5) == 20
    assert candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],duration = 1) == 10
    assert candidate(timeSeries = [10, 14, 15],duration = 4) == 9
    assert candidate(timeSeries = [1, 1, 1, 1],duration = 2) == 2
    assert candidate(timeSeries = [1, 2],duration = 2) == 3
    assert candidate(timeSeries = [1, 4],duration = 2) == 4
    assert candidate(timeSeries = [10, 20, 30, 40, 50],duration = 10) == 50
    assert candidate(timeSeries = [1, 10, 15, 20, 25],duration = 5) == 25
    assert candidate(timeSeries = [5, 7, 8, 10],duration = 3) == 8
    assert candidate(timeSeries = [1, 100, 200, 300, 400, 500],duration = 10) == 60
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 8) == 53
    assert candidate(timeSeries = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],duration = 100) == 427
    assert candidate(timeSeries = [1, 3, 5, 6, 10, 12, 15],duration = 3) == 16
    assert candidate(timeSeries = [1, 3, 6, 10],duration = 3) == 11
    assert candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 1) == 1
    assert candidate(timeSeries = [1, 2, 3, 5, 8, 13, 21, 34, 55],duration = 5) == 32
    assert candidate(timeSeries = [0, 2, 4, 6, 8, 10],duration = 2) == 12
    assert candidate(timeSeries = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],duration = 10) == 19
    assert candidate(timeSeries = [5, 10, 15, 20, 25],duration = 3) == 15
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 8) == 80
    assert candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],duration = 3) == 30
    assert candidate(timeSeries = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],duration = 1) == 10
    assert candidate(timeSeries = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],duration = 2) == 15
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 1) == 10
    assert candidate(timeSeries = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],duration = 50) == 249
    assert candidate(timeSeries = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],duration = 7) == 47
    assert candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],duration = 2) == 30
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 7) == 52
    assert candidate(timeSeries = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45],duration = 8) == 52
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 7) == 32
    assert candidate(timeSeries = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40],duration = 5) == 44
    assert candidate(timeSeries = [2, 3, 5, 6, 8, 9, 11],duration = 2) == 11
    assert candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],duration = 2) == 30
    assert candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 1) == 11
    assert candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 5) == 23
    assert candidate(timeSeries = [0, 2, 5, 10, 15, 20, 25],duration = 5) == 30
    assert candidate(timeSeries = [0, 5, 10, 15, 20, 25, 30, 35, 40],duration = 5) == 45
    assert candidate(timeSeries = [1, 4, 7, 10, 13, 16],duration = 3) == 18
    assert candidate(timeSeries = [0, 2, 5, 9, 12, 15, 18, 21, 24, 27],duration = 5) == 32
    assert candidate(timeSeries = [100, 200, 300, 400, 500],duration = 150) == 550
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 7) == 32
    assert candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],duration = 3) == 33
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],duration = 4) == 18
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 109
    assert candidate(timeSeries = [10, 12, 15, 17, 18, 20, 25, 30],duration = 4) == 22
    assert candidate(timeSeries = [1, 3, 5, 7, 9],duration = 3) == 11
    assert candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],duration = 2) == 16
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],duration = 2) == 16
    assert candidate(timeSeries = [100, 101, 102, 103, 104, 105],duration = 5) == 10
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],duration = 1) == 20
    assert candidate(timeSeries = [2, 5, 10, 15, 20],duration = 6) == 24
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 3) == 18
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],duration = 15) == 60
    assert candidate(timeSeries = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],duration = 10) == 60
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 10) == 99
    assert candidate(timeSeries = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9],duration = 3) == 11
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],duration = 10) == 39
    assert candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],duration = 2) == 40
    assert candidate(timeSeries = [1, 2, 3, 5, 7, 9, 12, 15, 20, 25],duration = 2) == 18
    assert candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],duration = 15) == 305
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 15) == 104
    assert candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 2) == 20
    assert candidate(timeSeries = [0, 2, 5, 10, 15, 20, 25, 30],duration = 10) == 40
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 3) == 12
    assert candidate(timeSeries = [1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 26],duration = 4) == 29
    assert candidate(timeSeries = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],duration = 10) == 100
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],duration = 1) == 20
    assert candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 100
    assert candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],duration = 2) == 20
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15],duration = 3) == 15
    assert candidate(timeSeries = [100, 102, 105, 110, 115, 121, 128, 136, 145, 155],duration = 15) == 70
    assert candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 1) == 1
    assert candidate(timeSeries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],duration = 2) == 20
    assert candidate(timeSeries = [5, 10, 15, 20, 25],duration = 5) == 25
    assert candidate(timeSeries = [0, 0, 0, 0, 0],duration = 10000) == 10000
    assert candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14],duration = 2) == 16
    assert candidate(timeSeries = [1000, 1005, 1010, 1015, 1020, 1025],duration = 5) == 30
    assert candidate(timeSeries = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],duration = 50) == 500
    assert candidate(timeSeries = [2, 2, 2, 2, 2],duration = 5) == 5
    assert candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 5) == 5
    assert candidate(timeSeries = [2, 4, 8, 12, 16, 20, 24, 28],duration = 6) == 32
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30],duration = 5) == 30
    assert candidate(timeSeries = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],duration = 50) == 263
    assert candidate(timeSeries = [1, 3, 6, 10, 15],duration = 3) == 14
    assert candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 5) == 25
    assert candidate(timeSeries = [1, 3, 5, 6, 8, 10, 12, 15],duration = 4) == 18
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 2) == 11
    assert candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],duration = 3) == 33
    assert candidate(timeSeries = [1, 3, 6, 10, 15, 21, 28, 36, 45],duration = 7) == 48
    assert candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 100
    assert candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 3) == 13
    assert candidate(timeSeries = [5, 15, 25, 35, 45, 55],duration = 10) == 60
    assert candidate(timeSeries = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 10) == 110
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],duration = 10) == 149
    assert candidate(timeSeries = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],duration = 100) == 1099
    assert candidate(timeSeries = [1, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 5) == 53
    assert candidate(timeSeries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],duration = 3) == 23
    assert candidate(timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],duration = 5) == 14
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],duration = 8) == 78
    assert candidate(timeSeries = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],duration = 3) == 45
    assert candidate(timeSeries = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82],duration = 9) == 90
    assert candidate(timeSeries = [5, 10, 15, 20, 25, 30, 35, 40],duration = 10) == 45
    assert candidate(timeSeries = [1, 4, 8, 12, 16],duration = 3) == 15
    assert candidate(timeSeries = [100, 200, 300, 400, 500],duration = 150) == 550
    assert candidate(timeSeries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],duration = 50) == 500
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],duration = 50) == 249
    assert candidate(timeSeries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],duration = 100) == 100
    assert candidate(timeSeries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],duration = 15) == 105
    assert candidate(timeSeries = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],duration = 7) == 77
    assert candidate(timeSeries = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],duration = 10) == 10
    assert candidate(timeSeries = [1, 2, 3, 10, 15, 20],duration = 5) == 22
    assert candidate(timeSeries = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],duration = 9) == 90
    assert candidate(timeSeries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],duration = 2) == 27


