def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],multipliers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],multipliers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [10, 9, 8, 7, 6]) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [10, 9, 8, 7, 6]) == 330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6],multipliers = [-1, -2, -3, -4, -5, -6]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6],multipliers = [-1, -2, -3, -4, -5, -6]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 1, 2, 3],multipliers = [1, -1, 1, -1, 1, -1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 1, 2, 3],multipliers = [1, -1, 1, -1, 1, -1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [1, 2, 3, 4, 5]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [1, 2, 3, 4, 5]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300],multipliers = [1, 2]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300],multipliers = [1, 2]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],multipliers = [9, 8, 7]) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],multipliers = [9, 8, 7]) == 194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 5, -3, 5, 5],multipliers = [-1, 1, -1, 1, -1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 5, -3, 5, 5],multipliers = [-1, 1, -1, 1, -1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [1, 2, 3, 4]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [1, 2, 3, 4]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -3, -2, 7, 1],multipliers = [-10, -5, 3, 4, 6]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -3, -2, 7, 1],multipliers = [-10, -5, 3, 4, 6]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],multipliers = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],multipliers = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],multipliers = [-1, -2, -3]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],multipliers = [-1, -2, -3]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],multipliers = [1, 2, 3, 4, 5]) == -35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],multipliers = [1, 2, 3, 4, 5]) == -35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],multipliers = [5, 4, 3, 2, 1]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],multipliers = [5, 4, 3, 2, 1]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],multipliers = [1, 2, 3, 4, 5]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],multipliers = [1, 2, 3, 4, 5]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6],multipliers = [1, 2, 3]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6],multipliers = [1, 2, 3]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],multipliers = [1, 2, 3, 4]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],multipliers = [1, 2, 3, 4]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],multipliers = [3, 2, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],multipliers = [3, 2, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5],multipliers = [-1, -2, -3]) == -37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5],multipliers = [-1, -2, -3]) == -37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],multipliers = [-1, -2, -3, -4, -5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],multipliers = [-1, -2, -3, -4, -5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],multipliers = [1, 2, 3]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],multipliers = [1, 2, 3]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 3, 8, 6],multipliers = [3, 2, 4]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 3, 8, 6],multipliers = [3, 2, 4]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 4, 9, 2, 7, 1, 6, 0],multipliers = [10, -20, 30, -40, 50]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 4, 9, 2, 7, 1, 6, 0],multipliers = [10, -20, 30, -40, 50]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [10, -20, 30, -40, 50]) == 115000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [10, -20, 30, -40, 50]) == 115000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12],multipliers = [10, 9, 8, 7, 6, 5]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12],multipliers = [10, 9, 8, 7, 6, 5]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 38500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 38500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],multipliers = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],multipliers = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 6, 9, 2, 7, 4, 10],multipliers = [-1, 2, -3, 4, -5, 6]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 6, 9, 2, 7, 4, 10],multipliers = [-1, 2, -3, 4, -5, 6]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 205: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],multipliers = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -5550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],multipliers = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -5550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],multipliers = [-1, -2, -3, -4, -5]) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],multipliers = [-1, -2, -3, -4, -5]) == 185: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [-1, 1, -1, 1, -1, 1]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [-1, 1, -1, 1, -1, 1]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1000, 10000, 100000, 1000000],multipliers = [10, 20, 30, 40, 50]) == 50432010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1000, 10000, 100000, 1000000],multipliers = [10, 20, 30, 40, 50]) == 50432010: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 8, 2, -7, 6, 1, 4, -9, 11],multipliers = [3, -2, 7, 5, -8, 6]) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 8, 2, -7, 6, 1, 4, -9, 11],multipliers = [3, -2, 7, 5, -8, 6]) == 234: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 21250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 21250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [5, 4, 3, 2, 1]) == -350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [5, 4, 3, 2, 1]) == -350: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [10, -20, 30, -40, 50]) == 115000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [10, -20, 30, -40, 50]) == 115000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, 400, 500, 600, -700, 800, -900],multipliers = [10, 20, 30, 40, 50, 60, 70]) == 77000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, 400, 500, 600, -700, 800, -900],multipliers = [10, 20, 30, 40, 50, 60, 70]) == 77000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [-1, -1, -1, -1, -1]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [-1, -1, -1, -1, -1]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],multipliers = [1, 2, 3, 4, 5, 6, 7]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],multipliers = [1, 2, 3, 4, 5, 6, 7]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500],multipliers = [1, -1, 1, -1, 1, -1]) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500],multipliers = [1, -1, 1, -1, 1, -1]) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],multipliers = [1, -1, 1, -1, 1]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],multipliers = [1, -1, 1, -1, 1]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [5, 10, 15, 20, 25]) == 925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [5, 10, 15, 20, 25]) == 925: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],multipliers = [29, 27, 25, 23, 21]) == 3165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],multipliers = [29, 27, 25, 23, 21]) == 3165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 10, 15, 1, 4, 7],multipliers = [10, 20, 30, 40, 50]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 10, 15, 1, 4, 7],multipliers = [10, 20, 30, 40, 50]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -30500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -30500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],multipliers = [-1, 2, -3, 4, -5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],multipliers = [-1, 2, -3, 4, -5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 1, 4, 3],multipliers = [-1, -2, -3]) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 1, 4, 3],multipliers = [-1, -2, -3]) == -12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 1000, 900, 800, 700],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 35400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 1000, 900, 800, 700],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 35400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -22000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 2485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 2485: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [10, 20, 30, 40, 50]) == -5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [10, 20, 30, 40, 50]) == -5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == 480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],multipliers = [10, 20, 30, 40, 50]) == 2150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],multipliers = [10, 20, 30, 40, 50]) == 2150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -22000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [1, -1, 1, -1, 1, -1, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [1, -1, 1, -1, 1, -1, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],multipliers = [-5, 10, -15, 20, -25, 30]) == 4625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],multipliers = [-5, 10, -15, 20, -25, 30]) == 4625: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [15, 14, 13, 12, 11]) == 855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [15, 14, 13, 12, 11]) == 855: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50],multipliers = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50],multipliers = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [20, 19, 18, 17, 16, 15, 14]) == 2051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [20, 19, 18, 17, 16, 15, 14]) == 2051: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],multipliers = [1, 2, 3, 4, 5, 6]) == 15300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],multipliers = [1, 2, 3, 4, 5, 6]) == 15300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700],multipliers = [1, -2, 3, -4, 5]) == 7500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700],multipliers = [1, -2, 3, -4, 5]) == 7500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],multipliers = [1, 2, -3, 4, -5]) == 1030
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],multipliers = [1, 2, -3, 4, -5]) == 1030: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],multipliers = [100, -50, 25, -12, 6]) == 9630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],multipliers = [100, -50, 25, -12, 6]) == 9630: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 821
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 821: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1925: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [1, 2, 3, 4, 5]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [1, 2, 3, 4, 5]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],multipliers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],multipliers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 3, -1, 2, -4, 6, -7, 8, -9, 10],multipliers = [1, -1, 1, -1, 1, -1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 3, -1, 2, -4, 6, -7, 8, -9, 10],multipliers = [1, -1, 1, -1, 1, -1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2670: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [1, -1, 2, -2, 3]) == 4700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [1, -1, 2, -2, 3]) == 4700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [1, 2, 3, 4, 5, 6]) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [1, 2, 3, 4, 5, 6]) == 161: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10],multipliers = [10, -10, 20, -20, 30]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10],multipliers = [10, -10, 20, -20, 30]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [1, -1, 1, -1, 1, -1]) == 4100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [1, -1, 1, -1, 1, -1]) == 4100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000, 6000, -6000, 7000, -7000, 8000, -8000, 9000, -9000, 10000, -10000],multipliers = [100, -99, 98, -97, 96, -95, 94, -93, 92, -91, 90, -89, 88, -87, 86, -85, 84, -83, 82, -81]) == 10195000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000, 6000, -6000, 7000, -7000, 8000, -8000, 9000, -9000, 10000, -10000],multipliers = [100, -99, 98, -97, 96, -95, 94, -93, 92, -91, 90, -89, 88, -87, 86, -85, 84, -83, 82, -81]) == 10195000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, -2, 6, 7, -4, 10, 15, -20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8]) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, -2, 6, 7, -4, 10, 15, -20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8]) == 242: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, -100, 200, -200, 500, -300, 400, -400, 600, -500],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 61000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, -100, 200, -200, 500, -300, 400, -400, 600, -500],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 61000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21]) == -1320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21]) == -1320: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [2, -3, 4, -5, 6]) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [2, -3, 4, -5, 6]) == 211: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 100, -50, -25, -75, -100, 200, 150, 175, 200],multipliers = [10, -5, 2, -1, 3, -2]) == 2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 100, -50, -25, -75, -100, 200, 150, 175, 200],multipliers = [10, -5, 2, -1, 3, -2]) == 2750: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 3850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 3850: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [-1, -2, -3, -4, -5]) == -550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [-1, -2, -3, -4, -5]) == -550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],multipliers = [-1, 1, -1, 1, -1, 1, -1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],multipliers = [-1, 1, -1, 1, -1, 1, -1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],multipliers = [5, -5, 4, -4, 3, -3]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],multipliers = [5, -5, 4, -4, 3, -3]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -334: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [100, -100, 100, -100, 100]) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [100, -100, 100, -100, 100]) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1081
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1081: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1540: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, -2, 6, 7, -4, 10],multipliers = [1, 2, 3, 4, 5]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, -2, 6, 7, -4, 10],multipliers = [1, 2, 3, 4, 5]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [1, 2, 3, 4, 5]) == 1850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [1, 2, 3, 4, 5]) == 1850: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54666: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [-1, -2, -3, -4, -5]) == 1150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [-1, -2, -3, -4, -5]) == 1150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],multipliers = [1, 2, 3, 4, 5]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],multipliers = [1, 2, 3, 4, 5]) == 600: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 385
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],multipliers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 385
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [10, 9, 8, 7, 6]) == 330
    assert candidate(nums = [-1, -2, -3, -4, -5, -6],multipliers = [-1, -2, -3, -4, -5, -6]) == 91
    assert candidate(nums = [-3, -2, -1, 1, 2, 3],multipliers = [1, -1, 1, -1, 1, -1]) == 12
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [1, 2, 3, 4, 5]) == 101
    assert candidate(nums = [100, 200, 300],multipliers = [1, 2]) == 700
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],multipliers = [9, 8, 7]) == 194
    assert candidate(nums = [5, -2, 5, -3, 5, 5],multipliers = [-1, 1, -1, 1, -1, 1]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [1, 2, 3, 4]) == 80
    assert candidate(nums = [-5, -3, -3, -2, 7, 1],multipliers = [-10, -5, 3, 4, 6]) == 102
    assert candidate(nums = [1],multipliers = [1]) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5],multipliers = [-1, -2, -3]) == 23
    assert candidate(nums = [-1, -2, -3, -4, -5],multipliers = [1, 2, 3, 4, 5]) == -35
    assert candidate(nums = [10, 20, 30, 40, 50],multipliers = [5, 4, 3, 2, 1]) == 550
    assert candidate(nums = [10, 20, 30, 40, 50],multipliers = [1, 2, 3, 4, 5]) == 550
    assert candidate(nums = [1, 2, 3, 4, 5, 6],multipliers = [1, 2, 3]) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],multipliers = [1, 2, 3, 4]) == 71
    assert candidate(nums = [1, 2, 3],multipliers = [3, 2, 1]) == 14
    assert candidate(nums = [9, 8, 7, 6, 5],multipliers = [-1, -2, -3]) == -37
    assert candidate(nums = [-1, -2, -3, -4, -5],multipliers = [-1, -2, -3, -4, -5]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5],multipliers = [1, 2, 3]) == 23
    assert candidate(nums = [5, 7, 3, 8, 6],multipliers = [3, 2, 4]) == 60
    assert candidate(nums = [5, 3, 8, 4, 9, 2, 7, 1, 6, 0],multipliers = [10, -20, 30, -40, 50]) == 540
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -10
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [10, -20, 30, -40, 50]) == 115000
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12],multipliers = [10, 9, 8, 7, 6, 5]) == 105
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 38500
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],multipliers = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55250
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [5, 3, 8, 1, 6, 9, 2, 7, 4, 10],multipliers = [-1, 2, -3, 4, -5, 6]) == 75
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 75
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 205
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],multipliers = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -5550
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],multipliers = [-1, -2, -3, -4, -5]) == 185
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [-1, 1, -1, 1, -1, 1]) == 6000
    assert candidate(nums = [1, 100, 1000, 10000, 100000, 1000000],multipliers = [10, 20, 30, 40, 50]) == 50432010
    assert candidate(nums = [5, -3, 8, 2, -7, 6, 1, 4, -9, 11],multipliers = [3, -2, 7, 5, -8, 6]) == 234
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 21250
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [5, 4, 3, 2, 1]) == -350
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [10, -20, 30, -40, 50]) == 115000
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -220
    assert candidate(nums = [-100, -200, -300, 400, 500, 600, -700, 800, -900],multipliers = [10, 20, 30, 40, 50, 60, 70]) == 77000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [-1, -1, -1, -1, -1]) == -5
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],multipliers = [1, 2, 3, 4, 5, 6, 7]) == 52
    assert candidate(nums = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500],multipliers = [1, -1, 1, -1, 1, -1]) == 2400
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],multipliers = [1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 800
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],multipliers = [1, -1, 1, -1, 1]) == 240
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [5, 10, 15, 20, 25]) == 925
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],multipliers = [29, 27, 25, 23, 21]) == 3165
    assert candidate(nums = [5, 3, 8, 10, 15, 1, 4, 7],multipliers = [10, 20, 30, 40, 50]) == 1500
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -30500
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],multipliers = [-1, 2, -3, 4, -5]) == 110
    assert candidate(nums = [5, 2, 1, 4, 3],multipliers = [-1, -2, -3]) == -12
    assert candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 1000, 900, 800, 700],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 35400
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -22000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 2485
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [10, 20, 30, 40, 50]) == -5000
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],multipliers = [-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]) == 480
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],multipliers = [10, 20, 30, 40, 50]) == 2150
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -22000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [1, -1, 1, -1, 1, -1, 1]) == 48
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],multipliers = [-5, 10, -15, 20, -25, 30]) == 4625
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 155
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [15, 14, 13, 12, 11]) == 855
    assert candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50],multipliers = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 300
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [20, 19, 18, 17, 16, 15, 14]) == 2051
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],multipliers = [1, 2, 3, 4, 5, 6]) == 15300
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700],multipliers = [1, -2, 3, -4, 5]) == 7500
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],multipliers = [1, 2, -3, 4, -5]) == 1030
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],multipliers = [100, -50, 25, -12, 6]) == 9630
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 821
    assert candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1925
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 200
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [1, 2, 3, 4, 5]) == 7000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],multipliers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 700
    assert candidate(nums = [-5, 3, -1, 2, -4, 6, -7, 8, -9, 10],multipliers = [1, -1, 1, -1, 1, -1]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2670
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -8
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],multipliers = [1, -1, 2, -2, 3]) == 4700
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],multipliers = [1, 2, 3, 4, 5, 6]) == 161
    assert candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10],multipliers = [10, -10, 20, -20, 30]) == 450
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],multipliers = [1, -1, 1, -1, 1, -1]) == 4100
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000, 6000, -6000, 7000, -7000, 8000, -8000, 9000, -9000, 10000, -10000],multipliers = [100, -99, 98, -97, 96, -95, 94, -93, 92, -91, 90, -89, 88, -87, 86, -85, 84, -83, 82, -81]) == 10195000
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 26800
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [5, 3, 8, -2, 6, 7, -4, 10, 15, -20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8]) == 242
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 75
    assert candidate(nums = [300, -100, 200, -200, 500, -300, 400, -400, 600, -500],multipliers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 61000
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],multipliers = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21]) == -1320
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [2, -3, 4, -5, 6]) == 211
    assert candidate(nums = [50, 25, 75, 100, -50, -25, -75, -100, 200, 150, 175, 200],multipliers = [10, -5, 2, -1, 3, -2]) == 2750
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],multipliers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -220
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 3850
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [-1, -2, -3, -4, -5]) == -550
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],multipliers = [-1, 1, -1, 1, -1, 1, -1, 1]) == 50
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],multipliers = [5, -5, 4, -4, 3, -3]) == 87
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],multipliers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -334
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [100, -100, 100, -100, 100]) == 500000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],multipliers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1081
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1540
    assert candidate(nums = [5, 3, 8, -2, 6, 7, -4, 10],multipliers = [1, 2, 3, 4, 5]) == 77
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],multipliers = [1, 2, 3, 4, 5]) == 1850
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54666
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],multipliers = [1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],multipliers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],multipliers = [-1, -2, -3, -4, -5]) == 1150
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],multipliers = [1, 2, 3, 4, 5]) == 600


