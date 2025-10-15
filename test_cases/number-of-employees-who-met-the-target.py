def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(hours = [5, 5, 5, 5, 5],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 5, 5, 5, 5],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [3, 4, 5, 6, 7],target = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [3, 4, 5, 6, 7],target = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 5, 7, 9],target = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 5, 7, 9],target = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10],target = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10],target = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 1, 2, 3, 4],target = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 1, 2, 3, 4],target = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50],target = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50],target = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 50, 50, 50, 50],target = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 50, 50, 50, 50],target = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [3, 5, 7, 9, 11],target = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [3, 5, 7, 9, 11],target = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5],target = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5],target = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100, 200, 300],target = 150) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100, 200, 300],target = 150) == 2: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 1, 1, 1, 1],target = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 1, 1, 1, 1],target = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [3, 3, 3, 3, 3],target = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [3, 3, 3, 3, 3],target = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 1, 4, 2, 2],target = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 1, 4, 2, 2],target = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100, 200, 300, 400, 500],target = 150) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100, 200, 300, 400, 500],target = 150) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 55000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 55000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10000, 20000, 30000, 40000, 50000],target = 30000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10000, 20000, 30000, 40000, 50000],target = 30000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],target = 45) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],target = 45) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 150) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 150) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330],target = 198) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330],target = 198) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],target = 54) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],target = 54) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 101) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 101) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],target = 25) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],target = 25) == 13: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100000, 50000, 75000, 25000, 0],target = 50000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100000, 50000, 75000, 25000, 0],target = 50000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 100000, 50000, 75000, 25000],target = 50000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 100000, 50000, 75000, 25000],target = 50000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [15, 25, 35, 45, 55],target = 35) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [15, 25, 35, 45, 55],target = 35) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100, 200, 300, 400, 500],target = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100, 200, 300, 400, 500],target = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 95) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 95) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 50, 50, 50, 50],target = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 50, 50, 50, 50],target = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [99995, 99996, 99997, 99998, 99999, 100000],target = 99995) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [99995, 99996, 99997, 99998, 99999, 100000],target = 99995) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 50) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 50) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 10, 100, 1000, 10000, 100000, 0, 0, 0, 0],target = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 10, 100, 1000, 10000, 100000, 0, 0, 0, 0],target = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40],target = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40],target = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],target = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],target = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 9) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 9) == 30: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],target = 100000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],target = 100000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 40, 30, 20, 10, 0],target = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 40, 30, 20, 10, 0],target = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 39) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 39) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50],target = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50],target = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 10, 100, 1000, 10000],target = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 10, 100, 1000, 10000],target = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50],target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50],target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],target = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],target = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],target = 60) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],target = 60) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 25) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 25) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 15, 25, 35, 45],target = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 15, 25, 35, 45],target = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],target = 99995) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],target = 99995) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [9, 9, 9, 9, 9],target = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [9, 9, 9, 9, 9],target = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],target = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],target = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17],target = 8) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17],target = 8) == 18: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],target = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],target = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50],target = 25) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50],target = 25) == 14: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 50000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 50000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40],target = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40],target = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hours = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],target = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],target = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50, 40, 30, 20, 10],target = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50, 40, 30, 20, 10],target = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 40) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 40) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],target = 125) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],target = 125) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 25) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 25) == 26: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100000, 99999, 99998, 99997, 99996],target = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100000, 99999, 99998, 99997, 99996],target = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 99) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 99) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100000, 99999, 100000, 100000, 99999],target = 100000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100000, 99999, 100000, 100000, 99999],target = 100000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],target = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],target = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 105) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 105) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],target = 99) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],target = 99) == 52: {e}')
    
    total += 1
    try:
        result = candidate(hours = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == 39: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],target = 50000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],target = 50000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == 57: {e}')
    
    total += 1
    try:
        result = candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hours = [12, 34, 56, 78, 90],target = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [12, 34, 56, 78, 90],target = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hours = [30, 25, 20, 15, 10],target = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hours = [30, 25, 20, 15, 10],target = 20) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(hours = [5, 5, 5, 5, 5],target = 5) == 5
    assert candidate(hours = [3, 4, 5, 6, 7],target = 4) == 4
    assert candidate(hours = [1, 5, 7, 9],target = 8) == 1
    assert candidate(hours = [10, 10, 10],target = 10) == 3
    assert candidate(hours = [0, 1, 2, 3, 4],target = 2) == 3
    assert candidate(hours = [10, 20, 30, 40, 50],target = 25) == 3
    assert candidate(hours = [50, 50, 50, 50, 50],target = 50) == 5
    assert candidate(hours = [1],target = 1) == 1
    assert candidate(hours = [3, 5, 7, 9, 11],target = 10) == 1
    assert candidate(hours = [1, 2, 3, 4, 5],target = 0) == 5
    assert candidate(hours = [100, 200, 300],target = 150) == 2
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 6
    assert candidate(hours = [1, 1, 1, 1, 1],target = 1) == 5
    assert candidate(hours = [3, 3, 3, 3, 3],target = 3) == 5
    assert candidate(hours = [0, 0, 0, 0, 0],target = 1) == 0
    assert candidate(hours = [5, 1, 4, 2, 2],target = 6) == 0
    assert candidate(hours = [100, 200, 300, 400, 500],target = 150) == 4
    assert candidate(hours = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 55000) == 5
    assert candidate(hours = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 25) == 10
    assert candidate(hours = [10000, 20000, 30000, 40000, 50000],target = 30000) == 3
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0
    assert candidate(hours = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],target = 45) == 6
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 150) == 6
    assert candidate(hours = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330],target = 198) == 5
    assert candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 5) == 10
    assert candidate(hours = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],target = 54) == 10
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 101) == 0
    assert candidate(hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],target = 25) == 13
    assert candidate(hours = [100000, 50000, 75000, 25000, 0],target = 50000) == 3
    assert candidate(hours = [0, 100000, 50000, 75000, 25000],target = 50000) == 3
    assert candidate(hours = [15, 25, 35, 45, 55],target = 35) == 3
    assert candidate(hours = [100, 200, 300, 400, 500],target = 500) == 1
    assert candidate(hours = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 95) == 5
    assert candidate(hours = [50, 50, 50, 50, 50],target = 50) == 5
    assert candidate(hours = [99995, 99996, 99997, 99998, 99999, 100000],target = 99995) == 6
    assert candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 50) == 11
    assert candidate(hours = [1, 10, 100, 1000, 10000, 100000, 0, 0, 0, 0],target = 100) == 4
    assert candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == 6
    assert candidate(hours = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 25) == 8
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 0) == 10
    assert candidate(hours = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40],target = 25) == 5
    assert candidate(hours = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],target = 100) == 7
    assert candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 9) == 30
    assert candidate(hours = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 5) == 5
    assert candidate(hours = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],target = 100000) == 10
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 15) == 16
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 2) == 9
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == 5
    assert candidate(hours = [50, 40, 30, 20, 10, 0],target = 25) == 3
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 39) == 1
    assert candidate(hours = [10, 20, 30, 40, 50],target = 25) == 3
    assert candidate(hours = [1, 10, 100, 1000, 10000],target = 50) == 3
    assert candidate(hours = [10, 20, 30, 40, 50],target = 100) == 0
    assert candidate(hours = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == 26
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 10) == 10
    assert candidate(hours = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],target = 10) == 5
    assert candidate(hours = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],target = 60) == 5
    assert candidate(hours = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 25) == 20
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == 10
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0
    assert candidate(hours = [5, 15, 25, 35, 45],target = 25) == 3
    assert candidate(hours = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],target = 99995) == 5
    assert candidate(hours = [9, 9, 9, 9, 9],target = 9) == 5
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == 6
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],target = 30) == 15
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == 1
    assert candidate(hours = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1000) == 1
    assert candidate(hours = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17],target = 8) == 18
    assert candidate(hours = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],target = 5) == 6
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50],target = 25) == 14
    assert candidate(hours = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 50000) == 6
    assert candidate(hours = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40],target = 10) == 9
    assert candidate(hours = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],target = 25) == 8
    assert candidate(hours = [50, 40, 30, 20, 10],target = 25) == 3
    assert candidate(hours = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 40) == 6
    assert candidate(hours = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],target = 125) == 6
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 25) == 26
    assert candidate(hours = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 25) == 6
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 6
    assert candidate(hours = [100000, 99999, 99998, 99997, 99996],target = 100000) == 1
    assert candidate(hours = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 500) == 6
    assert candidate(hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 9) == 1
    assert candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 5) == 6
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 99) == 1
    assert candidate(hours = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 3) == 6
    assert candidate(hours = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 2) == 16
    assert candidate(hours = [100000, 99999, 100000, 100000, 99999],target = 100000) == 3
    assert candidate(hours = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],target = 3) == 10
    assert candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == 10
    assert candidate(hours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 10) == 1
    assert candidate(hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == 11
    assert candidate(hours = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 20) == 15
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 105) == 0
    assert candidate(hours = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],target = 99) == 52
    assert candidate(hours = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == 39
    assert candidate(hours = [0, 0, 0, 0, 0],target = 1) == 0
    assert candidate(hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 11) == 5
    assert candidate(hours = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],target = 50000) == 30
    assert candidate(hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == 57
    assert candidate(hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 0
    assert candidate(hours = [12, 34, 56, 78, 90],target = 50) == 3
    assert candidate(hours = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == 5
    assert candidate(hours = [30, 25, 20, 15, 10],target = 20) == 3


