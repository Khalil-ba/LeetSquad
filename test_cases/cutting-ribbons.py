def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [5, 5, 5, 5, 5],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [5, 5, 5, 5, 5],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5],k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5],k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000],k = 100000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000],k = 100000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10, 10],k = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10, 10],k = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000],k = 3) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000],k = 3) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 3, 5, 7, 9],k = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 3, 5, 7, 9],k = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10, 10, 10],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10, 10, 10],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000],k = 1) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000],k = 1) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [9, 7, 5],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [9, 7, 5],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [5, 7, 9],k = 22) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [5, 7, 9],k = 22) == 0: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10, 10],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10, 10],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [7, 5, 9],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [7, 5, 9],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1],k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50],k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50],k = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50],k = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50],k = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000, 100000],k = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000, 100000],k = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [15, 15, 15, 15, 15],k = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [15, 15, 15, 15, 15],k = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 500000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 500000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 20) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 20) == 35: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 20) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 20) == 83: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7],k = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7],k = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [12345, 12345, 12345, 12345, 12345],k = 25000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [12345, 12345, 12345, 12345, 12345],k = 25000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 22: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [33, 33, 33, 33, 33],k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [33, 33, 33, 33, 33],k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 1000, 1000, 1000, 1000],k = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 1000, 1000, 1000, 1000],k = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10000, 20000, 30000, 40000, 50000],k = 100) == 1470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10000, 20000, 30000, 40000, 50000],k = 100) == 1470: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10000, 10000, 10000, 10000, 10000],k = 10000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10000, 10000, 10000, 10000, 10000],k = 10000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50],k = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50],k = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [9, 7, 5, 3, 1],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [9, 7, 5, 3, 1],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 50000, 25000, 12500, 6250],k = 15) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 50000, 25000, 12500, 6250],k = 15) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 50) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 50) == 200: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 100000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 100000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [500, 400, 300, 200, 100],k = 15) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [500, 400, 300, 200, 100],k = 15) == 100: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 999) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 999) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 20: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 1000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 1000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [99999, 99999, 99999, 99999, 99999],k = 250000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [99999, 99999, 99999, 99999, 99999],k = 250000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],k = 25) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],k = 25) == 20: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100, 200, 300, 400, 500],k = 10) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100, 200, 300, 400, 500],k = 10) == 125: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 10) == 49997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 10) == 49997: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 499975) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 499975) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 25) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 25) == 30: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [99999, 99999, 99999, 99999, 99999],k = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [99999, 99999, 99999, 99999, 99999],k = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 35) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 35) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50],k = 12) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50],k = 12) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 10, 100, 1000, 10000],k = 1000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 10, 100, 1000, 10000],k = 1000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 11: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 2000, 3000, 4000, 5000],k = 100) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 2000, 3000, 4000, 5000],k = 100) == 147: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],k = 20) == 8333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],k = 20) == 8333: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],k = 20) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],k = 20) == 22: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 1) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 1) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 50) == 19998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 50) == 19998: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 1000, 1000, 1000, 1000],k = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 1000, 1000, 1000, 1000],k = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 30) == 1600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 30) == 1600: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [15, 25, 35, 45, 55, 65, 75, 85, 95],k = 20) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [15, 25, 35, 45, 55, 65, 75, 85, 95],k = 20) == 21: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 100: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [100, 200, 300, 400, 500],k = 15) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [100, 200, 300, 400, 500],k = 15) == 100: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 5) == 99995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 5) == 99995: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3
    assert candidate(ribbons = [1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(ribbons = [5, 5, 5, 5, 5],k = 5) == 5
    assert candidate(ribbons = [1, 2, 3, 4, 5],k = 1) == 5
    assert candidate(ribbons = [1, 2, 3, 4, 5],k = 15) == 1
    assert candidate(ribbons = [100000, 100000, 100000],k = 100000) == 2
    assert candidate(ribbons = [10, 10, 10, 10],k = 8) == 5
    assert candidate(ribbons = [100000, 100000, 100000],k = 3) == 100000
    assert candidate(ribbons = [1, 3, 5, 7, 9],k = 9) == 2
    assert candidate(ribbons = [10, 10, 10, 10, 10],k = 1) == 10
    assert candidate(ribbons = [100000],k = 1) == 100000
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 1
    assert candidate(ribbons = [10, 20, 30],k = 5) == 10
    assert candidate(ribbons = [10, 10, 10],k = 5) == 5
    assert candidate(ribbons = [1, 2, 3, 4, 5],k = 10) == 1
    assert candidate(ribbons = [1, 2, 3, 4, 5],k = 5) == 2
    assert candidate(ribbons = [9, 7, 5],k = 3) == 5
    assert candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 10) == 50
    assert candidate(ribbons = [5, 7, 9],k = 22) == 0
    assert candidate(ribbons = [10, 10, 10, 10],k = 5) == 5
    assert candidate(ribbons = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(ribbons = [7, 5, 9],k = 4) == 4
    assert candidate(ribbons = [1, 1, 1, 1, 1],k = 3) == 1
    assert candidate(ribbons = [10, 20, 30, 40, 50],k = 10) == 12
    assert candidate(ribbons = [10, 20, 30, 40, 50],k = 5) == 20
    assert candidate(ribbons = [1],k = 1) == 1
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(ribbons = [100000, 100000, 100000, 100000],k = 100000) == 4
    assert candidate(ribbons = [15, 15, 15, 15, 15],k = 6) == 7
    assert candidate(ribbons = [1, 1, 1, 1],k = 1) == 1
    assert candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 1000) == 0
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1
    assert candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 500000) == 1
    assert candidate(ribbons = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 20) == 35
    assert candidate(ribbons = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 20) == 83
    assert candidate(ribbons = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7],k = 20) == 4
    assert candidate(ribbons = [12345, 12345, 12345, 12345, 12345],k = 25000) == 2
    assert candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 22
    assert candidate(ribbons = [33, 33, 33, 33, 33],k = 10) == 16
    assert candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 100) == 10
    assert candidate(ribbons = [1000, 1000, 1000, 1000, 1000],k = 1) == 1000
    assert candidate(ribbons = [10000, 20000, 30000, 40000, 50000],k = 100) == 1470
    assert candidate(ribbons = [10000, 10000, 10000, 10000, 10000],k = 10000) == 5
    assert candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 20) == 50
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 2
    assert candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 10
    assert candidate(ribbons = [10, 20, 30, 40, 50],k = 100) == 1
    assert candidate(ribbons = [9, 7, 5, 3, 1],k = 5) == 3
    assert candidate(ribbons = [100000, 50000, 25000, 12500, 6250],k = 15) == 12500
    assert candidate(ribbons = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 50) == 200
    assert candidate(ribbons = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 100000) == 1
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 10
    assert candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 5
    assert candidate(ribbons = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 30) == 5
    assert candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 100000) == 5
    assert candidate(ribbons = [500, 400, 300, 200, 100],k = 15) == 100
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 1
    assert candidate(ribbons = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 999) == 10
    assert candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 20
    assert candidate(ribbons = [100000, 100000, 100000, 100000, 100000],k = 1000000) == 0
    assert candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 10
    assert candidate(ribbons = [99999, 99999, 99999, 99999, 99999],k = 250000) == 1
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 21) == 0
    assert candidate(ribbons = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],k = 25) == 20
    assert candidate(ribbons = [100, 200, 300, 400, 500],k = 10) == 125
    assert candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 10) == 49997
    assert candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 499975) == 1
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 4
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(ribbons = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 25) == 30
    assert candidate(ribbons = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 10
    assert candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 40
    assert candidate(ribbons = [99999, 99999, 99999, 99999, 99999],k = 100000) == 4
    assert candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 9) == 10
    assert candidate(ribbons = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 35) == 1400
    assert candidate(ribbons = [10, 20, 30, 40, 50],k = 12) == 10
    assert candidate(ribbons = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 2
    assert candidate(ribbons = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 10
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 1
    assert candidate(ribbons = [1, 10, 100, 1000, 10000],k = 1000) == 11
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3
    assert candidate(ribbons = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 100) == 5
    assert candidate(ribbons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 11
    assert candidate(ribbons = [1000, 2000, 3000, 4000, 5000],k = 100) == 147
    assert candidate(ribbons = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],k = 20) == 8333
    assert candidate(ribbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 25) == 6
    assert candidate(ribbons = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],k = 20) == 22
    assert candidate(ribbons = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 1) == 100000
    assert candidate(ribbons = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 50) == 19998
    assert candidate(ribbons = [1000, 1000, 1000, 1000, 1000],k = 100) == 50
    assert candidate(ribbons = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 30) == 1600
    assert candidate(ribbons = [15, 25, 35, 45, 55, 65, 75, 85, 95],k = 20) == 21
    assert candidate(ribbons = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 1000000) == 1
    assert candidate(ribbons = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 100
    assert candidate(ribbons = [100, 200, 300, 400, 500],k = 15) == 100
    assert candidate(ribbons = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(ribbons = [99999, 99998, 99997, 99996, 99995],k = 5) == 99995


