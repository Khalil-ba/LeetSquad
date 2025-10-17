def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5],target = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5],target = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3],target = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3],target = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5],target = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5],target = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 2, 4, 3],target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 2, 4, 3],target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 4, 4, 5],target = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 4, 4, 5],target = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, 1000],target = 2000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, 1000],target = 2000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 3, 4, 7],target = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 3, 4, 7],target = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, 1000, 1000, 1000],target = 2000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, 1000, 1000, 1000],target = 2000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3],target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3],target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, 1000, 1000, 1000],target = 5000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, 1000, 1000, 1000],target = 5000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5],target = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5],target = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],target = 60) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],target = 60) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 4, 4, 4, 4, 4, 4, 4, 1],target = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 4, 4, 4, 4, 4, 4, 4, 1],target = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 3, 2, 6, 2, 3, 4],target = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 3, 2, 6, 2, 3, 4],target = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],target = 90) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],target = 90) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1],target = 1000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1],target = 1000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 4, 3, 2, 1, 3, 4, 2, 1, 3, 5, 2, 1, 3, 4, 2, 1, 3],target = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 4, 3, 2, 1, 3, 4, 2, 1, 3, 5, 2, 1, 3, 4, 2, 1, 3],target = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 30) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 30) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 500) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 500) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 300) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 300) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 1, 5, 2, 3, 1, 4, 2, 3, 1, 5, 2, 3, 1, 4, 2, 3, 1],target = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 1, 5, 2, 3, 1, 4, 2, 3, 1, 5, 2, 3, 1, 4, 2, 3, 1],target = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 2, 3, 5, 7, 9, 11, 13, 15],target = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 2, 3, 5, 7, 9, 11, 13, 15],target = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8, 6],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8, 6],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 4, 1, 1, 2, 3, 5, 3, 2, 3, 4, 1],target = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 4, 1, 1, 2, 3, 5, 3, 2, 3, 4, 1],target = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 30) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 30) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50],target = 60) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50],target = 60) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 2, 3, 9, 4, 5, 9, 6, 7, 8, 9],target = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 2, 3, 9, 4, 5, 9, 6, 7, 8, 9],target = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 3, 4, 1, 5, 2, 3, 4, 1, 5, 2, 3, 4, 1, 5, 2, 3, 4, 1],target = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 3, 4, 1, 5, 2, 3, 4, 1, 5, 2, 3, 4, 1, 5, 2, 3, 4, 1],target = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3],target = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3],target = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 8, 3, 4, 7, 6, 5, 4, 3, 2, 1],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 8, 3, 4, 7, 6, 5, 4, 3, 2, 1],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 21) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 21) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],target = 3000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],target = 3000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3],target = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3],target = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],target = 600) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],target = 600) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 2, 2, 3, 3, 2, 2, 2, 3],target = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 2, 2, 3, 3, 2, 2, 2, 3],target = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300],target = 600) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300],target = 600) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 5, 2, 4, 8, 6, 3, 7],target = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 5, 2, 4, 8, 6, 3, 7],target = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3],target = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3],target = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 400) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 400) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],target = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],target = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 100, 300, 200, 400, 300, 500, 400, 600],target = 300) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 100, 300, 200, 400, 300, 500, 400, 600],target = 300) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],target = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],target = 1000) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [5, 5, 5, 5, 5],target = 10) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 6) == 6
    assert candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3],target = 6) == 5
    assert candidate(arr = [1, 2, 3, 4, 5],target = 9) == -1
    assert candidate(arr = [3, 2, 2, 4, 3],target = 3) == 2
    assert candidate(arr = [5, 5, 4, 4, 5],target = 9) == 4
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 4) == 4
    assert candidate(arr = [1000, 1000, 1000],target = 2000) == -1
    assert candidate(arr = [7, 3, 4, 7],target = 7) == 2
    assert candidate(arr = [1000, 1000, 1000, 1000, 1000],target = 2000) == 4
    assert candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3],target = 3) == 2
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 3) == 4
    assert candidate(arr = [1000, 1000, 1000, 1000, 1000],target = 5000) == -1
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
    assert candidate(arr = [1, 2, 3, 4, 5],target = 10) == -1
    assert candidate(arr = [10, 20, 30, 40, 50],target = 60) == -1
    assert candidate(arr = [1, 4, 4, 4, 4, 4, 4, 4, 4, 1],target = 8) == 4
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
    assert candidate(arr = [4, 3, 2, 6, 2, 3, 4],target = 6) == -1
    assert candidate(arr = [10, 20, 30, 40, 50],target = 90) == -1
    assert candidate(arr = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1],target = 1000) == 4
    assert candidate(arr = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],target = 50) == 4
    assert candidate(arr = [3, 1, 2, 4, 3, 2, 1, 3, 4, 2, 1, 3, 5, 2, 1, 3, 4, 2, 1, 3],target = 6) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 30) == 4
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 15) == 3
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 500) == -1
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 300) == 8
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 100) == 13
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 20) == 8
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == -1
    assert candidate(arr = [1, 3, 2, 1, 5, 2, 3, 1, 4, 2, 3, 1, 5, 2, 3, 1, 4, 2, 3, 1],target = 6) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == 3
    assert candidate(arr = [1, 4, 2, 3, 5, 7, 9, 11, 13, 15],target = 15) == 4
    assert candidate(arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8, 6],target = 15) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 4
    assert candidate(arr = [1, 4, 4, 1, 1, 2, 3, 5, 3, 2, 3, 4, 1],target = 8) == 4
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 30) == 6
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 20
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 20) == 8
    assert candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50],target = 60) == 4
    assert candidate(arr = [9, 1, 2, 3, 9, 4, 5, 9, 6, 7, 8, 9],target = 9) == 2
    assert candidate(arr = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 6) == 6
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
    assert candidate(arr = [5, 2, 3, 4, 1, 5, 2, 3, 4, 1, 5, 2, 3, 4, 1, 5, 2, 3, 4, 1],target = 10) == 6
    assert candidate(arr = [5, 1, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3],target = 9) == -1
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 5
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 4
    assert candidate(arr = [7, 8, 3, 4, 7, 6, 5, 4, 3, 2, 1],target = 15) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == -1
    assert candidate(arr = [7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1, 2, 1, 3, 1, 7, 1, 3, 1],target = 10) == 10
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
    assert candidate(arr = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 21) == 5
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],target = 3000) == 8
    assert candidate(arr = [1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3, 5, 2, 3, 1, 4, 2, 3],target = 8) == 4
    assert candidate(arr = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],target = 600) == 5
    assert candidate(arr = [2, 3, 2, 2, 3, 3, 2, 2, 2, 3],target = 6) == 5
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 5
    assert candidate(arr = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300],target = 600) == 6
    assert candidate(arr = [5, 1, 3, 5, 2, 4, 8, 6, 3, 7],target = 10) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 8
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 4
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 5
    assert candidate(arr = [3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3, 3, 2, 2, 4, 3],target = 5) == 4
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 10
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 400) == -1
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 40
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == -1
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 20) == 6
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 4
    assert candidate(arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8],target = 15) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],target = 3) == 3
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 4) == 6
    assert candidate(arr = [100, 200, 100, 300, 200, 400, 300, 500, 400, 600],target = 300) == 2
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 4
    assert candidate(arr = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500],target = 1000) == 8


