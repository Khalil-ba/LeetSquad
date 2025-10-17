def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2],k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2],k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 0, -2, -3, 1],k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 0, -2, -3, 1],k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 4, 5, 6],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 4, 5, 6],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7],k = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7],k = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 3, 1, 2, 3, -4],k = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 3, 1, 2, 3, -4],k = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 0, 3, -2],k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 0, 3, -2],k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 4) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 4) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104, -104, 208, -208, 312, -312, 416, -416, 520, -520],k = 104) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104, -104, 208, -208, 312, -312, 416, -416, 520, -520],k = 104) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 3) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 3) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 6) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 6) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 250) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 250) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10],k = 5) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10],k = 5) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 100) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 100) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 5, 1, 2, 4, 6],k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 5, 1, 2, 4, 6],k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, -9999, 9999, -9999, 9999, -9999],k = 10000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, -9999, 9999, -9999, 9999, -9999],k = 10000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 1, -1, -1, -1, 0, 1, 2],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 1, -1, -1, -1, 0, 1, 2],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 3) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 3) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 3, 2, 3, 1, 2, 3],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 3, 2, 3, 1, 2, 3],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 3) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 3) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, -1, -2, 3, 5, -7, 10, -12, 15, -18, 21, -24, 27, -30, 33, -36, 39, -42, 45, -48],k = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, -1, -2, 3, 5, -7, 10, -12, 15, -18, 21, -24, 27, -30, 33, -36, 39, -42, 45, -48],k = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0],k = 10) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0],k = 10) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 100) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 100) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -9999, -9998, -9997, -9996, -9995, -9994, -9993, -9992, -9991],k = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -9999, -9998, -9997, -9996, -9995, -9994, -9993, -9992, -9991],k = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 13) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 13) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 1000) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 1000) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 4) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 4) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 13) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 13) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000],k = 10000) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000],k = 10000) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90],k = 15) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90],k = 15) == 78: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, -9999, 9999, -9999, 9999, -9999, 9999, -9999],k = 9999) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, -9999, 9999, -9999, 9999, -9999, 9999, -9999],k = 9999) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10],k = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10],k = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -5, 6, 1, -7, 8, 9, 10, -11, 12],k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -5, 6, 1, -7, 8, 9, 10, -11, 12],k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, -2, 2, 1, 3],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, -2, 2, 1, 3],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4],k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4],k = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 2000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 2000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40],k = 10) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40],k = 10) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10000) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10000) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],k = 6) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],k = 6) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10],k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10],k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0],k = 4) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0],k = 4) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, -1000, -2000, -3000],k = 1000) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, -1000, -2000, -3000],k = 1000) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000],k = 1000) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000],k = 1000) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [104, -104, 104, -104, 104, -104, 104, -104, 104, -104],k = 104) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [104, -104, 104, -104, 104, -104, 104, -104, 104, -104],k = 104) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, 0, 5, 10, 15, 20],k = 5) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, 0, 5, 10, 15, 20],k = 5) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2],k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2],k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144],k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144],k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 11) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 11) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 10000) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 10000) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -6, 1, 2, 3, 4, 5],k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -6, 1, 2, 3, 4, 5],k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -2, 2, -4, 6, 5, -1, 3, -3, 4],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -2, 2, -4, 6, 5, -1, 3, -3, 4],k = 5) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 2, 2, 2, 2],k = 6) == 3
    assert candidate(nums = [0, 0, 0, 0],k = 2) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 25
    assert candidate(nums = [-1, 2, -3, 4, -5],k = 2) == 6
    assert candidate(nums = [4, 5, 0, -2, -3, 1],k = 5) == 7
    assert candidate(nums = [2, 2, 2, 2, 2],k = 2) == 15
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == 27
    assert candidate(nums = [0, 0, 0, 0, 0],k = 1) == 15
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 7
    assert candidate(nums = [0, 0, 0, 0, 0],k = 2) == 15
    assert candidate(nums = [-1, -2, -3, 4, 5, 6],k = 2) == 9
    assert candidate(nums = [7, 7, 7, 7, 7, 7],k = 7) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 17
    assert candidate(nums = [-1, 2, -3, 4, -5, 6],k = 4) == 3
    assert candidate(nums = [-1, -2, -3, 3, 1, 2, 3, -4],k = 3) == 16
    assert candidate(nums = [1, -1, 2, -2, 3, -3],k = 2) == 11
    assert candidate(nums = [0, 0, 0, 0],k = 1) == 10
    assert candidate(nums = [1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(nums = [5],k = 9) == 0
    assert candidate(nums = [10, 5, 0, 3, -2],k = 7) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],k = 10) == 15
    assert candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 3
    assert candidate(nums = [-10, -5, 0, 5, 10],k = 5) == 15
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 4) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27
    assert candidate(nums = [104, -104, 208, -208, 312, -312, 416, -416, 520, -520],k = 104) == 55
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 3) == 34
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 6) == 14
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 55
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 250) == 17
    assert candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10],k = 5) == 36
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 11) == 5
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 100) == 55
    assert candidate(nums = [7, 3, 5, 1, 2, 4, 6],k = 7) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 25
    assert candidate(nums = [9999, -9999, 9999, -9999, 9999, -9999],k = 10000) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 55
    assert candidate(nums = [10, 20, 30, 40, 50],k = 10) == 15
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 55
    assert candidate(nums = [1, 0, 2, 1, -1, -1, -1, 0, 1, 2],k = 4) == 11
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 3) == 64
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 35
    assert candidate(nums = [3, 1, 2, 5, 3, 2, 3, 1, 2, 3],k = 5) == 9
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 3) == 28
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 11) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 34
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 210
    assert candidate(nums = [9, -1, -2, 3, 5, -7, 10, -12, 15, -18, 21, -24, 27, -30, 33, -36, 39, -42, 45, -48],k = 15) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 10
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 4) == 14
    assert candidate(nums = [-5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0],k = 10) == 225
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 100) == 120
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 21
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2) == 120
    assert candidate(nums = [-10000, -9999, -9998, -9997, -9996, -9995, -9994, -9993, -9992, -9991],k = 1000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 13) == 12
    assert candidate(nums = [10, 20, 30, 40, 50],k = 15) == 7
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 1000) == 55
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 4) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 13) == 22
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 7
    assert candidate(nums = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000],k = 10000) == 55
    assert candidate(nums = [15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90],k = 15) == 78
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 27
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 63
    assert candidate(nums = [9999, -9999, 9999, -9999, 9999, -9999, 9999, -9999],k = 9999) == 36
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2) == 106
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10],k = 5) == 45
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5000) == 7
    assert candidate(nums = [2, 3, -5, 6, 1, -7, 8, 9, 10, -11, 12],k = 7) == 12
    assert candidate(nums = [-3, -1, -2, 2, 1, 3],k = 5) == 3
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4],k = 4) == 15
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 2000) == 25
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40],k = 10) == 28
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10000) == 55
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],k = 6) == 72
    assert candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10],k = 10) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0],k = 4) == 28
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 120
    assert candidate(nums = [1000, 2000, 3000, -1000, -2000, -3000],k = 1000) == 21
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == 27
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 48
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 11) == 5
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000],k = 1000) == 36
    assert candidate(nums = [104, -104, 104, -104, 104, -104, 104, -104, 104, -104],k = 104) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 55
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 225
    assert candidate(nums = [-10, -20, -30, 0, 5, 10, 15, 20],k = 5) == 36
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 210
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 55
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 3) == 55
    assert candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2],k = 4) == 16
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 25
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27
    assert candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144],k = 7) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 11) == 28
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 10000) == 15
    assert candidate(nums = [1, 2, 3, -6, 1, 2, 3, 4, 5],k = 7) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 27
    assert candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5],k = 5) == 55
    assert candidate(nums = [2, -2, 2, -4, 6, 5, -1, 3, -3, 4],k = 5) == 8


