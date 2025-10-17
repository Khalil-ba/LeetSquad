def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 10, 1, 1, 10],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 10, 1, 1, 10],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 1, 2, 3],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 1, 2, 3],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 9, 3, 1],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 9, 3, 1],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 9],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 9],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 25, 30, 35, 40],k = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 25, 30, 35, 40],k = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 3) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 3) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 1, 8, 5, 2, 9, 4, 7, 10],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 1, 8, 5, 2, 9, 4, 7, 10],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 20, 25, 15, 30, 35, 40, 45, 50],k = 8) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 20, 25, 15, 30, 35, 40, 45, 50],k = 8) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 2, 9, 1, 10, 8, 6, 4],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 2, 9, 1, 10, 8, 6, 4],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 8, 4, 7, 3, 9, 5, 6, 1],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 8, 4, 7, 3, 9, 5, 6, 1],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 6) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 6) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 10) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 10) == 67: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 1, 100, 10, 1, 100, 10, 1, 100],k = 4) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 1, 100, 10, 1, 100, 10, 1, 100],k = 4) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 8) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 8) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 10, 1, 1, 10, 1, 1, 10],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 10, 1, 1, 10, 1, 1, 10],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 2) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 2) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 7) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 7) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 10) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 10) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 10, 2, 8, 14, 1, 11, 7, 6],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 10, 2, 8, 14, 1, 11, 7, 6],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 7, 5, 3, 0, 9],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 7, 5, 3, 0, 9],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 3, 9, 2, 7, 4, 6, 1, 5, 10],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 3, 9, 2, 7, 4, 6, 1, 5, 10],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 1, 2, 1, 5, 1, 4, 1],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 1, 2, 1, 5, 1, 4, 1],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 7, 8, 4, 5, 6, 9],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 7, 8, 4, 5, 6, 9],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 9, 4, 7, 3, 8, 5, 6, 1],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 9, 4, 7, 3, 8, 5, 6, 1],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3],k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3],k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 2, 5, 7, 1, 3, 8, 6, 4, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 2, 5, 7, 1, 3, 8, 6, 4, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 12, 34, 56, 78, 89, 67, 45, 23, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],k = 6) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 12, 34, 56, 78, 89, 67, 45, 23, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],k = 6) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 4, 3, 20, 15],k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 4, 3, 20, 15],k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 10) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 10) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 2, 8, 7, 2, 5, 9, 4, 10],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 2, 8, 7, 2, 5, 9, 4, 10],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 7, 12, 14, 11, 14, 13, 15, 10, 11, 13],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 7, 12, 14, 11, 14, 13, 15, 10, 11, 13],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 1000000000, 500000000, 1000000000, 500000000, 1000000000],k = 3) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 1000000000, 500000000, 1000000000, 500000000, 1000000000],k = 3) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 10, 20, 30, 400, 500, 600, 1000],k = 5) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 10, 20, 30, 400, 500, 600, 1000],k = 5) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 7, 6, 4, 8, 9, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 7, 6, 4, 8, 9, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 1, 7, 3, 8, 5, 2, 6, 0],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 1, 7, 3, 8, 5, 2, 6, 0],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 7, 1, 3, 8, 6, 4, 2, 10, 1, 11, 13, 12, 14, 15, 16, 17, 18, 19],k = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 7, 1, 3, 8, 6, 4, 2, 10, 1, 11, 13, 12, 14, 15, 16, 17, 18, 19],k = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 5, 3, 7, 11, 15, 13, 17, 19],k = 4) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 5, 3, 7, 11, 15, 13, 17, 19],k = 4) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 20, 10, 5, 1, 25, 30, 40, 50, 60],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 20, 10, 5, 1, 25, 30, 40, 50, 60],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 100, 3, 4, 100, 5, 6, 100, 7, 8, 100, 9, 10, 100],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 100, 3, 4, 100, 5, 6, 100, 7, 8, 100, 9, 10, 100],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 10, 25, 60, 20, 30, 70, 5, 80, 1],k = 6) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 10, 25, 60, 20, 30, 70, 5, 80, 1],k = 6) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 7, 8, 6, 9, 4, 10],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 7, 8, 6, 9, 4, 10],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 4) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 4) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 1, 6, 5, 3, 7, 10, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 1, 6, 5, 3, 7, 10, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9
    assert candidate(nums = [10, 1, 1, 10, 1, 1, 10],k = 3) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 5
    assert candidate(nums = [10, 20, 30, 40, 50],k = 1) == 10
    assert candidate(nums = [5, 3, 1, 1, 2, 3],k = 2) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 5
    assert candidate(nums = [2, 7, 9, 3, 1],k = 2) == 2
    assert candidate(nums = [2, 3, 5, 9],k = 2) == 5
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 4) == 2
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 15) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9
    assert candidate(nums = [10, 5, 15, 20, 25, 30, 35, 40],k = 4) == 35
    assert candidate(nums = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1],k = 5) == 1
    assert candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 3) == 250
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 2
    assert candidate(nums = [3, 6, 1, 8, 5, 2, 9, 4, 7, 10],k = 4) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 37
    assert candidate(nums = [10, 5, 20, 25, 15, 30, 35, 40, 45, 50],k = 8) == 51
    assert candidate(nums = [3, 5, 7, 2, 9, 1, 10, 8, 6, 4],k = 3) == 3
    assert candidate(nums = [10, 2, 8, 4, 7, 3, 9, 5, 6, 1],k = 4) == 4
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 3) == 1
    assert candidate(nums = [10, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],k = 6) == 29
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],k = 10) == 67
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 11
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 5) == 1
    assert candidate(nums = [100, 10, 1, 100, 10, 1, 100, 10, 1, 100],k = 4) == 100
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 8) == 29
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 5) == 1
    assert candidate(nums = [10, 1, 1, 10, 1, 1, 10, 1, 1, 10],k = 5) == 10
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 2) == 1000000000
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == 50
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 35
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 10) == 1
    assert candidate(nums = [8, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 7) == 56
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 10) == 38
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 5
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 13
    assert candidate(nums = [3, 5, 10, 2, 8, 14, 1, 11, 7, 6],k = 5) == 10
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 5) == 50
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 900
    assert candidate(nums = [8, 6, 7, 5, 3, 0, 9],k = 3) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 15) == 3
    assert candidate(nums = [3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 10],k = 4) == 3
    assert candidate(nums = [8, 3, 9, 2, 7, 4, 6, 1, 5, 10],k = 4) == 4
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 90
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 6) == 22
    assert candidate(nums = [1, 3, 1, 1, 2, 1, 5, 1, 4, 1],k = 4) == 1
    assert candidate(nums = [2, 3, 7, 8, 4, 5, 6, 9],k = 3) == 6
    assert candidate(nums = [10, 2, 9, 4, 7, 3, 8, 5, 6, 1],k = 3) == 3
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3],k = 8) == 3
    assert candidate(nums = [9, 2, 5, 7, 1, 3, 8, 6, 4, 10],k = 5) == 9
    assert candidate(nums = [23, 45, 12, 34, 56, 78, 89, 67, 45, 23, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],k = 6) == 20
    assert candidate(nums = [7, 10, 4, 3, 20, 15],k = 3) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 17
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 10) == 98
    assert candidate(nums = [2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 5) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 500
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [3, 6, 2, 8, 7, 2, 5, 9, 4, 10],k = 4) == 4
    assert candidate(nums = [3, 6, 7, 12, 14, 11, 14, 13, 15, 10, 11, 13],k = 4) == 11
    assert candidate(nums = [1000000000, 500000000, 1000000000, 500000000, 1000000000, 500000000, 1000000000],k = 3) == 500000000
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1],k = 5) == 1
    assert candidate(nums = [100, 200, 300, 10, 20, 30, 400, 500, 600, 1000],k = 5) == 600
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == 26
    assert candidate(nums = [1, 3, 2, 5, 7, 6, 4, 8, 9, 10],k = 5) == 9
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 5) == 1
    assert candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3],k = 4) == 3
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 5) == 1
    assert candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5],k = 3) == 3
    assert candidate(nums = [9, 4, 1, 7, 3, 8, 5, 2, 6, 0],k = 4) == 3
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 50
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 5) == 1
    assert candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9],k = 4) == 1
    assert candidate(nums = [5, 9, 7, 1, 3, 8, 6, 4, 2, 10, 1, 11, 13, 12, 14, 15, 16, 17, 18, 19],k = 6) == 7
    assert candidate(nums = [9, 1, 5, 3, 7, 11, 15, 13, 17, 19],k = 4) == 13
    assert candidate(nums = [15, 20, 10, 5, 1, 25, 30, 40, 50, 60],k = 5) == 50
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],k = 4) == 1
    assert candidate(nums = [15, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 80
    assert candidate(nums = [1, 2, 100, 3, 4, 100, 5, 6, 100, 7, 8, 100, 9, 10, 100],k = 5) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 19
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 10
    assert candidate(nums = [50, 10, 25, 60, 20, 30, 70, 5, 80, 1],k = 6) == 81
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == 5
    assert candidate(nums = [1, 3, 2, 5, 7, 8, 6, 9, 4, 10],k = 3) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 17
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 11
    assert candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],k = 10) == 1
    assert candidate(nums = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60],k = 3) == 10
    assert candidate(nums = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10],k = 5) == 5
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == 5
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 4) == 70
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 7) == 5
    assert candidate(nums = [8, 2, 4, 1, 6, 5, 3, 7, 10, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == 11


