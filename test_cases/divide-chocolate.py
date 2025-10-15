def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sweetness = [1, 3, 1, 5, 2],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 3, 1, 5, 2],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000],k = 0) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000],k = 0) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 29) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 29) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [3, 6, 8, 4, 2, 9, 3, 2, 1, 7],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [3, 6, 8, 4, 2, 9, 3, 2, 1, 7],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10, 1],k = 5) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10, 1],k = 5) == 111: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 7) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 7) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 9, 2, 8, 3, 7, 4, 6, 5],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 9, 2, 8, 3, 7, 4, 6, 5],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 19) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 19) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000, 100000, 100000, 100000, 100000],k = 2) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000, 100000, 100000, 100000, 100000],k = 2) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 19) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 19) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 9) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 9) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 120: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],k = 4) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],k = 4) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4],k = 32) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4],k = 32) == 4: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 100000, 10000, 1000, 100, 10, 1],k = 5) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 100000, 10000, 1000, 100, 10, 1],k = 5) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6],k = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6],k = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 6, 1, 2, 3, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4],k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 6, 1, 2, 3, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4],k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 19) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 19) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 14) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 14) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [500, 400, 300, 200, 100, 100, 200, 300, 400, 500],k = 4) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [500, 400, 300, 200, 100, 100, 200, 300, 400, 500],k = 4) == 500: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 29) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 29) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 12) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 12) == 20: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 5) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 5) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 7, 5, 3, 1],k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 7, 5, 3, 1],k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 55: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 3) == 199995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 3) == 199995: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3],k = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3],k = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],k = 4) == 90000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],k = 4) == 90000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == 16: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [100000, 100000, 100000, 100000, 100000],k = 4) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [100000, 100000, 100000, 100000, 100000],k = 4) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 23: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 9) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 9) == 160: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 90: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 24) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 24) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 45: {e}')
    
    total += 1
    try:
        result = candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sweetness = [1, 3, 1, 5, 2],k = 2) == 2
    assert candidate(sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4],k = 8) == 1
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 1
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 6
    assert candidate(sweetness = [100000],k = 0) == 100000
    assert candidate(sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 5
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 29) == 1
    assert candidate(sweetness = [3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 10) == 4
    assert candidate(sweetness = [3, 6, 8, 4, 2, 9, 3, 2, 1, 7],k = 3) == 9
    assert candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10, 1],k = 5) == 111
    assert candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 9
    assert candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 10
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 12
    assert candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 7) == 40000
    assert candidate(sweetness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 8
    assert candidate(sweetness = [1, 9, 2, 8, 3, 7, 4, 6, 5],k = 4) == 5
    assert candidate(sweetness = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 9) == 8
    assert candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 19) == 5
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 1
    assert candidate(sweetness = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 9) == 3
    assert candidate(sweetness = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 9) == 9
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 10
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 1
    assert candidate(sweetness = [100000, 100000, 100000, 100000, 100000],k = 2) == 100000
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 19) == 10
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 10
    assert candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 9) == 100000
    assert candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 120
    assert candidate(sweetness = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],k = 4) == 1001
    assert candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4],k = 32) == 4
    assert candidate(sweetness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 9
    assert candidate(sweetness = [1, 10, 100, 1000, 10000, 100000, 100000, 10000, 1000, 100, 10, 1],k = 5) == 1111
    assert candidate(sweetness = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 19) == 3
    assert candidate(sweetness = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6],k = 9) == 11
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
    assert candidate(sweetness = [5, 6, 1, 2, 3, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4],k = 10) == 6
    assert candidate(sweetness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 19) == 10
    assert candidate(sweetness = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 5
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 14) == 1
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 14) == 10
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 3
    assert candidate(sweetness = [500, 400, 300, 200, 100, 100, 200, 300, 400, 500],k = 4) == 500
    assert candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == 100000
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 10
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 29) == 1
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 12) == 20
    assert candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 8) == 8
    assert candidate(sweetness = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 20) == 19
    assert candidate(sweetness = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
    assert candidate(sweetness = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 4) == 11
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 15
    assert candidate(sweetness = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 5) == 100000
    assert candidate(sweetness = [9, 7, 5, 3, 1],k = 2) == 7
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 55
    assert candidate(sweetness = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 3) == 199995
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6) == 13
    assert candidate(sweetness = [3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 4, 3, 3],k = 25) == 3
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 2
    assert candidate(sweetness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1500
    assert candidate(sweetness = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],k = 4) == 90000
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == 16
    assert candidate(sweetness = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 10
    assert candidate(sweetness = [100000, 100000, 100000, 100000, 100000],k = 4) == 100000
    assert candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 5
    assert candidate(sweetness = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 23
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 9) == 160
    assert candidate(sweetness = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 10
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 1
    assert candidate(sweetness = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 25) == 9
    assert candidate(sweetness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 90
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 24) == 1
    assert candidate(sweetness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 19) == 1
    assert candidate(sweetness = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 8) == 1
    assert candidate(sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 1
    assert candidate(sweetness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 45
    assert candidate(sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 7


