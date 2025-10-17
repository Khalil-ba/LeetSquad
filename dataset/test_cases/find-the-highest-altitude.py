def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(gain = [4, 3, 2, 1, 0, -1, -2, -3, -4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [4, 3, 2, 1, 0, -1, -2, -3, -4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, -2, -3, -4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, -2, -3, -4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, -20, -30, -40, -50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, -20, -30, -40, -50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-5, -4, -3, -2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-5, -4, -3, -2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-100, 50, -50, 100, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-100, 50, -50, 100, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-100, 100, -100, 100, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-100, 100, -100, 100, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -100, 100, -100, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -100, 100, -100, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, -2, -3, -4, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, -2, -3, -4, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-50, 50, -25, 25, -12, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-50, 50, -25, 25, -12, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -50, 50, -100, 50]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -50, 50, -100, 50]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -100, 50, -50, 25, -25]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -100, 50, -50, 25, -25]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -100, 100, -100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -100, 100, -100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-5, 1, 5, 0, -7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-5, 1, 5, 0, -7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [50, 50, 50, 50, 50]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [50, 50, 50, 50, 50]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-4, -3, -2, -1, 4, 3, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-4, -3, -2, -1, 4, 3, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [23, -15, 42, -5, 0, 17, -30, 29]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [23, -15, 42, -5, 0, 17, -30, 29]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, -20, 30, 40, -50, 60, -70, 80, -90, 100]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, -20, 30, 40, -50, 60, -70, 80, -90, 100]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -5, 15, -20, 25, -30, 35, -40]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -5, 15, -20, 25, -30, 35, -40]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -100, 100, -100, 100, -100, 100, -100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -100, 100, -100, 100, -100, 100, -100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -98]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -98]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -5, 3, 2, -3, 4, -2, 5, -6, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -5, 3, 2, -3, 4, -2, 5, -6, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -1, 99, -2, 98, -3, 97, -4, 96, -5, 95, -6, 94, -7, 93, -8, 92, -9, 91, -10]) == 910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -1, 99, -2, 98, -3, 97, -4, 96, -5, 95, -6, 94, -7, 93, -8, 92, -9, 91, -10]) == 910: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -5, 3, 2, -3, 4, -1, -2, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -5, 3, 2, -3, 4, -1, -2, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, -3, 20, -20, 30, -10, 15, -5, 25, -15, 10, -5, 30, -30, 40]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, -3, 20, -20, 30, -10, 15, -5, 25, -15, 10, -5, 30, -30, 40]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, 15, 20, 25, 30, 35, 40, 45, 50, -100]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, 15, 20, 25, 30, 35, 40, 45, 50, -100]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(gain = [50, -20, 30, -10, 40, -5, 60, -25, 70, -10]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [50, -20, 30, -10, 40, -5, 60, -25, 70, -10]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 25, -25, 50, -50, 100, -100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 25, -25, 50, -50, 100, -100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [20, 30, -10, -40, 50, 10, -20, 30, -40, 50]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [20, 30, -10, -40, 50, 10, -20, 30, -40, 50]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, 10, 15, 20, 25, -5, -10, -15, -20, -25, 5, 10, 15, 20, 25, -5, -10, -15, -20, -25]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, 10, 15, 20, 25, -5, -10, -15, -20, -25, 5, 10, 15, 20, 25, -5, -10, -15, -20, -25]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(gain = [99, -50, 50, -100, 100, -99, 99, -49, 49, -51, 51, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [99, -50, 50, -100, 100, -99, 99, -49, 49, -51, 51, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -25, 25, -50, 50, -75, 75, -100, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -25, 25, -50, 50, -75, 75, -100, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -5, 3, -2, 8, -4, 6, -3, 5, -1, 7, -2, 9, -4, 11, -5, 13, -6, 15, -7]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -5, 3, -2, 8, -4, 6, -3, 5, -1, 7, -2, 9, -4, 11, -5, 13, -6, 15, -7]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, 5, 5, 5, 5, -5, -5, -5, -5, -5, 10, 10, -10, -10, 15]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, 5, 5, 5, 5, -5, -5, -5, -5, -5, 10, 10, -10, -10, 15]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, 50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, 50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 20, -10, 5, -3, 15, -10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 20, -10, 5, -3, 15, -10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -5, 3, 8, -2, 15, -7, 20]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -5, 3, 8, -2, 15, -7, 20]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-5, -10, -15, 20, 25, -30, 35, -40, 45, -50, 55, -60, 65, -70, 75, -80, 85, -90, 95]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-5, -10, -15, 20, 25, -30, 35, -40, 45, -50, 55, -60, 65, -70, 75, -80, 85, -90, 95]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -110, 120, -130, 140, -150]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -110, 120, -130, 140, -150]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27, 28, -29, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27, 28, -29, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, 10, 15, 20, 25, 30, -5, -10, -15, -20, -25, -30]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, 10, 15, 20, 25, 30, -5, -10, -15, -20, -25, -30]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -50, 50, -100, 100, -100, 50, -50, 25, -25, 75, -75, 125, -125, 62, -62, 31, -31, 15, -15]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -50, 50, -100, 100, -100, 50, -50, 25, -25, 75, -75, 125, -125, 62, -62, 31, -31, 15, -15]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120, 130, -140, 150, -160, 170, -180, 190, -200]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120, 130, -140, 150, -160, 170, -180, 190, -200]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -50, 25, -12, 50, -25, 60, -30, 70, -35, 80, -40, 90, -45, 100]) == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -50, 25, -12, 50, -25, 60, -30, 70, -35, 80, -40, 90, -45, 100]) == 338: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [20, -10, 30, -15, 40, -20, 50, -25, 60, -30, 70, -35, 80, -40, 90]) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [20, -10, 30, -15, 40, -20, 50, -25, 60, -30, 70, -35, 80, -40, 90]) == 265: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [2, 3, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [2, 3, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-50, 25, -25, 50, -50, 75, -100, 125]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-50, 25, -25, 50, -50, 75, -100, 125]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-50, 0, 50, 0, -50, 0, 50, 0, -50, 0, 50, 0, -50, 0, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-50, 0, 50, 0, -50, 0, 50, 0, -50, 0, 50, 0, -50, 0, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 20, -10, 30, -20, 10, -30, 40, -50, 60]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 20, -10, 30, -20, 10, -30, 40, -50, 60]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -50, 50, -50, 100, -50, 50, -50, 100]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -50, 50, -50, 100, -50, 50, -50, 100]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20, 21, -22, 23, -24, 25, -26, 27, -28, 29, -30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20, 21, -22, 23, -24, 25, -26, 27, -28, 29, -30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -20, 30, -40, 50, -60, 70]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -20, 30, -40, 50, -60, 70]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27, 28, -29, 30, -30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27, 28, -29, 30, -30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(gain = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -99, 98, -97, 96, -95, 94, -93, 92, -91, 90, -89, 88, -87, 86, -85, 84, -83, 82, -81, 80]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -99, 98, -97, 96, -95, 94, -93, 92, -91, 90, -89, 88, -87, 86, -85, 84, -83, 82, -81, 80]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [2, 4, -3, 1, -2, 1, 5, -4, 3, -1, 0, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [2, 4, -3, 1, -2, 1, 5, -4, 3, -1, 0, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(gain = [100, -50, 50, -100, 50, -50, 100, -100, 50, -50]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [100, -50, 50, -100, 50, -50, 100, -100, 50, -50]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-50, 50, -50, 50, -50, 50, -50, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-50, 50, -50, 50, -50, 50, -50, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(gain = [-1, 3, -2, 4, -3, 5, -4, 6, -5, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(gain = [-1, 3, -2, 4, -3, 5, -4, 6, -5, 7]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(gain = [4, 3, 2, 1, 0, -1, -2, -3, -4]) == 10
    assert candidate(gain = [-1, -2, -3, -4]) == 0
    assert candidate(gain = [-10, -20, -30, -40, -50]) == 0
    assert candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 145
    assert candidate(gain = [-1, 1, -1, 1, -1, 1]) == 0
    assert candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(gain = [-5, -4, -3, -2, -1]) == 0
    assert candidate(gain = [5, 5, 5, 5]) == 20
    assert candidate(gain = [-100, 50, -50, 100, -100]) == 0
    assert candidate(gain = [-100, 100, -100, 100, -100]) == 0
    assert candidate(gain = [100, -100, 100, -100, 100]) == 100
    assert candidate(gain = [1, 2, 3, 4, 5]) == 15
    assert candidate(gain = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -100]) == 0
    assert candidate(gain = [-1, -2, -3, -4, -5]) == 0
    assert candidate(gain = [1, -1, 1, -1, 1, -1]) == 1
    assert candidate(gain = [-50, 50, -25, 25, -12, 12]) == 0
    assert candidate(gain = [10, 20, 30, 40, 50]) == 150
    assert candidate(gain = [0, 0, 0, 0, 0]) == 0
    assert candidate(gain = [100, -50, 50, -100, 50]) == 100
    assert candidate(gain = [100, -100, 50, -50, 25, -25]) == 100
    assert candidate(gain = [100, -100, 100, -100]) == 100
    assert candidate(gain = [-5, 1, 5, 0, -7]) == 1
    assert candidate(gain = [0, 0, 0, 0]) == 0
    assert candidate(gain = [50, 50, 50, 50, 50]) == 250
    assert candidate(gain = [-4, -3, -2, -1, 4, 3, 2]) == 0
    assert candidate(gain = [23, -15, 42, -5, 0, 17, -30, 29]) == 62
    assert candidate(gain = [-10, -20, 30, 40, -50, 60, -70, 80, -90, 100]) == 70
    assert candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(gain = [10, -5, 15, -20, 25, -30, 35, -40]) == 30
    assert candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(gain = [100, -100, 100, -100, 100, -100, 100, -100]) == 100
    assert candidate(gain = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == 50
    assert candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10
    assert candidate(gain = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -98]) == 100
    assert candidate(gain = [10, -5, 3, 2, -3, 4, -2, 5, -6, 1]) == 14
    assert candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(gain = [100, -1, 99, -2, 98, -3, 97, -4, 96, -5, 95, -6, 94, -7, 93, -8, 92, -9, 91, -10]) == 910
    assert candidate(gain = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
    assert candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 55
    assert candidate(gain = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 0
    assert candidate(gain = [10, -5, 3, 2, -3, 4, -1, -2, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 18
    assert candidate(gain = [5, -3, 20, -20, 30, -10, 15, -5, 25, -15, 10, -5, 30, -30, 40]) == 87
    assert candidate(gain = [10, 15, 20, 25, 30, 35, 40, 45, 50, -100]) == 270
    assert candidate(gain = [50, -20, 30, -10, 40, -5, 60, -25, 70, -10]) == 190
    assert candidate(gain = [0, 25, -25, 50, -50, 100, -100]) == 100
    assert candidate(gain = [20, 30, -10, -40, 50, 10, -20, 30, -40, 50]) == 80
    assert candidate(gain = [5, 10, 15, 20, 25, -5, -10, -15, -20, -25, 5, 10, 15, 20, 25, -5, -10, -15, -20, -25]) == 75
    assert candidate(gain = [99, -50, 50, -100, 100, -99, 99, -49, 49, -51, 51, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 99
    assert candidate(gain = [100, -25, 25, -50, 50, -75, 75, -100, 100]) == 100
    assert candidate(gain = [10, -5, 3, -2, 8, -4, 6, -3, 5, -1, 7, -2, 9, -4, 11, -5, 13, -6, 15, -7]) == 55
    assert candidate(gain = [5, 5, 5, 5, 5, -5, -5, -5, -5, -5, 10, 10, -10, -10, 15]) == 25
    assert candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11]) == 210
    assert candidate(gain = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(gain = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 5
    assert candidate(gain = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100]) == 100
    assert candidate(gain = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 0
    assert candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10
    assert candidate(gain = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15
    assert candidate(gain = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, 50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 150
    assert candidate(gain = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 0
    assert candidate(gain = [0, 20, -10, 5, -3, 15, -10]) == 27
    assert candidate(gain = [10, -5, 3, 8, -2, 15, -7, 20]) == 42
    assert candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(gain = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 0
    assert candidate(gain = [-5, -10, -15, 20, 25, -30, 35, -40, 45, -50, 55, -60, 65, -70, 75, -80, 85, -90, 95]) == 50
    assert candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
    assert candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -110, 120, -130, 140, -150]) == 70
    assert candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 50
    assert candidate(gain = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == 99
    assert candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27, 28, -29, 30]) == 15
    assert candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(gain = [5, 10, 15, 20, 25, 30, -5, -10, -15, -20, -25, -30]) == 105
    assert candidate(gain = [100, -50, 50, -100, 100, -100, 50, -50, 25, -25, 75, -75, 125, -125, 62, -62, 31, -31, 15, -15]) == 125
    assert candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 5
    assert candidate(gain = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120, 130, -140, 150, -160, 170, -180, 190, -200]) == 100
    assert candidate(gain = [100, -50, 25, -12, 50, -25, 60, -30, 70, -35, 80, -40, 90, -45, 100]) == 338
    assert candidate(gain = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 0
    assert candidate(gain = [20, -10, 30, -15, 40, -20, 50, -25, 60, -30, 70, -35, 80, -40, 90]) == 265
    assert candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 50
    assert candidate(gain = [2, 3, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]) == 17
    assert candidate(gain = [-50, 25, -25, 50, -50, 75, -100, 125]) == 50
    assert candidate(gain = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == 275
    assert candidate(gain = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10]) == 0
    assert candidate(gain = [1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 9
    assert candidate(gain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(gain = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 10
    assert candidate(gain = [-50, 0, 50, 0, -50, 0, 50, 0, -50, 0, 50, 0, -50, 0, 50]) == 0
    assert candidate(gain = [0, 20, -10, 30, -20, 10, -30, 40, -50, 60]) == 50
    assert candidate(gain = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 50
    assert candidate(gain = [100, -50, 50, -50, 100, -50, 50, -50, 100]) == 200
    assert candidate(gain = [100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99, 100, -99]) == 114
    assert candidate(gain = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 9
    assert candidate(gain = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 10
    assert candidate(gain = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20, 21, -22, 23, -24, 25, -26, 27, -28, 29, -30]) == 15
    assert candidate(gain = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25]) == 25
    assert candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 210
    assert candidate(gain = [10, -20, 30, -40, 50, -60, 70]) == 40
    assert candidate(gain = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
    assert candidate(gain = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
    assert candidate(gain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55
    assert candidate(gain = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27, 28, -29, 30, -30]) == 15
    assert candidate(gain = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10
    assert candidate(gain = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(gain = [100, -99, 98, -97, 96, -95, 94, -93, 92, -91, 90, -89, 88, -87, 86, -85, 84, -83, 82, -81, 80]) == 100
    assert candidate(gain = [2, 4, -3, 1, -2, 1, 5, -4, 3, -1, 0, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 12
    assert candidate(gain = [100, -50, 50, -100, 50, -50, 100, -100, 50, -50]) == 100
    assert candidate(gain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(gain = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 100
    assert candidate(gain = [-50, 50, -50, 50, -50, 50, -50, 50]) == 0
    assert candidate(gain = [-1, 3, -2, 4, -3, 5, -4, 6, -5, 7]) == 10


