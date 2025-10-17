def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(dist = [5, 4, 3, 2, 1],hour = 5.5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 4, 3, 2, 1],hour = 5.5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 4, 1, 2],hour = 3.5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 4, 1, 2],hour = 3.5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],hour = 9.0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],hour = 9.0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9],hour = 0.5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9],hour = 0.5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2],hour = 1.9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2],hour = 1.9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 100000],hour = 2.01) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 100000],hour = 2.01) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5],hour = 9.0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5],hour = 9.0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000],hour = 2.5) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000],hour = 2.5) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000],hour = 1.0) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000],hour = 1.0) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],hour = 3.5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],hour = 3.5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2],hour = 2.7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2],hour = 2.7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],hour = 10.0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],hour = 10.0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],hour = 2.5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],hour = 2.5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1],hour = 1.0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1],hour = 1.0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],hour = 29.99) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],hour = 29.99) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2],hour = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2],hour = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],hour = 3.0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],hour = 3.0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5],hour = 10.0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5],hour = 10.0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 100000.0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 100000.0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 19.99) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 19.99) == 11: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 4.5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 4.5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],hour = 50.0) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],hour = 50.0) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],hour = 30.0) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],hour = 30.0) == 50: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],hour = 15.5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],hour = 15.5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],hour = 15.0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],hour = 15.0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 10.1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 10.1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 50.0) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 50.0) == 12: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],hour = 20.0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],hour = 20.0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 9.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 9.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 10.5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 10.5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],hour = 45.0) == 13334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],hour = 45.0) == 13334: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],hour = 15.0) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],hour = 15.0) == 25: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 30.5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 30.5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],hour = 14.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],hour = 14.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],hour = 10.0) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],hour = 10.0) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000, 100000],hour = 25.0) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000, 100000],hour = 25.0) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 1, 1, 1, 1],hour = 10.1) == 14286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 1, 1, 1, 1],hour = 10.1) == 14286: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.99) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.99) == 11: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 200000, 300000, 400000, 500000],hour = 100.0) == 15385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 200000, 300000, 400000, 500000],hour = 100.0) == 15385: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 2.5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 2.5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 200000, 300000, 400000],hour = 25.0) == 42858
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 200000, 300000, 400000],hour = 25.0) == 42858: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],hour = 2.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],hour = 2.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99999, 99999, 99999],hour = 20.0) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99999, 99999, 99999],hour = 20.0) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],hour = 50.0) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],hour = 50.0) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 15.0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 15.0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 49.99) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 49.99) == 12: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000],hour = 7.0) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000],hour = 7.0) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 5.5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 5.5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 25.5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 25.5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],hour = 15.0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],hour = 15.0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 5.5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 5.5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 25.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 25.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 20.0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 20.0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],hour = 9.99) == 101010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],hour = 9.99) == 101010: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 15.0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 15.0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 10, 100, 1000, 10000],hour = 12.0) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 10, 100, 1000, 10000],hour = 12.0) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10000, 20000, 30000, 40000, 50000],hour = 12.5) == 14286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10000, 20000, 30000, 40000, 50000],hour = 12.5) == 14286: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],hour = 12.5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],hour = 12.5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],hour = 12.5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],hour = 12.5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 10.0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 10.0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 19.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 19.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 18.0) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 18.0) == 40: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 18.0) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 18.0) == 40: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],hour = 9.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],hour = 9.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 1.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 1.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 20.0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 20.0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 15.25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 15.25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 4.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 4.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 5.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 5.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],hour = 15.5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],hour = 15.5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 9.5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 9.5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99999, 99999, 99999, 99999],hour = 25.0) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99999, 99999, 99999, 99999],hour = 25.0) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],hour = 10.0) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],hour = 10.0) == 200: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 19.99) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 19.99) == 21: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],hour = 50.5) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],hour = 50.5) == 118: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 11.0) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 11.0) == 9: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],hour = 14.0) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],hour = 14.0) == 125: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],hour = 20.0) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],hour = 20.0) == 84: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 50.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 50.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000],hour = 10.5) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000],hour = 10.5) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],hour = 10.0) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],hour = 10.0) == 19: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],hour = 25.0) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],hour = 25.0) == 70: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 99999, 99998, 99997, 99996],hour = 5.0) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 99999, 99998, 99997, 99996],hour = 5.0) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 21.5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 21.5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 9.5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 9.5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 2.99) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 2.99) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25],hour = 9.0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25],hour = 9.0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 9.99) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 9.99) == 102: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 5.0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 5.0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 100000, 1, 1, 1],hour = 10.1) == 14286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 100000, 1, 1, 1],hour = 10.1) == 14286: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 20.0) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 20.0) == 35: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],hour = 30.5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],hour = 30.5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99999, 99999],hour = 3.5) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99999, 99999],hour = 3.5) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10000, 10000, 10000, 10000, 10000],hour = 25.0) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10000, 10000, 10000, 10000, 10000],hour = 25.0) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],hour = 7.5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],hour = 7.5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 1.5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 1.5) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(dist = [5, 4, 3, 2, 1],hour = 5.5) == 4
    assert candidate(dist = [5, 4, 1, 2],hour = 3.5) == 5
    assert candidate(dist = [1, 2, 3, 4, 5],hour = 9.0) == 2
    assert candidate(dist = [9],hour = 0.5) == 18
    assert candidate(dist = [1, 3, 2],hour = 1.9) == -1
    assert candidate(dist = [1, 1, 100000],hour = 2.01) == 10000000
    assert candidate(dist = [5, 5, 5, 5, 5],hour = 9.0) == 5
    assert candidate(dist = [100000],hour = 2.5) == 40000
    assert candidate(dist = [100000],hour = 1.0) == 100000
    assert candidate(dist = [10, 10, 10],hour = 3.5) == 10
    assert candidate(dist = [1, 3, 2],hour = 2.7) == 3
    assert candidate(dist = [1, 2, 3, 4, 5],hour = 10.0) == 2
    assert candidate(dist = [10, 10, 10],hour = 2.5) == 20
    assert candidate(dist = [1],hour = 1.0) == 1
    assert candidate(dist = [10, 10, 10],hour = 29.99) == 2
    assert candidate(dist = [1, 3, 2],hour = 6) == 1
    assert candidate(dist = [10, 10, 10],hour = 3.0) == 10
    assert candidate(dist = [5, 5, 5, 5],hour = 10.0) == 3
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 100000.0) == 1
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 19.99) == 11
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 4.5) == -1
    assert candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],hour = 50.0) == 20000
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],hour = 30.0) == 50
    assert candidate(dist = [100, 200, 300, 400, 500],hour = 15.5) == 100
    assert candidate(dist = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],hour = 15.0) == 100
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 10.1) == 1
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 50.0) == 12
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.5) == 20
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],hour = 20.0) == 10
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 9.0) == -1
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 10.5) == 20
    assert candidate(dist = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],hour = 45.0) == 13334
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],hour = 15.0) == 25
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 30.5) == 20
    assert candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],hour = 14.0) == -1
    assert candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],hour = 10.0) == 100000
    assert candidate(dist = [100000, 100000, 100000, 100000, 100000],hour = 25.0) == 20000
    assert candidate(dist = [100000, 1, 1, 1, 1],hour = 10.1) == 14286
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.99) == 11
    assert candidate(dist = [100000, 200000, 300000, 400000, 500000],hour = 100.0) == 15385
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 2.5) == -1
    assert candidate(dist = [100000, 200000, 300000, 400000],hour = 25.0) == 42858
    assert candidate(dist = [1, 2, 3, 4, 5],hour = 2.0) == -1
    assert candidate(dist = [99999, 99999, 99999, 99999],hour = 20.0) == 20000
    assert candidate(dist = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],hour = 50.0) == 1200
    assert candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 15.0) == 5
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 49.99) == 12
    assert candidate(dist = [1000, 2000, 3000],hour = 7.0) == 1000
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 5.5) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 25.5) == 14
    assert candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],hour = 15.0) == 5
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 5.5) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 25.0) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 20.0) == 4
    assert candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],hour = 9.99) == 101010
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 15.0) == 5
    assert candidate(dist = [1, 10, 100, 1000, 10000],hour = 12.0) == 1250
    assert candidate(dist = [10000, 20000, 30000, 40000, 50000],hour = 12.5) == 14286
    assert candidate(dist = [10, 20, 30, 40, 50],hour = 12.5) == 15
    assert candidate(dist = [10, 20, 30, 40, 50],hour = 12.5) == 15
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 10.0) == 1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 19.0) == -1
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 18.0) == 40
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 18.0) == 40
    assert candidate(dist = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],hour = 9.0) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 1.0) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 20.0) == 1
    assert candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 15.25) == 5
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],hour = 4.0) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 5.0) == -1
    assert candidate(dist = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],hour = 15.5) == 5
    assert candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 9.5) == 10
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 9.0) == -1
    assert candidate(dist = [99999, 99999, 99999, 99999, 99999],hour = 25.0) == 20000
    assert candidate(dist = [100, 200, 300, 400, 500],hour = 10.0) == 200
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 19.99) == 21
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],hour = 50.5) == 118
    assert candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],hour = 11.0) == 9
    assert candidate(dist = [100, 200, 300, 400, 500],hour = 14.0) == 125
    assert candidate(dist = [100, 200, 300, 400, 500],hour = 20.0) == 84
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 50.0) == -1
    assert candidate(dist = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000],hour = 10.5) == 10000
    assert candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],hour = 10.0) == 19
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],hour = 25.0) == 70
    assert candidate(dist = [100000, 99999, 99998, 99997, 99996],hour = 5.0) == 100000
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],hour = 21.5) == 18
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 9.5) == 2
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 2.99) == -1
    assert candidate(dist = [5, 10, 15, 20, 25],hour = 9.0) == 10
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 9.99) == 102
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],hour = 5.0) == -1
    assert candidate(dist = [1, 100000, 1, 1, 1],hour = 10.1) == 14286
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],hour = 20.0) == 35
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],hour = 30.5) == 200
    assert candidate(dist = [99999, 99999, 99999],hour = 3.5) == 99999
    assert candidate(dist = [10000, 10000, 10000, 10000, 10000],hour = 25.0) == 2000
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],hour = 7.5) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],hour = 1.5) == -1


