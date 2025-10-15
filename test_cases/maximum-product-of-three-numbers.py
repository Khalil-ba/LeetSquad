def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-10, -10, 5, 2]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -10, 5, 2]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 99]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 99]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, -1, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, -1, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -10, 5, 2]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -10, 5, 2]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 5, 7]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 5, 7]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 0, -1, -2, -3, -4]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 0, -1, -2, -3, -4]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, -5, 1, -100]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, -5, 1, -100]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 3, 5, 9]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 3, 5, 9]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 24273
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 24273: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 1, 2, 3, 100, 200]) == 60000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 1, 2, 3, 100, 200]) == 60000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, 0, 5, 15, 25]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, 0, 5, 15, 25]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, 500, -500, 250, -250, 125, -125]) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, 500, -500, 250, -250, 125, -125]) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30]) == 18000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30]) == 18000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -999, -998, -997, -996, -995]) == -988046940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -999, -998, -997, -996, -995]) == -988046940: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, -5, 5, 5, 5, 5, 5]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, -5, 5, 5, 5, 5, 5]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, 1, 2, 3]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, 1, 2, 3]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -6, -7, 1, 2, 3]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -6, -7, 1, 2, 3]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, 500, -500, 0, 1, -1]) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, 500, -500, 0, 1, -1]) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -900, -800, -700, -600, -500, 400, 300, 200, 100, 0]) == 360000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -900, -800, -700, -600, -500, 400, 300, 200, 100, 0]) == 360000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125]) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125]) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1000, -1000, -1000]) == 5000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1000, -1000, -1000]) == 5000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, -100, -200, -300]) == 18000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, -100, -200, -300]) == 18000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, -2, -3, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, -2, -3, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 60000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 60000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, 0, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, 0, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10, 20, -30, 40]) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10, 20, -30, 40]) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, 3, 4, -5, 6, -7, 8, 9, -10]) == 630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, 3, 4, -5, 6, -7, 8, 9, -10]) == 630: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -999, -998, 0, 1, 2]) == 1998000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -999, -998, 0, 1, 2]) == 1998000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, 1000, 1000, 1000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, 1000, 1000, 1000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 0, 50, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 0, 50, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, -11, -13]) == 1287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, -11, -13]) == 1287: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995]) == 997002000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995]) == 997002000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, -5, 1, -100]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, -5, 1, -100]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, -1, -2, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, -1, -2, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, 5, 6, 2]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, 5, 6, 2]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1000, 1000, 1000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1000, 1000, 1000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, 1, 2]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, 1, 2]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 0, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 0, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, 3, 4, 5, 6]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, 3, 4, 5, 6]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-999, -998, -997, 997, 998, 999]) == 996004998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-999, -998, -997, 997, 998, 999]) == 996004998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 200, 100, 50, 25]) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 200, 100, 50, 25]) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, -1, -2, -3]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, -1, -2, -3]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -6, -7, -8]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -6, -7, -8]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 280000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 280000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -999, -998, -1, -2, -3]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -999, -998, -1, -2, -3]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, 5, 6, 7]) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, 5, 6, 7]) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200]) == 60000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200]) == 60000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, 5, 10, 15]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, 5, 10, 15]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -1000, -1000, 1, 2, 3]) == 3000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -1000, -1000, 1, 2, 3]) == 3000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -1, -2, -3, 4, 5, 6, 7, 8, 9]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -1, -2, -3, 4, 5, 6, 7, 8, 9]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500]) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500]) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -6, -7, -8, -9]) == -210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -6, -7, -8, -9]) == -210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31]) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31]) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, -1000]) == 997002000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, -1000]) == 997002000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, 500, -500, 200, -200]) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, 500, -500, 200, -200]) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, 30, -40, 50]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, 30, -40, 50]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -2, 0, 2, 5, 10]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -2, 0, 2, 5, 10]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, -5, -5, -5]) == -125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, -5, -5, -5]) == -125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, -30, -40, 50, 60]) == 72000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, -30, -40, 50, 60]) == 72000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -6, 2, 3, 4]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -6, 2, 3, 4]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -4, -5, -6]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -4, -5, -6]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -90, -80, 70, 60, 50, 40, 30, 20, 10]) == 630000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -90, -80, 70, 60, 50, 40, 30, 20, 10]) == 630000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5]) == -210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5]) == -210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -999, -998, 998, 999, 1000]) == 999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -999, -998, 998, 999, 1000]) == 999000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, -100, -90]) == 900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, -100, -90]) == 900000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -999, -998, 1000, 999, 998]) == 999000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -999, -998, 1000, 999, 998]) == 999000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 4, 5, 6, 7, 8, 9]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 4, 5, 6, 7, 8, 9]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, 100]) == 120000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, 100]) == 120000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, 1, 2, 3]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, 1, 2, 3]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 997002000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 997002000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -3, 4, -5, 6]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -3, 4, -5, 6]) == 90: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-10, -10, 5, 2]) == 500
    assert candidate(nums = [1, 2, 3, 4]) == 24
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 99]) == 99
    assert candidate(nums = [0, 2, 3, 5]) == 30
    assert candidate(nums = [0, 2, 3, -1, 5]) == 30
    assert candidate(nums = [1, 2, 3]) == 6
    assert candidate(nums = [-10, -10, 5, 2]) == 500
    assert candidate(nums = [0, 2, 3, 5, 7]) == 105
    assert candidate(nums = [1, 2, 3, 0, -1, -2, -3, -4]) == 36
    assert candidate(nums = [-1, -2, -3, -4, -5]) == -6
    assert candidate(nums = [-1, -2, -3, -4]) == -6
    assert candidate(nums = [1, 10, -5, 1, -100]) == 5000
    assert candidate(nums = [0, 2, 3, 5, 9]) == 135
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 720
    assert candidate(nums = [-1, -2, -3]) == -6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 24273
    assert candidate(nums = [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]) == 1
    assert candidate(nums = [-10, 1, 2, 3, 100, 200]) == 60000
    assert candidate(nums = [0, 0, 0, 0, 0, 1, -1]) == 0
    assert candidate(nums = [-10, -20, 0, 5, 15, 25]) == 5000
    assert candidate(nums = [-1000, 1000, 500, -500, 250, -250, 125, -125]) == 500000000
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == 18000
    assert candidate(nums = [-1000, -999, -998, -997, -996, -995]) == -988046940
    assert candidate(nums = [-5, -5, -5, -5, -5, 5, 5, 5, 5, 5]) == 125
    assert candidate(nums = [-10, -20, -30, 1, 2, 3]) == 1800
    assert candidate(nums = [-5, -6, -7, 1, 2, 3]) == 126
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [-1000, 1000, 500, -500, 0, 1, -1]) == 500000000
    assert candidate(nums = [-1000, -900, -800, -700, -600, -500, 400, 300, 200, 100, 0]) == 360000000
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125]) == 500000000
    assert candidate(nums = [1, 2, 3, 4, 5, -1000, -1000, -1000]) == 5000000
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 48
    assert candidate(nums = [-5, -4, -3, -2, -1]) == -6
    assert candidate(nums = [100, 200, 300, -100, -200, -300]) == 18000000
    assert candidate(nums = [-1, 0, 1]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 2, 3]) == 6
    assert candidate(nums = [-1, 0, 1, 2, -2, -3, 3]) == 18
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 100
    assert candidate(nums = [100, 200, 300, 400, 500]) == 60000000
    assert candidate(nums = [-1, -2, 0, 2, 1]) == 4
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(nums = [-10, 0, 10, 20, -30, 40]) == 12000
    assert candidate(nums = [0, 0, 0, 0, 1]) == 0
    assert candidate(nums = [-1, -2, 3, 4, -5, 6, -7, 8, 9, -10]) == 630
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [-1000, -999, -998, 0, 1, 2]) == 1998000
    assert candidate(nums = [-1, -1, -1, 1000, 1000, 1000]) == 1000000000
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 27
    assert candidate(nums = [-100, 0, 50, 100]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, -11, -13]) == 1287
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 100
    assert candidate(nums = [1000, 999, 998, 997, 996, 995]) == 997002000
    assert candidate(nums = [1, 10, -5, 1, -100]) == 5000
    assert candidate(nums = [0, 0, 0, -1, -2, -3]) == 0
    assert candidate(nums = [-10, -20, 5, 6, 2]) == 1200
    assert candidate(nums = [1, 1, 1, 1000, 1000, 1000]) == 1000000000
    assert candidate(nums = [-10, -20, -30, 1, 2]) == 1200
    assert candidate(nums = [-100, 0, 100]) == 0
    assert candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002000
    assert candidate(nums = [-1, -2, -3, -4, -5]) == -6
    assert candidate(nums = [-1, -2, -3, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1000]) == 1000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert candidate(nums = [-1, -2, 3, 4, 5, 6]) == 120
    assert candidate(nums = [-999, -998, -997, 997, 998, 999]) == 996004998
    assert candidate(nums = [1000, 500, 200, 100, 50, 25]) == 100000000
    assert candidate(nums = [10, 20, 30, -1, -2, -3]) == 6000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 720
    assert candidate(nums = [1, 2, 3, 4, 5, -6, -7, -8]) == 280
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 280000
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 720
    assert candidate(nums = [-1000, -999, -998, -1, -2, -3]) == -6
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 100000
    assert candidate(nums = [-10, -20, 5, 6, 7]) == 1400
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200]) == 60000000
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 100
    assert candidate(nums = [-10, -20, 5, 10, 15]) == 3000
    assert candidate(nums = [-1000, -1000, -1000, 1, 2, 3]) == 3000000
    assert candidate(nums = [1, 2, 3, -1, -2, -3, 4, 5, 6, 7, 8, 9]) == 504
    assert candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500]) == 100000000
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 125
    assert candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002000
    assert candidate(nums = [-5, -6, -7, -8, -9]) == -210
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 64
    assert candidate(nums = [-1000, 1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31]) == 500000000
    assert candidate(nums = [1000, 999, 998, -1000]) == 997002000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [-1000, 1000, 500, -500, 200, -200]) == 500000000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [0, 0, 0, 1, 2, 3]) == 6
    assert candidate(nums = [-10, 20, 30, -40, 50]) == 30000
    assert candidate(nums = [-10, -5, -2, 0, 2, 5, 10]) == 500
    assert candidate(nums = [-5, -5, -5, -5, -5, -5, -5]) == -125
    assert candidate(nums = [10, 20, -30, -40, 50, 60]) == 72000
    assert candidate(nums = [-5, -6, 2, 3, 4]) == 120
    assert candidate(nums = [1, 2, 3, -4, -5, -6]) == 90
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -6
    assert candidate(nums = [-100, -90, -80, 70, 60, 50, 40, 30, 20, 10]) == 630000
    assert candidate(nums = [-10, -9, -8, -7, -6, -5]) == -210
    assert candidate(nums = [0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5]) == 60
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [-1000, -999, -998, 998, 999, 1000]) == 999000000
    assert candidate(nums = [100, 90, 80, -100, -90]) == 900000
    assert candidate(nums = [-1000, -999, -998, 1000, 999, 998]) == 999000000
    assert candidate(nums = [-1, -2, -3, 4, 5, 6, 7, 8, 9]) == 504
    assert candidate(nums = [-10, -20, -30, -40, 100]) == 120000
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(nums = [-5, -4, -3, 1, 2, 3]) == 60
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 997002000
    assert candidate(nums = [1, 2, -3, 4, -5, 6]) == 90


