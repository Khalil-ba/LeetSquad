def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 1, 4, 1, 3],indexDiff = 5,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 1, 4, 1, 3],indexDiff = 5,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10],indexDiff = 3,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10],indexDiff = 3,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 1,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 1,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 3, 1, 5],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 3, 1, 5],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1],indexDiff = 3,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1],indexDiff = 3,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483647],indexDiff = 1,valueDiff = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483647],indexDiff = 1,valueDiff = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 1, 0, 1],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 1, 0, 1],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 2],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 2],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],indexDiff = 2,valueDiff = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],indexDiff = 2,valueDiff = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDiff = 5,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDiff = 5,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 3,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 3,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 4,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 4,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 8,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 8,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 10,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 10,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 5,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 5,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],indexDiff = 9,valueDiff = 3000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],indexDiff = 9,valueDiff = 3000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 8,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 8,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000, -999999999, 999999999, -1000000001, 1000000001],indexDiff = 5,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000, -999999999, 999999999, -1000000001, 1000000001],indexDiff = 5,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],indexDiff = 5,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],indexDiff = 5,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 1,valueDiff = 19) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 1,valueDiff = 19) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],indexDiff = 5,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],indexDiff = 5,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDiff = 10,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDiff = 10,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 3,valueDiff = 2000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 3,valueDiff = 2000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 10,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 10,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],indexDiff = 10,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],indexDiff = 10,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 4,valueDiff = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 4,valueDiff = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 10,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 10,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDiff = 7,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDiff = 7,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 3,valueDiff = 2000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 3,valueDiff = 2000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDiff = 19,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDiff = 19,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 2,valueDiff = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 2,valueDiff = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 10,valueDiff = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 10,valueDiff = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 20,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 20,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 10000,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 10000,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 7,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 7,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],indexDiff = 3,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],indexDiff = 3,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000],indexDiff = 10,valueDiff = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000],indexDiff = 10,valueDiff = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 50) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 50) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 2,valueDiff = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 2,valueDiff = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 5,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 5,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69],indexDiff = 6,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69],indexDiff = 6,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 150) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 150) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002],indexDiff = 4,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002],indexDiff = 4,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 7,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 7,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDiff = 15,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDiff = 15,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1000000000, -1000000000, 1000000000, 0, -1000000000, 1000000000, 0, -1000000000, 1000000000],indexDiff = 4,valueDiff = 500000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1000000000, -1000000000, 1000000000, 0, -1000000000, 1000000000, 0, -1000000000, 1000000000],indexDiff = 4,valueDiff = 500000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 20,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 20,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 25,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 25,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 5,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 5,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, 0],indexDiff = 4,valueDiff = 2000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, 0],indexDiff = 4,valueDiff = 2000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDiff = 10,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDiff = 10,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 5, 9, 10, 7, 6, 4, 2],indexDiff = 5,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 5, 9, 10, 7, 6, 4, 2],indexDiff = 5,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 1000000001, 3, 1000000002, 4, 1000000003],indexDiff = 7,valueDiff = 999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 1000000001, 3, 1000000002, 4, 1000000003],indexDiff = 7,valueDiff = 999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],indexDiff = 12,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],indexDiff = 12,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 2147483646, -2147483647],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 2147483646, -2147483647],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9],indexDiff = 4,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9],indexDiff = 4,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 15,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 15,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 10,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 10,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],indexDiff = 10,valueDiff = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],indexDiff = 10,valueDiff = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],indexDiff = 3,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],indexDiff = 3,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 19,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 19,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 5,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 5,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 20,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 20,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1000000000, 0, 1000000000, 0],indexDiff = 2,valueDiff = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1000000000, 0, 1000000000, 0],indexDiff = 2,valueDiff = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],indexDiff = 6,valueDiff = 999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],indexDiff = 6,valueDiff = 999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 1, 0, 1, 10, 100, 1000, 10000],indexDiff = 9,valueDiff = 9900) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 1, 0, 1, 10, 100, 1000, 10000],indexDiff = 9,valueDiff = 9900) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 5,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 5,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 8, 12, 15, 20, 22, 25, 28, 30],indexDiff = 4,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 8, 12, 15, 20, 22, 25, 28, 30],indexDiff = 4,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 5,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 5,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],indexDiff = 10,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],indexDiff = 10,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, -1000000000, 2, 1000000000, -1000000000],indexDiff = 5,valueDiff = 1999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, -1000000000, 2, 1000000000, -1000000000],indexDiff = 5,valueDiff = 1999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],indexDiff = 10,valueDiff = 999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],indexDiff = 10,valueDiff = 999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 100,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 100,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 6,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 6,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 10,valueDiff = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 10,valueDiff = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 5,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 5,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 10,valueDiff = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 10,valueDiff = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996, -999999995, -999999994, -999999993, -999999992, -999999991],indexDiff = 10,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996, -999999995, -999999994, -999999993, -999999992, -999999991],indexDiff = 10,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 5,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 5,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2147483647, -2147483648, 2147483647, -1, 2147483647, -2147483648, 2147483647, -1, 2147483647],indexDiff = 3,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2147483647, -2147483648, 2147483647, -1, 2147483647, -2147483648, 2147483647, -1, 2147483647],indexDiff = 3,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 3,valueDiff = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 3,valueDiff = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 2,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 2,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -1, 2147483647, -1],indexDiff = 1,valueDiff = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -1, 2147483647, -1],indexDiff = 1,valueDiff = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],indexDiff = 1,valueDiff = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],indexDiff = 1,valueDiff = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10, 100, 1000],indexDiff = 2,valueDiff = 899) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10, 100, 1000],indexDiff = 2,valueDiff = 899) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 1],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 1],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 5,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 5,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 5,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 5,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 10,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 10,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -3, -2, 0, -4, -2, -2, -2, -2, -2, -2, -2, -2],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -3, -2, 0, -4, -2, -2, -2, -2, -2, -2, -2, -2],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 8,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 8,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14],indexDiff = 1,valueDiff = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14],indexDiff = 1,valueDiff = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 5,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 5,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 9, 8, 7, 9, 3, 1],indexDiff = 2,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 9, 8, 7, 9, 3, 1],indexDiff = 2,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 23],indexDiff = 4,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 23],indexDiff = 4,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 23, 4, 25, 36, 7, 45, 8, 9, 45],indexDiff = 2,valueDiff = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 23, 4, 25, 36, 7, 45, 8, 9, 45],indexDiff = 2,valueDiff = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 2, 0, 4, 2, 2],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 2, 0, 4, 2, 2],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 3,valueDiff = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 3,valueDiff = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483647],indexDiff = 1,valueDiff = 4294967294) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483647],indexDiff = 1,valueDiff = 4294967294) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 1],indexDiff = 1,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 1],indexDiff = 1,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 8,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 8,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 9],indexDiff = 1,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 9],indexDiff = 1,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],indexDiff = 1,valueDiff = 4294967295) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],indexDiff = 1,valueDiff = 4294967295) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 7,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 7,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 5, 5, 1, 2, 5],indexDiff = 2,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 5, 5, 1, 2, 5],indexDiff = 2,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000],indexDiff = 3,valueDiff = 5000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000],indexDiff = 3,valueDiff = 5000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 2, 2, 5, 3, 9, 8, 2, 8],indexDiff = 4,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 2, 2, 5, 3, 9, 8, 2, 8],indexDiff = 4,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 1],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 1],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10, 20, 30, 40, 50],indexDiff = 3,valueDiff = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10, 20, 30, 40, 50],indexDiff = 3,valueDiff = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 9,valueDiff = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 9,valueDiff = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1],indexDiff = 3,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1],indexDiff = 3,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2147483647],indexDiff = 1,valueDiff = 2147483647) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2147483647],indexDiff = 1,valueDiff = 2147483647) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 3, 6, 5, 10, 12, 8],indexDiff = 5,valueDiff = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 3, 6, 5, 10, 12, 8],indexDiff = 5,valueDiff = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1],indexDiff = 1,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1],indexDiff = 1,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 3, 6, 5, 10, 12, 8],indexDiff = 5,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 3, 6, 5, 10, 12, 8],indexDiff = 5,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 999999999, 999999999, 999999999],indexDiff = 3,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 999999999, 999999999, 999999999],indexDiff = 3,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2],indexDiff = 0,valueDiff = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2],indexDiff = 0,valueDiff = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 5, 0, 1, 7, 9],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 5, 0, 1, 7, 9],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 1],indexDiff = 1,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 1],indexDiff = 1,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 10, 1000, 100, 10],indexDiff = 1,valueDiff = 90) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 10, 1000, 100, 10],indexDiff = 1,valueDiff = 90) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000, 100000],indexDiff = 4,valueDiff = 90000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000, 100000],indexDiff = 4,valueDiff = 90000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 6, 11, 7, 10, 3, 4, 7, 13, 1, 3, 15, 5],indexDiff = 2,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 6, 11, 7, 10, 3, 4, 7, 13, 1, 3, 15, 5],indexDiff = 2,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 0, -2, 2],indexDiff = 2,valueDiff = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 0, -2, 2],indexDiff = 2,valueDiff = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1],indexDiff = 1,valueDiff = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1],indexDiff = 1,valueDiff = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 11,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 11,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 2],indexDiff = 3,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 2],indexDiff = 3,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 4,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 4,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],indexDiff = 4,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],indexDiff = 4,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 21],indexDiff = 2,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 21],indexDiff = 2,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2147483647, -1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2147483647, -1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 1,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 1,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 5,valueDiff = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 5,valueDiff = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 2000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 2000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000],indexDiff = 0,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000],indexDiff = 0,valueDiff = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],indexDiff = 7,valueDiff = 9999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],indexDiff = 7,valueDiff = 9999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 3,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 3,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 5, 0, 1, 9, 3],indexDiff = 3,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 5, 0, 1, 9, 3],indexDiff = 3,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 2, 0, 14, 1, 13],indexDiff = 5,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 2, 0, 14, 1, 13],indexDiff = 5,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10],indexDiff = 1,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10],indexDiff = 1,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 1,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 1,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 21233, 15334453, 123345],indexDiff = 3,valueDiff = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 21233, 15334453, 123345],indexDiff = 3,valueDiff = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 2,valueDiff = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 2,valueDiff = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000, 100000],indexDiff = 5,valueDiff = 90000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000, 100000],indexDiff = 5,valueDiff = 90000) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 5, 0, 7, 9],indexDiff = 1,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 5, 0, 7, 9],indexDiff = 1,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 5, 0, 1, 9, 3],indexDiff = 2,valueDiff = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 5, 0, 1, 9, 3],indexDiff = 2,valueDiff = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2],indexDiff = 1,valueDiff = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2],indexDiff = 1,valueDiff = 0) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 1, 4, 1, 3],indexDiff = 5,valueDiff = 2) == True
    assert candidate(nums = [10, 10, 10, 10, 10, 10],indexDiff = 3,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 1,valueDiff = 3) == True
    assert candidate(nums = [2, 1, 2, 3, 1, 5],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 1],indexDiff = 3,valueDiff = 0) == True
    assert candidate(nums = [2147483647, -2147483647],indexDiff = 1,valueDiff = 2147483647) == False
    assert candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 3) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 5) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 1, 0, 1],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 2) == True
    assert candidate(nums = [10, 10, 10, 10],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [-1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False
    assert candidate(nums = [4, 1, 2],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],indexDiff = 2,valueDiff = 20) == True
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDiff = 5,valueDiff = 5) == True
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 3,valueDiff = 0) == True
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 4,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 8,valueDiff = 4) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 1,valueDiff = 0) == False
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 10,valueDiff = 10) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 5,valueDiff = 10) == True
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],indexDiff = 9,valueDiff = 3000000) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 0) == False
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 8,valueDiff = 1) == True
    assert candidate(nums = [-1000000000, 1000000000, -999999999, 999999999, -1000000001, 1000000001],indexDiff = 5,valueDiff = 1) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],indexDiff = 5,valueDiff = 4) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 1,valueDiff = 19) == True
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],indexDiff = 5,valueDiff = 10) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDiff = 10,valueDiff = 10) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 3,valueDiff = 2000000000) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 10,valueDiff = 0) == False
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],indexDiff = 10,valueDiff = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 1) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 4,valueDiff = 25) == True
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 10,valueDiff = 5) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDiff = 7,valueDiff = 5) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 3,valueDiff = 2000000000) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 5) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDiff = 19,valueDiff = 10) == True
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 2,valueDiff = 9) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 10,valueDiff = 9) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 20,valueDiff = 0) == False
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 1) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 10000,valueDiff = 0) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 7,valueDiff = 3) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],indexDiff = 3,valueDiff = 1) == True
    assert candidate(nums = [0, 1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000],indexDiff = 10,valueDiff = 1000000000) == True
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 50) == False
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 2,valueDiff = 8) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 5,valueDiff = 0) == True
    assert candidate(nums = [1, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69],indexDiff = 6,valueDiff = 5) == True
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 150) == True
    assert candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002],indexDiff = 4,valueDiff = 2) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 7,valueDiff = 4) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDiff = 15,valueDiff = 5) == True
    assert candidate(nums = [0, 1000000000, -1000000000, 1000000000, 0, -1000000000, 1000000000, 0, -1000000000, 1000000000],indexDiff = 4,valueDiff = 500000000) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 20,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 5) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 25,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 5,valueDiff = 4) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 2) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, 0],indexDiff = 4,valueDiff = 2000000000) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDiff = 10,valueDiff = 5) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [1, 3, 1, 5, 9, 10, 7, 6, 4, 2],indexDiff = 5,valueDiff = 3) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDiff = 5,valueDiff = 100) == True
    assert candidate(nums = [1, 1000000000, 2, 1000000001, 3, 1000000002, 4, 1000000003],indexDiff = 7,valueDiff = 999999999) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],indexDiff = 12,valueDiff = 5) == True
    assert candidate(nums = [2147483647, -2147483648, 2147483646, -2147483647],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9],indexDiff = 4,valueDiff = 3) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 15,valueDiff = 10) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 10,valueDiff = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 4) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],indexDiff = 10,valueDiff = 15) == True
    assert candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],indexDiff = 3,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 19,valueDiff = 1) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == False
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 5,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 20,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 1) == True
    assert candidate(nums = [0, 1000000000, 0, 1000000000, 0],indexDiff = 2,valueDiff = 1000000000) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],indexDiff = 6,valueDiff = 999999999) == True
    assert candidate(nums = [1000, 100, 10, 1, 0, 1, 10, 100, 1000, 10000],indexDiff = 9,valueDiff = 9900) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 2) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 5,valueDiff = 0) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [1, 3, 6, 8, 12, 15, 20, 22, 25, 28, 30],indexDiff = 4,valueDiff = 3) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 5,valueDiff = 4) == True
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],indexDiff = 10,valueDiff = 0) == True
    assert candidate(nums = [1, 1000000000, -1000000000, 2, 1000000000, -1000000000],indexDiff = 5,valueDiff = 1999999999) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],indexDiff = 10,valueDiff = 999999999) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 100,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 4) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 6,valueDiff = 4) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 10,valueDiff = 9) == True
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],indexDiff = 5,valueDiff = 0) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 10,valueDiff = 15) == True
    assert candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996, -999999995, -999999994, -999999993, -999999992, -999999991],indexDiff = 10,valueDiff = 0) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDiff = 5,valueDiff = 5) == True
    assert candidate(nums = [-1, 2147483647, -2147483648, 2147483647, -1, 2147483647, -2147483648, 2147483647, -1, 2147483647],indexDiff = 3,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 0) == True
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],indexDiff = 3,valueDiff = 9) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 1) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 3) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 10,valueDiff = 0) == True
    assert candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 2,valueDiff = 3) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 1) == True
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [2, 1, 2, 1],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [2147483647, -1, 2147483647, -1],indexDiff = 1,valueDiff = 2147483647) == False
    assert candidate(nums = [1],indexDiff = 1,valueDiff = 1) == False
    assert candidate(nums = [10, 100, 1000, 10, 100, 1000],indexDiff = 2,valueDiff = 899) == True
    assert candidate(nums = [1, 0, 1, 1],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 5,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 5,valueDiff = 10) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 1,valueDiff = 0) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 5,valueDiff = 0) == False
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 10,valueDiff = 0) == True
    assert candidate(nums = [-1, -1, -1, -3, -2, 0, -4, -2, -2, -2, -2, -2, -2, -2, -2],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 8,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 1, 2],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14],indexDiff = 1,valueDiff = 1) == False
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 5,valueDiff = 4) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1000000000) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 9, 8, 7, 9, 3, 1],indexDiff = 2,valueDiff = 3) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 23],indexDiff = 4,valueDiff = 1) == True
    assert candidate(nums = [8, 2, 23, 4, 25, 36, 7, 45, 8, 9, 45],indexDiff = 2,valueDiff = 5) == True
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 0) == False
    assert candidate(nums = [8, 2, 4, 2, 0, 2, 0, 4, 2, 2],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [5, 4, 3, 2, 1],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDiff = 3,valueDiff = 15) == True
    assert candidate(nums = [2147483647, -2147483647],indexDiff = 1,valueDiff = 4294967294) == True
    assert candidate(nums = [0, 1, 1, 1],indexDiff = 1,valueDiff = 2) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1999999999) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 8,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 9],indexDiff = 1,valueDiff = 2) == True
    assert candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],indexDiff = 1,valueDiff = 4294967295) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 7,valueDiff = 2) == True
    assert candidate(nums = [10, 10, 10, 10, 10],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 1, 2, 5, 5, 1, 2, 5],indexDiff = 2,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 4,valueDiff = 4) == True
    assert candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 3) == False
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 1999999999) == True
    assert candidate(nums = [10, 100, 1000, 10000],indexDiff = 3,valueDiff = 5000) == True
    assert candidate(nums = [8, 2, 2, 2, 5, 3, 9, 8, 2, 8],indexDiff = 4,valueDiff = 2) == True
    assert candidate(nums = [1, 0, 1, 1],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 1,valueDiff = 0) == False
    assert candidate(nums = [0, 10, 20, 30, 40, 50],indexDiff = 3,valueDiff = 10) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],indexDiff = 4,valueDiff = 2) == True
    assert candidate(nums = [0, 0, 0, 0, 0],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 9,valueDiff = 9) == True
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [1, 2, 3, 1],indexDiff = 3,valueDiff = 0) == True
    assert candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [0, 2147483647],indexDiff = 1,valueDiff = 2147483647) == True
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 4,valueDiff = 2) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [7, 1, 3, 6, 5, 10, 12, 8],indexDiff = 5,valueDiff = 8) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1],indexDiff = 1,valueDiff = 2) == True
    assert candidate(nums = [7, 1, 3, 6, 5, 10, 12, 8],indexDiff = 5,valueDiff = 2) == True
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999],indexDiff = 3,valueDiff = 0) == True
    assert candidate(nums = [1, 2],indexDiff = 0,valueDiff = 1) == False
    assert candidate(nums = [1, 2, 1, 2, 1, 2],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [8, 2, 4, 5, 0, 1, 7, 9],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 3, 1, 3, 1, 3],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [1, 0, 1, 1],indexDiff = 1,valueDiff = 2) == True
    assert candidate(nums = [10, 100, 10, 1000, 100, 10],indexDiff = 1,valueDiff = 90) == True
    assert candidate(nums = [10, 100, 1000, 10000, 100000],indexDiff = 4,valueDiff = 90000) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1, 1, 10, 6, 11, 7, 10, 3, 4, 7, 13, 1, 3, 15, 5],indexDiff = 2,valueDiff = 3) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 1,valueDiff = 0) == False
    assert candidate(nums = [2, 0, -2, 2],indexDiff = 2,valueDiff = 1) == False
    assert candidate(nums = [2, 1, 2, 1],indexDiff = 1,valueDiff = 0) == False
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1],indexDiff = 1,valueDiff = 1) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 11,valueDiff = 0) == True
    assert candidate(nums = [1, 3, 1, 2],indexDiff = 3,valueDiff = 1) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 4,valueDiff = 3) == True
    assert candidate(nums = [1, 2, 3, 4, 5],indexDiff = 4,valueDiff = 3) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDiff = 10,valueDiff = 9) == True
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 21],indexDiff = 2,valueDiff = 1) == True
    assert candidate(nums = [-1, 2147483647, -1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False
    assert candidate(nums = [8, 7, 15, 1, 6, 1, 9, 15],indexDiff = 1,valueDiff = 3) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],indexDiff = 5,valueDiff = 4) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],indexDiff = 2,valueDiff = 2000000000) == True
    assert candidate(nums = [1000000000, 1000000000],indexDiff = 0,valueDiff = 0) == False
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],indexDiff = 7,valueDiff = 9999999) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDiff = 3,valueDiff = 0) == True
    assert candidate(nums = [8, 2, 4, 5, 0, 1, 9, 3],indexDiff = 3,valueDiff = 2) == True
    assert candidate(nums = [1, 5, 9, 1, 5, 9],indexDiff = 2,valueDiff = 2) == False
    assert candidate(nums = [-1, 2147483647],indexDiff = 1,valueDiff = 2147483647) == False
    assert candidate(nums = [8, 2, 4, 2, 0, 14, 1, 13],indexDiff = 5,valueDiff = 3) == True
    assert candidate(nums = [10, 10, 10, 10, 10, 10],indexDiff = 1,valueDiff = 0) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],indexDiff = 1,valueDiff = 1) == True
    assert candidate(nums = [0, 21233, 15334453, 123345],indexDiff = 3,valueDiff = 3) == False
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 3) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDiff = 2,valueDiff = 0) == True
    assert candidate(nums = [10, 100, 1000, 10000, 100000],indexDiff = 5,valueDiff = 90000) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 1) == True
    assert candidate(nums = [8, 2, 4, 5, 0, 7, 9],indexDiff = 1,valueDiff = 2) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDiff = 5,valueDiff = 2) == True
    assert candidate(nums = [8, 2, 4, 5, 0, 1, 9, 3],indexDiff = 2,valueDiff = 3) == True
    assert candidate(nums = [1, 2],indexDiff = 1,valueDiff = 0) == False


