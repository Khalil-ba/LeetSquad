def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [-1, 0, 2, 3, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0, 2, 3, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -1, 0, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -1, 0, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 0, 1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0, 1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, 2, 3, 4, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, 2, 3, 4, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -8, -7, -6, -5, -4, -3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -8, -7, -6, -5, -4, -3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -3, -1, 2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -3, -1, 2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -5, 0, 3, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -5, 0, 3, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 5, 8, 17]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 5, 8, 17]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -5, 3, 4, 7, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -5, 3, 4, 7, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-3, -2, -1, 0, 1, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-3, -2, -1, 0, 1, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-3, -2, -1, 0, 1, 5, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-3, -2, -1, 0, 1, 5, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -3, -1, 2, 4, 6, 8, 10, 12, 14]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -3, -1, 2, 4, 6, 8, 10, 12, 14]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -50, -20, -10, 0, 1, 3, 5, 7, 9, 10, 20, 50, 100]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -50, -20, -10, 0, 1, 3, 5, 7, 9, 10, 20, 50, 100]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-15, -8, -5, -2, 0, 3, 6, 10, 12, 15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-15, -8, -5, -2, 0, 3, 6, 10, 12, 15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -7, -5, -3, -1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -7, -5, -3, -1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-999, -888, -777, -666, -555, -444, -333, -222, -111, 0, 111, 222, 333, 444, 555]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-999, -888, -777, -666, -555, -444, -333, -222, -111, 0, 111, 222, 333, 444, 555]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -50, -20, -10, -1, 0, 1, 20, 50, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -50, -20, -10, -1, 0, 1, 20, 50, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, 40, 41, 42, 43]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, 40, 41, 42, 43]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-500, -400, -300, -200, -100, -50, -25, -10, -5, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-500, -400, -300, -200, -100, -50, -25, -10, -5, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -50, -20, -10, -5, -1, 0, 2, 10, 20, 50, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -50, -20, -10, -5, -1, 0, 2, 10, 20, 50, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -15, -10, -5, 0, 1, 3, 4, 5, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -15, -10, -5, 0, 1, 3, 4, 5, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -500, -250, -125, -63, -31, -16, -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 31, 63, 125, 250, 500, 1000]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -500, -250, -125, -63, -31, -16, -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 31, 63, 125, 250, 500, 1000]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -50, -25, -10, -5, 0, 1, 5, 10, 15, 20, 25, 50, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -50, -25, -10, -5, 0, 1, 5, 10, 15, 20, 25, 50, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, -1, 0, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, -1, 0, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-15, -7, -2, 0, 2, 4, 6, 8, 10, 12, 14]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-15, -7, -2, 0, 2, 4, 6, 8, 10, 12, 14]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-50, -25, -10, -5, -2, -1, 0, 1, 5, 10, 25, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-50, -25, -10, -5, -2, -1, 0, 1, 5, 10, 25, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -50, -10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -50, -10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -15, -5, 0, 5, 6, 7, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -15, -5, 0, 5, 6, 7, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100, -50, -20, -10, -5, -2, 0, 2, 4, 6, 8, 10, 20, 30, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100, -50, -20, -10, -5, -2, 0, 2, 4, 6, 8, 10, 20, 30, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, 0, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, 0, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -500, -250, -100, -50, -25, -10, -5, -2, 0, 2, 5, 10, 25, 50, 100, 250, 500, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -500, -250, -100, -50, -25, -10, -5, -2, 0, 2, 5, 10, 25, 50, 100, 250, 500, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -4, -3, -2, -1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -4, -3, -2, -1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -15, -10, -5, 0, 5, 10, 15, 20]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -15, -10, -5, 0, 5, 10, 15, 20]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -15, -10, -5, -2, 0, 2, 4, 7, 9, 11]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -15, -10, -5, -2, 0, 2, 4, 7, 9, 11]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-15, -10, -5, 0, 1, 3, 6, 8, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-15, -10, -5, 0, 1, 3, 6, 8, 10]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [-1, 0, 2, 3, 5]) == 2
    assert candidate(arr = [-1, -1, 0, 1, 2]) == -1
    assert candidate(arr = [-1, 0, 1, 2, 3, 4, 5]) == -1
    assert candidate(arr = [0]) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7]) == -1
    assert candidate(arr = [-1, 1, 2, 3, 4, 5, 6]) == 1
    assert candidate(arr = [-9, -8, -7, -6, -5, -4, -3]) == -1
    assert candidate(arr = [-1, 0]) == -1
    assert candidate(arr = [-5, -3, -1, 2, 4, 6, 8]) == 4
    assert candidate(arr = [1, 1, 1, 1, 1]) == -1
    assert candidate(arr = [0, 1]) == 0
    assert candidate(arr = [-10, -5, 0, 3, 7]) == 3
    assert candidate(arr = [-1, 0, 1]) == -1
    assert candidate(arr = [0, 2, 5, 8, 17]) == 0
    assert candidate(arr = [1, 2, 3, 4, 5]) == -1
    assert candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == -1
    assert candidate(arr = [-10, -5, 3, 4, 7, 9]) == -1
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70]) == -1
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(arr = [-5, -4, -3, -2, -1]) == -1
    assert candidate(arr = [-3, -2, -1, 0, 1, 2, 3]) == -1
    assert candidate(arr = [-3, -2, -1, 0, 1, 5, 6]) == 5
    assert candidate(arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
    assert candidate(arr = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]) == 9
    assert candidate(arr = [-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 2
    assert candidate(arr = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == -1
    assert candidate(arr = [-5, -3, -1, 2, 4, 6, 8, 10, 12, 14]) == 4
    assert candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0
    assert candidate(arr = [-100, -50, -20, -10, 0, 1, 3, 5, 7, 9, 10, 20, 50, 100]) == 9
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(arr = [-15, -8, -5, -2, 0, 3, 6, 10, 12, 15]) == 6
    assert candidate(arr = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(arr = [-2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == -1
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(arr = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40]) == -1
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == -1
    assert candidate(arr = [-500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 2, 3, 4, 5]) == -1
    assert candidate(arr = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == -1
    assert candidate(arr = [-9, -7, -5, -3, -1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 8
    assert candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(arr = [-1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]) == -1
    assert candidate(arr = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == -1
    assert candidate(arr = [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]) == 1
    assert candidate(arr = [-50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == -1
    assert candidate(arr = [-999, -888, -777, -666, -555, -444, -333, -222, -111, 0, 111, 222, 333, 444, 555]) == -1
    assert candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(arr = [-100, -50, -20, -10, -1, 0, 1, 20, 50, 100]) == -1
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == -1
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == -1
    assert candidate(arr = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, 40, 41, 42, 43]) == -1
    assert candidate(arr = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
    assert candidate(arr = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 10
    assert candidate(arr = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]) == -1
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1
    assert candidate(arr = [-500, -400, -300, -200, -100, -50, -25, -10, -5, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [-100, -50, -20, -10, -5, -1, 0, 2, 10, 20, 50, 100]) == -1
    assert candidate(arr = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]) == -1
    assert candidate(arr = [-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == -1
    assert candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]) == -1
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(arr = [-1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1
    assert candidate(arr = [-20, -15, -10, -5, 0, 1, 3, 4, 5, 6]) == -1
    assert candidate(arr = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == -1
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(arr = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == -1
    assert candidate(arr = [-1000, -500, -250, -125, -63, -31, -16, -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 31, 63, 125, 250, 500, 1000]) == 16
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(arr = [-100, -50, -25, -10, -5, 0, 1, 5, 10, 15, 20, 25, 50, 100]) == -1
    assert candidate(arr = [-30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -1
    assert candidate(arr = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 5
    assert candidate(arr = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == -1
    assert candidate(arr = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, -1, 0, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == -1
    assert candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 11
    assert candidate(arr = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 21]) == -1
    assert candidate(arr = [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == -1
    assert candidate(arr = [-1, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 4
    assert candidate(arr = [-15, -7, -2, 0, 2, 4, 6, 8, 10, 12, 14]) == 6
    assert candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == -1
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1
    assert candidate(arr = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81]) == -1
    assert candidate(arr = [-50, -25, -10, -5, -2, -1, 0, 1, 5, 10, 25, 50]) == -1
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [-100, -50, -10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1
    assert candidate(arr = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == -1
    assert candidate(arr = [-20, -15, -5, 0, 5, 6, 7, 8, 10]) == -1
    assert candidate(arr = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(arr = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1
    assert candidate(arr = [-100, -50, -20, -10, -5, -2, 0, 2, 4, 6, 8, 10, 20, 30, 50]) == -1
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
    assert candidate(arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == -1
    assert candidate(arr = [-1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000]) == -1
    assert candidate(arr = [-5, 0, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 2
    assert candidate(arr = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 0
    assert candidate(arr = [-1000, -500, -250, -100, -50, -25, -10, -5, -2, 0, 2, 5, 10, 25, 50, 100, 250, 500, 1000]) == -1
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 11, 12, 13, 14, 15]) == 10
    assert candidate(arr = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17]) == -1
    assert candidate(arr = [-5, -4, -3, -2, -1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 10
    assert candidate(arr = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [-2, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 2
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1
    assert candidate(arr = [-20, -15, -10, -5, 0, 5, 10, 15, 20]) == 5
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(arr = [-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 0
    assert candidate(arr = [-20, -15, -10, -5, -2, 0, 2, 4, 7, 9, 11]) == 9
    assert candidate(arr = [-2, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(arr = [-15, -10, -5, 0, 1, 3, 6, 8, 10]) == 6


