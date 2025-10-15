def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-3, -2, -1, 0, 0, 1, 2, 3]) == [-1, -2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-3, -2, -1, 0, 0, 1, 2, 3]) == [-1, -2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,sums = [0, 0, 0, 0]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,sums = [0, 0, 0, 0]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, 5]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, 5]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [3, 1, 2, 0, 4, 5, 6, 8]) == [1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [3, 1, 2, 0, 4, 5, 6, 8]) == [1, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8]) == [0, -1, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8]) == [0, -1, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, -1]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, -1]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, -4, 8, -16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, -4, 8, -16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-1, 0, 1, 2, 3, 4, -2, -3, -4]) == [1, 2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-1, 0, 1, 2, 3, 4, -2, -3, -4]) == [1, 2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [-21, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-2, -3, 4, 8, -16, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [-21, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-2, -3, 4, 8, -16, 21]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [-1, 2, 4, -8, -16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [-1, 2, 4, -8, -16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == [0, 1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == [0, 1, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [0, 2, 2, 4, 6, 6, 8, 10]) == [2, 2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [0, 2, 2, 4, 6, 6, 8, 10]) == [2, 2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == [-1, -2, -4, 8, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == [-1, -2, -4, 8, 17]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-5, -4, -3, -2, -1, 0, 1, 2, 3]) == [-1, 2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-5, -4, -3, -2, -1, 0, 1, 2, 3]) == [-1, 2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-6, -5, -5, -4, -2, -1, -1, 0, 1, 1, 2, 4, 5, 5, 6, 7]) == [-1, -1, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-6, -5, -5, -4, -2, -1, -1, 0, 1, 1, 2, 4, 5, 5, 6, 7]) == [-1, -1, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-7, -6, -5, -4, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, -7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-7, -6, -5, -4, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, -7]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, -2, -4, -8, -16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, -2, -4, -8, -16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, -2, 4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, -2, 4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -8, -7, -6, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 10]) == [2, 3, -4, -6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -8, -7, -6, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 10]) == [2, 3, -4, -6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0]) == [1, -2, 4, -8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0]) == [1, -2, 4, -8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [10, -10, 5, -5, 15, -15, 0, 20, -20]) == [5, 10, -20, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [10, -10, 5, -5, 15, -15, 0, 20, -20]) == [5, 10, -20, 40]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-2, -1, 0, 1, 2, 3]) == [1, -2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-2, -1, 0, 1, 2, 3]) == [1, -2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == [-1, 1, 2, -4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == [-1, 1, 2, -4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, -2, 4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, -2, 4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [0, -1, -2, -3, -4, 1, 2, 3, 4, -5, 5, -6, 6, -7, 7, 8]) == [-1, -2, -4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [0, -1, -2, -3, -4, 1, 2, 3, 4, -5, 5, -6, 6, -7, 7, 8]) == [-1, -2, -4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [10, 20, 30, 40, 50, 60, 70, 80]) == [10, 20, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [10, 20, 30, 40, 50, 60, 70, 80]) == [10, 20, 40]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [1, -1, 2, -2, 3, -3, 4, -4, 0]) == [1, 2, -4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [1, -1, 2, -2, 3, -3, 4, -4, 0]) == [1, 2, -4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 2, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 2, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-1, -2, -3, -4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, -4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-1, -2, -3, -4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, -4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-9, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]) == [-2, -3, -4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-9, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]) == [-2, -3, -4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [-20, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [2, 3, -4, 8, -16, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [-20, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [2, 3, -4, 8, -16, 32]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]) == [1, 2, 4, 8, 16, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]) == [1, 2, 4, 8, 16, 32]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]) == [1, 2, 3, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]) == [1, 2, 3, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]) == [1, -2, 4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]) == [1, -2, 4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [-1, -2, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [-1, -2, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == [-1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == [-1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-10, -7, -9, -8, -5, -6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-10, -7, -9, -8, -5, -6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, -2, 4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, -2, 4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [-63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]) == [-1, -2, -4, -8, -16, -32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [-63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]) == [-1, -2, -4, -8, -16, -32]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-4, -2, -1, 0, 0, 1, 2, 4]) == [2, 3, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-4, -2, -1, 0, 0, 1, 2, 4]) == [2, 3, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-1, -2, -3, 0, 1, 2, 3, 4, 5]) == [-1, -2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-1, -2, -3, 0, 1, 2, 3, 4, 5]) == [-1, -2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-6, -3, -5, -2, -4, -1, 0, 1, 3, 2, 4, 5]) == [1, -2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-6, -3, -5, -2, -4, -1, 0, 1, 3, 2, 4, 5]) == [1, -2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-5, -4, -3, -2, -1, -1, 0, 0, 1, 1, 2, 3, 4, 5]) == [-1, 2, -4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-5, -4, -3, -2, -1, -1, 0, 0, 1, 1, 2, 3, 4, 5]) == [-1, 2, -4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-1, 1, 2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-1, 1, 2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-6, -4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 4, 6]) == [-2, 3, -4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-6, -4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 4, 6]) == [-2, 3, -4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == [0, 1, 2, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == [0, 1, 2, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2]) == [-1, -1, 2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2]) == [-1, -1, 2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 15]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, 2]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, 2]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == [-2, 3, 4, -8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == [-2, 3, 4, -8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [-10, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10]) == [1, -2, 2, 4, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [-10, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10]) == [1, -2, 2, 4, -8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [-31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [-1, -2, -4, -8, -16, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [-31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [-1, -2, -4, -8, -16, 31]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [31, 17, 21, 18, 12, 13, 19, 14, 20, 24, 8, 11, 9, 5, 4, 10, 0, 15, 7, 3, 16, 6, 2, 1, 23, 22, 16, 25, 26, 30, 27, 29, 31]) == [1, 2, 4, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [31, 17, 21, 18, 12, 13, 19, 14, 20, 24, 8, 11, 9, 5, 4, 10, 0, 15, 7, 3, 16, 6, 2, 1, 23, 22, 16, 25, 26, 30, 27, 29, 31]) == [1, 2, 4, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-5, -3, -2, -1, 0, 0, 1, 2]) == [-2, -3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-5, -3, -2, -1, 0, 0, 1, 2]) == [-2, -3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-1, -1, -1, -1, -1, 0, 0, 0]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-1, -1, -1, -1, -1, 0, 0, 0]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, -1, -1, -1, -1, -2, -2, -2, -2, -3, -3, -3, -3, -4, -4, -4, -4, -5, -5, -5, -5]) == [0, 0, -1, 2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, -1, -1, -1, -1, -2, -2, -2, -2, -3, -3, -3, -3, -4, -4, -4, -4, -5, -5, -5, -5]) == [0, 0, -1, 2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, 1]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, 1]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, 3]) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, 3]) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,sums = [-1, 0, 1, 2]) == [-1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,sums = [-1, 0, 1, 2]) == [-1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-1, 0, 1, 2, 3, 4]) == [-1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-1, 0, 1, 2, 3, 4]) == [-1, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,sums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14, -15, 15, -16, 16, -17, 17, -18, 18, -19, 19, -20, 20, -21, 21, -22, 22, -23, 23, -24, 24, -25, 25, -26, 26, -27, 27, -28, 28, -29, 29, -30, 30, -31, 31, -32, 32]) == [1, 2, 4, 8, 16, -32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,sums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14, -15, 15, -16, 16, -17, 17, -18, 18, -19, 19, -20, 20, -21, 21, -22, 22, -23, 23, -24, 24, -25, 25, -26, 26, -27, 27, -28, 28, -29, 29, -30, 30, -31, 31, -32, 32]) == [1, 2, 4, 8, 16, -32]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == [1, -2, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == [1, -2, -4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, -5]) == [-5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, -5]) == [-5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,sums = [-2, -1, 0, 1]) == [1, -2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,sums = [-2, -1, 0, 1]) == [1, -2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-3, -1, 0, 1, 2, 3, 4, 6]) == [2, -3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-3, -1, 0, 1, 2, 3, 4, 6]) == [2, -3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-1, -2, -3, 0, 1, 2, 3, 4]) == [-1, -2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-1, -2, -3, 0, 1, 2, 3, 4]) == [-1, -2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,sums = [0, 0]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,sums = [0, 0]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-6, -5, -5, -4, -3, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6]) == [1, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-6, -5, -5, -4, -3, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6]) == [1, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [-3, -2, -1, -1, 0, 0, 1, 2]) == [-1, -2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [-3, -2, -1, -1, 0, 0, 1, 2]) == [-1, -2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,sums = [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,sums = [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert candidate(n = 3,sums = [-3, -2, -1, 0, 0, 1, 2, 3]) == [-1, -2, 3]
    assert candidate(n = 2,sums = [0, 0, 0, 0]) == [0, 0]
    assert candidate(n = 1,sums = [0, 5]) == [5]
    assert candidate(n = 3,sums = [3, 1, 2, 0, 4, 5, 6, 8]) == [1, 2, 4]
    assert candidate(n = 4,sums = [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8]) == [0, -1, 4, 5]
    assert candidate(n = 1,sums = [0, -1]) == [-1]
    assert candidate(n = 5,sums = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, -4, 8, -16]
    assert candidate(n = 3,sums = [-1, 0, 1, 2, 3, 4, -2, -3, -4]) == [1, 2, -4]
    assert candidate(n = 6,sums = [-21, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-2, -3, 4, 8, -16, 21]
    assert candidate(n = 5,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 2, 4, 8, 16]
    assert candidate(n = 5,sums = [-25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [-1, 2, 4, -8, -16]
    assert candidate(n = 4,sums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == [0, 1, 2, 4]
    assert candidate(n = 4,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 4, 8]
    assert candidate(n = 3,sums = [0, 2, 2, 4, 6, 6, 8, 10]) == [2, 2, 6]
    assert candidate(n = 5,sums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]) == [1, 2, 4, 8, 16]
    assert candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]
    assert candidate(n = 5,sums = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == [-1, -2, -4, 8, 17]
    assert candidate(n = 3,sums = [-5, -4, -3, -2, -1, 0, 1, 2, 3]) == [-1, 2, -4]
    assert candidate(n = 3,sums = [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4]
    assert candidate(n = 3,sums = [-6, -5, -5, -4, -2, -1, -1, 0, 1, 1, 2, 4, 5, 5, 6, 7]) == [-1, -1, -4]
    assert candidate(n = 4,sums = [-7, -6, -5, -4, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, -7]
    assert candidate(n = 5,sums = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, -2, -4, -8, -16]
    assert candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, -2, 4, -8, 16]
    assert candidate(n = 5,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 2, 4, 8, 16]
    assert candidate(n = 5,sums = [-10, -8, -7, -6, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 10]) == [2, 3, -4, -6, 7]
    assert candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0]) == [1, -2, 4, -8, 10]
    assert candidate(n = 4,sums = [10, -10, 5, -5, 15, -15, 0, 20, -20]) == [5, 10, -20, 40]
    assert candidate(n = 3,sums = [-2, -1, 0, 1, 2, 3]) == [1, -2, 4]
    assert candidate(n = 4,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]
    assert candidate(n = 5,sums = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == [-1, 1, 2, -4, 8]
    assert candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, -2, 4, -8, 16]
    assert candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 4, 8, 16]
    assert candidate(n = 4,sums = [0, -1, -2, -3, -4, 1, 2, 3, 4, -5, 5, -6, 6, -7, 7, 8]) == [-1, -2, -4, 8]
    assert candidate(n = 3,sums = [10, 20, 30, 40, 50, 60, 70, 80]) == [10, 20, 40]
    assert candidate(n = 4,sums = [1, -1, 2, -2, 3, -3, 4, -4, 0]) == [1, 2, -4, 8]
    assert candidate(n = 5,sums = [0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 2, 4, 8]
    assert candidate(n = 4,sums = [-1, -2, -3, -4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, -4, 8]
    assert candidate(n = 4,sums = [-9, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]) == [-2, -3, -4, 8]
    assert candidate(n = 6,sums = [-20, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [2, 3, -4, 8, -16, 32]
    assert candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == [1, 2, 4, 8, 16]
    assert candidate(n = 6,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert candidate(n = 6,sums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]) == [1, 2, 4, 8, 16, 32]
    assert candidate(n = 5,sums = [0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]) == [1, 2, 3, 4, 8]
    assert candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]) == [1, -2, 4, -8, 16]
    assert candidate(n = 4,sums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [-1, -2, 4, 8]
    assert candidate(n = 5,sums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == [-1, 2, 4, 8, 16]
    assert candidate(n = 4,sums = [-10, -7, -9, -8, -5, -6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]
    assert candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 2, 4, 8, 16]
    assert candidate(n = 5,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, -2, 4, -8, 16]
    assert candidate(n = 6,sums = [-63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]) == [-1, -2, -4, -8, -16, -32]
    assert candidate(n = 3,sums = [-4, -2, -1, 0, 0, 1, 2, 4]) == [2, 3, -4]
    assert candidate(n = 5,sums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [1, 2, 4, 8, 16]
    assert candidate(n = 3,sums = [-1, -2, -3, 0, 1, 2, 3, 4, 5]) == [-1, -2, 4]
    assert candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]
    assert candidate(n = 3,sums = [-6, -3, -5, -2, -4, -1, 0, 1, 3, 2, 4, 5]) == [1, -2, -4]
    assert candidate(n = 4,sums = [-5, -4, -3, -2, -1, -1, 0, 0, 1, 1, 2, 3, 4, 5]) == [-1, 2, -4, 4]
    assert candidate(n = 4,sums = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-1, 1, 2, -4]
    assert candidate(n = 4,sums = [-6, -4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 4, 6]) == [-2, 3, -4, 4]
    assert candidate(n = 5,sums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == [0, 1, 2, 4, 8]
    assert candidate(n = 4,sums = [-6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2]) == [-1, -1, 2, -4]
    assert candidate(n = 5,sums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 15]
    assert candidate(n = 1,sums = [0, 2]) == [2]
    assert candidate(n = 5,sums = [-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == [-2, 3, 4, -8, 10]
    assert candidate(n = 5,sums = [-10, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10]) == [1, -2, 2, 4, -8]
    assert candidate(n = 6,sums = [-31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == [-1, -2, -4, -8, -16, 31]
    assert candidate(n = 5,sums = [31, 17, 21, 18, 12, 13, 19, 14, 20, 24, 8, 11, 9, 5, 4, 10, 0, 15, 7, 3, 16, 6, 2, 1, 23, 22, 16, 25, 26, 30, 27, 29, 31]) == [1, 2, 4, 8, 16]
    assert candidate(n = 3,sums = [-5, -3, -2, -1, 0, 0, 1, 2]) == [-2, -3, 4]
    assert candidate(n = 3,sums = [-1, -1, -1, -1, -1, 0, 0, 0]) == [0, 0, 0]
    assert candidate(n = 5,sums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, -1, -1, -1, -1, -2, -2, -2, -2, -3, -3, -3, -3, -4, -4, -4, -4, -5, -5, -5, -5]) == [0, 0, -1, 2, -4]
    assert candidate(n = 1,sums = [0, 1]) == [1]
    assert candidate(n = 4,sums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [0, 0, 1, 2]
    assert candidate(n = 1,sums = [0, 3]) == [3]
    assert candidate(n = 2,sums = [-1, 0, 1, 2]) == [-1, 2]
    assert candidate(n = 3,sums = [-1, 0, 1, 2, 3, 4]) == [-1, 2, 4]
    assert candidate(n = 6,sums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14, -15, 15, -16, 16, -17, 17, -18, 18, -19, 19, -20, 20, -21, 21, -22, 22, -23, 23, -24, 24, -25, 25, -26, 26, -27, 27, -28, 28, -29, 29, -30, 30, -31, 31, -32, 32]) == [1, 2, 4, 8, 16, -32]
    assert candidate(n = 4,sums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, -2, 4, -8]
    assert candidate(n = 3,sums = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == [1, -2, -4]
    assert candidate(n = 1,sums = [0, -5]) == [-5]
    assert candidate(n = 5,sums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-1, -2, -4, -8, 16]
    assert candidate(n = 4,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0]
    assert candidate(n = 2,sums = [-2, -1, 0, 1]) == [1, -2]
    assert candidate(n = 3,sums = [-3, -1, 0, 1, 2, 3, 4, 6]) == [2, -3, 4]
    assert candidate(n = 3,sums = [-1, -2, -3, 0, 1, 2, 3, 4]) == [-1, -2, 4]
    assert candidate(n = 1,sums = [0, 0]) == [0]
    assert candidate(n = 3,sums = [-6, -5, -5, -4, -3, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6]) == [1, 1, 3]
    assert candidate(n = 3,sums = [-3, -2, -1, -1, 0, 0, 1, 2]) == [-1, -2, 2]
    assert candidate(n = 5,sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 0]
    assert candidate(n = 3,sums = [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4]


