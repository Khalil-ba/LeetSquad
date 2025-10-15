def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50],k = 5) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50],k = 5) == 140: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100000000, 100000000, 100000000],k = 2) == 199999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100000000, 100000000, 100000000],k = 2) == 199999999: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100000000, 100000000, 100000000, 100000000],k = 2) == 199999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100000000, 100000000, 100000000, 100000000],k = 2) == 199999999: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 25: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6],k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6],k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 100, 100],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 100, 100],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 3, 4, 5],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 3, 4, 5],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 4, 3, 2, 1],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 4, 3, 2, 1],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 334: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 12) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 12) == 110: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 18) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 18) == 55: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50],k = 3) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50],k = 3) == 117: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 7) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 7) == 24: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000, 30000000, 20000000, 10000000],k = 10) == 549999955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000, 30000000, 20000000, 10000000],k = 10) == 549999955: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 5455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 5455: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 140: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 110: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 10) == 910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 10) == 910: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 492
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 492: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 100000000, 1, 100000000, 1, 100000000, 1, 100000000, 1, 100000000],k = 5) == 499999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 100000000, 1, 100000000, 1, 100000000, 1, 100000000, 1, 100000000],k = 5) == 499999990: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79],k = 15) == 1260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79],k = 15) == 1260: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15) == 273
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15) == 273: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == 156: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 63: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 15) == 9995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 15) == 9995: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 63: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 110: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000, 30000000, 20000000, 10000000],k = 5) == 399999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000, 30000000, 20000000, 10000000],k = 5) == 399999990: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 465: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 9, 7, 5, 3, 1, 8, 6, 4, 2, 0],k = 10) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 9, 7, 5, 3, 1, 8, 6, 4, 2, 0],k = 10) == 33: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 10) == 910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 10) == 910: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 3990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 3990: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 3) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 3) == 132: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 15) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 15) == 256: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 4) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 4) == 34: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10],k = 15) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10],k = 15) == 43: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 8) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 8) == 25: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 4, 3, 2, 1],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 4, 3, 2, 1],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 55: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 390: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 20: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 64: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 50, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 50, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 159: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 8) == 772
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 8) == 772: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 1845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 1845: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 390: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 8) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 8) == 40: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [20, 15, 10, 5, 0, 0, 0, 0, 0, 0],k = 4) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [20, 15, 10, 5, 0, 0, 0, 0, 0, 0],k = 4) == 44: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 9) == 9864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 9) == 9864: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 240: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 15, 25, 35, 45, 55, 65],k = 4) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 15, 25, 35, 45, 55, 65],k = 4) == 194: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 240: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 110: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],k = 6) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],k = 6) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 8) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 8) == 64: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000],k = 3) == 269999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000],k = 3) == 269999997: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 15, 25, 35, 45, 55],k = 4) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 15, 25, 35, 45, 55],k = 4) == 154: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 505: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 255: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 3, 8, 6, 2, 7, 4, 1, 9],k = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 3, 8, 6, 2, 7, 4, 1, 9],k = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0],k = 5) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0],k = 5) == 183: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 267
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 267: {e}')
    
    total += 1
    try:
        result = candidate(happiness = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11],k = 5) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(happiness = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11],k = 5) == 35: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 30
    assert candidate(happiness = [10, 20, 30, 40, 50],k = 5) == 140
    assert candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 15
    assert candidate(happiness = [100000000, 100000000, 100000000],k = 2) == 199999999
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 30
    assert candidate(happiness = [1],k = 1) == 1
    assert candidate(happiness = [100000000, 100000000, 100000000, 100000000],k = 2) == 199999999
    assert candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 25
    assert candidate(happiness = [10, 9, 8, 7, 6],k = 3) == 24
    assert candidate(happiness = [100, 100, 100],k = 1) == 100
    assert candidate(happiness = [1, 1, 1, 1],k = 2) == 1
    assert candidate(happiness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 5) == 12
    assert candidate(happiness = [1, 2, 3],k = 2) == 4
    assert candidate(happiness = [2, 3, 4, 5],k = 1) == 5
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(happiness = [5, 4, 3, 2, 1],k = 3) == 9
    assert candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 12
    assert candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 40
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 24
    assert candidate(happiness = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 10) == 15
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 334
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 12) == 110
    assert candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 15
    assert candidate(happiness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 18) == 55
    assert candidate(happiness = [10, 20, 30, 40, 50],k = 3) == 117
    assert candidate(happiness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 7) == 24
    assert candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000, 30000000, 20000000, 10000000],k = 10) == 549999955
    assert candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 5455
    assert candidate(happiness = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 140
    assert candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 40
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 1
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 110
    assert candidate(happiness = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10) == 3
    assert candidate(happiness = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 10) == 910
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 492
    assert candidate(happiness = [1, 100000000, 1, 100000000, 1, 100000000, 1, 100000000, 1, 100000000],k = 5) == 499999990
    assert candidate(happiness = [98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79],k = 15) == 1260
    assert candidate(happiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15) == 273
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(happiness = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6) == 30
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1
    assert candidate(happiness = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == 156
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 63
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
    assert candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 15) == 9995
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 63
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 110
    assert candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000, 30000000, 20000000, 10000000],k = 5) == 399999990
    assert candidate(happiness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 465
    assert candidate(happiness = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 9, 7, 5, 3, 1, 8, 6, 4, 2, 0],k = 10) == 33
    assert candidate(happiness = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 10) == 910
    assert candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 30
    assert candidate(happiness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 40
    assert candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 3990
    assert candidate(happiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 3) == 132
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 30
    assert candidate(happiness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 15) == 256
    assert candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 4) == 34
    assert candidate(happiness = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10],k = 15) == 43
    assert candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 8) == 25
    assert candidate(happiness = [5, 4, 3, 2, 1],k = 3) == 9
    assert candidate(happiness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 55
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 390
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(happiness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 20
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 64
    assert candidate(happiness = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 3
    assert candidate(happiness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 25
    assert candidate(happiness = [100, 50, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 159
    assert candidate(happiness = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 8) == 772
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 1845
    assert candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 15
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 390
    assert candidate(happiness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 8) == 40
    assert candidate(happiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1
    assert candidate(happiness = [20, 15, 10, 5, 0, 0, 0, 0, 0, 0],k = 4) == 44
    assert candidate(happiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 9) == 9864
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 30
    assert candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 5) == 30
    assert candidate(happiness = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 240
    assert candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 30
    assert candidate(happiness = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 5) == 12
    assert candidate(happiness = [5, 15, 25, 35, 45, 55, 65],k = 4) == 194
    assert candidate(happiness = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 240
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 110
    assert candidate(happiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 30
    assert candidate(happiness = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],k = 6) == 30
    assert candidate(happiness = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 8) == 64
    assert candidate(happiness = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 10) == 14
    assert candidate(happiness = [100000000, 90000000, 80000000, 70000000, 60000000],k = 3) == 269999997
    assert candidate(happiness = [5, 15, 25, 35, 45, 55],k = 4) == 154
    assert candidate(happiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 30
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 505
    assert candidate(happiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 255
    assert candidate(happiness = [5, 3, 8, 6, 2, 7, 4, 1, 9],k = 4) == 24
    assert candidate(happiness = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0],k = 5) == 183
    assert candidate(happiness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 15
    assert candidate(happiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 267
    assert candidate(happiness = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11],k = 5) == 35


