def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, 100000, -100000, 100000, -100000]) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, 100000, -100000, 100000, -100000]) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 600000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 600000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -999, 1000, -999, 1000, -999]) == 5997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -999, 1000, -999, 1000, -999]) == 5997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, -100, -200, -300, 100, 200, 300, -100, -200, -300]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, -100, -200, -300, 100, 200, 300, -100, -200, -300]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, -5, -5, -5, -5, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, -5, -5, -5, -5, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 2, 9, 1, 7, 4, 6, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 2, 9, 1, 7, 4, 6, 0]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110]) == 660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110]) == 660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 5, -3, 7, -2, 8, -1, 6, -4, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 5, -3, 7, -2, 8, -1, 6, -4, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, 0, -1, 5, -5, 1, -1, 0, 1, 5, -5, 0, 1, -1, 5]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, 0, -1, 5, -5, 1, -1, 0, 1, 5, -5, 0, 1, -1, 5]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 3, -2, 7, -1, 4, -8, 10, -6, 2]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 3, -2, 7, -1, 4, -8, 10, -6, 2]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, -200, 300, -400, 500, -600]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, -200, 300, -400, 500, -600]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 200, -100, 300, -150]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 200, -100, 300, -150]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, -50, 300, 400, -600, 700, 800, -900, 1000]) == 2700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, -50, 300, 400, -600, 700, 800, -900, 1000]) == 2700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, -1, 0, 1, -1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, -1, 0, 1, -1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25, 27, -29, 31]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25, 27, -29, 31]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 15, -20, 25, -30, 35]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 15, -20, 25, -30, 35]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -4, 3, -2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -4, 3, -2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 20, -10, 5, -2, 1]) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 20, -10, 5, -2, 1]) == 188: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -12, 6, -3, 1, -1, 0]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -12, 6, -3, 1, -1, 0]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -1, 4, -2, 3, -6, 2, -1, 7, -3]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -1, 4, -2, 3, -6, 2, -1, 7, -3]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -4, 5, 6, -7, 8, 9, -10]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -4, 5, 6, -7, 8, 9, -10]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 2, -1, 4, -2, 3, -1, 2, -3, 4]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 2, -1, 4, -2, 3, -1, 2, -3, 4]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 200, -50, 300, 400, -600, 700, 800, -900, 1000, -1100, 1200, -1300]) == 6300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 200, -50, 300, 400, -600, 700, 800, -900, 1000, -1100, 1200, -1300]) == 6300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12]) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12]) == 374: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, -5, 3, 2, -1, -10, 4, 7, -3]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, -5, 3, 2, -1, -10, 4, 7, -3]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -99999, 99998, -99997, 99996, -99995, 99994, -99993, 99992, -99991]) == 999955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -99999, 99998, -99997, 99996, -99995, 99994, -99993, 99992, -99991]) == 999955: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, 11, -2, 12, -3, 13, -4, 14, -5]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, 11, -2, 12, -3, 13, -4, 14, -5]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000, -100000, -100000, -100000, -100000, -100000, 100000, 100000, 100000, 100000, 100000]) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000, -100000, -100000, -100000, -100000, -100000, 100000, 100000, 100000, 100000, 100000]) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -3, 2, -4, 3, -5, 4, -6, 5, -7, 6, -8, 7, -9, 8, -10, 9, -11, 10, -12]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -3, 2, -4, 3, -5, 4, -6, 5, -7, 6, -8, 7, -9, 8, -10, 9, -11, 10, -12]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 8, -2, 7, -4, 6, -1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 8, -2, 7, -4, 6, -1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, -5, -5, 5, 5, -5, -5, 5, 5, -5, -5, 5, 5, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, -5, -5, 5, 5, -5, -5, 5, 5, -5, -5, 5, 5, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 600000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 600000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25, 27, -29, 31, -33, 35, -37, 39]) == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25, 27, -29, 31, -33, 35, -37, 39]) == 399: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 0, 2, -2, 0, 3, -3, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 0, 2, -2, 0, 3, -3, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 8, 0, 2, -1, 7]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 8, 0, 2, -1, 7]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, -4, 1, 2, -1, 4, -3, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, -4, 1, 2, -1, 4, -3, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 200, -250, 300, -350, 400]) == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 200, -250, 300, -350, 400]) == 1650: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 6, 4, 9, 2, 7, 0]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 6, 4, 9, 2, 7, 0]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000]) == 700000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000]) == 700000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, 100000, -100000, 100000, -100000, 100000]) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, 100000, -100000, 100000, -100000, 100000]) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 7, -4, 9, -1, 6, -3, 8]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 7, -4, 9, -1, 6, -3, 8]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 10, -15, 20, -25, 30]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 10, -15, 20, -25, 30]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, 16, -17, 18, -19, 20]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, 16, -17, 18, -19, 20]) == 120: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [-1, 2, -3, 4, -5]) == 14
    assert candidate(nums = [1, -1, 1, -1, 1]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 3, 5, 7, 9]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 500000
    assert candidate(nums = [3, -1, 1, 2]) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 2
    assert candidate(nums = [-5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [-100000, 100000, -100000, 100000, -100000]) == 400000
    assert candidate(nums = [5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [5]) == 5
    assert candidate(nums = [2, 2, 2, 2, 2]) == 2
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 600000
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]) == 119
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1
    assert candidate(nums = [1000, -999, 1000, -999, 1000, -999]) == 5997
    assert candidate(nums = [100, 200, 300, -100, -200, -300, 100, 200, 300, -100, -200, -300]) == 900
    assert candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 90
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 250
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, -5, -5, -5, -5, -5]) == 10
    assert candidate(nums = [5, 3, 8, 2, 9, 1, 7, 4, 6, 0]) == 25
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110]) == 660
    assert candidate(nums = [-10, 5, -3, 7, -2, 8, -1, 6, -4, 9]) == 45
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 39
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 150
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 20
    assert candidate(nums = [-5, 1, 0, -1, 5, -5, 1, -1, 0, 1, 5, -5, 0, 1, -1, 5]) == 22
    assert candidate(nums = [-5, 3, -2, 7, -1, 4, -8, 10, -6, 2]) == 43
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 30
    assert candidate(nums = [1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 1]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [-10, 100, -200, 300, -400, 500, -600]) == 2100
    assert candidate(nums = [100, -50, 200, -100, 300, -150]) == 900
    assert candidate(nums = [100, 200, -50, 300, 400, -600, 700, 800, -900, 1000]) == 2700
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 20
    assert candidate(nums = [1, 0, -1, 0, 1, -1, 0, 1, -1, 0]) == 2
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9]) == 44
    assert candidate(nums = [1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25, 27, -29, 31]) == 255
    assert candidate(nums = [10, -5, 15, -20, 25, -30, 35]) == 140
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 300
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5]) == 4
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60]) == 360
    assert candidate(nums = [5, -4, 3, -2, 1]) == 15
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 550
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100
    assert candidate(nums = [1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1]) == 14
    assert candidate(nums = [100, -50, 20, -10, 5, -2, 1]) == 188
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 20
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 1
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 10
    assert candidate(nums = [100, -50, 25, -12, 6, -3, 1, -1, 0]) == 198
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 1
    assert candidate(nums = [5, -1, 4, -2, 3, -6, 2, -1, 7, -3]) == 34
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 42
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000]) == 1000000
    assert candidate(nums = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 50
    assert candidate(nums = [1, 2, 3, -4, 5, 6, -7, 8, 9, -10]) == 21
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 120
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54
    assert candidate(nums = [5, -3, 2, -1, 4, -2, 3, -1, 2, -3, 4]) == 30
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54
    assert candidate(nums = [-100, 200, -50, 300, 400, -600, 700, 800, -900, 1000, -1100, 1200, -1300]) == 6300
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 100
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 500000
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12]) == 374
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80]) == 350
    assert candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 55
    assert candidate(nums = [1, 10, -5, 3, 2, -1, -10, 4, 7, -3]) == 29
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90]) == 450
    assert candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [100000, -99999, 99998, -99997, 99996, -99995, 99994, -99993, 99992, -99991]) == 999955
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, -1, 11, -2, 12, -3, 13, -4, 14, -5]) == 75
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, -100000, -100000, -100000, -100000, -100000, 100000, 100000, 100000, 100000, 100000]) == 300000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, -3, 2, -4, 3, -5, 4, -6, 5, -7, 6, -8, 7, -9, 8, -10, 9, -11, 10, -12]) == 130
    assert candidate(nums = [5, -3, 8, -2, 7, -4, 6, -1]) == 36
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100002
    assert candidate(nums = [5, 5, -5, -5, 5, 5, -5, -5, 5, 5, -5, -5, 5, 5, -5]) == 10
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1000
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 54
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 600000
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 11
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 45
    assert candidate(nums = [-1, 3, -5, 7, -9, 11, -13, 15, -17, 19, -21, 23, -25, 27, -29, 31, -33, 35, -37, 39]) == 399
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
    assert candidate(nums = [0, 1, -1, 0, 2, -2, 0, 3, -3, 0]) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [5, -3, 8, 0, 2, -1, 7]) == 26
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
    assert candidate(nums = [5, -2, 3, -4, 1, 2, -1, 4, -3, 2]) == 15
    assert candidate(nums = [100, -50, 200, -250, 300, -350, 400]) == 1650
    assert candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 11
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7]) == 28
    assert candidate(nums = [5, 3, 8, 1, 6, 4, 9, 2, 7, 0]) == 25
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000]) == 700000
    assert candidate(nums = [-100000, 100000, -100000, 100000, -100000, 100000]) == 500000
    assert candidate(nums = [5, -2, 7, -4, 9, -1, 6, -3, 8]) == 45
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1]) == 8
    assert candidate(nums = [-5, 10, -15, 20, -25, 30]) == 100
    assert candidate(nums = [-100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 100000
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, 16, -17, 18, -19, 20]) == 120


