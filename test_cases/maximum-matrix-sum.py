def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2], [3, 4]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2], [3, 4]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, -4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, -4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, 4]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, 4]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100000, -100000], [-100000, 100000]]) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100000, -100000], [-100000, 100000]]) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, -1], [0, 1, 0], [-1, 0, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, -1], [0, 1, 0], [-1, 0, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -2], [-3, 4]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -2], [-3, 4]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1], [-1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1], [-1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-20, 15, 30], [5, -25, 40], [-10, 25, -35]]) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-20, 15, 30], [5, -25, 40], [-10, 25, -35]]) == 205: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, -100000, 100000, 0], [100000, 0, 0, -100000], [0, 100000, 0, -100000], [-100000, 0, 100000, 0]]) == 800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, -100000, 100000, 0], [100000, 0, 0, -100000], [0, 100000, 0, -100000], [-100000, 0, 100000, 0]]) == 800000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3, -4], [5, 6, 7, 8], [-9, -10, -11, -12], [13, 14, 15, 16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3, -4], [5, 6, 7, 8], [-9, -10, -11, -12], [13, 14, 15, 16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100000, 0, 0], [0, 0, 0], [0, 0, -100000]]) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100000, 0, 0], [0, 0, 0], [0, 0, -100000]]) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 1], [0, -2, 0], [1, 0, -1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 1], [0, -2, 0], [1, 0, -1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1], [-1, 1], [1, -1], [-1, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1], [-1, 1], [1, -1], [-1, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20, 30], [-40, -50, -60], [70, 80, 90]]) == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20, 30], [-40, -50, -60], [70, 80, 90]]) == 430: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [13, -14, 15, -16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [13, -14, 15, -16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, -25]]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, -25]]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000, -1000, 1000, -1000], [1000, -1000, 1000, -1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000]]) == 16000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000, -1000, 1000, -1000], [1000, -1000, 1000, -1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000]]) == 16000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -2, 3, -4, 5], [-6, 7, -8, 9, -10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, -20], [21, -22, 23, -24, 25]]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -2, 3, -4, 5], [-6, 7, -8, 9, -10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, -20], [21, -22, 23, -24, 25]]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -1, 1, 1], [1, 1, -1, -1], [-1, -1, 1, 1], [1, 1, -1, -1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -1, 1, 1], [1, 1, -1, -1], [-1, -1, 1, 1], [1, 1, -1, -1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 1, -1, 1], [-1, 1, -1, 1], [-1, 1, -1, 1], [-1, 1, -1, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 1, -1, 1], [-1, 1, -1, 1], [-1, 1, -1, 1], [-1, 1, -1, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5]]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5]]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10000, 20000, -30000], [40000, -50000, 60000], [-70000, 80000, -90000]]) == 430000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10000, 20000, -30000], [40000, -50000, 60000], [-70000, 80000, -90000]]) == 430000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100000, 0, -100000, 0], [0, 100000, 0, -100000], [-100000, 0, 100000, 0], [0, -100000, 0, 100000]]) == 800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100000, 0, -100000, 0], [0, 100000, 0, -100000], [-100000, 0, 100000, 0], [0, -100000, 0, 100000]]) == 800000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, 3], [4, -5, 6], [-7, 8, -9]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, 3], [4, -5, 6], [-7, 8, -9]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100000, 100000, -100000], [100000, -100000, 100000], [-100000, 100000, -100000]]) == 700000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100000, 100000, -100000], [100000, -100000, 100000], [-100000, 100000, -100000]]) == 700000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9], [10, -11, 12], [-13, 14, -15]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9], [10, -11, 12], [-13, 14, -15]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-99999, 99999], [100000, -100000]]) == 399998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-99999, 99999], [100000, -100000]]) == 399998: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -20, -30, -40], [-50, -60, -70, -80], [-90, -100, -110, -120], [-130, -140, -150, -160]]) == 1360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -20, -30, -40], [-50, -60, -70, -80], [-90, -100, -110, -120], [-130, -140, -150, -160]]) == 1360: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100000, -100000], [-100000, -100000]]) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100000, -100000], [-100000, -100000]]) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100000, 100000], [-100000, 100000], [100000, -100000], [100000, -100000]]) == 800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100000, 100000], [-100000, 100000], [100000, -100000], [100000, -100000]]) == 800000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, 3, -2], [-1, 4, -6], [7, -8, 9]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, 3, -2], [-1, 4, -6], [7, -8, 9]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [-6, -7, -8, -9, -10], [11, 12, 13, 14, 15], [-16, -17, -18, -19, -20], [21, 22, 23, 24, 25]]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [-6, -7, -8, -9, -10], [11, 12, 13, 14, 15], [-16, -17, -18, -19, -20], [21, 22, 23, 24, 25]]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-50000, 50000, -60000], [60000, -70000, 70000], [-80000, 80000, -90000]]) == 510000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-50000, 50000, -60000], [60000, -70000, 70000], [-80000, 80000, -90000]]) == 510000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1, 2, -2, 3, -3], [4, -4, 5, -5, 6, -6], [7, -7, 8, -8, 9, -9]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1, 2, -2, 3, -3], [4, -4, 5, -5, 6, -6], [7, -7, 8, -8, 9, -9]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 323: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == 205: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20], [21, 22, 23, 24, 25]]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20], [21, 22, 23, 24, 25]]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -2, 3, -4, 5], [-6, 7, -8, 9, -10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, -20], [21, -22, 23, -24, 25]]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -2, 3, -4, 5], [-6, 7, -8, 9, -10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, -20], [21, -22, 23, -24, 25]]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-99999, 99998, -99997, 99996], [99995, -99994, 99993, -99992], [-99991, 99990, -99989, 99988], [99987, -99986, 99985, -99984]]) == 1599864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-99999, 99998, -99997, 99996], [99995, -99994, 99993, -99992], [-99991, 99990, -99989, 99988], [99987, -99986, 99985, -99984]]) == 1599864: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -20, -30], [-40, -50, -60], [-70, -80, -90]]) == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -20, -30], [-40, -50, -60], [-70, -80, -90]]) == 430: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10, -20, -30], [-40, -50, -60], [-70, -80, -90]]) == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10, -20, -30], [-40, -50, -60], [-70, -80, -90]]) == 430: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 1, 0, -1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-1, 0, 1, 0, -1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 1, 0, -1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-1, 0, 1, 0, -1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-99999, 100000, 99999], [-100000, -99999, 100000], [99999, -100000, -99999]]) == 699997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-99999, 100000, 99999], [-100000, -99999, 100000], [99999, -100000, -99999]]) == 699997: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1, 1, -1], [1, -1, 1, -1], [-1, 1, -1, 1], [-1, 1, -1, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1, 1, -1], [1, -1, 1, -1], [-1, 1, -1, 1], [-1, 1, -1, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]) == 223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]) == 223: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 0, 1], [-2, 0, 2], [-3, 0, 3]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 0, 1], [-2, 0, 2], [-3, 0, 3]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-10000, 10000, -10000, 10000, -10000], [10000, -10000, 10000, -10000, 10000], [-10000, 10000, -10000, 10000, -10000], [10000, -10000, 10000, -10000, 10000], [-10000, 10000, -10000, 10000, -10000]]) == 230000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-10000, 10000, -10000, 10000, -10000], [10000, -10000, 10000, -10000, 10000], [-10000, 10000, -10000, 10000, -10000], [10000, -10000, 10000, -10000, 10000], [-10000, 10000, -10000, 10000, -10000]]) == 230000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-100000, 100000, -100000, 100000], [100000, -100000, 100000, -100000], [-100000, 100000, -100000, 100000], [100000, -100000, 100000, -100000]]) == 1600000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-100000, 100000, -100000, 100000], [100000, -100000, 100000, -100000], [-100000, 100000, -100000, 100000], [100000, -100000, 100000, -100000]]) == 1600000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100, -100, 200], [-300, 400, -500], [600, -700, 800]]) == 3700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100, -100, 200], [-300, 400, -500], [600, -700, 800]]) == 3700: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-2, 3, -4], [-1, -2, -3], [4, 5, -6]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-2, 3, -4], [-1, -2, -3], [4, 5, -6]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, -1], [1, 0, -1], [-1, 1, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, -1], [1, 0, -1], [-1, 1, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100000, -100000, 100000], [-100000, 100000, -100000], [100000, -100000, 100000]]) == 900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100000, -100000, 100000], [-100000, 100000, -100000], [100000, -100000, 100000]]) == 900000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-5, -4, 3], [2, 1, 0], [-1, 6, -7]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-5, -4, 3], [2, 1, 0], [-1, 6, -7]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100000, 0, -100000], [-100000, 0, 100000], [0, 100000, 0]]) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100000, 0, -100000], [-100000, 0, 100000], [0, 100000, 0]]) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, -1, 2, -2], [3, -3, 4, -4], [5, -5, 6, -6], [7, -7, 8, -8]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, -1, 2, -2], [3, -3, 4, -4], [5, -5, 6, -6], [7, -7, 8, -8]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100, -200, 300, -400], [500, -600, 700, -800], [900, -1000, 1100, -1200], [-1300, 1400, -1500, 1600]]) == 13600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100, -200, 300, -400], [500, -600, 700, -800], [900, -1000, 1100, -1200], [-1300, 1400, -1500, 1600]]) == 13600: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 323: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100000, 100000], [100000, 100000]]) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100000, 100000], [100000, 100000]]) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == 136: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(matrix = [[-1, -2], [3, 4]]) == 10
    assert candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 43
    assert candidate(matrix = [[1, 2], [3, -4]]) == 8
    assert candidate(matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(matrix = [[1, 2], [3, 4]]) == 10
    assert candidate(matrix = [[100000, -100000], [-100000, 100000]]) == 400000
    assert candidate(matrix = [[1, 0, -1], [0, 1, 0], [-1, 0, 1]]) == 5
    assert candidate(matrix = [[1, -2], [-3, 4]]) == 10
    assert candidate(matrix = [[1, -1], [-1, 1]]) == 4
    assert candidate(matrix = [[-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]) == 160
    assert candidate(matrix = [[-1, 2, -3, 4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 136
    assert candidate(matrix = [[-20, 15, 30], [5, -25, 40], [-10, 25, -35]]) == 205
    assert candidate(matrix = [[0, -100000, 100000, 0], [100000, 0, 0, -100000], [0, 100000, 0, -100000], [-100000, 0, 100000, 0]]) == 800000
    assert candidate(matrix = [[-1, -2, -3, -4], [5, 6, 7, 8], [-9, -10, -11, -12], [13, 14, 15, 16]]) == 136
    assert candidate(matrix = [[100000, 0, 0], [0, 0, 0], [0, 0, -100000]]) == 200000
    assert candidate(matrix = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 25
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(matrix = [[-1, 0, 1], [0, -2, 0], [1, 0, -1]]) == 6
    assert candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 7
    assert candidate(matrix = [[1, -1], [-1, 1], [1, -1], [-1, 1]]) == 8
    assert candidate(matrix = [[10, 20, 30], [-40, -50, -60], [70, 80, 90]]) == 430
    assert candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [13, -14, 15, -16]]) == 136
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, -25]]) == 47
    assert candidate(matrix = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]) == 1
    assert candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 7
    assert candidate(matrix = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 25
    assert candidate(matrix = [[1000, -1000, 1000, -1000], [1000, -1000, 1000, -1000], [-1000, 1000, -1000, 1000], [-1000, 1000, -1000, 1000]]) == 16000
    assert candidate(matrix = [[1, -2, 3, -4, 5], [-6, 7, -8, 9, -10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, -20], [21, -22, 23, -24, 25]]) == 325
    assert candidate(matrix = [[-1, -1, 1, 1], [1, 1, -1, -1], [-1, -1, 1, 1], [1, 1, -1, -1]]) == 16
    assert candidate(matrix = [[-1, 1, -1, 1], [-1, 1, -1, 1], [-1, 1, -1, 1], [-1, 1, -1, 1]]) == 16
    assert candidate(matrix = [[-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5], [5, -4, 3, -2, 1], [-1, 2, -3, 4, -5]]) == 73
    assert candidate(matrix = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 136
    assert candidate(matrix = [[-10000, 20000, -30000], [40000, -50000, 60000], [-70000, 80000, -90000]]) == 430000
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]) == 5050
    assert candidate(matrix = [[100000, 0, -100000, 0], [0, 100000, 0, -100000], [-100000, 0, 100000, 0], [0, -100000, 0, 100000]]) == 800000
    assert candidate(matrix = [[-1, 2, 3], [4, -5, 6], [-7, 8, -9]]) == 45
    assert candidate(matrix = [[-100000, 100000, -100000], [100000, -100000, 100000], [-100000, 100000, -100000]]) == 700000
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == 136
    assert candidate(matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9], [10, -11, 12], [-13, 14, -15]]) == 120
    assert candidate(matrix = [[-99999, 99999], [100000, -100000]]) == 399998
    assert candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 136
    assert candidate(matrix = [[-10, -20, -30, -40], [-50, -60, -70, -80], [-90, -100, -110, -120], [-130, -140, -150, -160]]) == 1360
    assert candidate(matrix = [[-100000, -100000], [-100000, -100000]]) == 400000
    assert candidate(matrix = [[-100000, 100000], [-100000, 100000], [100000, -100000], [100000, -100000]]) == 800000
    assert candidate(matrix = [[-5, 3, -2], [-1, 4, -6], [7, -8, 9]]) == 43
    assert candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 43
    assert candidate(matrix = [[1, 2, 3, 4, 5], [-6, -7, -8, -9, -10], [11, 12, 13, 14, 15], [-16, -17, -18, -19, -20], [21, 22, 23, 24, 25]]) == 325
    assert candidate(matrix = [[-50000, 50000, -60000], [60000, -70000, 70000], [-80000, 80000, -90000]]) == 510000
    assert candidate(matrix = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 136
    assert candidate(matrix = [[1, -1, 2, -2, 3, -3], [4, -4, 5, -5, 6, -6], [7, -7, 8, -8, 9, -9]]) == 88
    assert candidate(matrix = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 323
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == 205
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20], [21, 22, 23, 24, 25]]) == 325
    assert candidate(matrix = [[1, -2, 3, -4, 5], [-6, 7, -8, 9, -10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, -20], [21, -22, 23, -24, 25]]) == 325
    assert candidate(matrix = [[-99999, 99998, -99997, 99996], [99995, -99994, 99993, -99992], [-99991, 99990, -99989, 99988], [99987, -99986, 99985, -99984]]) == 1599864
    assert candidate(matrix = [[-10, -20, -30], [-40, -50, -60], [-70, -80, -90]]) == 430
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
    assert candidate(matrix = [[-10, -20, -30], [-40, -50, -60], [-70, -80, -90]]) == 430
    assert candidate(matrix = [[-1, 0, 1, 0, -1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-1, 0, 1, 0, -1]]) == 13
    assert candidate(matrix = [[-99999, 100000, 99999], [-100000, -99999, 100000], [99999, -100000, -99999]]) == 699997
    assert candidate(matrix = [[1, -1, 1, -1], [1, -1, 1, -1], [-1, 1, -1, 1], [-1, 1, -1, 1]]) == 16
    assert candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]) == 450
    assert candidate(matrix = [[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]) == 223
    assert candidate(matrix = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]) == 9
    assert candidate(matrix = [[-1, 0, 1], [-2, 0, 2], [-3, 0, 3]]) == 12
    assert candidate(matrix = [[-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1]]) == 36
    assert candidate(matrix = [[-10000, 10000, -10000, 10000, -10000], [10000, -10000, 10000, -10000, 10000], [-10000, 10000, -10000, 10000, -10000], [10000, -10000, 10000, -10000, 10000], [-10000, 10000, -10000, 10000, -10000]]) == 230000
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 25
    assert candidate(matrix = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]]) == 16
    assert candidate(matrix = [[-100000, 100000, -100000, 100000], [100000, -100000, 100000, -100000], [-100000, 100000, -100000, 100000], [100000, -100000, 100000, -100000]]) == 1600000
    assert candidate(matrix = [[100, -100, 200], [-300, 400, -500], [600, -700, 800]]) == 3700
    assert candidate(matrix = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 325
    assert candidate(matrix = [[-2, 3, -4], [-1, -2, -3], [4, 5, -6]]) == 30
    assert candidate(matrix = [[0, 1, -1], [1, 0, -1], [-1, 1, 0]]) == 6
    assert candidate(matrix = [[100000, -100000, 100000], [-100000, 100000, -100000], [100000, -100000, 100000]]) == 900000
    assert candidate(matrix = [[-5, -4, 3], [2, 1, 0], [-1, 6, -7]]) == 29
    assert candidate(matrix = [[100000, 0, -100000], [-100000, 0, 100000], [0, 100000, 0]]) == 500000
    assert candidate(matrix = [[1, -1, 2, -2], [3, -3, 4, -4], [5, -5, 6, -6], [7, -7, 8, -8]]) == 72
    assert candidate(matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 1
    assert candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 136
    assert candidate(matrix = [[100, -200, 300, -400], [500, -600, 700, -800], [900, -1000, 1100, -1200], [-1300, 1400, -1500, 1600]]) == 13600
    assert candidate(matrix = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20], [-21, 22, -23, 24, -25]]) == 323
    assert candidate(matrix = [[100000, 100000], [100000, 100000]]) == 400000
    assert candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == 136


