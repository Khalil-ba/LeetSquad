def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10]],k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10]],k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100000000, 100000000], [200000000, 200000000], [300000000, 300000000]],k = 100000000) == 600000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100000000, 100000000], [200000000, 200000000], [300000000, 300000000]],k = 100000000) == 600000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 3], [4, 7], [8, 10]],k = 6) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 3], [4, 7], [8, 10]],k = 6) == 21: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10], [7, 5]],k = 4) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10], [7, 5]],k = 4) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10]],k = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10]],k = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4]],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4]],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [-2, 2], [-3, 3]],k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [-2, 2], [-3, 3]],k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 5], [0, 0], [10, 10], [20, -5]],k = 25) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 5], [0, 0], [10, 10], [20, -5]],k = 25) == 35: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, -10], [0, 0], [10, 10]],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, -10], [0, 0], [10, 10]],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [100000000, 1]],k = 200000000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [100000000, 1]],k = 200000000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 3], [5, 5]],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 3], [5, 5]],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [3, 0], [9, 2]],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [3, 0], [9, 2]],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 2], [-3, 3], [1, 3], [2, 4]],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 2], [-3, 3], [1, 3], [2, 4]],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 20], [-10, 15], [-5, 10], [0, 5], [5, 0], [10, -5], [15, -10]],k = 12) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 20], [-10, 15], [-5, 10], [0, 5], [5, 0], [10, -5], [15, -10]],k = 12) == 30: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996], [6, 99999995]],k = 4) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996], [6, 99999995]],k = 4) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 100000000], [3, 1], [4, 100000000], [5, 1]],k = 1) == 100000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 100000000], [3, 1], [4, 100000000], [5, 1]],k = 1) == 100000002: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100000000, 100000000], [200000000, -200000000], [300000000, 300000000]],k = 150000000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100000000, 100000000], [200000000, -200000000], [300000000, 300000000]],k = 150000000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 4], [5, 7], [8, 10], [12, 13], [15, 14], [18, 15], [20, 16], [25, 17], [30, 18]],k = 15) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 4], [5, 7], [8, 10], [12, 13], [15, 14], [18, 15], [20, 16], [25, 17], [30, 18]],k = 15) == 47: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100000000, -100000000], [100000001, 100000000], [100000002, -100000000], [100000003, 100000000]],k = 4) == 200000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100000000, -100000000], [100000001, 100000000], [100000002, -100000000], [100000003, 100000000]],k = 4) == 200000002: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [4, 1], [8, 5], [15, 10], [20, 6], [25, 3]],k = 15) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [4, 1], [8, 5], [15, 10], [20, 6], [25, 3]],k = 15) == 27: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],k = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],k = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [4, 5], [7, 8], [10, 12], [13, 15], [16, 18]],k = 5) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [4, 5], [7, 8], [10, 12], [13, 15], [16, 18]],k = 5) == 36: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0], [7, -1], [8, -2], [9, -3], [10, -4]],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0], [7, -1], [8, -2], [9, -3], [10, -4]],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 2) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 2) == 30: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700]],k = 3) == 1301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700]],k = 3) == 1301: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [5, 10], [8, 15], [10, 7], [12, 20], [16, 5], [20, 25]],k = 10) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [5, 10], [8, 15], [10, 7], [12, 20], [16, 5], [20, 25]],k = 10) == 53: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10], [11, -11], [12, -12], [13, -13], [14, -14], [15, -15], [16, -16], [17, -17], [18, -18], [19, -19], [20, -20]],k = 5) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10], [11, -11], [12, -12], [13, -13], [14, -14], [15, -15], [16, -16], [17, -17], [18, -18], [19, -19], [20, -20]],k = 5) == -2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [0, 0], [1, -1], [2, 2], [3, -3], [4, 4], [5, -5], [6, 6]],k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [0, 0], [1, -1], [2, 2], [3, -3], [4, 4], [5, -5], [6, 6]],k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100], [5, 200], [10, 300], [15, 400], [20, 500], [25, 600], [30, 700]],k = 10) == 1305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100], [5, 200], [10, 300], [15, 400], [20, 500], [25, 600], [30, 700]],k = 10) == 1305: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10], [7, 2], [8, -5], [10, 4]],k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10], [7, 2], [8, -5], [10, 4]],k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [4, 2], [5, 3], [6, 5], [8, 6], [9, 7], [10, 8]],k = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [4, 2], [5, 3], [6, 5], [8, 6], [9, 7], [10, 8]],k = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10]],k = 5) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10]],k = 5) == -2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [2, -100000000], [3, 100000000], [4, -100000000], [5, 100000000], [6, -100000000], [7, 100000000], [8, -100000000], [9, 100000000], [10, -100000000]],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [2, -100000000], [3, 100000000], [4, -100000000], [5, 100000000], [6, -100000000], [7, 100000000], [8, -100000000], [9, 100000000], [10, -100000000]],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 5], [5, 3], [7, 9], [9, 4], [11, 10], [13, 6], [15, 8], [17, 2], [19, 12]],k = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 5], [5, 3], [7, 9], [9, 4], [11, 10], [13, 6], [15, 8], [17, 2], [19, 12]],k = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100000, -100000], [100005, 100000], [100010, -100000], [100015, 100000]],k = 10) == 200010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100000, -100000], [100005, 100000], [100010, -100000], [100015, 100000]],k = 10) == 200010: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [3, 20], [5, 15], [7, 5], [9, 25], [11, 30], [13, 10], [15, 35]],k = 15) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [3, 20], [5, 15], [7, 5], [9, 25], [11, 30], [13, 10], [15, 35]],k = 15) == 69: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, 10], [-2, 3], [0, 0], [3, -5], [7, 2], [8, -1], [10, 6]],k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, 10], [-2, 3], [0, 0], [3, -5], [7, 2], [8, -1], [10, 6]],k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 4], [6, 7], [8, 10], [11, 13], [15, 16], [18, 19]],k = 7) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 4], [6, 7], [8, 10], [11, 13], [15, 16], [18, 19]],k = 7) == 39: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100000000, -100000000], [200000000, -200000000], [300000000, 100000000], [400000000, 200000000]],k = 250000000) == 400000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100000000, -100000000], [200000000, -200000000], [300000000, 100000000], [400000000, 200000000]],k = 250000000) == 400000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-3, -3], [0, 0], [4, 4], [6, 6], [10, 10]],k = 6) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-3, -3], [0, 0], [4, 4], [6, 6], [10, 10]],k = 6) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-20, 20], [-18, 18], [-16, 16], [-14, 14], [-12, 12], [-10, 10], [-8, 8], [-6, 6], [-4, 4], [-2, 2]],k = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-20, 20], [-18, 18], [-16, 16], [-14, 14], [-12, 12], [-10, 10], [-8, 8], [-6, 6], [-4, 4], [-2, 2]],k = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100000000, -100000000], [-90000000, -90000000], [-80000000, -80000000], [-70000000, -70000000], [-60000000, -60000000], [-50000000, -50000000], [-40000000, -40000000], [-30000000, -30000000], [-20000000, -20000000], [-10000000, -10000000]],k = 20000000) == -20000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100000000, -100000000], [-90000000, -90000000], [-80000000, -80000000], [-70000000, -70000000], [-60000000, -60000000], [-50000000, -50000000], [-40000000, -40000000], [-30000000, -30000000], [-20000000, -20000000], [-10000000, -10000000]],k = 20000000) == -20000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996]],k = 1) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996]],k = 1) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [2, 50000000], [5, 10000000], [10, 5000000], [20, 1000000], [50, 500000], [100, 100000]],k = 99) == 150000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [2, 50000000], [5, 10000000], [10, 5000000], [20, 1000000], [50, 500000], [100, 100000]],k = 99) == 150000001: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -10], [-3, -7], [-1, -2], [1, 3], [4, 9]],k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -10], [-3, -7], [-1, -2], [1, 3], [4, 9]],k = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [4, 3], [6, 7], [8, 2], [10, 8]],k = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [4, 3], [6, 7], [8, 2], [10, 8]],k = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [3, 4], [7, 10], [8, 2], [10, 1]],k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [3, 4], [7, 10], [8, 2], [10, 1]],k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [4, 5], [6, 7], [8, 9], [10, 12], [12, 15], [14, 17], [16, 19], [18, 21], [20, 23]],k = 10) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [4, 5], [6, 7], [8, 9], [10, 12], [12, 15], [14, 17], [16, 19], [18, 21], [20, 23]],k = 10) == 46: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 15) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 15) == 29: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [-50000000, -100000000], [100000000, -100000000], [-100000000, 100000000]],k = 200000000) == 99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [-50000000, -100000000], [100000000, -100000000], [-100000000, 100000000]],k = 200000000) == 99999999: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 5], [6, 2], [8, 8], [10, 4], [15, 7], [20, 1]],k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 5], [6, 2], [8, 8], [10, 4], [15, 7], [20, 1]],k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [100000000, 1], [100000001, 2], [200000000, 3], [300000000, 4], [400000000, 5], [500000000, 6], [600000000, 7], [700000000, 8], [800000000, 9], [900000000, 10]],k = 100000000) == 200000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [100000000, 1], [100000001, 2], [200000000, 3], [300000000, 4], [400000000, 5], [500000000, 6], [600000000, 7], [700000000, 8], [800000000, 9], [900000000, 10]],k = 100000000) == 200000002: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1000000, -1000000], [-900000, -900000], [-800000, -800000], [-700000, -700000], [-600000, -600000]],k = 100000) == -1200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1000000, -1000000], [-900000, -900000], [-800000, -800000], [-700000, -700000], [-600000, -600000]],k = 100000) == -1200000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, 5], [0, 0], [1, 3], [3, -1], [5, 10], [6, -10], [8, 2], [10, 3], [15, 0]],k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, 5], [0, 0], [1, 3], [3, -1], [5, 10], [6, -10], [8, 2], [10, 3], [15, 0]],k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9]],k = 2) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9]],k = 2) == -2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [10, 10], [100, 100], [1000, 1000], [10000, 10000], [100000, 100000], [1000000, 1000000], [10000000, 10000000], [100000000, 100000000]],k = 50000000) == 20000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [10, 10], [100, 100], [1000, 1000], [10000, 10000], [100000, 100000], [1000000, 1000000], [10000000, 10000000], [100000000, 100000000]],k = 50000000) == 20000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100000, -100000], [100001, -99999], [100002, -99998], [100003, -99997], [100004, -99996]],k = 4) == -199992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100000, -100000], [100001, -99999], [100002, -99998], [100003, -99997], [100004, -99996]],k = 4) == -199992: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, -10], [-9, -9], [-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1]],k = 2) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, -10], [-9, -9], [-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1]],k = 2) == -2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],k = 3) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],k = 3) == 200: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [3, 7], [6, 8], [8, 6], [10, 9], [15, 1]],k = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [3, 7], [6, 8], [8, 6], [10, 9], [15, 1]],k = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-50, -50], [-25, -100], [0, 0], [25, 100], [50, 50]],k = 75) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-50, -50], [-25, -100], [0, 0], [25, 100], [50, 50]],k = 75) == 175: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],k = 3) == 1901
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],k = 3) == 1901: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 4], [3, 8], [4, 16], [5, 32]],k = 4) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 4], [3, 8], [4, 16], [5, 32]],k = 4) == 49: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 15], [5, 20], [8, 25], [10, 30], [15, 35], [20, 40], [25, 45], [30, 50], [35, 55]],k = 15) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 15], [5, 20], [8, 25], [10, 30], [15, 35], [20, 40], [25, 45], [30, 50], [35, 55]],k = 15) == 110: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-3, -1], [0, 0], [2, 4], [3, 6], [8, 8]],k = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-3, -1], [0, 0], [2, 4], [3, 6], [8, 8]],k = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [10, 2], [20, 3], [30, 4], [40, 5], [50, 6], [60, 7], [70, 8], [80, 9], [90, 10]],k = 15) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [10, 2], [20, 3], [30, 4], [40, 5], [50, 6], [60, 7], [70, 8], [80, 9], [90, 10]],k = 15) == 29: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100000000, 100000000], [-90000000, 90000000], [0, -50000000], [100000000, 50000000]],k = 110000000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100000000, 100000000], [-90000000, 90000000], [0, -50000000], [100000000, 50000000]],k = 110000000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, -1], [3, -2], [5, -3], [7, -4], [9, -5], [11, -6], [13, -7], [15, -8], [17, -9], [19, -10]],k = 18) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, -1], [3, -2], [5, -3], [7, -4], [9, -5], [11, -6], [13, -7], [15, -8], [17, -9], [19, -10]],k = 18) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 3], [5, 6], [8, 9], [11, 12], [14, 15]],k = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 3], [5, 6], [8, 9], [11, 12], [14, 15]],k = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],k = 1) == -inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],k = 1) == -inf: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],k = 1) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],k = 1) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, -100000000], [2, 100000000], [3, -100000000], [4, 100000000], [5, -100000000], [6, 100000000], [7, -100000000]],k = 2) == 200000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, -100000000], [2, 100000000], [3, -100000000], [4, 100000000], [5, -100000000], [6, 100000000], [7, -100000000]],k = 2) == 200000002: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],k = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],k = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996], [6, 99999995], [7, 99999994], [8, 99999993], [9, 99999992], [10, 99999991]],k = 1) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996], [6, 99999995], [7, 99999994], [8, 99999993], [9, 99999992], [10, 99999991]],k = 1) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 3], [3, 5], [4, 7], [5, 2], [6, 8]],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 3], [3, 5], [4, 7], [5, 2], [6, 8]],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 50], [20, 30], [30, 20], [40, 10], [50, 0], [60, -10], [70, -20], [80, -30], [90, -40]],k = 25) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 50], [20, 30], [30, 20], [40, 10], [50, 0], [60, -10], [70, -20], [80, -30], [90, -40]],k = 25) == 90: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100000000], [2, 90000000], [3, 80000000], [4, 70000000], [5, 60000000]],k = 3) == 190000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100000000], [2, 90000000], [3, 80000000], [4, 70000000], [5, 60000000]],k = 3) == 190000001: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [15, 10], [25, 3], [35, 15], [45, 10], [55, 20], [65, 5], [75, 25]],k = 20) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [15, 10], [25, 3], [35, 15], [45, 10], [55, 20], [65, 5], [75, 25]],k = 20) == 65: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]],k = 30) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]],k = 30) == 180: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 10], [3, 3], [4, 15], [5, 5], [6, 20], [7, 7], [8, 25], [9, 9], [10, 30]],k = 10) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 10], [3, 3], [4, 15], [5, 5], [6, 20], [7, 7], [8, 25], [9, 9], [10, 30]],k = 10) == 57: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23], [25, 25], [27, 27], [29, 29], [31, 31], [33, 33], [35, 35], [37, 37], [39, 39]],k = 2) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23], [25, 25], [27, 27], [29, 29], [31, 31], [33, 33], [35, 35], [37, 37], [39, 39]],k = 2) == 78: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100000000, 100000000], [0, 0], [100000000, -100000000]],k = 200000000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100000000, 100000000], [0, 0], [100000000, -100000000]],k = 200000000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10]],k = 20) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10]],k = 20) == 200: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-2, 3], [-1, 2], [0, 0], [1, 5], [2, 1], [4, -2], [6, 3]],k = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-2, 3], [-1, 2], [0, 0], [1, 5], [2, 1], [4, -2], [6, 3]],k = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 0], [-9, 1], [-8, 2], [-7, 3], [-6, 4], [-5, 5], [-4, 6], [-3, 7], [-2, 8], [-1, 9]],k = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 0], [-9, 1], [-8, 2], [-7, 3], [-6, 4], [-5, 5], [-4, 6], [-3, 7], [-2, 8], [-1, 9]],k = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [15, 10], [20, 20], [25, 30], [30, 5], [35, 25], [40, 30]],k = 10) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [15, 10], [20, 20], [25, 30], [30, 5], [35, 25], [40, 30]],k = 10) == 65: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [3, 4], [6, 7], [8, 2], [10, 10]],k = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [3, 4], [6, 7], [8, 2], [10, 10]],k = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, 10], [0, -1], [4, 3], [7, -2], [12, 5]],k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, 10], [0, -1], [4, 3], [7, -2], [12, 5]],k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100, 100], [-90, -80], [-80, 80], [-70, -70], [-60, 60], [-50, -50]],k = 20) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100, 100], [-90, -80], [-80, 80], [-70, -70], [-60, 60], [-50, -50]],k = 20) == 200: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 10], [2, 5], [3, -5], [4, -10], [5, -15], [6, -20], [7, -25], [8, -30]],k = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 10], [2, 5], [3, -5], [4, -10], [5, -15], [6, -20], [7, -25], [8, -30]],k = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 3], [2, 1], [3, 2], [4, 4], [5, 1], [6, 3], [7, 2], [8, 5], [9, 4]],k = 4) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 3], [2, 1], [3, 2], [4, 4], [5, 1], [6, 3], [7, 2], [8, 5], [9, 4]],k = 4) == 13: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-3, -2], [-1, 0], [2, 3], [5, 5], [8, 8], [11, 11]],k = 7) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-3, -2], [-1, 0], [2, 3], [5, 5], [8, 8], [11, 11]],k = 7) == 22: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 2], [5, 3], [7, 4], [9, 5], [11, 6], [13, 7], [15, 8], [17, 9]],k = 8) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 2], [5, 3], [7, 4], [9, 5], [11, 6], [13, 7], [15, 8], [17, 9]],k = 8) == 22: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [3, 5], [5, 7], [7, 10], [9, 15], [11, 20], [13, 25], [15, 30], [17, 35], [19, 40]],k = 10) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [3, 5], [5, 7], [7, 10], [9, 15], [11, 20], [13, 25], [15, 30], [17, 35], [19, 40]],k = 10) == 77: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-50, 10], [-30, 20], [-10, 30], [10, 40], [30, 50], [50, 60], [70, 70], [90, 80], [110, 90]],k = 30) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-50, 10], [-30, 20], [-10, 30], [10, 40], [30, 50], [50, 60], [70, 70], [90, 80], [110, 90]],k = 30) == 190: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100000000, 100000000], [0, -100000000], [100000000, 100000000]],k = 200000000) == 400000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100000000, 100000000], [0, -100000000], [100000000, 100000000]],k = 200000000) == 400000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],k = 2) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],k = 2) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100000000, 100000000], [-99999999, 99999999], [-99999998, 99999998], [-99999997, 99999997], [-99999996, 99999996], [-99999995, 99999995]],k = 4) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100000000, 100000000], [-99999999, 99999999], [-99999998, 99999998], [-99999997, 99999997], [-99999996, 99999996], [-99999995, 99999995]],k = 4) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100000, 100000], [-90000, 50000], [-80000, 0], [-70000, -50000], [-60000, -100000], [-50000, 100000], [-40000, 50000], [-30000, 0], [-20000, -50000], [-10000, -100000], [0, 100000], [10000, 50000], [20000, 0], [30000, -50000], [40000, -100000], [50000, 100000], [60000, 50000], [70000, 0], [80000, -50000], [90000, -100000], [100000, 100000]],k = 20000) == 160000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100000, 100000], [-90000, 50000], [-80000, 0], [-70000, -50000], [-60000, -100000], [-50000, 100000], [-40000, 50000], [-30000, 0], [-20000, -50000], [-10000, -100000], [0, 100000], [10000, 50000], [20000, 0], [30000, -50000], [40000, -100000], [50000, 100000], [60000, 50000], [70000, 0], [80000, -50000], [90000, -100000], [100000, 100000]],k = 20000) == 160000: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100], [2, 50], [3, 75], [4, 25], [5, 150]],k = 4) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100], [2, 50], [3, 75], [4, 25], [5, 150]],k = 4) == 254: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10]],k = 1) == 4
    assert candidate(points = [[100000000, 100000000], [200000000, 200000000], [300000000, 300000000]],k = 100000000) == 600000000
    assert candidate(points = [[1, 5], [2, 3], [4, 7], [8, 10]],k = 6) == 21
    assert candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10], [7, 5]],k = 4) == 17
    assert candidate(points = [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10]],k = 15) == 20
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4]],k = 2) == 8
    assert candidate(points = [[-1, 1], [-2, 2], [-3, 3]],k = 1) == 4
    assert candidate(points = [[-10, 5], [0, 0], [10, 10], [20, -5]],k = 25) == 35
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]],k = 2) == 10
    assert candidate(points = [[-10, -10], [0, 0], [10, 10]],k = 20) == 20
    assert candidate(points = [[1, 100000000], [100000000, 1]],k = 200000000) == 200000000
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 4) == 10
    assert candidate(points = [[1, 1], [3, 3], [5, 5]],k = 4) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],k = 2) == 10
    assert candidate(points = [[0, 0], [3, 0], [9, 2]],k = 3) == 3
    assert candidate(points = [[-1, 2], [-3, 3], [1, 3], [2, 4]],k = 4) == 10
    assert candidate(points = [[-1, 20], [-10, 15], [-5, 10], [0, 5], [5, 0], [10, -5], [15, -10]],k = 12) == 30
    assert candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996], [6, 99999995]],k = 4) == 200000000
    assert candidate(points = [[1, 1], [2, 100000000], [3, 1], [4, 100000000], [5, 1]],k = 1) == 100000002
    assert candidate(points = [[100000000, 100000000], [200000000, -200000000], [300000000, 300000000]],k = 150000000) == 200000000
    assert candidate(points = [[1, 1], [3, 4], [5, 7], [8, 10], [12, 13], [15, 14], [18, 15], [20, 16], [25, 17], [30, 18]],k = 15) == 47
    assert candidate(points = [[100000000, -100000000], [100000001, 100000000], [100000002, -100000000], [100000003, 100000000]],k = 4) == 200000002
    assert candidate(points = [[1, 3], [4, 1], [8, 5], [15, 10], [20, 6], [25, 3]],k = 15) == 27
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],k = 9) == 11
    assert candidate(points = [[1, 3], [4, 5], [7, 8], [10, 12], [13, 15], [16, 18]],k = 5) == 36
    assert candidate(points = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0], [7, -1], [8, -2], [9, -3], [10, -4]],k = 4) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],k = 2) == 30
    assert candidate(points = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700]],k = 3) == 1301
    assert candidate(points = [[1, 3], [5, 10], [8, 15], [10, 7], [12, 20], [16, 5], [20, 25]],k = 10) == 53
    assert candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10], [11, -11], [12, -12], [13, -13], [14, -14], [15, -15], [16, -16], [17, -17], [18, -18], [19, -19], [20, -20]],k = 5) == -2
    assert candidate(points = [[-1, 1], [0, 0], [1, -1], [2, 2], [3, -3], [4, 4], [5, -5], [6, 6]],k = 2) == 12
    assert candidate(points = [[1, 100], [5, 200], [10, 300], [15, 400], [20, 500], [25, 600], [30, 700]],k = 10) == 1305
    assert candidate(points = [[1, 3], [2, 0], [5, 10], [6, -10], [7, 2], [8, -5], [10, 4]],k = 3) == 14
    assert candidate(points = [[1, 1], [2, 3], [4, 2], [5, 3], [6, 5], [8, 6], [9, 7], [10, 8]],k = 5) == 17
    assert candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10]],k = 5) == -2
    assert candidate(points = [[1, 100000000], [2, -100000000], [3, 100000000], [4, -100000000], [5, 100000000], [6, -100000000], [7, 100000000], [8, -100000000], [9, 100000000], [10, -100000000]],k = 1) == 1
    assert candidate(points = [[1, 1], [3, 5], [5, 3], [7, 9], [9, 4], [11, 10], [13, 6], [15, 8], [17, 2], [19, 12]],k = 4) == 24
    assert candidate(points = [[100000, -100000], [100005, 100000], [100010, -100000], [100015, 100000]],k = 10) == 200010
    assert candidate(points = [[1, 10], [3, 20], [5, 15], [7, 5], [9, 25], [11, 30], [13, 10], [15, 35]],k = 15) == 69
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],k = 1) == 3
    assert candidate(points = [[-5, 10], [-2, 3], [0, 0], [3, -5], [7, 2], [8, -1], [10, 6]],k = 4) == 16
    assert candidate(points = [[1, 1], [3, 4], [6, 7], [8, 10], [11, 13], [15, 16], [18, 19]],k = 7) == 39
    assert candidate(points = [[100000000, -100000000], [200000000, -200000000], [300000000, 100000000], [400000000, 200000000]],k = 250000000) == 400000000
    assert candidate(points = [[-5, -5], [-3, -3], [0, 0], [4, 4], [6, 6], [10, 10]],k = 6) == 20
    assert candidate(points = [[-20, 20], [-18, 18], [-16, 16], [-14, 14], [-12, 12], [-10, 10], [-8, 8], [-6, 6], [-4, 4], [-2, 2]],k = 4) == 40
    assert candidate(points = [[-100000000, -100000000], [-90000000, -90000000], [-80000000, -80000000], [-70000000, -70000000], [-60000000, -60000000], [-50000000, -50000000], [-40000000, -40000000], [-30000000, -30000000], [-20000000, -20000000], [-10000000, -10000000]],k = 20000000) == -20000000
    assert candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996]],k = 1) == 200000000
    assert candidate(points = [[1, 100000000], [2, 50000000], [5, 10000000], [10, 5000000], [20, 1000000], [50, 500000], [100, 100000]],k = 99) == 150000001
    assert candidate(points = [[-5, -10], [-3, -7], [-1, -2], [1, 3], [4, 9]],k = 4) == 15
    assert candidate(points = [[1, 5], [4, 3], [6, 7], [8, 2], [10, 8]],k = 5) == 19
    assert candidate(points = [[1, 5], [3, 4], [7, 10], [8, 2], [10, 1]],k = 5) == 18
    assert candidate(points = [[1, 2], [4, 5], [6, 7], [8, 9], [10, 12], [12, 15], [14, 17], [16, 19], [18, 21], [20, 23]],k = 10) == 46
    assert candidate(points = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],k = 15) == 29
    assert candidate(points = [[1, 100000000], [-50000000, -100000000], [100000000, -100000000], [-100000000, 100000000]],k = 200000000) == 99999999
    assert candidate(points = [[1, 1], [3, 5], [6, 2], [8, 8], [10, 4], [15, 7], [20, 1]],k = 5) == 18
    assert candidate(points = [[1, 100000000], [100000000, 1], [100000001, 2], [200000000, 3], [300000000, 4], [400000000, 5], [500000000, 6], [600000000, 7], [700000000, 8], [800000000, 9], [900000000, 10]],k = 100000000) == 200000002
    assert candidate(points = [[-1000000, -1000000], [-900000, -900000], [-800000, -800000], [-700000, -700000], [-600000, -600000]],k = 100000) == -1200000
    assert candidate(points = [[-5, 5], [0, 0], [1, 3], [3, -1], [5, 10], [6, -10], [8, 2], [10, 3], [15, 0]],k = 5) == 18
    assert candidate(points = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9]],k = 2) == -2
    assert candidate(points = [[1, 1], [10, 10], [100, 100], [1000, 1000], [10000, 10000], [100000, 100000], [1000000, 1000000], [10000000, 10000000], [100000000, 100000000]],k = 50000000) == 20000000
    assert candidate(points = [[100000, -100000], [100001, -99999], [100002, -99998], [100003, -99997], [100004, -99996]],k = 4) == -199992
    assert candidate(points = [[-10, -10], [-9, -9], [-8, -8], [-7, -7], [-6, -6], [-5, -5], [-4, -4], [-3, -3], [-2, -2], [-1, -1]],k = 2) == -2
    assert candidate(points = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],k = 3) == 200
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 3) == 20
    assert candidate(points = [[1, 5], [3, 7], [6, 8], [8, 6], [10, 9], [15, 1]],k = 5) == 21
    assert candidate(points = [[-50, -50], [-25, -100], [0, 0], [25, 100], [50, 50]],k = 75) == 175
    assert candidate(points = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],k = 3) == 1901
    assert candidate(points = [[1, 2], [2, 4], [3, 8], [4, 16], [5, 32]],k = 4) == 49
    assert candidate(points = [[1, 10], [2, 15], [5, 20], [8, 25], [10, 30], [15, 35], [20, 40], [25, 45], [30, 50], [35, 55]],k = 15) == 110
    assert candidate(points = [[-5, -5], [-3, -1], [0, 0], [2, 4], [3, 6], [8, 8]],k = 5) == 19
    assert candidate(points = [[1, 1], [10, 2], [20, 3], [30, 4], [40, 5], [50, 6], [60, 7], [70, 8], [80, 9], [90, 10]],k = 15) == 29
    assert candidate(points = [[-100000000, 100000000], [-90000000, 90000000], [0, -50000000], [100000000, 50000000]],k = 110000000) == 200000000
    assert candidate(points = [[1, -1], [3, -2], [5, -3], [7, -4], [9, -5], [11, -6], [13, -7], [15, -8], [17, -9], [19, -10]],k = 18) == 7
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 1) == 20
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 10) == 20
    assert candidate(points = [[2, 3], [5, 6], [8, 9], [11, 12], [14, 15]],k = 3) == 30
    assert candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],k = 1) == -inf
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],k = 1) == 18
    assert candidate(points = [[1, -100000000], [2, 100000000], [3, -100000000], [4, 100000000], [5, -100000000], [6, 100000000], [7, -100000000]],k = 2) == 200000002
    assert candidate(points = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 6], [6, 5], [7, 8], [8, 7], [9, 10], [10, 9]],k = 1) == 20
    assert candidate(points = [[1, 100000000], [2, 99999999], [3, 99999998], [4, 99999997], [5, 99999996], [6, 99999995], [7, 99999994], [8, 99999993], [9, 99999992], [10, 99999991]],k = 1) == 200000000
    assert candidate(points = [[1, 10], [2, 3], [3, 5], [4, 7], [5, 2], [6, 8]],k = 4) == 20
    assert candidate(points = [[10, 50], [20, 30], [30, 20], [40, 10], [50, 0], [60, -10], [70, -20], [80, -30], [90, -40]],k = 25) == 90
    assert candidate(points = [[1, 100000000], [2, 90000000], [3, 80000000], [4, 70000000], [5, 60000000]],k = 3) == 190000001
    assert candidate(points = [[5, 5], [15, 10], [25, 3], [35, 15], [45, 10], [55, 20], [65, 5], [75, 25]],k = 20) == 65
    assert candidate(points = [[1, 1], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]],k = 30) == 180
    assert candidate(points = [[1, 1], [2, 10], [3, 3], [4, 15], [5, 5], [6, 20], [7, 7], [8, 25], [9, 9], [10, 30]],k = 10) == 57
    assert candidate(points = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23], [25, 25], [27, 27], [29, 29], [31, 31], [33, 33], [35, 35], [37, 37], [39, 39]],k = 2) == 78
    assert candidate(points = [[-100000000, 100000000], [0, 0], [100000000, -100000000]],k = 200000000) == 200000000
    assert candidate(points = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10]],k = 20) == 200
    assert candidate(points = [[-5, -5], [-2, 3], [-1, 2], [0, 0], [1, 5], [2, 1], [4, -2], [6, 3]],k = 4) == 11
    assert candidate(points = [[-10, 0], [-9, 1], [-8, 2], [-7, 3], [-6, 4], [-5, 5], [-4, 6], [-3, 7], [-2, 8], [-1, 9]],k = 3) == 18
    assert candidate(points = [[10, 20], [15, 10], [20, 20], [25, 30], [30, 5], [35, 25], [40, 30]],k = 10) == 65
    assert candidate(points = [[1, 5], [3, 4], [6, 7], [8, 2], [10, 10]],k = 4) == 21
    assert candidate(points = [[-5, 10], [0, -1], [4, 3], [7, -2], [12, 5]],k = 5) == 14
    assert candidate(points = [[-100, 100], [-90, -80], [-80, 80], [-70, -70], [-60, 60], [-50, -50]],k = 20) == 200
    assert candidate(points = [[1, 10], [2, 5], [3, -5], [4, -10], [5, -15], [6, -20], [7, -25], [8, -30]],k = 3) == 16
    assert candidate(points = [[1, 3], [2, 1], [3, 2], [4, 4], [5, 1], [6, 3], [7, 2], [8, 5], [9, 4]],k = 4) == 13
    assert candidate(points = [[-5, -5], [-3, -2], [-1, 0], [2, 3], [5, 5], [8, 8], [11, 11]],k = 7) == 22
    assert candidate(points = [[1, 1], [3, 2], [5, 3], [7, 4], [9, 5], [11, 6], [13, 7], [15, 8], [17, 9]],k = 8) == 22
    assert candidate(points = [[1, 2], [3, 5], [5, 7], [7, 10], [9, 15], [11, 20], [13, 25], [15, 30], [17, 35], [19, 40]],k = 10) == 77
    assert candidate(points = [[-50, 10], [-30, 20], [-10, 30], [10, 40], [30, 50], [50, 60], [70, 70], [90, 80], [110, 90]],k = 30) == 190
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],k = 3) == 20
    assert candidate(points = [[-100000000, 100000000], [0, -100000000], [100000000, 100000000]],k = 200000000) == 400000000
    assert candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],k = 2) == 40
    assert candidate(points = [[-100000000, 100000000], [-99999999, 99999999], [-99999998, 99999998], [-99999997, 99999997], [-99999996, 99999996], [-99999995, 99999995]],k = 4) == 200000000
    assert candidate(points = [[-100000, 100000], [-90000, 50000], [-80000, 0], [-70000, -50000], [-60000, -100000], [-50000, 100000], [-40000, 50000], [-30000, 0], [-20000, -50000], [-10000, -100000], [0, 100000], [10000, 50000], [20000, 0], [30000, -50000], [40000, -100000], [50000, 100000], [60000, 50000], [70000, 0], [80000, -50000], [90000, -100000], [100000, 100000]],k = 20000) == 160000
    assert candidate(points = [[1, 100], [2, 50], [3, 75], [4, 25], [5, 150]],k = 4) == 254


