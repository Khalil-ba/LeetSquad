def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 5, 2, 6, 2],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 5, 2, 6, 2],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 7, 1, 9, 2, 10, 4, 11, 6],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 7, 1, 9, 2, 10, 4, 11, 6],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 5, 4, 3, 2, 1],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 5, 4, 3, 2, 1],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1],k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1],k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1],k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1],k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 2, 5, 3, 7, 101, 18],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 2, 5, 3, 7, 101, 18],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 4, 2, 6, 3, 5, 1, 8],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 4, 2, 6, 3, 5, 1, 8],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 2, 5, 3, 7, 101, 18],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 2, 5, 3, 7, 101, 18],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 4, 2, 3, 1, 5, 7, 8, 6, 10],k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 4, 2, 3, 1, 5, 7, 8, 6, 10],k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 5, 2, 6, 2],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 5, 2, 6, 2],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 9, 4, 6, 7, 2, 8, 10, 3, 11],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 9, 4, 6, 7, 2, 8, 10, 3, 11],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 2, 4, 6, 3, 5, 7, 4, 6, 8],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 2, 4, 6, 3, 5, 7, 4, 6, 8],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2, 11],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2, 11],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 10, 12, 14, 13, 15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28, 30, 32, 31, 33, 35, 34, 36, 38, 37, 39, 41, 40, 42, 44, 43, 45, 47, 46, 48, 50, 49],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 10, 12, 14, 13, 15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28, 30, 32, 31, 33, 35, 34, 36, 38, 37, 39, 41, 40, 42, 44, 43, 45, 47, 46, 48, 50, 49],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 15, 10, 20, 25, 20, 30, 35, 30, 40],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 15, 10, 20, 25, 20, 30, 35, 30, 40],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4],k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4],k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 20, 30, 10, 40, 60, 50, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 20, 30, 10, 40, 60, 50, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 8, 6, 9, 7, 10, 12, 11, 15, 13, 16, 18, 14, 19, 20],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 8, 6, 9, 7, 10, 12, 11, 15, 13, 16, 18, 14, 19, 20],k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70],k = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70],k = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 4, 2, 6, 3, 5, 1, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 4, 2, 6, 3, 5, 1, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 29) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 29) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9],k = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9],k = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 25, 40, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 25, 40, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 1, 11, 21, 31, 41, 51, 2, 12, 22, 32, 42, 52],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 1, 11, 21, 31, 41, 51, 2, 12, 22, 32, 42, 52],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 8, 6, 2, 7, 4, 9, 1],k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 8, 6, 2, 7, 4, 9, 1],k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450],k = 4) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [2, 2, 2, 2, 2],k = 1) == 0
    assert candidate(arr = [1, 5, 9, 13, 17],k = 4) == 0
    assert candidate(arr = [4, 1, 5, 2, 6, 2],k = 3) == 2
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 0
    assert candidate(arr = [5, 3, 7, 1, 9, 2, 10, 4, 11, 6],k = 2) == 1
    assert candidate(arr = [6, 5, 4, 3, 2, 1],k = 2) == 4
    assert candidate(arr = [5, 4, 3, 2, 1],k = 1) == 4
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 0
    assert candidate(arr = [9, 7, 5, 3, 1],k = 2) == 3
    assert candidate(arr = [1, 2, 3, 4, 5, 6],k = 2) == 0
    assert candidate(arr = [10, 9, 2, 5, 3, 7, 101, 18],k = 2) == 2
    assert candidate(arr = [5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(arr = [1, 3, 5, 7, 9],k = 2) == 0
    assert candidate(arr = [1, 2, 3, 4, 5],k = 1) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 5
    assert candidate(arr = [1, 2, 3, 4, 5],k = 5) == 0
    assert candidate(arr = [7, 4, 2, 6, 3, 5, 1, 8],k = 3) == 3
    assert candidate(arr = [10, 9, 2, 5, 3, 7, 101, 18],k = 3) == 2
    assert candidate(arr = [1, 1, 1, 1, 1, 1],k = 2) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
    assert candidate(arr = [2, 2, 2, 2, 2],k = 5) == 0
    assert candidate(arr = [9, 4, 2, 3, 1, 5, 7, 8, 6, 10],k = 1) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6],k = 1) == 0
    assert candidate(arr = [4, 1, 5, 2, 6, 2],k = 2) == 0
    assert candidate(arr = [1, 3, 5, 7, 9],k = 3) == 0
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 0
    assert candidate(arr = [1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(arr = [5, 9, 4, 6, 7, 2, 8, 10, 3, 11],k = 2) == 4
    assert candidate(arr = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 3
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 15
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(arr = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 20
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 0
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 2) == 9
    assert candidate(arr = [1, 3, 5, 2, 4, 6, 3, 5, 7, 4, 6, 8],k = 2) == 6
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 0
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1) == 9
    assert candidate(arr = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60],k = 2) == 0
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 16
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 0
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 26
    assert candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 2) == 0
    assert candidate(arr = [9, 7, 5, 3, 1, 10, 8, 6, 4, 2, 11],k = 5) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10],k = 5) == 7
    assert candidate(arr = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 10, 12, 14, 13, 15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28, 30, 32, 31, 33, 35, 34, 36, 38, 37, 39, 41, 40, 42, 44, 43, 45, 47, 46, 48, 50, 49],k = 3) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 4) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 0
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 10) == 5
    assert candidate(arr = [10, 15, 10, 20, 25, 20, 30, 35, 30, 40],k = 3) == 0
    assert candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4],k = 4) == 6
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == 0
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 5) == 4
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 7
    assert candidate(arr = [50, 20, 30, 10, 40, 60, 50, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 10) == 0
    assert candidate(arr = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 3) == 0
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 4) == 4
    assert candidate(arr = [5, 3, 8, 6, 9, 7, 10, 12, 11, 15, 13, 16, 18, 14, 19, 20],k = 3) == 1
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 0
    assert candidate(arr = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 5) == 0
    assert candidate(arr = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9],k = 3) == 3
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 5) == 0
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70],k = 10) == 21
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 7
    assert candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 27
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 0
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 0
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 3) == 0
    assert candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15],k = 3) == 0
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 0
    assert candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12],k = 2) == 0
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 18
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 0
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == 0
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57],k = 1) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 10) == 0
    assert candidate(arr = [7, 4, 2, 6, 3, 5, 1, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 3
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],k = 2) == 0
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 2) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0
    assert candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20],k = 3) == 0
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 0
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1) == 9
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 2) == 3
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 1) == 0
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 29) == 0
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 8
    assert candidate(arr = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9],k = 1) == 12
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 2) == 4
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 0
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15],k = 1) == 9
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 2) == 0
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 5) == 9
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 14
    assert candidate(arr = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 2
    assert candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1) == 9
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 10
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],k = 2) == 0
    assert candidate(arr = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11],k = 3) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 0
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 12
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 25
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 0
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 2) == 5
    assert candidate(arr = [10, 20, 30, 25, 40, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],k = 7) == 0
    assert candidate(arr = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],k = 2) == 0
    assert candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],k = 2) == 0
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 3) == 8
    assert candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 0
    assert candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 2) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 0
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 3) == 0
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(arr = [10, 20, 30, 40, 50, 1, 11, 21, 31, 41, 51, 2, 12, 22, 32, 42, 52],k = 5) == 10
    assert candidate(arr = [5, 3, 8, 6, 2, 7, 4, 9, 1],k = 2) == 3
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 0
    assert candidate(arr = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450],k = 4) == 0


