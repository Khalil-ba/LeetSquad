def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 4, 7, 8],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 4, 7, 8],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [6, 5, 4, 3, 2, 1],k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [6, 5, 4, 3, 2, 1],k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60],k = 3) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60],k = 3) == 70: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 12) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 12) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 6) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 6) == 18: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 12) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 12) == 120: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 12) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 12) == 1: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 2, 3],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 2, 3],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 5, 3, 2, 4, 1],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 5, 3, 2, 4, 1],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 3) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 3) == 26: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [12, 3, 5, 8, 9, 4, 7, 6, 2, 10, 11, 1],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [12, 3, 5, 8, 9, 4, 7, 6, 2, 10, 11, 1],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 6) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 6) == 100: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 5) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 5) == 160: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 2) == 39000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 2) == 39000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 0],k = 4) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 0],k = 4) == 140: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 7) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 7) == 120: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 4) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 4) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],k = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],k = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 3) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 3) == 130: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == 36: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 7, 1, 10, 5, 2, 8, 6, 4, 9, 11, 12],k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 7, 1, 10, 5, 2, 8, 6, 4, 9, 11, 12],k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000],k = 6) == 20000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000],k = 6) == 20000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],k = 6) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],k = 6) == 24: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 36: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 5) == 1600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 5) == 1600: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 12) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 12) == 23: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [30, 15, 40, 10, 25, 5, 60, 45, 20, 50, 55, 35],k = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [30, 15, 40, 10, 25, 5, 60, 45, 20, 50, 55, 35],k = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 1) == 12000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 1) == 12000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [20, 10, 30, 25, 15, 5, 40, 35, 50, 100, 200, 50],k = 3) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [20, 10, 30, 25, 15, 5, 40, 35, 50, 100, 200, 50],k = 3) == 200: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14],k = 3) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14],k = 3) == 28: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 6) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 6) == 56: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 6) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 6) == 65: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],k = 4) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],k = 4) == 38: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 2) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 2) == 390: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 2) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 2) == 39: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 4) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 4) == 140: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 1) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 1) == 78: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 11) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 11) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000, 3000, 3000, 3000, 3000],k = 8) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000, 3000, 3000, 3000, 3000],k = 8) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],k = 4) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],k = 4) == 60: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145],k = 4) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145],k = 4) == 168: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 12) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 12) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 2) == 39000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 2) == 39000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 6) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 6) == 91: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 2) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 2) == 390: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 5) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 5) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 11],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 11],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000],k = 4) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000],k = 4) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1],k = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1],k = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],k = 3) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],k = 3) == 66: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 3) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 3) == 260: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 8) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 8) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 3) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 3) == 260: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 8) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 8) == 14: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 5, 7, 12, 4, 8, 9, 11, 6, 10, 2, 1],k = 3) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 5, 7, 12, 4, 8, 9, 11, 6, 10, 2, 1],k = 3) == 26: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3],k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3],k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 12) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 12) == 120: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == 36: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 6) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 6) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 1, 1, 1],k = 7) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 1, 1, 1],k = 7) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5],k = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5],k = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115],k = 5) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115],k = 5) == 150: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 3) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 3) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 26: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 6) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 6) == 14: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [7, 2, 8, 9, 4, 3, 6, 1, 5, 10, 11, 12],k = 3) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [7, 2, 8, 9, 4, 3, 6, 1, 5, 10, 11, 12],k = 3) == 26: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 1, 1, 1],k = 3) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 1, 1, 1],k = 3) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 40: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 8) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 8) == 60: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 6) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 6) == 130: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],k = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],k = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 20, 25],k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 20, 25],k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 3) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 3) == 56: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [5, 7, 12, 18, 23, 30, 37, 40, 45, 50, 55, 60],k = 3) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [5, 7, 12, 18, 23, 30, 37, 40, 45, 50, 55, 60],k = 3) == 128: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 5) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 5) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000, 100000, 10000],k = 6) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000, 100000, 10000],k = 6) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 1) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 1) == 78: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],k = 9) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],k = 9) == 144: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(jobs = [10000000, 5000000, 2500000, 1250000, 625000, 312500, 156250, 78125, 39062, 19531, 9765, 4882],k = 3) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(jobs = [10000000, 5000000, 2500000, 1250000, 625000, 312500, 156250, 78125, 39062, 19531, 9765, 4882],k = 3) == 10000000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(jobs = [1, 2, 4, 7, 8],k = 2) == 11
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == 20
    assert candidate(jobs = [6, 5, 4, 3, 2, 1],k = 6) == 6
    assert candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 20
    assert candidate(jobs = [10, 20, 30, 40, 50, 60],k = 3) == 70
    assert candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 12) == 10
    assert candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 3
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 6) == 13
    assert candidate(jobs = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 6) == 18
    assert candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 6) == 10
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 12) == 120
    assert candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 12) == 1
    assert candidate(jobs = [3, 2, 3],k = 3) == 3
    assert candidate(jobs = [5, 5, 3, 2, 4, 1],k = 3) == 7
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 3) == 26
    assert candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 15
    assert candidate(jobs = [12, 3, 5, 8, 9, 4, 7, 6, 2, 10, 11, 1],k = 5) == 16
    assert candidate(jobs = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 6) == 100
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 5) == 160
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 7) == 12
    assert candidate(jobs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 2) == 39000
    assert candidate(jobs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 0],k = 4) == 140
    assert candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == 18
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 7) == 120
    assert candidate(jobs = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 4) == 10000000
    assert candidate(jobs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],k = 4) == 40
    assert candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 3) == 130
    assert candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == 36
    assert candidate(jobs = [3, 7, 1, 10, 5, 2, 8, 6, 4, 9, 11, 12],k = 5) == 16
    assert candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 4) == 11
    assert candidate(jobs = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000],k = 6) == 20000000
    assert candidate(jobs = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],k = 6) == 24
    assert candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 36
    assert candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 5) == 1600
    assert candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 8) == 12
    assert candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 12) == 23
    assert candidate(jobs = [30, 15, 40, 10, 25, 5, 60, 45, 20, 50, 55, 35],k = 5) == 80
    assert candidate(jobs = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 1) == 12000000
    assert candidate(jobs = [20, 10, 30, 25, 15, 5, 40, 35, 50, 100, 200, 50],k = 3) == 200
    assert candidate(jobs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14],k = 3) == 28
    assert candidate(jobs = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 6) == 56
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200
    assert candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 6) == 65
    assert candidate(jobs = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],k = 4) == 38
    assert candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 6) == 4
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 2) == 390
    assert candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10],k = 4) == 20
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 2) == 39
    assert candidate(jobs = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 4) == 140
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 1) == 78
    assert candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 11) == 1200
    assert candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 7) == 12
    assert candidate(jobs = [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000, 3000, 3000, 3000, 3000],k = 8) == 3000
    assert candidate(jobs = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200
    assert candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 8
    assert candidate(jobs = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],k = 4) == 60
    assert candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 5) == 30
    assert candidate(jobs = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 12
    assert candidate(jobs = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145],k = 4) == 168
    assert candidate(jobs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 8) == 4
    assert candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 12) == 1200
    assert candidate(jobs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 2) == 39000
    assert candidate(jobs = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],k = 6) == 91
    assert candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 13
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 2) == 390
    assert candidate(jobs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 5) == 2048
    assert candidate(jobs = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 11],k = 6) == 13
    assert candidate(jobs = [1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000],k = 4) == 5000
    assert candidate(jobs = [7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1],k = 2) == 17
    assert candidate(jobs = [10000000, 10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 10000000
    assert candidate(jobs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],k = 3) == 66
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 3) == 260
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 200
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 12
    assert candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 8) == 20
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 3) == 260
    assert candidate(jobs = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 8) == 14
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == 20
    assert candidate(jobs = [3, 5, 7, 12, 4, 8, 9, 11, 6, 10, 2, 1],k = 3) == 26
    assert candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3],k = 5) == 11
    assert candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 3) == 14
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 12) == 120
    assert candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 4) == 36
    assert candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 6) == 1300
    assert candidate(jobs = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 1, 1, 1],k = 7) == 10000000
    assert candidate(jobs = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5],k = 6) == 7
    assert candidate(jobs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 4) == 11
    assert candidate(jobs = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115],k = 5) == 150
    assert candidate(jobs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],k = 3) == 2048
    assert candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1],k = 5) == 10
    assert candidate(jobs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 26
    assert candidate(jobs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11],k = 4) == 20
    assert candidate(jobs = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 6) == 14
    assert candidate(jobs = [7, 2, 8, 9, 4, 3, 6, 1, 5, 10, 11, 12],k = 3) == 26
    assert candidate(jobs = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 1, 1, 1, 1],k = 3) == 10000000
    assert candidate(jobs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 40
    assert candidate(jobs = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 4) == 8
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 12
    assert candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 8) == 60
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 6) == 130
    assert candidate(jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 5) == 18
    assert candidate(jobs = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],k = 4) == 14
    assert candidate(jobs = [9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 20, 25],k = 5) == 25
    assert candidate(jobs = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 3) == 56
    assert candidate(jobs = [5, 7, 12, 18, 23, 30, 37, 40, 45, 50, 55, 60],k = 3) == 128
    assert candidate(jobs = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 5) == 10000000
    assert candidate(jobs = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000, 100000, 10000],k = 6) == 10000000
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 1) == 78
    assert candidate(jobs = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],k = 9) == 144
    assert candidate(jobs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],k = 5) == 40
    assert candidate(jobs = [10000000, 5000000, 2500000, 1250000, 625000, 312500, 156250, 78125, 39062, 19531, 9765, 4882],k = 3) == 10000000


