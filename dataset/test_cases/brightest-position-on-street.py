def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(lights = [[-1, 1], [-2, 2], [-3, 3]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 1], [-2, 2], [-3, 3]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-5, 4], [-2, 3], [0, 2], [2, 1]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-5, 4], [-2, 3], [0, 2], [2, 1]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 50000000], [50000000, 25000000], [-50000000, 30000000]]) == 50000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 50000000], [50000000, 25000000], [-50000000, 30000000]]) == 50000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[5, 3], [10, 2], [15, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[5, 3], [10, 2], [15, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-5, 3], [5, 3], [0, 1], [2, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-5, 3], [5, 3], [0, 1], [2, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-5, 10], [5, 10], [15, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-5, 10], [5, 10], [15, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 0], [0, 0], [1, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 0], [0, 0], [1, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-3, 2], [1, 2], [3, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-3, 2], [1, 2], [3, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [0, 0], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [0, 0], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 0], [0, 1], [1, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 0], [0, 1], [1, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 5], [5, 5], [10, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 5], [5, 5], [10, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[1, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[1, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 5], [0, 5], [10, 5]]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 5], [0, 5], [10, 5]]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[1, 0], [0, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[1, 0], [0, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 5], [10, 5], [0, 0]]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 5], [10, 5], [0, 0]]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 100000000], [-100000000, 100000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 100000000], [-100000000, 100000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [0, 5], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [0, 5], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 0], [1, 0], [-1, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 0], [1, 0], [-1, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[10, 5], [15, 5], [20, 5], [25, 5], [30, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[10, 5], [15, 5], [20, 5], [25, 5], [30, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[10000000, 10000000], [10000001, 10000000]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[10000000, 10000000], [10000001, 10000000]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 0], [0, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 0], [0, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 0], [1, 0], [-1, 0], [2, 0], [-2, 0]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 0], [1, 0], [-1, 0], [2, 0], [-2, 0]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-500000, 100000], [0, 100000], [500000, 100000], [-250000, 50000], [250000, 50000], [150000, 200000]]) == -50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-500000, 100000], [0, 100000], [500000, 100000], [-250000, 50000], [250000, 50000], [150000, 200000]]) == -50000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6], [-6, 7], [-7, 8], [-8, 9], [-9, 10], [-10, 11]]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6], [-6, 7], [-7, 8], [-8, 9], [-9, 10], [-10, 11]]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [-50000000, 50000000], [0, 0], [1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [-50000000, 50000000], [0, 0], [1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50000000, 50000000], [0, 50000000], [50000000, 50000000], [100000000, 50000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50000000, 50000000], [0, 50000000], [50000000, 50000000], [100000000, 50000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-20, 10], [20, 10], [0, 15], [5, 5], [-5, 5], [-15, 10]]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-20, 10], [20, 10], [0, 15], [5, 5], [-5, 5], [-15, 10]]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 1], [0, 2], [10, 3], [20, 4], [30, 5], [40, 6]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 1], [0, 2], [10, 3], [20, 4], [30, 5], [40, 6]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 100000000], [0, 0], [50000000, 100000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 100000000], [0, 0], [50000000, 100000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000, 100000], [0, 0], [100000, 100000], [-50000, 50000], [50000, 50000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000, 100000], [0, 0], [100000, 100000], [-50000, 50000], [50000, 50000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 10], [-90, 20], [-80, 30], [-70, 40], [-60, 50], [-50, 60], [-40, 70], [-30, 80], [-20, 90], [-10, 100]]) == -110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 10], [-90, 20], [-80, 30], [-70, 40], [-60, 50], [-50, 60], [-40, 70], [-30, 80], [-20, 90], [-10, 100]]) == -110: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 100000000], [1, 100000000], [0, 100000000]]) == -99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 100000000], [1, 100000000], [0, 100000000]]) == -99999999: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-2, 3], [-1, 2], [0, 1], [1, 0], [2, 1], [3, 2], [4, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-2, 3], [-1, 2], [0, 1], [1, 0], [2, 1], [3, 2], [4, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 50], [-25, 25], [0, 0], [25, 25], [50, 50]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 50], [-25, 25], [0, 0], [25, 25], [50, 50]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 50000000], [0, 50000000], [100000000, 50000000], [200000000, 50000000], [-200000000, 50000000], [-300000000, 50000000]]) == -250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 50000000], [0, 50000000], [100000000, 50000000], [200000000, 50000000], [-200000000, 50000000], [-300000000, 50000000]]) == -250000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 50], [-50, 50], [0, 50], [50, 50], [100, 50], [150, 50], [200, 50], [250, 50], [300, 50], [350, 50]]) == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 50], [-50, 50], [0, 50], [50, 50], [100, 50], [150, 50], [200, 50], [250, 50], [300, 50], [350, 50]]) == -50: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 100000000], [-100000000, 100000000], [0, 100000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 100000000], [-100000000, 100000000], [0, 100000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 50], [0, 0], [50, 50], [-100, 100], [25, 25]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 50], [0, 0], [50, 50], [-100, 100], [25, 25]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 2], [2, 3], [5, 4], [10, 5], [15, 6], [20, 7], [25, 8], [30, 9]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 2], [2, 3], [5, 4], [10, 5], [15, 6], [20, 7], [25, 8], [30, 9]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 1], [-8, 2], [-6, 3], [-4, 4], [-2, 5], [0, 6], [2, 7], [4, 8], [6, 9], [8, 10]]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 1], [-8, 2], [-6, 3], [-4, 4], [-2, 5], [0, 6], [2, 7], [4, 8], [6, 9], [8, 10]]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [0, 100000000]]) == -100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [0, 100000000]]) == -100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [-5, 5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [-5, 5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 100], [0, 100], [100, 100], [200, 100], [300, 100], [400, 100], [500, 100]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 100], [0, 100], [100, 100], [200, 100], [300, 100], [400, 100], [500, 100]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 99999999], [1, 99999999], [-100000000, 99999999], [100000000, 99999999]]) == -99999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 99999999], [1, 99999999], [-100000000, 99999999], [100000000, 99999999]]) == -99999998: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-500, 250], [-250, 125], [0, 62], [62, 31], [93, 15], [108, 7], [115, 3], [118, 1]]) == -375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-500, 250], [-250, 125], [0, 62], [62, 31], [93, 15], [108, 7], [115, 3], [118, 1]]) == -375: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 0], [100000000, 0], [-99999999, 1], [99999999, 1], [-50000000, 50000000], [50000000, 50000000]]) == -100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 0], [100000000, 0], [-99999999, 1], [99999999, 1], [-50000000, 50000000], [50000000, 50000000]]) == -100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 1], [-9, 2], [-8, 3], [-7, 4], [-6, 5], [-5, 6], [-4, 7], [-3, 8], [-2, 9], [-1, 10], [0, 11], [1, 12], [2, 13], [3, 14], [4, 15], [5, 16], [6, 17], [7, 18], [8, 19], [9, 20]]) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 1], [-9, 2], [-8, 3], [-7, 4], [-6, 5], [-5, 6], [-4, 7], [-3, 8], [-2, 9], [-1, 10], [0, 11], [1, 12], [2, 13], [3, 14], [4, 15], [5, 16], [6, 17], [7, 18], [8, 19], [9, 20]]) == -11: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 50], [0, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350], [300, 400], [350, 450], [400, 500]]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 50], [0, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350], [300, 400], [350, 450], [400, 500]]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000, 50000], [0, 50000], [50000, 50000], [100000, 50000], [150000, 50000], [200000, 50000]]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000, 50000], [0, 50000], [50000, 50000], [100000, 50000], [150000, 50000], [200000, 50000]]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 0], [-8, 0], [-6, 0], [-4, 0], [-2, 0], [0, 0], [2, 0], [4, 0], [6, 0], [8, 0]]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 0], [-8, 0], [-6, 0], [-4, 0], [-2, 0], [0, 0], [2, 0], [4, 0], [6, 0], [8, 0]]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-5, 2], [-4, 1], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 1], [5, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-5, 2], [-4, 1], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 1], [5, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [100000000, 50000000]]) == 50000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [100000000, 50000000]]) == 50000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 100000000], [1, 100000000], [2, 100000000], [3, 100000000], [4, 100000000], [5, 100000000], [6, 100000000], [7, 100000000], [8, 100000000], [9, 100000000]]) == -99999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 100000000], [1, 100000000], [2, 100000000], [3, 100000000], [4, 100000000], [5, 100000000], [6, 100000000], [7, 100000000], [8, 100000000], [9, 100000000]]) == -99999991: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 20], [-5, 15], [0, 10], [5, 5], [10, 0], [15, 5], [20, 10], [25, 15]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 20], [-5, 15], [0, 10], [5, 5], [10, 0], [15, 5], [20, 10], [25, 15]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 50], [-200, 100], [-300, 150], [-400, 200], [-500, 250], [0, 50], [100, 100], [200, 150], [300, 200], [400, 250], [500, 300]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 50], [-200, 100], [-300, 150], [-400, 200], [-500, 250], [0, 50], [100, 100], [200, 150], [300, 200], [400, 250], [500, 300]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-20, 30], [10, 10], [0, 0], [25, 25], [-15, 15], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-20, 30], [10, 10], [0, 0], [25, 25], [-15, 15], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10]]) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10]]) == -20: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 25], [-25, 25], [0, 25], [25, 25], [50, 25], [75, 25], [100, 25], [125, 25], [150, 25], [175, 25]]) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 25], [-25, 25], [0, 25], [25, 25], [50, 25], [75, 25], [100, 25], [125, 25], [150, 25], [175, 25]]) == -25: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1000, 1000], [-500, 500], [-250, 250], [-125, 125], [-62, 62], [-31, 31], [-15, 15], [-7, 7], [-3, 3], [-1, 1]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1000, 1000], [-500, 500], [-250, 250], [-125, 125], [-62, 62], [-31, 31], [-15, 15], [-7, 7], [-3, 3], [-1, 1]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000, 50000], [100000, 50000], [0, 200000], [200000, 50000], [-200000, 50000]]) == -150000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000, 50000], [100000, 50000], [0, 200000], [200000, 50000], [-200000, 50000]]) == -150000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50000000, 49999999], [49999999, 49999999], [0, 99999998], [1, 1], [-1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50000000, 49999999], [49999999, 49999999], [0, 99999998], [1, 1], [-1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10000, 10000], [-9000, 9000], [-8000, 8000], [-7000, 7000], [-6000, 6000], [-5000, 5000], [-4000, 4000], [-3000, 3000], [-2000, 2000], [-1000, 1000]]) == -2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10000, 10000], [-9000, 9000], [-8000, 8000], [-7000, 7000], [-6000, 6000], [-5000, 5000], [-4000, 4000], [-3000, 3000], [-2000, 2000], [-1000, 1000]]) == -2000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 0], [99999999, 1], [99999998, 2], [99999997, 3], [99999996, 4]]) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 0], [99999999, 1], [99999998, 2], [99999997, 3], [99999996, 4]]) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 100], [0, 100], [100, 100], [200, 100], [300, 100]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 100], [0, 100], [100, 100], [200, 100], [300, 100]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6], [-6, 7], [-7, 8], [-8, 9], [-9, 10]]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6], [-6, 7], [-7, 8], [-8, 9], [-9, 10]]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 100000000], [-100000000, 100000000], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 100000000], [-100000000, 100000000], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1000, 1000], [1000, 1000], [0, 2000], [500, 500], [-500, 500]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1000, 1000], [1000, 1000], [0, 2000], [500, 500], [-500, 500]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0]]) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0]]) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 0], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 0], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 100000000], [0, 100000000], [1, 100000000]]) == -99999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 100000000], [0, 100000000], [1, 100000000]]) == -99999999: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[100000000, 0], [-100000000, 0], [50000000, 0], [-50000000, 0]]) == -100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[100000000, 0], [-100000000, 0], [50000000, 0], [-50000000, 0]]) == -100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [0, 100000000]]) == -100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [0, 100000000]]) == -100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-50, 20], [0, 0], [25, 50], [75, 25], [100, 30]]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-50, 20], [0, 0], [25, 50], [75, 25], [100, 30]]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 100000000], [1, 100000000], [-2, 100000000], [2, 100000000]]) == -99999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 100000000], [1, 100000000], [-2, 100000000], [2, 100000000]]) == -99999998: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [0, 99999999]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [0, 99999999]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 50], [0, 200], [100, 30], [200, 10], [300, 5]]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 50], [0, 200], [100, 30], [200, 10], [300, 5]]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [-50000000, 50000000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [-50000000, 50000000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 5], [-9, 4], [-8, 3], [-7, 2], [-6, 1], [-5, 0], [-4, 1], [-3, 2], [-2, 3], [-1, 4]]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 5], [-9, 4], [-8, 3], [-7, 2], [-6, 1], [-5, 0], [-4, 1], [-3, 2], [-2, 3], [-1, 4]]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 10], [100000000, 10], [-90000000, 9], [90000000, 9], [-80000000, 8], [80000000, 8], [-70000000, 7], [70000000, 7], [-60000000, 6], [60000000, 6]]) == -100000010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 10], [100000000, 10], [-90000000, 9], [90000000, 9], [-80000000, 8], [80000000, 8], [-70000000, 7], [70000000, 7], [-60000000, 6], [60000000, 6]]) == -100000010: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000, 100000], [0, 50000], [50000, 50000], [100000, 50000], [150000, 50000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000, 100000], [0, 50000], [50000, 50000], [100000, 50000], [150000, 50000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 1], [10, 1], [0, 2], [1, 3], [-1, 4], [2, 5], [-2, 6], [3, 7], [-3, 8], [4, 9]]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 1], [10, 1], [0, 2], [1, 3], [-1, 4], [2, 5], [-2, 6], [3, 7], [-3, 8], [4, 9]]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100, 100], [0, 50], [50, 50], [-50, 50], [-25, 25], [25, 25]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100, 100], [0, 50], [50, 50], [-50, 50], [-25, 25], [25, 25]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [-5, 5], [0, 0], [5, 5], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [-5, 5], [0, 0], [5, 5], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 5], [0, 3], [10, 2], [5, 4], [-5, 1]]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 5], [0, 3], [10, 2], [5, 4], [-5, 1]]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 10000000], [10000000, 10000000], [20000000, 10000000], [30000000, 10000000], [40000000, 10000000], [50000000, 10000000], [60000000, 10000000], [70000000, 10000000], [80000000, 10000000], [90000000, 10000000]]) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 10000000], [10000000, 10000000], [20000000, 10000000], [30000000, 10000000], [40000000, 10000000], [50000000, 10000000], [60000000, 10000000], [70000000, 10000000], [80000000, 10000000], [90000000, 10000000]]) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[0, 100000000], [100000001, 100000000], [-200000000, 100000000]]) == -100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[0, 100000000], [100000001, 100000000], [-200000000, 100000000]]) == -100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 50000000], [50000000, 50000000]]) == -150000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 50000000], [50000000, 50000000]]) == -150000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 2], [0, 10], [10, 1], [20, 3], [30, 4], [40, 5], [50, 6], [60, 7], [70, 8], [80, 9]]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 2], [0, 10], [10, 1], [20, 3], [30, 4], [40, 5], [50, 6], [60, 7], [70, 8], [80, 9]]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 0], [0, 1], [1, 0], [-2, 2], [2, 2], [-3, 3], [3, 3], [-4, 4], [4, 4], [-5, 5], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 0], [0, 1], [1, 0], [-2, 2], [2, 2], [-3, 3], [3, 3], [-4, 4], [4, 4], [-5, 5], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1000, 1000], [-2000, 2000], [-3000, 3000], [-4000, 4000], [-5000, 5000], [0, 1000], [1000, 2000], [2000, 3000], [3000, 4000], [4000, 5000]]) == -1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1000, 1000], [-2000, 2000], [-3000, 3000], [-4000, 4000], [-5000, 5000], [0, 1000], [1000, 2000], [2000, 3000], [3000, 4000], [4000, 5000]]) == -1000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000000, 0], [-90000000, 0], [-80000000, 0], [-70000000, 0], [-60000000, 0], [-50000000, 0], [-40000000, 0], [-30000000, 0], [-20000000, 0], [-100000000, 0]]) == -100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000000, 0], [-90000000, 0], [-80000000, 0], [-70000000, 0], [-60000000, 0], [-50000000, 0], [-40000000, 0], [-30000000, 0], [-20000000, 0], [-100000000, 0]]) == -100000000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10000, 10000], [0, 5000], [5000, 5000], [10000, 5000], [15000, 5000], [20000, 5000], [25000, 5000], [30000, 5000]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10000, 10000], [0, 5000], [5000, 5000], [10000, 5000], [15000, 5000], [20000, 5000], [25000, 5000], [30000, 5000]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-100000, 100000], [-90000, 90000], [-80000, 80000], [-70000, 70000], [-60000, 60000]]) == -120000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-100000, 100000], [-90000, 90000], [-80000, 80000], [-70000, 70000], [-60000, 60000]]) == -120000: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-20, 15], [-10, 10], [0, 7], [5, 8], [15, 12]]) == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-20, 15], [-10, 10], [0, 7], [5, 8], [15, 12]]) == -7: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[-1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90]]) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[-1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90]]) == -11: {e}')
    
    total += 1
    try:
        result = candidate(lights = [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5], [100, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lights = [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5], [100, 5]]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(lights = [[-1, 1], [-2, 2], [-3, 3]]) == -2
    assert candidate(lights = [[-5, 4], [-2, 3], [0, 2], [2, 1]]) == -2
    assert candidate(lights = [[100000000, 50000000], [50000000, 25000000], [-50000000, 30000000]]) == 50000000
    assert candidate(lights = [[5, 3], [10, 2], [15, 1]]) == 8
    assert candidate(lights = [[-5, 3], [5, 3], [0, 1], [2, 2]]) == 0
    assert candidate(lights = [[-5, 10], [5, 10], [15, 10]]) == 5
    assert candidate(lights = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 8
    assert candidate(lights = [[-1, 0], [0, 0], [1, 0]]) == -1
    assert candidate(lights = [[-3, 2], [1, 2], [3, 3]]) == -1
    assert candidate(lights = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0]]) == 0
    assert candidate(lights = [[-10, 10], [0, 0], [10, 10]]) == 0
    assert candidate(lights = [[-1, 0], [0, 1], [1, 0]]) == -1
    assert candidate(lights = [[0, 5], [5, 5], [10, 5]]) == 5
    assert candidate(lights = [[1, 2]]) == -1
    assert candidate(lights = [[-10, 5], [0, 5], [10, 5]]) == -5
    assert candidate(lights = [[1, 0], [0, 1]]) == 1
    assert candidate(lights = [[-10, 5], [10, 5], [0, 0]]) == -15
    assert candidate(lights = [[100000000, 100000000], [-100000000, 100000000]]) == 0
    assert candidate(lights = [[-10, 10], [0, 5], [5, 5]]) == 0
    assert candidate(lights = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5]]) == -2
    assert candidate(lights = [[0, 0], [1, 0], [-1, 0]]) == -1
    assert candidate(lights = [[10, 5], [15, 5], [20, 5], [25, 5], [30, 5]]) == 15
    assert candidate(lights = [[10000000, 10000000], [10000001, 10000000]]) == 1
    assert candidate(lights = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == 0
    assert candidate(lights = [[0, 0], [0, 0], [0, 0]]) == 0
    assert candidate(lights = [[0, 0], [1, 0], [-1, 0], [2, 0], [-2, 0]]) == -2
    assert candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 0
    assert candidate(lights = [[-500000, 100000], [0, 100000], [500000, 100000], [-250000, 50000], [250000, 50000], [150000, 200000]]) == -50000
    assert candidate(lights = [[-1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6], [-6, 7], [-7, 8], [-8, 9], [-9, 10], [-10, 11]]) == -3
    assert candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [-50000000, 50000000], [0, 0], [1, 1]]) == 0
    assert candidate(lights = [[-50000000, 50000000], [0, 50000000], [50000000, 50000000], [100000000, 50000000]]) == 0
    assert candidate(lights = [[-20, 10], [20, 10], [0, 15], [5, 5], [-5, 5], [-15, 10]]) == -10
    assert candidate(lights = [[-10, 1], [0, 2], [10, 3], [20, 4], [30, 5], [40, 6]]) == 34
    assert candidate(lights = [[-100000000, 100000000], [0, 0], [50000000, 100000000]]) == 0
    assert candidate(lights = [[-100000, 100000], [0, 0], [100000, 100000], [-50000, 50000], [50000, 50000]]) == 0
    assert candidate(lights = [[-100, 10], [-90, 20], [-80, 30], [-70, 40], [-60, 50], [-50, 60], [-40, 70], [-30, 80], [-20, 90], [-10, 100]]) == -110
    assert candidate(lights = [[-1, 100000000], [1, 100000000], [0, 100000000]]) == -99999999
    assert candidate(lights = [[-2, 3], [-1, 2], [0, 1], [1, 0], [2, 1], [3, 2], [4, 3]]) == 1
    assert candidate(lights = [[-50, 50], [-25, 25], [0, 0], [25, 25], [50, 50]]) == 0
    assert candidate(lights = [[-100000000, 50000000], [0, 50000000], [100000000, 50000000], [200000000, 50000000], [-200000000, 50000000], [-300000000, 50000000]]) == -250000000
    assert candidate(lights = [[-100, 50], [-50, 50], [0, 50], [50, 50], [100, 50], [150, 50], [200, 50], [250, 50], [300, 50], [350, 50]]) == -50
    assert candidate(lights = [[100000000, 100000000], [-100000000, 100000000], [0, 100000000]]) == 0
    assert candidate(lights = [[-50, 50], [0, 0], [50, 50], [-100, 100], [25, 25]]) == 0
    assert candidate(lights = [[-1, 2], [2, 3], [5, 4], [10, 5], [15, 6], [20, 7], [25, 8], [30, 9]]) == 21
    assert candidate(lights = [[-10, 1], [-8, 2], [-6, 3], [-4, 4], [-2, 5], [0, 6], [2, 7], [4, 8], [6, 9], [8, 10]]) == -3
    assert candidate(lights = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]]) == 1
    assert candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1]]) == -2
    assert candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [0, 100000000]]) == -100000000
    assert candidate(lights = [[-10, 10], [-5, 5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 0
    assert candidate(lights = [[-100, 100], [0, 100], [100, 100], [200, 100], [300, 100], [400, 100], [500, 100]]) == 0
    assert candidate(lights = [[-1, 99999999], [1, 99999999], [-100000000, 99999999], [100000000, 99999999]]) == -99999998
    assert candidate(lights = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9], [-10, -10]]) == 0
    assert candidate(lights = [[-500, 250], [-250, 125], [0, 62], [62, 31], [93, 15], [108, 7], [115, 3], [118, 1]]) == -375
    assert candidate(lights = [[-100000000, 0], [100000000, 0], [-99999999, 1], [99999999, 1], [-50000000, 50000000], [50000000, 50000000]]) == -100000000
    assert candidate(lights = [[-10, 1], [-9, 2], [-8, 3], [-7, 4], [-6, 5], [-5, 6], [-4, 7], [-3, 8], [-2, 9], [-1, 10], [0, 11], [1, 12], [2, 13], [3, 14], [4, 15], [5, 16], [6, 17], [7, 18], [8, 19], [9, 20]]) == -11
    assert candidate(lights = [[-50, 50], [0, 100], [50, 150], [100, 200], [150, 250], [200, 300], [250, 350], [300, 400], [350, 450], [400, 500]]) == -100
    assert candidate(lights = [[-100000, 50000], [0, 50000], [50000, 50000], [100000, 50000], [150000, 50000], [200000, 50000]]) == 50000
    assert candidate(lights = [[-10, 0], [-8, 0], [-6, 0], [-4, 0], [-2, 0], [0, 0], [2, 0], [4, 0], [6, 0], [8, 0]]) == -10
    assert candidate(lights = [[-5, 2], [-4, 1], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 1], [5, 2]]) == 0
    assert candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [100000000, 50000000]]) == 50000000
    assert candidate(lights = [[-1, 100000000], [1, 100000000], [2, 100000000], [3, 100000000], [4, 100000000], [5, 100000000], [6, 100000000], [7, 100000000], [8, 100000000], [9, 100000000]]) == -99999991
    assert candidate(lights = [[-10, 20], [-5, 15], [0, 10], [5, 5], [10, 0], [15, 5], [20, 10], [25, 15]]) == 10
    assert candidate(lights = [[-100, 50], [-200, 100], [-300, 150], [-400, 200], [-500, 250], [0, 50], [100, 100], [200, 150], [300, 200], [400, 250], [500, 300]]) == 200
    assert candidate(lights = [[-20, 30], [10, 10], [0, 0], [25, 25], [-15, 15], [5, 5]]) == 0
    assert candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10]]) == -20
    assert candidate(lights = [[-50, 25], [-25, 25], [0, 25], [25, 25], [50, 25], [75, 25], [100, 25], [125, 25], [150, 25], [175, 25]]) == -25
    assert candidate(lights = [[-1000, 1000], [-500, 500], [-250, 250], [-125, 125], [-62, 62], [-31, 31], [-15, 15], [-7, 7], [-3, 3], [-1, 1]]) == -2
    assert candidate(lights = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 0
    assert candidate(lights = [[-100000, 50000], [100000, 50000], [0, 200000], [200000, 50000], [-200000, 50000]]) == -150000
    assert candidate(lights = [[-50000000, 49999999], [49999999, 49999999], [0, 99999998], [1, 1], [-1, 1]]) == 0
    assert candidate(lights = [[-10000, 10000], [-9000, 9000], [-8000, 8000], [-7000, 7000], [-6000, 6000], [-5000, 5000], [-4000, 4000], [-3000, 3000], [-2000, 2000], [-1000, 1000]]) == -2000
    assert candidate(lights = [[100000000, 0], [99999999, 1], [99999998, 2], [99999997, 3], [99999996, 4]]) == 100000000
    assert candidate(lights = [[-100, 100], [0, 100], [100, 100], [200, 100], [300, 100]]) == 0
    assert candidate(lights = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 0
    assert candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
    assert candidate(lights = [[-1, 2], [-2, 3], [-3, 4], [-4, 5], [-5, 6], [-6, 7], [-7, 8], [-8, 9], [-9, 10]]) == -3
    assert candidate(lights = [[100000000, 100000000], [-100000000, 100000000], [0, 0]]) == 0
    assert candidate(lights = [[-1000, 1000], [1000, 1000], [0, 2000], [500, 500], [-500, 500]]) == 0
    assert candidate(lights = [[100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0], [100000000, 0]]) == 100000000
    assert candidate(lights = [[-100, 100], [-90, 90], [-80, 80], [-70, 70], [-60, 60], [-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0]]) == 0
    assert candidate(lights = [[-1, 0], [1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4]]) == 4
    assert candidate(lights = [[-1, 100000000], [0, 100000000], [1, 100000000]]) == -99999999
    assert candidate(lights = [[100000000, 0], [-100000000, 0], [50000000, 0], [-50000000, 0]]) == -100000000
    assert candidate(lights = [[-100000000, 50000000], [50000000, 50000000], [0, 100000000]]) == -100000000
    assert candidate(lights = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]) == 1
    assert candidate(lights = [[-50, 20], [0, 0], [25, 50], [75, 25], [100, 30]]) == 70
    assert candidate(lights = [[-1, 100000000], [1, 100000000], [-2, 100000000], [2, 100000000]]) == -99999998
    assert candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [0, 99999999]]) == 0
    assert candidate(lights = [[-10, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == 2
    assert candidate(lights = [[-100, 50], [0, 200], [100, 30], [200, 10], [300, 5]]) == -150
    assert candidate(lights = [[-100000000, 100000000], [50000000, 50000000], [-50000000, 50000000]]) == 0
    assert candidate(lights = [[-10, 5], [-9, 4], [-8, 3], [-7, 2], [-6, 1], [-5, 0], [-4, 1], [-3, 2], [-2, 3], [-1, 4]]) == -5
    assert candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
    assert candidate(lights = [[-100000000, 10], [100000000, 10], [-90000000, 9], [90000000, 9], [-80000000, 8], [80000000, 8], [-70000000, 7], [70000000, 7], [-60000000, 6], [60000000, 6]]) == -100000010
    assert candidate(lights = [[-100000, 100000], [0, 50000], [50000, 50000], [100000, 50000], [150000, 50000]]) == 0
    assert candidate(lights = [[-10, 1], [10, 1], [0, 2], [1, 3], [-1, 4], [2, 5], [-2, 6], [3, 7], [-3, 8], [4, 9]]) == -2
    assert candidate(lights = [[-100, 100], [0, 50], [50, 50], [-50, 50], [-25, 25], [25, 25]]) == 0
    assert candidate(lights = [[-10, 10], [-5, 5], [0, 0], [5, 5], [10, 10]]) == 0
    assert candidate(lights = [[-10, 5], [0, 3], [10, 2], [5, 4], [-5, 1]]) == -6
    assert candidate(lights = [[0, 10000000], [10000000, 10000000], [20000000, 10000000], [30000000, 10000000], [40000000, 10000000], [50000000, 10000000], [60000000, 10000000], [70000000, 10000000], [80000000, 10000000], [90000000, 10000000]]) == 10000000
    assert candidate(lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
    assert candidate(lights = [[0, 100000000], [100000001, 100000000], [-200000000, 100000000]]) == -100000000
    assert candidate(lights = [[-100000000, 50000000], [50000000, 50000000]]) == -150000000
    assert candidate(lights = [[-10, 2], [0, 10], [10, 1], [20, 3], [30, 4], [40, 5], [50, 6], [60, 7], [70, 8], [80, 9]]) == -10
    assert candidate(lights = [[-1, 0], [0, 1], [1, 0], [-2, 2], [2, 2], [-3, 3], [3, 3], [-4, 4], [4, 4], [-5, 5], [5, 5]]) == 0
    assert candidate(lights = [[-1000, 1000], [-2000, 2000], [-3000, 3000], [-4000, 4000], [-5000, 5000], [0, 1000], [1000, 2000], [2000, 3000], [3000, 4000], [4000, 5000]]) == -1000
    assert candidate(lights = [[-100000000, 0], [-90000000, 0], [-80000000, 0], [-70000000, 0], [-60000000, 0], [-50000000, 0], [-40000000, 0], [-30000000, 0], [-20000000, 0], [-100000000, 0]]) == -100000000
    assert candidate(lights = [[-10000, 10000], [0, 5000], [5000, 5000], [10000, 5000], [15000, 5000], [20000, 5000], [25000, 5000], [30000, 5000]]) == 0
    assert candidate(lights = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
    assert candidate(lights = [[-100000, 100000], [-90000, 90000], [-80000, 80000], [-70000, 70000], [-60000, 60000]]) == -120000
    assert candidate(lights = [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
    assert candidate(lights = [[-20, 15], [-10, 10], [0, 7], [5, 8], [15, 12]]) == -7
    assert candidate(lights = [[-1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90]]) == -11
    assert candidate(lights = [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5], [100, 5]]) == 15


