def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(triangle = [[-10]]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10]]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [2, 3], [1, -1, -3], [-2, 1, -1, -2]]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [2, 3], [1, -1, -3], [-2, 1, -1, -2]]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [2, -2], [3, -3, 3], [-4, -4, 4, 4]]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [2, -2], [3, -3, 3], [-4, -4, 4, 4]]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [2, 3], [1, -1, -3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [2, 3], [1, -1, -3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [1, 0], [1, 1, 1], [1, 2, 3, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [1, 0], [1, 1, 1], [1, 2, 3, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [-1, -2], [-3, -4, -5]]) == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [-1, -2], [-3, -4, -5]]) == -7: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [10000, -10000], [10000, 10000, 10000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [10000, -10000], [10000, 10000, 10000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [2, -3], [4, -5, 6], [-7, 8, -9, 10]]) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [2, -3], [4, -5, 6], [-7, 8, -9, 10]]) == -18: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 3], [4, 5, 6]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 3], [4, 5, 6]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10], [20, 30], [40, 50, 60], [70, 80, 90, 100], [110, 120, 130, 140, 150]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10], [20, 30], [40, 50, 60], [70, 80, 90, 100], [110, 120, 130, 140, 150]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [9, 6], [4, 6, 8], [4, 2, 6, 5], [8, 4, 9, 6, 1]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [9, 6], [4, 6, 8], [4, 2, 6, 5], [8, 4, 9, 6, 1]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10000], [10000, -10000], [10000, 10000, 10000], [10000, -10000, 10000, -10000], [10000, 10000, 10000, 10000, 10000]]) == -10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10000], [10000, -10000], [10000, 10000, 10000], [10000, -10000, 10000, -10000], [10000, 10000, 10000, 10000, 10000]]) == -10000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [0, -2], [0, -1, 0], [-1, 0, -1, 0]]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [0, -2], [0, -1, 0], [-1, 0, -1, 0]]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [9, 4], [2, 6, 7], [4, 6, 8, 4], [9, 5, 2, 1, 3]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [9, 4], [2, 6, 7], [4, 6, 8, 4], [9, 5, 2, 1, 3]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 1], [1, 2, 3], [4, 1, 2, 3], [3, 4, 1, 2, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 1], [1, 2, 3], [4, 1, 2, 3], [3, 4, 1, 2, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [-2, -3], [-4, -5, -6], [-7, -8, -9, -10], [-11, -12, -13, -14, -15]]) == -35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [-2, -3], [-4, -5, -6], [-7, -8, -9, -10], [-11, -12, -13, -14, -15]]) == -35: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [0, -1], [0, 0, -1], [0, 0, 0, -1], [0, 0, 0, 0, -1]]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [0, -1], [0, 0, -1], [0, 0, 0, -1], [0, 0, 0, 0, -1]]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [-1, -2], [-1, -2, -3], [-1, -2, -3, -4], [-1, -2, -3, -4, -5]]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [-1, -2], [-1, -2, -3], [-1, -2, -3, -4], [-1, -2, -3, -4, -5]]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [-2, 3], [-4, 5, -6], [-7, -8, 9, 10], [-11, 12, -13, 14, -15]]) == -26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [-2, 3], [-4, 5, -6], [-7, -8, 9, 10], [-11, 12, -13, 14, -15]]) == -26: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 1], [3, 3, 2], [4, 6, 5, 4], [5, 7, 9, 8, 5]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 1], [3, 3, 2], [4, 6, 5, 4], [5, 7, 9, 8, 5]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[100], [90, 110], [80, 90, 100], [70, 80, 90, 100], [60, 70, 80, 90, 100]]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[100], [90, 110], [80, 90, 100], [70, 80, 90, 100], [60, 70, 80, 90, 100]]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 3], [1, 1, 1], [3, 2, 1, 4], [4, 5, 2, 3, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 3], [1, 1, 1], [3, 2, 1, 4], [4, 5, 2, 3, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10000], [9999, 10001], [-10000, 10000, 10000], [10000, 10000, 10000, 10000], [0, 0, 0, 0, 0]]) == 19999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10000], [9999, 10001], [-10000, 10000, 10000], [10000, 10000, 10000, 10000], [0, 0, 0, 0, 0]]) == 19999: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-5], [3, -8], [6, -7, -4], [2, -6, 5, -7], [8, -4, -3, 5, -2]]) == -30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-5], [3, -8], [6, -7, -4], [2, -6, 5, -7], [8, -4, -3, 5, -2]]) == -30: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-7], [10, -3], [-6, 1, -4], [6, -5, 8, -6], [4, 3, -6, 2, -5]]) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-7], [10, -3], [-6, 1, -4], [6, -5, 8, -6], [4, 3, -6, 2, -5]]) == -25: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10000], [10000, -10000], [0, 0, 0], [10000, 10000, -10000, -10000], [10000, -10000, 10000, -10000, 10000]]) == -40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10000], [10000, -10000], [0, 0, 0], [10000, 10000, -10000, -10000], [10000, -10000, 10000, -10000, 10000]]) == -40000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [-2, -2], [-3, -3, -3], [-4, -4, -4, -4], [-5, -5, -5, -5, -5], [-6, -6, -6, -6, -6, -6]]) == -21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [-2, -2], [-3, -3, -3], [-4, -4, -4, -4], [-5, -5, -5, -5, -5], [-6, -6, -6, -6, -6, -6]]) == -21: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [4, 4], [3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [4, 4], [3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [9, 6], [4, 6, 8], [4, 2, 6, 5], [4, 4, 1, 7, 6]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [9, 6], [4, 6, 8], [4, 2, 6, 5], [4, 4, 1, 7, 6]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[9999], [9998, 9999], [9997, 9998, 9999], [9996, 9997, 9998, 9999]]) == 39990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[9999], [9998, 9999], [9997, 9998, 9999], [9996, 9997, 9998, 9999]]) == 39990: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-9999], [-9998, -9999], [-9997, -9998, -9999], [-9996, -9997, -9998, -9999]]) == -39996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-9999], [-9998, -9999], [-9997, -9998, -9999], [-9996, -9997, -9998, -9999]]) == -39996: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [0, -1], [-1, 0, -1], [-1, -1, 0, -1]]) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [0, -1], [-1, 0, -1], [-1, -1, 0, -1]]) == -4: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-100], [100, -200], [300, -400, 500], [-600, 700, -800, 900], [1000, -1100, 1200, -1300, 1400]]) == -2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-100], [100, -200], [300, -400, 500], [-600, 700, -800, 900], [1000, -1100, 1200, -1300, 1400]]) == -2800: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [3, 4], [1, 6, 5], [9, 4, 3, 8], [8, 9, 6, 4, 5]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [3, 4], [1, 6, 5], [9, 4, 3, 8], [8, 9, 6, 4, 5]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10], [10, -20], [20, 30, -40], [-40, 50, 60, 70], [-70, 80, -90, 100, 110]]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10], [10, -20], [20, 30, -40], [-40, 50, 60, 70], [-70, 80, -90, 100, 110]]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [9, 2], [8, 7, 3], [6, 5, 4, 9], [5, 7, 8, 4, 6], [1, 5, 6, 7, 2, 3]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [9, 2], [8, 7, 3], [6, 5, 4, 9], [5, 7, 8, 4, 6], [1, 5, 6, 7, 2, 3]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-100], [200, -300], [400, -500, 600], [-700, 800, -900, 1000], [-1100, 1200, -1300, 1400, -1500]]) == -3100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-100], [200, -300], [400, -500, 600], [-700, 800, -900, 1000], [-1100, 1200, -1300, 1400, -1500]]) == -3100: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10], [-10, 20], [-20, 30, 40], [-30, 40, 50, 60], [-40, 50, 60, 70, 80]]) == -90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10], [-10, 20], [-20, 30, 40], [-30, 40, 50, 60], [-40, 50, 60, 70, 80]]) == -90: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10], [5, 3], [2, 3, 4], [7, 1, 0, 2], [6, 3, 2, 5, 4]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10], [5, 3], [2, 3, 4], [7, 1, 0, 2], [6, 3, 2, 5, 4]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [3, -2], [1, -4, 7], [-8, 2, 3, -1], [1, -1, 2, -2, 3]]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [3, -2], [1, -4, 7], [-8, 2, 3, -1], [1, -1, 2, -2, 3]]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1000], [-500, 2500], [-200, 1000, -750], [-1000, 500, -250, 1000], [-750, 1250, -375, 625, -1000]]) == -3450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1000], [-500, 2500], [-200, 1000, -750], [-1000, 500, -250, 1000], [-750, 1250, -375, 625, -1000]]) == -3450: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [2, 3], [-4, 5, 6], [7, -8, 9, 10], [-11, 12, -13, 14, 15], [16, -17, 18, -19, 20, 21]]) == -43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [2, 3], [-4, 5, 6], [7, -8, 9, 10], [-11, 12, -13, 14, 15], [16, -17, 18, -19, 20, 21]]) == -43: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10], [9, 11], [7, 15, 12], [4, 8, 10, 13], [6, 7, 12, 7, 8]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10], [9, 11], [7, 15, 12], [4, 8, 10, 13], [6, 7, 12, 7, 8]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9, -10], [-11, -12, -13, -14, -15]]) == -29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9, -10], [-11, -12, -13, -14, -15]]) == -29: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1000], [-500, 500], [-250, 0, 250], [-125, -50, 50, 125], [-62, -25, 0, 25, 62]]) == -1937
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1000], [-500, 500], [-250, 0, 250], [-125, -50, 50, 125], [-62, -25, 0, 25, 62]]) == -1937: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [1, -1], [2, -2, 2], [-3, 3, -3, 3], [4, -4, 4, -4, 4]]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [1, -1], [2, -2, 2], [-3, 3, -3, 3], [4, -4, 4, -4, 4]]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-5000], [-4000, 4000], [-3000, -2000, 3000], [-1000, 0, 2000, -3000], [-4000, 1000, -2000, 3000, 4000]]) == -17000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-5000], [-4000, 4000], [-3000, -2000, 3000], [-1000, 0, 2000, -3000], [-4000, 1000, -2000, 3000, 4000]]) == -17000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-100], [100, -200], [300, -400, 500], [1000, -1000, 1000, -1000], [2000, -2000, 2000, -2000, 2000]]) == -3700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-100], [100, -200], [300, -400, 500], [1000, -1000, 1000, -1000], [2000, -2000, 2000, -2000, 2000]]) == -3700: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10000], [-10000, 10000], [-10000, -10000, -10000], [-10000, -10000, -10000, -10000]]) == -20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10000], [-10000, 10000], [-10000, -10000, -10000], [-10000, -10000, -10000, -10000]]) == -20000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [7, 8, 4, 5, 9]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [7, 8, 4, 5, 9]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[9999], [10000, 9999], [10000, 10000, 9999], [10000, 10000, 10000, 9999], [10000, 10000, 10000, 10000, 9999]]) == 49995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[9999], [10000, 9999], [10000, 10000, 9999], [10000, 10000, 10000, 9999], [10000, 10000, 10000, 10000, 9999]]) == 49995: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-5], [-2, -3], [-1, -2, -4], [3, 2, -1, -1], [-1, -2, -3, -4, -5]]) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-5], [-2, -3], [-1, -2, -4], [3, 2, -1, -1], [-1, -2, -3, -4, -5]]) == -18: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10], [100, -200], [300, 400, -500], [-600, 700, -800, 900]]) == -1510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10], [100, -200], [300, 400, -500], [-600, 700, -800, 900]]) == -1510: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10], [20, 30], [-10, -20, -30], [40, 50, 60, 70], [-80, -90, -100, -110, -120]]) == -60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10], [20, 30], [-10, -20, -30], [40, 50, 60, 70], [-80, -90, -100, -110, -120]]) == -60: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10000], [-9000, -9000], [-8000, -8000, -8000], [-7000, -7000, -7000, -7000], [-6000, -6000, -6000, -6000, -6000]]) == -40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10000], [-9000, -9000], [-8000, -8000, -8000], [-7000, -7000, -7000, -7000], [-6000, -6000, -6000, -6000, -6000]]) == -40000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[100], [-50, 100], [-25, 50, -75], [20, -20, 20, -20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[100], [-50, 100], [-25, 50, -75], [20, -20, 20, -20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10000], [9999, -9999], [9998, -9998, -9998], [9997, -9997, -9997, -9997]]) == -19994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10000], [9999, -9999], [9998, -9998, -9998], [9997, -9997, -9997, -9997]]) == -19994: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10000], [10000, 10000], [10000, 10000, 10000], [10000, 10000, 10000, 10000], [10000, 10000, 10000, 10000, 10000]]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10000], [10000, 10000], [10000, 10000, 10000], [10000, 10000, 10000, 10000], [10000, 10000, 10000, 10000, 10000]]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[100], [200, 300], [400, 500, 600], [700, 800, 900, 1000], [1100, 1200, 1300, 1400, 1500], [1600, 1700, 1800, 1900, 2000, 2100]]) == 4100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[100], [200, 300], [400, 500, 600], [700, 800, 900, 1000], [1100, 1200, 1300, 1400, 1500], [1600, 1700, 1800, 1900, 2000, 2100]]) == 4100: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[5], [3, 8], [6, 7, 4], [2, 6, 5, 7], [8, 4, 3, 5, 2]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[5], [3, 8], [6, 7, 4], [2, 6, 5, 7], [8, 4, 3, 5, 2]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1, 2, 3], [4, 5, -6], [7, -8, 9, 10], [11, 12, 13, -14, 15]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1, 2, 3], [4, 5, -6], [7, -8, 9, 10], [11, 12, 13, -14, 15]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1], [1, 9999], [9999, 9999, 9999], [9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999]]) == 29999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1], [1, 9999], [9999, 9999, 9999], [9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999]]) == 29999: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-100], [-50, 20], [-15, -25, 30], [-5, -10, 15, 20], [10, 20, 30, -40, -50]]) == -200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-100], [-50, 20], [-15, -25, 30], [-5, -10, 15, 20], [10, 20, 30, -40, -50]]) == -200: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-5], [10, -4], [-6, 1, -5], [7, -8, 9, -2], [4, 3, -7, 2, -6], [1, 5, 6, 7, 2, -3]]) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-5], [10, -4], [-6, 1, -5], [7, -8, 9, -2], [4, 3, -7, 2, -6], [1, 5, 6, 7, 2, -3]]) == -25: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[0], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[0], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10000], [10000, -9999], [9998, -9997, 9996], [9995, -9994, 9993, -9992], [9991, -9990, 9989, -9988, 9987]]) == -49980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10000], [10000, -9999], [9998, -9997, 9996], [9995, -9994, 9993, -9992], [9991, -9990, 9989, -9988, 9987]]) == -49980: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-10000], [10000, -10000], [10000, -10000, 10000], [-10000, 10000, -10000, 10000]]) == -40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-10000], [10000, -10000], [10000, -10000, 10000], [-10000, 10000, -10000, 10000]]) == -40000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[100], [101, 102], [103, 104, 105], [106, 107, 108, 109], [110, 111, 112, 113, 114]]) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[100], [101, 102], [103, 104, 105], [106, 107, 108, 109], [110, 111, 112, 113, 114]]) == 520: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35]]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35]]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [0, -2], [1, 2, -3], [0, -1, 2, 3], [-1, 0, 2, -2, 3]]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [0, -2], [1, 2, -3], [0, -1, 2, 3], [-1, 0, 2, -2, 3]]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-100], [-200, -300], [-400, -500, -600], [-700, -800, -900, -1000]]) == -2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-100], [-200, -300], [-400, -500, -600], [-700, -800, -900, -1000]]) == -2000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[10000], [-10000, 10000], [-10000, -10000, 10000], [10000, 10000, -10000, 10000]]) == -20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[10000], [-10000, 10000], [-10000, -10000, 10000], [10000, 10000, -10000, 10000]]) == -20000: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[100], [-200, 300], [-400, 500, 600], [-700, 800, -900, 1000], [-1100, 1200, 1300, 1400, 1500]]) == -2300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[100], [-200, 300], [-400, 500, 600], [-700, 800, -900, 1000], [-1100, 1200, 1300, 1400, 1500]]) == -2300: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1000], [1000, -1000], [500, -500, 500], [250, -250, 250, -250]]) == -2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1000], [1000, -1000], [500, -500, 500], [250, -250, 250, -250]]) == -2750: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-5], [-4, -6], [-3, -6, -9], [-2, -6, -9, -12], [-1, -6, -9, -12, -15]]) == -47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-5], [-4, -6], [-3, -6, -9], [-2, -6, -9, -12], [-1, -6, -9, -12, -15]]) == -47: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-100], [-200, 150], [-50, -100, -150], [200, 300, 400, 500]]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-100], [-200, 150], [-50, -100, -150], [200, 300, 400, 500]]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(triangle = [[-1], [2, 3], [-4, -5, -6], [-7, 8, -9, 10], [-11, -12, 13, -14, 15]]) == -27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(triangle = [[-1], [2, 3], [-4, -5, -6], [-7, 8, -9, 10], [-11, -12, 13, -14, 15]]) == -27: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(triangle = [[-10]]) == -10
    assert candidate(triangle = [[-1], [2, 3], [1, -1, -3], [-2, 1, -1, -2]]) == -3
    assert candidate(triangle = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]) == 10
    assert candidate(triangle = [[-1], [2, -2], [3, -3, 3], [-4, -4, 4, 4]]) == -10
    assert candidate(triangle = [[-1], [2, 3], [1, -1, -3]]) == -1
    assert candidate(triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert candidate(triangle = [[0], [1, 0], [1, 1, 1], [1, 2, 3, 4]]) == 3
    assert candidate(triangle = [[0], [-1, -2], [-3, -4, -5]]) == -7
    assert candidate(triangle = [[0], [10000, -10000], [10000, 10000, 10000]]) == 0
    assert candidate(triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 16
    assert candidate(triangle = [[-1], [2, -3], [4, -5, 6], [-7, 8, -9, 10]]) == -18
    assert candidate(triangle = [[1], [2, 3], [4, 5, 6]]) == 7
    assert candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) == 14
    assert candidate(triangle = [[10], [20, 30], [40, 50, 60], [70, 80, 90, 100], [110, 120, 130, 140, 150]]) == 250
    assert candidate(triangle = [[5], [9, 6], [4, 6, 8], [4, 2, 6, 5], [8, 4, 9, 6, 1]]) == 23
    assert candidate(triangle = [[-10000], [10000, -10000], [10000, 10000, 10000], [10000, -10000, 10000, -10000], [10000, 10000, 10000, 10000, 10000]]) == -10000
    assert candidate(triangle = [[-1], [0, -2], [0, -1, 0], [-1, 0, -1, 0]]) == -5
    assert candidate(triangle = [[5], [9, 4], [2, 6, 7], [4, 6, 8, 4], [9, 5, 2, 1, 3]]) == 21
    assert candidate(triangle = [[1], [2, 1], [1, 2, 3], [4, 1, 2, 3], [3, 4, 1, 2, 3]]) == 6
    assert candidate(triangle = [[-1], [-2, -3], [-4, -5, -6], [-7, -8, -9, -10], [-11, -12, -13, -14, -15]]) == -35
    assert candidate(triangle = [[-1], [0, -1], [0, 0, -1], [0, 0, 0, -1], [0, 0, 0, 0, -1]]) == -5
    assert candidate(triangle = [[-1], [-1, -2], [-1, -2, -3], [-1, -2, -3, -4], [-1, -2, -3, -4, -5]]) == -15
    assert candidate(triangle = [[1], [-2, 3], [-4, 5, -6], [-7, -8, 9, 10], [-11, 12, -13, 14, -15]]) == -26
    assert candidate(triangle = [[1], [2, 1], [3, 3, 2], [4, 6, 5, 4], [5, 7, 9, 8, 5]]) == 13
    assert candidate(triangle = [[100], [90, 110], [80, 90, 100], [70, 80, 90, 100], [60, 70, 80, 90, 100]]) == 400
    assert candidate(triangle = [[1], [2, 3], [1, 1, 1], [3, 2, 1, 4], [4, 5, 2, 3, 1]]) == 7
    assert candidate(triangle = [[10000], [9999, 10001], [-10000, 10000, 10000], [10000, 10000, 10000, 10000], [0, 0, 0, 0, 0]]) == 19999
    assert candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8]]) == 36
    assert candidate(triangle = [[-5], [3, -8], [6, -7, -4], [2, -6, 5, -7], [8, -4, -3, 5, -2]]) == -30
    assert candidate(triangle = [[-7], [10, -3], [-6, 1, -4], [6, -5, 8, -6], [4, 3, -6, 2, -5]]) == -25
    assert candidate(triangle = [[-10000], [10000, -10000], [0, 0, 0], [10000, 10000, -10000, -10000], [10000, -10000, 10000, -10000, 10000]]) == -40000
    assert candidate(triangle = [[-1], [-2, -2], [-3, -3, -3], [-4, -4, -4, -4], [-5, -5, -5, -5, -5], [-6, -6, -6, -6, -6, -6]]) == -21
    assert candidate(triangle = [[5], [4, 4], [3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 15
    assert candidate(triangle = [[5], [9, 6], [4, 6, 8], [4, 2, 6, 5], [4, 4, 1, 7, 6]]) == 20
    assert candidate(triangle = [[9999], [9998, 9999], [9997, 9998, 9999], [9996, 9997, 9998, 9999]]) == 39990
    assert candidate(triangle = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 17
    assert candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 25
    assert candidate(triangle = [[-9999], [-9998, -9999], [-9997, -9998, -9999], [-9996, -9997, -9998, -9999]]) == -39996
    assert candidate(triangle = [[-1], [0, -1], [-1, 0, -1], [-1, -1, 0, -1]]) == -4
    assert candidate(triangle = [[-100], [100, -200], [300, -400, 500], [-600, 700, -800, 900], [1000, -1100, 1200, -1300, 1400]]) == -2800
    assert candidate(triangle = [[5], [3, 4], [1, 6, 5], [9, 4, 3, 8], [8, 9, 6, 4, 5]]) == 19
    assert candidate(triangle = [[-10], [10, -20], [20, 30, -40], [-40, 50, 60, 70], [-70, 80, -90, 100, 110]]) == -100
    assert candidate(triangle = [[1], [9, 2], [8, 7, 3], [6, 5, 4, 9], [5, 7, 8, 4, 6], [1, 5, 6, 7, 2, 3]]) == 16
    assert candidate(triangle = [[-100], [200, -300], [400, -500, 600], [-700, 800, -900, 1000], [-1100, 1200, -1300, 1400, -1500]]) == -3100
    assert candidate(triangle = [[10], [-10, 20], [-20, 30, 40], [-30, 40, 50, 60], [-40, 50, 60, 70, 80]]) == -90
    assert candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]]) == 21
    assert candidate(triangle = [[10], [5, 3], [2, 3, 4], [7, 1, 0, 2], [6, 3, 2, 5, 4]]) == 18
    assert candidate(triangle = [[-1], [3, -2], [1, -4, 7], [-8, 2, 3, -1], [1, -1, 2, -2, 3]]) == -6
    assert candidate(triangle = [[-1000], [-500, 2500], [-200, 1000, -750], [-1000, 500, -250, 1000], [-750, 1250, -375, 625, -1000]]) == -3450
    assert candidate(triangle = [[-1], [2, 3], [-4, 5, 6], [7, -8, 9, 10], [-11, 12, -13, 14, 15], [16, -17, 18, -19, 20, 21]]) == -43
    assert candidate(triangle = [[10], [9, 11], [7, 15, 12], [4, 8, 10, 13], [6, 7, 12, 7, 8]]) == 36
    assert candidate(triangle = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 15
    assert candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]) == 15
    assert candidate(triangle = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9, -10], [-11, -12, -13, -14, -15]]) == -29
    assert candidate(triangle = [[-1000], [-500, 500], [-250, 0, 250], [-125, -50, 50, 125], [-62, -25, 0, 25, 62]]) == -1937
    assert candidate(triangle = [[0], [1, -1], [2, -2, 2], [-3, 3, -3, 3], [4, -4, 4, -4, 4]]) == -10
    assert candidate(triangle = [[0], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]) == 4
    assert candidate(triangle = [[-5000], [-4000, 4000], [-3000, -2000, 3000], [-1000, 0, 2000, -3000], [-4000, 1000, -2000, 3000, 4000]]) == -17000
    assert candidate(triangle = [[-100], [100, -200], [300, -400, 500], [1000, -1000, 1000, -1000], [2000, -2000, 2000, -2000, 2000]]) == -3700
    assert candidate(triangle = [[10000], [-10000, 10000], [-10000, -10000, -10000], [-10000, -10000, -10000, -10000]]) == -20000
    assert candidate(triangle = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [7, 8, 4, 5, 9]]) == 23
    assert candidate(triangle = [[9999], [10000, 9999], [10000, 10000, 9999], [10000, 10000, 10000, 9999], [10000, 10000, 10000, 10000, 9999]]) == 49995
    assert candidate(triangle = [[-5], [-2, -3], [-1, -2, -4], [3, 2, -1, -1], [-1, -2, -3, -4, -5]]) == -18
    assert candidate(triangle = [[-10], [100, -200], [300, 400, -500], [-600, 700, -800, 900]]) == -1510
    assert candidate(triangle = [[-10], [20, 30], [-10, -20, -30], [40, 50, 60, 70], [-80, -90, -100, -110, -120]]) == -60
    assert candidate(triangle = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]]) == 45
    assert candidate(triangle = [[-10000], [-9000, -9000], [-8000, -8000, -8000], [-7000, -7000, -7000, -7000], [-6000, -6000, -6000, -6000, -6000]]) == -40000
    assert candidate(triangle = [[100], [-50, 100], [-25, 50, -75], [20, -20, 20, -20]]) == 5
    assert candidate(triangle = [[10000], [9999, -9999], [9998, -9998, -9998], [9997, -9997, -9997, -9997]]) == -19994
    assert candidate(triangle = [[10000], [10000, 10000], [10000, 10000, 10000], [10000, 10000, 10000, 10000], [10000, 10000, 10000, 10000, 10000]]) == 50000
    assert candidate(triangle = [[100], [200, 300], [400, 500, 600], [700, 800, 900, 1000], [1100, 1200, 1300, 1400, 1500], [1600, 1700, 1800, 1900, 2000, 2100]]) == 4100
    assert candidate(triangle = [[5], [3, 8], [6, 7, 4], [2, 6, 5, 7], [8, 4, 3, 5, 2]]) == 20
    assert candidate(triangle = [[-1, 2, 3], [4, 5, -6], [7, -8, 9, 10], [11, 12, 13, -14, 15]]) == -1
    assert candidate(triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21]]) == 41
    assert candidate(triangle = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 7
    assert candidate(triangle = [[1], [1, 9999], [9999, 9999, 9999], [9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999]]) == 29999
    assert candidate(triangle = [[-100], [-50, 20], [-15, -25, 30], [-5, -10, 15, 20], [10, 20, 30, -40, -50]]) == -200
    assert candidate(triangle = [[-5], [10, -4], [-6, 1, -5], [7, -8, 9, -2], [4, 3, -7, 2, -6], [1, 5, 6, 7, 2, -3]]) == -25
    assert candidate(triangle = [[0], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 5
    assert candidate(triangle = [[-10000], [10000, -9999], [9998, -9997, 9996], [9995, -9994, 9993, -9992], [9991, -9990, 9989, -9988, 9987]]) == -49980
    assert candidate(triangle = [[-10000], [10000, -10000], [10000, -10000, 10000], [-10000, 10000, -10000, 10000]]) == -40000
    assert candidate(triangle = [[100], [101, 102], [103, 104, 105], [106, 107, 108, 109], [110, 111, 112, 113, 114]]) == 520
    assert candidate(triangle = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35]]) == 65
    assert candidate(triangle = [[-1], [0, -2], [1, 2, -3], [0, -1, 2, 3], [-1, 0, 2, -2, 3]]) == -6
    assert candidate(triangle = [[-100], [-200, -300], [-400, -500, -600], [-700, -800, -900, -1000]]) == -2000
    assert candidate(triangle = [[10000], [-10000, 10000], [-10000, -10000, 10000], [10000, 10000, -10000, 10000]]) == -20000
    assert candidate(triangle = [[100], [-200, 300], [-400, 500, 600], [-700, 800, -900, 1000], [-1100, 1200, 1300, 1400, 1500]]) == -2300
    assert candidate(triangle = [[-1000], [1000, -1000], [500, -500, 500], [250, -250, 250, -250]]) == -2750
    assert candidate(triangle = [[-5], [-4, -6], [-3, -6, -9], [-2, -6, -9, -12], [-1, -6, -9, -12, -15]]) == -47
    assert candidate(triangle = [[-100], [-200, 150], [-50, -100, -150], [200, 300, 400, 500]]) == -150
    assert candidate(triangle = [[-1], [2, 3], [-4, -5, -6], [-7, 8, -9, 10], [-11, -12, 13, -14, 15]]) == -27


