def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4],k = 5) == [5, 3, 1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4],k = 5) == [5, 3, 1, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],k = 3) == [10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],k = 3) == [10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 2) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 2) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, 3, 4],k = 3) == [-1, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, 3, 4],k = 3) == [-1, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == [3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == [3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 3, 4],k = 3) == [5, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 3, 4],k = 3) == [5, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == [6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == [6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],k = 2) == [-1, -2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],k = 2) == [-1, -2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1],k = 3) == [-1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1],k = 3) == [-1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 4) == [200, 300, 400, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 4) == [200, 300, 400, 500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 1) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 1) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 3],k = 2) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 3],k = 2) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40],k = 2) == [-10, -20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40],k = 2) == [-10, -20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],k = 4) == [5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],k = 4) == [5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000, 0],k = 2) == [100000, 50000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000, 0],k = 2) == [100000, 50000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 200000, -200000],k = 2) == [100000, 200000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 200000, -200000],k = 2) == [100000, 200000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -2, 0, 5],k = 2) == [10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -2, 0, 5],k = 2) == [10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 4, 3],k = 3) == [5, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 4, 3],k = 3) == [5, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 3, 3],k = 2) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 3, 3],k = 2) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],k = 2) == [-2, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],k = 2) == [-2, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 15) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 15) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 7) == [50, 50, 50, 50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 7) == [50, 50, 50, 50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 3) == [-1, -2, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 3) == [-1, -2, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 4) == [300, 500, 700, 900]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 4) == [300, 500, 700, 900]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],k = 7) == [10, 20, 30, 40, 50, -10, -20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],k = 7) == [10, 20, 30, 40, 50, -10, -20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 7) == [-1, -2, -3, -4, -5, -6, -7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 7) == [-1, -2, -3, -4, -5, -6, -7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 6) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 6) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -50000, 100000, -50000, 100000],k = 3) == [100000, 100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -50000, 100000, -50000, 100000],k = 3) == [100000, 100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 5) == [10, 30, 50, 70, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 5) == [10, 30, 50, 70, 90]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 15) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 15) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 3) == [-1, -2, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 3) == [-1, -2, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 1) == [500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 1) == [500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],k = 5) == [10, 20, 30, 40, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],k = 5) == [10, 20, 30, 40, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],k = 7) == [70, 80, 90, 100, 110, 120, 130]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],k = 7) == [70, 80, 90, 100, 110, 120, 130]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, -20, 200, -30, 300, -40, 400, -50, 500, -60, 600, -70, 700, -80, 800],k = 8) == [100, 200, 300, 400, 500, 600, 700, 800]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, -20, 200, -30, 300, -40, 400, -50, 500, -60, 600, -70, 700, -80, 800],k = 8) == [100, 200, 300, 400, 500, 600, 700, 800]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == [10, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == [10, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 15) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 15) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 3) == [99999, 99998, 99997]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 3) == [99999, 99998, 99997]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 7) == [10, 9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 7) == [10, 9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, 2, -3, 4, -5, 6, -7, 8, -9],k = 5) == [10, 2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, 2, -3, 4, -5, 6, -7, 8, -9],k = 5) == [10, 2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90],k = 15) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90],k = 15) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 5) == [100, 200, 300, 400, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 5) == [100, 200, 300, 400, 500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 15) == [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -1, -2, -3, -4, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 15) == [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -1, -2, -3, -4, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == [-1, -2, -3, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == [-1, -2, -3, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300],k = 7) == [100, 300, 500, 700, 900, 1100, 1300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300],k = 7) == [100, 300, 500, 700, 900, 1100, 1300]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == [6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == [6, 6, 7, 7, 8, 8, 9, 9, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 4) == [50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 4) == [50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == [60, 70, 80, 90, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == [60, 70, 80, 90, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000, 0, 25000, -25000, 75000, -75000],k = 3) == [100000, 50000, 75000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000, 0, 25000, -25000, 75000, -75000],k = 3) == [100000, 50000, 75000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 10) == [7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 10) == [7, 6, 9, 8, 11, 10, 13, 12, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500],k = 3) == [-100, -200, -300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500],k = 3) == [-100, -200, -300]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 8) == [1000, 900, 800, 700, 600, 500, 400, 300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 8) == [1000, 900, 800, 700, 600, 500, 400, 300]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 5) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 5) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == [-10, -20, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == [-10, -20, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 10) == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 10) == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 6) == [1, -1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 6) == [1, -1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 6) == [9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 6) == [9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 20000, -20000, 30000, -30000, 40000, -40000],k = 4) == [10000, 20000, 30000, 40000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 20000, -20000, 30000, -30000, 40000, -40000],k = 4) == [10000, 20000, 30000, 40000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == [-1, -2, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == [-1, -2, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10],k = 5) == [9, 6, 7, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10],k = 5) == [9, 6, 7, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500],k = 10) == [300, 400, 500, 300, 400, 500, 200, 300, 400, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500],k = 10) == [300, 400, 500, 300, 400, 500, 200, 300, 400, 500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 20) == [21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 20) == [21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 6) == [25, 30, 35, 40, 45, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 6) == [25, 30, 35, 40, 45, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == [1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == [1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110],k = 5) == [-10, -20, -30, -40, -50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110],k = 5) == [-10, -20, -30, -40, -50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == [15, 14, 13, 12, 11, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == [15, 14, 13, 12, 11, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1],k = 10) == [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1],k = 10) == [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 8) == [1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 8) == [1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 100, 200],k = 3) == [-10, 100, 200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 100, 200],k = 3) == [-10, 100, 200]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 3, 1, 2, 4],k = 5) == [5, 3, 1, 2, 4]
    assert candidate(nums = [10, 10, 10, 10, 10],k = 3) == [10, 10, 10]
    assert candidate(nums = [0, 0, 0, 0],k = 2) == [0, 0]
    assert candidate(nums = [-1, -2, 3, 4],k = 3) == [-1, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == [3, 4, 5]
    assert candidate(nums = [5, 1, 2, 3, 4],k = 3) == [5, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == [6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == [1, 1, 1, 1, 1]
    assert candidate(nums = [-1, -2, -3, -4],k = 2) == [-1, -2]
    assert candidate(nums = [-1, -1, -1, -1, -1],k = 3) == [-1, -1, -1]
    assert candidate(nums = [100, 200, 300, 400, 500],k = 4) == [200, 300, 400, 500]
    assert candidate(nums = [1],k = 1) == [1]
    assert candidate(nums = [2, 1, 3, 3],k = 2) == [3, 3]
    assert candidate(nums = [-10, -20, -30, -40],k = 2) == [-10, -20]
    assert candidate(nums = [5, 4, 3, 2, 1],k = 4) == [5, 4, 3, 2]
    assert candidate(nums = [100000, -100000, 50000, -50000, 0],k = 2) == [100000, 50000]
    assert candidate(nums = [100000, -100000, 200000, -200000],k = 2) == [100000, 200000]
    assert candidate(nums = [10, -2, 0, 5],k = 2) == [10, 5]
    assert candidate(nums = [5, 1, 2, 4, 3],k = 3) == [5, 4, 3]
    assert candidate(nums = [3, 4, 3, 3],k = 2) == [4, 3]
    assert candidate(nums = [-5, -4, -3, -2, -1],k = 2) == [-2, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 15) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 7) == [50, 50, 50, 50, 50, 50, 50]
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 3) == [-1, -2, -3]
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 4) == [300, 500, 700, 900]
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],k = 7) == [10, 20, 30, 40, 50, -10, -20]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 7) == [-1, -2, -3, -4, -5, -6, -7]
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 6) == [0, 1, 2, 3, 4, 5]
    assert candidate(nums = [100000, -50000, 100000, -50000, 100000],k = 3) == [100000, 100000, 100000]
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 5) == [10, 30, 50, 70, 90]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 15) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 3) == [-1, -2, -3]
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1) == [500]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],k = 5) == [10, 20, 30, 40, 50]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],k = 7) == [70, 80, 90, 100, 110, 120, 130]
    assert candidate(nums = [-10, 100, -20, 200, -30, 300, -40, 400, -50, 500, -60, 600, -70, 700, -80, 800],k = 8) == [100, 200, 300, 400, 500, 600, 700, 800]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [10, -1, 2, 9, 3, 8, 4, 7, 5, 6],k = 5) == [10, 9, 8, 7, 6]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 15) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 3) == [99999, 99998, 99997]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == [100, 90, 80]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == [1, 2, 3, 4, 5]
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 7) == [10, 9, 8, 7, 6, 5, 4]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == [1, 1, 1]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [10, -1, 2, -3, 4, -5, 6, -7, 8, -9],k = 5) == [10, 2, 4, 6, 8]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90],k = 15) == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == [1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [9, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 5) == [100, 200, 300, 400, 500]
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 15) == [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -1, -2, -3, -4, -5]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == [-1, -2, -3, -4]
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300],k = 7) == [100, 300, 500, 700, 900, 1100, 1300]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == [6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 4) == [50, 50, 50, 50]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == [60, 70, 80, 90, 100]
    assert candidate(nums = [100000, -100000, 50000, -50000, 0, 25000, -25000, 75000, -75000],k = 3) == [100000, 50000, 75000]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 10) == [7, 6, 9, 8, 11, 10, 13, 12, 15, 14]
    assert candidate(nums = [-100, -200, -300, -400, -500],k = 3) == [-100, -200, -300]
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 8) == [1000, 900, 800, 700, 600, 500, 400, 300]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 5) == [1, 3, 5, 7, 9]
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == [-10, -20, -30]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 10) == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 6) == [1, -1, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 6) == [9, 8, 7, 6, 5, 4]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == [0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == [9, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert candidate(nums = [10000, -10000, 20000, -20000, 30000, -30000, 40000, -40000],k = 4) == [10000, 20000, 30000, 40000]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == [-1, -2, -3]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]
    assert candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10],k = 5) == [9, 6, 7, 8, 10]
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500],k = 10) == [300, 400, 500, 300, 400, 500, 200, 300, 400, 500]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 20) == [21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 6) == [25, 30, 35, 40, 45, 50]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == [0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == [1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110],k = 5) == [-10, -20, -30, -40, -50]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == [15, 14, 13, 12, 11, 10, 9, 8]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1],k = 10) == [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 8) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [-10, -20, -30, -40, -50, 100, 200],k = 3) == [-10, 100, 200]


