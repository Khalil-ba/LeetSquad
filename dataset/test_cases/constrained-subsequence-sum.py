def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 7, -3, 5],k = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, -3, 5],k = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, -10, 5, 20],k = 2) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, -10, 5, 20],k = 2) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, 4, -2, 2, 1],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, 4, -2, 2, 1],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, 5],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, 5],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, -5, -10, -3, 7],k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, -5, -10, -3, 7],k = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 5, -2, 3],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 5, -2, 3],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -2, -10, -5, 20],k = 2) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -2, -10, -5, 20],k = 2) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 2) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 2) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70],k = 1) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70],k = 1) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 4) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 4) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 15) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 15) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -500, 200, -300, 400, -200, 600, -100, 700, -300],k = 5) == 2900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -500, 200, -300, 400, -200, 600, -100, 700, -300],k = 5) == 2900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 4) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 4) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -3, -5, -1, -6, -2, -4, -8, -9],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -3, -5, -1, -6, -2, -4, -8, -9],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981],k = 5) == 19810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981],k = 5) == 19810: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -2, 3, 5, -1, 2, 0, 8, -5, 10],k = 4) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -2, 3, 5, -1, 2, 0, 8, -5, 10],k = 4) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100],k = 2) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100],k = 2) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, 600, -700, 800, -900, 1000],k = 3) == 3300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, 600, -700, 800, -900, 1000],k = 3) == 3300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],k = 2) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],k = 2) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -4, 5, 6, -7, 8, 9, -10],k = 3) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -4, 5, 6, -7, 8, 9, -10],k = 3) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 7) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 7) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -2000, -3000, -4000, -5000, 5000, 4000, 3000, 2000, 1000],k = 4) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -2000, -3000, -4000, -5000, 5000, 4000, 3000, 2000, 1000],k = 4) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9],k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9],k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 6, 4, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 6, 4, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -300, 200, 50, -150, 400, 300],k = 3) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -300, 200, 50, -150, 400, 300],k = 3) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],k = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],k = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 5) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 5) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 8) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 8) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 2, -3, -4, 5, 6, -1, 2, 3, -10, 100, -200, 300],k = 4) == 418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 2, -3, -4, 5, 6, -1, 2, 3, -10, 100, -200, 300],k = 4) == 418: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 6) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 6) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 15) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 15) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, -5000, -4000, -3000, -2000, -1000],k = 5) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, -5000, -4000, -3000, -2000, -1000],k = 5) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 7) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 7) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 4) == 1045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 4) == 1045: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 600, 700, 800, 900, 1000],k = 7) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 600, 700, 800, 900, 1000],k = 7) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19],k = 9) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19],k = 9) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 200, -250, 300, -350, 400, -450, 500],k = 5) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 200, -250, 300, -350, 400, -450, 500],k = 5) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, 5, -1, 2, 4, -3, 7],k = 3) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, 5, -1, 2, 4, -3, 7],k = 3) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10],k = 6) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10],k = 6) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 5) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 5) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3, 5, -7, 8, -2, 6],k = 5) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3, 5, -7, 8, -2, 6],k = 5) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 20, 10, -10, -20, -50, -100, 30, 40],k = 4) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 20, 10, -10, -20, -50, -100, 30, 40],k = 4) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 2, -3, 4, -1, 5, -6, 7, -8, 9],k = 4) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 2, -3, 4, -1, 5, -6, 7, -8, 9],k = 4) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 7) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 7) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -2, -10, 5, 20, -30, 40, -50, 60, -70],k = 3) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -2, -10, 5, 20, -30, 40, -50, 60, -70],k = 3) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100],k = 7) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100],k = 7) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 5) == -91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 5) == -91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -6, 4, 5, -7, 6, 7, -8, 8, 9],k = 3) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -6, 4, 5, -7, 6, 7, -8, 8, 9],k = 3) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -100, 1000, -10000, 100000, -1000000, 10000000, -100000000, 1000000000],k = 2) == 1010101001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -100, 1000, -10000, 100000, -1000000, 10000000, -100000000, 1000000000],k = 2) == 1010101001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -2, 5, -1, 6, 2, -5, 10],k = 3) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -2, 5, -1, 6, 2, -5, 10],k = 3) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120],k = 6) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120],k = 6) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 4) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 4) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6, 3, -3, 1, -1],k = 6) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6, 3, -3, 1, -1],k = 6) == 197: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, -10, 4, 13, -5, 12, -3, 15, -10, 7, 8],k = 3) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, -10, 4, 13, -5, 12, -3, 15, -10, 7, 8],k = 3) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000],k = 3) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000],k = 3) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 5) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 5) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -1, -2, -3, -4, -5, 60, 70, 80, 90, 100],k = 10) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -1, -2, -3, -4, -5, 60, 70, 80, 90, 100],k = 10) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],k = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],k = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 4) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 4) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],k = 2) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],k = 2) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 7) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 7) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 3) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 3) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 20, -10, 5, 15, -3],k = 3) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 20, -10, 5, 15, -3],k = 3) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],k = 1) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],k = 1) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 3, -2, 5, -6, 4, 2, -3, 5, -4],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 3, -2, 5, -6, 4, 2, -3, 5, -4],k = 3) == 19: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 7, -3, 5],k = 1) == 14
    assert candidate(nums = [10, 2, -10, 5, 20],k = 2) == 37
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 15
    assert candidate(nums = [3, -1, 4, -2, 2, 1],k = 2) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 4) == -1
    assert candidate(nums = [5, -1, 5],k = 2) == 10
    assert candidate(nums = [-1, -2, -3],k = 1) == -1
    assert candidate(nums = [5, 4, 3, 2, 1],k = 5) == 15
    assert candidate(nums = [5, 3, -5, -10, -3, 7],k = 4) == 15
    assert candidate(nums = [1, -1, 5, -2, 3],k = 3) == 9
    assert candidate(nums = [10, -2, -10, -5, 20],k = 2) == 23
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 2) == 15
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 2) == 150
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 5) == -1
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70],k = 1) == -10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 4) == 150
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 10) == 55
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 15) == 5500
    assert candidate(nums = [1000, -500, 200, -300, 400, -200, 600, -100, 700, -300],k = 5) == 2900
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 4) == 50000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
    assert candidate(nums = [-10, -3, -5, -1, -6, -2, -4, -8, -9],k = 2) == -1
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981],k = 5) == 19810
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 2) == 8
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
    assert candidate(nums = [10, -2, 3, 5, -1, 2, 0, 8, -5, 10],k = 4) == 38
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100],k = 2) == 500
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550
    assert candidate(nums = [100, -200, 300, -400, 500, 600, -700, 800, -900, 1000],k = 3) == 3300
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000],k = 2) == 15000
    assert candidate(nums = [1, 2, 3, -4, 5, 6, -7, 8, 9, -10],k = 3) == 34
    assert candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 7) == 400
    assert candidate(nums = [-1000, -2000, -3000, -4000, -5000, 5000, 4000, 3000, 2000, 1000],k = 4) == 15000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9],k = 4) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 550
    assert candidate(nums = [5, 2, 3, 1, 6, 4, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 65
    assert candidate(nums = [100, -300, 200, 50, -150, 400, 300],k = 3) == 1050
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],k = 3) == 30
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 5) == 1500
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 8) == 400
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 1) == -1
    assert candidate(nums = [-10, 2, -3, -4, 5, 6, -1, 2, 3, -10, 100, -200, 300],k = 4) == 418
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 5) == 15
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 6) == 64
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 2) == 5
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 15) == 50
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, -5000, -4000, -3000, -2000, -1000],k = 5) == 15000
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 7) == 8000
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5],k = 5) == 50
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 4) == 1045
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 600, 700, 800, 900, 1000],k = 7) == 5500
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 50
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 2) == -1
    assert candidate(nums = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19],k = 9) == 90
    assert candidate(nums = [100, -50, 200, -250, 300, -350, 400, -450, 500],k = 5) == 1500
    assert candidate(nums = [1, -2, 3, 5, -1, 2, 4, -3, 7],k = 3) == 22
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10],k = 6) == 550
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == 55
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1) == 5500
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 5) == 105
    assert candidate(nums = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3, 5, -7, 8, -2, 6],k = 5) == 42
    assert candidate(nums = [100, 50, 20, 10, -10, -20, -50, -100, 30, 40],k = 4) == 240
    assert candidate(nums = [-10, 2, -3, 4, -1, 5, -6, 7, -8, 9],k = 4) == 27
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 7) == 325
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 2100
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 6
    assert candidate(nums = [10, -2, -10, 5, 20, -30, 40, -50, 60, -70],k = 3) == 135
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100],k = 7) == 550
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 5) == -91
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 3) == -1
    assert candidate(nums = [1, 2, 3, -6, 4, 5, -7, 6, 7, -8, 8, 9],k = 3) == 45
    assert candidate(nums = [1, -100, 1000, -10000, 100000, -1000000, 10000000, -100000000, 1000000000],k = 2) == 1010101001
    assert candidate(nums = [3, -2, 5, -1, 6, 2, -5, 10],k = 3) == 26
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120],k = 6) == 360
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 1) == 1
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 4) == 2500
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6, 3, -3, 1, -1],k = 6) == 197
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 5
    assert candidate(nums = [3, -1, -10, 4, 13, -5, 12, -3, 15, -10, 7, 8],k = 3) == 62
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000],k = 3) == 15000
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],k = 5) == 2500
    assert candidate(nums = [10, 20, 30, 40, 50, -1, -2, -3, -4, -5, 60, 70, 80, 90, 100],k = 10) == 550
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],k = 10) == 100
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 4) == -10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
    assert candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],k = 2) == -1000
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 7) == 64
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 3) == 55
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 4) == -1
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 120
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
    assert candidate(nums = [10, -5, 20, -10, 5, 15, -3],k = 3) == 50
    assert candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],k = 1) == -5
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [-1, 3, -2, 5, -6, 4, 2, -3, 5, -4],k = 3) == 19


